# Changelog: BPM Analysis Script
## Version 0.2
This update transitions the script from a command-line tool to a graphical user interface (GUI) application, improving usability and adding new features for more accurate analysis.
### ✨ New Features
- **Graphical User Interface (GUI):** The script is now a user-friendly desktop application built with `tkinter` and `ttkbootstrap`.
    - **File Browser:** Users can now browse and select audio files directly from the application.
    - **Auto-File Detection:** The application automatically finds and loads the first supported audio file in the current directory on startup.
- **BPM Hint:** A new input field allows users to provide an optional "Starting BPM" hint. This helps the algorithm more accurately identify the initial S1-S2 heart sound interval, improving peak detection for recordings where the heart rate is known.
### 🚀 Improvements
- **Peak Detection Algorithm:**
    - The `find_heartbeat_peaks` function was enhanced to use the new user-provided BPM hint to calculate a more precise S1-S2 interval threshold.
    - In the absence of a hint, the automatic detection logic was made more robust by analyzing beat cycle estimates (systolic + diastolic intervals) rather than just the median of all peak intervals.
- **Plotting and Visualization:**
    - The x-axis of the output plot is now more informative, displaying time in both total seconds and a `minutes:seconds` format for easier interpretation of longer recordings.
    - The plot's y-axis range for signal amplitude was adjusted for better visualization of the waveform.
- **User Experience:**
    - The `main` function was refactored to launch the `BPMApp` GUI instead of automatically processing all files in a directory.
    - The application now provides real-time status updates (e.g., "Analyzing...", "Complete") and displays clear error messages to the user.
### 🐛 Bug Fixes
- The `downsample_factor` in the core processing parameters was changed from `10` in `v0.1` to `50` in `v0.2` within the `preprocess_audio` function and changed from `100` to `100` in the main function. This change likely addresses performance on larger files.
- The script now correctly handles the case where `pydub`/`FFmpeg` are not installed when attempting to convert non-WAV files, showing an error message in the GUI instead of just in the console.