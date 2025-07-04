'use client';

import { useState } from 'react';
import { Upload, Activity, BarChart3, FileAudio } from 'lucide-react';

interface AnalysisResult {
  bpm: number;
  confidence: number;
  audioFile: string;
}

export default function Home() {
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    // Validate file type
    if (!file.type.startsWith('audio/')) {
      setError('Please select an audio file');
      return;
    }

    setIsAnalyzing(true);
    setError(null);

    try {
      // TODO: Implement actual BPM analysis
      // For now, simulate analysis with random result
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      const mockResult: AnalysisResult = {
        bpm: Math.floor(Math.random() * (180 - 60) + 60),
        confidence: Math.random() * 0.4 + 0.6, // 60-100% confidence
        audioFile: file.name
      };

      setAnalysisResult(mockResult);
    } catch (err) {
      setError('Failed to analyze audio file');
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-blue-900">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Activity className="w-8 h-8 text-blue-600 dark:text-blue-400" />
            <h1 className="text-4xl font-bold text-gray-900 dark:text-white">
              BPM Analyzer
            </h1>
          </div>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            Upload your audio file and get accurate BPM analysis with advanced signal processing techniques.
            Perfect for musicians, DJs, and audio enthusiasts.
          </p>
        </header>

        {/* Main Content */}
        <div className="max-w-4xl mx-auto">
          {/* Upload Section */}
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
                      {isAnalyzing ? 'Analyzing...' : 'Click to upload audio file'}
                    </p>
                    <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                      Supports MP3, WAV, M4A, and other audio formats
                    </p>
                  </div>
                </label>
              </div>
            </div>
          </div>

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
                  Processing audio signal and detecting beats
                </p>
              </div>
            </div>
          )}

          {/* Results Section */}
          {analysisResult && (
            <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
              <div className="flex items-center gap-3 mb-6">
                <BarChart3 className="w-6 h-6 text-green-600" />
                <h3 className="text-2xl font-semibold text-gray-900 dark:text-white">
                  Analysis Results
                </h3>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div className="text-center p-6 bg-blue-50 dark:bg-blue-900/30 rounded-xl">
                  <div className="text-3xl font-bold text-blue-600 dark:text-blue-400 mb-2">
                    {analysisResult.bpm}
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    BPM (Beats Per Minute)
                  </div>
                </div>
                
                <div className="text-center p-6 bg-green-50 dark:bg-green-900/30 rounded-xl">
                  <div className="text-3xl font-bold text-green-600 dark:text-green-400 mb-2">
                    {Math.round(analysisResult.confidence * 100)}%
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Confidence Score
                  </div>
                </div>
                
                <div className="text-center p-6 bg-purple-50 dark:bg-purple-900/30 rounded-xl">
                  <div className="text-lg font-bold text-purple-600 dark:text-purple-400 mb-2 truncate">
                    {analysisResult.audioFile}
                  </div>
                  <div className="text-gray-600 dark:text-gray-300 font-medium">
                    Analyzed File
                  </div>
                </div>
              </div>

              <div className="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
                <button
                  onClick={() => setAnalysisResult(null)}
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-6 rounded-xl transition-colors"
                >
                  Analyze Another File
                </button>
              </div>
            </div>
          )}

          {/* Features Section */}
          <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center p-6">
              <Activity className="w-8 h-8 text-blue-500 mx-auto mb-3" />
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                Accurate Detection
              </h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                Advanced signal processing algorithms for precise BPM detection
              </p>
            </div>
            
            <div className="text-center p-6">
              <FileAudio className="w-8 h-8 text-green-500 mx-auto mb-3" />
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                Multiple Formats
              </h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                Support for MP3, WAV, M4A and other popular audio formats
              </p>
            </div>
            
            <div className="text-center p-6">
              <BarChart3 className="w-8 h-8 text-purple-500 mx-auto mb-3" />
              <h3 className="font-semibold text-gray-900 dark:text-white mb-2">
                Real-time Analysis
              </h3>
              <p className="text-gray-600 dark:text-gray-300 text-sm">
                Fast client-side processing with instant results
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
