# BPM Analysis Web Application

A Django-based web application for heartbeat detection and BPM (Beats Per Minute) analysis from audio files.

## Features

- **File Upload**: Support for multiple audio formats (WAV, MP3, M4A, FLAC, OGG)
- **Real-time Analysis**: Advanced algorithms detect S1 and S2 heart sounds
- **Interactive Graphs**: Plotly-powered visualizations showing heartbeat patterns
- **BPM Detection**: Precise beats per minute calculation with trend analysis
- **Export Results**: Download detailed analysis reports and interactive graphs
- **Modern UI**: Beautiful, responsive interface with drag-and-drop functionality

## Installation

1. **Install system dependencies** (if not already installed):
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pip python3-django python3-venv
   ```

2. **Install Python dependencies**:
   ```bash
   pip3 install --break-system-packages -r requirements.txt
   ```

3. **Run Django migrations**:
   ```bash
   python3 manage.py migrate
   ```

## Usage

1. **Start the development server**:
   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:8000
   ```

3. **Upload an audio file**:
   - Drag and drop your audio file onto the upload area
   - Or click "Select File" to browse for a file
   - Supported formats: WAV, MP3, M4A, FLAC, OGG (Max: 100MB)

4. **Start analysis**:
   - Click "Start Analysis" to begin processing
   - The analysis may take a few moments depending on file size

5. **View results**:
   - You'll be redirected to the results page
   - Interactive graphs show heartbeat patterns and BPM trends
   - Download additional analysis reports in various formats

## Project Structure

```
bpm-analysis-web/
├── analyzer/                 # Django app for BPM analysis
│   ├── views.py             # Main application logic
│   ├── urls.py              # URL routing
│   └── models.py            # Database models
├── bmp_analyzer/            # Django project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   └── analyzer/            # App-specific templates
├── media/                   # User uploaded files
├── static/                  # Static files (CSS, JS)
├── bpm_analysis.py          # Core BPM analysis engine
├── config.py                # Analysis parameters
└── manage.py                # Django management script
```

## Core Analysis Features

### Heart Sound Detection
- **S1 (lub)**: First heart sound detection when tricuspid and mitral valves close
- **S2 (dub)**: Second heart sound detection when aortic and pulmonary valves close
- Advanced signal processing for accurate peak identification

### BPM Calculation
- Real-time beats per minute calculation
- Trend analysis and smoothing algorithms
- Statistical validation of results

### Output Formats
- Interactive HTML graphs with Plotly
- JSON data for further analysis
- Markdown reports with detailed statistics
- Analysis settings and metadata

## Understanding Results

### Normal BPM Ranges
- **Normal**: 60-100 BPM at rest
- **Bradycardia**: Below 60 BPM
- **Tachycardia**: Above 100 BPM

### Graph Interpretation
- Blue markers: S1 heart sounds (lub)
- Red markers: S2 heart sounds (dub)
- Line graph: BPM trend over time
- Green line: Dynamic noise floor

## Technical Details

### Requirements
- Python 3.8+
- Django 4.2+
- NumPy, Pandas, SciPy for data processing
- Plotly for interactive visualizations
- Pydub for audio file conversion

### Performance
- Processing time varies based on file size
- Typical 30-second audio file: 10-30 seconds analysis time
- Results are cached for faster subsequent access

## API Endpoints

- `GET /` - Main upload page
- `POST /upload/` - File upload and analysis endpoint
- `GET /result/<analysis_id>/` - View analysis results

## Configuration

Edit `config.py` to adjust analysis parameters:
- Signal processing settings
- Peak detection thresholds
- BPM calculation parameters
- Output formatting options

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
   ```bash
   pip3 install --break-system-packages -r requirements.txt
   ```

2. **File Upload Fails**: Check file size (max 100MB) and format support

3. **Analysis Errors**: Verify audio file quality and ensure it contains heartbeat sounds

4. **Server Won't Start**: Check if port 8000 is available
   ```bash
   python3 manage.py runserver 0.0.0.0:8001  # Use different port
   ```

### Debug Mode
For development, Django debug mode is enabled by default. To disable:
1. Edit `bmp_analyzer/settings.py`
2. Set `DEBUG = False`
3. Configure `ALLOWED_HOSTS` for production

## Medical Disclaimer

⚠️ **Important**: This tool is for educational and research purposes only. It should not be used for medical diagnosis or treatment decisions. Always consult qualified healthcare professionals for medical concerns.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions:
1. Check this README for troubleshooting
2. Review the analysis logic in `BPM Detection logic explained.md`
3. Check the changelog in `Changelog.md` for recent updates

## Development

To contribute or modify the application:
1. Follow Django best practices
2. Test changes with various audio files
3. Ensure analysis accuracy against known BPM values
4. Update documentation for any new features