'use client';

import { useState } from 'react';
import { Upload, Activity, BarChart3, FileAudio, Heart, TrendingUp } from 'lucide-react';
import { BpmAnalyzer, AnalysisResult } from './lib/bpmAnalyzer';
import BpmPlot from './components/BpmPlot';
import TestInfo from './components/TestInfo';

export default function Home() {
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [analysisProgress, setAnalysisProgress] = useState<string>('');

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    // Validate file type
    if (!file.type.startsWith('audio/')) {
      setError('Please select an audio file (WAV, MP3, M4A, etc.)');
      return;
    }

    setIsAnalyzing(true);
    setError(null);
    setAnalysisResult(null);
    setAnalysisProgress('Initializing audio processing...');

    try {
      const analyzer = new BpmAnalyzer();
      
      // Update progress during analysis
      const updateProgress = (stage: string) => {
        setAnalysisProgress(stage);
      };

      // Perform the actual BPM analysis
      setAnalysisProgress('Processing audio file...');
      const result = await analyzer.analyze(file);
      
      setAnalysisProgress('Analysis complete!');
      setAnalysisResult(result);
      console.log('Analysis complete:', result);
      
    } catch (err) {
      console.error('Analysis error:', err);
      setError(`Failed to analyze audio file: ${err instanceof Error ? err.message : 'Unknown error'}`);
    } finally {
      setIsAnalyzing(false);
      setAnalysisProgress('');
    }
  };

  const resetAnalysis = () => {
    setAnalysisResult(null);
    setError(null);
    // Reset file input
    const fileInput = document.getElementById('audio-upload') as HTMLInputElement;
    if (fileInput) fileInput.value = '';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-blue-900">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Activity className="w-8 h-8 text-blue-600 dark:text-blue-400" />
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white">
              Heartbeat BPM Analyzer
            </h1>
          </div>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            Upload your audio file and get accurate heart rate analysis with advanced signal processing.
            Detects S1/S2 heart sounds and calculates BPM with heart rate variability metrics.
          </p>
        </header>

        {/* Main Content */}
        <div className="max-w-6xl mx-auto">
          {/* Upload Section */}
          {!analysisResult && (
            <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
              <div className="text-center">
                <FileAudio className="w-16 h-16 text-blue-500 mx-auto mb-4" />
                <h2 className="text-2xl font-semibold text-gray-900 dark:text-white mb-4">
                  Upload Audio File
                </h2>
                
                <div className="border-2 border-dashed border-blue-300 dark:border-blue-600 rounded-xl p-8 hover:border-blue-400 transition-colors">
                  <input
                    type="file"
                    accept="audio/*"
                    onChange={handleFileUpload}
                    className="hidden"
                    id="audio-upload"
                    disabled={isAnalyzing}
                  />
                  <label
                    htmlFor="audio-upload"
                    className="cursor-pointer flex flex-col items-center gap-4"
                  >
                    <Upload className="w-12 h-12 text-blue-500" />
                    <div>
                      <p className="text-lg font-medium text-gray-700 dark:text-gray-300">
                        {isAnalyzing ? analysisProgress || 'Analyzing...' : 'Click to upload audio file'}
                      </p>
                      <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                        Supports WAV, MP3, M4A, and other audio formats
                      </p>
                      <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                        Best results with clear heart sound recordings
                      </p>
                    </div>
                  </label>
                </div>
              </div>
            </div>
          )}

          {/* Error Message */}
          {error && (
            <div className="bg-red-50 dark:bg-red-900/30 border border-red-200 dark:border-red-700 rounded-xl p-4 mb-8">
              <p className="text-red-700 dark:text-red-300">{error}</p>
            </div>
          )}

          {/* Loading State */}
          {isAnalyzing && (
            <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 mb-8">
              <div className="text-center">
                <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-blue-600 mx-auto mb-4"></div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
                  Analyzing Audio...
                </h3>
                <p className="text-gray-600 dark:text-gray-300 mt-2">
                  {analysisProgress || 'Processing audio signal and detecting heartbeats'}
                </p>
                <div className="mt-4 text-sm text-gray-500 dark:text-gray-400">
                  <p>• Filtering audio signal (20-150 Hz)</p>
                  <p>• Calculating noise floor and envelope</p>
                  <p>• Detecting and classifying peaks</p>
                  <p>• Computing BPM and HRV metrics</p>
                </div>
              </div>
            </div>
          )}

          {/* Results Section */}
          {analysisResult && (
            <div className="space-y-8">
              {/* Summary Cards */}
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div className="text-center p-6 bg-blue-50 dark:bg-blue-900/30 rounded-xl">
                  <Heart className="w-8 h-8 text-blue-600 dark:text-blue-400 mx-auto mb-2" />
                  <div className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">
                    {analysisResult.bpm}
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Average BPM
                  </div>
                </div>
                
                <div className="text-center p-6 bg-green-50 dark:bg-green-900/30 rounded-xl">
                  <TrendingUp className="w-8 h-8 text-green-600 dark:text-green-400 mx-auto mb-2" />
                  <div className="text-3xl font-bold text-green-600 dark:text-green-400 mb-2">
                    {Math.round(analysisResult.confidence * 100)}%
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Confidence Score
                  </div>
                </div>
                
                <div className="text-center p-6 bg-purple-50 dark:bg-purple-900/30 rounded-xl">
                  <Activity className="w-8 h-8 text-purple-600 dark:text-purple-400 mx-auto mb-2" />
                  <div className="text-3xl font-bold text-purple-600 dark:text-purple-400 mb-2">
                    {analysisResult.s1Peaks.length}
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Heartbeats Detected
                  </div>
                </div>

                <div className="text-center p-6 bg-orange-50 dark:bg-orange-900/30 rounded-xl">
                  <BarChart3 className="w-8 h-8 text-orange-600 dark:text-orange-400 mx-auto mb-2" />
                  <div className="text-3xl font-bold text-orange-600 dark:text-orange-400 mb-2">
                    {(analysisResult.timeAxis[analysisResult.timeAxis.length - 1]).toFixed(1)}s
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Duration
                  </div>
                </div>
              </div>

              {/* HRV Metrics */}
              {analysisResult.hrvMetrics && (
                <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-6">
                  <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
                    <Heart className="w-5 h-5 text-red-500" />
                    Heart Rate Variability Metrics
                  </h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-1">
                        {analysisResult.hrvMetrics.minBpm.toFixed(0)}
                      </div>
                      <div className="text-sm text-gray-600 dark:text-gray-400">Min BPM</div>
                    </div>
                    <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-1">
                        {analysisResult.hrvMetrics.maxBpm.toFixed(0)}
                      </div>
                      <div className="text-sm text-gray-600 dark:text-gray-400">Max BPM</div>
                    </div>
                    <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-1">
                        {analysisResult.hrvMetrics.rmssd.toFixed(1)}
                      </div>
                      <div className="text-sm text-gray-600 dark:text-gray-400">RMSSD (ms)</div>
                    </div>
                    <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                      <div className="text-2xl font-bold text-gray-700 dark:text-gray-300 mb-1">
                        {analysisResult.hrvMetrics.sdnn.toFixed(1)}
                      </div>
                      <div className="text-sm text-gray-600 dark:text-gray-400">SDNN (ms)</div>
                    </div>
                  </div>
                </div>
              )}

              {/* Interactive Plot */}
              <BpmPlot result={analysisResult} />

              {/* Action Buttons */}
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <button
                  onClick={resetAnalysis}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-xl transition-colors"
                >
                  Analyze Another File
                </button>
                <button
                  onClick={() => {
                    const dataStr = JSON.stringify(analysisResult, null, 2);
                    const dataBlob = new Blob([dataStr], { type: 'application/json' });
                    const url = URL.createObjectURL(dataBlob);
                    const link = document.createElement('a');
                    link.href = url;
                    link.download = `bpm_analysis_${analysisResult.audioFile}.json`;
                    link.click();
                    URL.revokeObjectURL(url);
                  }}
                  className="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-xl transition-colors"
                >
                  Export Results (JSON)
                </button>
              </div>
            </div>
          )}

          {/* Test Info Section */}
          {!analysisResult && !isAnalyzing && (
            <div className="mb-8">
              <TestInfo />
            </div>
          )}

          {/* Features Section */}
          {!analysisResult && !isAnalyzing && (
            <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="text-center p-6">
                <Activity className="w-8 h-8 text-blue-500 mx-auto mb-3" />
                <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                  Advanced Detection
                </h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm">
                  Sophisticated S1/S2 heart sound detection with noise filtering and peak classification
                </p>
              </div>
              
              <div className="text-center p-6">
                <Heart className="w-8 h-8 text-red-500 mx-auto mb-3" />
                <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                  HRV Analysis
                </h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm">
                  Calculate heart rate variability metrics including RMSSD and SDNN
                </p>
              </div>
              
              <div className="text-center p-6">
                <BarChart3 className="w-8 h-8 text-purple-500 mx-auto mb-3" />
                <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                  Interactive Visualization
                </h3>
                <p className="text-gray-600 dark:text-gray-300 text-sm">
                  Explore your data with zoomable plots showing signal, peaks, and BPM over time
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
