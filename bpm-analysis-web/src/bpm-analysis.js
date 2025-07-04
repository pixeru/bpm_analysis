// Default parameters matching the Python configuration
const DEFAULT_PARAMS = {
    // Signal preprocessing
    downsampleFactor: 300,
    bandpassFreqs: [20, 150],
    
    // Peak detection
    minPeakDistanceSec: 0.05,
    peakProminenceQuantile: 0.1,
    
    // Noise estimation
    noiseFloorQuantile: 0.20,
    noiseWindowSec: 10,
    troughProminenceQuantile: 0.1,
    troughRejectionMultiplier: 4.0,
    
    // S1/S2 pairing
    pairingConfidenceThreshold: 0.50,
    s1s2IntervalCapSec: 0.4,
    s1s2IntervalRrFraction: 0.7,
    
    // Confidence model
    deviationSmoothingFactor: 0.05,
    confidenceDeviationPoints: [0.0, 0.25, 0.40, 0.80, 1.0],
    confidenceCurveLowBpm: [0.9, 0.9, 0.7, 0.1, 0.1],
    confidenceCurveHighBpm: [0.1, 0.5, 0.75, 0.65, 0],
    
    // Stability and rhythm
    stabilityHistoryWindow: 20,
    stabilityConfidenceFloor: 0.60,
    stabilityConfidenceCeiling: 1.25,
    
    // Long-term BPM
    longTermBpmLearningRate: 0.05,
    maxBpmChangePerBeat: 3.0,
    minBpm: 40,
    maxBpm: 240,
    
    // Lone S1 validation
    loneS1ConfidenceThreshold: 0.50,
    loneS1RhythmWeight: 0.65,
    loneS1AmplitudeWeight: 0.35,
    loneS1ForwardCheckPct: 0.50,
    
    // Output smoothing
    outputSmoothingWindowSec: 5,
    
    // HRV calculation
    hrvWindowSizeBeats: 40,
    hrvStepSizeBeats: 5
};

// Peak type enumeration
const PeakType = {
    S1_PAIRED: "S1 (Paired)",
    S2_PAIRED: "S2 (Paired)",
    LONE_S1_VALIDATED: "Lone S1 (Validated)",
    LONE_S1_CASCADE: "Lone S1 (Corrected by Cascade Reset)",
    LONE_S1_LAST: "Lone S1 (Last Peak)",
    NOISE: "Noise/Rejected",
    S1_CORRECTED_GAP: "S1 (Paired - Corrected from Gap)",
    S2_CORRECTED_GAP: "S2 (Paired - Corrected from Gap)",
    S2_CORRECTED_CONFLICT: "S2 (Paired - Corrected from Conflict)"
};

export class BPMAnalyzer {
    constructor(params = {}) {
        this.params = { ...DEFAULT_PARAMS, ...params };
    }

    async analyzeHeartbeat(processedData, options = {}) {
        const { startBpmHint, sampleRate } = options;
        
        // Initialize analysis state
        const state = this.initializeState(processedData, startBpmHint || 80.0);
        
        // Find all potential peaks
        const allPeaks = this.findRawPeaks(processedData.envelope, processedData.noiseFloor);
        
        // Classify peaks into S1, S2, and noise
        const { finalPeaks, peakDebugInfo } = this.classifyPeaks(
            allPeaks, 
            processedData.envelope, 
            processedData.noiseFloor,
            state
        );
        
        // Calculate BPM time series
        const bpmSeries = this.calculateBpmSeries(finalPeaks, processedData.sampleRate);
        
        // Calculate HRV metrics
        const hrvMetrics = this.calculateHRV(finalPeaks, processedData.sampleRate);
        
        // Generate final metrics
        const finalMetrics = this.calculateFinalMetrics(finalPeaks, bpmSeries, hrvMetrics);
        
        return {
            ...finalMetrics,
            peaks: finalPeaks,
            allPeaks: allPeaks,
            peakDebugInfo: peakDebugInfo,
            bpmSeries: bpmSeries,
            hrvMetrics: hrvMetrics,
            processedData: processedData
        };
    }

    initializeState(processedData, startBpmHint) {
        return {
            longTermBpm: startBpmHint,
            candidateBeats: [],
            beatDebugInfo: {},
            longTermBpmHistory: [],
            consecutiveRrRejections: 0,
            loopIdx: 0
        };
    }

    findRawPeaks(envelope, noiseFloor) {
        const peaks = [];
        const minDistance = Math.floor(this.params.minPeakDistanceSec * 1000); // Assuming 1000 Hz after processing
        
        // Calculate prominence threshold
        const prominenceThreshold = this.quantile(envelope, this.params.peakProminenceQuantile);
        
        for (let i = 1; i < envelope.length - 1; i++) {
            // Check if this is a local maximum
            if (envelope[i] > envelope[i-1] && envelope[i] > envelope[i+1]) {
                // Check height threshold
                if (envelope[i] > noiseFloor[i]) {
                    // Check prominence
                    const leftMin = Math.min(...envelope.slice(Math.max(0, i-20), i));
                    const rightMin = Math.min(...envelope.slice(i+1, Math.min(envelope.length, i+21)));
                    const prominence = Math.min(envelope[i] - leftMin, envelope[i] - rightMin);
                    
                    if (prominence >= prominenceThreshold) {
                        // Check minimum distance
                        let validDistance = true;
                        for (let j = peaks.length - 1; j >= 0; j--) {
                            if (i - peaks[j] < minDistance) {
                                validDistance = false;
                                break;
                            }
                            if (i - peaks[j] >= minDistance) {
                                break;
                            }
                        }
                        
                        if (validDistance) {
                            peaks.push(i);
                        }
                    }
                }
            }
        }
        
        return peaks;
    }

    classifyPeaks(allPeaks, envelope, noiseFloor, state) {
        const peakDebugInfo = {};
        
        while (state.loopIdx < allPeaks.length) {
            const currentPeakIdx = allPeaks[state.loopIdx];
            const isLastPeak = state.loopIdx >= allPeaks.length - 1;
            
            if (isLastPeak) {
                this.handleLastPeak(currentPeakIdx, state, peakDebugInfo);
            } else {
                this.processPeakPair(currentPeakIdx, allPeaks, envelope, noiseFloor, state, peakDebugInfo);
            }
            
            this.updateLongTermBpm(state);
        }
        
        return {
            finalPeaks: [...state.candidateBeats],
            peakDebugInfo: peakDebugInfo
        };
    }

    handleLastPeak(peakIdx, state, debugInfo) {
        state.candidateBeats.push(peakIdx);
        debugInfo[peakIdx] = PeakType.LONE_S1_LAST;
        state.loopIdx++;
    }

    processPeakPair(currentPeakIdx, allPeaks, envelope, noiseFloor, state, debugInfo) {
        const nextPeakIdx = allPeaks[state.loopIdx + 1];
        const pairingRatio = this.calculatePairingRatio(state);
        
        const { isPaired, reason } = this.attemptS1S2Pairing(
            currentPeakIdx, 
            nextPeakIdx, 
            envelope, 
            noiseFloor, 
            state.longTermBpm, 
            pairingRatio
        );
        
        if (isPaired) {
            state.candidateBeats.push(currentPeakIdx);
            debugInfo[currentPeakIdx] = PeakType.S1_PAIRED;
            debugInfo[nextPeakIdx] = PeakType.S2_PAIRED;
            state.consecutiveRrRejections = 0;
            state.loopIdx += 2;
        } else {
            this.classifyLonePeak(currentPeakIdx, envelope, noiseFloor, state, debugInfo, reason);
            state.loopIdx++;
        }
    }

    attemptS1S2Pairing(s1Idx, s2Idx, envelope, noiseFloor, longTermBpm, pairingRatio) {
        const intervalSec = (s2Idx - s1Idx) / 1000; // Assuming 1000 Hz sample rate
        
        // Check minimum distance
        if (intervalSec < this.params.minPeakDistanceSec) {
            return { isPaired: false, reason: `Interval too short: ${intervalSec.toFixed(3)}s` };
        }
        
        // Calculate confidence based on amplitude deviation
        const confidence = this.calculatePairingConfidence(s1Idx, s2Idx, envelope, longTermBpm);
        
        // Apply stability adjustments
        const adjustedConfidence = this.adjustConfidenceWithStability(confidence, pairingRatio);
        
        // Check interval penalty
        const finalConfidence = this.applyIntervalPenalty(adjustedConfidence, intervalSec, longTermBpm);
        
        const isPaired = finalConfidence >= this.params.pairingConfidenceThreshold;
        const reason = `Confidence: ${finalConfidence.toFixed(3)} (threshold: ${this.params.pairingConfidenceThreshold})`;
        
        return { isPaired, reason };
    }

    calculatePairingConfidence(s1Idx, s2Idx, envelope, longTermBpm) {
        const s1Strength = envelope[s1Idx];
        const s2Strength = envelope[s2Idx];
        
        // Calculate normalized deviation between S1 and S2
        const deviation = Math.abs(s1Strength - s2Strength) / Math.max(s1Strength, s2Strength);
        
        // Use blended confidence model based on BPM
        const blendRatio = Math.max(0, Math.min(1, 
            (longTermBpm - 120) / (140 - 120)
        ));
        
        // Interpolate confidence curves
        const lowBpmConf = this.interpolateConfidence(deviation, this.params.confidenceDeviationPoints, this.params.confidenceCurveLowBpm);
        const highBpmConf = this.interpolateConfidence(deviation, this.params.confidenceDeviationPoints, this.params.confidenceCurveHighBpm);
        
        return lowBpmConf * (1 - blendRatio) + highBpmConf * blendRatio;
    }

    interpolateConfidence(x, xPoints, yPoints) {
        // Linear interpolation
        for (let i = 0; i < xPoints.length - 1; i++) {
            if (x >= xPoints[i] && x <= xPoints[i + 1]) {
                const t = (x - xPoints[i]) / (xPoints[i + 1] - xPoints[i]);
                return yPoints[i] * (1 - t) + yPoints[i + 1] * t;
            }
        }
        
        // Extrapolation
        if (x < xPoints[0]) return yPoints[0];
        return yPoints[yPoints.length - 1];
    }

    adjustConfidenceWithStability(confidence, pairingRatio) {
        const floor = this.params.stabilityConfidenceFloor;
        const ceiling = this.params.stabilityConfidenceCeiling;
        const multiplier = floor + (ceiling - floor) * pairingRatio;
        return confidence * multiplier;
    }

    applyIntervalPenalty(confidence, intervalSec, longTermBpm) {
        const maxInterval = Math.min(
            this.params.s1s2IntervalCapSec,
            (60.0 / longTermBpm) * this.params.s1s2IntervalRrFraction
        );
        
        if (intervalSec <= maxInterval) {
            return confidence;
        }
        
        const penaltyStart = maxInterval * this.params.intervalPenaltyStartFactor || maxInterval;
        const penaltyFull = maxInterval * this.params.intervalPenaltyFullFactor || (maxInterval * 1.4);
        
        if (intervalSec <= penaltyStart) {
            return confidence;
        }
        
        let penaltyFactor = 0;
        if (intervalSec >= penaltyFull) {
            penaltyFactor = 1;
        } else {
            penaltyFactor = (intervalSec - penaltyStart) / (penaltyFull - penaltyStart);
        }
        
        const maxPenalty = this.params.intervalMaxPenalty || 0.75;
        return Math.max(0, confidence - maxPenalty * penaltyFactor);
    }

    classifyLonePeak(peakIdx, envelope, noiseFloor, state, debugInfo, pairingFailureReason) {
        const isValid = this.validateLoneS1(peakIdx, envelope, state);
        
        if (isValid) {
            state.candidateBeats.push(peakIdx);
            debugInfo[peakIdx] = PeakType.LONE_S1_VALIDATED;
            state.consecutiveRrRejections = 0;
        } else {
            state.consecutiveRrRejections++;
            
            // Cascade reset mechanism
            if (state.consecutiveRrRejections >= 3) {
                state.candidateBeats.push(peakIdx);
                debugInfo[peakIdx] = PeakType.LONE_S1_CASCADE;
                state.consecutiveRrRejections = 0;
            } else {
                debugInfo[peakIdx] = PeakType.NOISE;
            }
        }
    }

    validateLoneS1(peakIdx, envelope, state) {
        if (state.candidateBeats.length === 0) {
            return true; // First beat
        }
        
        const lastBeatIdx = state.candidateBeats[state.candidateBeats.length - 1];
        const rrInterval = (peakIdx - lastBeatIdx) / 1000; // Assuming 1000 Hz
        const expectedRr = 60.0 / state.longTermBpm;
        
        // Check rhythm fit
        const rhythmDeviation = Math.abs(rrInterval - expectedRr) / expectedRr;
        const rhythmConfidence = this.interpolateConfidence(
            rhythmDeviation, 
            [0.0, 0.15, 0.30, 0.50], 
            [1.0, 0.8, 0.4, 0.0]
        );
        
        // Check amplitude consistency
        const currentStrength = envelope[peakIdx];
        const lastStrength = envelope[lastBeatIdx];
        const amplitudeRatio = currentStrength / lastStrength;
        const amplitudeConfidence = this.interpolateConfidence(
            amplitudeRatio,
            [0.0, 0.4, 0.7, 1.0],
            [0.0, 0.4, 0.8, 1.0]
        );
        
        // Combined confidence
        const combinedConfidence = 
            rhythmConfidence * this.params.loneS1RhythmWeight + 
            amplitudeConfidence * this.params.loneS1AmplitudeWeight;
        
        return combinedConfidence >= this.params.loneS1ConfidenceThreshold;
    }

    calculatePairingRatio(state) {
        const historyWindow = this.params.stabilityHistoryWindow;
        if (state.candidateBeats.length < historyWindow) {
            return 0.5; // Default neutral ratio
        }
        
        // This is a simplified version - in the full implementation,
        // we'd track which beats were paired vs lone S1s
        return 0.7; // Assume reasonable pairing ratio for now
    }

    updateLongTermBpm(state) {
        if (state.candidateBeats.length > 1) {
            const lastIdx = state.candidateBeats.length - 1;
            const newRr = (state.candidateBeats[lastIdx] - state.candidateBeats[lastIdx - 1]) / 1000;
            if (newRr > 0) {
                const newBpm = 60.0 / newRr;
                const learningRate = this.params.longTermBpmLearningRate;
                const maxChange = this.params.maxBpmChangePerBeat;
                
                let bpmChange = (newBpm - state.longTermBpm) * learningRate;
                bpmChange = Math.max(-maxChange, Math.min(maxChange, bpmChange));
                
                state.longTermBpm = Math.max(this.params.minBpm, 
                    Math.min(this.params.maxBpm, state.longTermBpm + bpmChange));
            }
        }
        
        // Record BPM history
        if (state.candidateBeats.length > 0) {
            const timeSec = state.candidateBeats[state.candidateBeats.length - 1] / 1000;
            state.longTermBpmHistory.push({ time: timeSec, bpm: state.longTermBpm });
        }
    }

    calculateBpmSeries(peaks, sampleRate) {
        if (peaks.length < 2) {
            return { times: [], bpm: [] };
        }
        
        const times = [];
        const bpm = [];
        
        for (let i = 1; i < peaks.length; i++) {
            const rrInterval = (peaks[i] - peaks[i-1]) / sampleRate;
            const instantBpm = 60.0 / rrInterval;
            const timeSec = peaks[i] / sampleRate;
            
            times.push(timeSec);
            bpm.push(instantBpm);
        }
        
        // Apply smoothing
        const smoothedBpm = this.applySmoothingFilter(bpm, this.params.outputSmoothingWindowSec);
        
        return { times, bpm: smoothedBpm };
    }

    applySmoothingFilter(data, windowSec) {
        // Simple moving average
        const windowSize = Math.max(1, Math.floor(windowSec));
        const smoothed = [];
        
        for (let i = 0; i < data.length; i++) {
            let sum = 0;
            let count = 0;
            
            for (let j = Math.max(0, i - windowSize); j <= Math.min(data.length - 1, i + windowSize); j++) {
                sum += data[j];
                count++;
            }
            
            smoothed.push(sum / count);
        }
        
        return smoothed;
    }

    calculateHRV(peaks, sampleRate) {
        if (peaks.length < 3) {
            return { rmssd: 0, meanRr: 0, sdnn: 0 };
        }
        
        // Calculate RR intervals
        const rrIntervals = [];
        for (let i = 1; i < peaks.length; i++) {
            const rrMs = (peaks[i] - peaks[i-1]) / sampleRate * 1000;
            rrIntervals.push(rrMs);
        }
        
        // Calculate HRV metrics
        const meanRr = rrIntervals.reduce((a, b) => a + b, 0) / rrIntervals.length;
        
        // SDNN (standard deviation of RR intervals)
        const variance = rrIntervals.reduce((sum, rr) => sum + Math.pow(rr - meanRr, 2), 0) / rrIntervals.length;
        const sdnn = Math.sqrt(variance);
        
        // RMSSD (root mean square of successive differences)
        if (rrIntervals.length < 2) {
            return { rmssd: 0, meanRr, sdnn };
        }
        
        const successiveDiffs = [];
        for (let i = 1; i < rrIntervals.length; i++) {
            successiveDiffs.push(Math.pow(rrIntervals[i] - rrIntervals[i-1], 2));
        }
        const rmssd = Math.sqrt(successiveDiffs.reduce((a, b) => a + b, 0) / successiveDiffs.length);
        
        return { rmssd, meanRr, sdnn };
    }

    calculateFinalMetrics(peaks, bpmSeries, hrvMetrics) {
        if (peaks.length === 0) {
            return {
                totalS1Beats: 0,
                s1s2Pairs: 0,
                averageBpm: 0,
                peakBpm: 0,
                minBpm: 0,
                hrv: 0
            };
        }
        
        const totalS1Beats = peaks.length;
        const s1s2Pairs = Math.floor(peaks.length / 2); // Simplified estimation
        
        let averageBpm = 0;
        let peakBpm = 0;
        let minBpm = Infinity;
        
        if (bpmSeries.bpm.length > 0) {
            averageBpm = bpmSeries.bpm.reduce((a, b) => a + b, 0) / bpmSeries.bpm.length;
            peakBpm = Math.max(...bpmSeries.bpm);
            minBpm = Math.min(...bpmSeries.bpm);
        }
        
        return {
            totalS1Beats,
            s1s2Pairs,
            averageBpm,
            peakBpm,
            minBpm: minBpm === Infinity ? 0 : minBpm,
            hrv: hrvMetrics.rmssd
        };
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