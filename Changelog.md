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

# Changelog: BPM Analysis Script
## Version 0.6
This version introduces a fundamental change in the beat detection philosophy, moving from a single complex function to a clearer, multi-stage "Relax and Refine" strategy. This makes the algorithm more robust and easier to debug.
### ✨ New Features
- **"Relax and Refine" Peak Detection Strategy:** The core `find_heartbeat_peaks` function was entirely re-architected into a sequential, four-step process:
    1. **Broad Peak Detection:** The algorithm now starts with a very "relaxed" initial peak detection phase. It uses minimal distance and prominence constraints specifically to capture _all_ potential sound events, including both the primary (S1) and secondary (S2) heart sounds.
    2. **Logical Beat Grouping:** The script then processes the rich list of raw peaks from the first step. It logically groups them into beats by identifying plausible S1-S2 pairs based on timing. This is a significant change from previous versions which attempted to find only S1 peaks from the start.
    3. **Beat Rescue:** The successful "beat rescue" logic from previous versions is retained. It now operates on the more reliable list of candidate beats from the grouping step to find any beats that were missed in noisy sections.
    4. **Final BPM Filtering:** The final, strict filter that ensures the interval between beats is within a physiologically plausible BPM range is kept as the last step to clean up any remaining anomalies.
### 🚀 Improvements
- **Algorithmic Clarity:** By separating the detection, grouping, and refining steps, the code's logic is now much clearer and more maintainable.
- **Robustness:** The new approach is less likely to miss S2 sounds and is better able to distinguish them from noise, leading to a more accurate set of candidate beats for the subsequent refining steps.

# Changelog: BPM Analysis Script
## Version 0.7
This version evolves the beat detection strategy by introducing a new "confidence score" metric. This makes the beat grouping logic more intelligent and adds powerful new debugging capabilities to the visualization.
### ✨ New Features
- **Confidence-Based S1-S2 Pairing:**
    - A new preliminary analysis step has been added. It calculates the **normalized amplitude deviation** between all adjacent raw peaks to generate a "confidence score." This score quantifies how likely a pair of peaks is a true S1-S2 couplet versus random noise.
    - The beat grouping logic now uses a dual-criteria system: a pair of peaks is only grouped into a single heartbeat if both the **time interval** is appropriate AND the **confidence score** is above a set threshold.
- **Advanced Debugging in Plots:**
    - **Detailed Hover Information:** The interactive plot now has rich tooltips. Hovering over any peak (both raw and final) displays its status and the reasoning behind the algorithm's decision (e.g., "S1 (Kept)", "S2 (Discarded)", "Lone S1 (Confidence too low)").
    - **New Data Traces:** The plot includes new, initially hidden traces for the "Normalized Deviation" and "Pairing Confidence" scores, allowing for in-depth visual debugging of the algorithm's performance.
### ♻️ Refactoring
- **Algorithm Simplification (for Debugging):** To isolate and evaluate the effectiveness of the new confidence-based system, the "Beat Rescue" and "Final BPM Filtering" steps (Steps 4 and 5 from v0.6) have been temporarily removed from the `find_heartbeat_peaks` function.

# Changelog: BPM Analysis Script
## Version 0.8
This major update transforms the beat detection algorithm from a stateless process to a **stateful** one. The algorithm now maintains an internal "belief" about the heart rate, allowing it to make more context-aware and intelligent decisions as it analyzes the audio.
### ✨ New Features
- **Stateful Long-Term BPM Tracking:**
    - The core of the new system is a `long_term_bpm` variable that acts as the algorithm's "belief" about the current heart rate.
    - This belief is initialized using the user's hint (or a default) and is then continuously updated after each beat is identified. The update is smoothed and rate-limited to prevent erratic jumps while still being responsive to real changes in heart rate.
- **Blended Confidence Model:**
    - The previous confidence function has been replaced with a more sophisticated `calculate_blended_confidence` model.
    - This new function is dynamic, producing different confidence scores for the same peak deviation based on the current `long_term_bpm`. It effectively has different models for resting, exercise, and exertion heart rates, and blends between them.
- **Heuristic Overrides and Boosts:**
    - **Pattern Match Override:** A new heuristic has been added that looks for a classic High-Low amplitude pattern between adjacent peaks. If this pattern is detected along with a significant local amplitude deviation, it will override the confidence model and force a pairing, catching obvious beats the model might otherwise miss.
    - **Confidence Boost:** The system now boosts the confidence score for potential pairs that would correspond to a sudden (but plausible) increase in heart rate, making it better at catching the start of an acceleration.
### 🚀 Improvements
- **Visualization:** A new "Long-Term BPM (Belief)" trace has been added to the interactive plot. This allows for powerful debugging, making it possible to visualize how the algorithm's internal state evolves and influences decisions throughout the analysis.

# Changelog: BPM Analysis Script
## Version 0.9
This version introduces significant new features for both analysis and debugging, including a noise floor estimation mechanism, a "lookahead veto" to prevent misclassification of peaks, and a comprehensive chronological event log.
### ✨ New Features
- **Noise Floor Estimation:**
    - The algorithm now performs a robust trough detection on the audio envelope at the start of the analysis.
    - It uses the quietest 25% of these troughs to calculate an estimated **noise floor**, which is then visualized as a dotted line on the plot. This helps provide context for the peak detection thresholds.
- **Lookahead Veto Heuristic:**
    - A new "lookahead veto" logic has been added to the S1-S2 pairing process.
    - Before pairing a peak with the one immediately following it, the algorithm now looks ahead to the _next_ peak. If the upcoming peak is significantly stronger, the pairing is vetoed. This prevents a strong S1 beat from being incorrectly classified as a secondary S2 sound of a weaker preceding peak.
- **Chronological Debug Log:**
    - A new function (`print_and_log_chronological_data`) has been created to generate an exhaustive, time-sorted log of the entire analysis process.
    - This log captures every event (raw peak detection, trough detection, BPM belief updates, etc.) and prints it to the console.
    - Crucially, it also saves this log to a separate, well-formatted **Markdown file** (e.g., `your_file_Debug_Log.md`), creating a permanent and detailed record of the algorithm's decisions for deep analysis.
### 🚀 Improvements
- **Visualization:**
    - The interactive plot now includes new traces for the detected **troughs** and the calculated **noise floor**.
    - Hover-labels for peaks in the plot are now multi-line for improved readability of complex decision reasons.

# Changelog: BPM Analysis Script
## Version 1.0
This version marks a significant advancement in noise handling and visualization. It introduces a fully dynamic noise floor and a proactive noise rejection system, making the beat detection far more robust in varied conditions.
### ✨ New Features
- **Dynamic Noise Floor:**
    - The previous static noise floor estimation has been upgraded to a **dynamic** system. It now calculates the noise floor using a rolling quantile over the detected signal troughs.
    - This allows the peak detection `height` threshold to adapt continuously throughout the audio file, making it more sensitive in quiet sections and more robust in noisy ones.
- **Intelligent Noise Rejection:**
    - The core algorithm now includes a new pre-emptive noise rejection step that runs _before_ S1-S2 pairing is attempted.
    - **Lookahead Amplitude Veto:** A peak is proactively rejected if the immediately following peak is substantially larger, preventing it from being considered in the pairing logic.
    - **Trough-based Noise Confidence:** The algorithm checks the amplitude of the trough preceding a peak. If the trough is significantly elevated above the local dynamic noise floor, the peak is classified as noise and rejected.
### 🚀 Improvements
- **Categorical Peak Visualization:**
    - The interactive plot has been completely overhauled to improve clarity. Instead of plotting all raw peaks as one series, it now classifies every detected peak as either **S1**, **S2**, or **Noise**.
    - Each category is plotted as a separate trace with a unique color and symbol, making it immediately obvious which peaks were kept, which were paired, and which were rejected.

# Changelog: BPM Analysis Script
## Version 1.1
This update focuses on significantly improving the quality, readability, and accuracy of the debug logging features, making it much easier to understand the algorithm's behavior.
### ✨ New Features
- **Chronological Debug Log Overhaul:**
    - The log generation logic has been completely refactored to be event-driven. It now gathers all significant events (classified peaks and troughs), sorts them chronologically, and generates a comprehensive report.
    - The output Markdown log (`_Debug_Log.md`) is now significantly more structured and readable. For each event, it displays the associated state of the algorithm (e.g., Audio Envelope, Noise Floor, Long-Term BPM) at that precise moment, making it much easier to trace the algorithm's state and decisions.
### 🐛 Bug Fixes
- **Log Parser Correction:** Fixed a critical bug in the debug log's text parser that caused it to incorrectly split the "reason" string when it contained decimal points. The parser is now more robust and formats the details correctly.
### 🚀 Improvements
- **Enhanced S2 Peak Information:** The debug information for S2 peaks (in both the plot's hover-label and the log) now includes the precise, high-precision timestamp of the S1 beat it was paired with, improving traceability.
- **Plotting Adjustments:** The default vertical axis range for the signal amplitude in the plot has been adjusted to provide better scaling and visualization by default.

# Changelog: BPM Analysis Script
## Version 1.2
This version further refines the intelligent noise rejection system with a more sophisticated, trough-aware lookahead veto and makes the noise confidence rule more flexible.
### ✨ New Features
- **Trough-based Lookahead Veto:**
    - The previous "Lookahead Amplitude Veto" has been replaced with a more robust, **trough-based** system.
    - Instead of just comparing the heights of two adjacent peaks, the new logic finds the trough _between_ them. It then compares how much each peak rises _above that trough_. A peak is now vetoed only if the subsequent peak has a significantly greater rise from the common trough, making the veto decision more resilient to baseline signal drift.
### 🚀 Improvements
- **S2 Exception for Noise Rule:**
    - The trough-based noise confidence rule, which rejects peaks in noisy areas, has been improved.
    - It now has a specific **exception** that prevents it from rejecting a peak if that peak falls within the expected time window for an S2 beat. This helps "rescue" valid S2 sounds that might occur during a noisy segment of the audio.

# Changelog: BPM Analysis Script
## Version 1.3
This version introduces a "Strong Peak Exception" to the noise rejection logic and enhances the detail in the debug outputs for better traceability.
### ✨ New Features
- **Strong Peak Exception for Noise Rule:**
    - A new exception has been added to the trough-based noise confidence system.
    - The algorithm now calculates a peak's amplitude relative to the local dynamic noise floor. If a peak is exceptionally prominent (e.g., more than 6 times the noise floor), it will bypass the noise rejection rule.
    - This prevents very strong, clear S1 beats from being accidentally discarded just because they occur in a segment with a high baseline noise level.
### 🚀 Improvements
- **Enhanced S2 Debug Information:** The debug information for S2 peaks has been improved. It now includes the full justification (confidence scores, BPM belief, etc.) that was used to make the original S1 pairing decision, providing complete context for why an S2 was identified.
- **Refined S2 Time Window:** The dynamic time window used to identify potential S2 peaks (`s1_s2_max_interval_sec`) has been slightly widened, making the algorithm a little more generous in its search for the second heart sound.
- **Code Refactoring:** The plotting and logging functions have been updated to correctly parse and display the new, more detailed S2 justification strings. The hover-label templates in the plot have also been unified for consistency.

# Changelog: BPM Analysis Script
## Version 1.4
This version introduces a final set of quality-of-life improvements to the GUI and internal code structure, marking a feature-complete milestone for this development cycle.
### ✨ New Features
- **Clear Button in GUI:** A "Clear" button has been added to the main application window. This allows the user to easily reset the selected file and analysis parameters without needing to restart the entire application, improving workflow when analyzing multiple files.
### 🚀 Improvements
- **Code Organization:** The entire script has been restructured using `#%%` cell separators. This divides the code into logical blocks (e.g., Audio Conversion, Preprocessing, Core Logic, GUI Class), making it significantly easier to navigate, read, and maintain within IDEs that support cell-based execution, such as VS Code or Spyder.
- **Analysis Engine Versioning:** The `find_heartbeat_peaks` function and all corresponding output titles (in plots and logs) now explicitly reference the analysis engine version number (e.g., v6.9). This ensures that all generated artifacts are traceable to the exact version of the algorithm that produced them.
- **GUI Code Cleanup:** Minor code cleanup and condensation have been applied within the `BPMApp` class to improve readability and maintainability.

# Changelog: BPM Analysis Script
## Version 1.5
This is a major architectural update focused on improving application stability, responsiveness, and maintainability. The core analysis logic is now decoupled from the user interface, and the project structure has been professionalized.
### ✨ New Features
- **Thread-Safe, Non-Blocking GUI:**
    - The entire analysis pipeline (file conversion, preprocessing, and beat detection) now runs on a separate background thread.
    - This prevents the graphical user interface from freezing or becoming unresponsive, even when processing very large audio files.
    - A `queue` is used to safely pass status updates, completion signals, and error messages from the background thread to the GUI for display.
- **Centralized Parameter Configuration:**
    - All tunable parameters for the analysis algorithm have been extracted and consolidated into a single `DEFAULT_PARAMS` dictionary at the top of the script.
    - This makes it significantly easier to experiment with and fine-tune the algorithm's behavior without having to search for values scattered throughout the code.
- **Professional Logging:**
    - All `print()` statements used for debugging have been replaced with Python's standard `logging` module.
    - This provides a more professional and structured logging output, including timestamps and log levels (e.g., INFO, WARNING, ERROR).
### 🚀 Improvements
- **Code Refactoring & Maintainability:**
    - The core `find_heartbeat_peaks` function has been refactored. The initial peak finding and noise floor calculation steps have been moved into their own dedicated helper functions (`_find_raw_peaks` and `_calculate_dynamic_noise_floor`), improving clarity and modularity.
    - The main analysis functions now accept the `params` dictionary, eliminating the need to pass numerous individual arguments.
- **GUI Status Updates:** The GUI status bar is now more informative, providing real-time updates as the analysis progresses through different stages (e.g., "Converting file...", "Processing and analyzing...").

# Changelog: BPM Analysis Script
## Version 1.6
This version focuses on improving the tunability and maintainability of the core algorithm by externalizing a key parameter and providing extensive documentation for all configuration settings.
### ✨ New Features
- **Tunable Lookahead Veto:** The multiplier used in the "Trough-based Lookahead Veto" is no longer a hardcoded value. It has been extracted into the `DEFAULT_PARAMS` dictionary as `trough_veto_multiplier`, allowing users to easily adjust the aggressiveness of this noise rejection heuristic.
### 🚀 Improvements
- **Exhaustive Parameter Documentation:** The `DEFAULT_PARAMS` dictionary has been thoroughly commented. Each parameter now has a detailed explanation of its function, its impact on the analysis, and the trade-offs involved in increasing or decreasing its value. This dramatically improves the usability and maintainability of the script for developers and advanced users.
- **S2 Beat Justification:** The full justification string (including confidence scores, BPM belief, etc.) for an S1-S2 pairing decision is now correctly stored for the S2 peak. This makes the reasoning for S2 classification fully visible in both the plot's hover-label and the Markdown debug log.
- **Algorithm Tuning:** The default `pairing_confidence_threshold` has been lowered from `0.6` to `0.55`, making the algorithm slightly more inclined to form S1-S2 pairs.

# Changelog: BPM Analysis Script
## Version 1.7
This version introduces a critical new outlier rejection system to prevent noise from creating impossible BPM spikes and further refines the core algorithm's logic.
### ✨ New Features
- **BPM Outlier Rejection:**
    - A new safety check has been integrated into the main classification loop. Before a peak is confirmed as a "Lone S1," the algorithm now calculates the instantaneous BPM that would result from its inclusion.
    - If this BPM is determined to be physiologically impossible (i.e., greater than a tunable multiple of the `max_bpm`), the peak is rejected as noise.
    - This significantly improves the robustness of the final BPM graph by preventing single, errant noise peaks from causing extreme, unrealistic spikes.
    - The sensitivity of this feature can be tuned via the new `max_bpm_rejection_factor` parameter in `DEFAULT_PARAMS`.
### 🚀 Improvements
- **Refined Pairing Logic:** The "Pattern Match Override" heuristic has been removed from the final pairing decision. A pairing is now determined exclusively by the time interval and the blended confidence score, simplifying the logic and relying more on the core stateful model.
- **Stateful Update Correction:** The logic for updating the `long_term_bpm` belief has been refactored to ensure it only runs _after_ a beat has been fully validated and added to the list of candidates, improving logical consistency and the accuracy of the belief state.
- **Algorithm Tuning:** The default `noise_confidence_threshold` has been lowered from `0.7` to `0.6`, making the trough-based noise rejection slightly more aggressive.

# Changelog: BPM Analysis Script
## Version 1.8
This version introduces Heart Rate Variability (HRV) analysis as a major new feature and replaces the previous outlier rejection system with a more sophisticated, dynamic model based on HRV principles.
### ✨ New Features
- **Heart Rate Variability (HRV) Analysis:**
    - The script now performs time-domain HRV analysis on the detected S1 beats.
    - A new function, `calculate_hrv_metrics`, has been added to compute two key metrics:
        - **SDNN** (Standard Deviation of NN intervals): An indicator of overall heart rate variability.
        - **RMSSD** (Root Mean Square of Successive Differences): A measure of short-term, high-frequency variability.
- **Analysis Summary Box in Plot:**
    - The results plot now includes a prominent **Analysis Summary** box in the top-left corner.
    - This box displays the key calculated metrics at a glance, including Avg/Min/Max BPM, SDNN, and RMSSD.
### 🚀 Improvements
- **Dynamic HRV-Based Outlier Rejection:**
    - The previous "BPM Outlier Rejection" logic, which used a static multiple of `max_bpm`, has been completely replaced.
    - The new system is more intelligent and context-aware. It rejects a potential beat if the resulting beat-to-beat (RR) interval represents a physiologically implausible percentage change from the _previous_ RR interval.
    - This allows the algorithm to follow gradual changes in heart rate while effectively rejecting sudden, sharp spikes caused by noise.
    - The sensitivity of this feature can be tuned via the new `rr_interval_max_decrease_pct` and `rr_interval_max_increase_pct` parameters.
### **Changelog: Heartbeat BPM Analyzer - Version 1.9**
This update introduces a more sophisticated multi-stage analysis pipeline, significantly improving the algorithm's robustness, accuracy, and ability to handle noisy or complex recordings without manual tuning.
#### **Major Enhancements**
- **Multi-Stage Analysis Pipeline:** The core analysis logic has been refactored from a single pass into a four-stage process to make more intelligent, context-aware decisions.
    1. **Stage 1: High-Confidence First Pass & Auto-BPM-Estimation:** The analyzer first performs a "high-confidence" pass with stricter parameters to find only the most obvious "anchor" beats. It uses the rhythm of these beats to automatically estimate a global BPM for the entire recording. This reduces the reliance on the optional "Starting BPM" hint.
    2. **Stage 2: Trough Sanitization & Refined Noise Floor:** The algorithm for calculating the dynamic noise floor has been completely redesigned. It now uses a "trough sanitization" technique to identify and discard false troughs (i.e., small divots within a larger heartbeat sound), resulting in a much more accurate and stable noise floor, especially in noisy audio.
    3. **Stage 3: Main Analysis Pass:** The primary beat detection and classification algorithm now runs using the refined inputs from the first two stages (the auto-estimated BPM and the sanitized noise floor), leading to more accurate S1/S2 pairing and noise rejection.
    4. **Stage 4: Rhythm-Based Post-Correction:** A new final pass has been added to validate the detected S1 beats based on rhythmic plausibility. If two beats are detected too close together, this stage intelligently discards the one with the lower amplitude, correcting for errors where a single beat was split into two.
#### **New Configuration Parameters**
- To support the new pipeline, several advanced parameters have been added to the `DEFAULT_PARAMS` dictionary for fine-tuning:
    - `trough_rejection_multiplier`: Controls the sensitivity of the new trough sanitization algorithm.
    - `rr_correction_threshold_pct`: Sets the threshold for the new rhythm-based post-correction pass.
    - `enable_bpm_boost`: Allows a specific heuristic in the pairing logic to be enabled or disabled for advanced testing.
#### **Minor Improvements**
- **Plotting:** The Y-axis of the interactive HTML plot now uses a percentile-based quantile for auto-scaling, making it more robust to single large outlier peaks in the audio envelope.
- **Parameter Tuning:** Minor adjustments were made to `trough_veto_multiplier` and `s1_s2_interval_rr_fraction` for better general performance.