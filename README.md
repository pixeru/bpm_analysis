# Heartbeat BPM Analyzer v3.1
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A, MOV) by converting them to a standard format for analysis.
- **Intelligent Preprocessing:** The audio processing pipeline filters the audio at its original sample rate _before_ downsampling to preserve maximum signal fidelity and prevent aliasing errors.
- **Dynamic and State-Aware Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Dynamic Confidence Curve (New in v3.1):** The S1/S2 pairing logic now uses a dynamic confidence model. It smoothly interpolates between two physiological models—one for resting heart rates (where S1/S2 amplitudes are similar) and one for high heart rates (where S1 is typically much louder than S2). This greatly improves pairing accuracy across different activity levels.
    - **State-Aware Contractility Model:** The algorithm runs a preliminary analysis to identify the peak heart rate. It then enters a "post-exertion recovery" state, applying stricter and more physiologically appropriate rules for beat pairing during this phase.
- **Multi-Stage Analysis Pipeline:** The core of the application is a multi-stage analysis pipeline designed for maximum accuracy:
    1. **High-Confidence Preliminary Pass:** The analysis starts by finding only the most obvious "anchor beats."
    2. **Peak BPM & Recovery Phase Detection:** It uses these anchor beats to find the point of peak exertion and defines a subsequent "post-exertion recovery phase."
    3. **Global BPM & Refined Noise Floor Estimation:** The script uses the anchor beats to automatically estimate a global starting BPM. It also performs a sophisticated **trough sanitization** to calculate a more accurate and robust dynamic noise floor.
    4. **State-Aware Primary Analysis:** A second, more sensitive analysis pass is performed using the global BPM estimate, the refined noise floor, and the dynamic confidence model.
    5. **Rhythmic Correction:** A post-processing step validates the detected beats against a plausible rhythm, removing any remaining outliers that are too close together.
    6. **Iterative Contextual Correction:** A final, iterative pass re-evaluates beats based on the local rhythm.
- **Advanced Recovery & Exertion Analysis:**
    - **Heart Rate Recovery (HRR):** Calculates the standard 1-minute HRR.
    - **Slope Analysis:** Identifies the most significant periods of heart rate increase (exertion) and decrease (recovery).
    - **Peak Exertion/Recovery Rates:** Finds and highlights the single steepest period of exertion and recovery over a fixed time window.
- **Windowed Heart Rate Variability (HRV) Analysis:**
    - The script performs a **sliding window analysis** over the detected beats to calculate time-varying HRV metrics (SDNN and RMSSDc).
- **Comprehensive Visualization & Outputs:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich, interactive plot showing the audio envelope, detected peaks, an **Analysis Summary** box with key metrics, and visualizations for exertion/recovery slopes.
    - **Markdown Summary Report:** A detailed report containing all key metrics, slope analysis, and a table of BPM data over time.
    - **Chronological Debug Log:** A detailed, time-sorted log is saved as a separate Markdown file for troubleshooting and verification.
## Configuration
All tunable parameters for the analysis engine are located in the `DEFAULT_PARAMS` dictionary near the top of the script. Each parameter is accompanied by comments explaining its purpose.
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
    python bpm_analysis_v3.1.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM. If left blank, the script will automatically estimate it.
    - Click **Analyze**. Analysis outputs will be saved automatically in the same folder as the script.