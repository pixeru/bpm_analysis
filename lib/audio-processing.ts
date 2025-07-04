/**
 * Audio processing utilities for BPM analysis using Web Audio API
 */

// Simple peak detection algorithm
export function findPeaks(data: number[], options: {
  height?: number[];
  prominence?: number;
  distance?: number;
} = {}): number[] {
  const peaks: number[] = [];
  const { height, prominence = 0, distance = 1 } = options;

  for (let i = 1; i < data.length - 1; i++) {
    // Check if it's a local maximum
    if (data[i] > data[i - 1] && data[i] > data[i + 1]) {
      // Check height threshold
      if (height && (data[i] < height[i])) continue;
      
      // Check prominence
      if (prominence > 0) {
        let leftMin = data[i];
        let rightMin = data[i];
        
        // Find left minimum
        for (let j = i - 1; j >= 0; j--) {
          if (data[j] < leftMin) leftMin = data[j];
          if (data[j] > data[i]) break;
        }
        
        // Find right minimum
        for (let j = i + 1; j < data.length; j++) {
          if (data[j] < rightMin) rightMin = data[j];
          if (data[j] > data[i]) break;
        }
        
        const actualProminence = data[i] - Math.max(leftMin, rightMin);
        if (actualProminence < prominence) continue;
      }
      
      // Check distance from last peak
      if (distance > 1 && peaks.length > 0) {
        if (i - peaks[peaks.length - 1] < distance) continue;
      }
      
      peaks.push(i);
    }
  }
  
  return peaks;
}

// Simple Butterworth bandpass filter implementation
export function butterworthBandpass(data: number[], lowCut: number, highCut: number, sampleRate: number): number[] {
  // This is a simplified implementation. For production use, consider using a proper DSP library
  const nyquist = sampleRate / 2;
  const low = lowCut / nyquist;
  const high = highCut / nyquist;
  
  // Simple moving average approximation for demonstration
  // In a real implementation, you'd want to use proper IIR filter coefficients
  const filtered = [...data];
  const windowSize = Math.floor(sampleRate / (highCut + lowCut));
  
  for (let i = windowSize; i < filtered.length - windowSize; i++) {
    let sum = 0;
    for (let j = -windowSize; j <= windowSize; j++) {
      sum += data[i + j];
    }
    filtered[i] = sum / (2 * windowSize + 1);
  }
  
  return filtered;
}

// Calculate quantile of an array
export function quantile(data: number[], q: number): number {
  const sorted = [...data].sort((a, b) => a - b);
  const index = (sorted.length - 1) * q;
  const lower = Math.floor(index);
  const upper = Math.ceil(index);
  const weight = index % 1;
  
  if (upper >= sorted.length) return sorted[sorted.length - 1];
  return sorted[lower] * (1 - weight) + sorted[upper] * weight;
}

// Rolling window calculation
export function rollingWindow<T>(data: T[], windowSize: number, func: (window: T[]) => number): number[] {
  const result: number[] = [];
  const halfWindow = Math.floor(windowSize / 2);
  
  for (let i = 0; i < data.length; i++) {
    const start = Math.max(0, i - halfWindow);
    const end = Math.min(data.length, i + halfWindow + 1);
    const window = data.slice(start, end);
    result.push(func(window));
  }
  
  return result;
}

// Calculate audio envelope
export function calculateEnvelope(audioData: Float32Array): number[] {
  const envelope: number[] = [];
  const windowSize = Math.floor(audioData.length / 1000); // Adaptive window size
  
  for (let i = 0; i < audioData.length; i += windowSize) {
    const end = Math.min(i + windowSize, audioData.length);
    let max = 0;
    
    for (let j = i; j < end; j++) {
      max = Math.max(max, Math.abs(audioData[j]));
    }
    
    envelope.push(max);
  }
  
  return envelope;
}

// Downsample audio data
export function downsample(data: Float32Array, factor: number): Float32Array {
  const length = Math.floor(data.length / factor);
  const downsampled = new Float32Array(length);
  
  for (let i = 0; i < length; i++) {
    downsampled[i] = data[i * factor];
  }
  
  return downsampled;
}

// Load and decode audio file
export async function loadAudioFile(file: File): Promise<{ audioData: Float32Array; sampleRate: number }> {
  return new Promise((resolve, reject) => {
    const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
    const reader = new FileReader();
    
    reader.onload = async (e) => {
      try {
        const arrayBuffer = e.target?.result as ArrayBuffer;
        const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
        
        // Get mono channel data
        const audioData = audioBuffer.getChannelData(0);
        const sampleRate = audioBuffer.sampleRate;
        
        resolve({ audioData, sampleRate });
      } catch (error) {
        reject(error);
      }
    };
    
    reader.onerror = () => reject(new Error('Failed to read file'));
    reader.readAsArrayBuffer(file);
  });
}

// Smooth data using moving average
export function smoothData(data: number[], windowSize: number): number[] {
  const smoothed: number[] = [];
  const halfWindow = Math.floor(windowSize / 2);
  
  for (let i = 0; i < data.length; i++) {
    const start = Math.max(0, i - halfWindow);
    const end = Math.min(data.length, i + halfWindow + 1);
    
    let sum = 0;
    for (let j = start; j < end; j++) {
      sum += data[j];
    }
    
    smoothed.push(sum / (end - start));
  }
  
  return smoothed;
}

// Calculate HRV metrics
export function calculateHRV(rrIntervals: number[]): {
  mean_rr: number;
  rmssd: number;
  pnn50: number;
  triangular_index: number;
  sample_entropy: number;
} {
  const mean_rr = rrIntervals.reduce((a, b) => a + b, 0) / rrIntervals.length;
  
  // RMSSD calculation
  const diffSquares: number[] = [];
  for (let i = 1; i < rrIntervals.length; i++) {
    const diff = rrIntervals[i] - rrIntervals[i - 1];
    diffSquares.push(diff * diff);
  }
  const rmssd = Math.sqrt(diffSquares.reduce((a, b) => a + b, 0) / diffSquares.length);
  
  // pNN50 calculation
  let nn50Count = 0;
  for (let i = 1; i < rrIntervals.length; i++) {
    if (Math.abs(rrIntervals[i] - rrIntervals[i - 1]) > 0.05) { // 50ms in seconds
      nn50Count++;
    }
  }
  const pnn50 = (nn50Count / (rrIntervals.length - 1)) * 100;
  
  // Simplified triangular index (histogram-based)
  const triangular_index = rrIntervals.length / 0.01; // Simplified calculation
  
  // Simplified sample entropy
  const sample_entropy = Math.log(rrIntervals.length); // Placeholder calculation
  
  return {
    mean_rr,
    rmssd,
    pnn50,
    triangular_index,
    sample_entropy
  };
}