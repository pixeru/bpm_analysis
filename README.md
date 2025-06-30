# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Dynamic Noise Floor:** The analysis begins by detecting local minima (troughs) and calculating a dynamic noise floor that adapts to changing noise levels throughout the recording.
    - **Intelligent Noise Rejection:** Before attempting to pair peaks, the algorithm uses advanced heuristics to proactively identify and reject noise.
    - **Dynamic HRV Outlier Rejection:** A key feature that prevents noise from creating unrealistic BPM spikes. It rejects any beat that would result in a beat-to-beat interval that changes by more than a plausible percentage from the previous interval.
    - **Long-Term BPM Tracking:** The algorithm tracks a smoothed, long-term BPM "belief" to dynamically adjust pairing parameters.
    - **Blended Confidence Model:** A continuous confidence model evaluates how likely a pair of sound peaks is a true S1-S2 couplet.
- **Heart Rate Variability (HRV) Analysis:**
    - The script now calculates key time-domain HRV metrics:
        - **SDNN:** The standard deviation of beat-to-beat (RR) intervals, reflecting overall HRV.
        - **RMSSD:** The root mean square of successive differences between RR intervals, reflecting short-term, high-frequency HRV.
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, detected peaks (classified as S1, S2, or Noise), and an **Analysis Summary** box displaying the calculated HRV metrics.
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file (`_Debug_Log.md`).
- **Data Export:** Saves the calculated BPM data to a CSV file for further analysis.
## Configuration
All tunable parameters for the analysis engine are located in the `DEFAULT_PARAMS` dictionary near the top of the script. Each parameter is accompanied by comments explaining its purpose and the trade-offs involved in changing its value. This allows advanced users to fine-tune the algorithm's sensitivity and behavior for specific types of recordings.
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
    python bpm_analysis_v1.8.py
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