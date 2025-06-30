# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Dynamic Noise Floor:** The analysis begins by detecting local minima (troughs) and calculating a dynamic noise floor that adapts to changing noise levels throughout the recording. This is used to set a dynamic height threshold for peak detection.
    - **Intelligent Noise Rejection:** Before attempting to pair peaks, the algorithm uses advanced heuristics to proactively identify and reject noise, including a "Lookahead Veto" and trough-based confidence scoring.
    - **Long-Term BPM Tracking:** The algorithm tracks a smoothed, long-term BPM. This "belief" is used to dynamically adjust pairing parameters and is updated with each beat detected.
    - **Blended Confidence Model:** A continuous confidence model evaluates how likely a pair of sound peaks is a true S1-S2 couplet, blending multiple factors based on the current long-term BPM belief.
- **BPM Hint:** Users can provide an estimated starting BPM to give the algorithm an initial "belief" to work from.
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, dynamic noise floor, and all detected peaks, which are color-coded and symbol-coded by their final classification (S1, S2, or Noise).
    - **Chronological Debug Log:** A detailed, time-sorted log is printed to the console and saved as a separate Markdown file (`_Debug_Log.md`). This log has been overhauled to present a clean, event-driven report, associating the algorithm's state (BPM belief, noise floor, etc.) with each detected peak and trough at the moment it occurred.
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
    python bpm_analysis_v1.1.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field.
    - Click **Analyze**.
5. **View Results:**
    - An HTML plot file (e.g., `your_audio_file_bpm_plot.html`) will be saved in the same directory as the script.
    - A CSV file with the BPM data (e.g., `your_audio_file_bpm_analysis.csv`) will also be created.
    - A detailed Markdown log file (e.g., `your_audio_file_Debug_Log.md`) will be generated for in-depth review.