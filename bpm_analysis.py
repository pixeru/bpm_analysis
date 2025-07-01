import os
import warnings
import numpy as np
import pandas as pd
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, find_peaks
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import traceback
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
import datetime
import logging
import threading
import sys
import queue
import time

# --- Do not remove the debug code from this project! ---
# --- Setup Professional Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    stream=sys.stdout
)

# --- Audio Conversion (requires pydub/ffmpeg) ---
try:
    from pydub import AudioSegment
except ImportError:
    logging.warning("Pydub library not found. Please install with 'pip install pydub'")
    logging.warning("FFmpeg is also required for audio conversion (add to system PATH).")
    AudioSegment = None

# --- Centralized Configuration for Easy Tuning (don't remove the comments)---
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
    "penalty_amount_max": 0.25,             # Subtractive confidence penalty for a "bad" pair in an unstable section.
    "s2_s1_ratio_low_bpm": 1.5,             # At low BPM, allows S2 to be up to 1.5x S1 strength before penalty.
    "s2_s1_ratio_high_bpm": 1.1,            # At high BPM, expects S2 to be no more than 1.1x S1 strength.
    "contractility_bpm_low": 120.0,         # Below this BPM, the 'low BPM' confidence model is used.
    "contractility_bpm_high": 140.0,        # Above this BPM, the 'high BPM' confidence model is used.
    "recovery_phase_duration_sec": 120,     # Duration (seconds) of the high-contractility state after peak BPM.

    # --- 4.4. Kick-Start Mechanism to Recover from Pairing Failure ---
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
    "lone_s1_forward_check_pct": 0.60,    # A Lone S1 is rejected if the next peak is too close, implying a BPM spike.

    # =================================================================================
    # 6. Post-Processing Correction Pass
    # Final analysis pass to identify and fix rhythmic discontinuities.
    # =================================================================================
    "enable_correction_pass": True,
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

def convert_to_wav(file_path, target_path):
    if not AudioSegment:
        raise ImportError("Pydub/FFmpeg is required for audio conversion.")
    logging.info(f"Converting {os.path.basename(file_path)} to WAV format...")
    try:
        sound = AudioSegment.from_file(file_path)
        sound = sound.set_channels(1)
        sound.export(target_path, format="wav")
        return True
    except Exception as e:
        logging.error(f"Could not convert file {file_path}. Error: {e}")
        return False

def preprocess_audio(file_path, params):
    """Reads, filters, and prepares the audio envelope for analysis."""
    downsample_factor = params['downsample_factor']
    bandpass_freqs = params['bandpass_freqs']
    save_debug_file = params['save_filtered_wav']

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        sample_rate, audio_data = wavfile.read(file_path)
    if audio_data.ndim > 1:
        audio_data = np.mean(audio_data, axis=1)

    lowcut, highcut = bandpass_freqs

    # Check if the downsample factor is too aggressive for the filter settings.
    max_safe_downsample = int((sample_rate / (highcut * 2)) - 1)

    if downsample_factor > max_safe_downsample:
        logging.warning(
            f"Original 'downsample_factor' of {downsample_factor} is too high for a "
            f"{highcut}Hz filter with a {sample_rate}Hz sample rate."
        )
        downsample_factor = max(1, max_safe_downsample)
        logging.warning(f"Adjusting 'downsample_factor' to a safe value of {downsample_factor}.")

    if downsample_factor > 1:
        new_sample_rate = sample_rate // downsample_factor
        audio_downsampled = audio_data[::downsample_factor]
    else:
        new_sample_rate = sample_rate
        audio_downsampled = audio_data

    nyquist = 0.5 * new_sample_rate
    low, high = lowcut / nyquist, highcut / nyquist

    if high >= 1.0:
        raise ValueError(f"Cannot create a {highcut}Hz filter. The effective sample rate of {new_sample_rate}Hz is too low.")

    b, a = butter(2, [low, high], btype='band')
    audio_filtered = filtfilt(b, a, audio_downsampled)

    if save_debug_file:
        debug_path = f"{os.path.splitext(file_path)[0]}_filtered_debug.wav"
        normalized_audio = np.int16(audio_filtered / np.max(np.abs(audio_filtered)) * 32767)
        wavfile.write(debug_path, new_sample_rate, normalized_audio)

    audio_abs = np.abs(audio_filtered)
    window_size = new_sample_rate // 10
    audio_envelope = pd.Series(audio_abs).rolling(window=window_size, min_periods=1, center=True).mean().values

    return audio_envelope, new_sample_rate

def _calculate_dynamic_noise_floor(audio_envelope, sample_rate, params):
    """Calculates a dynamic noise floor based on a sanitized set of audio troughs."""
    min_peak_dist_samples = int(params['min_peak_distance_sec'] * sample_rate)
    trough_prom_thresh = np.quantile(audio_envelope, params['trough_prominence_quantile'])

    # --- STEP 1: Find all potential troughs initially ---
    all_trough_indices, _ = find_peaks(-audio_envelope, distance=min_peak_dist_samples, prominence=trough_prom_thresh)

    # If we don't have enough troughs to begin with, fall back to a simple static floor.
    if len(all_trough_indices) < 5:
        logging.warning("Not enough troughs found for sanitization. Using a static noise floor.")
        fallback_value = np.quantile(audio_envelope, params['noise_floor_quantile'])
        dynamic_noise_floor = pd.Series(fallback_value, index=np.arange(len(audio_envelope)))
        return dynamic_noise_floor, all_trough_indices

    # --- STEP 2: Create a preliminary 'draft' noise floor from ALL troughs ---
    # This draft version is used only to evaluate the troughs themselves.
    trough_series_draft = pd.Series(index=all_trough_indices, data=audio_envelope[all_trough_indices])
    dense_troughs_draft = trough_series_draft.reindex(np.arange(len(audio_envelope))).interpolate()
    noise_window_samples = int(params['noise_window_sec'] * sample_rate)
    quantile_val = params['noise_floor_quantile']
    draft_noise_floor = dense_troughs_draft.rolling(window=noise_window_samples, min_periods=3, center=True).quantile(quantile_val)
    draft_noise_floor = draft_noise_floor.bfill().ffill() # Fill any gaps

    # --- STEP 3: Sanitize the trough list ---
    # remove any toughs too far from the noise floor
    sanitized_trough_indices = []
    rejection_multiplier = params.get('trough_rejection_multiplier', 4.0)
    for trough_idx in all_trough_indices:
        trough_amp = audio_envelope[trough_idx]
        floor_at_trough = draft_noise_floor.iloc[trough_idx]
        # Keep the trough only if it's not too high above the draft floor
        if not pd.isna(floor_at_trough) and trough_amp <= (rejection_multiplier * floor_at_trough):
            sanitized_trough_indices.append(trough_idx)

    logging.info(f"Trough Sanitization: Kept {len(sanitized_trough_indices)} of {len(all_trough_indices)} initial troughs.")

    # --- STEP 4: Calculate more accurate noise floor using only sanitized troughs ---
    if len(sanitized_trough_indices) > 2:
        trough_series_final = pd.Series(index=sanitized_trough_indices, data=audio_envelope[sanitized_trough_indices])
        dense_troughs_final = trough_series_final.reindex(np.arange(len(audio_envelope))).interpolate()
        dynamic_noise_floor = dense_troughs_final.rolling(window=noise_window_samples, min_periods=3, center=True).quantile(quantile_val)
        dynamic_noise_floor = dynamic_noise_floor.bfill().ffill()
    else:
        # If sanitization removed too many troughs, it's safer to use the original draft floor.
        logging.warning("Not enough sanitized troughs remaining. Using non-sanitized floor as fallback.")
        dynamic_noise_floor = draft_noise_floor

    # Final check for any remaining null values
    if dynamic_noise_floor.isnull().all():
         fallback_val = np.quantile(audio_envelope, 0.1)
         dynamic_noise_floor = pd.Series(fallback_val, index=np.arange(len(audio_envelope)))

    return dynamic_noise_floor, np.array(sanitized_trough_indices)

def _find_raw_peaks(audio_envelope, height_threshold, params, sample_rate):
    """Finds all potential peaks above the given height threshold."""
    prominence_thresh = np.quantile(audio_envelope, params['peak_prominence_quantile'])
    min_peak_dist_samples = int(params['min_peak_distance_sec'] * sample_rate)

    peaks, _ = find_peaks(
        audio_envelope,
        height=height_threshold,
        prominence=prominence_thresh,
        distance=min_peak_dist_samples
    )
    logging.info(f"Found {len(peaks)} raw peaks using dynamic height threshold.")
    return peaks

def calculate_blended_confidence(deviation, bpm, params):
    """
    Calculates a confidence score for pairing two peaks based on amplitude deviation.
    This version dynamically constructs the confidence curve based on the current BPM
    to reflect physiological expectations (heart's contractility).
    """
    # Get the anchor points for our dynamic model from params
    bpm_points = [params['contractility_bpm_low'], params['contractility_bpm_high']]
    deviation_points = params['confidence_deviation_points']

    # Get the two boundary curves (for low and high BPM)
    curve_low = np.array(params['confidence_curve_low_bpm'])
    curve_high = np.array(params['confidence_curve_high_bpm'])

    # --- Create the Live Confidence Curve ---
    # Calculate how far the current BPM is into the transition zone (0.0 to 1.0)
    blend_ratio = np.clip((bpm - bpm_points[0]) / (bpm_points[1] - bpm_points[0]), 0, 1)

    # Linearly interpolate between the low and high curves to get the live curve
    live_confidence_curve = curve_low + (curve_high - curve_low) * blend_ratio

    final_confidence = np.interp(deviation, deviation_points, live_confidence_curve)

    return final_confidence

def should_veto_by_lookahead(current_peak_idx, next_peak_idx, sorted_troughs, audio_envelope, params):
    """Checks if a peak should be vetoed by the 'lookahead' rule."""
    trough_search_start_idx = np.searchsorted(sorted_troughs, current_peak_idx, side='right')

    if trough_search_start_idx < len(sorted_troughs):
        trough_between_idx = sorted_troughs[trough_search_start_idx]
        if trough_between_idx < next_peak_idx:
            current_peak_amp = audio_envelope[current_peak_idx]
            next_peak_amp = audio_envelope[next_peak_idx]
            trough_amp = audio_envelope[trough_between_idx]
            veto_multiplier = params['trough_veto_multiplier']

            # The core veto condition
            current_rel_amp = current_peak_amp - trough_amp
            next_rel_amp = next_peak_amp - trough_amp

            if veto_multiplier * current_rel_amp < next_rel_amp:
                reason = (
                    f"Noise (Vetoed by Lookahead).\n- Reason: Next peak is significantly larger.\n"
                    f"- veto_multiplier * (CurrentPeak - Trough) < (NextPeak - Trough)\n"
                    f"- Values: {veto_multiplier:.1f} * ({current_peak_amp:.0f} - {trough_amp:.0f}) < ({next_peak_amp:.0f} - {trough_amp:.0f})\n"
                    f"- Result: {veto_multiplier * current_rel_amp:.0f} < {next_rel_amp:.0f}"
                )
                return True, reason
    return False, ""

def calculate_surrounding_trough_noise(current_peak_idx, sorted_troughs, dynamic_noise_floor, audio_envelope, params):
    """
    Calculates a noise confidence score based on the amplitude of the troughs surrounding a peak.
    It checks the deeper of the two troughs (the local baseline) to see if it's noisy.
    """
    # Find the trough immediately before the current peak
    preceding_trough_search = np.searchsorted(sorted_troughs, current_peak_idx, side='left')
    # Find the trough immediately after the current peak
    following_trough_search = np.searchsorted(sorted_troughs, current_peak_idx, side='right')

    # Ensure that troughs exist on both sides of the peak
    if preceding_trough_search > 0 and following_trough_search < len(sorted_troughs):
        preceding_trough_idx = sorted_troughs[preceding_trough_search - 1]
        following_trough_idx = sorted_troughs[following_trough_search]

        preceding_trough_amp = audio_envelope[preceding_trough_idx]
        following_trough_amp = audio_envelope[following_trough_idx]

        # Determine which trough is the deeper valley (the local baseline)
        if preceding_trough_amp < following_trough_amp:
            min_trough_amp = preceding_trough_amp
            min_trough_idx = preceding_trough_idx
        else:
            min_trough_amp = following_trough_amp
            min_trough_idx = following_trough_idx

        # Now, perform the noise check on this local baseline trough
        noise_floor_at_trough = dynamic_noise_floor.iloc[min_trough_idx]
        trough_noise_multiplier = params['trough_noise_multiplier']

        if min_trough_amp > (noise_floor_at_trough * trough_noise_multiplier):
            reason = (
                f"Noise (High local noise confidence).\n"
                f"  - Reason: The baseline (min adjacent trough) before or after this peak is unusually loud.\n"
                f"  - Calculation: Min Trough Amp > (Noise Floor * Multiplier)\n"
                f"  - Values: {min_trough_amp:.0f} > ({noise_floor_at_trough:.0f} * {trough_noise_multiplier:.1f})\n"
                f"  - Result: {min_trough_amp:.0f} > {(noise_floor_at_trough * trough_noise_multiplier):.0f}"
            )
            return 0.8, reason
    return 0.0, ""

def update_long_term_bpm(new_rr_sec, current_long_term_bpm, params):
    """Updates the long-term BPM belief based on a new R-R interval."""
    instant_bpm = 60.0 / new_rr_sec
    lr = params['long_term_bpm_learning_rate']
    max_change_per_beat = params['max_bpm_change_per_beat']

    # Calculate the target BPM using an exponential moving average
    target_bpm = ((1 - lr) * current_long_term_bpm) + (lr * instant_bpm)

    # Limit how much the BPM can change in a single beat (a "speed limiter")
    max_change = max_change_per_beat * new_rr_sec # Scale limit by interval duration
    proposed_change = target_bpm - current_long_term_bpm
    limited_change = np.clip(proposed_change, -max_change, max_change)

    # Apply the limited change and enforce absolute min/max BPM boundaries
    new_bpm = current_long_term_bpm + limited_change
    return max(params['min_bpm'], min(new_bpm, params['max_bpm']))

def _calculate_pairing_ratio(candidate_beats, beat_debug_info, params):
    """Calculates the recent rhythm stability as a ratio from 0.0 to 1.0."""
    history_window = params.get("stability_history_window", 20)
    if len(candidate_beats) < history_window:
        # In the startup phase, assume moderate stability
        return 0.5

    recent_beats = candidate_beats[-history_window:]
    paired_count = sum(1 for beat_idx in recent_beats if "S1 (Paired)" in beat_debug_info.get(beat_idx, ""))
    return paired_count / history_window

def _adjust_confidence_with_stability_and_ratio(confidence, s1_idx, s2_idx, audio_envelope, dynamic_noise_floor,
                                               long_term_bpm, pairing_ratio, params, sample_rate,
                                               peak_bpm_time_sec, recovery_end_time_sec, beat_count):
    """Applies a full suite of confidence adjustments based on rhythm stability and S1/S2 strength ratio."""
    reason = ""

    # --- 1. Universal Stability Pre-Adjustment ---
    # Do not apply this logic for the first 5 beats, as the rhythm is not yet established.
    if beat_count >= 5:
        floor = params.get("stability_confidence_floor", 0.85)
        ceiling = params.get("stability_confidence_ceiling", 1.10)
        stability_factor = np.interp(pairing_ratio, [0.0, 1.0], [floor, ceiling])
        confidence *= stability_factor
        reason += f"\n- Stability Pre-Adjust: Confidence modified by {stability_factor:.2f}x based on pairing ratio of {pairing_ratio:.0%} to new confidence:{confidence:.0%}"

    # --- 2. Calculate Peak Strengths and Expected Ratio ---
    s1_strength = max(0, audio_envelope[s1_idx] - dynamic_noise_floor.iloc[s1_idx])
    s2_strength = max(0, audio_envelope[s2_idx] - dynamic_noise_floor.iloc[s2_idx])
    current_s2_s1_strength_ratio = s2_strength / (s1_strength + 1e-9)

    # Determine expected ratio based on BPM and recovery state
    is_in_recovery = (peak_bpm_time_sec is not None and recovery_end_time_sec is not None and
                      peak_bpm_time_sec < (s1_idx / sample_rate) < recovery_end_time_sec)
    effective_bpm = max(long_term_bpm, params['contractility_bpm_low']) if is_in_recovery else long_term_bpm
    max_expected_s2_s1_ratio = np.interp(effective_bpm,
                                       [params['contractility_bpm_low'], params['contractility_bpm_high']],
                                       [params['s2_s1_ratio_low_bpm'], params['s2_s1_ratio_high_bpm']])

    # --- 3. Apply Final Dynamic Boost or Penalty Amount ---
    if current_s2_s1_strength_ratio > max_expected_s2_s1_ratio:
        # PENALTY: S2 is stronger than expected.
        # The penalty is scaled by the severity of the violation.
        min_penalty = params.get("penalty_amount_min", 0.15)
        max_penalty = params.get("penalty_amount_max", 0.40)
        violation_severity = current_s2_s1_strength_ratio / max_expected_s2_s1_ratio

        # A minor violation (severity near 1.0) gets a small penalty.
        # A major violation (e.g., severity of 3.0 or more) gets the maximum penalty.
        # The divisor (2.0) controls how quickly the penalty ramps up; a smaller number means it ramps up faster.
        severity_scale = np.clip((violation_severity - 1.0) / 2.0, 0, 1)

        penalty_range = max_penalty - min_penalty
        penalty_amount = min_penalty + (severity_scale * penalty_range)

        confidence -= penalty_amount
        reason += f"\n- PENALIZED by {penalty_amount:.2f} (S2 strength ratio {current_s2_s1_strength_ratio:.1f}x > expected {max_expected_s2_s1_ratio:.1f}x)."

    elif s1_strength > (s2_strength * params.get('s1_s2_boost_ratio', 1.2)):
        # BOOST: S1 is clearly stronger. Boost is higher in stable sections.
        min_boost = params.get("boost_amount_min", 0.10)
        max_boost = params.get("boost_amount_max", 0.35)
        boost_amount = np.interp(pairing_ratio, [0.0, 1.0], [min_boost, max_boost])
        confidence += boost_amount
        actual_s1_s2_ratio = s1_strength / (s2_strength + 1e-9)
        reason += f"\n- BOOSTED by {boost_amount:.2f} (S1 strength {actual_s1_s2_ratio:.1f}x > S2)."

    return max(0.0, min(1.0, confidence)), reason # Ensure confidence stays between 0 and 1

def is_rhythmically_plausible(new_s1_idx, last_s1_idx, long_term_bpm, sample_rate, params):
    """
    Checks if a new S1 peak has a plausible R-R interval compared to the last beat.
    Returns: boolean of plausibility and a reason string if not plausible.
    """
    rr_interval_sec = (new_s1_idx - last_s1_idx) / sample_rate
    if rr_interval_sec <= 0:
        return False, "Negative/Zero RR Interval"

    expected_rr_sec = 60.0 / long_term_bpm
    min_plausible_rr = expected_rr_sec * (1 - params['rr_interval_max_decrease_pct'])
    max_plausible_rr = expected_rr_sec * (1 + params['rr_interval_max_increase_pct'])

    if not (min_plausible_rr <= rr_interval_sec <= max_plausible_rr):
        instant_bpm = 60.0 / rr_interval_sec
        reason = (f"RR interval from {last_s1_idx} to {new_s1_idx} ({rr_interval_sec:.3f}s) "
                  f"is outside plausible range [{min_plausible_rr:.3f}s - {max_plausible_rr:.3f}s] "
                  f"based on current BPM of {long_term_bpm:.1f}. "
                  f"Implies instant BPM of {instant_bpm:.0f}.")
        return False, reason
    return True, ""

def _validate_lone_s1(current_peak_idx, all_peaks, candidate_beats, long_term_bpm, audio_envelope,
                      dynamic_noise_floor, sample_rate, params):
    """
    Performs a series of checks to determine if a peak is a valid Lone S1.
    Returns a tuple: (is_valid: bool, rejection_reason: str)
    """
    # If this is the first beat, it's valid by default.
    if not candidate_beats:
        return True, ""

    # CHECK 1: Is it rhythmically plausible (looks backward)?
    plausible, rhythm_reason = is_rhythmically_plausible(
        current_peak_idx, candidate_beats[-1], long_term_bpm, sample_rate, params
    )
    if not plausible:
        return False, rhythm_reason

    # CHECK 2: Is its amplitude consistent with the previous beat?
    last_s1_idx = candidate_beats[-1]
    last_s1_strength = audio_envelope[last_s1_idx] - dynamic_noise_floor.iloc[last_s1_idx]
    current_peak_strength = audio_envelope[current_peak_idx] - dynamic_noise_floor.iloc[current_peak_idx]
    strength_ratio = current_peak_strength / (last_s1_strength + 1e-9)
    min_strength_ratio = params.get('lone_s1_min_strength_ratio', 0.25)

    if strength_ratio < min_strength_ratio:
        return False, f"Rejected Lone S1: Insufficient strength (Ratio {strength_ratio:.2f} < {min_strength_ratio:.2f})"

    # CHECK 3: Does it cause an immediate BPM spike (looks forward)?
    current_peak_all_peaks_idx = np.searchsorted(all_peaks, current_peak_idx)
    if current_peak_all_peaks_idx < len(all_peaks) - 1:
        next_raw_peak_idx = all_peaks[current_peak_all_peaks_idx + 1]
        forward_interval_sec = (next_raw_peak_idx - current_peak_idx) / sample_rate
        expected_rr_sec = 60.0 / long_term_bpm
        min_forward_interval = expected_rr_sec * params.get('lone_s1_forward_check_pct', 0.60)

        if forward_interval_sec < min_forward_interval:
            # --- Sanity Check ---
            # The interval is short. Before rejecting, check if the next peak is just insignificant noise.
            # If our current S1 peak is much stronger, we override the rejection.
            current_peak_amp = audio_envelope[current_peak_idx]
            next_peak_amp = audio_envelope[next_raw_peak_idx]

            # This ratio can be tuned in params, e.g., 1.7 means the current peak must be 70% stronger.
            rejection_override_ratio = 1.4

            # Only reject if the next peak is of similar or greater strength.
            if not (current_peak_amp > (next_peak_amp * rejection_override_ratio)):
                implied_bpm = 60.0 / forward_interval_sec if forward_interval_sec > 0 else float('inf')
                rejection_detail = (
                    f"Rejected Lone S1: Peak is too close to the next, implying an unrealistic BPM spike.\n"
                    f"  - Justification: Forward interval:{forward_interval_sec:.3f}s is < minimum allowed:({min_forward_interval:.3f}s).\n"
                    f"  - Implication: Instantaneous {implied_bpm:.0f}BPM, from the current trend of {long_term_bpm:.0f}BPM."
                )
                return False, rejection_detail
    # It passed all three checks
    return True, ""

def find_heartbeat_peaks(audio_envelope, sample_rate, params, start_bpm_hint=None, precomputed_noise_floor=None, precomputed_troughs=None,
                         peak_bpm_time_sec=None, recovery_end_time_sec=None):
    """ Main logic to classify raw peaks into S1, S2, and Noise by calling helper functions."""
    analysis_data = {}

    # Step 1: Setup
    if precomputed_noise_floor is not None and precomputed_troughs is not None:
        dynamic_noise_floor, trough_indices = precomputed_noise_floor, precomputed_troughs
    else:
        dynamic_noise_floor, trough_indices = _calculate_dynamic_noise_floor(audio_envelope, sample_rate, params)
    analysis_data['dynamic_noise_floor_series'] = dynamic_noise_floor
    analysis_data['trough_indices'] = trough_indices

    all_peaks = _find_raw_peaks(audio_envelope, dynamic_noise_floor.values, params, sample_rate)
    if len(all_peaks) < 2:
        return all_peaks, all_peaks, {"beat_debug_info": {}}

    # --- Calculate deviation based on peak "strength" over the noise floor ---
    noise_floor_at_peaks = dynamic_noise_floor.reindex(all_peaks, method='nearest').values
    peak_strengths = audio_envelope[all_peaks] - noise_floor_at_peaks
    peak_strengths[peak_strengths < 0] = 0 # Strength cannot be negative
    normalized_deviations = np.abs(np.diff(peak_strengths)) / (np.maximum(peak_strengths[:-1], peak_strengths[1:]) + 1e-9)

    deviation_times = (all_peaks[:-1] + all_peaks[1:]) / 2 / sample_rate
    deviation_series = pd.Series(normalized_deviations, index=deviation_times)

    smoothing_window_peaks = max(5, int(len(deviation_series) * params['deviation_smoothing_factor']))
    smoothed_dev_series = deviation_series.rolling(window=smoothing_window_peaks, min_periods=1, center=True).mean()

    analysis_data["deviation_series"] = smoothed_dev_series
    analysis_data["deviation_times"] = deviation_times


    # Step 2: Stateful classification loop
    long_term_bpm = float(start_bpm_hint) if start_bpm_hint else 80.0
    candidate_beats, beat_debug_info, long_term_bpm_history = [], {}, []
    sorted_troughs = sorted(trough_indices)
    consecutive_rr_rejections = 0
    i = 0
    while i < len(all_peaks):
        # --- DYNAMIC STABILITY CALCULATION ---
        pairing_ratio = _calculate_pairing_ratio(candidate_beats, beat_debug_info, params)

        # --- KICK-START MECHANISM ---
        # If pairing has failed consistently, look for a pattern of Lone S1 -> Noise,
        # which suggests S2s are being missed. If found, temporarily boost the pairing ratio.
        if pairing_ratio < params.get("kickstart_check_threshold", 0.3):
            history = params.get("kickstart_history_beats", 4)
            min_s1s = params.get("kickstart_min_s1_candidates", 3)
            min_matches = params.get("kickstart_min_matches", 3)

            if len(candidate_beats) >= history:
                # Get recent beats that were classified as Lone S1
                recent_lone_s1s = [
                    idx for idx in candidate_beats[-history:]
                    if "Lone S1" in beat_debug_info.get(idx, "")
                ]

                # For each Lone S1, check if the next raw peak was labeled as Noise
                if len(recent_lone_s1s) >= min_s1s:
                    matches = 0
                    for s1_idx in recent_lone_s1s:
                        current_raw_idx = np.searchsorted(all_peaks, s1_idx)
                        if current_raw_idx < len(all_peaks) - 1:
                            next_raw_peak_idx = all_peaks[current_raw_idx + 1]
                            if "Noise" in beat_debug_info.get(next_raw_peak_idx, ""):
                                matches += 1

                    # If the pattern is consistent, trigger the kick-start
                    if matches >= min_matches:
                        override_ratio = params.get("kickstart_override_ratio", 0.6)
                        logging.info(
                            f"KICK-START: Found {matches}/{len(recent_lone_s1s)} S1->Noise patterns. "
                            f"Temporarily overriding pairing ratio from {pairing_ratio:.2f} to {override_ratio}."
                        )
                        pairing_ratio = override_ratio

        current_peak_idx = all_peaks[i]
        reason = ""

        # --- A. Initial checks for noise before attempting to pair ---
        s1_s2_max_interval = min(params['s1_s2_interval_cap_sec'], (60.0/long_term_bpm) * params['s1_s2_interval_rr_fraction'])
        is_potential_s2 = candidate_beats and (current_peak_idx - candidate_beats[-1]) / sample_rate <= s1_s2_max_interval

        if i < len(all_peaks) - 1 and not is_potential_s2:
            vetoed, veto_reason = should_veto_by_lookahead(current_peak_idx, all_peaks[i+1], sorted_troughs, audio_envelope, params)
            if vetoed:
                beat_debug_info[current_peak_idx] = veto_reason
                i += 1
                continue

        noise_confidence, noise_reason_str = calculate_surrounding_trough_noise(current_peak_idx, sorted_troughs, dynamic_noise_floor, audio_envelope, params)
        if noise_confidence > 0:
            reason += "| Preceding trough is noisy "

        peak_to_floor_ratio = audio_envelope[current_peak_idx] / (dynamic_noise_floor.iloc[current_peak_idx] + 1e-9)
        strong_peak_override = peak_to_floor_ratio >= params['strong_peak_override_ratio']

        if noise_confidence > params['noise_confidence_threshold'] and not is_potential_s2 and not strong_peak_override:
            beat_debug_info[current_peak_idx] = noise_reason_str
            i += 1
            continue

        # --- B. Main Pairing or Lone S1 Logic ---
        if i >= len(all_peaks) - 1:
            candidate_beats.append(current_peak_idx)
            beat_debug_info[current_peak_idx] = "Lone S1 (Last Peak)"
            i += 1
        else:
            next_peak_idx = all_peaks[i + 1]
            interval_sec = (next_peak_idx - current_peak_idx) / sample_rate
            current_time = current_peak_idx / sample_rate
            deviation_value = smoothed_dev_series.asof(current_time)

            # --- Calculate base confidence ---
            base_confidence = calculate_blended_confidence(deviation_value, long_term_bpm, params)
            reason += f"| Base Conf: {base_confidence:.2f} (vs Threshold: {params['pairing_confidence_threshold']:.2f}) "

            # --- Apply the new unified adjustment logic ---
            final_confidence, adjust_reason = _adjust_confidence_with_stability_and_ratio(
                base_confidence, current_peak_idx, next_peak_idx, audio_envelope,
                dynamic_noise_floor, long_term_bpm, pairing_ratio, params,
                sample_rate, peak_bpm_time_sec, recovery_end_time_sec, len(candidate_beats)
            )
            reason += adjust_reason

            is_paired = interval_sec <= s1_s2_max_interval and final_confidence >= params['pairing_confidence_threshold']

            if is_paired:
                candidate_beats.append(current_peak_idx)
                beat_debug_info[current_peak_idx] = f"S1 (Paired). {reason.lstrip(' |')}"
                beat_debug_info[next_peak_idx] = f"S2 (Paired). Justification: {reason.lstrip(' |')}"
                consecutive_rr_rejections = 0 # Reset counter on a successful pair
                i += 2
            else:
                # --- LONE S1 VALIDATION ---
                is_valid, rejection_detail = _validate_lone_s1(
                    current_peak_idx, all_peaks, candidate_beats, long_term_bpm,
                    audio_envelope, dynamic_noise_floor, sample_rate, params
                )

                if is_valid:
                    candidate_beats.append(current_peak_idx)
                    beat_debug_info[current_peak_idx] = f"Lone S1. {reason.lstrip(' |')}"
                    consecutive_rr_rejections = 0 # Reset counter on a successful beat
                else:
                    # Cascade failure reset logic
                    is_rr_rejection = "outside plausible range" in rejection_detail
                    trigger_count = params.get("cascade_reset_trigger_count", 2)

                    if is_rr_rejection and consecutive_rr_rejections >= trigger_count:
                        # We've failed multiple times in a row. Override the rejection to re-anchor the rhythm.
                        logging.info(
                            f"CASCADE RESET: Forcing peak at {current_peak_idx/sample_rate:.2f}s as Lone S1 to break failure loop."
                        )
                        candidate_beats.append(current_peak_idx)
                        beat_debug_info[current_peak_idx] = f"Lone S1 (Corrected by Cascade Reset). Original Rejection: [{rejection_detail}]"
                        consecutive_rr_rejections = 0 # Reset counter after the correction
                    else:
                        # Standard rejection logic
                        beat_debug_info[current_peak_idx] = f"Noise ({rejection_detail}). Original pairing reason: [{reason.lstrip(' |')}]"
                        if is_rr_rejection:
                            consecutive_rr_rejections += 1
                        else:
                            consecutive_rr_rejections = 0 # Reset if it was rejected for a different reason
                i += 1

        # --- C. Update Long-Term BPM Belief ---
        if len(candidate_beats) > 1:
            new_rr = (candidate_beats[-1] - candidate_beats[-2]) / sample_rate
            if new_rr > 0:
                long_term_bpm = update_long_term_bpm(new_rr, long_term_bpm, params)
        if candidate_beats:
            long_term_bpm_history.append((candidate_beats[-1] / sample_rate, long_term_bpm))

    # --- D. Finalize and return results ---
    final_peaks = np.array(sorted(list(dict.fromkeys(candidate_beats))))
    analysis_data["beat_debug_info"] = beat_debug_info
    if long_term_bpm_history:
        lt_bpm_times, lt_bpm_values = zip(*long_term_bpm_history)
        analysis_data["long_term_bpm_series"] = pd.Series(lt_bpm_values, index=lt_bpm_times)
    else:
        analysis_data["long_term_bpm_series"] = pd.Series(dtype=np.float64)

    return final_peaks, all_peaks, analysis_data


def correct_peaks_by_rhythm(peaks, audio_envelope, sample_rate, params):
    """
    Refines a list of S1 peaks by removing rhythmically implausible beats.
    If two beats are too close together, the one with the lower amplitude is discarded.
    """
    # If we have too few peaks, correction is unreliable and unnecessary.
    if len(peaks) < 5:
        return peaks

    logging.info(f"--- STAGE 4: Correcting peaks based on rhythm. Initial count: {len(peaks)} ---")

    # Calculate the median R-R interval to establish a stable rhythmic expectation.
    rr_intervals_sec = np.diff(peaks) / sample_rate
    median_rr_sec = np.median(rr_intervals_sec)

    # Any interval shorter than this threshold is considered a conflict.
    correction_threshold_sec = median_rr_sec * params.get("rr_correction_threshold_pct", 0.6)
    logging.info(f"Median R-R: {median_rr_sec:.3f}s. Correction threshold: {correction_threshold_sec:.3f}s.")

    # We build a new list of corrected peaks. Start with the first peak as a given.
    corrected_peaks = [peaks[0]]

    # Iterate through the original peaks, starting from the second one.
    for i in range(1, len(peaks)):
        current_peak = peaks[i]
        last_accepted_peak = corrected_peaks[-1]
        interval_sec = (current_peak - last_accepted_peak) / sample_rate
        if interval_sec < correction_threshold_sec:
            # CONFLICT: The current peak is too close to the last accepted one.
            # We must decide which one to keep. The one with the higher amplitude wins.
            last_peak_amp = audio_envelope[last_accepted_peak]
            current_peak_amp = audio_envelope[current_peak]
            if current_peak_amp > last_peak_amp:
                # The current peak is stronger, so it REPLACES the last accepted peak.
                logging.info(f"Conflict at {current_peak/sample_rate:.2f}s. Replaced previous peak at {last_accepted_peak/sample_rate:.2f}s due to higher amplitude.")
                corrected_peaks[-1] = current_peak
            else:
                # The last accepted peak was stronger, so we DISCARD the current peak.
                logging.info(f"Conflict at {current_peak/sample_rate:.2f}s. Discarding current peak due to lower amplitude.")
                pass  # Do nothing, effectively dropping the current_peak
        else:
            # NO CONFLICT: The interval is plausible. Add the peak to our corrected list.
            corrected_peaks.append(current_peak)

    final_peak_count = len(corrected_peaks)
    if final_peak_count < len(peaks):
        logging.info(f"Correction complete. Removed {len(peaks) - final_peak_count} peak(s). Final count: {final_peak_count}")
    else:
        logging.info("Correction pass complete. No rhythmic conflicts found.")
    return np.array(corrected_peaks)

def _fix_rhythmic_discontinuities(s1_peaks, all_raw_peaks, debug_info, audio_envelope, dynamic_noise_floor, params, sample_rate):
    """
    Identifies and attempts to fix rhythmic discontinuities by re-evaluating misclassified peaks.
    Includes a margin at the start and end to prevent corrections there.
    """
    log_level = params.get("correction_log_level", "INFO").upper()
    def log_debug(msg):
        if log_level == "DEBUG":
            logging.info(f"[Correction DEBUG] {msg}")

    # Define a margin of beats to leave untouched at the start and end of the recording.
    margin = 3

    # If the recording is too short to have a "middle" section, skip the correction pass.
    if len(s1_peaks) < margin * 2:
        log_debug(f"Skipping correction pass: Not enough S1 peaks ({len(s1_peaks)}) to apply a margin of {margin}.")
        return s1_peaks, debug_info, 0

    rr_intervals_sec = np.diff(s1_peaks) / sample_rate
    q1, q3 = np.percentile(rr_intervals_sec, [25, 75])
    iqr = q3 - q1
    stable_rr_intervals = rr_intervals_sec[(rr_intervals_sec > (q1 - 1.5 * iqr)) & (rr_intervals_sec < (q3 + 1.5 * iqr))]

    if len(stable_rr_intervals) < 1:
        log_debug("Not enough stable R-R intervals to determine median. Skipping correction.")
        return s1_peaks, debug_info, 0

    median_rr_sec = np.median(stable_rr_intervals)
    short_conflict_threshold_sec = median_rr_sec * params["rr_correction_threshold_pct"]
    long_conflict_threshold_sec = median_rr_sec * params.get("rr_correction_long_interval_pct", 1.7)

    log_debug(f"Median R-R: {median_rr_sec:.3f}s. Short Threshold: < {short_conflict_threshold_sec:.3f}s. Long Threshold: > {long_conflict_threshold_sec:.3f}s.")

    corrected_debug_info = debug_info.copy()
    peaks_to_add = set()
    peaks_to_remove = set()
    corrections_made = 0

    # --- Pass 1: Look for LONG intervals (missed beats) ---
    log_debug(f"Checking for long intervals between beat {margin} and beat {len(s1_peaks) - margin}...")
    for i in range(margin, len(s1_peaks) - 1 - margin):
        s1_start_idx = s1_peaks[i]
        s1_end_idx = s1_peaks[i+1]
        interval_sec = (s1_end_idx - s1_start_idx) / sample_rate

        if interval_sec > long_conflict_threshold_sec:
            log_debug(f"Found LONG interval of {interval_sec:.3f}s between beats at {s1_start_idx/sample_rate:.2f}s and {s1_end_idx/sample_rate:.2f}s. Investigating gap...")

            gap_candidates = [p for p in all_raw_peaks if s1_start_idx < p < s1_end_idx and "Noise" in debug_info.get(p, "")]
            log_debug(f"Found {len(gap_candidates)} potential candidates in the gap.")

            for j, candidate_s1 in enumerate(gap_candidates):
                if candidate_s1 in peaks_to_add or candidate_s1 in peaks_to_remove:
                    continue
                log_debug(f"  - Evaluating candidate S1 at {candidate_s1/sample_rate:.2f}s")
                current_raw_idx = np.searchsorted(all_raw_peaks, candidate_s1)
                if current_raw_idx + 1 >= len(all_raw_peaks):
                    log_debug(f"    - SKIPPING: This is the last raw peak in the recording; no S2 can follow.")
                    continue
                candidate_s2 = all_raw_peaks[current_raw_idx + 1]
                if candidate_s2 > s1_end_idx:
                    reason = f"REJECTED: Its potential S2 at {candidate_s2/sample_rate:.2f}s is outside the current gap (which ends at {s1_end_idx/sample_rate:.2f}s)."
                    log_debug(f"    - {reason}")
                    corrected_debug_info[candidate_s1] += f" | Correction Pass: {reason}"
                    continue
                if "Noise" not in debug_info.get(candidate_s2, ""):
                    s2_original_label = debug_info.get(candidate_s2, "Unknown")
                    reason = f"REJECTED: Its potential S2 at {candidate_s2/sample_rate:.2f}s was not labeled 'Noise' (it was '{s2_original_label}')."
                    log_debug(f"    - {reason}")
                    corrected_debug_info[candidate_s1] += f" | Correction Pass: {reason}"
                    continue
                log_debug(f"    - Found potential S2 partner at {candidate_s2/sample_rate:.2f}s. Checking safety waivers...")
                s1_amp = audio_envelope[candidate_s1]
                s2_amp = audio_envelope[candidate_s2]
                noise_at_s1 = dynamic_noise_floor.iloc[candidate_s1]
                is_strong_s1 = (s1_amp - noise_at_s1) > (params["penalty_waiver_strength_ratio"] * noise_at_s1)
                is_ratio_plausible = (s2_amp / (s1_amp + 1e-9)) < params["penalty_waiver_max_s2_s1_ratio"]
                strength_msg = f"Strength check: {'PASS' if is_strong_s1 else 'FAIL'}"
                ratio_msg = f"Ratio check: {'PASS' if is_ratio_plausible else 'FAIL'}"
                log_debug(f"      - {strength_msg}. {ratio_msg}.")
                if is_strong_s1 and is_ratio_plausible:
                    log_debug(f"      - SUCCESS: Conditions met. Re-labeling pair.")
                    corrections_made += 1
                    peaks_to_add.add(candidate_s1)
                    peaks_to_remove.add(candidate_s2)
                    base_reason_A = corrected_debug_info.get(candidate_s1, "Noise").split(". Original: [")[0]
                    corrected_debug_info[candidate_s1] = f"S1 (Paired - Corrected from Gap). Original: [{base_reason_A}]"
                    base_reason_B = corrected_debug_info.get(candidate_s2, "Noise").split(". Original: [")[0]
                    corrected_debug_info[candidate_s2] = f"S2 (Paired - Corrected from Gap). Original: [{base_reason_B}]"
                    break
                else:
                    corrected_debug_info[candidate_s1] += f" | Correction Pass: REJECTED ({strength_msg}, {ratio_msg})"

    # --- Pass 2: Look for SHORT intervals (adjacent S1s) ---
    temp_s1_list = sorted(list(set(s1_peaks) | peaks_to_add))
    if not temp_s1_list: return np.array([]), corrected_debug_info, corrections_made

    # Initialize the final list with the first `margin` beats, which are accepted without checking.
    final_s1_peaks = temp_s1_list[:margin]
    log_debug(f"Auto-accepted first {margin} beats. Starting SHORT interval check...")

    # Iterate only over the middle section, comparing each candidate to the last accepted peak.
    for i in range(margin, len(temp_s1_list) - margin):
        beat_A_idx = final_s1_peaks[-1]
        beat_B_idx = temp_s1_list[i]
        interval_sec = (beat_B_idx - beat_A_idx) / sample_rate

        if interval_sec < short_conflict_threshold_sec:
            log_debug(f"Found SHORT interval of {interval_sec:.3f}s between beats at {beat_A_idx/sample_rate:.2f}s and {beat_B_idx/sample_rate:.2f}s. Evaluating...")
            s1_amp = audio_envelope[beat_A_idx]
            s2_amp = audio_envelope[beat_B_idx]
            noise_at_s1 = dynamic_noise_floor.iloc[beat_A_idx]
            is_strong_s1 = (s1_amp - noise_at_s1) > (params["penalty_waiver_strength_ratio"] * noise_at_s1)
            is_ratio_plausible = (s2_amp / (s1_amp + 1e-9)) < params["penalty_waiver_max_s2_s1_ratio"]
            log_debug(f"  - Strength check: {'PASS' if is_strong_s1 else 'FAIL'}. Ratio check: {'PASS' if is_ratio_plausible else 'FAIL'}.")

            if is_strong_s1 and is_ratio_plausible:
                log_debug(f"  - SUCCESS: Conditions met. Re-labeling Beat B as S2.")
                corrections_made += 1
                base_reason_B = corrected_debug_info.get(beat_B_idx, "Lone S1").split(". Original: [")[0]
                corrected_debug_info[beat_B_idx] = f"S2 (Paired - Corrected from Conflict). Original: [{base_reason_B}]"
            else:
                if s2_amp > s1_amp:
                    log_debug(f"  - UNRESOLVABLE: Keeping stronger peak at {beat_B_idx/sample_rate:.2f}s.")
                    final_s1_peaks[-1] = beat_B_idx
                else:
                    log_debug(f"  - UNRESOLVABLE: Keeping stronger peak at {beat_A_idx/sample_rate:.2f}s.")
                    pass
        else:
            final_s1_peaks.append(beat_B_idx)

    # Append the last `margin` beats, which are also accepted without being checked.
    final_s1_peaks.extend(temp_s1_list[-margin:])
    log_debug(f"Auto-accepted last {margin} beats. Short interval check complete.")

    return np.array(sorted(final_s1_peaks)), corrected_debug_info, corrections_made

def calculate_windowed_hrv(s1_peaks, sample_rate, params):
    """ Calculates HRV metrics using R-R intervals based on changing heart rate """
    window_size_beats = params['hrv_window_size_beats']
    step_size_beats = params['hrv_step_size_beats']

    # First, calculate all R-R intervals from the S1 peaks
    if len(s1_peaks) < window_size_beats:
        logging.warning(f"Not enough beats ({len(s1_peaks)}) to perform windowed HRV analysis with a window of {window_size_beats} beats.")
        return pd.DataFrame(columns=['time', 'rmssdc', 'sdnn', 'bpm'])

    rr_intervals_sec = np.diff(s1_peaks) / sample_rate
    s1_times_sec = s1_peaks / sample_rate

    results = []
    # Iterate through the R-R intervals with a sliding window
    for i in range(0, len(rr_intervals_sec) - window_size_beats + 1, step_size_beats):
        window_rr_sec = rr_intervals_sec[i : i + window_size_beats]
        window_rr_ms = window_rr_sec * 1000
        start_time = s1_times_sec[i]
        end_time = s1_times_sec[i + window_size_beats]
        window_mid_time = (start_time + end_time) / 2.0

        # --- Calculate HRV Metrics for the Window ---
        mean_rr_ms = np.mean(window_rr_ms)
        sdnn = np.std(window_rr_ms)
        successive_diffs_ms = np.diff(window_rr_ms)
        rmssd = np.sqrt(np.mean(successive_diffs_ms**2))

        # --- Calculate Corrected RMSSD (RMSSDc) ---
        mean_rr_sec = mean_rr_ms / 1000.0
        rmssdc = rmssd / mean_rr_sec if mean_rr_sec > 0 else 0

        # Calculate the average BPM within this specific window
        window_bpm = 60 / mean_rr_sec if mean_rr_sec > 0 else 0

        results.append({
            'time': window_mid_time,
            'rmssdc': rmssdc,
            'sdnn': sdnn,
            'bpm': window_bpm
        })

    if not results:
        logging.warning("Could not perform windowed HRV analysis. Recording may be too short or have too few beats.")
        return pd.DataFrame(columns=['time', 'rmssdc', 'sdnn', 'bpm'])

    logging.info(f"Beat-based windowed HRV analysis complete. Generated {len(results)} data points.")
    return pd.DataFrame(results)

def calculate_bpm_series(peaks, sample_rate, params):
    """Calculates and smooths the final BPM series from S1 peaks."""
    if len(peaks) < 2: return pd.Series(dtype=np.float64), np.array([])
    peak_times = peaks / sample_rate
    time_diffs = np.diff(peak_times)
    valid_diffs = time_diffs > 1e-6
    if not np.any(valid_diffs): return pd.Series(dtype=np.float64), np.array([])

    instant_bpm = 60.0 / time_diffs[valid_diffs]
    start_time = datetime.datetime.fromtimestamp(0)
    valid_peak_times_dt = [start_time + datetime.timedelta(seconds=t) for t in peak_times[1:][valid_diffs]]
    bpm_series = pd.Series(instant_bpm, index=valid_peak_times_dt)
    avg_heart_rate = np.median(instant_bpm)
    if avg_heart_rate > 0:
        smoothing_window_sec = params['output_smoothing_window_sec']
        smoothing_window_str = f"{smoothing_window_sec}s"
        smoothed_bpm = bpm_series.rolling(window=smoothing_window_str, min_periods=1, center=True).mean()
    else:
        smoothed_bpm = pd.Series(dtype=np.float64)

    # Return the original numpy time points for compatibility with older functions that need it
    return smoothed_bpm, peak_times[1:][valid_diffs]

# --- Plotting Helper Functions ---
def _add_base_traces(fig, time_axis_dt, audio_envelope, analysis_data, params):
    """Adds the audio envelope, troughs, and noise floor traces to the plot."""

    # --- Prepare data for plotting ---
    plot_time_axis_dt = time_axis_dt
    plot_envelope = audio_envelope
    plot_noise_floor = analysis_data.get('dynamic_noise_floor_series')

    if params.get("plot_downsample_audio_envelope", False):
        factor = params.get("plot_downsample_factor", 5)
        if factor > 1 and len(audio_envelope) > factor:
            logging.info(f"Downsampling line traces by a factor of {factor} for plotting.")
            plot_time_axis_dt = time_axis_dt[::factor]
            plot_envelope = audio_envelope[::factor]
            if plot_noise_floor is not None and not plot_noise_floor.empty:
                plot_noise_floor = plot_noise_floor.iloc[::factor]

    # Add the potentially downsampled line traces
    fig.add_trace(go.Scatter(x=plot_time_axis_dt, y=plot_envelope, name="Audio Envelope", line=dict(color="#47a5c4")), secondary_y=False)
    if plot_noise_floor is not None and not plot_noise_floor.empty:
        fig.add_trace(go.Scatter(
            x=plot_time_axis_dt, y=plot_noise_floor.values, name="Dynamic Noise Floor",
            line=dict(color="green", dash="dot", width=1.5), hovertemplate="Noise Floor: %{y:.2f}<extra></extra>"
        ), secondary_y=False)

    # Add the trough markers using original full-resolution data for accuracy
    if 'trough_indices' in analysis_data and analysis_data['trough_indices'].size > 0:
        trough_indices = analysis_data['trough_indices']
        start_datetime = datetime.datetime.fromtimestamp(0)
        trough_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (trough_indices / analysis_data['sample_rate'])])
        fig.add_trace(go.Scatter(
            x=trough_times_dt, y=audio_envelope[trough_indices], mode='markers', name='Troughs',
            marker=dict(color='green', symbol='circle-open', size=6), visible='legendonly'
        ), secondary_y=False)

def _categorize_peaks(all_raw_peaks, debug_info, audio_envelope, sample_rate):
    """Categorizes raw peaks into S1, S2, and Noise for plotting."""
    all_peaks_data = {'S1': {'indices': [], 'customdata': []}, 'S2': {'indices': [], 'customdata': []}, 'Noise': {'indices': [], 'customdata': []}}
    for p_idx in all_raw_peaks:
        reason_str = debug_info.get(p_idx, 'Unknown')
        category = 'Noise'
        if reason_str.startswith('S1') or reason_str.startswith('Lone S1'): category = 'S1'
        elif reason_str.startswith('S2'): category = 'S2'

        peak_type, reason_details = reason_str, ""
        if '. Justification: ' in reason_str and category == 'S2':
            parts = reason_str.split('. Justification: ', 1)
            peak_type, details = parts[0].strip(), parts[1].strip().replace(' | ', '<br>- ').replace('\n', '<br>')
            reason_details = f"<b>Justification:</b><br>- {details}"
        elif '. ' in reason_str:
            parts = reason_str.split('. ', 1)
            peak_type, reason_details = parts[0].strip(), parts[1].strip().replace(' | ', '<br>- ').replace('\n', '<br>')
        elif '(' in reason_str and ')' in reason_str:
            parts = reason_str.split('(', 1)
            peak_type = parts[0].strip()
            details_part = parts[1].rsplit(')', 1)[0]
            reason_details = details_part.strip().replace(' | ', '<br>- ').replace('\n', '<br>')

        custom_data_tuple = (peak_type, p_idx / sample_rate, audio_envelope[p_idx], reason_details)
        all_peaks_data[category]['indices'].append(p_idx)
        all_peaks_data[category]['customdata'].append(custom_data_tuple)
    return all_peaks_data

def _add_peak_traces(fig, all_peaks_data, audio_envelope, sample_rate):
    """Adds S1, S2, and Noise peak markers to the plot."""
    start_datetime = datetime.datetime.fromtimestamp(0)
    peak_hovertemplate = ("<b>Type:</b> %{customdata[0]}<br>" + "<b>Time:</b> %{customdata[1]:.2f}s<br>" +
                          "<b>Amp:</b> %{customdata[2]:.0f}<br>" + "<b>Details:</b><br>%{customdata[3]}<extra></extra>")

    if all_peaks_data['S1']['indices']:
        s1_indices, s1_customdata = np.array(all_peaks_data['S1']['indices']), np.stack(all_peaks_data['S1']['customdata'], axis=0)
        s1_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (s1_indices / sample_rate)])
        fig.add_trace(go.Scatter(x=s1_times_dt, y=audio_envelope[s1_indices], mode='markers', name='S1 Beats',
                                 marker=dict(color='#e36f6f', size=8, symbol='diamond'),
                                 customdata=s1_customdata, hovertemplate=peak_hovertemplate), secondary_y=False)
    if all_peaks_data['S2']['indices']:
        s2_indices, s2_customdata = np.array(all_peaks_data['S2']['indices']), np.stack(all_peaks_data['S2']['customdata'], axis=0)
        s2_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (s2_indices / sample_rate)])
        fig.add_trace(go.Scatter(x=s2_times_dt, y=audio_envelope[s2_indices], mode='markers', name='S2 Beats',
                                 marker=dict(color='orange', symbol='circle', size=6),
                                 customdata=s2_customdata, hovertemplate=peak_hovertemplate), secondary_y=False)
    if all_peaks_data['Noise']['indices']:
        noise_indices, noise_customdata = np.array(all_peaks_data['Noise']['indices']), np.stack(all_peaks_data['Noise']['customdata'], axis=0)
        noise_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (noise_indices / sample_rate)])
        fig.add_trace(go.Scatter(x=noise_times_dt, y=audio_envelope[noise_indices], mode='markers', name='Noise/Rejected Peaks',
                                 marker=dict(color='grey', symbol='x', size=6),
                                 customdata=noise_customdata, hovertemplate=peak_hovertemplate), secondary_y=False)

def _add_bpm_hrv_traces(fig, smoothed_bpm, analysis_data, windowed_hrv_df):
    """Adds BPM, BPM trend, and HRV traces to the plot."""
    start_datetime = datetime.datetime.fromtimestamp(0)
    if not smoothed_bpm.empty:
        fig.add_trace(go.Scatter(x=smoothed_bpm.index, y=smoothed_bpm.values, name="Average BPM",
                                 line=dict(color="#4a4a4a", width=3, dash='solid')), secondary_y=True)
    if "long_term_bpm_series" in analysis_data and not analysis_data["long_term_bpm_series"].empty:
        lt_series = analysis_data["long_term_bpm_series"]
        lt_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in lt_series.index])
        fig.add_trace(go.Scatter(x=lt_times_dt, y=lt_series.values, name="BPM Trend (Belief)",
                                 line=dict(color='orange', width=2, dash='dot'), visible='legendonly'), secondary_y=True)
    if windowed_hrv_df is not None and not windowed_hrv_df.empty:
        hrv_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in windowed_hrv_df['time']])
        fig.add_trace(go.Scatter(x=hrv_times_dt, y=windowed_hrv_df['rmssdc'], name="RMSSD",
                                 line=dict(color='cyan', width=2), visible='legendonly'), secondary_y=True)
        fig.add_trace(go.Scatter(x=hrv_times_dt, y=windowed_hrv_df['sdnn'], name="SDNN",
                                 line=dict(color='magenta', width=2), visible='legendonly'), secondary_y=True)

def _add_annotations_and_summary(fig, smoothed_bpm, hrv_summary, hrr_stats, peak_recovery_stats):
    """Adds min/max BPM annotations and the main summary box."""
    if not smoothed_bpm.empty:
        max_bpm_val, min_bpm_val = smoothed_bpm.max(), smoothed_bpm.min()
        max_bpm_time, min_bpm_time = smoothed_bpm.idxmax(), smoothed_bpm.idxmin()
        fig.add_annotation(x=max_bpm_time, y=max_bpm_val, text=f"Max: {max_bpm_val:.1f} BPM", showarrow=True, arrowhead=1, ax=20, ay=-40, font=dict(color="#e36f6f"), yref="y2")
        fig.add_annotation(x=min_bpm_time, y=min_bpm_val, text=f"Min: {min_bpm_val:.1f} BPM", showarrow=True, arrowhead=1, ax=20, ay=40, font=dict(color="#a3d194"), yref="y2")

    if hrv_summary:
        annotation_text = "<b>Analysis Summary</b><br>"
        if hrv_summary.get('avg_bpm') is not None:
            annotation_text += f"Avg/Min/Max BPM: {hrv_summary['avg_bpm']:.1f} / {hrv_summary['min_bpm']:.1f} / {hrv_summary['max_bpm']:.1f}<br>"
        if hrr_stats and hrr_stats.get('hrr_value_bpm') is not None:
            annotation_text += f"<b>1-Min HRR: {hrr_stats['hrr_value_bpm']:.1f} BPM Drop</b><br>"
        if peak_recovery_stats and peak_recovery_stats.get('slope_bpm_per_sec') is not None:
            annotation_text += f"<b>Peak Recovery Rate: {peak_recovery_stats['slope_bpm_per_sec']:.2f} BPM/sec</b><br>"
        if hrv_summary.get('avg_rmssdc') is not None:
            annotation_text += f"Avg. Corrected RMSSD: {hrv_summary['avg_rmssdc']:.2f}<br>"
        if hrv_summary.get('avg_sdnn') is not None:
            annotation_text += f"Avg. Windowed SDNN: {hrv_summary['avg_sdnn']:.2f} ms"
        fig.add_annotation(text=annotation_text, align='left', showarrow=False, xref='paper', yref='paper',
                           x=0.02, y=0.98, bordercolor='black', borderwidth=1, bgcolor='rgba(255, 253, 231, 0.4)')

def _add_slope_traces(fig, major_inclines, major_declines, peak_recovery_stats, peak_exertion_stats):
    """Adds traces for major exertion and recovery periods."""
    if major_inclines:
        for i, incline in enumerate(major_inclines):
            c_data = [incline['duration_sec'], incline['bpm_increase'], incline['slope_bpm_per_sec']]
            fig.add_trace(go.Scatter(
                x=[incline['start_time'], incline['end_time']], y=[incline['start_bpm'], incline['end_bpm']],
                mode='lines', line=dict(color="purple", width=4, dash="dash"), name='Exertion', legendgroup='Exertion',
                showlegend=(i == 0), visible='legendonly', yaxis='y2',
                hovertemplate="<b>Exertion Period</b><br>Duration: %{customdata[0]:.1f}s<br>BPM Increase: %{customdata[1]:.1f}<br>Slope: %{customdata[2]:.2f} BPM/sec<extra></extra>",
                customdata=np.array([c_data, c_data])))

    if major_declines:
        for i, decline in enumerate(major_declines):
            c_data = [decline['duration_sec'], decline['bpm_decrease'], decline['slope_bpm_per_sec']]
            fig.add_trace(go.Scatter(
                x=[decline['start_time'], decline['end_time']], y=[decline['start_bpm'], decline['end_bpm']],
                mode='lines', line=dict(color="#2ca02c", width=4, dash="dash"), name='Recovery', legendgroup='Recovery',
                showlegend=(i == 0), visible='legendonly', yaxis='y2',
                hovertemplate="<b>Recovery Period</b><br>Duration: %{customdata[0]:.1f}s<br>BPM Decrease: %{customdata[1]:.1f}<br>Slope: %{customdata[2]:.2f} BPM/sec<extra></extra>",
                customdata=np.array([c_data, c_data])))

    if peak_recovery_stats:
        stats = peak_recovery_stats
        fig.add_trace(go.Scatter(
            x=[stats['start_time'], stats['end_time']], y=[stats['start_bpm'], stats['end_bpm']],
            mode='lines', line=dict(color="#ff69b4", width=5, dash="solid"), name='Peak Recovery Slope', legendgroup='Steepest Slopes',
            visible='legendonly', yaxis='y2',
            hovertemplate="<b>Peak Recovery Slope</b><br>Slope: %{customdata[0]:.2f} BPM/sec<br>Duration: %{customdata[1]:.1f}s<extra></extra>",
            customdata=np.array([[stats['slope_bpm_per_sec'], stats['duration_sec']]]*2)))

    if peak_exertion_stats:
        stats = peak_exertion_stats
        fig.add_trace(go.Scatter(
            x=[stats['start_time'], stats['end_time']], y=[stats['start_bpm'], stats['end_bpm']],
            mode='lines', line=dict(color="#9d32a8", width=5, dash="solid"), name='Peak Exertion Slope', legendgroup='Steepest Slopes',
            visible='legendonly', yaxis='y2',
            hovertemplate="<b>Peak Exertion Slope</b><br>Slope: +%{customdata[0]:.2f} BPM/sec<br>Duration: %{customdata[1]:.1f}s<extra></extra>",
            customdata=np.array([[stats['slope_bpm_per_sec'], stats['duration_sec']]]*2)))

def plot_results(audio_envelope, peaks, all_raw_peaks, analysis_data, smoothed_bpm, bpm_times,
                 sample_rate, file_name, params, hrv_summary=None, windowed_hrv_df=None,
                 major_inclines=None, major_declines=None, hrr_stats=None, peak_recovery_stats=None,
                 peak_exertion_stats=None):
    """Generates and saves the main analysis plot by calling helper functions."""
    start_datetime = datetime.datetime.fromtimestamp(0)
    time_axis_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (np.arange(len(audio_envelope)) / sample_rate)])
    analysis_data['sample_rate'] = sample_rate

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    _add_base_traces(fig, time_axis_dt, audio_envelope, analysis_data, params)
    all_peaks_data = _categorize_peaks(all_raw_peaks, analysis_data.get('beat_debug_info', {}), audio_envelope, sample_rate)
    _add_peak_traces(fig, all_peaks_data, audio_envelope, sample_rate)
    _add_bpm_hrv_traces(fig, smoothed_bpm, analysis_data, windowed_hrv_df)
    _add_annotations_and_summary(fig, smoothed_bpm, hrv_summary, hrr_stats, peak_recovery_stats)
    _add_slope_traces(fig, major_inclines, major_declines, peak_recovery_stats, peak_exertion_stats)

    plot_title = f"Heartbeat Analysis - {os.path.basename(file_name)}"
    fig.update_layout(
        template="plotly_dark", title_text=plot_title, dragmode='pan',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(t=140, b=100),
        xaxis=dict(title_text="Time (mm:ss)", tickformat='%M:%S', hoverformat='%M:%S'),
        hovermode='x unified'
    )
    robust_upper_limit = np.quantile(audio_envelope, 0.95)
    amplitude_scale = params.get("plot_amplitude_scale_factor", 60.0)
    fig.update_yaxes(title_text="Signal Amplitude", secondary_y=False, range=[0, robust_upper_limit * amplitude_scale])
    fig.update_yaxes(title_text="BPM / HRV (ms)", secondary_y=True, range=[50, 200])

    output_html_path = f"{os.path.splitext(file_name)[0]}_bpm_plot.html"
    plot_config = {'scrollZoom': True, 'toImageButtonOptions': {'filename': plot_title, 'format': 'png', 'scale': 2}}
    fig.write_html(output_html_path, config=plot_config)
    logging.info(f"Interactive plot saved to {output_html_path}")


# --- Summary Report Helper Functions ---
def _write_summary_header(f, file_name):
    f.write(f"# Analysis Report for: {os.path.basename(file_name)}\n")
    f.write(f"*Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

def _write_overall_summary(f, hrv_summary, hrr_stats):
    f.write("## Overall Summary\n\n| Metric | Value |\n|:---|:---|\n")
    if hrv_summary:
        if hrv_summary.get('avg_bpm') is not None:
            f.write(f"| **Average BPM** | {hrv_summary['avg_bpm']:.1f} BPM |\n")
            f.write(f"| **BPM Range** | {hrv_summary['min_bpm']:.1f} to {hrv_summary['max_bpm']:.1f} BPM |\n")
        if hrv_summary.get('avg_rmssdc') is not None:
            f.write(f"| **Avg. Corrected RMSSD** | {hrv_summary['avg_rmssdc']:.2f} |\n")
        if hrv_summary.get('avg_sdnn') is not None:
            f.write(f"| **Avg. Windowed SDNN** | {hrv_summary['avg_sdnn']:.2f} ms |\n")
    if hrr_stats and hrr_stats.get('hrr_value_bpm') is not None:
        f.write(f"| **1-Minute HRR** | {hrr_stats['hrr_value_bpm']:.1f} BPM Drop |\n")
    f.write("\n")

def _write_steepest_slopes(f, peak_exertion_stats, peak_recovery_stats):
    f.write("## Steepest Slopes Analysis\n\n### Peak Exertion (Fastest HR Increase)\n\n")
    if peak_exertion_stats:
        pes = peak_exertion_stats
        f.write("| Attribute | Value |\n|:---|:---|\n")
        f.write(f"| **Rate** | `+{pes['slope_bpm_per_sec']:.2f}` BPM/second |\n")
        f.write(f"| **Period** | {pes['start_time'].strftime('%M:%S')} to {pes['end_time'].strftime('%M:%S')} |\n")
        f.write(f"| **Duration** | {pes['duration_sec']:.1f} seconds |\n")
        f.write(f"| **BPM Change** | {pes['start_bpm']:.1f} to {pes['end_bpm']:.1f} BPM |\n\n")
    else:
        f.write("*No significant peak exertion period found.*\n\n")

    f.write("### Peak Recovery (Fastest HR Decrease)\n\n")
    if peak_recovery_stats:
        prs = peak_recovery_stats
        f.write("| Attribute | Value |\n|:---|:---|\n")
        f.write(f"| **Rate** | `{prs['slope_bpm_per_sec']:.2f}` BPM/second |\n")
        f.write(f"| **Period** | {prs['start_time'].strftime('%M:%S')} to {prs['end_time'].strftime('%M:%S')} |\n")
        f.write(f"| **Duration** | {prs['duration_sec']:.1f} seconds |\n")
        f.write(f"| **BPM Change** | {prs['start_bpm']:.1f} to {prs['end_bpm']:.1f} BPM |\n\n")
    else:
        f.write("*No significant peak recovery period found post-peak.*\n\n")

def _write_significant_changes(f, major_inclines, major_declines):
    f.write("## All Significant HR Changes\n\n### Exertion Periods (Sustained HR Increase)\n\n")
    if major_inclines:
        epoch = datetime.datetime.fromtimestamp(0)
        for incline in major_inclines:
            start_sec = (incline['start_time'] - epoch).total_seconds()
            end_sec = (incline['end_time'] - epoch).total_seconds()
            f.write(f"- **From {start_sec:.1f}s to {end_sec:.1f}s:** Duration={incline['duration_sec']:.1f}s, Change=`+{incline['bpm_increase']:.1f}` BPM\n")
    else:
        f.write("*None found.*\n")
    f.write("\n### Recovery Periods (Sustained HR Decrease)\n\n")
    if major_declines:
        epoch = datetime.datetime.fromtimestamp(0)
        for decline in major_declines:
            start_sec = (decline['start_time'] - epoch).total_seconds()
            end_sec = (decline['end_time'] - epoch).total_seconds()
            f.write(f"- **From {start_sec:.1f}s to {end_sec:.1f}s:** Duration={decline['duration_sec']:.1f}s, Change=`-{decline['bpm_decrease']:.1f}` BPM\n")
    else:
        f.write("*None found.*\n")
    f.write("\n")

def _write_heartbeat_data_table(f, smoothed_bpm, bpm_times):
    f.write("## Heartbeat Data (BPM over Time)\n\n| Time (s) | Average BPM |\n|:---:|:---:|\n")
    if not smoothed_bpm.empty:
        for t, bpm in zip(bpm_times, smoothed_bpm.values):
            f.write(f"| {t:.2f} | {bpm:.1f} |\n")
    else:
        f.write("| *No data* | *No data* |\n")

def save_analysis_summary(output_path, file_name, hrv_summary, hrr_stats, peak_exertion_stats,
                          peak_recovery_stats, major_inclines, major_declines,
                          smoothed_bpm, bpm_times):
    """Saves a comprehensive Markdown summary of the analysis results."""
    with open(output_path, "w", encoding="utf-8") as f:
        _write_summary_header(f, file_name)
        _write_overall_summary(f, hrv_summary, hrr_stats)
        _write_steepest_slopes(f, peak_exertion_stats, peak_recovery_stats)
        _write_significant_changes(f, major_inclines, major_declines)
        _write_heartbeat_data_table(f, smoothed_bpm, bpm_times)
    logging.info(f"Markdown analysis summary saved to {output_path}")

def _prepare_log_data(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm, bpm_times):
    """Prepares and merges all data sources into a single DataFrame for logging."""
    events = []
    debug_info = analysis_data.get('beat_debug_info', {})
    for p in all_raw_peaks:
        reason = debug_info.get(p, 'Unknown')
        if reason != 'Unknown':
            events.append({'time': p / sample_rate, 'type': 'Peak', 'amp': audio_envelope[p], 'reason': reason})
    if 'trough_indices' in analysis_data:
        for p in analysis_data['trough_indices']:
            events.append({'time': p / sample_rate, 'type': 'Trough', 'amp': audio_envelope[p], 'reason': ''})

    if not events:
        return None

    events_df = pd.DataFrame(events).sort_values(by='time').set_index('time')
    master_df = pd.DataFrame(index=np.arange(len(audio_envelope)) / sample_rate)
    master_df['envelope'] = audio_envelope
    if 'dynamic_noise_floor_series' in analysis_data:
        master_df['noise_floor'] = analysis_data['dynamic_noise_floor_series'].values

    if not smoothed_bpm.empty:
        smoothed_bpm_sec_index = pd.Series(data=smoothed_bpm.values, index=bpm_times)
        if not smoothed_bpm_sec_index.index.is_unique:
            smoothed_bpm_sec_index = smoothed_bpm_sec_index.groupby(level=0).mean()
        master_df['smoothed_bpm'] = smoothed_bpm_sec_index

    # Handle long_term_bpm_series
    if 'long_term_bpm_series' in analysis_data and not analysis_data['long_term_bpm_series'].empty:
        lt_bpm_series = analysis_data['long_term_bpm_series']
        if not lt_bpm_series.index.is_unique:
            lt_bpm_series = lt_bpm_series.groupby(level=0).mean()
        master_df['lt_bpm'] = lt_bpm_series

    # Handle deviation_series
    if 'deviation_series' in analysis_data and not analysis_data['deviation_series'].empty:
        dev_series = analysis_data['deviation_series']
        if not dev_series.index.is_unique:
            dev_series = dev_series.groupby(level=0).mean()
        master_df['deviation'] = dev_series

    master_df.sort_index(inplace=True)
    return pd.merge_asof(left=events_df, right=master_df.ffill(), left_index=True,
                         right_index=True, direction='nearest', tolerance=pd.Timedelta(seconds=0.5).total_seconds())

def _write_log_events(log_file, merged_df, file_name):
    """Writes the formatted log events to the file using itertuples for efficiency."""
    log_file.write(f"# Chronological Debug Log for {os.path.basename(file_name)}\n")
    log_file.write(f"Analysis performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    for row in merged_df.itertuples(name="LogEvent"):
        log_file.write(f"## Time: `{row.Index:.4f}s`\n")

        # --- Part 1: Format the main event line (Peak or Trough) ---
        peak_type, details = _parse_reason_string(getattr(row, 'reason', ''))
        if row.type == 'Peak':
            log_file.write(f"**{peak_type}**\n")
            if details:
                formatted_details = details.replace(' | ', '\n- ').replace('\n', '\n- ')
                log_file.write(f"- {formatted_details}\n")
        else: # Trough
            log_file.write(f"**Trough Detected**\n")

        # --- Part 2: Create a dictionary of available signal metrics ---
        metrics = {
            "Raw Amp": getattr(row, 'amp', None),
            "Audio Envelope": getattr(row, 'envelope', None),
            "Noise Floor": getattr(row, 'noise_floor', None),
            "Average BPM (Smoothed)": getattr(row, 'smoothed_bpm', None),
            "Long-Term BPM (Belief)": getattr(row, 'lt_bpm', None),
            "Norm. Deviation": getattr(row, 'deviation', None)
        }

        # --- Part 3: Write all available metrics in a consistent format ---
        for name, value in metrics.items():
            if pd.notna(value):
                if name == "Norm. Deviation":
                    log_file.write(f"**{name}**: {value * 100:.1f}%\n")
                else:
                    log_file.write(f"**{name}**: `{value:.2f}`\n")

        log_file.write("\n")

def _parse_reason_string(reason):
    """A helper function to decouple reason string parsing from the main logging logic."""
    if not reason:
        return "Unknown Peak", ""

    separators = ['. Justification: ', '. ', '(']
    for sep in separators:
        if sep in reason:
            parts = reason.split(sep, 1)
            peak_type = parts[0].strip()
            details = parts[1].rsplit(')', 1)[0].strip() if sep == '(' else parts[1].strip()
            return peak_type, details

    return reason.strip(), ""

def create_chronological_log_file(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm, bpm_times, output_log_path, file_name):
    """Creates a chronological debug log using efficient, vectorized pandas operations."""
    logging.info(f"Generating readable debug log at '{output_log_path}'...")
    merged_df = _prepare_log_data(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm, bpm_times)

    with open(output_log_path, "w", encoding="utf-8") as log_file:
        if merged_df is None or merged_df.empty:
            log_file.write("# No significant events (peaks or troughs) were detected to log.\n")
        else:
            _write_log_events(log_file, merged_df, file_name)
    logging.info("Debug log generation complete.")

def find_major_hr_inclines(smoothed_bpm_series, min_duration_sec=10, min_bpm_increase=15):
    """Identifies significant, sustained periods of heart rate increase."""
    if smoothed_bpm_series.empty or len( smoothed_bpm_series) < 2:
        return []

    logging.info(f"Searching for major HR inclines (min_duration={min_duration_sec}s, min_increase={min_bpm_increase} BPM)...")
    time_diffs_sec = smoothed_bpm_series.index.to_series().diff().dt.total_seconds()
    mean_time_diff = np.nanmean(time_diffs_sec)
    distance_samples = 5 if np.isnan(mean_time_diff) or mean_time_diff == 0 else int((min_duration_sec / 2) / mean_time_diff)

    peaks, _ = find_peaks(smoothed_bpm_series.values, prominence=5, distance=distance_samples)
    troughs, _ = find_peaks(-smoothed_bpm_series.values, prominence=5, distance=distance_samples)
    logging.info(f"Found {len(troughs)} potential start points (troughs) and {len(peaks)} potential end points (peaks) for inclines.")
    if len(troughs) == 0 or len(peaks) == 0:
        return []

    major_inclines = []
    for trough_idx in troughs:
        following_peaks_indices = peaks[peaks > trough_idx]
        if len(following_peaks_indices) > 0:
            peak_idx = following_peaks_indices[0]
            start_time, end_time = smoothed_bpm_series.index[trough_idx], smoothed_bpm_series.index[peak_idx]
            start_bpm, end_bpm = smoothed_bpm_series.values[trough_idx], smoothed_bpm_series.values[peak_idx]
            duration, bpm_increase = (end_time - start_time).total_seconds(), end_bpm - start_bpm

            if duration >= min_duration_sec and bpm_increase >= min_bpm_increase:
                major_inclines.append({
                    'start_time': start_time, 'end_time': end_time, 'start_bpm': start_bpm, 'end_bpm': end_bpm,
                    'duration_sec': duration, 'bpm_increase': bpm_increase, 'slope_bpm_per_sec': bpm_increase / duration
                })
    major_inclines.sort(key=lambda x: x['slope_bpm_per_sec'], reverse=True)
    return major_inclines

def find_major_hr_declines(smoothed_bpm_series, min_duration_sec=10, min_bpm_decrease=15):
    """Identifies significant, sustained periods of heart rate decrease (recovery)."""
    if smoothed_bpm_series.empty or len(smoothed_bpm_series) < 2:
        return []

    logging.info(f"Searching for major HR declines (min_duration={min_duration_sec}s, min_decrease={min_bpm_decrease} BPM)...")
    time_diffs_sec = smoothed_bpm_series.index.to_series().diff().dt.total_seconds()
    mean_time_diff = np.nanmean(time_diffs_sec)
    distance_samples = 5 if np.isnan(mean_time_diff) or mean_time_diff == 0 else int((min_duration_sec / 2) / mean_time_diff)

    peaks, _ = find_peaks(smoothed_bpm_series.values, prominence=5, distance=distance_samples)
    troughs, _ = find_peaks(-smoothed_bpm_series.values, prominence=5, distance=distance_samples)
    logging.info(f"Found {len(peaks)} potential start points (peaks) and {len(troughs)} potential end points (troughs) for declines.")
    if len(troughs) == 0 or len(peaks) == 0:
        return []

    major_declines = []
    for peak_idx in peaks:
        following_troughs_indices = troughs[troughs > peak_idx]
        if len(following_troughs_indices) > 0:
            trough_idx = following_troughs_indices[0]
            start_time, end_time = smoothed_bpm_series.index[peak_idx], smoothed_bpm_series.index[trough_idx]
            start_bpm, end_bpm = smoothed_bpm_series.values[peak_idx], smoothed_bpm_series.values[trough_idx]
            duration, bpm_decrease = (end_time - start_time).total_seconds(), start_bpm - end_bpm

            if duration >= min_duration_sec and bpm_decrease >= min_bpm_decrease:
                major_declines.append({
                    'start_time': start_time, 'end_time': end_time, 'start_bpm': start_bpm, 'end_bpm': end_bpm,
                    'duration_sec': duration, 'bpm_decrease': bpm_decrease, 'slope_bpm_per_sec': (end_bpm - start_bpm) / duration
                })
    major_declines.sort(key=lambda x: x['slope_bpm_per_sec'])
    return major_declines

def find_peak_recovery_rate(smoothed_bpm_series, window_sec=20):
    """Finds the steepest slope of heart rate decline after the peak BPM."""
    if smoothed_bpm_series.empty or len(smoothed_bpm_series) < 2: return None
    recovery_series = smoothed_bpm_series[smoothed_bpm_series.idxmax():]
    if recovery_series.empty: return None

    times_sec = (recovery_series.index - recovery_series.index[0]).total_seconds()
    if times_sec[-1] < window_sec: return None

    bpm_values, steepest_slope, best_period = recovery_series.values, 0, None
    for i in range(len(times_sec) - 1):
        end_idx_candidates = np.where(times_sec >= times_sec[i] + window_sec)[0]
        if len(end_idx_candidates) == 0: break
        end_idx = end_idx_candidates[0]
        duration = times_sec[end_idx] - times_sec[i]
        if duration > 0:
            slope = (bpm_values[end_idx] - bpm_values[i]) / duration
            if slope < steepest_slope:
                steepest_slope = slope
                best_period = {'start_time': recovery_series.index[i], 'end_time': recovery_series.index[end_idx],
                               'start_bpm': bpm_values[i], 'end_bpm': bpm_values[end_idx],
                               'slope_bpm_per_sec': slope, 'duration_sec': duration}
    return best_period

def find_peak_exertion_rate(smoothed_bpm_series, window_sec=20):
    """Finds the steepest slope of heart rate increase across the entire recording."""
    if smoothed_bpm_series.empty or len(smoothed_bpm_series) < 2: return None
    times_sec = (smoothed_bpm_series.index - smoothed_bpm_series.index[0]).total_seconds()
    if times_sec[-1] < window_sec: return None

    bpm_values, steepest_slope, best_period = smoothed_bpm_series.values, 0, None
    for i in range(len(times_sec) - 1):
        end_idx_candidates = np.where(times_sec >= times_sec[i] + window_sec)[0]
        if len(end_idx_candidates) == 0: break
        end_idx = end_idx_candidates[0]
        duration = times_sec[end_idx] - times_sec[i]
        if duration > 0:
            slope = (bpm_values[end_idx] - bpm_values[i]) / duration
            if slope > steepest_slope:
                steepest_slope = slope
                best_period = {'start_time': smoothed_bpm_series.index[i], 'end_time': smoothed_bpm_series.index[end_idx],
                               'start_bpm': bpm_values[i], 'end_bpm': bpm_values[end_idx],
                               'slope_bpm_per_sec': slope, 'duration_sec': duration}
    return best_period

def calculate_hrr(smoothed_bpm_series, interval_sec=60):
    """Calculates the standard Heart Rate Recovery (HRR) over a fixed interval."""
    if smoothed_bpm_series.empty or len(smoothed_bpm_series) < 2: return None
    peak_bpm, peak_time = smoothed_bpm_series.max(), smoothed_bpm_series.idxmax()
    recovery_check_time = peak_time + pd.Timedelta(seconds=interval_sec)
    if recovery_check_time > smoothed_bpm_series.index.max(): return None

    recovery_bpm = np.interp(
        recovery_check_time.timestamp(),
        smoothed_bpm_series.index.astype(np.int64) // 10**9,
        smoothed_bpm_series.values)
    return {'peak_bpm': peak_bpm, 'peak_time': peak_time, 'recovery_bpm': recovery_bpm,
            'recovery_check_time': recovery_check_time, 'hrr_value_bpm': peak_bpm - recovery_bpm,
            'interval_sec': interval_sec}

def find_recovery_phase(bpm_series, bpm_times_sec, params):
    """Analyzes a preliminary BPM series to find the peak heart rate and define the subsequent recovery phase window."""
    if bpm_times_sec is None or len(bpm_times_sec) < 2:
        logging.warning("Not enough preliminary beats to determine a recovery phase.")
        return None, None
    peak_time_sec = bpm_times_sec[np.argmax(bpm_series.values)]
    recovery_end_time_sec = peak_time_sec + params.get("recovery_phase_duration_sec", 120.0)
    logging.info(f"Peak BPM detected in preliminary pass at {peak_time_sec:.2f}s. High-contractility state defined until {recovery_end_time_sec:.2f}s.")
    return peak_time_sec, recovery_end_time_sec

# --- Analysis Pipeline Helpers ---
def _run_stage1_anchor_beat_pass(audio_envelope, sample_rate, params, precomputed_noise_floor, precomputed_troughs):
    """Runs a high-confidence first pass to find anchor beats and estimate global BPM."""
    logging.info("--- STAGE 2: Running High-Confidence pass to find anchor beats ---")
    params_pass_1 = params.copy()
    params_pass_1["pairing_confidence_threshold"] = 0.75
    params_pass_1["enable_bpm_boost"] = True

    anchor_beats, _, _ = find_heartbeat_peaks(
        audio_envelope, sample_rate, params_pass_1,
        precomputed_noise_floor=precomputed_noise_floor,
        precomputed_troughs=precomputed_troughs
    )

    global_bpm_estimate = None
    if len(anchor_beats) >= 10:
        rr_intervals_sec = np.diff(anchor_beats) / sample_rate
        median_rr_sec = np.median(rr_intervals_sec)
        if median_rr_sec > 0:
            global_bpm_estimate = 60.0 / median_rr_sec
            logging.info(f"Automatically determined Global BPM Estimate: {global_bpm_estimate:.1f} BPM")
    else:
        logging.warning(f"Found only {len(anchor_beats)} anchor beats. Cannot reliably estimate global BPM.")

    prelim_bpm_series, prelim_bpm_times = calculate_bpm_series(anchor_beats, sample_rate, params)
    peak_bpm_time_sec, recovery_end_time_sec = find_recovery_phase(prelim_bpm_series, prelim_bpm_times, params)

    return global_bpm_estimate, peak_bpm_time_sec, recovery_end_time_sec

def _determine_start_bpm(start_bpm_hint, global_bpm_estimate):
    """Determines the starting BPM for the main analysis based on hints or estimates."""
    if start_bpm_hint:
        logging.info(f"Using user-provided starting BPM of {start_bpm_hint:.1f} BPM for main analysis.")
        return start_bpm_hint
    if global_bpm_estimate:
        logging.info(f"Using automatically determined BPM of {global_bpm_estimate:.1f} BPM for main analysis.")
        return global_bpm_estimate
    logging.warning("Could not determine starting BPM. Using fallback default of 80.0 BPM.")
    return 80.0

def _run_iterative_correction_pass(s1_peaks, all_raw_peaks, analysis_data, params, sample_rate):
    """
    Runs the contextual correction pass iteratively until it stabilizes.
    """
    if not params.get("enable_correction_pass", False):
        logging.info("Correction pass skipped (disabled by parameter).")
        return s1_peaks, analysis_data["beat_debug_info"]

    logging.info("--- STAGE 5: Running Iterative Correction Pass ---")

    final_peaks = s1_peaks
    corrected_debug_info = analysis_data["beat_debug_info"].copy()
    max_iterations = 5  # Safeguard against infinite loops

    for i in range(max_iterations):
        new_peaks, new_debug_info, corrections_made = _fix_rhythmic_discontinuities(
            s1_peaks=final_peaks,
            all_raw_peaks=all_raw_peaks,
            debug_info=corrected_debug_info,
            audio_envelope=analysis_data['audio_envelope'],
            dynamic_noise_floor=analysis_data['dynamic_noise_floor_series'],
            params=params,
            sample_rate=sample_rate
        )

        final_peaks = new_peaks
        corrected_debug_info = new_debug_info

        logging.info(f"Correction Pass Iteration {i + 1} made {corrections_made} changes.")
        if corrections_made == 0:
            logging.info("Correction process stabilized. Exiting loop.")
            break
    else:
        logging.warning("Correction process reached max iterations without stabilizing.")

    return final_peaks, corrected_debug_info

def _calculate_final_metrics(final_peaks, sample_rate, params):
    """Calculates all final BPM, HRV, and slope metrics for reporting."""
    metrics = {}
    metrics['smoothed_bpm'], metrics['bpm_times'] = calculate_bpm_series(final_peaks, sample_rate, params)
    metrics['major_inclines'] = find_major_hr_inclines(metrics['smoothed_bpm'])
    metrics['major_declines'] = find_major_hr_declines(metrics['smoothed_bpm'])
    metrics['hrr_stats'] = calculate_hrr(metrics['smoothed_bpm'])
    metrics['peak_recovery_stats'] = find_peak_recovery_rate(metrics['smoothed_bpm'])
    metrics['peak_exertion_stats'] = find_peak_exertion_rate(metrics['smoothed_bpm'])
    metrics['windowed_hrv_df'] = calculate_windowed_hrv(final_peaks, sample_rate, params)

    hrv_summary_stats = {}
    if not metrics['smoothed_bpm'].empty:
        hrv_summary_stats['avg_bpm'] = metrics['smoothed_bpm'].mean()
        hrv_summary_stats['min_bpm'] = metrics['smoothed_bpm'].min()
        hrv_summary_stats['max_bpm'] = metrics['smoothed_bpm'].max()
    if not metrics['windowed_hrv_df'].empty:
        hrv_summary_stats['avg_rmssdc'] = metrics['windowed_hrv_df']['rmssdc'].mean()
        hrv_summary_stats['avg_sdnn'] = metrics['windowed_hrv_df']['sdnn'].mean()
    metrics['hrv_summary'] = hrv_summary_stats

    return metrics

def analyze_wav_file(wav_file_path, params, start_bpm_hint):
    """Main analysis pipeline that orchestrates multiple analysis passes."""
    start_time = time.time()
    file_name_no_ext = os.path.splitext(wav_file_path)[0]
    logging.info(f"--- Processing file: {os.path.basename(wav_file_path)} ---")
    audio_envelope, sample_rate = preprocess_audio(wav_file_path, params)

    # STAGE 1 - Calculate Noise Floor
    logging.info("--- STAGE 1: Calculating refined noise floor ---")
    sanitized_noise_floor, sanitized_troughs = _calculate_dynamic_noise_floor(audio_envelope, sample_rate, params)

    # STAGE 2 - Estimate global BPM
    global_bpm_estimate, peak_bpm_time_sec, recovery_end_time_sec = _run_stage1_anchor_beat_pass(
        audio_envelope, sample_rate, params,
        precomputed_noise_floor=sanitized_noise_floor,
        precomputed_troughs=sanitized_troughs
    )
    final_start_bpm = _determine_start_bpm(start_bpm_hint, global_bpm_estimate)

    # STAGE 3: Primary analysis pass reuses the same floor
    logging.info("--- STAGE 3: Running Main Analysis Pass with refined inputs ---")
    s1_peaks_pass1, all_raw_peaks, analysis_data = find_heartbeat_peaks(
        audio_envelope, sample_rate, params,
        start_bpm_hint=final_start_bpm,
        precomputed_noise_floor=sanitized_noise_floor,
        precomputed_troughs=sanitized_troughs,
        peak_bpm_time_sec=peak_bpm_time_sec,
        recovery_end_time_sec=recovery_end_time_sec
    )

    # STAGE 4: Rhythm-based correction pass
    s1_peaks_pass2 = correct_peaks_by_rhythm(s1_peaks_pass1, audio_envelope, sample_rate, params)
    analysis_data['audio_envelope'] = audio_envelope

    # STAGE 5: Iterative contextual correction pass
    final_peaks, final_debug_info = _run_iterative_correction_pass(
        s1_peaks_pass2, all_raw_peaks, analysis_data, params, sample_rate)
    analysis_data["beat_debug_info"] = final_debug_info

    # --- FINAL CALCULATIONS AND OUTPUT ---
    if len(final_peaks) < 2:
        logging.warning("Not enough S1 peaks detected after correction to calculate BPM.")
        plot_results(audio_envelope, final_peaks, all_raw_peaks, analysis_data, pd.Series(dtype=np.float64), np.array([]), sample_rate, wav_file_path, params)
        return

    metrics = _calculate_final_metrics(final_peaks, sample_rate, params)

    # --- Save Reports and Plots ---
    output_summary_path = f"{file_name_no_ext}_Analysis_Summary.md"
    save_analysis_summary(
        output_path=output_summary_path,
        file_name=wav_file_path,
        hrv_summary=metrics['hrv_summary'],
        hrr_stats=metrics['hrr_stats'],
        peak_exertion_stats=metrics['peak_exertion_stats'],
        peak_recovery_stats=metrics['peak_recovery_stats'],
        major_inclines=metrics['major_inclines'],
        major_declines=metrics['major_declines'],
        smoothed_bpm=metrics['smoothed_bpm'],
        bpm_times=metrics['bpm_times']
    )

    plot_results(
        audio_envelope=audio_envelope,
        peaks=final_peaks,
        all_raw_peaks=all_raw_peaks,
        analysis_data=analysis_data,
        smoothed_bpm=metrics['smoothed_bpm'],
        bpm_times=metrics['bpm_times'],
        sample_rate=sample_rate,
        file_name=wav_file_path,
        params=params,
        hrv_summary=metrics['hrv_summary'],
        windowed_hrv_df=metrics['windowed_hrv_df'],
        major_inclines=metrics['major_inclines'],
        major_declines=metrics['major_declines'],
        hrr_stats=metrics['hrr_stats'],
        peak_recovery_stats=metrics['peak_recovery_stats'],
        peak_exertion_stats=metrics['peak_exertion_stats']
    )

    output_log_path = f"{file_name_no_ext}_Debug_Log.md"
    create_chronological_log_file(audio_envelope, sample_rate, all_raw_peaks, analysis_data, metrics['smoothed_bpm'], metrics['bpm_times'], output_log_path, wav_file_path)
    # --- Calculate and log total execution time ---
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"--- Analysis finished in {duration:.2f} seconds. ---")

# --- GUI Class ---
class BPMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heartbeat BPM Analyzer")
        self.root.geometry("550x350")
        self.style = ttkb.Style(theme='minty')
        self.current_file = None
        self.params = DEFAULT_PARAMS.copy()
        self.log_queue = queue.Queue()
        self.create_widgets()
        self.root.after(100, self.process_log_queue)
        self._find_initial_audio_file()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # File selection
        file_frame = ttk.LabelFrame(main_frame, text="Audio File", padding=10)
        file_frame.pack(fill=tk.X, pady=5)
        self.file_label = ttk.Label(file_frame, text="No file selected", wraplength=450)
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.select_file, bootstyle=INFO)
        browse_btn.pack(side=tk.RIGHT, padx=5)

        # Parameters
        param_frame = ttk.LabelFrame(main_frame, text="Analysis Parameters", padding=10)
        param_frame.pack(fill=tk.X, pady=5)
        ttk.Label(param_frame, text="Starting BPM (optional):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.bpm_entry = ttk.Entry(param_frame)
        self.bpm_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)

        # Action Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)
        self.analyze_btn = ttk.Button(btn_frame, text="Analyze", command=self.start_analysis_thread, bootstyle=SUCCESS, state=tk.DISABLED)
        self.analyze_btn.pack(side=tk.RIGHT, padx=5)

        # Status Bar
        self.status_var = tk.StringVar(value="Select an audio file to begin.")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding=5)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

        param_frame.columnconfigure(1, weight=1)

    def process_log_queue(self):
        try:
            while not self.log_queue.empty():
                message_type, data = self.log_queue.get(0)

                if message_type == "status":
                    self.status_var.set(data)
                elif message_type == "analysis_complete":
                    self.status_var.set("Analysis complete!")
                    self.analyze_btn.config(state=tk.NORMAL)
                elif message_type == "error":
                     self.status_var.set("An error occurred. Check logs.")
                     self.analyze_btn.config(state=tk.NORMAL)
                     messagebox.showerror("Analysis Error", data)

        finally:
            self.root.after(100, self.process_log_queue)

    def select_file(self):
        filetypes = [('Audio files', '*.wav *.mp3 *.m4a *.flac *.ogg *.mp4 *.mkv *.mov'), ('All files', '*.*')]
        filename = filedialog.askopenfilename(title="Select audio file", filetypes=filetypes)
        if filename:
            self.current_file = filename
            self.file_label.config(text=os.path.basename(filename))
            self.analyze_btn.config(state=tk.NORMAL)
            self._update_status(f"Ready to analyze: {os.path.basename(filename)}")

    def _find_initial_audio_file(self):
        supported = ('.wav', '.mp3', '.m4a', '.flac', '.ogg', '.mp4', '.mkv', '.mov')
        try:
            for filename in os.listdir(os.getcwd()):
                if filename.lower().endswith(supported):
                    self.current_file = os.path.join(os.getcwd(), filename)
                    self.file_label.config(text=os.path.basename(self.current_file))
                    self.analyze_btn.config(state=tk.NORMAL)
                    self._update_status(f"Auto-loaded: {os.path.basename(self.current_file)}")
                    return
        except Exception as e:
            logging.error(f"Could not auto-find file: {e}")

    def _update_status(self, message):
        """Safely update the status bar from any thread."""
        self.root.after(0, lambda: self.status_var.set(message))

    def start_analysis_thread(self):
        """Starts the analysis in a new thread."""
        if not self.current_file:
            messagebox.showerror("Error", "No file selected")
            return

        self.analyze_btn.config(state=tk.DISABLED)
        self._update_status("Starting analysis...")

        analysis_thread = threading.Thread(target=self._run_analysis_in_background)
        analysis_thread.daemon = True
        analysis_thread.start()

    def _run_analysis_in_background(self):
        try:
            bpm_input = self.bpm_entry.get().strip()
            start_bpm_hint = float(bpm_input) if bpm_input else None

            converted_dir = os.path.join(os.getcwd(), "converted_wavs")
            os.makedirs(converted_dir, exist_ok=True)
            base_name, ext = os.path.splitext(self.current_file)
            wav_path = os.path.join(converted_dir, f"{os.path.basename(base_name)}.wav")

            if ext.lower() != '.wav':
                self.log_queue.put(("status", "Converting file to WAV..."))
                if not convert_to_wav(self.current_file, wav_path):
                    self.log_queue.put(("error", "File conversion failed."))
                    return
            else:
                import shutil
                shutil.copy(self.current_file, wav_path)

            self.log_queue.put(("status", "Processing and analyzing heartbeat..."))
            analyze_wav_file(wav_path, self.params, start_bpm_hint)
            self.log_queue.put(("analysis_complete", None))

        except Exception as e:
            error_info = f"An error occurred:\n{str(e)}"
            self.log_queue.put(("error", error_info))
            logging.error(f"Full analysis error: {traceback.format_exc()}")

def main():
    root = ttkb.Window(themename="minty")
    app = BPMApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()