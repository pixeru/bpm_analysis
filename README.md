# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **Thread-Safe GUI:** The user interface remains fully responsive during analysis. All file I/O and heavy computation are performed on a separate background thread, preventing the application from freezing.
- **Centralized Configuration:** All core analysis parameters are consolidated into a single `DEFAULT_PARAMS` dictionary at the top of the script, making it easy to tune and experiment with the algorithm's behavior.
- **Professional Logging:** The script now uses Python's built-in `logging` module to provide professional, timestamped logs for better debugging and monitoring.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Dynamic Noise Floor:** The analysis begins by detecting local minima (troughs) and calculating a dynamic noise floor that adapts to changing noise levels throughout the recording.
    - **Intelligent Noise Rejection:** Before attempting to pair peaks, the algorithm uses advanced heuristics to proactively identify and reject noise.
    - **Long-Term BPM Tracking:** The algorithm tracks a smoothed, long-term BPM "belief" to dynamically adjust pairing parameters.
    - **Blended Confidence Model:** A continuous confidence model evaluates how likely a pair of sound peaks is a true S1-S2 couplet.
- **BPM Hint:** Users can provide an estimated starting BPM to give the algorithm an initial "belief" to work from.
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, dynamic noise floor, and all detected peaks, which are color-coded and symbol-coded by their final classification (S1, S2, or Noise).
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file (`_Debug_Log.md`).
- **Data Export:** Saves the calculated BPM data to a CSV file for further analysis.
## Dependencies
To run this script, you will need Python and the following libraries:
- **`numpy`**: For numerical operations.
- **`pandas`**: For data manipulation and creating the signal envelope.
- **`scipy`**: For signal processing (filtering and peak finding).
- **`plotly`**: For creating the interactive plots.
- **`ttkbootstrap`**: For the modern GUI theme.
- **`pydub`**: For converting non-WAV audio files.
You will also need **FFmpeg** installed and accessible in your system's PATH for `pydub` to function correctly.
## How to Use
1. **Install Dependencies:**
    ```
    pip install numpy pandas scipy plotly ttkbootstrap pydub
    ```
2. **Install FFmpeg:** Follow the installation instructions for your operating system from the official [FFmpeg website](https://ffmpeg.org/download.html "null").
3. **Run the Script:**
    ```
    python bpm_analysis_v1.5.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field.
    - Click **Analyze**. The GUI will remain responsive while the analysis runs in the background.
    - The status bar will provide real-time updates on the analysis progress.
5. **View Results:**
    - An HTML plot file (e.g., `your_audio_file_bpm_plot.html`) will be saved in the same directory as the script.
    - A CSV file with the BPM data (e.g., `your_audio_file_bpm_analysis.csv`) will also be created.
    - A detailed Markdown log file (e.g., `your_audio_file_Debug_Log.md`) will be generated for in-depth review.