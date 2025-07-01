# Heartbeat BPM Analyzer v4.0
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis, with a focus on robust, non-blocking performance.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A, MOV) by converting them to a standard format for analysis.
- **Intelligent Preprocessing:** The audio processing pipeline filters the audio at its original sample rate _before_ downsampling to preserve maximum signal fidelity and prevent aliasing errors.
- **Dynamic and Self-Correcting Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate and can now actively recover from periods of signal ambiguity.
    - **Rhythm Recovery System (New in v4.0):** The algorithm includes two new mechanisms to prevent analysis failure in difficult audio sections:
        - **"Kick-Start" Mechanism:** Automatically detects when S1-S2 pairing is consistently failing and temporarily boosts pairing confidence to "kick-start" the rhythm detection.
        - **"Cascade Reset" Logic:** Prevents a cascade of failed beat detections by identifying consecutive rhythmic errors and forcing a re-anchoring of the beat sequence.
    - **Proportional Penalty System (New in v4.0):** The confidence penalty for an unexpectedly loud S2 is no longer a fixed value. It now scales proportionally to the severity of the amplitude violation, providing a more nuanced adjustment.
    - **Unified Confidence Adjustment Model:** The logic for S1/S2 pairing considers rhythm stability and physiological expectations simultaneously.
    - **Surrounding Trough Noise Check:** The noise detection logic analyzes the baseline on both sides of a peak to prevent misclassifications.
    - **Peak Strength Deviation:** The algorithm compares the "strength" of each peak (amplitude relative to the dynamic noise floor) instead of raw amplitude.
- **Multi-Stage Analysis Pipeline:** The core of the application is a modular, multi-stage analysis pipeline designed for maximum accuracy:
    1. **Refined Noise Floor Calculation:** The analysis begins by calculating a robust, dynamic noise floor based on a sanitized set of audio troughs.
    2. **High-Confidence Preliminary Pass:** Finds only the most obvious "anchor beats" using the pre-calculated noise floor.
    3. **Peak BPM & Recovery Phase Detection:** Uses anchor beats to find the point of peak exertion and define a subsequent "post-exertion recovery phase."
    4. **State-Aware Primary Analysis:** A sensitive analysis pass is performed using the refined noise floor and the advanced physiological and self-correction models.
    5. **Advanced Lone S1 Validation:** A robust, multi-point check validates single beats to prevent noise from being misclassified.
    6. **Rhythmic Correction:** A final post-processing step validates the detected beats against a plausible rhythm.
- **Advanced Recovery & Exertion Analysis:**
    - **Heart Rate Recovery (HRR):** Calculates the standard 1-minute HRR.
    - **Slope Analysis:** Identifies the most significant periods of heart rate increase (exertion) and decrease (recovery).
    - **Peak Exertion/Recovery Rates:** Finds and highlights the single steepest period of exertion and recovery over a fixed time window.
- **Windowed Heart Rate Variability (HRV) Analysis:**
    - Performs a **sliding window analysis** to calculate time-varying HRV metrics (SDNN and RMSSDc).
- **Comprehensive Visualization & Outputs:**
    - **Performance-Optimized HTML Plot:** A rich, interactive plot that optionally downsamples the main audio envelope trace for significantly faster rendering.
    - **Markdown Summary Report:** A detailed report containing all key metrics, slope analysis, and a table of BPM data.
    - **Context-Rich Debug Log:** A detailed, time-sorted log with justifications and full signal metrics for every detected event.
## Configuration
All tunable parameters for the analysis engine are located in the `DEFAULT_PARAMS` dictionary near the top of the script. The parameters are organized into logical categories for easier navigation and tuning.
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
    python bpm_analysis_v4.0.py
    ```
4. **Use the Application:**
    - The application will attempt to automatically load a supported audio file from the same directory.
    - If no file is loaded, click **Browse** to select an audio file.
    - (Optional) Enter an estimated starting BPM. If left blank, the script will automatically estimate it.
    - Click **Analyze**. Analysis outputs will be saved automatically in the same folder as the script.