# BPM Analysis Web Tool

A web-based heartbeat BPM analysis tool that processes audio files to detect S1/S2 heart sounds and calculate heart rate metrics.

## Features

- 🫀 **Advanced Heartbeat Detection**: Sophisticated S1/S2 pairing algorithm
- 📊 **Interactive Visualization**: Real-time plotting with Plotly.js
- 📈 **Comprehensive Metrics**: BPM tracking, HRV analysis, peak detection
- 🎵 **Multiple Audio Formats**: Supports WAV, MP3, M4A, FLAC, OGG
- 🎨 **Modern UI**: Beautiful, responsive interface
- ⚡ **Fast Processing**: Optimized algorithms for web performance

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:
   ```bash
   cd bpm-analysis-web
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser and go to `http://localhost:3000`

## Usage

1. **Upload Audio File**: 
   - Click "Choose File" or drag and drop an audio file
   - Supported formats: WAV, MP3, M4A, FLAC, OGG
   - A sample file (`sample_input.wav`) is included for testing

2. **Set Parameters**:
   - Optionally enter a starting BPM hint (e.g., 80)
   - This helps the algorithm converge faster

3. **Analyze**:
   - Click "Analyze Heartbeat" to start processing
   - Watch the progress bar for real-time updates

4. **View Results**:
   - Interactive plot showing:
     - Audio envelope and noise floor
     - S1/S2 heartbeat markers
     - BPM time series
     - HRV metrics (optional)
   - Statistics cards with key metrics:
     - Average BPM
     - Peak BPM
     - Minimum BPM
     - Heart Rate Variability
     - Total S1 beats
     - S1-S2 pairs

## Technical Details

### Algorithm Features

- **Dynamic Noise Floor**: Adaptive noise filtering based on signal characteristics
- **S1/S2 Classification**: Advanced pairing algorithm using confidence scoring
- **Rhythm Validation**: Long-term BPM tracking with stability analysis
- **HRV Calculation**: RMSSD and SDNN metrics for heart rate variability

### Signal Processing

- **Bandpass Filtering**: 20-150 Hz frequency range optimized for heart sounds
- **Downsampling**: Configurable factor for performance optimization
- **Envelope Detection**: Smooth amplitude tracking
- **Peak Detection**: Prominence-based with minimum distance constraints

### Visualization

- **Interactive Plotting**: Zoom, pan, and hover for detailed inspection
- **Multiple Traces**: Audio, noise floor, peaks, BPM, and HRV
- **Color Coding**: 
  - 🔴 S1 heartbeats (red triangles)
  - 🔵 S2 heartbeats (blue triangles)
  - ⚫ Noise/rejected peaks (gray X's)
- **Real-time Updates**: Responsive UI with progress tracking

## File Structure

```
bpm-analysis-web/
├── index.html              # Main HTML interface
├── package.json            # Dependencies and scripts
├── vite.config.js          # Vite build configuration
├── sample_input.wav        # Sample audio file for testing
├── src/
│   ├── main.js             # Main application logic
│   ├── audio-processor.js  # Audio loading and preprocessing
│   ├── bpm-analysis.js     # Core BPM analysis algorithms
│   └── plotting.js         # Plotly.js visualization
└── README.md              # This file
```

## Configuration

The analysis can be customized by modifying parameters in `src/bpm-analysis.js`:

- `minPeakDistanceSec`: Minimum time between peaks (default: 0.05s)
- `pairingConfidenceThreshold`: S1/S2 pairing threshold (default: 0.50)
- `noiseFloorQuantile`: Noise floor calculation percentile (default: 0.20)
- And many more advanced parameters...

## Comparison with Python Version

This web version implements the same core algorithms as the Python `bpm_analysis.py`:

- ✅ Dynamic noise floor calculation
- ✅ S1/S2 pairing with confidence scoring
- ✅ Long-term BPM belief tracking
- ✅ HRV metrics (RMSSD, SDNN)
- ✅ Interactive visualization
- ✅ Peak classification and debugging

## Building for Production

```bash
npm run build
```

This creates optimized files in the `dist/` directory.

## Browser Compatibility

- Chrome/Edge 70+
- Firefox 65+
- Safari 12+

Requires Web Audio API support for audio processing.

## Troubleshooting

### Common Issues

1. **File won't load**: Ensure the audio file is in a supported format
2. **No peaks detected**: Try adjusting the starting BPM hint
3. **Poor performance**: Large files may take time to process
4. **Browser compatibility**: Ensure you're using a modern browser

### Tips for Best Results

- Use high-quality audio recordings
- Avoid very noisy environments
- Provide a reasonable BPM hint if known
- Files under 50MB work best for web processing

## Contributing

This tool is designed to match the accuracy and functionality of the Python version while providing a modern web interface. For improvements or bug reports, please refer to the main project documentation.