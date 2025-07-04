import Plotly from 'plotly.js-dist';

export class PlotGenerator {
    constructor() {
        this.darkTheme = {
            paper_bgcolor: '#2d3748',
            plot_bgcolor: '#1a202c',
            font: { color: '#e2e8f0' },
            xaxis: { 
                gridcolor: '#4a5568',
                zerolinecolor: '#4a5568',
                color: '#e2e8f0'
            },
            yaxis: { 
                gridcolor: '#4a5568',
                zerolinecolor: '#4a5568',
                color: '#e2e8f0'
            }
        };
    }

    async createAnalysisPlot(processedData, analysisResults, container) {
        const traces = [];
        
        // Create time axis
        const timeAxis = this.createTimeAxis(processedData.envelope.length, processedData.sampleRate);
        
        // Add audio envelope trace
        traces.push(this.createEnvelopeTrace(timeAxis, processedData.envelope));
        
        // Add noise floor trace
        if (processedData.noiseFloor) {
            traces.push(this.createNoiseFloorTrace(timeAxis, processedData.noiseFloor));
        }
        
        // Add trough markers
        if (processedData.troughs) {
            traces.push(this.createTroughTrace(processedData.troughs, processedData.envelope, processedData.sampleRate));
        }
        
        // Add peak traces (S1, S2, Noise)
        const peakTraces = this.createPeakTraces(
            analysisResults.peaks,
            analysisResults.allPeaks,
            analysisResults.peakDebugInfo,
            processedData.envelope,
            processedData.sampleRate
        );
        traces.push(...peakTraces);
        
        // Add BPM trace
        if (analysisResults.bpmSeries && analysisResults.bpmSeries.times.length > 0) {
            traces.push(this.createBpmTrace(analysisResults.bpmSeries));
        }
        
        // Add HRV trace (if available)
        if (analysisResults.hrvMetrics) {
            traces.push(this.createHrvTrace(analysisResults.bpmSeries, analysisResults.hrvMetrics));
        }
        
        // Create layout
        const layout = this.createLayout(processedData.duration);
        
        // Plot configuration
        const config = {
            scrollZoom: true,
            displayModeBar: true,
            toImageButtonOptions: {
                filename: 'heartbeat_analysis',
                format: 'png',
                scale: 2
            },
            responsive: true
        };
        
        // Create the plot
        await Plotly.newPlot(container, traces, layout, config);
        
        return container;
    }

    createTimeAxis(length, sampleRate) {
        const timeArray = [];
        for (let i = 0; i < length; i++) {
            timeArray.push(i / sampleRate);
        }
        return timeArray;
    }

    createEnvelopeTrace(timeAxis, envelope) {
        return {
            x: timeAxis,
            y: envelope,
            type: 'scatter',
            mode: 'lines',
            name: 'Audio Envelope',
            line: { 
                color: '#47a5c4',
                width: 1.5
            },
            yaxis: 'y1',
            hovertemplate: 'Time: %{x:.2f}s<br>Amplitude: %{y:.2f}<extra></extra>'
        };
    }

    createNoiseFloorTrace(timeAxis, noiseFloor) {
        return {
            x: timeAxis,
            y: noiseFloor,
            type: 'scatter',
            mode: 'lines',
            name: 'Dynamic Noise Floor',
            line: { 
                color: '#48bb78',
                width: 1.5,
                dash: 'dot'
            },
            yaxis: 'y1',
            hovertemplate: 'Time: %{x:.2f}s<br>Noise Floor: %{y:.2f}<extra></extra>'
        };
    }

    createTroughTrace(troughs, envelope, sampleRate) {
        const troughTimes = troughs.map(idx => idx / sampleRate);
        const troughValues = troughs.map(idx => envelope[idx]);
        
        return {
            x: troughTimes,
            y: troughValues,
            type: 'scatter',
            mode: 'markers',
            name: 'Troughs',
            marker: {
                color: '#48bb78',
                symbol: 'circle-open',
                size: 6
            },
            visible: 'legendonly',
            yaxis: 'y1',
            hovertemplate: 'Trough<br>Time: %{x:.2f}s<br>Amplitude: %{y:.2f}<extra></extra>'
        };
    }

    createPeakTraces(finalPeaks, allPeaks, peakDebugInfo, envelope, sampleRate) {
        const traces = [];
        
        // Categorize peaks
        const s1Peaks = { indices: [], customData: [] };
        const s2Peaks = { indices: [], customData: [] };
        const noisePeaks = { indices: [], customData: [] };
        
        // Process all peaks with debug info
        Object.entries(peakDebugInfo).forEach(([peakIdx, debugInfo]) => {
            const idx = parseInt(peakIdx);
            const time = idx / sampleRate;
            const amplitude = envelope[idx];
            
            const hoverInfo = this.createPeakHoverInfo(idx, time, amplitude, debugInfo);
            
            if (debugInfo.includes('S1')) {
                s1Peaks.indices.push(idx);
                s1Peaks.customData.push(hoverInfo);
            } else if (debugInfo.includes('S2')) {
                s2Peaks.indices.push(idx);
                s2Peaks.customData.push(hoverInfo);
            } else {
                noisePeaks.indices.push(idx);
                noisePeaks.customData.push(hoverInfo);
            }
        });
        
        // Create S1 trace
        if (s1Peaks.indices.length > 0) {
            traces.push({
                x: s1Peaks.indices.map(idx => idx / sampleRate),
                y: s1Peaks.indices.map(idx => envelope[idx]),
                type: 'scatter',
                mode: 'markers',
                name: 'S1 Heartbeats',
                marker: {
                    color: '#e53e3e',
                    symbol: 'triangle-up',
                    size: 10,
                    line: { color: '#c53030', width: 1 }
                },
                customdata: s1Peaks.customData,
                yaxis: 'y1',
                hovertemplate: '%{customdata}<extra></extra>'
            });
        }
        
        // Create S2 trace
        if (s2Peaks.indices.length > 0) {
            traces.push({
                x: s2Peaks.indices.map(idx => idx / sampleRate),
                y: s2Peaks.indices.map(idx => envelope[idx]),
                type: 'scatter',
                mode: 'markers',
                name: 'S2 Heartbeats',
                marker: {
                    color: '#3182ce',
                    symbol: 'triangle-down',
                    size: 8,
                    line: { color: '#2c5aa0', width: 1 }
                },
                customdata: s2Peaks.customData,
                yaxis: 'y1',
                hovertemplate: '%{customdata}<extra></extra>'
            });
        }
        
        // Create noise trace
        if (noisePeaks.indices.length > 0) {
            traces.push({
                x: noisePeaks.indices.map(idx => idx / sampleRate),
                y: noisePeaks.indices.map(idx => envelope[idx]),
                type: 'scatter',
                mode: 'markers',
                name: 'Noise/Rejected',
                marker: {
                    color: '#718096',
                    symbol: 'x',
                    size: 6
                },
                customdata: noisePeaks.customData,
                visible: 'legendonly',
                yaxis: 'y1',
                hovertemplate: '%{customdata}<extra></extra>'
            });
        }
        
        return traces;
    }

    createPeakHoverInfo(peakIdx, time, amplitude, debugInfo) {
        let hoverText = `<b>Peak Index:</b> ${peakIdx}<br>`;
        hoverText += `<b>Time:</b> ${time.toFixed(2)}s<br>`;
        hoverText += `<b>Amplitude:</b> ${amplitude.toFixed(0)}<br>`;
        hoverText += `<b>Type:</b> ${debugInfo}<br>`;
        
        return hoverText;
    }

    createBpmTrace(bpmSeries) {
        return {
            x: bpmSeries.times,
            y: bpmSeries.bpm,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Heart Rate (BPM)',
            line: { 
                color: '#f56565',
                width: 2
            },
            marker: {
                color: '#f56565',
                size: 4
            },
            yaxis: 'y2',
            hovertemplate: 'Time: %{x:.2f}s<br>BPM: %{y:.1f}<extra></extra>'
        };
    }

    createHrvTrace(bpmSeries, hrvMetrics) {
        // Create a simplified HRV representation
        // This would need more sophisticated calculation for full accuracy
        if (!bpmSeries.times || bpmSeries.times.length < 10) {
            return null;
        }
        
        const hrvWindow = 20; // Points
        const hrvTimes = [];
        const hrvValues = [];
        
        for (let i = hrvWindow; i < bpmSeries.bpm.length; i += 5) {
            const windowStart = Math.max(0, i - hrvWindow);
            const windowData = bpmSeries.bpm.slice(windowStart, i);
            
            if (windowData.length > 2) {
                // Calculate RMSSD for this window
                const diffs = [];
                for (let j = 1; j < windowData.length; j++) {
                    diffs.push(Math.pow(windowData[j] - windowData[j-1], 2));
                }
                const rmssd = Math.sqrt(diffs.reduce((a, b) => a + b, 0) / diffs.length);
                
                hrvTimes.push(bpmSeries.times[i]);
                hrvValues.push(rmssd);
            }
        }
        
        if (hrvTimes.length === 0) return null;
        
        return {
            x: hrvTimes,
            y: hrvValues,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'HRV (RMSSD)',
            line: { 
                color: '#38b2ac',
                width: 2,
                dash: 'dashdot'
            },
            marker: {
                color: '#38b2ac',
                size: 3
            },
            yaxis: 'y2',
            visible: 'legendonly',
            hovertemplate: 'Time: %{x:.2f}s<br>HRV: %{y:.1f}<extra></extra>'
        };
    }

    createLayout(duration) {
        return {
            title: {
                text: 'Heartbeat Analysis - BPM and Signal Processing',
                font: { size: 18, color: '#2d3748' }
            },
            xaxis: {
                title: 'Time (seconds)',
                domain: [0, 1],
                tickformat: '.1f',
                hoverformat: '.2f',
                gridcolor: '#e2e8f0',
                zerolinecolor: '#cbd5e0'
            },
            yaxis: {
                title: 'Signal Amplitude',
                side: 'left',
                gridcolor: '#e2e8f0',
                zerolinecolor: '#cbd5e0'
            },
            yaxis2: {
                title: 'BPM / HRV',
                side: 'right',
                overlaying: 'y',
                range: [50, 200],
                gridcolor: 'rgba(226, 232, 240, 0.3)',
                zerolinecolor: 'rgba(203, 213, 224, 0.3)'
            },
            legend: {
                orientation: 'h',
                yanchor: 'bottom',
                y: 1.02,
                xanchor: 'right',
                x: 1,
                bgcolor: 'rgba(255, 255, 255, 0.8)',
                bordercolor: '#cbd5e0',
                borderwidth: 1
            },
            hovermode: 'x unified',
            margin: { t: 100, b: 60, l: 60, r: 60 },
            plot_bgcolor: '#f7fafc',
            paper_bgcolor: '#ffffff',
            dragmode: 'pan',
            height: 600
        };
    }

    // Utility method to format time for display
    formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = (seconds % 60).toFixed(1);
        return `${minutes}:${secs.padStart(4, '0')}`;
    }

    // Method to add annotations for significant events
    addAnnotations(layout, analysisResults) {
        if (!layout.annotations) {
            layout.annotations = [];
        }
        
        // Add peak BPM annotation
        if (analysisResults.peakBpm && analysisResults.bpmSeries) {
            const peakIndex = analysisResults.bpmSeries.bpm.indexOf(analysisResults.peakBpm);
            if (peakIndex !== -1) {
                layout.annotations.push({
                    x: analysisResults.bpmSeries.times[peakIndex],
                    y: analysisResults.peakBpm,
                    text: `Peak: ${analysisResults.peakBpm.toFixed(1)} BPM`,
                    showarrow: true,
                    arrowhead: 2,
                    arrowcolor: '#e53e3e',
                    bgcolor: 'rgba(255, 255, 255, 0.8)',
                    bordercolor: '#e53e3e',
                    borderwidth: 1,
                    yref: 'y2'
                });
            }
        }
        
        return layout;
    }
}