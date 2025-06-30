# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Multi-Stage Beat Detection Algorithm:** Employs a sophisticated, multi-stage algorithm that builds a comprehensive understanding of the audio before making final decisions.
    - **Automated BPM Estimation:** The analysis begins with a high-confidence first pass to find "anchor" beats and automatically estimate a global starting BPM, making the algorithm less dependent on user input.
    - **Sanitized Dynamic Noise Floor:** A robust trough-sanitization process identifies and rejects false troughs (divots in larger waveforms) to calculate a highly accurate dynamic noise floor that adapts to changing noise levels.
    - **Intelligent Noise Rejection:** Before attempting to pair peaks, the algorithm uses advanced heuristics to proactively identify and reject noise based on the refined noise floor.
    - **Rhythm-Based Post-Correction:** After the main analysis, a final validation pass corrects for rhythmic errors, such as when a single heartbeat is mistakenly detected as two separate, closely spaced beats.
    - **Dynamic HRV Outlier Rejection:** A key feature that prevents noise from creating unrealistic BPM spikes. It rejects any beat that would result in a beat-to-beat interval that changes by more than a plausible percentage from the previous interval.
    - **Long-Term BPM Tracking:** The algorithm tracks a smoothed, long-term BPM "belief" (initialized by the auto-estimated BPM) to dynamically adjust pairing parameters.
    - **Blended Confidence Model:** A continuous confidence model evaluates how likely a pair of sound peaks is a true S1-S2 couplet.
- **Heart Rate Variability (HRV) Analysis:**
    - The script calculates key time-domain HRV metrics:
        - **SDNN:** The standard deviation of beat-to-beat (RR) intervals, reflecting overall HRV.
        - **RMSSD:** The root mean square of successive differences between RR intervals, reflecting short-term, high-frequency HRV.
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, detected peaks (classified as S1, S2, or Noise), and an **Analysis Summary** box displaying the calculated HRV metrics.
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file (`_Debug_Log.md`).
- **Data Export:** Saves the calculated BPM data to a CSV file for further analysis.
## Configuration
All tunable parameters for the analysis engine are located in the `DEFAULT_PARAMS` dictionary near the top of the script. Each parameter is accompanied by comments explaining its purpose and the trade-offs involved in changing its value. This allows advanced users to fine-tune the algorithm's sensitivity and behavior for specific types of recordings. Key parameters include:
- `rr_interval_max_decrease_pct` / `rr_interval_max_increase_pct`: Define the plausible window for beat-to-beat changes, forming the core of the HRV outlier rejection.
- `pairing_confidence_threshold`: The confidence score required to classify two peaks as an S1-S2 pair.
- `trough_rejection_multiplier`: Controls how aggressively the trough sanitization algorithm rejects potential divots in the main waveform.
- `rr_correction_threshold_pct`: Sets the threshold for the rhythm-based post-correction pass, defining how close two beats must be to be considered a conflict.
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
2. **Install FFmpeg:** Follow the installation instructions for your operating system from the official [FFmpeg website](https://ffmpeg.org/download.html).
3. **Run the Script:**
    ```
    python bpm_analysis_v1.9.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field. This is no longer required for good performance but can be used to override the algorithm's auto-estimation for difficult recordings.
    - Click **Analyze**.
5. **View Results:**
    - An HTML plot file (e.g., `your_audio_file_bpm_plot.html`) will be saved in the same directory as the script.
    - A CSV file with the BPM data (e.g., `your_audio_file_bpm_analysis.csv`) will also be created.
    - A detailed Markdown log file (e.g., `your_audio_file_Debug_Log.md`) will be generated for in-depth review.