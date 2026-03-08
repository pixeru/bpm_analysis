# fft_profiles.py
# Computes aggregate FFT profiles for S1 and S2 peaks from raw and bandpass-only audio.
# Uses full sample rate to preserve all frequency information.

import logging
import os
from typing import Dict, Optional, Tuple

import numpy as np
import plotly.graph_objects as go
import librosa

from audio_preprocessing import apply_bandpass_only
from peak_utils import PeakType, _get_peak_type_from_debug


def _collect_s1_s2_indices(beat_debug_info: Dict) -> Tuple[list, list]:
    """Extract S1 and S2 peak indices (at envelope sample rate) from beat_debug_info."""
    s1_indices = []
    s2_indices = []
    for peak_idx, entry in beat_debug_info.items():
        pt = _get_peak_type_from_debug(entry) or ""
        if PeakType.is_s1(pt):
            s1_indices.append(peak_idx)
        elif PeakType.is_s2(pt):
            s2_indices.append(peak_idx)
    return s1_indices, s2_indices


def _peak_indices_to_full_rate(
    indices: list, envelope_sample_rate: int, full_sample_rate: int
) -> np.ndarray:
    """Convert peak indices from envelope (600 Hz) to full-rate sample indices."""
    if not indices:
        return np.array([], dtype=np.int64)
    times_sec = np.array(indices, dtype=float) / envelope_sample_rate
    full_indices = (times_sec * full_sample_rate).astype(np.int64)
    return full_indices


def _extract_window(
    audio: np.ndarray, center_idx: int, half_samples: int
) -> Optional[np.ndarray]:
    """Extract a window centered at center_idx. Returns None if out of bounds."""
    start = center_idx - half_samples
    end = center_idx + half_samples
    if start < 0 or end > len(audio):
        return None
    return audio[start:end].astype(np.float64)


def _compute_profiles_from_audio(
    audio: np.ndarray,
    full_sr: int,
    s1_full: np.ndarray,
    s2_full: np.ndarray,
    s1_amps: np.ndarray,
    s2_amps: np.ndarray,
    n_fft: int,
    half_samples: int,
) -> Tuple[np.ndarray, np.ndarray, int, int]:
    """
    Compute FFT profiles from a single audio array.
    Normalizes in dB: each peak's spectrum is expressed relative to the RMS energy
    of the same window (fft_db - ref_db), then averaged. Both profiles are then
    shifted to a common reference (mean of S1 and S2 aggregate amplitude) so
    S1 and S2 are on the same scale and only spectral shape differences remain.
    Returns (profile_s1_db, profile_s2_db, n_s1, n_s2).
    """
    profile_s1_sum = np.zeros(n_fft // 2 + 1, dtype=np.float64)
    profile_s2_sum = np.zeros(n_fft // 2 + 1, dtype=np.float64)
    eps = 1e-10
    rms_floor = 1e-10  # Minimum RMS for dB conversion to avoid -inf

    def _add_to_profile(
        indices: np.ndarray, amps: np.ndarray, profile_sum: np.ndarray
    ) -> Tuple[int, float]:
        """Returns (count, sum_ref_db) for aggregate amplitude normalization."""
        count = 0
        sum_ref_db = 0.0
        for i, idx in enumerate(indices):
            window = _extract_window(audio, idx, half_samples)
            if window is None:
                continue
            windowed = window * np.hanning(len(window))
            rms = np.sqrt(np.mean(windowed ** 2) + eps)
            ref_db = 20.0 * np.log10(max(rms, rms_floor))
            padded = np.zeros(n_fft, dtype=np.float64)
            padded[: len(windowed)] = windowed
            fft_mag = np.abs(np.fft.rfft(padded))
            fft_db = 20.0 * np.log10(fft_mag + eps)
            profile_sum += fft_db - ref_db
            sum_ref_db += ref_db
            count += 1
        return count, sum_ref_db

    n_s1, sum_ref_s1 = _add_to_profile(s1_full, s1_amps, profile_s1_sum)
    n_s2, sum_ref_s2 = _add_to_profile(s2_full, s2_amps, profile_s2_sum)

    if n_s1 > 0:
        profile_s1_db = profile_s1_sum / n_s1
    else:
        profile_s1_db = profile_s1_sum.copy()
    if n_s2 > 0:
        profile_s2_db = profile_s2_sum / n_s2
    else:
        profile_s2_db = profile_s2_sum.copy()

    # Normalize both profiles to a common scale using aggregate S1/S2 amplitude
    if n_s1 > 0 and n_s2 > 0:
        mean_ref_s1 = sum_ref_s1 / n_s1
        mean_ref_s2 = sum_ref_s2 / n_s2
        common_ref = (mean_ref_s1 + mean_ref_s2) / 2.0
        profile_s1_db = profile_s1_db + (mean_ref_s1 - common_ref)
        profile_s2_db = profile_s2_db + (mean_ref_s2 - common_ref)

    return profile_s1_db, profile_s2_db, n_s1, n_s2


def compute_fft_profiles(
    audio_path: str,
    beat_debug_info: Dict,
    envelope_sample_rate: int,
    audio_envelope: np.ndarray,
    params: Optional[Dict] = None,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute aggregate FFT profiles for S1 and S2 from raw and bandpass-only audio.
    Normalizes by RMS energy of each peak's window so each peak contributes equally.

    Returns:
        (freqs, raw_s1_db, raw_s2_db, bandpass_s1_db, bandpass_s2_db)
    """
    params = params or {}
    window_ms = float(params.get("fft_window_ms", 100.0))

    audio_raw, full_sr = librosa.load(audio_path, sr=None, mono=True)
    if audio_raw.size == 0:
        logging.warning("Empty audio file for FFT profiles.")
        return (
            np.array([]), np.array([]), np.array([]),
            np.array([]), np.array([]),
        )

    s1_indices, s2_indices = _collect_s1_s2_indices(beat_debug_info)
    s1_full = _peak_indices_to_full_rate(s1_indices, envelope_sample_rate, full_sr)
    s2_full = _peak_indices_to_full_rate(s2_indices, envelope_sample_rate, full_sr)

    # Envelope amplitudes at each peak (for amplitude normalization)
    env = np.asarray(audio_envelope)
    s1_amps = np.array([env[min(int(idx), len(env) - 1)] for idx in s1_indices], dtype=np.float64)
    s2_amps = np.array([env[min(int(idx), len(env) - 1)] for idx in s2_indices], dtype=np.float64)

    window_samples = int(round(window_ms * 0.001 * full_sr))
    half_samples = window_samples // 2
    n_fft = 1 << (window_samples - 1).bit_length()
    if n_fft < window_samples:
        n_fft *= 2
    freqs = np.fft.rfftfreq(n_fft, d=1.0 / full_sr)

    raw_s1_db, raw_s2_db, n_s1_raw, n_s2_raw = _compute_profiles_from_audio(
        audio_raw, full_sr, s1_full, s2_full, s1_amps, s2_amps, n_fft, half_samples
    )
    audio_preproc = apply_bandpass_only(audio_raw, full_sr, params)
    preproc_s1_db, preproc_s2_db, n_s1_pre, n_s2_pre = _compute_profiles_from_audio(
        audio_preproc, full_sr, s1_full, s2_full, s1_amps, s2_amps, n_fft, half_samples
    )

    logging.info(
        f"FFT profiles: raw ({n_s1_raw} S1, {n_s2_raw} S2), bandpass ({n_s1_pre} S1, {n_s2_pre} S2), "
        f"{full_sr} Hz, {window_ms} ms window"
    )
    return freqs, raw_s1_db, raw_s2_db, preproc_s1_db, preproc_s2_db


def save_fft_profiles_html(
    audio_path: str,
    beat_debug_info: Dict,
    envelope_sample_rate: int,
    output_path: str,
    audio_envelope: np.ndarray,
    params: Optional[Dict] = None,
) -> None:
    """
    Compute FFT profiles and save a minimal HTML plot.

    Args:
        audio_path: Path to the WAV file.
        beat_debug_info: From analysis_data["beat_debug_info"].
        envelope_sample_rate: Sample rate used for peak detection (e.g. 600 Hz).
        output_path: Path for the output HTML file.
        audio_envelope: Envelope used for peak detection; amplitudes used for normalization.
        params: Optional config dict for fft_window_ms.
    """
    params = params or {}
    s1_indices, s2_indices = _collect_s1_s2_indices(beat_debug_info)
    n_s1, n_s2 = len(s1_indices), len(s2_indices)
    if n_s1 == 0:
        logging.info("FFT profiles: no S1 labels; skipping FFT profiles HTML.")
        return
    if n_s2 <= 0.5 * n_s1:
        logging.warning(
            "FFT profiles: S2 labels (%d) are not > 50%% of S1 labels (%d); skipping (insufficient data).",
            n_s2,
            n_s1,
        )
        return

    freqs, raw_s1_db, raw_s2_db, preproc_s1_db, preproc_s2_db = compute_fft_profiles(
        audio_path, beat_debug_info, envelope_sample_rate, audio_envelope, params
    )
    if freqs.size == 0:
        logging.warning("No FFT data to plot; skipping FFT profiles HTML.")
        return

    window_ms = float(params.get("fft_window_ms", 100.0))
    trace_style = dict(width=1.5)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=freqs,
            y=raw_s1_db,
            name="S1 (raw)",
            line=trace_style,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=freqs,
            y=raw_s2_db,
            name="S2 (raw)",
            line=trace_style,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=freqs,
            y=preproc_s1_db,
            name="S1 (bandpass)",
            line=trace_style,
            visible="legendonly",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=freqs,
            y=preproc_s2_db,
            name="S2 (bandpass)",
            line=trace_style,
            visible="legendonly",
        )
    )
    # Auto-scale x-axis: show 0 Hz up to the frequency where dB drops to 50% of max dB value
    max_db = float(np.nanmax([raw_s1_db, raw_s2_db, preproc_s1_db, preproc_s2_db]))
    cutoff_db = 0.55 * max_db  # 50% of the dB value (not 50% of linear magnitude)
    combined = np.maximum(
        np.maximum(raw_s1_db, raw_s2_db),
        np.maximum(preproc_s1_db, preproc_s2_db),
    )
    above_cutoff = combined >= cutoff_db
    if np.any(above_cutoff):
        last_idx = int(np.nanmax(np.where(above_cutoff)[0]))
        x_max = float(freqs[last_idx])
        # Small margin so the cutoff point is visible
        x_max = min(freqs[-1], x_max * 1.05)
    else:
        x_max = float(freqs[-1])

    fig.update_layout(
        template="plotly_dark",
        title=f"S1 / S2 FFT Profiles ({window_ms:.0f} ms window)",
        xaxis_title="Frequency (Hz)",
        yaxis_title="Magnitude (dB)",
        margin=dict(t=60, b=60, l=70, r=20),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        dragmode="pan",
        uirevision="layout-stable",
        autosize=True,
    )
    fig.update_xaxes(range=[0, x_max], automargin=False)
    fig.update_yaxes(automargin=False)

    plot_config = {"scrollZoom": True, "showTips": False}
    plotly_html = fig.to_html(full_html=False, config=plot_config, include_plotlyjs="cdn")

    audio_file_name = os.path.basename(audio_path)
    page_title = f"S1 / S2 FFT Profiles - {audio_file_name}"
    wrapper_html = f"""<!DOCTYPE html>
<html style="height:100%;margin:0;padding:0;">
<head>
    <meta charset="utf-8" />
    <title>{page_title}</title>
    <style>
        html, body {{ height: 100%; margin: 0; padding: 0; background-color: #111; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #e0e0e0; }}
        body {{ display: flex; flex-direction: column; }}
        #fft-header {{ display: flex; align-items: center; gap: 8px; padding: 4px 8px; background: rgba(40, 40, 50, 0.6); border-bottom: 1px solid #333; font-size: 12px; flex-shrink: 0; }}
        #fft-header .chart-toolbar-title {{ color: #aaa; white-space: nowrap; }}
        #fft-header #audio-file-name {{ font-size: 12px; color: #ccc; white-space: nowrap; }}
        #fft-plot-container {{ flex: 1 1 0; min-height: 0; display: flex; flex-direction: column; }}
        #fft-plot-container > div {{ flex: 1 1 0 !important; min-height: 0 !important; height: 100% !important; }}
    </style>
</head>
<body>
    <div id="fft-header">
        <span class="chart-toolbar-title">S1 / S2 FFT Profiles – </span>
        <span id="audio-file-name" title="{audio_file_name}">{audio_file_name}</span>
    </div>
    <div id="fft-plot-container">
        {plotly_html}
    </div>
</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(wrapper_html)
    logging.info(f"FFT profiles saved to {output_path}")
