'use client';

import React, { useEffect, useRef } from 'react';
import { AnalysisResult } from '../lib/bpmAnalyzer';

// Dynamic import to avoid SSR issues
const Plot = React.lazy(() => import('react-plotly.js'));

interface BpmPlotProps {
  result: AnalysisResult;
}

export default function BpmPlot({ result }: BpmPlotProps) {
  const plotRef = useRef<HTMLDivElement>(null);

  const createPlotData = () => {
    const data: any[] = [];

    // Audio Envelope trace
    data.push({
      x: result.timeAxis,
      y: Array.from(result.audioEnvelope),
      type: 'scatter',
      mode: 'lines',
      name: 'Audio Envelope',
      line: { color: '#47a5c4', width: 1 },
      yaxis: 'y',
      hovertemplate: 'Time: %{x:.2f}s<br>Amplitude: %{y:.0f}<extra></extra>',
    });

    // Noise Floor trace
    data.push({
      x: result.timeAxis,
      y: Array.from(result.noiseFloor),
      type: 'scatter',
      mode: 'lines',
      name: 'Noise Floor',
      line: { color: 'green', width: 1, dash: 'dot' },
      yaxis: 'y',
      hovertemplate: 'Time: %{x:.2f}s<br>Noise Floor: %{y:.0f}<extra></extra>',
    });

    // S1 peaks (heartbeats)
    if (result.s1Peaks.length > 0) {
      const s1Times = result.s1Peaks.map(idx => result.timeAxis[idx]);
      const s1Amplitudes = result.s1Peaks.map(idx => result.audioEnvelope[idx]);
      
      data.push({
        x: s1Times,
        y: s1Amplitudes,
        type: 'scatter',
        mode: 'markers',
        name: 'S1 Peaks (Heartbeats)',
        marker: { 
          color: 'red', 
          size: 8,
          symbol: 'circle',
          line: { color: 'darkred', width: 1 }
        },
        yaxis: 'y',
        hovertemplate: 'S1 Peak<br>Time: %{x:.2f}s<br>Amplitude: %{y:.0f}<extra></extra>',
      });
    }

    // S2 peaks
    if (result.s2Peaks.length > 0) {
      const s2Times = result.s2Peaks.map(idx => result.timeAxis[idx]);
      const s2Amplitudes = result.s2Peaks.map(idx => result.audioEnvelope[idx]);
      
      data.push({
        x: s2Times,
        y: s2Amplitudes,
        type: 'scatter',
        mode: 'markers',
        name: 'S2 Peaks',
        marker: { 
          color: 'orange', 
          size: 6,
          symbol: 'triangle-up',
          line: { color: 'darkorange', width: 1 }
        },
        yaxis: 'y',
        hovertemplate: 'S2 Peak<br>Time: %{x:.2f}s<br>Amplitude: %{y:.0f}<extra></extra>',
      });
    }

    // Noise peaks
    if (result.noisePeaks.length > 0) {
      const noiseTimes = result.noisePeaks.map(idx => result.timeAxis[idx]);
      const noiseAmplitudes = result.noisePeaks.map(idx => result.audioEnvelope[idx]);
      
      data.push({
        x: noiseTimes,
        y: noiseAmplitudes,
        type: 'scatter',
        mode: 'markers',
        name: 'Noise/Rejected',
        marker: { 
          color: 'gray', 
          size: 4,
          symbol: 'x',
          line: { color: 'darkgray', width: 1 }
        },
        yaxis: 'y',
        visible: 'legendonly', // Hidden by default
        hovertemplate: 'Noise Peak<br>Time: %{x:.2f}s<br>Amplitude: %{y:.0f}<extra></extra>',
      });
    }

    // BPM series
    if (result.bpmSeries.length > 0) {
      data.push({
        x: result.bpmSeries.map(point => point.time),
        y: result.bpmSeries.map(point => point.bpm),
        type: 'scatter',
        mode: 'lines+markers',
        name: 'BPM Over Time',
        line: { color: '#e74c3c', width: 2 },
        marker: { size: 4, color: '#e74c3c' },
        yaxis: 'y2',
        hovertemplate: 'Time: %{x:.2f}s<br>BPM: %{y:.1f}<extra></extra>',
      });
    }

    return data;
  };

  const layout = {
    title: {
      text: `Heartbeat Analysis - ${result.audioFile}`,
      font: { size: 16, color: '#2c3e50' },
    },
    xaxis: {
      title: 'Time (seconds)',
      gridcolor: '#ecf0f1',
      showgrid: true,
    },
    yaxis: {
      title: 'Signal Amplitude',
      side: 'left',
      gridcolor: '#ecf0f1',
      showgrid: true,
    },
    yaxis2: {
      title: 'BPM',
      side: 'right',
      overlaying: 'y',
      range: [50, 200],
      gridcolor: 'rgba(236, 240, 241, 0.3)',
      showgrid: false,
    },
    legend: {
      orientation: 'h',
      yanchor: 'bottom',
      y: 1.02,
      xanchor: 'right',
      x: 1,
    },
    hovermode: 'x unified',
    template: 'plotly_white',
    margin: { t: 80, b: 60, l: 60, r: 60 },
    dragmode: 'pan',
    showlegend: true,
  };

  const config = {
    displayModeBar: true,
    modeBarButtonsToRemove: ['lasso2d', 'select2d'],
    displaylogo: false,
    toImageButtonOptions: {
      format: 'png',
      filename: `bpm_analysis_${result.audioFile}`,
      height: 600,
      width: 1200,
      scale: 2,
    },
    scrollZoom: true,
  };

  return (
    <div className="w-full">
      <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
        <React.Suspense 
          fallback={
            <div className="flex items-center justify-center h-96">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
              <span className="ml-2 text-gray-600 dark:text-gray-300">Loading interactive plot...</span>
            </div>
          }
        >
          <Plot
            data={createPlotData()}
            layout={layout}
            config={config}
            style={{ width: '100%', height: '500px' }}
            useResizeHandler={true}
          />
        </React.Suspense>
        
        {/* Plot Instructions */}
        <div className="mt-4 p-4 bg-blue-50 dark:bg-blue-900/30 rounded-lg">
          <h4 className="font-semibold text-blue-900 dark:text-blue-100 mb-2">Interactive Plot Guide:</h4>
          <div className="text-sm text-blue-800 dark:text-blue-200 space-y-1">
            <p>• <strong>Zoom:</strong> Scroll wheel or box select to zoom in/out</p>
            <p>• <strong>Pan:</strong> Click and drag to move around the plot</p>
            <p>• <strong>Reset:</strong> Double-click to reset zoom</p>
            <p>• <strong>Legend:</strong> Click legend items to show/hide traces</p>
            <p>• <strong>Red circles:</strong> S1 peaks (main heartbeats)</p>
            <p>• <strong>Orange triangles:</strong> S2 peaks (secondary heart sounds)</p>
            <p>• <strong>Red line (right axis):</strong> BPM over time</p>
          </div>
        </div>
      </div>
    </div>
  );
}