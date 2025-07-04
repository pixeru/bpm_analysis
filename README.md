# Heartbeat BPM Analyzer - Web Version

A sophisticated client-side web application for analyzing heartbeat patterns from audio recordings. This is a JavaScript/TypeScript port of the original Python BPM analysis tool, running entirely in your browser with no server required.

## Features

### 🎯 **Advanced Heartbeat Detection**

- **S1/S2 Peak Classification**: Sophisticated algorithm to distinguish between S1 (systolic) and S2 (diastolic) heart sounds
- **Dynamic Noise Floor**: Adaptive background noise filtering for improved accuracy
- **Rhythm Validation**: Intelligent validation of beat-to-beat timing consistency
- **Cascade Reset Mechanism**: Automatic recovery from analysis errors

### 📊 **Comprehensive Metrics**

- **Heart Rate Variability (HRV)**: RMSSD, pNN50, triangular index, sample entropy
- **Heart Rate Recovery (HRR)**: 1-minute and 2-minute recovery rates
- **BPM Tracking**: Real-time BPM calculation with smoothing
- **Peak Statistics**: Detailed classification of all detected peaks

### 🔒 **Privacy & Security**

- **100% Client-Side**: All processing happens in your browser
- **No Data Upload**: Your audio files never leave your device
- **No Server Required**: Can be used offline after initial load

### 🎨 **Interactive Visualization**

- **Plotly.js Charts**: Interactive, zoomable plots with hover details
- **Peak Markers**: Color-coded S1, S2, and noise peaks
- **Dual Y-Axis**: Signal amplitude and BPM on the same chart
- **Export Capable**: Built-in plot export functionality

## Supported Audio Formats

- **WAV** (recommended for best accuracy)
- **MP3**
- **M4A**
- **FLAC**
- **OGG**

## Usage Instructions

### 1. Start the Application

```bash
npm run dev
```

### 2. Upload Audio File

- Drag and drop an audio file onto the upload area, or
- Click "Choose File" to browse for a file
- Optionally provide a starting BPM hint for improved accuracy

### 3. View Results

The analysis will provide:

- **Summary Cards**: Peak BPM, average BPM, total beats, duration
- **Interactive Chart**: Signal waveform with classified peaks and BPM overlay
- **HRV Analysis**: Comprehensive heart rate variability metrics
- **HRR Analysis**: Heart rate recovery statistics
- **Technical Details**: Peak classification breakdown and analysis parameters

## Technical Implementation

### Core Analysis Engine

The application implements the same sophisticated algorithm as the original Python version:

1. **Audio Preprocessing**: Bandpass filtering and envelope extraction
2. **Dynamic Noise Floor**: Rolling quantile-based noise estimation
3. **Peak Detection**: Prominence and distance-based peak finding
4. **S1/S2 Classification**:
   - Amplitude deviation analysis
   - Physiological timing constraints
   - Stability-based confidence scoring
   - Interval penalty system
5. **Rhythm Validation**: Long-term BPM belief system with learning rate
6. **Quality Control**: Cascade reset for error recovery

### Technology Stack

- **Frontend**: Next.js 14, React 18, TypeScript
- **Styling**: Tailwind CSS
- **Plotting**: Plotly.js with React wrapper
- **Audio Processing**: Web Audio API
- **Signal Processing**: Custom JavaScript implementations

### Performance Optimizations

- **Downsampling**: Configurable audio downsampling for performance
- **Plot Optimization**: Automatic data reduction for large datasets
- **Streaming Analysis**: Progressive status updates during processing
- **Memory Management**: Efficient Float32Array handling

## Configuration

The analysis uses the same parameters as the original Python version, defined in `lib/config.ts`:

```typescript
// Example key parameters
{
  downsample_factor: 300,           // Audio downsampling
  bandpass_freqs: [20, 150],        // Hz range for filtering
  pairing_confidence_threshold: 0.50, // S1-S2 pairing threshold
  min_peak_distance_sec: 0.05,     // Minimum peak separation
  // ... 80+ configurable parameters
}
```

## Development

### Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

### Project Structure

```
├── app/                    # Next.js app directory
│   └── page.tsx           # Main application page
├── components/            # React components
│   ├── BPMChart.tsx      # Plotly chart component
│   ├── AnalysisResults.tsx # Results display
│   └── FileUploader.tsx  # File upload UI
├── lib/                   # Core analysis logic
│   ├── types.ts          # TypeScript interfaces
│   ├── config.ts         # Analysis parameters
│   ├── audio-processing.ts # Audio utilities
│   └── bmp-analysis.ts   # Main analysis engine
```

## Comparison with Python Version

| Feature            | Python Version             | Web Version             |
| ------------------ | -------------------------- | ----------------------- |
| Analysis Algorithm | ✅ Full implementation     | ✅ Full port            |
| Audio Formats      | ✅ All formats (via pydub) | ✅ Browser-supported    |
| Plotting           | ✅ Plotly                  | ✅ Plotly.js            |
| Performance        | ✅ Fast (scipy)            | ⚡ Good (Web Audio API) |
| Deployment         | 🖥️ Desktop app             | 🌐 Web browser          |
| Privacy            | ✅ Local processing        | ✅ Client-side only     |

## Known Limitations

1. **Signal Processing**: Simplified filters compared to scipy (but still effective)
2. **Audio Formats**: Limited to browser-decodable formats
3. **Performance**: Slower than native Python for very large files
4. **Memory**: Browser memory constraints for extremely long recordings

## Browser Compatibility

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 14+
- ✅ Edge 79+

Requires Web Audio API support for audio processing.

## Contributing

The codebase maintains the same structure and logic as the original Python version for easy comparison and maintenance. Key files to understand:

- `lib/bpm-analysis.ts`: Main BPMAnalyzer class (port of PeakClassifier)
- `lib/audio-processing.ts`: Audio utilities (port of scipy functions)
- `lib/config.ts`: Analysis parameters (port of config.py)

## License

This project maintains the same license as the original Python implementation.

---

_This web version provides the same sophisticated heartbeat analysis capabilities as the original Python tool, but runs entirely in your browser for maximum privacy and convenience._
