import { AudioProcessor, AudioAnalysisParams, DEFAULT_PARAMS, MathUtils } from './audioUtils';

export interface AnalysisResult {
  bpm: number;
  confidence: number;
  audioFile: string;
  s1Peaks: number[];
  s2Peaks: number[];
  noisePeaks: number[];
  audioEnvelope: Float32Array;
  sampleRate: number;
  timeAxis: number[];
  noiseFloor: Float32Array;
  bpmSeries: { time: number; bpm: number }[];
  hrvMetrics?: {
    avgBpm: number;
    minBpm: number;
    maxBpm: number;
    rmssd: number;
    sdnn: number;
  };
}

enum PeakType {
  S1_PAIRED = "S1 (Paired)",
  S2_PAIRED = "S2 (Paired)",
  LONE_S1_VALIDATED = "Lone S1 (Validated)",
  NOISE = "Noise/Rejected"
}

export class BpmAnalyzer {
  private params: AudioAnalysisParams;
  private audioProcessor: AudioProcessor;

  constructor(params: Partial<AudioAnalysisParams> = {}) {
    this.params = { ...DEFAULT_PARAMS, ...params };
    this.audioProcessor = new AudioProcessor();
  }

  async analyze(file: File): Promise<AnalysisResult> {
    console.log('Starting BPM analysis...');
    
    // Step 1: Process audio file
    const { audioData, sampleRate, duration } = await this.audioProcessor.processAudioFile(file);
    console.log(`Processed audio: ${duration.toFixed(2)}s at ${sampleRate}Hz`);

    // Update sample rate in params
    this.params.sampleRate = sampleRate;

    // Step 2: Downsample if needed for performance
    const downsampleFactor = Math.max(1, Math.floor(sampleRate / 4000)); // Target ~4kHz
    const processedAudio = this.audioProcessor.downsample(audioData, downsampleFactor);
    const processedSampleRate = sampleRate / downsampleFactor;
    this.params.sampleRate = processedSampleRate;

    console.log(`Downsampled to ${processedSampleRate}Hz (factor: ${downsampleFactor})`);

    // Step 3: Apply bandpass filter
    const filteredAudio = this.audioProcessor.bandpassFilter(
      processedAudio,
      processedSampleRate,
      this.params.bandpassFreqs[0],
      this.params.bandpassFreqs[1]
    );

    // Step 4: Calculate envelope
    const audioEnvelope = this.audioProcessor.calculateEnvelope(filteredAudio, processedSampleRate);
    console.log('Calculated audio envelope');

    // Step 5: Calculate dynamic noise floor
    const noiseFloor = this.calculateDynamicNoiseFloor(audioEnvelope, processedSampleRate);
    console.log('Calculated noise floor');

    // Step 6: Find and classify peaks
    const { s1Peaks, s2Peaks, noisePeaks } = this.classifyPeaks(audioEnvelope, noiseFloor, processedSampleRate);
    console.log(`Found peaks - S1: ${s1Peaks.length}, S2: ${s2Peaks.length}, Noise: ${noisePeaks.length}`);

    // Step 7: Calculate BPM and metrics
    const bpmResult = this.calculateBpmMetrics(s1Peaks, processedSampleRate);
    console.log(`Average BPM: ${bpmResult.avgBpm.toFixed(1)}`);

    // Step 8: Create time axis
    const timeAxis = Array.from({ length: audioEnvelope.length }, (_, i) => i / processedSampleRate);

    return {
      bpm: Math.round(bpmResult.avgBpm),
      confidence: this.calculateOverallConfidence(s1Peaks, s2Peaks, noisePeaks),
      audioFile: file.name,
      s1Peaks,
      s2Peaks,
      noisePeaks,
      audioEnvelope,
      sampleRate: processedSampleRate,
      timeAxis,
      noiseFloor,
      bpmSeries: bpmResult.bpmSeries,
      hrvMetrics: bpmResult.hrvMetrics,
    };
  }

  private calculateDynamicNoiseFloor(envelope: Float32Array, sampleRate: number): Float32Array {
    // Find troughs (inverted peaks)
    const invertedEnvelope = envelope.map(x => -x);
    const minDistance = Math.floor(this.params.minPeakDistanceSec * sampleRate);
    const troughIndices = MathUtils.findPeaks(new Float32Array(invertedEnvelope), minDistance);

    // Extract trough values
    const troughValues = troughIndices.map(i => envelope[i]);
    
    // Calculate noise floor using moving quantile
    const windowSamples = Math.floor(this.params.outputSmoothingWindowSec * sampleRate);
    const noiseFloor = new Float32Array(envelope.length);
    
    for (let i = 0; i < envelope.length; i++) {
      // Find nearby troughs
      const nearbyTroughs = troughIndices
        .filter(ti => Math.abs(ti - i) <= windowSamples)
        .map(ti => envelope[ti]);
      
      if (nearbyTroughs.length > 0) {
        // Use quantile of nearby troughs
        noiseFloor[i] = MathUtils.calculateQuantile(
          new Float32Array(nearbyTroughs),
          this.params.noiseFloorQuantile
        );
      } else {
        // Fallback to overall quantile
        noiseFloor[i] = MathUtils.calculateQuantile(envelope, this.params.noiseFloorQuantile);
      }
    }

    return MathUtils.movingAverage(noiseFloor, windowSamples);
  }

  private classifyPeaks(envelope: Float32Array, noiseFloor: Float32Array, sampleRate: number): {
    s1Peaks: number[];
    s2Peaks: number[];
    noisePeaks: number[];
  } {
    // Find all potential peaks
    const minDistance = Math.floor(this.params.minPeakDistanceSec * sampleRate);
    const allPeaks = MathUtils.findPeaks(envelope, minDistance, noiseFloor);

    const s1Peaks: number[] = [];
    const s2Peaks: number[] = [];
    const noisePeaks: number[] = [];

    let longTermBpm = 80; // Initial BPM estimate
    let i = 0;

    while (i < allPeaks.length) {
      const currentPeak = allPeaks[i];
      
      // Check if we can pair with next peak
      if (i < allPeaks.length - 1) {
        const nextPeak = allPeaks[i + 1];
        const interval = (nextPeak - currentPeak) / sampleRate;
        const maxInterval = Math.min(this.params.s1S2IntervalCapSec, (60 / longTermBpm) * 0.7);

        // Attempt S1-S2 pairing
        if (interval >= this.params.minPeakDistanceSec && interval <= maxInterval) {
          const confidence = this.calculatePairingConfidence(
            currentPeak, nextPeak, envelope, noiseFloor, longTermBpm
          );

          if (confidence >= this.params.pairingConfidenceThreshold) {
            // Accept as S1-S2 pair
            s1Peaks.push(currentPeak);
            s2Peaks.push(nextPeak);
            
            // Update long-term BPM
            if (s1Peaks.length > 1) {
              const rrInterval = (currentPeak - s1Peaks[s1Peaks.length - 2]) / sampleRate;
              const instantBpm = 60 / rrInterval;
              longTermBpm = this.updateLongTermBpm(instantBpm, longTermBpm);
            }
            
            i += 2; // Skip both peaks
            continue;
          }
        }
      }

      // Check if current peak is a valid lone S1
      if (this.validateLoneS1(currentPeak, s1Peaks, envelope, noiseFloor, sampleRate, longTermBpm)) {
        s1Peaks.push(currentPeak);
        
        // Update long-term BPM
        if (s1Peaks.length > 1) {
          const rrInterval = (currentPeak - s1Peaks[s1Peaks.length - 2]) / sampleRate;
          const instantBpm = 60 / rrInterval;
          longTermBpm = this.updateLongTermBpm(instantBpm, longTermBpm);
        }
      } else {
        // Classify as noise
        noisePeaks.push(currentPeak);
      }
      
      i += 1;
    }

    return { s1Peaks, s2Peaks, noisePeaks };
  }

  private calculatePairingConfidence(
    s1Idx: number,
    s2Idx: number,
    envelope: Float32Array,
    noiseFloor: Float32Array,
    longTermBpm: number
  ): number {
    // Base confidence from amplitude ratio
    const s1Strength = envelope[s1Idx] - noiseFloor[s1Idx];
    const s2Strength = envelope[s2Idx] - noiseFloor[s2Idx];
    const s2S1Ratio = s2Strength / (s1Strength + 1e-9);

    // Physiological expectation: S1 should generally be stronger than S2
    let confidence = s1Strength > s2Strength ? 0.8 : 0.4;

    // Adjust based on S2/S1 ratio (penalize if S2 is much stronger)
    const maxExpectedRatio = longTermBpm > 120 ? 1.1 : 1.5;
    if (s2S1Ratio > maxExpectedRatio) {
      confidence -= 0.3 * Math.min(1, (s2S1Ratio - maxExpectedRatio) / maxExpectedRatio);
    }

    // Boost if S1 is significantly stronger
    if (s1Strength > s2Strength * 1.2) {
      confidence += 0.2;
    }

    // Ensure confidence is in valid range
    return Math.max(0, Math.min(1, confidence));
  }

  private validateLoneS1(
    peakIdx: number,
    existingS1Peaks: number[],
    envelope: Float32Array,
    noiseFloor: Float32Array,
    sampleRate: number,
    longTermBpm: number
  ): boolean {
    if (existingS1Peaks.length === 0) return true; // First peak is always valid

    // Check rhythm consistency
    const lastS1 = existingS1Peaks[existingS1Peaks.length - 1];
    const interval = (peakIdx - lastS1) / sampleRate;
    const expectedInterval = 60 / longTermBpm;
    const rhythmDeviation = Math.abs(interval - expectedInterval) / expectedInterval;

    // Reject if rhythm deviation is too large
    if (rhythmDeviation > 0.5) return false;

    // Check amplitude consistency
    const currentStrength = envelope[peakIdx] - noiseFloor[peakIdx];
    const lastStrength = envelope[lastS1] - noiseFloor[lastS1];
    const strengthRatio = currentStrength / (lastStrength + 1e-9);

    // Reject if amplitude is too different
    if (strengthRatio < 0.3 || strengthRatio > 3.0) return false;

    return true;
  }

  private updateLongTermBpm(instantBpm: number, currentBpm: number): number {
    // Exponential moving average with constraints
    const learningRate = this.params.longTermBpmLearningRate;
    const targetBpm = (1 - learningRate) * currentBpm + learningRate * instantBpm;
    
    // Apply rate limiting
    const maxChange = 3.0; // Max BPM change per beat
    const change = Math.max(-maxChange, Math.min(maxChange, targetBpm - currentBpm));
    const newBpm = currentBpm + change;

    // Apply absolute limits
    return Math.max(this.params.minBpm, Math.min(this.params.maxBpm, newBpm));
  }

  private calculateBpmMetrics(s1Peaks: number[], sampleRate: number): {
    avgBpm: number;
    bpmSeries: { time: number; bpm: number }[];
    hrvMetrics?: {
      avgBpm: number;
      minBpm: number;
      maxBpm: number;
      rmssd: number;
      sdnn: number;
    };
  } {
    if (s1Peaks.length < 2) {
      return {
        avgBpm: 0,
        bpmSeries: [],
      };
    }

    // Calculate instantaneous BPM series
    const bpmSeries: { time: number; bpm: number }[] = [];
    const rrIntervals: number[] = [];

    for (let i = 1; i < s1Peaks.length; i++) {
      const rrInterval = (s1Peaks[i] - s1Peaks[i - 1]) / sampleRate;
      const instantBpm = 60 / rrInterval;
      const time = s1Peaks[i] / sampleRate;

      bpmSeries.push({ time, bpm: instantBpm });
      rrIntervals.push(rrInterval * 1000); // Convert to milliseconds for HRV
    }

    // Calculate average BPM
    const avgBpm = bpmSeries.reduce((sum, point) => sum + point.bpm, 0) / bpmSeries.length;

    // Calculate HRV metrics if we have enough data
    let hrvMetrics;
    if (rrIntervals.length >= 10) {
      const minBpm = Math.min(...bpmSeries.map(p => p.bpm));
      const maxBpm = Math.max(...bpmSeries.map(p => p.bpm));

      // SDNN: Standard deviation of NN intervals
      const meanRR = rrIntervals.reduce((sum, rr) => sum + rr, 0) / rrIntervals.length;
      const sdnn = Math.sqrt(
        rrIntervals.reduce((sum, rr) => sum + Math.pow(rr - meanRR, 2), 0) / rrIntervals.length
      );

      // RMSSD: Root mean square of successive differences
      const successiveDiffs = [];
      for (let i = 1; i < rrIntervals.length; i++) {
        successiveDiffs.push(Math.pow(rrIntervals[i] - rrIntervals[i - 1], 2));
      }
      const rmssd = Math.sqrt(successiveDiffs.reduce((sum, diff) => sum + diff, 0) / successiveDiffs.length);

      hrvMetrics = {
        avgBpm,
        minBpm,
        maxBpm,
        rmssd,
        sdnn,
      };
    }

    return { avgBpm, bpmSeries, hrvMetrics };
  }

  private calculateOverallConfidence(s1Peaks: number[], s2Peaks: number[], noisePeaks: number[]): number {
    const totalPeaks = s1Peaks.length + s2Peaks.length + noisePeaks.length;
    if (totalPeaks === 0) return 0;

    // Higher confidence if more peaks are classified as heartbeats vs noise
    const heartbeatPeaks = s1Peaks.length + s2Peaks.length;
    const heartbeatRatio = heartbeatPeaks / totalPeaks;

    // Higher confidence if we have good S1-S2 pairing
    const pairingRatio = s2Peaks.length / Math.max(1, s1Peaks.length);
    const pairingScore = Math.min(1, pairingRatio); // Ideal ratio is close to 1

    // Combine factors
    const confidence = (heartbeatRatio * 0.6) + (pairingScore * 0.4);
    return Math.min(1, Math.max(0, confidence));
  }
}