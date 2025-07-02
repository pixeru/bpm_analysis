# config.py

DEFAULT_PARAMS = {
    # =================================================================================
    # 1. General & Preprocessing Settings
    # Controls the initial loading and filtering of the audio.
    # =================================================================================
    "downsample_factor": 300,     # Factor to reduce sample rate. Higher = faster processing, less detail.
    "bandpass_freqs": (20, 150),  # (low_hz, high_hz) for the bandpass filter.
    "save_filtered_wav": False,    # If True, saves a .wav file of the filtered audio for debugging.

    # =================================================================================
    # 2. Signal Feature Detection
    # Governs the initial identification of peaks and troughs in the audio envelope.
    # =================================================================================
    "min_peak_distance_sec": 0.05,      # Minimum time allowed between any two raw peaks.
    "peak_prominence_quantile": 0.1,    # How much a spike must stand out to be considered a 'peak'.
    "trough_prominence_quantile": 0.1,  # How much a dip must stand out to be considered a 'trough'.

    # =================================================================================
    # 3. Noise Estimation & Rejection
    # Rules for calculating the dynamic noise floor and vetoing noisy peaks.
    # =================================================================================
    # --- 3.1. Dynamic Noise Floor ---
    "noise_floor_quantile": 0.20,       # Quantile of troughs used to calculate the noise floor. (0.2 = 20th percentile).
    "noise_window_sec": 10,             # Rolling window (in seconds) for calculating the dynamic noise floor.
    "trough_rejection_multiplier": 4.0, # A trough N-times higher than the draft noise floor is rejected.

    # --- 3.2. Peak Noise Vetoing ---
    "noise_confidence_threshold": 0.6,  # A peak is rejected if its calculated "noise confidence" exceeds this.
    "trough_veto_multiplier": 2.1,      # Vetoes a small peak if the next peak is N-times larger.
    "trough_noise_multiplier": 3.0,     # Marks a peak as noisy if its preceding trough is N-times the noise floor.
    "strong_peak_override_ratio": 6.0,  # A peak N-times the noise floor will bypass noise-rejection rules.

    # =================================================================================
    # 4. S1/S2 Pairing & Confidence Engine
    # The core logic for identifying S1-S2 pairs based on timing and physiology.
    # =================================================================================
    # --- 4.1. Core Pairing Rules ---
    "pairing_confidence_threshold": 0.50, # Confidence score required to classify two peaks as an S1-S2 pair.
    "s1_s2_interval_cap_sec": 0.4,      # The absolute maximum time (seconds) allowed between S1 and S2.
    "s1_s2_interval_rr_fraction": 0.7,  # The S1-S2 interval cannot be longer than this fraction of the R-R interval.

    # --- 4.2. Amplitude-Based Confidence Model ---
    "deviation_smoothing_factor": 0.05, # Smoothing applied to the peak-to-peak amplitude deviation series.
    "confidence_deviation_points": [0.0, 0.25, 0.40, 0.80, 1.0], # X-axis for the confidence curves (normalized deviation).
    "confidence_curve_low_bpm": [0.9, 0.9, 0.7, 0.1, 0.1],      # Y-axis curve for LOW heart rates (rewards similar amplitude).
    "confidence_curve_high_bpm": [0.1, 0.5, 0.75, 0.65, 0],      # Y-axis curve for HIGH heart rates (rewards S1 > S2).

    # --- 4.3. Physiology-Based Confidence Adjustment ---
    "stability_history_window": 20,         # Number of recent beats used to determine rhythm stability.
    "stability_confidence_floor": 0.60,     # At 0% pairing success, confidence is multiplied by this (e.g., a 50% reduction).
    "stability_confidence_ceiling": 1.25,   # At 100% pairing success, confidence is multiplied by this (e.g., a 10% boost).
    "s1_s2_boost_ratio": 1.2,               # S1 strength must be > (S2 strength * this value) to get a confidence boost.
    "boost_amount_min": 0.10,               # Additive confidence boost for a "good" pair in an unstable section.
    "boost_amount_max": 0.35,               # Additive confidence boost for a "good" pair in a stable section.
    "penalty_amount_min": 0.10,             # Subtractive confidence penalty for a "bad" pair in a stable section.
    "penalty_amount_max": 0.30,             # Subtractive confidence penalty for a "bad" pair in an unstable section.
    "s2_s1_ratio_low_bpm": 1.5,             # At low BPM, allows S2 to be up to 1.5x S1 strength before penalty.
    "s2_s1_ratio_high_bpm": 1.1,            # At high BPM, expects S2 to be no more than 1.1x S1 strength.
    "contractility_bpm_low": 120.0,         # Below this BPM, the 'low BPM' confidence model is used.
    "contractility_bpm_high": 140.0,        # Above this BPM, the 'high BPM' confidence model is used.
    "recovery_phase_duration_sec": 120,     # Duration (seconds) of the high-contractility state after peak BPM.

    # --- 4.4. Interval-Based Confidence Penalty ---
    "interval_penalty_start_factor": 1.0,     # Penalty begins when interval > (max_interval * this value).
    "interval_penalty_full_factor": 1.4,      # Penalty is at max when interval > (max_interval * this value).
    "interval_max_penalty": 0.75,             # Max confidence points to subtract for a long interval.

    # --- 4.5. Kick-Start Mechanism to Recover from Pairing Failure ---
    "kickstart_check_threshold": 0.3,           # Only run the check if pairing_ratio is BELOW this value.
    "kickstart_history_beats": 4,               # How many of the most recent beats to check.
    "kickstart_min_s1_candidates": 3,           # At least this many of the recent beats must be "Lone S1s" to be considered.
    "kickstart_min_matches": 3,                 # How many must match the "S1 -> Noise" pattern to trigger.
    "kickstart_override_ratio": 0.60,           # The temporary pairing ratio to use if kick-start is triggered.

    # =================================================================================
    # 5. Rhythm Plausibility & Validation
    # Rules for the algorithm's long-term BPM belief and beat-to-beat timing checks.
    # =================================================================================
    # --- 5.1. Long-Term BPM Belief ---
    "long_term_bpm_learning_rate": 0.05,    # How quickly the BPM belief adapts to new beats.
    "max_bpm_change_per_beat": 3.0,         # "Speed limit" on how much the BPM belief can change per beat.
    "min_bpm": 40,                          # Absolute minimum BPM the algorithm will consider valid.
    "max_bpm": 240,                         # Absolute maximum BPM the algorithm will consider valid.

    # --- 5.2. Beat-to-Beat Validation ---
    "rr_interval_max_decrease_pct": 0.45, # A new R-R interval can't be more than 45% shorter than the previous one.
    "rr_interval_max_increase_pct": 0.70, # A new R-R interval can't be more than 70% longer than the previous one.
    "lone_s1_min_strength_ratio": 0.30,   # A Lone S1 candidate's strength must be at least this fraction of the previous S1's.
    "lone_s1_forward_check_pct": 0.50,    # A Lone S1 is rejected if the next peak is too close, implying a BPM spike.

    # --- 5.4. Lone S1 Gradient Confidence Engine ---
    "lone_s1_confidence_threshold": 0.50, # Final combined score needed to be accepted as a Lone S1.
    "lone_s1_rhythm_weight": 0.65,         # The weight given to the rhythmic timing score (0.0 to 1.0).
    "lone_s1_amplitude_weight": 0.35,      # The weight given to the amplitude consistency score.
    "lone_s1_rhythm_deviation_points": [0.0, 0.15, 0.30, 0.50], # X-axis: % deviation from expected RR interval.
    "lone_s1_rhythm_confidence_curve": [1.0, 0.8, 0.4, 0.0],   # Y-axis: Confidence score for rhythmic fit.
    "lone_s1_amplitude_ratio_points": [0.0, 0.4, 0.7, 1.0],   # X-axis: Strength ratio compared to previous S1.
    "lone_s1_amplitude_confidence_curve": [0.0, 0.4, 0.8, 1.0], # Y-axis: Confidence score for amplitude consistency.

    # =================================================================================
    # 6. Post-Processing Correction Pass
    # Final analysis pass to identify and fix rhythmic discontinuities.
    # =================================================================================
    "enable_correction_pass": False,
    "rr_correction_threshold_pct": 0.40,      # An R-R interval shorter than (Median R-R * this_value) is a "discontinuity".
    "rr_correction_long_interval_pct": 1.70,  # An R-R interval longer than (Median R-R * this_value) is a "gap".
    "penalty_waiver_strength_ratio": 4.0,     # Required signal-to-noise ratio for an S1 to be used in a correction.
    "penalty_waiver_max_s2_s1_ratio": 2.5,    # Safety rail: S2/S1 amp ratio must be below this to allow a correction.
    "correction_log_level": "DEBUG",          # Verbosity of the correction pass logs. Set to "INFO" or "DEBUG".

    # =================================================================================
    # 7. Output, HRV & Reporting
    # Controls for final calculations, reports, and plots.
    # =================================================================================
    "output_smoothing_window_sec": 5,        # Time window (seconds) for smoothing the final BPM curve for display.
    "hrv_window_size_beats": 40,             # Sliding window size (in beats) for HRV calculation.
    "hrv_step_size_beats": 5,                # How many beats the HRV window moves in each step.
    "plot_amplitude_scale_factor": 250.0,    # Adjusts the default y-axis range of the signal amplitude plot.
    "plot_downsample_audio_envelope": True,  # If True, downsamples audio line traces for faster plotting.
    "plot_downsample_factor": 5,             # The factor for downsampling plot traces (e.g., 5 = keep 1 of every 5 points).
}