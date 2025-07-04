'use client';

import React from 'react';
import { AnalysisResult } from '@/lib/types';
import { Heart, Activity, TrendingDown, BarChart } from 'lucide-react';

interface AnalysisResultsProps {
  analysisResult: AnalysisResult;
}

export default function AnalysisResults({ analysisResult }: AnalysisResultsProps) {
  const { final_metrics } = analysisResult;
  const { hrv_summary, hrr_stats } = final_metrics;

  const formatTime = (seconds: number): string => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  };

  return (
    <div className="space-y-8">
      {/* HRV Analysis */}
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center mb-6">
          <Activity className="w-6 h-6 text-green-500 mr-2" />
          <h2 className="text-2xl font-semibold text-gray-800">Heart Rate Variability (HRV)</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">Mean RR Interval</h3>
            <p className="text-2xl font-bold text-gray-800">
              {(hrv_summary.mean_rr * 1000).toFixed(0)} ms
            </p>
            <p className="text-xs text-gray-500 mt-1">Average time between heartbeats</p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">RMSSD</h3>
            <p className="text-2xl font-bold text-gray-800">
              {(hrv_summary.rmssd * 1000).toFixed(1)} ms
            </p>
            <p className="text-xs text-gray-500 mt-1">Root mean square of successive differences</p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">pNN50</h3>
            <p className="text-2xl font-bold text-gray-800">
              {hrv_summary.pnn50.toFixed(1)}%
            </p>
                         <p className="text-xs text-gray-500 mt-1">Percentage of adjacent intervals differing by &gt;50ms</p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">Triangular Index</h3>
            <p className="text-2xl font-bold text-gray-800">
              {hrv_summary.triangular_index.toFixed(0)}
            </p>
            <p className="text-xs text-gray-500 mt-1">Geometric measure of HRV</p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">Sample Entropy</h3>
            <p className="text-2xl font-bold text-gray-800">
              {hrv_summary.sample_entropy.toFixed(2)}
            </p>
            <p className="text-xs text-gray-500 mt-1">Measure of time series regularity</p>
          </div>
        </div>
        
        <div className="mt-6 p-4 bg-blue-50 rounded-lg">
          <h4 className="font-medium text-blue-800 mb-2">HRV Interpretation</h4>
          <p className="text-sm text-blue-700">
            Higher HRV values generally indicate better cardiovascular health and autonomic nervous system function. 
            RMSSD values above 30ms are considered healthy for most adults.
          </p>
        </div>
      </div>

      {/* Heart Rate Recovery */}
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center mb-6">
          <TrendingDown className="w-6 h-6 text-blue-500 mr-2" />
          <h2 className="text-2xl font-semibold text-gray-800">Heart Rate Recovery (HRR)</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">Peak BPM</h3>
            <p className="text-2xl font-bold text-red-500">
              {hrr_stats.peak_bpm.toFixed(0)}
            </p>
            <p className="text-xs text-gray-500 mt-1">
              At {formatTime(hrr_stats.peak_time)}
            </p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">1-Minute Recovery</h3>
            <p className="text-2xl font-bold text-blue-500">
              {hrr_stats.recovery_rate_1min.toFixed(0)} BPM
            </p>
            <p className="text-xs text-gray-500 mt-1">
              {hrr_stats.recovery_percentage_1min.toFixed(1)}% recovery
            </p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">2-Minute Recovery</h3>
            <p className="text-2xl font-bold text-green-500">
              {hrr_stats.recovery_rate_2min.toFixed(0)} BPM
            </p>
            <p className="text-xs text-gray-500 mt-1">
              {hrr_stats.recovery_percentage_2min.toFixed(1)}% recovery
            </p>
          </div>
          
          <div className="bg-gray-50 rounded-lg p-4">
            <h3 className="text-sm font-medium text-gray-600 mb-2">Total Beats</h3>
            <p className="text-2xl font-bold text-purple-500">
              {analysisResult.final_peaks.length}
            </p>
            <p className="text-xs text-gray-500 mt-1">Detected heartbeats</p>
          </div>
        </div>
        
        <div className="mt-6 p-4 bg-green-50 rounded-lg">
          <h4 className="font-medium text-green-800 mb-2">HRR Interpretation</h4>
          <p className="text-sm text-green-700">
            Good heart rate recovery indicates cardiovascular fitness. A drop of 12+ BPM in the first minute 
            and 20+ BPM in the first two minutes is considered healthy.
          </p>
        </div>
      </div>

      {/* Technical Details */}
      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center mb-6">
          <BarChart className="w-6 h-6 text-purple-500 mr-2" />
          <h2 className="text-2xl font-semibold text-gray-800">Technical Details</h2>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 className="text-lg font-medium text-gray-800 mb-3">Analysis Summary</h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-600">Sample Rate:</span>
                <span className="font-medium">{analysisResult.sample_rate.toFixed(0)} Hz</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Total Raw Peaks:</span>
                <span className="font-medium">{analysisResult.all_raw_peaks.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Valid Heartbeats:</span>
                <span className="font-medium">{analysisResult.final_peaks.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Acceptance Rate:</span>
                <span className="font-medium">
                  {((analysisResult.final_peaks.length / analysisResult.all_raw_peaks.length) * 100).toFixed(1)}%
                </span>
              </div>
            </div>
          </div>
          
          <div>
            <h3 className="text-lg font-medium text-gray-800 mb-3">Peak Classification</h3>
            <div className="space-y-2 text-sm">
                             {Object.entries(
                 Object.entries(analysisResult.analysis_data.beat_debug_info).reduce((acc, [peakIdx, info]) => {
                   const type = (info as string).split('§')[0];
                   acc[type] = (acc[type] || 0) + 1;
                   return acc;
                 }, {} as Record<string, number>)
               ).map(([type, count]) => (
                <div key={type} className="flex justify-between">
                  <span className="text-gray-600">{type}:</span>
                  <span className="font-medium">{count}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}