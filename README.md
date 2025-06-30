# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Stateful Beat Detection Algorithm:** Employs a sophisticated, stateful algorithm that maintains a "belief" about the heart rate to make smarter decisions.
    - **Long-Term BPM Tracking:** The algorithm tracks a smoothed, long-term BPM throughout the analysis. This "belief" is used to dynamically adjust parameters and is updated with each beat detected.
    - **Blended Confidence Model:** A continuous confidence model evaluates how likely a pair of sound peaks is a true S1-S2 couplet. This model blends multiple factors, weighing peak amplitude deviation differently based on the current long-term BPM belief (e.g., at rest vs. during exertion).
    - **Heuristic Overrides:** The system uses intelligent overrides to improve accuracy, including a confidence "boost" for sudden BPM accelerations and a pattern-matching override that forces a pairing when a classic high-low amplitude pattern is detected.
- **BPM Hint:** Users can provide an estimated starting BPM to give the algorithm an initial "belief" to work from.
- **Interactive Visualization & Debugging:** Generates an interactive HTML plot showing:
    - The audio signal's envelope and final detected heartbeats.
    - **Advanced Hover-Labels:** Hover over any peak to see a detailed explanation of why it was kept or paired.
    - **Debug Traces:** The plot includes multiple optional traces for in-depth analysis, including the new **Long-Term BPM (Belief)**, which shows how the algorithm's state evolves over time.
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
    python bpm_analysis_v0.8.py
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