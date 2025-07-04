export class AudioProcessor {
    constructor() {
        this.audioContext = null;
    }

    async loadAudioFile(file) {
        // Initialize AudioContext if needed
        if (!this.audioContext) {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }

        // Read file as ArrayBuffer
        const arrayBuffer = await file.arrayBuffer();
        
        // Decode audio data
        const audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
        
        // Get the first channel (mono)
        const channelData = audioBuffer.getChannelData(0);
        
        return {
            data: channelData,
            sampleRate: audioBuffer.sampleRate,
            duration: audioBuffer.duration,
            numberOfChannels: audioBuffer.numberOfChannels
        };
    }

    async preprocessAudio(audioData, params = {}) {
        const {
            downsampleFactor = 300,
            bandpassFreqs = [20, 150],
            minPeakDistanceSec = 0.05
        } = params;

        let processedData = Array.from(audioData.data);
        let sampleRate = audioData.sampleRate;

        // Downsample the audio
        if (downsampleFactor > 1) {
            const newSampleRate = Math.floor(sampleRate / downsampleFactor);
            processedData = this.downsample(processedData, downsampleFactor);
            sampleRate = newSampleRate;
        }

        // Apply bandpass filter
        processedData = this.bandpassFilter(processedData, sampleRate, bandpassFreqs);

        // Calculate envelope (absolute value and smoothing)
        const envelope = this.calculateEnvelope(processedData);

        // Calculate dynamic noise floor
        const { noiseFloor, troughs } = this.calculateDynamicNoiseFloor(envelope, sampleRate);

        return {
            originalData: audioData.data,
            processedData: processedData,
            envelope: envelope,
            sampleRate: sampleRate,
            originalSampleRate: audioData.sampleRate,
            noiseFloor: noiseFloor,
            troughs: troughs,
            duration: audioData.duration
        };
    }

    downsample(data, factor) {
        const result = [];
        for (let i = 0; i < data.length; i += factor) {
            result.push(data[i]);
        }
        return result;
    }

    bandpassFilter(data, sampleRate, freqs) {
        // Simple bandpass filter implementation
        // This is a simplified version - in production, you'd want a more sophisticated filter
        const lowFreq = freqs[0];
        const highFreq = freqs[1];
        
        // Apply high-pass filter (remove very low frequencies)
        let filtered = this.highPassFilter(data, sampleRate, lowFreq);
        
        // Apply low-pass filter (remove very high frequencies)
        filtered = this.lowPassFilter(filtered, sampleRate, highFreq);
        
        return filtered;
    }

    highPassFilter(data, sampleRate, cutoffFreq) {
        // Simple first-order high-pass filter
        const RC = 1.0 / (2 * Math.PI * cutoffFreq);
        const dt = 1.0 / sampleRate;
        const alpha = RC / (RC + dt);
        
        const filtered = new Array(data.length);
        filtered[0] = data[0];
        
        for (let i = 1; i < data.length; i++) {
            filtered[i] = alpha * (filtered[i-1] + data[i] - data[i-1]);
        }
        
        return filtered;
    }

    lowPassFilter(data, sampleRate, cutoffFreq) {
        // Simple first-order low-pass filter
        const RC = 1.0 / (2 * Math.PI * cutoffFreq);
        const dt = 1.0 / sampleRate;
        const alpha = dt / (RC + dt);
        
        const filtered = new Array(data.length);
        filtered[0] = data[0];
        
        for (let i = 1; i < data.length; i++) {
            filtered[i] = filtered[i-1] + alpha * (data[i] - filtered[i-1]);
        }
        
        return filtered;
    }

    calculateEnvelope(data) {
        // Calculate absolute value
        const abs_data = data.map(x => Math.abs(x));
        
        // Apply smoothing (moving average)
        const windowSize = 5;
        const envelope = new Array(abs_data.length);
        
        for (let i = 0; i < abs_data.length; i++) {
            let sum = 0;
            let count = 0;
            
            for (let j = Math.max(0, i - windowSize); j <= Math.min(abs_data.length - 1, i + windowSize); j++) {
                sum += abs_data[j];
                count++;
            }
            
            envelope[i] = sum / count;
        }
        
        return envelope;
    }

    calculateDynamicNoiseFloor(envelope, sampleRate, params = {}) {
        const {
            noiseFloorQuantile = 0.20,
            noiseWindowSec = 10,
            troughProminenceQuantile = 0.1
        } = params;

        // Find troughs (local minima)
        const troughs = this.findTroughs(envelope, troughProminenceQuantile);
        
        // Calculate dynamic noise floor using rolling window
        const windowSize = Math.floor(noiseWindowSec * sampleRate);
        const noiseFloor = new Array(envelope.length);
        
        for (let i = 0; i < envelope.length; i++) {
            const windowStart = Math.max(0, i - windowSize / 2);
            const windowEnd = Math.min(envelope.length, i + windowSize / 2);
            
            // Get values in the window
            const windowValues = envelope.slice(windowStart, windowEnd);
            
            // Calculate the quantile (noise floor)
            windowValues.sort((a, b) => a - b);
            const quantileIndex = Math.floor(windowValues.length * noiseFloorQuantile);
            noiseFloor[i] = windowValues[quantileIndex] || 0;
        }
        
        return { noiseFloor, troughs };
    }

    findTroughs(data, prominenceQuantile) {
        const prominenceThreshold = this.quantile(data, prominenceQuantile);
        const troughs = [];
        
        for (let i = 1; i < data.length - 1; i++) {
            // Check if this is a local minimum
            if (data[i] < data[i-1] && data[i] < data[i+1]) {
                // Check prominence
                const leftMax = Math.max(...data.slice(Math.max(0, i-20), i));
                const rightMax = Math.max(...data.slice(i+1, Math.min(data.length, i+21)));
                const prominence = Math.min(leftMax - data[i], rightMax - data[i]);
                
                if (prominence >= prominenceThreshold) {
                    troughs.push(i);
                }
            }
        }
        
        return troughs;
    }

    quantile(arr, q) {
        const sorted = [...arr].sort((a, b) => a - b);
        const index = (sorted.length - 1) * q;
        const floor = Math.floor(index);
        const ceil = Math.ceil(index);
        
        if (floor === ceil) {
            return sorted[floor];
        }
        
        return sorted[floor] * (ceil - index) + sorted[ceil] * (index - floor);
    }
}