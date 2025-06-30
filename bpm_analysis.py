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
    # 1. Preprocessing & General Settings
    # These parameters control the initial handling of the audio file.
    # =================================================================================
    "downsample_factor": 300,     # The factor by which to reduce the audio's sample rate. higher = less detail, faster processing, lower file size
    "bandpass_freqs": (20, 150),  # (low_hz, high_hz) for the bandpass filter
    "save_filtered_wav": True,    # If True, saves a debug .wav file of the filtered audio

    # =================================================================================
    # 2. Peak & Trough Detection
    # These settings govern the initial identification of peaks and troughs in the signal.
    # =================================================================================
    "min_peak_distance_sec": 0.05,
    # The minimum time allowed between any two raw peaks found in the signal.
    # Increase: Prevents a single, wide heartbeat sound from being detected as multiple peaks.
    # Decrease: Allows detection of very close peaks, useful for high BPMs, but risks detecting noise as peaks.

    "peak_prominence_quantile": 0.1,
    # The prominence required for a signal spike to be considered a 'peak' in the first pass.
    # Increase: Requires peaks to stand out more from their surroundings. Filters out minor bumps more aggressively.
    # Decrease: Allows less prominent peaks to be included in the analysis, increasing sensitivity.

    "trough_prominence_quantile": 0.1,
    # The prominence required for a dip in the signal to be considered a 'trough' for noise floor calculation.
    # Increase: Requires troughs to be much deeper to be identified. Finds fewer, more significant troughs.
    # Decrease: Allows shallower dips to be considered troughs. Finds more troughs, but can make false positives.

    # =================================================================================
    # 3. Dynamic Noise Floor
    # Controls how the algorithm determines the background noise level over time.
    # =================================================================================
    "noise_floor_quantile": 0.20,
    # The quantile used to calculate the dynamic noise floor from audio troughs. (0.2 = 20th percentile).
    # Increase: Raises the noise floor, making the algorithm less sensitive. Requires peaks to be taller to be considered.
    # Decrease: Lowers the noise floor, making the algorithm more sensitive. More likely to detect smaller peaks.

    "noise_window_sec": 10,
    # The size of the rolling window (in seconds) for calculating the dynamic noise floor.
    # Increase: The noise floor adapts more slowly to changes in background noise, resulting in a smoother, more stable floor.
    # Decrease: The noise floor adapts very quickly to local changes in noise level.

    "trough_rejection_multiplier": 4.0, # For trough sanitization, a trough N-times higher than the draft noise floor is rejected.

    # =================================================================================
    # 4. Peak Rejection & Noise Vetoing
    # Rules for identifying and discarding peaks that are likely noise.
    # =================================================================================
    "trough_veto_multiplier": 2.1,
    # Lookahead Veto Logic: If `N * (current_peak - trough) < (next_peak - trough)`, the current peak is vetoed as noise.
    # This rule helps reject a small noise peak that occurs just before a large, real peak.
    # Increase: Makes the veto harder to trigger. Fewer peaks will be vetoed.
    # Decrease: Makes the veto easier to trigger. More aggressive at rejecting small peaks that precede large ones.

    "trough_noise_multiplier": 3.0,
    # A peak is considered "noisy" if the trough preceding it has an amplitude N-times higher than the dynamic noise floor.
    # Increase: Requires the trough to be much louder to be considered noisy. Less likely to classify peaks as noise.
    # Decrease: Even a slightly elevated trough can mark an area as noisy, making noise classification more likely.

    "noise_confidence_threshold": 0.6,
    # If the calculated "noise confidence" for a peak exceeds this value, it will be classified as noise.
    # Increase: Harder to reject a peak. The algorithm needs to be more certain it's noise.
    # Decrease: Easier to reject a peak as noise, making the filter more aggressive.

    "strong_peak_override_ratio": 6.0,
    # A peak whose amplitude is N-times the noise floor will bypass the noise-rejection rules and be kept.
    # Increase: Requires a peak to be exceptionally tall to bypass noise rules.
    # Decrease: Allows moderately tall peaks to be kept even if they are in a section considered noisy.

    # =================================================================================
    # 5. S1/S2 Pairing Logic
    # These settings control how the algorithm decides if two peaks are an S1/S2 pair.
    # =================================================================================
    "pairing_confidence_threshold": 0.50,
    # The confidence score required to classify two adjacent peaks as an S1-S2 pair.
    # Increase: Requires stronger evidence for pairing. Results in fewer S1-S2 pairs and more "Lone S1" beats.
    # Decrease: Easier to form S1-S2 pairs. Risks incorrectly pairing a true S1 with a nearby noise peak.

    "s1_s2_interval_cap_sec": 0.4,
    # The absolute maximum time (in seconds) allowed between a detected S1 and a subsequent S2.
    # Increase: Allows pairing of S1-S2 events that are further apart, which may be needed for very slow heart rates.
    # Decrease: Enforces a stricter time limit for pairing, preventing a distant noise peak from being classified as an S2.

    "s1_s2_interval_rr_fraction": 0.7,
    # The S1-S2 interval cannot be longer than this fraction of the current beat-to-beat (RR) interval.
    # Increase: Allows the S1-S2 interval to be a larger portion of the cardiac cycle.
    # Decrease: Restricts the S1-S2 interval to be a smaller fraction of the cycle, useful for higher heart rates.

    "deviation_smoothing_factor": 0.05,
    # Controls the amount of smoothing applied to the peak-to-peak amplitude deviation series.
    # Increase: More smoothing. The S1/S2 pairing confidence will be based on the general trend of amplitude changes.
    # Decrease: Less smoothing. Pairing confidence will be highly influenced by the amplitude change between two adjacent peaks.

    # =================================================================================
    # 6. Dynamic Confidence Curves (Physiology Model)
    # These curves model how S1/S2 amplitude changes with heart rate.
    # =================================================================================
    "confidence_deviation_points": [0.0, 0.25, 0.40, 0.80, 1.0],
    # The 'x-axis' for the confidence curves, representing normalized amplitude deviation (0.0 to 1.0).

    "confidence_curve_low_bpm": [0.9, 0.9, 0.7, 0.1, 0.1],
    # The 'y-axis' curve for LOW heart rates. Rewards pairs with similar amplitudes.

    "confidence_curve_high_bpm": [0.1, 0.5, 0.75, 0.65, 0],
    # The 'y-axis' curve for HIGH heart rates. Rewards pairs where S1 is louder than S2.

    "contractility_bpm_low": 120.0,  # Below this BPM, expect S2 can be louder than S1.
    "contractility_bpm_high": 140.0, # Above this BPM, strongly expect S1 to be louder than S2.

    "s2_s1_ratio_low_bpm": 1.5,   # At low BPM, allows S2 to be up to 1.5x louder than S1.
    "s2_s1_ratio_high_bpm": 1.1,  # At high BPM, expects S2 to be no more than 1.1x louder than S1.

    "confidence_adjustment_low_bpm": 0.8,  # Gentle confidence reduction (20%) if ratio is exceeded at low BPM.
    "confidence_adjustment_high_bpm": 0.4, # Harsh confidence reduction (60%) if ratio is exceeded at high BPM.

    "recovery_phase_duration_sec": 120.0, # Duration (in seconds) of the high-contractility state after peak BPM is detected.

    # =================================================================================
    # 7. Confidence Boost Logic
    # Dynamically boosts pairing confidence based on recent rhythm stability.
    # =================================================================================
    "enable_bpm_boost": True,     # Master switch to enable/disable the BPM spike prevention boost.
    "s1_s2_boost_ratio": 1.2,     # Apply boost if the S1 amplitude is more than 1.2 times the S2 amplitude.
    "boost_history_window": 20,   # The number of recent beats to look at to determine rhythm stability.
    "boost_amount_min": 0.10,     # The minimum confidence boost to apply (when pairing success is 0%).
    "boost_amount_max": 0.35,     # The maximum confidence boost to apply (when pairing success is 100%).

    # =================================================================================
    # 8. Long-Term BPM Belief
    # Controls the "memory" or "belief" state of the algorithm's BPM calculation.
    # =================================================================================
    "min_bpm": 40,   # The absolute minimum BPM the algorithm will consider valid for the long-term belief.
    "max_bpm": 240,  # The absolute maximum BPM the algorithm will consider valid for the long-term belief.

    "long_term_bpm_learning_rate": 0.05,
    # Controls how much a new beat influences the algorithm's long-term BPM belief (like an exponential moving average).
    # Increase: The BPM belief adapts very quickly to changes.
    # Decrease: The BPM belief is more stable and changes slowly.

    "max_bpm_change_per_beat": 3.0,
    # A "speed limit" on how much the long-term BPM belief can change from one beat to the next.
    # Increase: Allows the BPM belief to make larger jumps.
    # Decrease: Forces the BPM belief to be smoother.

    # =================================================================================
    # 9. Rhythm Plausibility & Lone S1 Validation
    # Rules for checking if beat-to-beat timing and lone S1 candidates are reasonable.
    # =================================================================================
    "rr_interval_max_decrease_pct": 0.45, # A new RR interval can't be more than 45% shorter than the previous one.
    "rr_interval_max_increase_pct": 0.70, # A new RR interval can't be more than 70% longer than the previous one.

    "lone_s1_min_strength_ratio": 0.30,
    # A Lone S1 candidate's strength must be at least this fraction of the previous S1's strength.

    "lone_s1_forward_check_pct": 0.60,
    # The time gap to the *next* peak must be greater than (R-R Interval * this value). Otherwise, it's a BPM spike.

    # =================================================================================
    # 10. Post-Processing & Correction Passes
    # Settings for the final analysis passes that use local context to fix errors.
    # =================================================================================
    "rr_correction_threshold_pct": 0.60, # For post-correction pass, an RR interval shorter than N% of the median is flagged for correction.
    "enable_correction_pass": False,          # Master switch to enable/disable the contextual correction feature.
    "correction_pass_window_beats": 40,       # The size of the moving window (in beats) to calculate the local pairing ratio.
    "correction_pass_ratio_threshold": 0.70,  # If the local pairing ratio is above this, the context is considered "high confidence".
    "penalty_waiver_strength_ratio": 4.0, # S1 peak must be this many times > noise floor to allow a penalty waiver.
    "penalty_waiver_max_s2_s1_ratio": 2.5, # Even if waived, penalty still applies if S2 is more than N times larger than S1.

    # =================================================================================
    # 11. Output & HRV Settings
    # Parameters that control the final output data and Heart Rate Variability (HRV) calculations.
    # =================================================================================
    "output_smoothing_window_sec": 5, # The time window (in seconds) for smoothing the final BPM curve for display.
    "hrv_window_size_beats": 40,      # The size of the sliding window in number of beats for HRV calculation.
    "hrv_step_size_beats": 5          # How many beats the HRV window moves in each step.
}

def convert_to_wav(file_path, target_path):
    if not AudioSegment:
        raise ImportError("Pydub/FFmpeg is required for audio conversion.")
    logging.info(f"Converting {os.path.basename(file_path)} to WAV format...")
    try:
        sound = AudioSegment.from_file(file_path)
        sound = sound.set_channels(1) # Convert to mono
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

    # This check now prevents the crash even if logic above fails.
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
    """
    Calculates a dynamic noise floor based on a sanitized set of audio troughs
    """
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
    to reflect physiological expectations (contractility).
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
    """
    Checks if a peak should be vetoed by the 'lookahead' rule.
    Returns a tuple: (True, reason_string) if the peak is vetoed, (False, "") otherwise.
    """
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
    Returns a tuple: (score, reason_string)
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
    """
    Updates the long-term BPM belief based on a new R-R interval.
    Returns the updated BPM value.
    """
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

def evaluate_pairing_confidence(s1_idx, s2_idx, smoothed_deviation, audio_envelope, dynamic_noise_floor,
                              long_term_bpm, dynamic_boost_amount, params, sample_rate,
                              peak_bpm_time_sec, recovery_end_time_sec):
    """
    Evaluates the confidence of an S1-S2 pair using a state-aware, BPM-dependent model
    that accounts for a high-contractility recovery phase post-exertion.
    """
    s1_amp = audio_envelope[s1_idx]
    s2_amp = audio_envelope[s2_idx]
    reason = ""
    penalty_applied = False # We can rename this to has_unexpected_ratio later


    # Base confidence from amplitude deviation
    threshold = params.get('pairing_confidence_threshold', 0.52)
    confidence = calculate_blended_confidence(smoothed_deviation, long_term_bpm, params)
    reason += f"| Base Pairing Conf: {confidence:.2f} (vs Threshold: {threshold:.2f}) "

    # --- State-Aware Contractility Logic ---
    current_beat_time_sec = s1_idx / sample_rate
    is_in_recovery = False

    # Check if a recovery phase was detected and if we are currently in it
    if peak_bpm_time_sec is not None and recovery_end_time_sec is not None:
        if peak_bpm_time_sec < current_beat_time_sec < recovery_end_time_sec:
            is_in_recovery = True

    if is_in_recovery:
        effective_bpm_for_rules = max(long_term_bpm, params['contractility_bpm_low'])
        reason += (
            f"\n- STATE: Post-Exertion Recovery."
            f"\n- Result: Effective BPM for rules is capped at a minimum of {params['contractility_bpm_low']:.0f}. (Actual: {long_term_bpm:.0f} BPM)"
        )
        # In recovery, the rules can relax as BPM drops, but only down to a certain point.
        # We use the current long_term_bpm, but prevent it from dropping below our 'low contractility' threshold.

        bpm_points = [params['contractility_bpm_low'], params['contractility_bpm_high']]
        ratio_points = [params['s2_s1_ratio_low_bpm'], params['s2_s1_ratio_high_bpm']]
        adjustment_points = [params['confidence_adjustment_low_bpm'], params['confidence_adjustment_high_bpm']]
        max_expected_s2_s1_ratio = np.interp(effective_bpm_for_rules, bpm_points, ratio_points)
        adjustment_factor = np.interp(effective_bpm_for_rules, bpm_points, adjustment_points)
    else:
        # STATE: Normal. Use the standard, flexible BPM-based interpolation.
        bpm_points = [params['contractility_bpm_low'], params['contractility_bpm_high']]
        ratio_points = [params['s2_s1_ratio_low_bpm'], params['s2_s1_ratio_high_bpm']]
        adjustment_points = [params['confidence_adjustment_low_bpm'], params['confidence_adjustment_high_bpm']]

        max_expected_s2_s1_ratio = np.interp(long_term_bpm, bpm_points, ratio_points)
        adjustment_factor = np.interp(long_term_bpm, bpm_points, adjustment_points)

    # Check if the observed S2/S1 ratio exceeds our state-aware expectation
    current_s2_s1_ratio = s2_amp / (s1_amp + 1e-9)
    if current_s2_s1_ratio > max_expected_s2_s1_ratio:
        confidence *= adjustment_factor
        penalty_applied = True
        reason += (
            f"\n- ADJUSTED (Next peak is too loud to be a plausible S2 at this BPM)."
            f"\n- Justification: S2/S1 Ratio {current_s2_s1_ratio:.1f}x > Expected {max_expected_s2_s1_ratio:.1f}x at {long_term_bpm:.0f} BPM."
            f"\n- Result: Confidence adjusted to {confidence:.2f}."
        )
    # Standard Boost Logic (when S1 > S2)
    elif s1_amp > (s2_amp * params.get('s1_s2_boost_ratio', 1.2)):
        # Use the new dynamic_boost_amount instead of a fixed value
        confidence = min(1.0, confidence + dynamic_boost_amount)
        reason += f"| BOOSTED to {confidence:.2f} (S1 > S2, Dynamic Boost: {dynamic_boost_amount:.2f}) "

    return confidence, reason, penalty_applied

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
        min_forward_interval = expected_rr_sec * params.get('lone_s1_forward_check_pct', 0.6)

        if forward_interval_sec < min_forward_interval:
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

    # Create a pandas Series with a proper time index from the start
    deviation_times = (all_peaks[:-1] + all_peaks[1:]) / 2 / sample_rate
    deviation_series = pd.Series(normalized_deviations, index=deviation_times)

    # Smooth the series
    smoothing_window_peaks = max(5, int(len(deviation_series) * params['deviation_smoothing_factor']))
    smoothed_dev_series = deviation_series.rolling(window=smoothing_window_peaks, min_periods=1, center=True).mean()

    # Store the final, smoothed PANDAS SERIES in analysis_data
    analysis_data["deviation_series"] = smoothed_dev_series
    # Also store the original times for any other potential use
    analysis_data["deviation_times"] = deviation_times


    # Step 2: Stateful classification loop
    long_term_bpm = float(start_bpm_hint) if start_bpm_hint else 80.0
    candidate_beats, beat_debug_info, long_term_bpm_history = [], {}, []
    sorted_troughs = sorted(trough_indices)
    i = 0
    while i < len(all_peaks):
        # --- DYNAMIC BOOST CALCULATION ---
        pairing_ratio = 0.0
        history_window = params.get('boost_history_window', 20)

        # Check if we are in the "startup phase" (not enough history yet)
        if len(candidate_beats) < history_window:
            # Use the default high startup boost
            dynamic_boost_amount = params.get('boost_startup_amount', 0.25)
        else:
            recent_beats = candidate_beats[-history_window:]
            paired_count = sum(1 for beat_idx in recent_beats if "S1 (Paired)" in beat_debug_info.get(beat_idx, ""))
            pairing_ratio = paired_count / history_window

            # Interpolate the boost amount based on the pairing ratio
            min_boost = params.get('boost_amount_min', 0.05)
            max_boost = params.get('boost_amount_max', 0.25)
            dynamic_boost_amount = np.interp(pairing_ratio, [0.0, 1.0], [min_boost, max_boost])

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

            # The deviation series index is now time-based, so we find the nearest value.
            current_time = current_peak_idx / sample_rate
            deviation_value = smoothed_dev_series.asof(current_time)


            pairing_confidence, pair_reason, penalty_applied = evaluate_pairing_confidence(
                current_peak_idx, next_peak_idx, deviation_value, audio_envelope,
                dynamic_noise_floor, long_term_bpm, dynamic_boost_amount, params,
                sample_rate, peak_bpm_time_sec, recovery_end_time_sec
            )
            reason += pair_reason
            is_paired = interval_sec <= s1_s2_max_interval and pairing_confidence >= params['pairing_confidence_threshold']

            if is_paired:
                candidate_beats.append(current_peak_idx)
                beat_debug_info[current_peak_idx] = f"S1 (Paired). {reason.lstrip(' |')}"
                beat_debug_info[next_peak_idx] = f"S2 (Paired). Justification: {reason.lstrip(' |')}"
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
                else:
                    beat_debug_info[current_peak_idx] = f"Noise ({rejection_detail}). Original pairing reason: [{reason.lstrip(' |')}]"
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

def correct_beats_with_local_context(s1_peaks, all_raw_peaks, beat_debug_info, params):
    """
    Performs a second analysis pass to correct misclassified beats using local rhythm context.

    This function identifies 'Lone S1' beats that are likely part of a missed pair
    by analyzing the pairing success rate in their local neighborhood.
    """
    if not params.get("enable_correction_pass", False) or len(s1_peaks) < params["correction_pass_window_beats"]:
        logging.info("Correction pass skipped (disabled or not enough beats).")
        return s1_peaks, beat_debug_info, 0

    logging.info("--- STAGE 5: Running Correction Pass with Local Rhythm Context ---")

    pairing_success = [1 if "S1 (Paired)" in beat_debug_info.get(peak_idx, "") else 0 for peak_idx in s1_peaks]
    pairing_series = pd.Series(pairing_success, name="pairing_ratio")
    window_size = params["correction_pass_window_beats"]
    local_pairing_ratio = pairing_series.rolling(window=window_size, min_periods=max(1, window_size // 2)).mean().bfill().ffill()

    if local_pairing_ratio.empty:
        logging.warning("Could not calculate local pairing ratio. Skipping correction.")
        return s1_peaks, beat_debug_info, 0

    corrected_debug_info = beat_debug_info.copy()
    raw_peaks_list = all_raw_peaks.tolist()
    corrections_made = 0
    s1_peak_to_position = {peak: i for i, peak in enumerate(s1_peaks)}

    for s1_peak_idx in s1_peaks:
        if beat_debug_info.get(s1_peak_idx, "").startswith("Lone S1"):
            try:
                current_raw_idx = raw_peaks_list.index(s1_peak_idx)
                if current_raw_idx + 1 < len(raw_peaks_list):
                    next_raw_peak = raw_peaks_list[current_raw_idx + 1]
                else:
                    continue
            except ValueError:
                continue

            if beat_debug_info.get(next_raw_peak, "").startswith("Noise (Rejected Failed S2 Candidate)"):
                s1_position = s1_peak_to_position.get(s1_peak_idx)
                if s1_position is None: continue

                current_local_ratio = local_pairing_ratio.iloc[s1_position]

                if current_local_ratio >= params["correction_pass_ratio_threshold"]:
                    corrections_made += 1

                    original_reason = corrected_debug_info[s1_peak_idx]
                    corrected_debug_info[s1_peak_idx] = f"S1 (Paired - Corrected). Original: [{original_reason}]"

                    original_noise_reason = corrected_debug_info[next_raw_peak]
                    corrected_debug_info[next_raw_peak] = f"S2 (Paired - Corrected). Justification: High local pairing ratio ({current_local_ratio:.2f}). Original: [{original_noise_reason}]"

    logging.info(f"Correction pass complete. Relabeled {corrections_made} S1/S2 pairs.")

    final_s1_peaks = np.array(sorted([
        peak for peak, reason in corrected_debug_info.items()
        if reason.startswith("S1 (Paired") or reason.startswith("Lone S1")
    ]))

    return final_s1_peaks, corrected_debug_info, corrections_made

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

def _add_base_traces(fig, time_axis_dt, audio_envelope, analysis_data):
    """Adds the audio envelope, troughs, and noise floor traces to the plot."""
    fig.add_trace(go.Scatter(x=time_axis_dt, y=audio_envelope, name="Audio Envelope", line=dict(color="#47a5c4")), secondary_y=False)
    if 'trough_indices' in analysis_data and analysis_data['trough_indices'].size > 0:
        trough_indices = analysis_data['trough_indices']
        start_datetime = datetime.datetime.fromtimestamp(0)
        trough_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in (trough_indices / analysis_data['sample_rate'])])
        fig.add_trace(go.Scatter(
            x=trough_times_dt, y=audio_envelope[trough_indices], mode='markers', name='Troughs',
            marker=dict(color='green', symbol='circle-open', size=6), visible='legendonly'
        ), secondary_y=False)
    if 'dynamic_noise_floor_series' in analysis_data and not analysis_data['dynamic_noise_floor_series'].empty:
        fig.add_trace(go.Scatter(
            x=time_axis_dt, y=analysis_data['dynamic_noise_floor_series'].values, name="Dynamic Noise Floor",
            line=dict(color="green", dash="dot", width=1.5), hovertemplate="Noise Floor: %{y:.2f}<extra></extra>"
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
    analysis_data['sample_rate'] = sample_rate # Ensure sample_rate is available for helpers

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Call helper functions to build the plot step-by-step
    _add_base_traces(fig, time_axis_dt, audio_envelope, analysis_data)
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
    fig.update_yaxes(title_text="Signal Amplitude", secondary_y=False, range=[0, robust_upper_limit * 60])
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

def _prepare_log_data(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm):
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
        smoothed_bpm_sec_index = pd.Series(data=smoothed_bpm.values, index=smoothed_bpm.index.astype(np.int64) // 10**9)
        if not smoothed_bpm_sec_index.index.is_unique:
            smoothed_bpm_sec_index = smoothed_bpm_sec_index.groupby(level=0).mean()
        master_df['smoothed_bpm'] = smoothed_bpm_sec_index

    # Handle long_term_bpm_series
    if 'long_term_bpm_series' in analysis_data and not analysis_data['long_term_bpm_series'].empty:
        lt_bpm_series = analysis_data['long_term_bpm_series']
        if not lt_bpm_series.index.is_unique:
            lt_bpm_series = lt_bpm_series.groupby(level=0).mean()
        master_df['lt_bpm'] = lt_bpm_series

    # Handle deviation_series (which is now guaranteed to be a Series)
    if 'deviation_series' in analysis_data and not analysis_data['deviation_series'].empty:
        dev_series = analysis_data['deviation_series']
        if not dev_series.index.is_unique:
            dev_series = dev_series.groupby(level=0).mean()
        master_df['deviation'] = dev_series

    master_df.sort_index(inplace=True)
    return pd.merge_asof(left=events_df, right=master_df.ffill(), left_index=True,
                         right_index=True, direction='nearest', tolerance=pd.Timedelta(seconds=0.5).total_seconds())

def _write_log_events(log_file, merged_df, file_name):
    """Writes the formatted log events to the file."""
    log_file.write(f"# Chronological Debug Log for {os.path.basename(file_name)}\n")
    log_file.write(f"Analysis performed on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    for t, row in merged_df.iterrows():
        log_file.write(f"## Time: `{t:.4f}s`\n")
        reason = row.get('reason', '')

        status_line = ""
        if row['type'] == 'Peak':
            if '. Justification: ' in reason:
                parts = reason.split('. Justification: ', 1)
                details = parts[1].strip().replace(' | ', '\n- ')
                status_line = f"**{parts[0].strip()}.**\n- **Justification:** {details}"
            elif '. ' in reason:
                parts = reason.split('. ', 1)
                details = parts[1].strip().replace(' | ', '\n- ')
                status_line = f"**{parts[0].strip()}.**\n- {details}"
            elif '(' in reason and ')' in reason:
                parts = reason.split('(', 1)
                details = parts[1].rsplit(')', 1)[0].strip().replace(' | ', '\n- ')
                status_line = f"**{parts[0].strip()}**\n- {details}"
            else:
                status_line = f"**{reason}**"
            log_file.write(f"{status_line}\n")
            if 'amp' in row and not pd.isna(row['amp']): log_file.write(f"**Raw Peak** (Amp: {row['amp']:.2f})\n")
        else: # Trough
             log_file.write(f"**Trough Detected** (Amp: {row['amp']:.2f})\n")

        if 'envelope' in row and not pd.isna(row['envelope']): log_file.write(f"**Audio Envelope**: `{row['envelope']:.2f}`\n")
        if 'noise_floor' in row and not pd.isna(row['noise_floor']): log_file.write(f"**Noise Floor**: `{row['noise_floor']:.2f}`\n")
        if 'S1' in reason:
            if 'smoothed_bpm' in row and not pd.isna(row['smoothed_bpm']): log_file.write(f"**Average BPM (Smoothed)**: {row['smoothed_bpm']:.2f}\n")
            if 'lt_bpm' in row and not pd.isna(row['lt_bpm']): log_file.write(f"**Long-Term BPM (Belief)**: {row['lt_bpm']:.2f}\n")
            if 'deviation' in row and not pd.isna(row['deviation']): log_file.write(f"**Norm. Deviation**: {row['deviation'] * 100:.2f}%\n")
        log_file.write("\n")

def create_chronological_log_file(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm, output_log_path, file_name):
    """Creates a chronological debug log using efficient, vectorized pandas operations."""
    logging.info(f"Generating readable debug log at '{output_log_path}'...")
    merged_df = _prepare_log_data(audio_envelope, sample_rate, all_raw_peaks, analysis_data, smoothed_bpm)

    with open(output_log_path, "w", encoding="utf-8") as log_file:
        if merged_df is None or merged_df.empty:
            log_file.write("# No significant events (peaks or troughs) were detected to log.\n")
        else:
            _write_log_events(log_file, merged_df, file_name)
    logging.info("Debug log generation complete.")

def find_major_hr_inclines(smoothed_bpm_series, min_duration_sec=10, min_bpm_increase=15):
    """ Identifies significant, sustained periods of heart rate increase."""
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
    """ Identifies significant, sustained periods of heart rate decrease (recovery)."""
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
    """ Finds the steepest slope of heart rate decline after the peak BPM."""
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
    """ Finds the steepest slope of heart rate increase across the entire recording."""
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
    """ Calculates the standard Heart Rate Recovery (HRR) over a fixed interval. """
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
    """
    Analyzes a preliminary BPM series to find the peak heart rate and define
    the subsequent recovery phase window.
    Returns the start and end time of the recovery phase in seconds.
    """
    if bpm_times_sec is None or len(bpm_times_sec) < 2:
        logging.warning("Not enough preliminary beats to determine a recovery phase.")
        return None, None
    peak_time_sec = bpm_times_sec[np.argmax(bpm_series.values)]
    recovery_end_time_sec = peak_time_sec + params.get("recovery_phase_duration_sec", 120.0)
    logging.info(f"Peak BPM detected in preliminary pass at {peak_time_sec:.2f}s. High-contractility state defined until {recovery_end_time_sec:.2f}s.")
    return peak_time_sec, recovery_end_time_sec

# --- Analysis Pipeline Helpers ---

def _run_stage1_anchor_beat_pass(audio_envelope, sample_rate, params):
    """Runs a high-confidence first pass to find anchor beats and estimate global BPM."""
    logging.info("--- STAGE 1: Running High-Confidence pass to find anchor beats ---")
    params_pass_1 = params.copy()
    params_pass_1["pairing_confidence_threshold"] = 0.75
    params_pass_1["enable_bpm_boost"] = True

    anchor_beats, _, _ = find_heartbeat_peaks(audio_envelope, sample_rate, params_pass_1)

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

def _run_iterative_correction_pass(s1_peaks, all_raw_peaks, debug_info, params):
    """Runs the contextual correction pass iteratively until it stabilizes."""
    final_peaks = s1_peaks
    corrected_debug_info = debug_info.copy()
    max_iterations = 5  # Safeguard

    for i in range(max_iterations):
        new_peaks, new_debug_info, corrections_made = correct_beats_with_local_context(
            s1_peaks=final_peaks, all_raw_peaks=all_raw_peaks,
            beat_debug_info=corrected_debug_info, params=params)

        final_peaks, corrected_debug_info = new_peaks, new_debug_info
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
    file_name_no_ext = os.path.splitext(wav_file_path)[0]
    logging.info(f"--- Processing file: {os.path.basename(wav_file_path)} ---")
    audio_envelope, sample_rate = preprocess_audio(wav_file_path, params)

    # STAGE 1: Automated global BPM estimation and recovery phase detection
    global_bpm_estimate, peak_bpm_time_sec, recovery_end_time_sec = _run_stage1_anchor_beat_pass(audio_envelope, sample_rate, params)
    final_start_bpm = _determine_start_bpm(start_bpm_hint, global_bpm_estimate)

    # STAGE 2: Refined noise floor calculation
    logging.info("--- STAGE 2: Performing trough sanitization for a refined noise floor ---")
    sanitized_noise_floor, sanitized_troughs = _calculate_dynamic_noise_floor(audio_envelope, sample_rate, params)

    # STAGE 3: Primary analysis pass with refined inputs
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

    # STAGE 5: Iterative contextual correction pass
    final_peaks, final_debug_info = _run_iterative_correction_pass(
        s1_peaks_pass2, all_raw_peaks, analysis_data["beat_debug_info"], params)
    analysis_data["beat_debug_info"] = final_debug_info

    # --- FINAL CALCULATIONS AND OUTPUT ---
    if len(final_peaks) < 2:
        logging.warning("Not enough S1 peaks detected after correction to calculate BPM.")
        plot_results(audio_envelope, final_peaks, all_raw_peaks, analysis_data, pd.Series(dtype=np.float64), np.array([]), sample_rate, wav_file_path, params)
        return

    metrics = _calculate_final_metrics(final_peaks, sample_rate, params)

    # --- Save Reports and Plots (Corrected Function Calls) ---
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
    create_chronological_log_file(audio_envelope, sample_rate, all_raw_peaks, analysis_data, metrics['smoothed_bpm'], output_log_path, wav_file_path)


# --- GUI Class (unchanged) ---
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