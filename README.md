# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Advanced Peak Detection:** Employs a sophisticated, multi-step algorithm to accurately identify heartbeats (peaks) in the audio signal:
    - **Fully Dynamic S1-S2 Pairing:** The core of the algorithm is its ability to differentiate between the two main heart sounds (S1 and S2). It uses a fully adaptive threshold that continuously updates based on a rolling window of the most recent beat-to-beat intervals. This makes the analysis highly responsive to changes in heart rate throughout the recording.
    - **Beat Rescue Logic:** Re-analyzes sections of the audio where a beat might have been missed due to noise or a weak signal.
- **BPM Hint:** Users can provide an estimated starting BPM to guide the algorithm, improving accuracy for difficult recordings.
- **Interactive Visualization:** Generates an interactive HTML plot showing:
    - The audio signal's envelope.
    - All raw peaks detected.
    - The final, filtered heartbeats.
    - A smoothed BPM trendline.
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
    python bpm_analysis_v0.5.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field.
    - Click **Analyze**.
5. **View Results:**
    - Check the console for detailed debug output.
    - An HTML plot file (e.g., `your_audio_file_bpm_plot.html`) will be saved in the same directory as the script.
    - A CSV file with the BPM data (e.g., `your_audio_file_bpm_analysis.csv`) will also be created.