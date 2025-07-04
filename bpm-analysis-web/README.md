# Heartbeat BPM Analyzer - Web Application

A sophisticated client-side web application for analyzing heart rate from audio recordings. This application performs advanced signal processing to detect S1 and S2 heart sounds, calculate beats per minute (BPM), and provide heart rate variability (HRV) analysis.

## Features

### 🫀 Advanced Heart Sound Detection
- **S1/S2 Classification**: Automatically detects and classifies S1 (lub) and S2 (dub) heart sounds
- **Dynamic Noise Filtering**: Intelligent noise floor calculation and peak classification
- **Rhythm Validation**: Validates detected beats based on physiological expectations

### 📊 Comprehensive Analysis
- **Real-time BPM Calculation**: Accurate beats per minute measurement
- **Heart Rate Variability**: RMSSD and SDNN metrics for cardiac health assessment
- **Confidence Scoring**: Algorithm provides confidence levels for reliability assessment

### 📈 Interactive Visualization
- **Zoomable Plots**: Interactive Plotly.js charts for exploring your data
- **Multi-layered Display**: Shows audio envelope, noise floor, detected peaks, and BPM over time
- **Export Capabilities**: Download analysis results as JSON files

### 🎵 Multi-format Support
- **Audio Formats**: WAV, MP3, M4A, and other common audio formats
- **Client-side Processing**: All analysis runs locally in your browser - no data leaves your device
- **Real-time Processing**: Fast analysis using Web Audio API

## Getting Started

### Prerequisites
- Node.js 18+ and npm
- Modern web browser with Web Audio API support

### Installation
```bash
# Clone or navigate to the project directory
cd bmp-analysis-web

# Install dependencies
npm install

# Start the development server
npm run dev
```

### Usage
1. **Open the application** in your browser (typically http://localhost:3000)
2. **Upload an audio file** containing heart sounds
3. **Wait for analysis** - the algorithm will process your audio in several steps:
   - Audio preprocessing and filtering (20-150 Hz bandpass)
   - Dynamic noise floor calculation
   - Peak detection and classification
   - BPM and HRV calculation
4. **Explore results** using the interactive plot and metrics

## Understanding the Results

### Main Metrics
- **Average BPM**: Overall heart rate from detected S1 peaks
- **Confidence Score**: Algorithm's confidence in the analysis (higher is better)
- **Heartbeats Detected**: Total number of S1 heart sounds found
- **Duration**: Length of the analyzed audio

### HRV Metrics (when available)
- **Min/Max BPM**: Range of heart rate variation
- **RMSSD**: Root mean square of successive differences (short-term HRV)
- **SDNN**: Standard deviation of NN intervals (overall HRV)

### Interactive Plot Elements
- **Blue Line**: Audio envelope (processed signal)
- **Green Dotted Line**: Dynamic noise floor
- **Red Circles**: S1 peaks (main heartbeats)
- **Orange Triangles**: S2 peaks (secondary heart sounds)
- **Gray X's**: Rejected noise peaks (hidden by default)
- **Red Line (Right Axis)**: BPM over time

## Best Practices for Audio Recording

### Optimal Recording Conditions
- **Quiet Environment**: Minimize background noise
- **Good Microphone**: Use a quality microphone or stethoscope adapter
- **Stable Placement**: Keep recording device steady
- **Appropriate Distance**: Position microphone close to the heart

### Recommended Settings
- **Sample Rate**: 44.1 kHz or higher
- **Bit Depth**: 16-bit minimum
- **Duration**: 30-120 seconds for best results
- **Format**: WAV preferred for highest quality

## Technical Implementation

### Core Algorithms
- **Bandpass Filtering**: Butterworth-like filter (20-150 Hz)
- **Envelope Detection**: Moving average for signal envelope
- **Peak Classification**: S1/S2 pairing with confidence scoring
- **Rhythm Analysis**: Physiological validation of detected beats

### Signal Processing Pipeline
1. **Audio Preprocessing**: Format conversion and filtering
2. **Noise Floor Calculation**: Dynamic baseline estimation
3. **Peak Detection**: Find potential heart sound candidates
4. **Classification**: Classify peaks as S1, S2, or noise
5. **Validation**: Apply physiological constraints
6. **Metrics Calculation**: Compute BPM and HRV metrics

## Browser Compatibility

- ✅ Chrome 66+
- ✅ Firefox 60+
- ✅ Safari 14+
- ✅ Edge 79+

## Privacy & Security

- **Local Processing**: All analysis happens in your browser
- **No Data Upload**: Audio files never leave your device
- **No Storage**: Files are processed in memory only
- **Export Control**: You choose what data to download

## Limitations

- **Audio Quality Dependent**: Results depend on recording quality
- **Not Medical Grade**: This tool is for educational/research purposes only
- **Client Performance**: Large files may take longer to process
- **Browser Support**: Requires modern browser with Web Audio API

## Troubleshooting

### Common Issues
- **"Failed to analyze"**: Check audio file format and quality
- **Low confidence scores**: Try a clearer recording with less noise
- **No peaks detected**: Ensure audio contains audible heart sounds
- **Slow processing**: Large files may take time; try shorter recordings

### Performance Tips
- Use shorter audio files (under 2 minutes) for faster processing
- Ensure good audio quality for better results
- Close other browser tabs if experiencing performance issues

## Development

### Project Structure
```
bpm-analysis-web/
├── app/
│   ├── lib/
│   │   ├── audioUtils.ts     # Audio processing utilities
│   │   └── bpmAnalyzer.ts    # Core BPM analysis engine
│   ├── components/
│   │   └── BpmPlot.tsx       # Interactive plotting component
│   └── page.tsx              # Main application page
├── package.json
└── README.md
```

### Key Dependencies
- **Next.js 15**: React framework
- **Plotly.js**: Interactive plotting
- **TypeScript**: Type safety
- **Tailwind CSS**: Styling
- **Lucide React**: Icons

## Contributing

This project is based on advanced signal processing research for heartbeat detection. The algorithms implement sophisticated peak classification and physiological validation techniques originally developed in Python and adapted for client-side JavaScript execution.

## License

This project is provided for educational and research purposes. Please ensure compliance with applicable medical device regulations if using for any clinical applications.
