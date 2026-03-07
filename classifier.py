import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import logging
from typing import List, Dict, Tuple, Optional, Any

from confidence_engine import (
    AnalysisState,
    PairingEngine,
    LookaheadSkipper,
    calculate_bpm_intervals,
    calculate_lone_s1_confidence,
    update_long_term_bpm,
    _append_s1_s2_interval,
    _append_s1_s2_contractility,
    _get_recent_s1_prominences_for_state,
)
from peak_utils import (
    PeakType,
    _is_lone_s1_debug,
    _is_noise_debug,
    calculate_peak_prominence,
)

# INSTRUCTIONS FOR AI:
# Do not remove debugging code unless specified by the user
# Do not over-engineer a solution, keep it simple


class PeakClassifier:
    """
    Encapsulates the logic for classifying raw audio peaks into S1, S2, and Noise.
    This class manages the state of the analysis loop, including BPM belief,
    beat candidates, and debug information.
    """
    def __init__(self, audio_envelope: np.ndarray, sample_rate: int, params: Dict,
                 start_bpm_hint: Optional[float], precomputed_noise_floor: pd.Series,
                 precomputed_troughs: np.ndarray, peak_bpm_time_sec: Optional[float],
                 recovery_end_time_sec: Optional[float],
                 band_envelopes: Optional[Dict[str, np.ndarray]] = None):

        self.audio_envelope = audio_envelope
        self.sample_rate = sample_rate
        self.params = params
        self.peak_bpm_time_sec = peak_bpm_time_sec
        self.recovery_end_time_sec = recovery_end_time_sec

        # Helper components that encapsulate specific decision logic.
        self.pairing_engine = PairingEngine(
            audio_envelope, sample_rate, params, peak_bpm_time_sec, recovery_end_time_sec,
            band_envelopes=band_envelopes,
        )
        self.lookahead_skipper = LookaheadSkipper(
            audio_envelope, sample_rate, params, self.pairing_engine
        )

        self.state = self._initialize_state(
            start_bpm_hint, precomputed_noise_floor, precomputed_troughs
        )

    def _initialize_state(self, start_bpm_hint, precomputed_noise_floor, precomputed_troughs) -> AnalysisState:
        """Pre-calculates all necessary data and initializes the state for the peak finding loop."""
        analysis_data: Dict[str, Any] = {}
        dynamic_noise_floor, trough_indices = precomputed_noise_floor, precomputed_troughs
        all_peaks = self._find_raw_peaks(dynamic_noise_floor.values)

        analysis_data["dynamic_noise_floor_series"] = dynamic_noise_floor
        analysis_data["trough_indices"] = trough_indices

        noise_floor_at_peaks = dynamic_noise_floor.reindex(all_peaks, method='nearest').values
        peak_strengths = self.audio_envelope[all_peaks] - noise_floor_at_peaks
        peak_strengths[peak_strengths < 0] = 0
        normalized_deviations = np.abs(np.diff(peak_strengths)) / (
            np.maximum(peak_strengths[:-1], peak_strengths[1:]) + 1e-9
        )
        deviation_times = (all_peaks[:-1] + all_peaks[1:]) / 2 / self.sample_rate
        deviation_series = pd.Series(normalized_deviations, index=deviation_times)
        smoothing_window = max(5, int(len(deviation_series) * self.params['deviation_smoothing_factor']))
        smoothed_dev_series = deviation_series.rolling(
            window=smoothing_window, min_periods=1, center=True
        ).mean()
        analysis_data["deviation_series"] = smoothed_dev_series

        long_term_bpm = float(start_bpm_hint) if start_bpm_hint else 80.0

        return AnalysisState(
            dynamic_noise_floor=dynamic_noise_floor,
            trough_indices=trough_indices,
            all_peaks=all_peaks,
            smoothed_dev_series=smoothed_dev_series,
            long_term_bpm=long_term_bpm,
            analysis_data=analysis_data,
            sorted_troughs=sorted(trough_indices),
        )

    def classify_peaks(self) -> Tuple[np.ndarray, np.ndarray, Dict]:
        """Main classification loop to iterate through all raw peaks."""
        if len(self.state.all_peaks) < 2:
            return self.state.all_peaks, self.state.all_peaks, {"beat_debug_info": {}}

        while self.state.loop_idx < len(self.state.all_peaks):
            # Calculate pairing ratio once per iteration so all consumers
            # (kick-start recovery, pairing engine, lookahead skipper) share
            # the same view of recent rhythm stability.
            pairing_ratio = self._calculate_pairing_ratio()

            self._kickstart_check(pairing_ratio)
            current_peak_idx = self.state.all_peaks[self.state.loop_idx]
            is_last_peak = self.state.loop_idx >= len(self.state.all_peaks) - 1

            if is_last_peak:
                self._handle_last_peak(current_peak_idx)
            else:
                self._process_peak_pair(current_peak_idx, pairing_ratio)

            self._update_long_term_bpm()

        return self._finalize_results()

    def _kickstart_check(self, pairing_ratio: float) -> None:
        """
        Specialized recovery function to kick-start the algorithm if it gets stuck.
        This is a "bandaid" fix to help the algorithm recover from pairing failures. but ideally we would have a more robust solution.
        If I manage to get the algorithm good enough, this feature should never activate...
        """
        # pairing_ratio is calculated once per main-loop iteration in classify_peaks.
        if pairing_ratio >= self.params.get("kickstart_check_threshold", 0.3):
            return

        history = self.params.get("kickstart_history_beats", 4)
        if len(self.state.candidate_beats) < history:
            return

        min_s1s = self.params.get("kickstart_min_lone_s1s", 3)
        recent_lone_s1s = [
            idx for idx in self.state.candidate_beats[-history:]
            if _is_lone_s1_debug(self.state.beat_debug_info.get(idx))
        ]
        if len(recent_lone_s1s) < min_s1s:
            return

        min_matches = self.params.get("kickstart_min_noise_matches", 3)
        matches = 0
        for s1_idx in recent_lone_s1s:
            current_raw_idx = np.searchsorted(self.state.all_peaks, s1_idx)
            if current_raw_idx < len(self.state.all_peaks) - 1:
                next_raw_peak_idx = self.state.all_peaks[current_raw_idx + 1]
                if _is_noise_debug(self.state.beat_debug_info.get(next_raw_peak_idx)):
                    matches += 1

        if matches >= min_matches:
            override_ratio = self.params.get("kickstart_override_ratio", 0.6)
            logging.info(f"KICK-START: Found {matches}/{len(recent_lone_s1s)} S1->Noise patterns. Overriding pairing ratio to {override_ratio}.")
            # This is a temporary state change, so we don't store the override ratio in self.state
            self.state.pairing_ratio_override = override_ratio

    def _handle_last_peak(self, peak_idx: int):
        """Classify the final peak in the sequence."""
        self.state.candidate_beats.append(peak_idx)
        self.state.beat_debug_info[peak_idx] = {
            "peak_type": PeakType.LONE_S1_LAST.value,
            "sections": []
        }
        self.state.loop_idx += 1

    def _calculate_pairing_ratio(self) -> float:
        """Calculate recent rhythm stability ratio."""
        from peak_utils import _is_s1_paired_debug
        history_window = self.params.get("stability_history_window", 20)
        if len(self.state.candidate_beats) < history_window:
            return 0.5

        recent_beats = self.state.candidate_beats[-history_window:]
        paired_count = sum(
            1 for beat_idx in recent_beats
            if _is_s1_paired_debug(self.state.beat_debug_info.get(beat_idx))
        )
        return paired_count / history_window

    def _process_peak_pair(self, current_peak_idx: int, pairing_ratio: float) -> None:
        """Processes a pair of peaks to determine if they are S1-S2."""
        all_peaks = self.state.all_peaks
        loop_idx = self.state.loop_idx

        # We always have at least one "next" peak here (caller guards last-peak case)
        next_peak_idx = all_peaks[loop_idx + 1]

        # --- LOOKAHEAD: optionally skip a weak middle peak between a strong S1 and S2 ---
        decision = self.lookahead_skipper.maybe_skip(self.state, loop_idx, pairing_ratio)
        if decision is not None:
            s1_idx = decision["s1_idx"]
            middle_idx = decision["middle_idx"]
            s2_idx = decision["s2_idx"]
            reason = decision["reason"]
            prominence_context = decision["prominence_context"]
            lookahead_msg = decision["lookahead_msg"]
            middle_noise_msg = decision["middle_noise_msg"]

            pairing_lines = [
                line.strip().lstrip('- ')
                for line in reason.strip().split("\n")
                if line.strip()
            ]

            s1_sections = [
                {"type": "lookahead", "text": lookahead_msg},
                {"type": "pairing", "lines": pairing_lines, "success": True},
                {"type": "prominence", "details": prominence_context},
            ]
            s2_sections = [
                {"type": "lookahead", "text": lookahead_msg},
                {"type": "pairing", "lines": pairing_lines, "success": True},
                {"type": "prominence", "details": prominence_context},
            ]

            self.state.candidate_beats.append(s1_idx)
            _append_s1_s2_interval(self.state, (s2_idx - s1_idx) / self.sample_rate, self.params)
            _append_s1_s2_contractility(
                self.state, s1_idx, s2_idx, self.audio_envelope, self.state.trough_indices, self.sample_rate, self.params
            )
            self.state.beat_debug_info[s1_idx] = {
                "peak_type": PeakType.S1_PAIRED.value,
                "sections": s1_sections,
            }

            original_middle_debug = self.state.beat_debug_info.get(middle_idx)
            self.state.beat_debug_info[middle_idx] = {
                "peak_type": PeakType.NOISE.value,
                "sections": [
                    {
                        "type": "lookahead",
                        "text": middle_noise_msg,
                    },
                    {
                        "type": "original",
                        "original_debug": original_middle_debug,
                    },
                ],
            }

            self.state.beat_debug_info[s2_idx] = {
                "peak_type": PeakType.S2_PAIRED.value,
                "sections": s2_sections,
            }

            self.state.consecutive_rr_rejections = 0
            # Skip the S1, middle noise, and S2 peaks
            self.state.loop_idx += 3
            return

        # --- Standard pairing attempt ---
        is_paired, reason, prominence_context = self.pairing_engine.attempt_pair(
            self.state, current_peak_idx, next_peak_idx, pairing_ratio
        )

        if is_paired:
            self.state.candidate_beats.append(current_peak_idx)
            _append_s1_s2_interval(self.state, (next_peak_idx - current_peak_idx) / self.sample_rate, self.params)
            _append_s1_s2_contractility(
                self.state, current_peak_idx, next_peak_idx, self.audio_envelope, self.state.trough_indices, self.sample_rate, self.params
            )
            pairing_lines = [
                line.strip().lstrip('- ')
                for line in reason.strip().split("\n")
                if line.strip()
            ]
            sections = [{"type": "pairing", "lines": pairing_lines, "success": True}]
            sections.append({"type": "prominence", "details": prominence_context})
            self.state.beat_debug_info[current_peak_idx] = {
                "peak_type": PeakType.S1_PAIRED.value,
                "sections": sections,
            }
            self.state.beat_debug_info[next_peak_idx] = {
                "peak_type": PeakType.S2_PAIRED.value,
                "sections": sections,
            }
            self.state.consecutive_rr_rejections = 0
            self.state.loop_idx += 2
        else:
            self._classify_lone_peak(current_peak_idx, reason)
            self.state.loop_idx += 1

    def _update_long_term_bpm(self):
        """Updates the long-term BPM belief after each decision."""
        if len(self.state.candidate_beats) > 1:
            new_rr = (self.state.candidate_beats[-1] - self.state.candidate_beats[-2]) / self.sample_rate
            if new_rr > 0:
                self.state.long_term_bpm = update_long_term_bpm(new_rr, self.state.long_term_bpm, self.params)

        if self.state.candidate_beats:
            time_sec = self.state.candidate_beats[-1] / self.sample_rate
            self.state.long_term_bpm_history.append((time_sec, self.state.long_term_bpm))

    def _finalize_results(self) -> Tuple[np.ndarray, np.ndarray, Dict]:
        """Finalizes and returns the analysis results."""
        final_peaks = np.array(sorted(list(dict.fromkeys(self.state.candidate_beats))))
        self.state.analysis_data["beat_debug_info"] = self.state.beat_debug_info
        if self.state.long_term_bpm_history:
            lt_bpm_times, lt_bpm_values = zip(*self.state.long_term_bpm_history)
            self.state.analysis_data["long_term_bpm_series"] = pd.Series(lt_bpm_values, index=lt_bpm_times)
        return final_peaks, self.state.all_peaks, self.state.analysis_data

    def _find_raw_peaks(self, height_threshold: np.ndarray) -> np.ndarray:
        """Finds all potential peaks above the given height threshold."""
        prominence_thresh = np.quantile(self.audio_envelope, self.params['peak_prominence_quantile'])
        min_peak_dist_samples = int(self.params['min_peak_distance_sec'] * self.sample_rate)
        peaks, _ = find_peaks(self.audio_envelope, height=height_threshold, prominence=prominence_thresh, distance=min_peak_dist_samples)
        logging.info(f"Found {len(peaks)} raw peaks using dynamic height threshold.")
        return peaks

    def _classify_lone_peak(self, peak_idx: int, pairing_failure_reason: str):
        """Validates if an unpaired peak is a Lone S1 or Noise."""
        is_valid, lone_s1_lines = self._validate_lone_s1(peak_idx)
        pairing_lines = [
            line.strip().lstrip('- ')
            for line in pairing_failure_reason.strip().split("\n")
            if line.strip()
        ]

        if is_valid:
            self.state.candidate_beats.append(peak_idx)
            # For a validated S1, the "rejection_detail" is just the success reason.
            self.state.beat_debug_info[peak_idx] = {
                "peak_type": PeakType.LONE_S1_VALIDATED.value,
                "sections": [
                    {"type": "pairing", "lines": pairing_lines, "success": False},
                    {"type": "lone_s1", "lines": lone_s1_lines, "validated": True},
                ],
            }
            self.state.consecutive_rr_rejections = 0
        else:
            is_rhythm_rejection = any("Rhythm Fit" in ln for ln in lone_s1_lines)
            if is_rhythm_rejection:
                self.state.consecutive_rr_rejections += 1
            else:
                self.state.consecutive_rr_rejections = 0

            if self.state.consecutive_rr_rejections >= self.params.get("cascade_reset_trigger_count", 3):
                logging.info(
                    f"CASCADE RESET: Forcing peak at {peak_idx / self.sample_rate:.2f}s as Lone S1 due to repeated rhythmic failures.")
                self.state.candidate_beats.append(peak_idx)
                self.state.beat_debug_info[peak_idx] = {
                    "peak_type": PeakType.LONE_S1_CASCADE.value,
                    "sections": [
                        {"type": "pairing", "lines": pairing_lines, "success": False},
                        {"type": "lone_s1", "lines": lone_s1_lines, "validated": False},
                    ],
                }
                self.state.consecutive_rr_rejections = 0
            else:
                self.state.beat_debug_info[peak_idx] = {
                    "peak_type": PeakType.NOISE.value,
                    "sections": [
                        {"type": "pairing", "lines": pairing_lines, "success": False},
                        {"type": "lone_s1", "lines": lone_s1_lines, "validated": False},
                    ],
                }

    def _validate_lone_s1(self, current_peak_idx: int) -> Tuple[bool, List[str]]:
        """Performs checks to determine if a peak is a valid Lone S1."""
        detail_lines = []

        # --- 1. Basic rhythm & amplitude calculation ---
        if not self.state.candidate_beats:
            return True, ["Outcome: First beat (no prior rhythm to compare) → Validated Lone S1 → --"]

        confidence, detail_lines = calculate_lone_s1_confidence(
            current_peak_idx, self.state.candidate_beats[-1], self.state.long_term_bpm,
            self.audio_envelope, self.state.dynamic_noise_floor, self.sample_rate, self.params,
            all_peaks=self.state.all_peaks
        )

        # --- 2. Absolute prominence guardrail ---
        # Track only high-quality S1s (avoid contaminating reference with noise)
        recent_s1_types = [self.state.beat_debug_info.get(idx, {}).get("peak_type")
                        for idx in self.state.candidate_beats[-20:]]  # Last 20 beats
        recent_prominences = [
            calculate_peak_prominence(idx, self.audio_envelope, self.state.trough_indices)
            for idx, typ in zip(self.state.candidate_beats[-20:], recent_s1_types)
            if typ in (PeakType.S1_PAIRED.value, PeakType.LONE_S1_VALIDATED.value)
        ]

        if len(recent_prominences) >= 5:  # Need minimum history
            # Top 20% quartile as reference (robust to outliers)
            reference_prominence = np.percentile(recent_prominences, 80)
            current_prominence = calculate_peak_prominence(
                current_peak_idx, self.audio_envelope, self.state.trough_indices
            )

            # Penalty if <40% of reference S1 prominence (adaptive threshold)
            min_ratio = self.params.get('lone_s1_min_prominence_ratio', 0.4)
            prominence_ratio = current_prominence / (reference_prominence + 1e-9)

            if prominence_ratio < min_ratio:
                # Linear penalty: 0.5x → 0.5 penalty, 0.2x → 0.2 penalty, etc.
                penalty_factor = np.clip(prominence_ratio / min_ratio, 0.0, 1.0)
                confidence *= penalty_factor
                detail_lines.append(
                    f"Absolute Prominence: {current_prominence:.3f} < {min_ratio:.1f}× reference "
                    f"({reference_prominence:.3f}) → ×{penalty_factor:.2f} → {confidence:.2f}"
                )

        # --- 3. Forward check ---
        current_peak_all_peaks_idx = np.searchsorted(self.state.all_peaks, current_peak_idx)
        if current_peak_all_peaks_idx < len(self.state.all_peaks) - 1:
            next_raw_peak_idx = self.state.all_peaks[current_peak_all_peaks_idx + 1]
            forward_interval_sec = (next_raw_peak_idx - current_peak_idx) / self.sample_rate
            expected_rr_sec = calculate_bpm_intervals(self.state.long_term_bpm, self.params)["rr_interval"]

            if forward_interval_sec < expected_rr_sec * 0.45:  # Too close
                current_amp = self.audio_envelope[current_peak_idx]
                next_amp = self.audio_envelope[next_raw_peak_idx]

                # If not MUCH stronger, it's likely S2, not S1
                if current_amp < next_amp * 1.69: # 1.69 is a random number I tuned, a better implementation would avoid the need for this magic number
                    detail_lines.append(
                        f"Forward check: next peak too close ({forward_interval_sec:.3f}s) and not strong enough "
                        f"→ veto → 0.00"
                    )
                    confidence = 0.0  # Hard veto

        # --- 4. Final threshold check ---
        threshold = self.params.get("lone_s1_confidence_threshold", 0.6)
        if confidence < threshold:
            detail_lines.append(
                f"Outcome: score {confidence:.2f} < threshold {threshold:.2f} → Rejected Lone S1 → {confidence:.2f}"
            )
            return False, detail_lines
        detail_lines.append(
            f"Outcome: score {confidence:.2f} >= threshold {threshold:.2f} → Validated Lone S1 → {confidence:.2f}"
        )
        return True, detail_lines
