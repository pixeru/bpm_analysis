export interface AudioAnalysisParams {
  sampleRate: number;
  bandpassFreqs: [number, number];
  minPeakDistanceSec: number;
  peakProminenceQuantile: number;
  noiseFloorQuantile: number;
  pairingConfidenceThreshold: number;
  s1S2IntervalCapSec: number;
  longTermBpmLearningRate: number;
  minBpm: number;
  maxBpm: number;
  outputSmoothingWindowSec: number;
}

export const DEFAULT_PARAMS: AudioAnalysisParams = {
  sampleRate: 8000, // Will be adjusted based on input
  bandpassFreqs: [20, 150],
  minPeakDistanceSec: 0.05,
  peakProminenceQuantile: 0.1,
  noiseFloorQuantile: 0.20,
  pairingConfidenceThreshold: 0.50,
  s1S2IntervalCapSec: 0.4,
  longTermBpmLearningRate: 0.05,
  minBpm: 40,
  maxBpm: 240,
  outputSmoothingWindowSec: 5,
};

export class AudioProcessor {
  private audioContext: AudioContext | null = null;

  async processAudioFile(file: File): Promise<{
    audioData: Float32Array;
    sampleRate: number;
    duration: number;
  }> {
    // Initialize audio context
    this.audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
    
    try {
      // Read file as ArrayBuffer
      const arrayBuffer = await file.arrayBuffer();
      
      // Decode audio data
      const audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
      
      // Convert to mono if stereo
      let audioData: Float32Array;
      if (audioBuffer.numberOfChannels === 1) {
        audioData = audioBuffer.getChannelData(0);
      } else {
        // Average all channels to mono
        const length = audioBuffer.length;
        audioData = new Float32Array(length);
        for (let i = 0; i < length; i++) {
          let sum = 0;
          for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
            sum += audioBuffer.getChannelData(channel)[i];
          }
          audioData[i] = sum / audioBuffer.numberOfChannels;
        }
      }

      return {
        audioData,
        sampleRate: audioBuffer.sampleRate,
        duration: audioBuffer.duration,
      };
    } finally {
      // Clean up audio context
      if (this.audioContext) {
        await this.audioContext.close();
        this.audioContext = null;
      }
    }
  }

  // Simple bandpass filter implementation
  bandpassFilter(
    data: Float32Array,
    sampleRate: number,
    lowFreq: number,
    highFreq: number
  ): Float32Array {
    // Simple Butterworth-like filter approximation
    const nyquist = sampleRate / 2;
    const lowNorm = lowFreq / nyquist;
    const highNorm = highFreq / nyquist;
    
    // Create a simple FIR filter
    const filtered = new Float32Array(data.length);
    const filterLength = 21; // Simple odd-length filter
    const center = Math.floor(filterLength / 2);
    
    // Generate filter coefficients (simplified Hamming window approach)
    const coeffs = new Float32Array(filterLength);
    for (let i = 0; i < filterLength; i++) {
      const n = i - center;
      if (n === 0) {
        coeffs[i] = highNorm - lowNorm;
      } else {
        coeffs[i] = (Math.sin(Math.PI * n * highNorm) - Math.sin(Math.PI * n * lowNorm)) / (Math.PI * n);
      }
      // Apply Hamming window
      coeffs[i] *= 0.54 - 0.46 * Math.cos(2 * Math.PI * i / (filterLength - 1));
    }

    // Apply filter
    for (let i = center; i < data.length - center; i++) {
      let sum = 0;
      for (let j = 0; j < filterLength; j++) {
        sum += data[i - center + j] * coeffs[j];
      }
      filtered[i] = sum;
    }

    return filtered;
  }

  // Calculate envelope of the signal
  calculateEnvelope(data: Float32Array, sampleRate: number): Float32Array {
    // Take absolute value
    const absData = data.map(Math.abs);
    
    // Apply moving average (envelope)
    const windowSize = Math.floor(sampleRate / 10); // 100ms window
    const envelope = new Float32Array(absData.length);
    
    for (let i = 0; i < absData.length; i++) {
      let sum = 0;
      let count = 0;
      const start = Math.max(0, i - Math.floor(windowSize / 2));
      const end = Math.min(absData.length, i + Math.floor(windowSize / 2));
      
      for (let j = start; j < end; j++) {
        sum += absData[j];
        count++;
      }
      envelope[i] = count > 0 ? sum / count : 0;
    }
    
    return envelope;
  }

  // Downsample audio data
  downsample(data: Float32Array, factor: number): Float32Array {
    if (factor <= 1) return data;
    
    const newLength = Math.floor(data.length / factor);
    const downsampled = new Float32Array(newLength);
    
    for (let i = 0; i < newLength; i++) {
      downsampled[i] = data[i * factor];
    }
    
    return downsampled;
  }
}

// Mathematical utilities for signal processing
export class MathUtils {
  static findPeaks(data: Float32Array, minDistance: number, threshold?: Float32Array): number[] {
    const peaks: number[] = [];
    
    for (let i = 1; i < data.length - 1; i++) {
      // Check if this is a local maximum
      if (data[i] > data[i - 1] && data[i] > data[i + 1]) {
        // Check minimum distance from previous peak
        if (peaks.length === 0 || i - peaks[peaks.length - 1] >= minDistance) {
          // Check threshold if provided
          if (!threshold || data[i] > threshold[i]) {
            peaks.push(i);
          }
        }
      }
    }
    
    return peaks;
  }

  static calculateQuantile(data: Float32Array, quantile: number): number {
    const sorted = Array.from(data).sort((a, b) => a - b);
    const index = Math.floor(sorted.length * quantile);
    return sorted[Math.min(index, sorted.length - 1)];
  }

  static movingAverage(data: Float32Array, windowSize: number): Float32Array {
    const result = new Float32Array(data.length);
    
    for (let i = 0; i < data.length; i++) {
      let sum = 0;
      let count = 0;
      const start = Math.max(0, i - Math.floor(windowSize / 2));
      const end = Math.min(data.length, i + Math.floor(windowSize / 2) + 1);
      
      for (let j = start; j < end; j++) {
        sum += data[j];
        count++;
      }
      result[i] = count > 0 ? sum / count : 0;
    }
    
    return result;
  }

  static interpolate(x: number[], y: number[], xi: number): number {
    if (xi <= x[0]) return y[0];
    if (xi >= x[x.length - 1]) return y[y.length - 1];
    
    for (let i = 0; i < x.length - 1; i++) {
      if (xi >= x[i] && xi <= x[i + 1]) {
        const t = (xi - x[i]) / (x[i + 1] - x[i]);
        return y[i] + t * (y[i + 1] - y[i]);
      }
    }
    return y[0];
  }
}