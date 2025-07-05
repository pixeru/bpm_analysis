## Heartbeat BPM Analyzer: Code Documentation
This document provides a comprehensive explanation of the heartbeat analysis script. The script is designed to process audio recordings of heartbeats, track Beats Per Minute (BPM) over time, and provide detailed physiological insights, particularly accounting for changes during exercise and recovery.

---
### ## 1. Centralized Configuration (`DEFAULT_PARAMS`)
All major logic in the script is controlled by a centralized dictionary called `DEFAULT_PARAMS`. This approach allows for easy tuning and experimentation without altering the core code.

| Section                         | Purpose                                                                                       | Key Parameters                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **1. General & Preprocessing**  | Controls initial audio loading and filtering.                                                 | `downsample_factor`, `bandpass_freqs`                                                              |
| **2. Signal Feature Detection** | Governs the raw identification of peaks and troughs.                                          | `min_peak_distance_sec`, `peak_prominence_quantile`                                                |
| **3. Noise Estimation**         | Defines rules for calculating a dynamic noise baseline and rejecting noisy peaks.             | `noise_floor_quantile`, `noise_window_sec`, `trough_veto_multiplier`                               |
| **4. S1/S2 Pairing Engine**     | The core logic for identifying S1​-S2​ pairs using timing, physiology, and rhythm stability.  | `pairing_confidence_threshold`, `s1_s2_interval_cap_sec`, parameters for the "Contractility Model" |
| **5. Rhythm Plausibility**      | Rules for the algorithm's long-term BPM "belief" and beat-to-beat timing validation.          | `long_term_bpm_learning_rate`, `rr_interval_max_decrease_pct`                                      |
| **6. Post-Processing**          | Final analysis pass to identify and fix rhythmic discontinuities based on the overall rhythm. | `enable_correction_pass`, `rr_correction_threshold_pct`                                            |
| **7. Output & Reporting**       | Controls for final calculations (HRV) and the generation of plots and reports.                | `output_smoothing_window_sec`, `hrv_window_size_beats`                                             |


---
### ## 2. The Analysis Pipeline
The script processes the audio file in a multi-stage pipeline, where each stage refines the data for the next. This is orchestrated by the `analyze_wav_file` function.
#### Stage 1: Preprocessing and Dynamic Noise Floor Calculation
This initial stage prepares the audio for analysis and addresses the problem of inconsistent recording volume.
- **Function:** `preprocess_audio()`
- **Purpose:** To convert the raw audio into a clean, analyzable signal envelope.
- **Logic:**
    1. **Convert to WAV:** If the input is not a `.wav` file, it's converted to a single-channel (mono) WAV file using the `pydub` library.
    2. **Bandpass Filter:** The signal is filtered to keep only the frequencies relevant to heart sounds (typically 20-150 Hz), removing low-frequency hum and high-frequency noise.
    3. **Envelope Generation:** The absolute value of the filtered signal is taken, and a rolling average is applied to create a smooth "envelope" that represents the intensity of the heart sounds over time.
- **Function:** `_calculate_dynamic_noise_floor()`
- **Purpose:** To establish a dynamic baseline for noise, which adapts to changes in background noise (like breathing or stethoscope movement) but ignores a temporary spike in noise.
- **Logic:**
    1. **Find All Troughs:** It first identifies all local minima (troughs) in the audio envelope.
    2. **Create a Draft Floor:** It calculates a preliminary, rolling quantile of these troughs.
    3. **Sanitize Troughs:** It re-evaluates the troughs. Any trough that is too high above the _draft_ noise floor is rejected as being part of a temporary noise event, not the true background noise.
    4. **Calculate Final Floor:** A new, more accurate noise floor is calculated using only the sanitized, legitimate troughs. This final floor represents the true, shifting background noise of the recording.
#### Stage 2: The Main Analysis Pass & Peak Classification
This is the core of the script where peaks are classified as S1​, S2​, or Noise.
- **Function:** `find_heartbeat_peaks()`
- **Purpose:** To intelligently classify all detected peaks based on a combination of timing, amplitude relationships, and physiological models.
- **Key Implemented Logic:**
    1. **Raw Peak Detection:** All potential peaks standing above the dynamic noise floor are identified using `_find_raw_peaks`.
    2. **Stateful Classification Loop:** The script iterates through the peaks one by one, making decisions based on the context of the beats it has already classified.
    3. **Long-Term BPM Belief:** The script maintains a `long_term_bpm` variable, which acts as its "memory" or "belief" about the heart rate. This value is updated slowly with a learning rate (`long_term_bpm_learning_rate`) and has a built-in "speed limiter" (`max_bpm_change_per_beat`) to prevent single erroneous beats from derailing the analysis.
    4. **The "Contractility" Model:** This is the most critical component for adapting to exercise. It dynamically changes its expectations of the S1​/S2​ amplitude relationship based on the `long_term_bpm`.
        - **Blended Confidence Curve (`calculate_blended_confidence`):** The confidence score for a potential pair is calculated using a dynamic curve. At **low BPMs**, the curve rewards pairs where S1​ and S2​ have similar amplitudes. At **high BPMs**, it rewards pairs where S1​ is significantly louder than S2​.
        - **Stability & Ratio Adjustments (`_adjust_confidence_with_stability_and_ratio`):**
            - **Stability Pre-Adjustment:** The confidence is first adjusted based on the recent success rate of pairing. In a stable rhythm (many successful pairs), the script becomes more confident. In an unstable rhythm, it becomes more cautious.
            - **Dynamic Boost/Penalty:** A final adjustment is made based on the S1​/S2​ strength ratio. It compares the actual ratio to an _expected_ ratio that changes with BPM. For example, at high BPM, it strongly expects S1​ > S2​ and will penalize a pair that doesn't fit this model.
    5. **Noise Vetoing Rules:** Before a peak is even considered for pairing, it's checked against several noise rules:
        - `should_veto_by_lookahead()`: A small peak is rejected if the _next_ peak is significantly larger, assuming the small peak is just noise preceding a real beat.
        - `calculate_surrounding_trough_noise()`: A peak is marked as noisy if the troughs on either side of it are too high above the dynamic noise floor.
    6. **Lone S1​ Validation (`_validate_lone_s1`):** If a peak cannot be paired, it undergoes a series of checks before it can be classified as a "Lone S1​". It must be rhythmically plausible, have a reasonable amplitude compared to the previous S1​, and not be too close to the next raw peak (which would imply a sudden, unrealistic BPM spike).
#### Stage 3: Post-Processing Correction Passes
After the initial classification, the script runs correction passes that use the "big picture" context to find and fix errors.
- **Function:** `correct_peaks_by_rhythm()`
- **Purpose:** A simple, non-iterative cleanup pass to resolve obvious rhythmic conflicts.
- **Logic:** It calculates the median R-R interval for the entire recording. It then iterates through the S1 peaks and if it finds two that are too close together (e.g., closer than 40% of the median interval), it discards the one with the lower amplitude.
- **Function:** `_run_iterative_correction_pass()`
- **Purpose:** A more advanced, iterative pass to find and fix rhythmic discontinuities (the "notches" in the BPM graph caused by a missed or extra beat).
- **Logic:** This function runs in a loop until no more corrections are made:
    1. **Find Discontinuities:** It identifies two types of problems based on the stable R-R interval:
        - **Gaps:** An interval that is too long (e.g., > 1.7x the median), suggesting a missed beat.
        - **Conflicts:** An interval that is too short (e.g., < 0.4x the median), suggesting an extra, invalid beat.
    2. **Fix Gaps:** When a long gap is found, the script searches for any peaks within that gap that were previously labeled as `Noise`. It re-evaluates them under less strict conditions to see if one could be a valid beat that was missed.
    3. **Fix Conflicts:** When a short interval is found between two S1s, it re-evaluates if the second one could plausibly be the S2​ of the first.
    4. **Margin:** This logic is intelligently applied only to the middle of the recording, leaving the first and last few beats untouched to avoid errors at the edges where context is limited.
#### Stage 4: Final Metrics and Output Generation
Once the final, corrected list of S1​ peaks is established, the script calculates high-level metrics and generates reports.
- **HRV Calculation (`calculate_windowed_hrv`):**
    - It calculates **RMSSD** (Root Mean Square of Successive Differences) and **SDNN** (Standard Deviation of N-N intervals) in a sliding window.
    - Crucially, it calculates **`rmssdc`**, which is the RMSSD corrected for the mean R-R interval in that window. This provides a more comparable measure of HRV across different heart rates, as HRV naturally decreases when BPM increases.
- **Slope Analysis (`find_major_hr_inclines`, `find_peak_recovery_rate`, etc.):**
    - These functions analyze the final smoothed BPM curve to identify periods of significant, sustained heart rate increase (exertion) and decrease (recovery).
    - They also find the single steepest slope of exertion and recovery over a fixed window (e.g., 20 seconds), providing metrics on the heart's responsiveness.
- **Output Files:**
    1. **Interactive Plot (`..._bpm_plot.html`):** A Plotly graph showing the audio envelope, noise floor, all peak classifications (S1​, S2​, Noise), the final BPM curve, and HRV metrics. Hovering over any peak provides detailed debug information about why it was classified that way.
    2. **Analysis Summary (`..._Analysis_Summary.md`):** A clean, readable Markdown report with overall statistics (Avg/Min/Max BPM, HRR, average HRV) and tables detailing the steepest exertion/recovery periods.
    3. **Debug Log (`..._Debug_Log.md`):** A highly detailed, chronological log of every single peak and trough detected, along with the state of the algorithm (e.g., noise floor, BPM belief, deviation) at that exact moment.

