import os
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import datetime
import logging
import sys
import time
from typing import List, Dict, Tuple, Optional
from enum import Enum

from audio_io import preprocess_audio

# --- Enums and Global Helpers ---
class PeakType(Enum):
    """Enumeration for classifying heartbeat peaks."""
    S1_PAIRED = "S1 (Paired)"
    S2_PAIRED = "S2 (Paired)"
    LONE_S1_VALIDATED = "Lone S1"
    LONE_S1_CASCADE = "Lone S1 (Corrected by Cascade Reset)"
    LONE_S1_LAST = "Lone S1 (Last Peak)"
    NOISE = "Noise/Rejected"
    S1_CORRECTED_GAP = "S1 (Paired - Corrected from Gap)"
    S2_CORRECTED_GAP = "S2 (Paired - Corrected from Gap)"
    S2_CORRECTED_CONFLICT = "S2 (Paired - Corrected from Conflict)"

    @classmethod
    def is_s1(cls, peak_type_str: str) -> bool:
        """Check if a string corresponds to any S1 type."""
        return peak_type_str.strip().startswith("S1") or peak_type_str.strip().startswith("Lone S1")

    @classmethod
    def is_s2(cls, peak_type_str: str) -> bool:
        """Check if a string corresponds to any S2 type."""
        return peak_type_str.strip().startswith("S2")


def _get_peak_type_from_debug(entry) -> str:
    """
    Helper to safely extract the peak_type string from a debug entry.
    Supports both the new dict-based structure and legacy string values.
    """
    if isinstance(entry, dict):
        return entry.get("peak_type", "")
    if isinstance(entry, str):
        # Legacy packing used '§' as a separator: '<PeakType>§TAG§VALUE...'
        return entry.split('§', 1)[0] if entry else ""
    return ""


def _is_s1_paired_debug(entry) -> bool:
    """Returns True if a debug entry represents a paired S1."""
    return _get_peak_type_from_debug(entry) == PeakType.S1_PAIRED.value


def _is_lone_s1_debug(entry) -> bool:
    """Returns True if a debug entry represents any Lone S1 classification."""
    pt = _get_peak_type_from_debug(entry)
    return pt.startswith("Lone S1")


def _is_noise_debug(entry) -> bool:
    """Returns True if a debug entry represents a Noise/Rejected classification."""
    pt = _get_peak_type_from_debug(entry)
    return "Noise" in pt


def format_debug_entry(debug_entry: Dict) -> List[str]:
    """
    Converts a structured debug entry into a list of human-readable lines.

    Shared formatter used by plotting tooltips and debug logs.
    """
    if not isinstance(debug_entry, dict):
        if not debug_entry:
            return []
        text = str(debug_entry)
        return ["- Details:", f"    - {text}"]

    lines: List[str] = []
    sections = debug_entry.get("sections", [])

    for sec in sections:
        sec_type = sec.get("type")

        if sec_type == "pairing":
            lines.append("- S1-S2 pairing decision:")
            raw_lines = sec.get("lines")
            if raw_lines is None:
                text = sec.get("text", "")
                raw_lines = [t.strip() for t in text.split("\n") if t.strip()]
            for ln in raw_lines:
                lines.append(f"    - {ln}")

        elif sec_type == "lone_s1":
            lines.append("- Lone S1 decision:")
            raw_lines = sec.get("lines") or []
            for ln in raw_lines:
                lines.append(f"    - {ln}")

        elif sec_type == "lookahead":
            msg = sec.get("text") or sec.get("message")
            if msg:
                lines.append(f"- {msg}")

        elif sec_type == "original":
            original = sec.get("original_debug")
            if isinstance(original, dict):
                orig_type = original.get("peak_type", "Unknown")
                lines.append(f"- Original Classification: {orig_type}")
            elif original:
                lines.append("- Original Classification:")
                lines.append(f"    - {original}")

    return lines

# Import helpers for plotting/reporting after they are defined to avoid circular imports
from plotting import Plotter
from reporting import ReportGenerator


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
    logging.warning("Pydub library not found. Install with 'pip install pydub'.")
    AudioSegment = None

# --- Core Classes for Analysis Pipeline ---
class PeakClassifier:
    """
    Encapsulates the logic for classifying raw audio peaks into S1, S2, and Noise.
    This class manages the state of the analysis loop, including BPM belief,
    beat candidates, and debug information.
    """
    def __init__(self, audio_envelope: np.ndarray, sample_rate: int, params: Dict,
                 start_bpm_hint: Optional[float], precomputed_noise_floor: pd.Series,
                 precomputed_troughs: np.ndarray, peak_bpm_time_sec: Optional[float],
                 recovery_end_time_sec: Optional[float]):

        self.audio_envelope = audio_envelope
        self.sample_rate = sample_rate
        self.params = params
        self.peak_bpm_time_sec = peak_bpm_time_sec
        self.recovery_end_time_sec = recovery_end_time_sec

        self.state = self._initialize_state(
            start_bpm_hint, precomputed_noise_floor, precomputed_troughs
        )

    def _initialize_state(self, start_bpm_hint, precomputed_noise_floor, precomputed_troughs) -> Dict:
        """Pre-calculates all necessary data and initializes the state for the peak finding loop."""
        state = {'analysis_data': {}}
        state['dynamic_noise_floor'], state['trough_indices'] = precomputed_noise_floor, precomputed_troughs
        state['all_peaks'] = self._find_raw_peaks(state['dynamic_noise_floor'].values)
        state['analysis_data']['dynamic_noise_floor_series'] = state['dynamic_noise_floor']
        state['analysis_data']['trough_indices'] = state['trough_indices']

        noise_floor_at_peaks = state['dynamic_noise_floor'].reindex(state['all_peaks'], method='nearest').values
        peak_strengths = self.audio_envelope[state['all_peaks']] - noise_floor_at_peaks
        peak_strengths[peak_strengths < 0] = 0
        normalized_deviations = np.abs(np.diff(peak_strengths)) / (np.maximum(peak_strengths[:-1], peak_strengths[1:]) + 1e-9)
        deviation_times = (state['all_peaks'][:-1] + state['all_peaks'][1:]) / 2 / self.sample_rate
        deviation_series = pd.Series(normalized_deviations, index=deviation_times)
        smoothing_window = max(5, int(len(deviation_series) * self.params['deviation_smoothing_factor']))
        state['smoothed_dev_series'] = deviation_series.rolling(window=smoothing_window, min_periods=1, center=True).mean()
        state['analysis_data']['deviation_series'] = state['smoothed_dev_series']

        state['long_term_bpm'] = float(start_bpm_hint) if start_bpm_hint else 80.0
        state['candidate_beats'] = []
        state['beat_debug_info'] = {}
        state['long_term_bpm_history'] = []
        state['sorted_troughs'] = sorted(state['trough_indices'])
        state['consecutive_rr_rejections'] = 0
        state['loop_idx'] = 0

        return state

    def classify_peaks(self) -> Tuple[np.ndarray, np.ndarray, Dict]:
        """Main classification loop to iterate through all raw peaks."""
        if len(self.state['all_peaks']) < 2:
            return self.state['all_peaks'], self.state['all_peaks'], {"beat_debug_info": {}}

        while self.state['loop_idx'] < len(self.state['all_peaks']):
            self._kickstart_check()
            current_peak_idx = self.state['all_peaks'][self.state['loop_idx']]
            is_last_peak = self.state['loop_idx'] >= len(self.state['all_peaks']) - 1

            if is_last_peak:
                self._handle_last_peak(current_peak_idx)
            else:
                self._process_peak_pair(current_peak_idx)

            self._update_long_term_bpm()

        return self._finalize_results()

    def _kickstart_check(self):
        """Specialized recovery function to kick-start the algorithm if it gets stuck."""
        # Calculate recent rhythm stability as a ratio
        history_window = self.params.get("stability_history_window", 20)
        if len(self.state['candidate_beats']) < history_window:
            pairing_ratio = 0.5
        else:
            recent_beats = self.state['candidate_beats'][-history_window:]
            paired_count = sum(
                1 for beat_idx in recent_beats
                if _is_s1_paired_debug(self.state['beat_debug_info'].get(beat_idx))
            )
            pairing_ratio = paired_count / history_window
            
        if pairing_ratio >= self.params.get("kickstart_check_threshold", 0.3):
            return

        history = 4  # Hardcoded history beats
        if len(self.state['candidate_beats']) < history:
            return

        min_s1s = 3  # Hardcoded min S1 candidates
        recent_lone_s1s = [
            idx for idx in self.state['candidate_beats'][-history:]
            if _is_lone_s1_debug(self.state['beat_debug_info'].get(idx))
        ]
        if len(recent_lone_s1s) < min_s1s:
            return

        min_matches = 3  # Hardcoded min matches
        matches = 0
        for s1_idx in recent_lone_s1s:
            current_raw_idx = np.searchsorted(self.state['all_peaks'], s1_idx)
            if current_raw_idx < len(self.state['all_peaks']) - 1:
                next_raw_peak_idx = self.state['all_peaks'][current_raw_idx + 1]
                if _is_noise_debug(self.state['beat_debug_info'].get(next_raw_peak_idx)):
                    matches += 1

        if matches >= min_matches:
            override_ratio = self.params.get("kickstart_override_ratio", 0.6)
            logging.info(f"KICK-START: Found {matches}/{len(recent_lone_s1s)} S1->Noise patterns. Overriding pairing ratio to {override_ratio}.")
            # This is a temporary state change, so we don't store the override ratio in self.state
            self.state['pairing_ratio_override'] = override_ratio

    def _handle_last_peak(self, peak_idx: int):
        """Classify the final peak in the sequence."""
        self.state['candidate_beats'].append(peak_idx)
        self.state['beat_debug_info'][peak_idx] = {
            "peak_type": PeakType.LONE_S1_LAST.value,
            "sections": []
        }
        self.state['loop_idx'] += 1

    def _calculate_pairing_ratio(self) -> float:
        """Calculate recent rhythm stability ratio."""
        history_window = self.params.get("stability_history_window", 20)
        if len(self.state['candidate_beats']) < history_window:
            return 0.5
        
        recent_beats = self.state['candidate_beats'][-history_window:]
        paired_count = sum(
            1 for beat_idx in recent_beats 
            if _is_s1_paired_debug(self.state['beat_debug_info'].get(beat_idx))
        )
        return paired_count / history_window

    def _process_peak_pair(self, current_peak_idx: int):
        """Processes a pair of peaks to determine if they are S1-S2."""
        all_peaks = self.state['all_peaks']
        loop_idx = self.state['loop_idx']

        # Calculate recent rhythm stability as a ratio (shared helper)
        pairing_ratio = self._calculate_pairing_ratio()

        # We always have at least one "next" peak here (caller guards last-peak case)
        next_peak_idx = all_peaks[loop_idx + 1]

        # --- LOOKAHEAD: optionally skip a weak middle peak between a strong S1 and S2 ---
        if self.params.get('enable_lookahead_skipping', True) and loop_idx + 2 < len(all_peaks):
            middle_peak_idx = next_peak_idx
            next_next_peak_idx = all_peaks[loop_idx + 2]

            # Heuristic: treat the middle peak as noise if its prominence is much weaker than the S1 candidate
            current_prom = calculate_peak_prominence(
                current_peak_idx, self.audio_envelope, self.state['trough_indices']
            )
            middle_prom = calculate_peak_prominence(
                middle_peak_idx, self.audio_envelope, self.state['trough_indices']
            )
            noise_thresh = self.params.get('noise_prominence_threshold', 0.35)

            if middle_prom < current_prom * noise_thresh:
                # Try pairing current + next_next (skip the middle)
                is_paired_skip, reason_skip = self._attempt_s1_s2_pairing(
                    current_peak_idx, next_next_peak_idx, pairing_ratio
                )

                if is_paired_skip:
                    # Build a shared pairing section from the skip reason
                    pairing_lines = [
                        line.strip().lstrip('- ')
                        for line in reason_skip.strip().split("\n")
                        if line.strip()
                    ]
                    lookahead_msg = (
                        "LOOKAHEAD SUCCESS: Skipped intermediate weak peak "
                        f"(middle prominence {middle_prom:.3f} < {noise_thresh:.2f} × "
                        f"S1 prominence {current_prom:.3f})"
                    )

                    s1_sections = [
                        {"type": "lookahead", "text": lookahead_msg},
                        {"type": "pairing", "lines": pairing_lines, "success": True},
                    ]
                    s2_sections = [
                        {"type": "lookahead", "text": lookahead_msg},
                        {"type": "pairing", "lines": pairing_lines, "success": True},
                    ]

                    self.state['candidate_beats'].append(current_peak_idx)
                    self.state['beat_debug_info'][current_peak_idx] = {
                        "peak_type": PeakType.S1_PAIRED.value,
                        "sections": s1_sections,
                    }

                    original_middle_debug = self.state['beat_debug_info'].get(middle_peak_idx)
                    self.state['beat_debug_info'][middle_peak_idx] = {
                        "peak_type": PeakType.NOISE.value,
                        "sections": [
                            {
                                "type": "lookahead",
                                "text": (
                                    "Middle peak treated as noise due to weak prominence "
                                    f"({middle_prom:.3f} < {noise_thresh:.2f} × "
                                    f"S1 prominence {current_prom:.3f})"
                                ),
                            },
                            {
                                "type": "original",
                                "original_debug": original_middle_debug,
                            },
                        ],
                    }

                    self.state['beat_debug_info'][next_next_peak_idx] = {
                        "peak_type": PeakType.S2_PAIRED.value,
                        "sections": s2_sections,
                    }

                    self.state['consecutive_rr_rejections'] = 0
                    # Skip the S1, middle noise, and S2 peaks
                    self.state['loop_idx'] += 3
                    return

        # --- Standard pairing attempt (existing logic) ---
        is_paired, reason = self._attempt_s1_s2_pairing(
            current_peak_idx, next_peak_idx, pairing_ratio
        )

        if is_paired:
            self.state['candidate_beats'].append(current_peak_idx)
            pairing_lines = [
                line.strip().lstrip('- ')
                for line in reason.strip().split("\n")
                if line.strip()
            ]
            sections = [{"type": "pairing", "lines": pairing_lines, "success": True}]
            self.state['beat_debug_info'][current_peak_idx] = {
                "peak_type": PeakType.S1_PAIRED.value,
                "sections": sections,
            }
            self.state['beat_debug_info'][next_peak_idx] = {
                "peak_type": PeakType.S2_PAIRED.value,
                "sections": sections,
            }
            self.state['consecutive_rr_rejections'] = 0
            self.state['loop_idx'] += 2
        else:
            self._classify_lone_peak(current_peak_idx, reason)
            self.state['loop_idx'] += 1

    def _update_long_term_bpm(self):
        """Updates the long-term BPM belief after each decision."""
        if len(self.state['candidate_beats']) > 1:
            new_rr = (self.state['candidate_beats'][-1] - self.state['candidate_beats'][-2]) / self.sample_rate
            if new_rr > 0:
                self.state['long_term_bpm'] = update_long_term_bpm(new_rr, self.state['long_term_bpm'], self.params)

        if self.state['candidate_beats']:
            time_sec = self.state['candidate_beats'][-1] / self.sample_rate
            self.state['long_term_bpm_history'].append((time_sec, self.state['long_term_bpm']))

    def _finalize_results(self) -> Tuple[np.ndarray, np.ndarray, Dict]:
        """Finalizes and returns the analysis results."""
        final_peaks = np.array(sorted(list(dict.fromkeys(self.state['candidate_beats']))))
        self.state['analysis_data']["beat_debug_info"] = self.state['beat_debug_info']
        if self.state['long_term_bpm_history']:
            lt_bpm_times, lt_bpm_values = zip(*self.state['long_term_bpm_history'])
            self.state['analysis_data']["long_term_bpm_series"] = pd.Series(lt_bpm_values, index=lt_bpm_times)
        return final_peaks, self.state['all_peaks'], self.state['analysis_data']

    def _find_raw_peaks(self, height_threshold: np.ndarray) -> np.ndarray:
        """Finds all potential peaks above the given height threshold."""
        prominence_thresh = np.quantile(self.audio_envelope, self.params['peak_prominence_quantile'])
        min_peak_dist_samples = int(self.params['min_peak_distance_sec'] * self.sample_rate)
        peaks, _ = find_peaks(self.audio_envelope, height=height_threshold, prominence=prominence_thresh, distance=min_peak_dist_samples)
        logging.info(f"Found {len(peaks)} raw peaks using dynamic height threshold.")
        return peaks

    def _attempt_s1_s2_pairing(self, s1_candidate_idx: int, s2_candidate_idx: int, pairing_ratio: float) -> Tuple[bool, str]:
        """Calculates the confidence score for pairing two candidate peaks."""
        interval_sec = (s2_candidate_idx - s1_candidate_idx) / self.sample_rate
        bpm = self.state['long_term_bpm']

        # Minimum S1-S2 as fraction of RR interval (adapts to current BPM)
        min_s1_s2_interval = (60.0 / bpm) * self.params.get('min_s1_s2_interval_rr_fraction', 0.35)
        
        # Absolute minimum S1-S2 interval
        min_s1_s2_interval = max(min_s1_s2_interval, self.params.get('min_s1_s2_interval_sec', 0.15))
        
        if interval_sec < min_s1_s2_interval:
            # Calculate implied BPM for debugging
            # Assuming S2-S1 is at least as long as S1-S2 (conservative estimate)
            implied_total_cycle = interval_sec * 2.0  # S1-S2 + S2-S1
            implied_bpm = 60.0 / implied_total_cycle if implied_total_cycle > 0 else float('inf')
            
            debug_msg = (
                f"Impossible: S1-S2 interval {interval_sec:.3f}s < min {min_s1_s2_interval:.3f}s "
                f"(implies {implied_bpm:.0f} BPM vs assumed {bpm:.0f} BPM)"
            )
            return False, debug_msg

        # --- Base confidence: neutral starting point (contractility handled by prominence adjustment) ---
        base_confidence = 0.60

        reason = f"Base Conf: {base_confidence:.2f}"

        # --- Contractility / prominence-based adjustment (S1 vs S2) ---
        s1_prominence = calculate_peak_prominence(
            s1_candidate_idx, self.audio_envelope, self.state['trough_indices']
        )
        s2_prominence = calculate_peak_prominence(
            s2_candidate_idx, self.audio_envelope, self.state['trough_indices']
        )

        confidence, contractility_reason = adjust_confidence_with_contractility(
            base_confidence,
            s1_prominence,
            s2_prominence,
            bpm,
            self.params,
        )
        reason += contractility_reason

        # --- Other adjustments (stability, ratio history, etc.) ---
        confidence, other_reason = _apply_other_pairing_adjustments(
            confidence,
            s1_candidate_idx,
            s2_candidate_idx,
            self.audio_envelope,
            self.state['dynamic_noise_floor'],
            bpm,
            pairing_ratio,
            self.params,
            self.sample_rate,
            self.peak_bpm_time_sec,
            self.recovery_end_time_sec,
            len(self.state['candidate_beats']),
        )
        reason += other_reason

        s1_s2_max_interval = min(self.params['s1_s2_interval_cap_sec'], (60.0 / self.state['long_term_bpm']) * self.params['s1_s2_interval_rr_fraction'])
        
        # Apply interval penalty if the S1-S2 interval is too long
        if self.params.get("enable_interval_penalty", True) and interval_sec > s1_s2_max_interval:
            start_factor = self.params.get("interval_penalty_start_factor", 1.0)
            full_factor = self.params.get("interval_penalty_full_factor", 1.4)
            max_penalty = self.params.get("interval_max_penalty", 0.75)
            
            penalty_zone_start = s1_s2_max_interval * start_factor
            penalty_zone_end = s1_s2_max_interval * full_factor
            
            if interval_sec > penalty_zone_start:
                exceedance_scale = (interval_sec - penalty_zone_start) / (penalty_zone_end - penalty_zone_start + 1e-9)
                exceedance_scale = np.clip(exceedance_scale, 0, 1)
                penalty_amount = exceedance_scale * max_penalty
                confidence = max(0, confidence - penalty_amount)
                interval_reason = f"\n- Interval penalty by {penalty_amount:.2f} (Interval {interval_sec:.3f}s > Max {s1_s2_max_interval:.3f}s)"
            else:
                interval_reason = ""
        else:
            interval_reason = ""
        reason += interval_reason

        # --- Forward-Looking Contextual Penalty ---
        # If pairing S1-S2 causes the next S2→S1 transition to be implausable, penalize it
        # This prevents: [noise]→[true S1 as S2]→[true S2 bein mislabeled]
        forward_look_penalty = 0.0
        if self.state['loop_idx'] + 2 < len(self.state['all_peaks']):
            next_next_peak_idx = self.state['all_peaks'][self.state['loop_idx'] + 2]
            
            # Use prominence for robust amplitude comparison
            s2_prominence = calculate_peak_prominence(
                s2_candidate_idx, self.audio_envelope, self.state['trough_indices']
            )
            next_s1_prominence = calculate_peak_prominence(
                next_next_peak_idx, self.audio_envelope, self.state['trough_indices']
            )
            
            # Only apply if we have valid data
            if s2_prominence > 1e-9 and next_s1_prominence > 1e-9:
                drop_ratio = next_s1_prominence / s2_prominence
                
                # If the following peak is substantially weaker, it suggests s2_candidate
                # is actually a strong S1, making this S1-S2 pairing incorrect
                threshold = self.params.get('forward_look_drop_threshold', 0.4)
                if drop_ratio < threshold:
                    # Scale penalty by severity of the drop
                    severity = (threshold - drop_ratio) / threshold
                    max_pen = self.params.get('forward_look_max_penalty', 0.3)
                    forward_look_penalty = severity * max_pen
                    
                    confidence = max(0.0, confidence - forward_look_penalty)
                    reason += f"\n- Penalized by Forward-Look {forward_look_penalty:.2f} (S2→S1 drop {drop_ratio:.2f}x < threshold {threshold:.1f}x)"

        is_paired = confidence >= self.params['pairing_confidence_threshold']
        reason += f"\n- Final Score: {confidence:.2f} vs Threshold {self.params['pairing_confidence_threshold']:.2f} -> {'Paired' if is_paired else 'Not Paired'}"
        return is_paired, reason

    def _classify_lone_peak(self, peak_idx: int, pairing_failure_reason: str):
        """Validates if an unpaired peak is a Lone S1 or Noise."""
        is_valid, rejection_detail = self._validate_lone_s1(peak_idx)
        pairing_lines = [
            line.strip().lstrip('- ')
            for line in pairing_failure_reason.strip().split("\n")
            if line.strip()
        ]

        if is_valid:
            self.state['candidate_beats'].append(peak_idx)
            # For a validated S1, the "rejection_detail" is just the success reason.
            self.state['beat_debug_info'][peak_idx] = {
                "peak_type": PeakType.LONE_S1_VALIDATED.value,
                "sections": [
                    {"type": "pairing", "lines": pairing_lines, "success": False},
                    {"type": "lone_s1", "lines": [rejection_detail], "validated": True},
                ],
            }
            self.state['consecutive_rr_rejections'] = 0
        else:
            is_rhythm_rejection = "Rhythm Fit" in rejection_detail
            if is_rhythm_rejection:
                self.state['consecutive_rr_rejections'] += 1
            else:
                self.state['consecutive_rr_rejections'] = 0

            if self.state['consecutive_rr_rejections'] >= self.params.get("cascade_reset_trigger_count", 3):
                logging.info(
                    f"CASCADE RESET: Forcing peak at {peak_idx / self.sample_rate:.2f}s as Lone S1 due to repeated rhythmic failures.")
                self.state['candidate_beats'].append(peak_idx)
                self.state['beat_debug_info'][peak_idx] = {
                    "peak_type": PeakType.LONE_S1_CASCADE.value,
                    "sections": [
                        {"type": "pairing", "lines": pairing_lines, "success": False},
                        {"type": "lone_s1", "lines": [rejection_detail], "validated": False},
                    ],
                }
                self.state['consecutive_rr_rejections'] = 0
            else:
                self.state['beat_debug_info'][peak_idx] = {
                    "peak_type": PeakType.NOISE.value,
                    "sections": [
                        {"type": "pairing", "lines": pairing_lines, "success": False},
                        {"type": "lone_s1", "lines": [rejection_detail], "validated": False},
                    ],
                }

    def _validate_lone_s1(self, current_peak_idx: int) -> Tuple[bool, str]:
        """Performs checks to determine if a peak is a valid Lone S1."""
        if not self.state['candidate_beats']: return True, "First beat"

        confidence, reason = calculate_lone_s1_confidence(
            current_peak_idx, self.state['candidate_beats'][-1], self.state['long_term_bpm'],
            self.audio_envelope, self.state['dynamic_noise_floor'], self.sample_rate, self.params
        )
        threshold = self.params.get("lone_s1_confidence_threshold", 0.6)
        if confidence < threshold:
            return False, f"Rejected Lone S1: Confidence {confidence:.2f} < Threshold {threshold:.2f}. ({reason})"

        current_peak_all_peaks_idx = np.searchsorted(self.state['all_peaks'], current_peak_idx)
        if current_peak_all_peaks_idx < len(self.state['all_peaks']) - 1:
            next_raw_peak_idx = self.state['all_peaks'][current_peak_all_peaks_idx + 1]
            forward_interval_sec = (next_raw_peak_idx - current_peak_idx) / self.sample_rate
            expected_rr_sec = 60.0 / self.state['long_term_bpm']
            min_forward_interval = expected_rr_sec * self.params.get('lone_s1_forward_check_pct', 0.45)
            # If the next peak is suspiciously close (<45% of expected RR)...
            if forward_interval_sec < min_forward_interval:
                # ...and current peak isn't MUCH stronger (1.7x), then it's probably S2, not S1
                current_amp = self.audio_envelope[current_peak_idx]
                next_amp = self.audio_envelope[next_raw_peak_idx]
                strength_ratio = current_amp / (next_amp + 1e-9)
                strength_threshold = 1.7
                if not (current_amp > (next_amp * strength_threshold)): 
                     implied_bpm = 60.0 / forward_interval_sec if forward_interval_sec > 0 else float('inf')
                     return False, (
                         f"Rejected Lone S1: Forward check failed, "
                         f"Next peak too close (interval {forward_interval_sec:.3f}s < {min_forward_interval:.3f}s, "
                         f"(45% of expected RR) AND current peak not strong enough "
                         f"(strength ratio {strength_ratio:.2f}x < threshold {strength_threshold:.1f}x). "
                         f"- <br> This suggests current peak is S2, not S1. "
                         f"If accepted, would imply {implied_bpm:.0f} BPM"
                     )
        # Get the weights for the calculation
        rhythm_weight = self.params.get('lone_s1_rhythm_weight', 0.65)
        amplitude_weight = self.params.get('lone_s1_amplitude_weight', 0.35)
        return True, f"Validated Lone S1: Confidence {confidence:.3f} >= Threshold {threshold:.2f}. ({reason}, Weights: Rhythm={rhythm_weight:.2f}, Amplitude={amplitude_weight:.2f}, Final={confidence:.3f})"



def _calculate_dynamic_noise_floor(audio_envelope: np.ndarray, sample_rate: int, params: Dict) -> Tuple[pd.Series, np.ndarray]:
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

def calculate_peak_prominence(peak_idx: int, audio_envelope: np.ndarray, trough_indices: np.ndarray) -> float:
    """
    Calculate the true prominence of a peak by finding adjacent troughs.
    Prominence = peak amplitude - higher adjacent trough amplitude (key col)
    
    Args:
        peak_idx: Index of the peak in the audio envelope
        audio_envelope: The audio envelope signal array
        trough_indices: Sorted array of trough indices from _calculate_dynamic_noise_floor()
    
    Returns:
        Prominence value (always ≥ 0)
    """
    if len(trough_indices) == 0:
        # Fallback if no troughs available
        return audio_envelope[peak_idx]
    
    # Find nearest trough on each side using binary search
    insert_pos = np.searchsorted(trough_indices, peak_idx)
    
    left_trough_idx = trough_indices[insert_pos - 1] if insert_pos > 0 else None
    right_trough_idx = trough_indices[insert_pos] if insert_pos < len(trough_indices) else None
    
    # Get amplitudes
    peak_amplitude = audio_envelope[peak_idx]
    left_trough_amp = audio_envelope[left_trough_idx] if left_trough_idx is not None else None
    right_trough_amp = audio_envelope[right_trough_idx] if right_trough_idx is not None else None
    
    # The key col is the higher (less deep) of the two adjacent troughs
    if left_trough_amp is not None and right_trough_amp is not None:
        key_col_amp = max(left_trough_amp, right_trough_amp)
    elif left_trough_amp is not None:
        key_col_amp = left_trough_amp
    elif right_trough_amp is not None:
        key_col_amp = right_trough_amp
    else:
        return peak_amplitude  # Should never reach here if troughs exist
    
    prominence = max(0.0, peak_amplitude - key_col_amp)
    
    return prominence

def adjust_confidence_with_contractility(
    base_confidence: float,
    s1_prominence: float,
    s2_prominence: float,
    bpm: float,
    params: Dict,
) -> Tuple[float, str]:
    """
    Contractility / prominence adjustment.

    Compares the measured S2/S1 prominence ratio against a BPM-based expectation:
    - If S2 is too prominent for this BPM → penalize confidence.
    - If S1 is much more prominent than expected → modestly boost confidence.
    """
    reason = ""

    # --- 1. Contractility Model: Expected S2/S1 ratio as a function of BPM ---
    expected_max_ratio = np.interp(
        bpm,
        [params["contractility_bpm_low"], params["contractility_bpm_high"]],
        [params["s2_s1_ratio_low_bpm"], params["s2_s1_ratio_high_bpm"]],
    )

    # --- 2. Reality: Measured S2/S1 prominence ratio ---
    actual_ratio = s2_prominence / (s1_prominence + 1e-9)
    reason += (
        f"\n- Prominence: S1={s1_prominence:.3f}, S2={s2_prominence:.3f}, "
        f"S2/S1={actual_ratio:.2f} (Expected max {expected_max_ratio:.2f} at {bpm:.0f} BPM)"
    )

    # --- 3. Apply contractility logic ---
    if actual_ratio > expected_max_ratio:
        # S2 is too prominent for this BPM → penalize
        violation = (actual_ratio / (expected_max_ratio + 1e-9)) - 1.0
        penalty_strength = params.get("contractility_penalty_strength", 0.4)
        penalty = violation * penalty_strength
        confidence = max(0.0, base_confidence - penalty)
        reason += (
            f"\n Contractility Penalty: -{penalty:.2f} "
            f"(S2 too prominent for BPM; prominence ratio {actual_ratio:.2f} > expected {expected_max_ratio:.2f}) -> {confidence:.2f}"
        )
    elif actual_ratio < expected_max_ratio * 0.5:
        # S1 is much more prominent than expected → mild boost
        boost = params.get("contractility_boost_amount", 0.15)
        confidence = min(1.0, base_confidence + boost)
        reason += (
            f"\n Contractility Boost: +{boost:.2f} "
            f"(S1 >> S2 at {bpm:.0f} BPM; prominence ratio {actual_ratio:.2f}) -> {confidence:.2f}"
        )
    else:
        # Within expected range → leave confidence unchanged
        confidence = base_confidence
        reason += (
            f"\n Contractility Neutral: prominence ratio {actual_ratio:.2f} within expected range "
            f"for {bpm:.0f} BPM, confidence unchanged"
        )

    return confidence, reason


def _apply_other_pairing_adjustments(
    confidence: float,
    s1_idx: int,
    s2_idx: int,
    audio_envelope: np.ndarray,
    dynamic_noise_floor: pd.Series,
    long_term_bpm: float,
    pairing_ratio: float,
    params: Dict,
    sample_rate: int,
    peak_bpm_time_sec: Optional[float],
    recovery_end_time_sec: Optional[float],
    beat_count: int,
) -> Tuple[float, str]:
    """
    Applies non-contractility adjustments:
    - Stability based on recent pairing success.
    - (Keeps the door open for future non-prominence heuristics.)

    All S1/S2 prominence-based contractility logic is handled separately.
    """
    reason = ""

    # --- Stability adjustment ---
    if beat_count >= 5:
        floor = params.get("stability_confidence_floor", 0.85)
        ceiling = params.get("stability_confidence_ceiling", 1.10)
        stability_factor = np.interp(pairing_ratio, [0.0, 1.0], [floor, ceiling])
        confidence *= stability_factor
        reason += f"\n- Stability Adjust: x{stability_factor:.2f} (Pairing Ratio: {pairing_ratio:.0%}) -> {confidence:.2f}"

    return max(0.0, min(1.0, confidence)), reason


def calculate_lone_s1_confidence(current_peak_idx: int, last_s1_idx: int, long_term_bpm: float, audio_envelope: np.ndarray,
                                 dynamic_noise_floor: pd.Series, sample_rate: int, params: Dict) -> Tuple[float, str]:
    """
    Calculates a confidence score for a Lone S1 candidate based on a weighted average of
    its rhythmic timing and its amplitude consistency with the previous beat.
    """
    # --- 1. Calculate Rhythmic Fit Score ---
    expected_rr_sec = 60.0 / long_term_bpm
    actual_rr_sec = (current_peak_idx - last_s1_idx) / sample_rate
    rhythm_deviation_pct = abs(actual_rr_sec - expected_rr_sec) / expected_rr_sec

    rhythm_score = np.interp(
        rhythm_deviation_pct,
        [0.0, 0.15, 0.30, 0.50],  # Hardcoded rhythm deviation points
        [1.0, 0.8, 0.4, 0.0]      # Hardcoded rhythm confidence curve
    )
    rhythm_reason = f"Rhythm Fit={rhythm_score:.2f} (Interval {actual_rr_sec:.3f}s vs Expected {expected_rr_sec:.3f}s)"

    # --- 2. Calculate Amplitude Fit Score ---
    last_s1_strength = max(0, audio_envelope[last_s1_idx] - dynamic_noise_floor.iloc[last_s1_idx])
    current_peak_strength = max(0, audio_envelope[current_peak_idx] - dynamic_noise_floor.iloc[current_peak_idx])
    amplitude_ratio = current_peak_strength / (last_s1_strength + 1e-9)

    amplitude_score = np.interp(
        amplitude_ratio,
        [0.0, 0.4, 0.7, 1.0],      # Hardcoded amplitude ratio points
        [0.0, 0.4, 0.8, 1.0]       # Hardcoded amplitude confidence curve
    )
    amplitude_reason = f"Amplitude Fit={amplitude_score:.2f} (Strength Ratio {amplitude_ratio:.2f}x)"

    # --- 3. Combine Scores with Weights ---
    rhythm_weight = params.get('lone_s1_rhythm_weight', 0.65)
    amplitude_weight = params.get('lone_s1_amplitude_weight', 0.35)
    final_confidence = (rhythm_score * rhythm_weight) + (amplitude_score * amplitude_weight)

    reason_str = f"{rhythm_reason}, {amplitude_reason}"
    return final_confidence, reason_str

def update_long_term_bpm(new_rr_sec: float, current_long_term_bpm: float, params: Dict) -> float:
    """Updates the long-term BPM belief based on a new R-R interval."""
    instant_bpm = 60.0 / new_rr_sec
    lr = 0.05  # Hardcoded learning rate
    max_change_per_beat = 3.0  # Hardcoded max change per beat

    # Calculate the target BPM using an exponential moving average
    target_bpm = ((1 - lr) * current_long_term_bpm) + (lr * instant_bpm)

    # Limit how much the BPM can change in a single beat (a "speed limiter")
    max_change = max_change_per_beat * new_rr_sec # Scale limit by interval duration
    proposed_change = target_bpm - current_long_term_bpm
    limited_change = np.clip(proposed_change, -max_change, max_change)

    # Apply the limited change and enforce absolute min/max BPM boundaries
    new_bpm = current_long_term_bpm + limited_change
    return max(params['min_bpm'], min(new_bpm, params['max_bpm']))

def correct_peaks_by_rhythm(peaks: np.ndarray, audio_envelope: np.ndarray, sample_rate: int, params: Dict) -> np.ndarray:
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


def _fix_rhythmic_discontinuities(s1_peaks: np.ndarray, all_raw_peaks: np.ndarray, debug_info: Dict,
                                  audio_envelope: np.ndarray, dynamic_noise_floor: pd.Series, params: Dict,
                                  sample_rate: int) -> Tuple[np.ndarray, Dict, int]:
    """
    Identifies and attempts to fix rhythmic discontinuities by re-evaluating misclassified peaks.
    """
    def log_debug(msg):
        logging.info(f"[Correction DEBUG] {msg}")

    margin = 3
    if len(s1_peaks) < margin * 2:
        log_debug(f"Skipping correction pass: Not enough S1 peaks ({len(s1_peaks)}) to apply a margin of {margin}.")
        return s1_peaks, debug_info, 0

    rr_intervals_sec = np.diff(s1_peaks) / sample_rate
    q1, q3 = np.percentile(rr_intervals_sec, [25, 75])
    iqr = q3 - q1
    stable_rr_intervals = rr_intervals_sec[
        (rr_intervals_sec > (q1 - 1.5 * iqr)) & (rr_intervals_sec < (q3 + 1.5 * iqr))]

    if len(stable_rr_intervals) < 1:
        log_debug("Not enough stable R-R intervals to determine median. Skipping correction.")
        return s1_peaks, debug_info, 0

    median_rr_sec = np.median(stable_rr_intervals)
    short_conflict_threshold_sec = median_rr_sec * params["rr_correction_threshold_pct"]
    long_conflict_threshold_sec = median_rr_sec * params.get("rr_correction_long_interval_pct", 1.7)

    log_debug(
        f"Median R-R: {median_rr_sec:.3f}s. Short Threshold: < {short_conflict_threshold_sec:.3f}s. Long Threshold: > {long_conflict_threshold_sec:.3f}s.")

    corrected_debug_info = debug_info.copy()
    peaks_to_add = set()
    corrections_made = 0

    # --- Pass 1: Look for LONG intervals (missed beats) ---
    log_debug(f"Checking for long intervals between beat {margin} and beat {len(s1_peaks) - margin}...")
    for i in range(margin, len(s1_peaks) - 1 - margin):
        s1_start_idx, s1_end_idx = s1_peaks[i], s1_peaks[i + 1]
        if (s1_end_idx - s1_start_idx) / sample_rate > long_conflict_threshold_sec:
            log_debug(f"Found LONG interval at {s1_start_idx / sample_rate:.2f}s. Investigating gap...")
            gap_candidates = [
                p for p in all_raw_peaks
                if s1_start_idx < p < s1_end_idx and _is_noise_debug(debug_info.get(p))
            ]
            for candidate_s1 in gap_candidates:
                if candidate_s1 in peaks_to_add: continue
                current_raw_idx = np.searchsorted(all_raw_peaks, candidate_s1)
                if current_raw_idx + 1 >= len(all_raw_peaks): continue
                candidate_s2 = all_raw_peaks[current_raw_idx + 1]
                if candidate_s2 >= s1_end_idx or not _is_noise_debug(debug_info.get(candidate_s2)): continue

                s1_strength = max(0, audio_envelope[candidate_s1] - dynamic_noise_floor.iloc[candidate_s1])
                is_strong_s1 = s1_strength > (
                            params["penalty_waiver_strength_ratio"] * dynamic_noise_floor.iloc[candidate_s1])
                is_ratio_plausible = (audio_envelope[candidate_s2] / (audio_envelope[candidate_s1] + 1e-9)) < params[
                    "penalty_waiver_max_s2_s1_ratio"]

                if is_strong_s1 and is_ratio_plausible:
                    log_debug(f"  - SUCCESS: Re-labeling S1/S2 pair at {candidate_s1 / sample_rate:.2f}s.")
                    corrections_made += 1
                    peaks_to_add.add(candidate_s1)

                    original_reason_s1 = corrected_debug_info.get(candidate_s1)
                    corrected_debug_info[candidate_s1] = {
                        "peak_type": PeakType.S1_CORRECTED_GAP.value,
                        "sections": [
                            {"type": "original", "original_debug": original_reason_s1},
                        ],
                    }

                    original_reason_s2 = corrected_debug_info.get(candidate_s2)
                    corrected_debug_info[candidate_s2] = {
                        "peak_type": PeakType.S2_CORRECTED_GAP.value,
                        "sections": [
                            {"type": "original", "original_debug": original_reason_s2},
                        ],
                    }
                    break

    # --- Pass 2: Look for SHORT intervals (adjacent S1s) ---
    temp_s1_list = sorted(list(set(s1_peaks) | peaks_to_add))
    peaks_to_remove = set()
    log_debug("Starting SHORT interval check...")

    # Correctly iterate and compare adjacent beats
    for i in range(margin, len(temp_s1_list) - 1 - margin):
        beat_A_idx = temp_s1_list[i]
        beat_B_idx = temp_s1_list[i + 1]

        # Skip if either beat has already been marked for removal
        if beat_A_idx in peaks_to_remove or beat_B_idx in peaks_to_remove:
            continue

        interval_sec = (beat_B_idx - beat_A_idx) / sample_rate
        if interval_sec < short_conflict_threshold_sec:
            log_debug(
                f"Found SHORT interval of {interval_sec:.3f}s between beats at {beat_A_idx / sample_rate:.2f}s and {beat_B_idx / sample_rate:.2f}s. Resolving...")

            # Decide which beat to remove based on amplitude
            amp_A = audio_envelope[beat_A_idx]
            amp_B = audio_envelope[beat_B_idx]

            if amp_B > amp_A:
                peaks_to_remove.add(beat_A_idx)
                log_debug(f"  - Removing weaker peak at {beat_A_idx / sample_rate:.2f}s.")
                corrections_made += 1
            else:
                peaks_to_remove.add(beat_B_idx)
                log_debug(f"  - Removing weaker peak at {beat_B_idx / sample_rate:.2f}s.")
                corrections_made += 1

    # Construct the final list of S1 peaks after all corrections
    final_s1_peaks = [p for p in temp_s1_list if p not in peaks_to_remove]

    return np.array(sorted(final_s1_peaks)), corrected_debug_info, corrections_made

def calculate_windowed_hrv(s1_peaks: np.ndarray, sample_rate: int, params: Dict) -> pd.DataFrame:
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

def calculate_bpm_series(peaks: np.ndarray, sample_rate: int, params: Dict) -> Tuple[pd.Series, np.ndarray]:
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

def find_major_hr_inclines(smoothed_bpm_series: pd.Series, min_duration_sec: int = 10, min_bpm_increase: int = 15) -> List[Dict]:
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

def find_major_hr_declines(smoothed_bpm_series: pd.Series, min_duration_sec: int = 10, min_bpm_decrease: int = 15) -> List[Dict]:
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

def find_peak_recovery_rate(smoothed_bpm_series: pd.Series, window_sec: int = 20) -> Optional[Dict]:
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

def find_peak_exertion_rate(smoothed_bpm_series: pd.Series, window_sec: int = 20) -> Optional[Dict]:
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

def calculate_hrr(smoothed_bpm_series: pd.Series, interval_sec: int = 60) -> Optional[Dict]:
    """Calculates the standard Heart Rate Recovery (HRR) over a fixed interval."""
    if smoothed_bpm_series.empty or len(smoothed_bpm_series) < 2: return None
    peak_bpm, peak_time = smoothed_bpm_series.max(), smoothed_bpm_series.idxmax()
    recovery_check_time = peak_time + pd.Timedelta(seconds=interval_sec)
    if recovery_check_time > smoothed_bpm_series.index.max(): return None

    recovery_bpm = np.interp(
        recovery_check_time.timestamp(),
        (smoothed_bpm_series.index.astype(np.int64) // 10**9).to_numpy(dtype=float),
        np.asarray(smoothed_bpm_series.values, dtype=float))
    return {'peak_bpm': peak_bpm, 'peak_time': peak_time, 'recovery_bpm': recovery_bpm,
            'recovery_check_time': recovery_check_time, 'hrr_value_bpm': peak_bpm - recovery_bpm,
            'interval_sec': interval_sec}

def find_recovery_phase(bpm_series: pd.Series, bpm_times_sec: np.ndarray, params: Dict) -> Tuple[Optional[float], Optional[float]]:
    """Analyzes a preliminary BPM series to find the peak heart rate and define the subsequent recovery phase window."""
    if bpm_times_sec is None or len(bpm_times_sec) < 2:
        logging.warning("Not enough preliminary beats to determine a recovery phase.")
        return None, None
    peak_time_sec = bpm_times_sec[np.argmax(bpm_series.to_numpy())]
    recovery_end_time_sec = peak_time_sec + params.get("recovery_phase_duration_sec", 120.0)
    logging.info(f"Peak BPM detected in preliminary pass at {peak_time_sec:.2f}s. High-contractility state defined until {recovery_end_time_sec:.2f}s.")
    return peak_time_sec, recovery_end_time_sec

# --- Main Analysis Pipeline (Orchestrator) ---
def _run_preliminary_pass(audio_envelope: np.ndarray, sample_rate: int, params: Dict,
                          noise_floor: pd.Series, troughs: np.ndarray,
                          start_bpm_hint: Optional[float]) -> Tuple[float, Optional[float], Optional[float]]:
    """
    Runs a high-confidence first pass to estimate global BPM and find the recovery phase.
    """
    logging.info("--- STAGE 2: Running High-Confidence pass to find anchor beats ---")
    params_pass_1 = params.copy()
    # Use a higher threshold for a more confident initial beat detection
    params_pass_1["pairing_confidence_threshold"] = 0.75

    # Use the classifier for a high-confidence dry run
    classifier = PeakClassifier(audio_envelope, sample_rate, params_pass_1, start_bpm_hint,
                                noise_floor, troughs, None, None)
    anchor_beats, _, _ = classifier.classify_peaks()

    global_bpm_estimate = None
    if len(anchor_beats) >= 10:
        median_rr_sec = np.median(np.diff(anchor_beats) / sample_rate)
        if median_rr_sec > 0:
            global_bpm_estimate = 60.0 / median_rr_sec
            logging.info(f"Automatically determined Global BPM Estimate: {global_bpm_estimate:.1f} BPM")

    # Determine the starting BPM for the main analysis
    start_bpm = start_bpm_hint or global_bpm_estimate or 80.0

    prelim_bpm_series, prelim_bpm_times = calculate_bpm_series(anchor_beats, sample_rate, params)
    peak_bpm_time_sec, recovery_end_time_sec = find_recovery_phase(prelim_bpm_series, prelim_bpm_times, params)

    return start_bpm, peak_bpm_time_sec, recovery_end_time_sec


def _refine_and_correct_peaks(s1_peaks: np.ndarray, all_raw_peaks: np.ndarray,
                              analysis_data: Dict, audio_envelope: np.ndarray,
                              sample_rate: int, params: Dict) -> Tuple[np.ndarray, Dict]:
    """
    Applies rhythmic and iterative contextual correction passes to refine S1 peaks.
    """
    logging.info("--- STAGES 4 & 5: Refining peaks with rhythmic and contextual correction ---")

    # STAGE 4: Simple rhythmic correction (e.g., remove beats that are too close)
    s1_peaks_rhythm_corrected = correct_peaks_by_rhythm(s1_peaks, audio_envelope, sample_rate, params)

    # Prepare data for the iterative pass
    dynamic_noise_floor = analysis_data['dynamic_noise_floor_series']
    current_debug_info = analysis_data["beat_debug_info"].copy()
    final_peaks = s1_peaks_rhythm_corrected

    # iterative correction loop
    max_iterations = 5  # Safeguard against infinite loops
    for i in range(max_iterations):
        logging.info(f"Correction Pass Iteration {i + 1}...")

        new_peaks, new_debug_info, corrections_made = _fix_rhythmic_discontinuities(
            s1_peaks=final_peaks,
            all_raw_peaks=all_raw_peaks,
            debug_info=current_debug_info,
            audio_envelope=audio_envelope,
            dynamic_noise_floor=dynamic_noise_floor,
            params=params,
            sample_rate=sample_rate
        )

        final_peaks = new_peaks # s1_peaks_rhythm_corrected
        current_debug_info = new_debug_info

        if corrections_made == 0:
            logging.info("Correction process stabilized. Exiting loop.")
            break
        else:
            logging.info(f"Made {corrections_made} corrections in iteration {i + 1}.")
    else:
        logging.warning("Correction process reached max iterations without stabilizing.")

    analysis_data["beat_debug_info"] = current_debug_info
    return final_peaks, analysis_data


def _calculate_final_metrics(final_peaks: np.ndarray, sample_rate: int, params: Dict) -> Dict:
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


def analyze_wav_file(wav_file_path: str, params: Dict, start_bpm_hint: Optional[float], original_file_path: str, output_directory: str, output_options: Optional[Dict] = None):
    """Main analysis pipeline that orchestrates the refactored classes."""
    start_time = time.time()
    logging.info(f"--- Processing file: {os.path.basename(original_file_path)} ---")

    # STAGE 1: Initialization
    audio_envelope, sample_rate = preprocess_audio(wav_file_path, params, output_directory, output_options)
    noise_floor, troughs = _calculate_dynamic_noise_floor(audio_envelope, sample_rate, params)

    start_bpm, peak_time, recovery_time = _run_preliminary_pass(
        audio_envelope, sample_rate, params, noise_floor, troughs, start_bpm_hint
    )

    # STAGE 3: Main Analysis, now informed by the preliminary pass
    logging.info("--- STAGE 3: Running Main Analysis Pass ---")
    classifier = PeakClassifier(
        audio_envelope, sample_rate, params, start_bpm,
        noise_floor, troughs, peak_time, recovery_time
    )
    s1_peaks, all_raw_peaks, analysis_data = classifier.classify_peaks()

    # STAGE 4 & 5: Correction and Refinement
    final_peaks, analysis_data = _refine_and_correct_peaks(
        s1_peaks, all_raw_peaks, analysis_data, audio_envelope, sample_rate, params
    )

    # STAGE 6: Final Reporting
    if len(final_peaks) < 2:
        logging.warning("Not enough S1 peaks detected to generate full report.")
        return None

    logging.info("--- STAGE 6: Calculating Metrics and Generating Outputs ---")
    final_metrics = _calculate_final_metrics(final_peaks, sample_rate, params)

    # Set default output options if none provided
    if output_options is None:
        output_options = {
            'html': True,
            'csv': True,
            'summary': True,
            'debug': True,
            'settings': True,
            'filtered_wav': True
        }

    plotly_figure = None
    
    # Generate HTML plot if requested
    if output_options.get('html', True):
        plotter = Plotter(original_file_path, params, sample_rate, output_directory)
        plotly_figure = plotter.plot_and_save(audio_envelope, all_raw_peaks, analysis_data, final_metrics, output_options)
    else:
        logging.info("Skipping HTML plot generation as requested.")

    # Generate other outputs if requested
    if output_options.get('summary', True) or output_options.get('debug', True) or output_options.get('settings', True):
        reporter = ReportGenerator(original_file_path, output_directory)
        
        if output_options.get('summary', True):
            reporter.save_analysis_summary(final_metrics)
        else:
            logging.info("Skipping summary generation as requested.")
            
        if output_options.get('debug', True):
            reporter.create_chronological_log(audio_envelope, sample_rate, all_raw_peaks, analysis_data, final_metrics)
        else:
            logging.info("Skipping debug log generation as requested.")
            
        if output_options.get('settings', True):
            reporter.save_analysis_settings(start_bpm_hint)
        else:
            logging.info("Skipping settings generation as requested.")
    else:
        logging.info("Skipping all report generation as requested.")

    duration = time.time() - start_time
    logging.info(f"--- Analysis finished in {duration:.2f} seconds. ---")
    
    return plotly_figure
