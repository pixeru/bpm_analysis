# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis. Includes a **"Save All Results"** button to re-export all output files from the last analysis on demand.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A, MOV) by converting them to a standard format for analysis.
- **Intelligent Preprocessing:** The audio processing pipeline filters the audio at its original sample rate _before_ downsampling to preserve maximum signal fidelity and prevent aliasing errors.
- **Multi-Stage Analysis Pipeline:** The core of the application is a five-stage analysis pipeline designed for maximum accuracy:
    1. **High-Confidence First Pass:** The analysis starts with a strict "high-confidence" pass to find only the most obvious "anchor beats."
    2. **Automated BPM & Noise Floor Estimation:** The script uses the anchor beats to automatically estimate a global starting BPM. It also performs a sophisticated **trough sanitization** to calculate a more accurate and robust dynamic noise floor.
    3. **Primary Analysis:** A second, more sensitive analysis pass is performed using the global BPM estimate and the refined noise floor to detect and classify all potential peaks.
    4. **Rhythmic Correction:** A post-processing step validates the detected beats against a plausible rhythm, removing any remaining outliers that are too close together.
    5. **Iterative Contextual Correction:** A final, iterative pass re-evaluates beats based on the local rhythm. It can "correct" a `Lone S1` that was likely a true beat pair by examining the pairing success rate of its neighbors, improving accuracy in recordings with inconsistent quality.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions during the primary analysis pass.
- **Advanced Recovery & Exertion Analysis:**
    - **Heart Rate Recovery (HRR):** Calculates the standard 1-minute HRR.
    - **Slope Analysis:** Identifies the most significant periods of heart rate increase (exertion) and decrease (recovery).
    - **Peak Exertion/Recovery Rates:** Finds and highlights the single steepest period of exertion and recovery over a fixed time window.
- **Windowed Heart Rate Variability (HRV) Analysis:**
    - The script performs a **sliding window analysis** over the detected beats to calculate time-varying HRV metrics (SDNN and RMSSDc).
- **Comprehensive Visualization & Debugging:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, detected peaks, an **Analysis Summary** box with key metrics, and visualizations for exertion/recovery slopes.
    - **High-Resolution Image Export:** The plot can be saved as a high-resolution PNG image directly from the plot's controls.
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file.
- **Data Export:** Exports a detailed **Analysis Summary** report, BPM data, and HRV data to separate files.
## Configuration
All tunable parameters for the analysis engine, including file output suffixes, are located in the `DEFAULT_PARAMS` dictionary near the top of the script. Each parameter is accompanied by comments explaining its purpose.
## Dependencies
To run this script, you will need Python and the following libraries:
- **`numpy`**
- **`pandas`**
- **`scipy`**
- **`plotly`**
- **`ttkbootstrap`**
- **`pydub`**
You will also need **FFmpeg** installed and accessible in your system's PATH for `pydub` to function correctly.
## How to Use
1. **Install Dependencies:**
    ```
    pip install numpy pandas scipy plotly ttkbootstrap pydub
    ```
2. **Install FFmpeg:** Follow the installation instructions for your operating system from the official [FFmpeg website](https://ffmpeg.org/download.html "null").
3. **Run the Script:**
    ```
    python bpm_analysis_v2.9.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM in the "Starting BPM" field.
    - Click **Analyze**.
    - Once analysis is complete, click **"Save All Results"** to save the outputs to a location of your choice.