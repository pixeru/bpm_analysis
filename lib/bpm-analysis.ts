import { AnalysisParams, AnalysisResult, AnalysisData, FinalMetrics, PeakType, AnalysisStatus, HRVSummary, HRRStats } from './types';
import { findPeaks, quantile, rollingWindow, smoothData, calculateHRV } from './audio-processing';

export class BPMAnalyzer {
  private params: AnalysisParams;
  private onStatusUpdate?: (status: AnalysisStatus) => void;

  constructor(params: AnalysisParams, onStatusUpdate?: (status: AnalysisStatus) => void) {
    this.params = params;
    this.onStatusUpdate = onStatusUpdate;
  }

  private updateStatus(stage: string, progress: number, message: string) {
    if (this.onStatusUpdate) {
      this.onStatusUpdate({ stage, progress, message });
    }
  }

  public async analyzeAudio(audioEnvelope: number[], sampleRate: number, startBpmHint?: number): Promise<AnalysisResult> {
    this.updateStatus('preprocessing', 10, 'Preprocessing audio data...');
    
    // Apply bandpass filter (simplified)
    const filteredEnvelope = this.applyBandpassFilter(audioEnvelope, sampleRate);
    
    this.updateStatus('noise-analysis', 20, 'Calculating noise floor...');
    
    // Calculate dynamic noise floor and find troughs
    const { noiseFloor, troughIndices } = this.calculateDynamicNoiseFloor(filteredEnvelope, sampleRate);
    
    this.updateStatus('peak-detection', 30, 'Detecting peaks...');
    
    // Find all raw peaks
    const allRawPeaks = this.findRawPeaks(filteredEnvelope, noiseFloor);
    
    this.updateStatus('peak-classification', 50, 'Classifying peaks...');
    
    // Classify peaks using the sophisticated algorithm
    const { finalPeaks, analysisData } = this.classifyPeaks(
      filteredEnvelope,
      allRawPeaks,
      noiseFloor,
      troughIndices,
      sampleRate,
      startBpmHint
    );
    
    this.updateStatus('metrics-calculation', 80, 'Calculating final metrics...');
    
    // Calculate final metrics
    const finalMetrics = this.calculateFinalMetrics(finalPeaks, sampleRate);
    
    this.updateStatus('complete', 100, 'Analysis complete!');
    
    return {
      final_peaks: finalPeaks,
      all_raw_peaks: allRawPeaks,
      analysis_data: analysisData,
      final_metrics: finalMetrics,
      audio_envelope: filteredEnvelope,
      sample_rate: sampleRate
    };
  }

  private applyBandpassFilter(audioEnvelope: number[], sampleRate: number): number[] {
    // Simplified bandpass filter - in production, use proper DSP
    const [lowCut, highCut] = this.params.bandpass_freqs;
    const windowSize = Math.floor(sampleRate / ((lowCut + highCut) / 2));
    
    return smoothData(audioEnvelope, Math.max(1, windowSize));
  }

  private calculateDynamicNoiseFloor(audioEnvelope: number[], sampleRate: number): {
    noiseFloor: number[];
    troughIndices: number[];
  } {
    // Find troughs (local minima)
    const invertedEnvelope = audioEnvelope.map(x => -x);
    const troughCandidates = findPeaks(invertedEnvelope, {
      prominence: quantile(audioEnvelope, this.params.trough_prominence_quantile)
    });
    
    // Calculate noise floor using quantile of troughs
    const windowSamples = Math.floor(this.params.noise_window_sec * sampleRate);
    const noiseFloor = rollingWindow(audioEnvelope, windowSamples, (window) => 
      quantile(window, this.params.noise_floor_quantile)
    );
    
    return {
      noiseFloor,
      troughIndices: troughCandidates
    };
  }

  private findRawPeaks(audioEnvelope: number[], noiseFloor: number[]): number[] {
    const prominence = quantile(audioEnvelope, this.params.peak_prominence_quantile);
    const minDistance = Math.floor(this.params.min_peak_distance_sec * audioEnvelope.length / (audioEnvelope.length / 60)); // Approximate sample rate conversion
    
    return findPeaks(audioEnvelope, {
      height: noiseFloor,
      prominence,
      distance: minDistance
    });
  }

  private classifyPeaks(
    audioEnvelope: number[],
    allRawPeaks: number[],
    noiseFloor: number[],
    troughIndices: number[],
    sampleRate: number,
    startBpmHint?: number
  ): { finalPeaks: number[]; analysisData: AnalysisData } {
    const candidateBeats: number[] = [];
    const beatDebugInfo: Record<number, string> = {};
    let longTermBpm = startBpmHint || 80.0;
    let consecutiveRrRejections = 0;
    
    // Calculate deviation series for amplitude-based confidence
    const deviationSeries = this.calculateDeviationSeries(audioEnvelope, allRawPeaks, noiseFloor);
    
    let loopIdx = 0;
    while (loopIdx < allRawPeaks.length) {
      const currentPeakIdx = allRawPeaks[loopIdx];
      const isLastPeak = loopIdx >= allRawPeaks.length - 1;
      
      if (isLastPeak) {
        // Handle last peak
        candidateBeats.push(currentPeakIdx);
        beatDebugInfo[currentPeakIdx] = PeakType.LONE_S1_LAST;
        loopIdx++;
      } else {
        // Process peak pair
        const nextPeakIdx = allRawPeaks[loopIdx + 1];
        const pairingRatio = this.calculatePairingRatio(candidateBeats, beatDebugInfo);
        
        const { isPaired, reason } = this.attemptS1S2Pairing(
          currentPeakIdx,
          nextPeakIdx,
          audioEnvelope,
          noiseFloor,
          deviationSeries,
          longTermBpm,
          pairingRatio,
          sampleRate
        );
        
        if (isPaired) {
          candidateBeats.push(currentPeakIdx);
          beatDebugInfo[currentPeakIdx] = `${PeakType.S1_PAIRED}§${reason}`;
          beatDebugInfo[nextPeakIdx] = `${PeakType.S2_PAIRED}§${reason}`;
          consecutiveRrRejections = 0;
          loopIdx += 2;
        } else {
          // Classify as lone peak or noise
          const { isValid, rejectionReason } = this.validateLoneS1(
            currentPeakIdx,
            candidateBeats,
            audioEnvelope,
            noiseFloor,
            longTermBpm,
            sampleRate
          );
          
          if (isValid) {
            candidateBeats.push(currentPeakIdx);
            beatDebugInfo[currentPeakIdx] = `${PeakType.LONE_S1_VALIDATED}§${rejectionReason}`;
            consecutiveRrRejections = 0;
          } else {
            // Check for cascade reset
            if (consecutiveRrRejections >= 3) {
              candidateBeats.push(currentPeakIdx);
              beatDebugInfo[currentPeakIdx] = `${PeakType.LONE_S1_CASCADE}§${rejectionReason}`;
              consecutiveRrRejections = 0;
            } else {
              beatDebugInfo[currentPeakIdx] = `${PeakType.NOISE}§${rejectionReason}`;
              consecutiveRrRejections++;
            }
          }
          loopIdx++;
        }
      }
      
      // Update long-term BPM belief
      if (candidateBeats.length > 1) {
        const newRr = (candidateBeats[candidateBeats.length - 1] - candidateBeats[candidateBeats.length - 2]) / sampleRate;
        if (newRr > 0) {
          longTermBpm = this.updateLongTermBpm(newRr, longTermBpm);
        }
      }
    }
    
    return {
      finalPeaks: candidateBeats,
      analysisData: {
        dynamic_noise_floor_series: noiseFloor,
        trough_indices: troughIndices,
        deviation_series: deviationSeries,
        beat_debug_info: beatDebugInfo
      }
    };
  }

  private calculateDeviationSeries(audioEnvelope: number[], allRawPeaks: number[], noiseFloor: number[]): number[] {
    const peakStrengths = allRawPeaks.map(peakIdx => {
      const noiseAtPeak = noiseFloor[peakIdx] || 0;
      return Math.max(0, audioEnvelope[peakIdx] - noiseAtPeak);
    });
    
    const deviations: number[] = [];
    for (let i = 1; i < peakStrengths.length; i++) {
      const deviation = Math.abs(peakStrengths[i] - peakStrengths[i - 1]) / 
        (Math.max(peakStrengths[i], peakStrengths[i - 1]) + 1e-9);
      deviations.push(deviation);
    }
    
    // Smooth the deviation series
    const smoothingWindow = Math.max(5, Math.floor(deviations.length * this.params.deviation_smoothing_factor));
    return smoothData(deviations, smoothingWindow);
  }

  private calculatePairingRatio(candidateBeats: number[], beatDebugInfo: Record<number, string>): number {
    const historyWindow = this.params.stability_history_window;
    if (candidateBeats.length < historyWindow) return 0.5;
    
    const recentBeats = candidateBeats.slice(-historyWindow);
    const pairedCount = recentBeats.filter(beatIdx => 
      beatDebugInfo[beatIdx]?.includes(PeakType.S1_PAIRED)
    ).length;
    
    return pairedCount / historyWindow;
  }

  private attemptS1S2Pairing(
    s1CandidateIdx: number,
    s2CandidateIdx: number,
    audioEnvelope: number[],
    noiseFloor: number[],
    deviationSeries: number[],
    longTermBpm: number,
    pairingRatio: number,
    sampleRate: number
  ): { isPaired: boolean; reason: string } {
    const intervalSec = (s2CandidateIdx - s1CandidateIdx) / sampleRate;
    
    // Check minimum distance
    if (intervalSec < this.params.min_peak_distance_sec) {
      return {
        isPaired: false,
        reason: `Interval too short: ${intervalSec.toFixed(3)}s < ${this.params.min_peak_distance_sec}s`
      };
    }
    
    // Calculate base confidence using blended model
    const deviationValue = deviationSeries[Math.floor(s1CandidateIdx / 100)] || 0;
    let confidence = this.calculateBlendedConfidence(deviationValue, longTermBpm);
    
    // Adjust confidence based on stability and amplitude ratios
    confidence = this.adjustConfidenceWithStability(
      confidence,
      s1CandidateIdx,
      s2CandidateIdx,
      audioEnvelope,
      noiseFloor,
      longTermBpm,
      pairingRatio
    );
    
    // Apply interval penalty
    const maxInterval = Math.min(
      this.params.s1_s2_interval_cap_sec,
      (60.0 / longTermBpm) * this.params.s1_s2_interval_rr_fraction
    );
    
    if (intervalSec > maxInterval * this.params.interval_penalty_start_factor) {
      const penaltyFactor = Math.min(1, (intervalSec - maxInterval) / (maxInterval * 0.4));
      confidence -= penaltyFactor * this.params.interval_max_penalty;
    }
    
    const isPaired = confidence >= this.params.pairing_confidence_threshold;
    const reason = `Confidence: ${confidence.toFixed(3)}, Threshold: ${this.params.pairing_confidence_threshold}`;
    
    return { isPaired, reason };
  }

  private calculateBlendedConfidence(deviation: number, bpm: number): number {
    // Interpolate between low and high BPM confidence curves
    const blendRatio = Math.max(0, Math.min(1, 
      (bpm - this.params.contractility_bpm_low) / 
      (this.params.contractility_bpm_high - this.params.contractility_bpm_low)
    ));
    
    // Find confidence value for deviation using interpolation
    const lowBpmConfidence = this.interpolateConfidence(deviation, this.params.confidence_curve_low_bpm);
    const highBpmConfidence = this.interpolateConfidence(deviation, this.params.confidence_curve_high_bpm);
    
    return lowBpmConfidence * (1 - blendRatio) + highBpmConfidence * blendRatio;
  }

  private interpolateConfidence(deviation: number, confidenceCurve: number[]): number {
    const points = this.params.confidence_deviation_points;
    
    for (let i = 0; i < points.length - 1; i++) {
      if (deviation >= points[i] && deviation <= points[i + 1]) {
        const ratio = (deviation - points[i]) / (points[i + 1] - points[i]);
        return confidenceCurve[i] * (1 - ratio) + confidenceCurve[i + 1] * ratio;
      }
    }
    
    // Handle edge cases
    if (deviation <= points[0]) return confidenceCurve[0];
    return confidenceCurve[confidenceCurve.length - 1];
  }

  private adjustConfidenceWithStability(
    confidence: number,
    s1Idx: number,
    s2Idx: number,
    audioEnvelope: number[],
    noiseFloor: number[],
    longTermBpm: number,
    pairingRatio: number
  ): number {
    // Get peak strengths
    const s1Strength = audioEnvelope[s1Idx] - (noiseFloor[s1Idx] || 0);
    const s2Strength = audioEnvelope[s2Idx] - (noiseFloor[s2Idx] || 0);
    
    // Apply stability-based adjustments
    const stabilityMultiplier = this.params.stability_confidence_floor + 
      (this.params.stability_confidence_ceiling - this.params.stability_confidence_floor) * pairingRatio;
    
    confidence *= stabilityMultiplier;
    
    // Apply amplitude ratio penalties/boosts
    if (s1Strength > s2Strength * this.params.s1_s2_boost_ratio) {
      confidence += this.params.boost_amount_min + 
        (this.params.boost_amount_max - this.params.boost_amount_min) * pairingRatio;
    } else if (s2Strength > s1Strength * this.params.s2_s1_ratio_high_bpm) {
      confidence -= this.params.penalty_amount_min + 
        (this.params.penalty_amount_max - this.params.penalty_amount_min) * (1 - pairingRatio);
    }
    
    return Math.max(0, confidence);
  }

  private validateLoneS1(
    currentPeakIdx: number,
    candidateBeats: number[],
    audioEnvelope: number[],
    noiseFloor: number[],
    longTermBpm: number,
    sampleRate: number
  ): { isValid: boolean; rejectionReason: string } {
    if (candidateBeats.length === 0) {
      return { isValid: true, rejectionReason: "First beat" };
    }
    
    const lastBeatIdx = candidateBeats[candidateBeats.length - 1];
    const rrInterval = (currentPeakIdx - lastBeatIdx) / sampleRate;
    const expectedRr = 60.0 / longTermBpm;
    
    // Check rhythm fit
    const rrDeviation = Math.abs(rrInterval - expectedRr) / expectedRr;
    const rhythmConfidence = this.interpolateArray(
      rrDeviation,
      this.params.lone_s1_rhythm_deviation_points,
      this.params.lone_s1_rhythm_confidence_curve
    );
    
    // Check amplitude consistency
    const currentStrength = audioEnvelope[currentPeakIdx] - (noiseFloor[currentPeakIdx] || 0);
    const lastStrength = audioEnvelope[lastBeatIdx] - (noiseFloor[lastBeatIdx] || 0);
    const strengthRatio = currentStrength / (lastStrength + 1e-9);
    
    const amplitudeConfidence = this.interpolateArray(
      strengthRatio,
      this.params.lone_s1_amplitude_ratio_points,
      this.params.lone_s1_amplitude_confidence_curve
    );
    
    // Combine confidences
    const finalConfidence = 
      rhythmConfidence * this.params.lone_s1_rhythm_weight +
      amplitudeConfidence * this.params.lone_s1_amplitude_weight;
    
    const isValid = finalConfidence >= this.params.lone_s1_confidence_threshold;
    const rejectionReason = `Rhythm: ${rhythmConfidence.toFixed(2)}, Amplitude: ${amplitudeConfidence.toFixed(2)}, Final: ${finalConfidence.toFixed(2)}`;
    
    return { isValid, rejectionReason };
  }

  private interpolateArray(value: number, xPoints: number[], yPoints: number[]): number {
    for (let i = 0; i < xPoints.length - 1; i++) {
      if (value >= xPoints[i] && value <= xPoints[i + 1]) {
        const ratio = (value - xPoints[i]) / (xPoints[i + 1] - xPoints[i]);
        return yPoints[i] * (1 - ratio) + yPoints[i + 1] * ratio;
      }
    }
    
    if (value <= xPoints[0]) return yPoints[0];
    return yPoints[yPoints.length - 1];
  }

  private updateLongTermBpm(newRrSec: number, currentLongTermBpm: number): number {
    const newBpm = 60.0 / newRrSec;
    const clampedBpm = Math.max(this.params.min_bpm, Math.min(this.params.max_bpm, newBpm));
    
    const maxChange = this.params.max_bpm_change_per_beat;
    const limitedBpm = Math.max(
      currentLongTermBpm - maxChange,
      Math.min(currentLongTermBpm + maxChange, clampedBpm)
    );
    
    return currentLongTermBpm + this.params.long_term_bpm_learning_rate * (limitedBpm - currentLongTermBpm);
  }

  private calculateFinalMetrics(finalPeaks: number[], sampleRate: number): FinalMetrics {
    if (finalPeaks.length < 2) {
      // Return default metrics for insufficient data
      return {
        smoothed_bpm: [],
        bpm_times: [],
        hrv_summary: {
          mean_rr: 0,
          rmssd: 0,
          pnn50: 0,
          triangular_index: 0,
          sample_entropy: 0
        },
        hrr_stats: {
          peak_bpm: 0,
          peak_time: 0,
          recovery_rate_1min: 0,
          recovery_rate_2min: 0,
          recovery_percentage_1min: 0,
          recovery_percentage_2min: 0
        }
      };
    }
    
    // Calculate RR intervals and BPM series
    const rrIntervals: number[] = [];
    const bpmValues: number[] = [];
    const bpmTimes: number[] = [];
    
    for (let i = 1; i < finalPeaks.length; i++) {
      const rrInterval = (finalPeaks[i] - finalPeaks[i - 1]) / sampleRate;
      const bpm = 60.0 / rrInterval;
      
      rrIntervals.push(rrInterval);
      bpmValues.push(bpm);
      bpmTimes.push(finalPeaks[i] / sampleRate);
    }
    
    // Smooth BPM series
    const smoothingWindow = Math.max(1, Math.floor(this.params.output_smoothing_window_sec * bpmValues.length / (bpmTimes[bpmTimes.length - 1] || 1)));
    const smoothedBpm = smoothData(bpmValues, smoothingWindow);
    
    // Calculate HRV
    const hrvSummary = calculateHRV(rrIntervals);
    
    // Calculate HRR stats
    const maxBpm = Math.max(...smoothedBpm);
    const maxBpmIndex = smoothedBpm.indexOf(maxBpm);
    const peakTime = bpmTimes[maxBpmIndex] || 0;
    
    // Find recovery rates (simplified)
    let recovery1min = 0;
    let recovery2min = 0;
    let recoveryPct1min = 0;
    let recoveryPct2min = 0;
    
    for (let i = maxBpmIndex; i < bpmTimes.length; i++) {
      const timeFromPeak = bpmTimes[i] - peakTime;
      
      if (timeFromPeak >= 60 && recovery1min === 0) {
        recovery1min = maxBpm - smoothedBpm[i];
        recoveryPct1min = (recovery1min / maxBpm) * 100;
      }
      
      if (timeFromPeak >= 120 && recovery2min === 0) {
        recovery2min = maxBpm - smoothedBpm[i];
        recoveryPct2min = (recovery2min / maxBpm) * 100;
        break;
      }
    }
    
    const hrrStats: HRRStats = {
      peak_bpm: maxBpm,
      peak_time: peakTime,
      recovery_rate_1min: recovery1min,
      recovery_rate_2min: recovery2min,
      recovery_percentage_1min: recoveryPct1min,
      recovery_percentage_2min: recoveryPct2min
    };
    
    return {
      smoothed_bpm: smoothedBpm,
      bpm_times: bpmTimes,
      hrv_summary: hrvSummary,
      hrr_stats: hrrStats
    };
  }
}