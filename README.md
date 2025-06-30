# Heartbeat BPM Analyzer v3.4
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A, MOV) by converting them to a standard format for analysis.
- **Intelligent Preprocessing:** The audio processing pipeline filters the audio at its original sample rate _before_ downsampling to preserve maximum signal fidelity and prevent aliasing errors.
- **Dynamic and State-Aware Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Dynamic Rhythm-Based Confidence Boost (New in v3.4):** The confidence boost for S1/S2 pairing is no longer a fixed value. It now dynamically adapts based on the recent history of successful beat pairings. When the rhythm is stable and clear, the boost is stronger to confidently pair beats. In noisy or arrhythmic sections, the boost is weaker to avoid incorrect pairings.
    - **Peak Strength Deviation:** The algorithm compares the "strength" of each peak (amplitude relative to the dynamic noise floor) instead of raw amplitude, making the analysis more robust against volume changes.
    - **Smarter Post-Exertion Logic:** The "post-exertion recovery" state is now more nuanced, using an "effective BPM" for its logic to ensure rules adapt correctly as the heart rate drops.
    - **Dynamic Confidence Curve:** The S1/S2 pairing logic uses a dynamic confidence model, smoothly interpolating between physiological models for resting and high heart rates.
- **Multi-Stage Analysis Pipeline:** The core of the application is a multi-stage analysis pipeline designed for maximum accuracy:
    1. **High-Confidence Preliminary Pass:** The analysis starts by finding only the most obvious "anchor beats."
    2. **Peak BPM & Recovery Phase Detection:** It uses these anchor beats to find the point of peak exertion and defines a subsequent "post-exertion recovery phase."
    3. **Global BPM & Refined Noise Floor Estimation:** The script uses the anchor beats to automatically estimate a global starting BPM and performs a sophisticated **trough sanitization** to calculate a robust dynamic noise floor.
    4. **State-Aware Primary Analysis:** A second, more sensitive analysis pass is performed using the global BPM estimate, the refined noise floor, and the advanced physiological models.
    5. **Advanced Lone S1 Validation:** A robust, multi-point check validates single beats to prevent noise from being misclassified.
    6. **Rhythmic Correction:** A final post-processing step validates the detected beats against a plausible rhythm, removing any remaining outliers.
- **Advanced Recovery & Exertion Analysis:**
    - **Heart Rate Recovery (HRR):** Calculates the standard 1-minute HRR.
    - **Slope Analysis:** Identifies the most significant periods of heart rate increase (exertion) and decrease (recovery).
    - **Peak Exertion/Recovery Rates:** Finds and highlights the single steepest period of exertion and recovery over a fixed time window.
- **Windowed Heart Rate Variability (HRV) Analysis:**
    - The script performs a **sliding window analysis** over the detected beats to calculate time-varying HRV metrics (SDNN and RMSSDc).
- **Comprehensive Visualization & Outputs:** Generates multiple outputs for in-depth analysis:
    - **Interactive HTML Plot:** A rich plot showing the audio envelope, detected peaks, an **Analysis Summary** box, and visualizations for exertion/recovery slopes.
    - **Markdown Summary Report:** A detailed report containing all key metrics, slope analysis, and a table of BPM data over time.
    - **Chronological Debug Log:** A detailed, time-sorted log with justifications for every classification decision.
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
    python bpm_analysis_v3.4.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM. If left blank, the script will automatically estimate it.
    - Click **Analyze**. Analysis outputs will be saved automatically in the same folder as the script.