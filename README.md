# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis. Includes a **"Save All Results"** button to re-export all output files from the last analysis on demand.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A, MOV) by converting them to a standard format for analysis.
- **Intelligent Preprocessing:** The audio processing pipeline now filters the audio at its original sample rate _before_ downsampling. This preserves maximum signal fidelity and includes a safety check to prevent aliasing errors from overly aggressive downsampling.
- **Multi-Stage Analysis Pipeline:** The core of the application is a four-stage analysis pipeline designed for maximum accuracy:
    1. **High-Confidence First Pass:** The analysis starts with a strict "high-confidence" pass to find only the most obvious "anchor beats."
    2. **Automated BPM & Noise Floor Estimation:** The script uses the anchor beats to automatically estimate a global starting BPM. It also performs a sophisticated **trough sanitization** to calculate a more accurate and robust dynamic noise floor.
    3. **Primary Analysis:** A second, more sensitive analysis pass is performed using the global BPM estimate and the refined noise floor to detect and classify all potential peaks.
    4. **Rhythmic Correction:** A final post-processing step validates the detected beats against a plausible rhythm, removing any remaining outliers that are too close together.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions during the primary analysis pass.
- **Advanced Recovery & Exertion Analysis:**
    - **Heart Rate Recovery (HRR):** Calculates the standard 1-minute HRR (the drop in BPM one minute after the peak heart rate).
    - **Slope Analysis:** Identifies the most significant, sustained periods of heart rate increase (exertion) and decrease (recovery), calculating and visualizing the slope (in BPM/sec) for each.
    - **Peak Exertion/Recovery Rates:** Finds and highlights the single steepest period of exertion and recovery over a fixed time window.
- **Windowed Heart Rate Variability (HRV) Analysis:**
    - The script performs a **sliding window analysis** over the detected beats to calculate time-varying HRV metrics.
    - It computes **SDNN** and **RMSSDc** (RMSSD corrected for mean heart rate) for each window, providing insight into how HRV changes throughout the recording.
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, detected peaks, an **Analysis Summary** box with key metrics, and visualizations for exertion/recovery slopes.
    - **High-Resolution Image Export:** The plot can be saved as a high-resolution PNG image directly from the plot's controls.
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file.
- **Data Export:** In addition to the BPM data, the script now exports a detailed **HRV data log** to a separate CSV file, containing the time-varying SDNN, RMSSDc, and windowed BPM.
## Configuration
All tunable parameters for the analysis engine, including file output suffixes, are located in the `DEFAULT_PARAMS` dictionary near the top of the script. Each parameter is accompanied by comments explaining its purpose.
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
    python bpm_analysis_v2.5.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field.
    - Click **Analyze**.
    - Once analysis is complete, click **"Save All Results"** to save the outputs to a location of your choice.
5. **View Results:**
    - An HTML plot file (`_bpm_plot.html`) will be saved.
    - A CSV file with the BPM data (`_bpm_analysis.csv`) will be created.
    - A new CSV file with the detailed HRV data (`_hrv_data.csv`) will be created.
    - A detailed Markdown log file (`_Debug_Log.md`) will be generated for in-depth review.