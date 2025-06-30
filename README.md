# Heartbeat BPM Analyzer
The Heartbeat BPM Analyzer is a desktop application that analyzes audio recordings of heart sounds to detect heartbeats and calculate the Beats Per Minute (BPM) over time. It is designed to work with various audio file formats and provides a visual representation of the analysis.
## Features
- **GUI Interface:** A user-friendly graphical interface for easy file selection and analysis.
- **Multi-Format Audio Support:** Can process common audio files (e.g., WAV, MP3, M4A) by converting them to a standard format for analysis.
- **Advanced Peak Detection:** Employs a sophisticated, multi-step algorithm to accurately identify heartbeats:
    - **Confidence Scoring:** The algorithm first performs a preliminary analysis to calculate a "confidence score" for every pair of adjacent sound peaks. This score is based on the normalized amplitude deviation between the peaks, quantifying how likely they are to be a distinct S1-S2 pair.
    - **Confidence-Based Grouping:** It then uses this confidence score, combined with a dynamic time interval, to logically group the raw sound peaks into distinct heartbeats. A pair is only formed if the timing is correct _and_ the confidence is high.
- **BPM Hint:** Users can provide an estimated starting BPM to guide the algorithm, improving accuracy for difficult recordings.
- **Interactive Visualization & Debugging:** Generates an interactive HTML plot showing:
    - The audio signal's envelope and final detected heartbeats.
    - **Advanced Hover-Labels:** Hover over any raw or final peak to see a detailed explanation of why it was kept, discarded, or paired.
    - **Debug Traces:** Optional, hidden traces for the raw sound peaks, the normalized deviation, and the pairing confidence scores can be enabled from the legend for in-depth analysis.
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
    python bpm_analysis_v0.7.py
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