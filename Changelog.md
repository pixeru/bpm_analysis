[# Changelog: BPM Analysis Script
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

# Changelog: BPM Analysis Script
## Version 0.3
This version focuses on improving the core beat detection algorithm to handle cases where beats might be missed, leading to more accurate and robust BPM analysis, especially in noisy recordings.
### 🚀 Improvements
- **Peak Detection Algorithm: Beat Rescue Logic**
    - The `find_heartbeat_peaks` function has been significantly enhanced with a new multi-step process to prevent missed beats:
        1. **Initial Analysis:** The algorithm first performs the S1-S2 pairing to create an initial set of candidate heartbeats, same as in v0.2.
        2. **Interval Validation:** It then analyzes the time intervals between these candidate beats.
        3. **Missed Beat Rescue:** If an interval is determined to be "suspiciously long" (i.e., it would imply a sudden, physiologically unlikely drop in heart rate), the algorithm now re-examines the original raw signal within that specific time window. It searches for any previously discarded peaks in that segment and "rescues" the most prominent one, adding it back into the list of beats.
    - This refinement makes the algorithm more resilient to artifacts and noise that might have caused weaker heartbeats to be initially overlooked.
### 🐛 Bug Fixes
- A potential bug in the final filtering stage was addressed to prevent duplicate peaks from being added to the final list after the new "beat rescue" logic has been applied.
_(No other significant changes were made to the GUI or other functions.)_

# Changelog: BPM Analysis Script
## Version 0.4
This version introduces a more intelligent and adaptive peak detection algorithm, specifically designed to improve accuracy for recordings with very high heart rates. It also includes more detailed debugging output.
### 🚀 Improvements
- **Peak Detection Algorithm: Adaptive Logic for High BPM**
    - The `find_heartbeat_peaks` function now dynamically changes its strategy based on an estimated BPM.
    - **High BPM Mode:** If an initial BPM estimate (or a user-provided hint) is above a certain threshold (160 BPM), the algorithm switches to a "very strict" S1-S2 pairing logic. This uses a much shorter, fixed time interval to identify the S1-S2 heart sound pair, which is critical for accuracy at high speeds where the two sounds are very close together.
    - **Moderate BPM Mode:** For lower heart rates, the algorithm continues to use the more flexible, dynamically-calculated S1-S2 interval from previous versions.
- **Initial Peak Finding:** The parameters for the initial `find_peaks` function (`prominence` and `height`) have been made less strict. This allows the algorithm to capture more potential raw peaks at the start, which gives the downstream adaptive logic and beat rescue logic more data to work with, improving the chances of finding the correct beats.
- **Debugging:** Extensive `print` statements have been added throughout the `find_heartbeat_peaks` function to provide a detailed, step-by-step log of the detection process. This is invaluable for troubleshooting and understanding how the final set of peaks was chosen.
_(No other significant changes were made to the GUI or other functions.)_

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

# Changelog: BPM Analysis Script
## Version 0.3
This version focuses on improving the core beat detection algorithm to handle cases where beats might be missed, leading to more accurate and robust BPM analysis, especially in noisy recordings.
### 🚀 Improvements
- **Peak Detection Algorithm: Beat Rescue Logic**
    - The `find_heartbeat_peaks` function has been significantly enhanced with a new multi-step process to prevent missed beats:
        1. **Initial Analysis:** The algorithm first performs the S1-S2 pairing to create an initial set of candidate heartbeats, same as in v0.2.
        2. **Interval Validation:** It then analyzes the time intervals between these candidate beats.
        3. **Missed Beat Rescue:** If an interval is determined to be "suspiciously long" (i.e., it would imply a sudden, physiologically unlikely drop in heart rate), the algorithm now re-examines the original raw signal within that specific time window. It searches for any previously discarded peaks in that segment and "rescues" the most prominent one, adding it back into the list of beats.
    - This refinement makes the algorithm more resilient to artifacts and noise that might have caused weaker heartbeats to be initially overlooked.
### 🐛 Bug Fixes
- A potential bug in the final filtering stage was addressed to prevent duplicate peaks from being added to the final list after the new "beat rescue" logic has been applied.
_(No other significant changes were made to the GUI or other functions.)_

# Changelog: BPM Analysis Script
## Version 0.4
This version introduces a more intelligent and adaptive peak detection algorithm, specifically designed to improve accuracy for recordings with very high heart rates. It also includes more detailed debugging output.
### 🚀 Improvements
- **Peak Detection Algorithm: Adaptive Logic for High BPM**
    - The `find_heartbeat_peaks` function now dynamically changes its strategy based on an estimated BPM.
    - **High BPM Mode:** If an initial BPM estimate (or a user-provided hint) is above a certain threshold (160 BPM), the algorithm switches to a "very strict" S1-S2 pairing logic. This uses a much shorter, fixed time interval to identify the S1-S2 heart sound pair, which is critical for accuracy at high speeds where the two sounds are very close together.
    - **Moderate BPM Mode:** For lower heart rates, the algorithm continues to use the more flexible, dynamically-calculated S1-S2 interval from previous versions.
- **Initial Peak Finding:** The parameters for the initial `find_peaks` function (`prominence` and `height`) have been made less strict. This allows the algorithm to capture more potential raw peaks at the start, which gives the downstream adaptive logic and beat rescue logic more data to work with, improving the chances of finding the correct beats.
- **Debugging:** Extensive `print` statements have been added throughout the `find_heartbeat_peaks` function to provide a detailed, step-by-step log of the detection process. This is invaluable for troubleshooting and understanding how the final set of peaks was chosen.
_(No other significant changes were made to the GUI or other functions.)_

# Changelog: BPM Analysis Script
## Version 0.5
This version represents a significant architectural improvement to the core beat detection algorithm, replacing the semi-static logic with a fully dynamic approach that is much more responsive to heart rate variability.
### ✨ New Features
- **Fully Dynamic S1-S2 Pairing Algorithm:**
    - The previous peak detection logic, which set a single S1-S2 interval threshold at the start of the analysis, has been completely replaced.
    - The new algorithm continuously updates the S1-S2 interval threshold based on a rolling window of the most recent beat-to-beat intervals.
    - This allows the analysis to adapt in real-time to accelerations and decelerations in heart rate within the same recording, significantly improving accuracy on audio with high variability.
### 🚀 Improvements
- **More Granular Initial Threshold:** The logic for setting the _initial_ S1-S2 interval from a user-provided `start_bpm_hint` is more nuanced, providing a better starting point for the new dynamic algorithm.
- **Increased BPM Range:** The default `max_bpm` parameter in the application has been raised from 220 to 270 to reflect the enhanced capability of the new algorithm to handle very high heart rates.
- **Algorithm Refinement:** A minor tweak was made to the fallback calculation within the "Beat Rescue" logic.](<# Changelog: BPM Analysis Script
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

# Changelog: BPM Analysis Script
## Version 0.3
This version focuses on improving the core beat detection algorithm to handle cases where beats might be missed, leading to more accurate and robust BPM analysis, especially in noisy recordings.
### 🚀 Improvements
- **Peak Detection Algorithm: Beat Rescue Logic**
    - The `find_heartbeat_peaks` function has been significantly enhanced with a new multi-step process to prevent missed beats:
        1. **Initial Analysis:** The algorithm first performs the S1-S2 pairing to create an initial set of candidate heartbeats, same as in v0.2.
        2. **Interval Validation:** It then analyzes the time intervals between these candidate beats.
        3. **Missed Beat Rescue:** If an interval is determined to be "suspiciously long" (i.e., it would imply a sudden, physiologically unlikely drop in heart rate), the algorithm now re-examines the original raw signal within that specific time window. It searches for any previously discarded peaks in that segment and "rescues" the most prominent one, adding it back into the list of beats.
    - This refinement makes the algorithm more resilient to artifacts and noise that might have caused weaker heartbeats to be initially overlooked.
### 🐛 Bug Fixes
- A potential bug in the final filtering stage was addressed to prevent duplicate peaks from being added to the final list after the new "beat rescue" logic has been applied.
_(No other significant changes were made to the GUI or other functions.)_

# Changelog: BPM Analysis Script
## Version 0.4
This version introduces a more intelligent and adaptive peak detection algorithm, specifically designed to improve accuracy for recordings with very high heart rates. It also includes more detailed debugging output.
### 🚀 Improvements
- **Peak Detection Algorithm: Adaptive Logic for High BPM**
    - The `find_heartbeat_peaks` function now dynamically changes its strategy based on an estimated BPM.
    - **High BPM Mode:** If an initial BPM estimate (or a user-provided hint) is above a certain threshold (160 BPM), the algorithm switches to a "very strict" S1-S2 pairing logic. This uses a much shorter, fixed time interval to identify the S1-S2 heart sound pair, which is critical for accuracy at high speeds where the two sounds are very close together.
    - **Moderate BPM Mode:** For lower heart rates, the algorithm continues to use the more flexible, dynamically-calculated S1-S2 interval from previous versions.
- **Initial Peak Finding:** The parameters for the initial `find_peaks` function (`prominence` and `height`) have been made less strict. This allows the algorithm to capture more potential raw peaks at the start, which gives the downstream adaptive logic and beat rescue logic more data to work with, improving the chances of finding the correct beats.
- **Debugging:** Extensive `print` statements have been added throughout the `find_heartbeat_peaks` function to provide a detailed, step-by-step log of the detection process. This is invaluable for troubleshooting and understanding how the final set of peaks was chosen.
_(No other significant changes were made to the GUI or other functions.)_

# Changelog: BPM Analysis Script
## Version 0.5
This version represents a significant architectural improvement to the core beat detection algorithm, replacing the semi-static logic with a fully dynamic approach that is much more responsive to heart rate variability.
### ✨ New Features
- **Fully Dynamic S1-S2 Pairing Algorithm:**
    - The previous peak detection logic, which set a single S1-S2 interval threshold at the start of the analysis, has been completely replaced.
    - The new algorithm continuously updates the S1-S2 interval threshold based on a rolling window of the most recent beat-to-beat intervals.
    - This allows the analysis to adapt in real-time to accelerations and decelerations in heart rate within the same recording, significantly improving accuracy on audio with high variability.
### 🚀 Improvements
- **More Granular Initial Threshold:** The logic for setting the _initial_ S1-S2 interval from a user-provided `start_bpm_hint` is more nuanced, providing a better starting point for the new dynamic algorithm.
- **Increased BPM Range:** The default `max_bpm` parameter in the application has been raised from 220 to 270 to reflect the enhanced capability of the new algorithm to handle very high heart rates.
- **Algorithm Refinement:** A minor tweak was made to the fallback calculation within the "Beat Rescue" logic.>)

