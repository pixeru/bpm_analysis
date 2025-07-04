'use client';

import React from 'react';
import { Info, Download, FileAudio, AlertCircle } from 'lucide-react';

export default function TestInfo() {
  const generateTestTone = () => {
    // Create a simple test audio file in the browser
    const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
    const sampleRate = audioContext.sampleRate;
    const duration = 10; // 10 seconds
    const length = sampleRate * duration;
    
    // Create a buffer
    const audioBuffer = audioContext.createBuffer(1, length, sampleRate);
    const channelData = audioBuffer.getChannelData(0);
    
    // Generate a synthetic heartbeat pattern
    const bpm = 75; // 75 BPM
    const beatInterval = 60 / bpm; // seconds between beats
    const s1Duration = 0.1; // S1 duration in seconds
    const s2Duration = 0.08; // S2 duration in seconds
    const s1S2Delay = 0.3; // delay between S1 and S2
    
    for (let i = 0; i < length; i++) {
      const time = i / sampleRate;
      const beatPhase = (time % beatInterval) / beatInterval;
      
      let amplitude = 0;
      
      // Generate S1 sound (lub)
      if (beatPhase < s1Duration / beatInterval) {
        const s1Phase = beatPhase / (s1Duration / beatInterval);
        amplitude = Math.sin(s1Phase * Math.PI) * 0.5 * Math.sin(2 * Math.PI * 40 * time);
      }
      
      // Generate S2 sound (dub)
      const s2Start = s1S2Delay / beatInterval;
      const s2End = s2Start + (s2Duration / beatInterval);
      if (beatPhase >= s2Start && beatPhase < s2End) {
        const s2Phase = (beatPhase - s2Start) / (s2Duration / beatInterval);
        amplitude = Math.sin(s2Phase * Math.PI) * 0.3 * Math.sin(2 * Math.PI * 60 * time);
      }
      
      // Add some subtle noise
      amplitude += (Math.random() - 0.5) * 0.05;
      
      channelData[i] = amplitude;
    }
    
    // Convert to WAV file
    const wavData = audioBufferToWav(audioBuffer);
    const blob = new Blob([wavData], { type: 'audio/wav' });
    const url = URL.createObjectURL(blob);
    
    // Download the file
    const link = document.createElement('a');
    link.href = url;
    link.download = 'test_heartbeat_75bpm.wav';
    link.click();
    
    URL.revokeObjectURL(url);
  };

  return (
    <div className="bg-amber-50 dark:bg-amber-900/30 border border-amber-200 dark:border-amber-700 rounded-xl p-6">
      <div className="flex items-start gap-3">
        <Info className="w-5 h-5 text-amber-600 dark:text-amber-400 mt-0.5 flex-shrink-0" />
        <div className="flex-1">
          <h3 className="font-semibold text-amber-800 dark:text-amber-200 mb-2">
            Testing the BPM Analyzer
          </h3>
          <div className="text-amber-700 dark:text-amber-300 text-sm space-y-2">
            <p>
              To test this application, you'll need an audio file containing heart sounds. Here are your options:
            </p>
            
            <div className="space-y-3 mt-4">
              <div className="flex items-center gap-2">
                <Download className="w-4 h-4" />
                <span className="font-medium">Option 1: Generate Test Audio</span>
              </div>
              <p className="text-xs ml-6">
                Click below to generate a synthetic heartbeat audio file (75 BPM) for testing:
              </p>
              <button
                onClick={generateTestTone}
                className="ml-6 bg-amber-600 hover:bg-amber-700 text-white text-sm px-4 py-2 rounded-lg transition-colors flex items-center gap-2"
              >
                <FileAudio className="w-4 h-4" />
                Generate Test Heartbeat (10s, 75 BPM)
              </button>
              
              <div className="flex items-center gap-2 mt-4">
                <AlertCircle className="w-4 h-4" />
                <span className="font-medium">Option 2: Use Real Heart Sound Recordings</span>
              </div>
              <p className="text-xs ml-6">
                For best results, use:
              </p>
              <ul className="text-xs ml-6 space-y-1 list-disc list-inside">
                <li>Clear recordings of heart sounds (stethoscope recordings work well)</li>
                <li>WAV format preferred, but MP3/M4A also supported</li>
                <li>30-120 seconds duration</li>
                <li>Minimal background noise</li>
                <li>Sample rate of 44.1 kHz or higher</li>
              </ul>
              
              <div className="mt-4 p-3 bg-amber-100 dark:bg-amber-800/50 rounded-lg">
                <p className="text-xs font-medium">
                  💡 Tip: Medical teaching websites often have sample heart sound recordings you can download for testing purposes.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// Utility function to convert AudioBuffer to WAV format
function audioBufferToWav(audioBuffer: AudioBuffer): ArrayBuffer {
  const numChannels = audioBuffer.numberOfChannels;
  const sampleRate = audioBuffer.sampleRate;
  const format = 1; // PCM
  const bitDepth = 16;
  
  const length = audioBuffer.length;
  const arrayBuffer = new ArrayBuffer(44 + length * numChannels * 2);
  const view = new DataView(arrayBuffer);
  
  // WAV header
  const writeString = (offset: number, string: string) => {
    for (let i = 0; i < string.length; i++) {
      view.setUint8(offset + i, string.charCodeAt(i));
    }
  };
  
  writeString(0, 'RIFF');
  view.setUint32(4, 36 + length * numChannels * 2, true);
  writeString(8, 'WAVE');
  writeString(12, 'fmt ');
  view.setUint32(16, 16, true);
  view.setUint16(20, format, true);
  view.setUint16(22, numChannels, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * numChannels * 2, true);
  view.setUint16(32, numChannels * 2, true);
  view.setUint16(34, bitDepth, true);
  writeString(36, 'data');
  view.setUint32(40, length * numChannels * 2, true);
  
  // Convert audio data
  let offset = 44;
  for (let i = 0; i < length; i++) {
    for (let channel = 0; channel < numChannels; channel++) {
      const sample = Math.max(-1, Math.min(1, audioBuffer.getChannelData(channel)[i]));
      view.setInt16(offset, sample * 0x7FFF, true);
      offset += 2;
    }
  }
  
  return arrayBuffer;
}