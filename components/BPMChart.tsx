'use client';

import React, { useMemo } from 'react';
import dynamic from 'next/dynamic';
import { AnalysisResult, PeakType } from '@/lib/types';

// Dynamically import Plotly to avoid SSR issues
const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });

interface BPMChartProps {
  analysisResult: AnalysisResult;
}

export default function BPMChart({ analysisResult }: BPMChartProps) {
  const plotData = useMemo(() => {
    const {
      audio_envelope,
      all_raw_peaks,
      final_peaks,
      analysis_data,
      final_metrics,
      sample_rate
    } = analysisResult;

    // Create time axis (in seconds)
    const timeAxis = audio_envelope.map((_, index) => index / sample_rate);
    
    // Downsample audio envelope for better performance if it's too large
    let plotTimeAxis = timeAxis;
    let plotEnvelope = audio_envelope;
    
    if (audio_envelope.length > 5000) {
      const downsampleFactor = Math.ceil(audio_envelope.length / 5000);
      plotTimeAxis = timeAxis.filter((_, index) => index % downsampleFactor === 0);
      plotEnvelope = audio_envelope.filter((_, index) => index % downsampleFactor === 0);
    }

    const traces: any[] = [];

    // Audio envelope trace
    traces.push({
      x: plotTimeAxis,
      y: plotEnvelope,
      type: 'scatter',
      mode: 'lines',
      name: 'Audio Envelope',
      line: { color: '#47a5c4', width: 1 },
      yaxis: 'y1'
    });

    // Dynamic noise floor trace
    if (analysis_data.dynamic_noise_floor_series.length > 0) {
      let noiseFloorTime = plotTimeAxis;
      let noiseFloorData = analysis_data.dynamic_noise_floor_series;
      
      // Match noise floor length to envelope
      if (noiseFloorData.length !== plotEnvelope.length) {
        const ratio = noiseFloorData.length / plotEnvelope.length;
        noiseFloorTime = plotTimeAxis;
        noiseFloorData = plotTimeAxis.map((_, i) => {
          const noiseIndex = Math.floor(i * ratio);
          return analysis_data.dynamic_noise_floor_series[Math.min(noiseIndex, analysis_data.dynamic_noise_floor_series.length - 1)];
        });
      }

      traces.push({
        x: noiseFloorTime,
        y: noiseFloorData,
        type: 'scatter',
        mode: 'lines',
        name: 'Dynamic Noise Floor',
        line: { color: 'green', width: 1, dash: 'dot' },
        yaxis: 'y1'
      });
    }

    // Peak markers by type
    const peaksByType = {
      s1_peaks: { indices: [] as Array<{x: number, y: number, peakIdx: number}>, colors: [] as string[] },
      s2_peaks: { indices: [] as Array<{x: number, y: number, peakIdx: number}>, colors: [] as string[] },
      noise_peaks: { indices: [] as Array<{x: number, y: number, peakIdx: number}>, colors: [] as string[] }
    };

    // Classify peaks by their debug info
    all_raw_peaks.forEach(peakIdx => {
      const debugInfo = analysis_data.beat_debug_info[peakIdx] || '';
      const time = peakIdx / sample_rate;
      const amplitude = audio_envelope[peakIdx] || 0;

      if (debugInfo.includes(PeakType.S1_PAIRED) || debugInfo.includes('Lone S1')) {
        peaksByType.s1_peaks.indices.push({ x: time, y: amplitude, peakIdx });
        peaksByType.s1_peaks.colors.push('#ff6b6b');
      } else if (debugInfo.includes(PeakType.S2_PAIRED)) {
        peaksByType.s2_peaks.indices.push({ x: time, y: amplitude, peakIdx });
        peaksByType.s2_peaks.colors.push('#4ecdc4');
      } else {
        peaksByType.noise_peaks.indices.push({ x: time, y: amplitude, peakIdx });
        peaksByType.noise_peaks.colors.push('#ffa726');
      }
    });

    // Add S1 peaks
    if (peaksByType.s1_peaks.indices.length > 0) {
      traces.push({
        x: peaksByType.s1_peaks.indices.map(p => p.x),
        y: peaksByType.s1_peaks.indices.map(p => p.y),
        type: 'scatter',
        mode: 'markers',
        name: 'S1 Peaks',
        marker: {
          color: '#ff6b6b',
          size: 8,
          symbol: 'circle'
        },
        text: peaksByType.s1_peaks.indices.map(p => {
          const debugInfo = analysis_data.beat_debug_info[p.peakIdx] || '';
          return `S1 Peak<br>Time: ${p.x.toFixed(2)}s<br>Amplitude: ${p.y.toFixed(0)}<br>Details: ${debugInfo.split('§')[0]}`;
        }),
        hovertemplate: '%{text}<extra></extra>',
        yaxis: 'y1'
      });
    }

    // Add S2 peaks
    if (peaksByType.s2_peaks.indices.length > 0) {
      traces.push({
        x: peaksByType.s2_peaks.indices.map(p => p.x),
        y: peaksByType.s2_peaks.indices.map(p => p.y),
        type: 'scatter',
        mode: 'markers',
        name: 'S2 Peaks',
        marker: {
          color: '#4ecdc4',
          size: 8,
          symbol: 'circle'
        },
        text: peaksByType.s2_peaks.indices.map(p => {
          const debugInfo = analysis_data.beat_debug_info[p.peakIdx] || '';
          return `S2 Peak<br>Time: ${p.x.toFixed(2)}s<br>Amplitude: ${p.y.toFixed(0)}<br>Details: ${debugInfo.split('§')[0]}`;
        }),
        hovertemplate: '%{text}<extra></extra>',
        yaxis: 'y1'
      });
    }

    // Add noise peaks (initially hidden)
    if (peaksByType.noise_peaks.indices.length > 0) {
      traces.push({
        x: peaksByType.noise_peaks.indices.map(p => p.x),
        y: peaksByType.noise_peaks.indices.map(p => p.y),
        type: 'scatter',
        mode: 'markers',
        name: 'Noise/Rejected',
        marker: {
          color: '#ffa726',
          size: 6,
          symbol: 'circle-open'
        },
        text: peaksByType.noise_peaks.indices.map(p => {
          const debugInfo = analysis_data.beat_debug_info[p.peakIdx] || '';
          return `Noise Peak<br>Time: ${p.x.toFixed(2)}s<br>Amplitude: ${p.y.toFixed(0)}<br>Details: ${debugInfo.split('§')[0]}`;
        }),
        hovertemplate: '%{text}<extra></extra>',
        visible: 'legendonly',
        yaxis: 'y1'
      });
    }

    // Add BPM trace
    if (final_metrics.smoothed_bpm.length > 0 && final_metrics.bpm_times.length > 0) {
      traces.push({
                 x: final_metrics.bpm_times,
        y: final_metrics.smoothed_bpm,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'BPM',
        line: { color: '#e74c3c', width: 2 },
        marker: { size: 4 },
        yaxis: 'y2'
      });
    }

    return traces;
  }, [analysisResult]);

  const layout = useMemo(() => {
    const maxTime = analysisResult.audio_envelope.length / analysisResult.sample_rate;
    const maxAmplitude = Math.max(...analysisResult.audio_envelope) * 1.1;
    
    return {
      title: {
        text: 'Heartbeat Analysis Results',
        font: { size: 18 }
      },
      xaxis: {
        title: 'Time (seconds)',
        gridcolor: '#f0f0f0'
      },
      yaxis: {
        title: 'Signal Amplitude',
        side: 'left',
        range: [0, maxAmplitude],
        gridcolor: '#f0f0f0'
      },
      yaxis2: {
        title: 'BPM',
        side: 'right',
        overlaying: 'y',
        range: [40, 200],
        gridcolor: '#f0f0f0'
      },
      hovermode: 'x unified',
      legend: {
        orientation: 'h',
        y: 1.02,
        x: 0.5,
        xanchor: 'center'
      },
      margin: { t: 80, b: 60, l: 60, r: 60 },
      plot_bgcolor: '#fafafa',
      paper_bgcolor: 'white',
      height: 500
    };
  }, [analysisResult]);

  const config = {
    displayModeBar: true,
    modeBarButtonsToRemove: ['lasso2d', 'select2d'],
    displaylogo: false,
    scrollZoom: true,
    responsive: true
  };

  return (
    <div className="w-full">
      <Plot
        data={plotData}
        layout={layout}
        config={config}
        style={{ width: '100%', height: '500px' }}
        useResizeHandler={true}
      />
    </div>
  );
}