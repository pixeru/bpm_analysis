import os
import logging
from time_utils import seconds_to_datetime
import csv
import shutil
import json
from typing import Dict, Optional, List, Any, Callable

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import librosa
import librosa.display
import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend for spectrogram generation
import matplotlib.pyplot as plt


class Plotter:
    """Handles the creation and generation of the final analysis plot."""

    def __init__(
        self,
        file_name: str,
        params: Dict,
        sample_rate: int,
        output_directory: str,
        source_audio_path: Optional[str] = None,
        peak_type_helper: Optional[Callable[[Any], str]] = None,
        format_debug_entry_func: Optional[Callable[[Dict], List[str]]] = None,
        peak_type_cls: Optional[Any] = None,
    ):
        self.file_name = file_name
        self.params = params
        self.sample_rate = sample_rate
        self.output_directory = output_directory
        self.audio_source_path = source_audio_path or file_name
        self.fig = make_subplots(specs=[[{"secondary_y": True}]])
        self.audio_duration_sec = None  # Will be set during plot_and_save
        # Optional spectrogram image filenames (saved in output dir); filtered generated on demand.
        self.spectrogram_original_filename: Optional[str] = None
        self.bpm_axis_center: float = float(params.get("default_bpm_axis_center", 125))
        self.bpm_axis_span: float = float(params.get("bpm_axis_span", 150))

        # Debug formatting helpers are injected from the analysis module to avoid
        # importing bpm_analysis here (which would create a circular dependency).
        # If they are not provided, we fall back to no-op implementations.
        self._get_peak_type_from_debug: Callable[[Any], str] = peak_type_helper or (lambda entry: "")
        self._format_debug_entry: Callable[[Dict], List[str]] = format_debug_entry_func or (lambda entry: [])
        self._PeakType = peak_type_cls

    def _generate_spectrogram_image(self, audio_path: str, output_path: str) -> Optional[str]:
        """
        Generate a spectrogram image from the audio file and save as PNG to output_path.
        Returns the basename of the saved file (for use in HTML/config), or None on failure.
        """
        try:
            # Load audio at a reasonable sample rate for spectrogram
            audio_data, sr = librosa.load(audio_path, sr=22050, mono=True)

            if audio_data is None or len(audio_data) == 0:
                logging.warning("Could not load audio for spectrogram generation")
                return None

            # Compute mel spectrogram for better visual representation
            n_fft = 2048
            hop_length = 128
            n_mels = 256  # Slightly smaller for reasonable file size

            # Generate mel spectrogram
            S = librosa.feature.melspectrogram(
                y=audio_data, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels
            )

            # Convert to dB scale
            S_dB = librosa.power_to_db(S, ref=np.max)

            # Calculate figure dimensions based on audio duration; cap width to limit file size
            duration = len(audio_data) / sr
            fig_width = min(max(20, duration / 10), 80)
            fig_height = 6

            # Create figure with transparent background
            fig, ax = plt.subplots(figsize=(fig_width, fig_height))
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)

            # Display spectrogram with a colormap that works well as background
            librosa.display.specshow(
                S_dB,
                sr=sr,
                hop_length=hop_length,
                x_axis="time",
                y_axis="mel",
                ax=ax,
                cmap="magma",
            )

            # Remove axes, labels, and all decorations for clean overlay
            ax.axis("off")
            ax.set_xlabel("")
            ax.set_ylabel("")
            ax.set_title("")

            # Remove all margins
            plt.tight_layout(pad=0)
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

            # Save to file as PNG with transparency (dpi 72 for smaller file size)
            fig.savefig(
                output_path,
                format="png",
                transparent=True,
                dpi=72,
                bbox_inches="tight",
                pad_inches=0,
            )
            plt.close(fig)

            basename = os.path.basename(output_path)
            logging.info("Generated spectrogram image for background overlay: %s", basename)
            return basename

        except Exception as e:
            logging.warning(f"Failed to generate spectrogram image: {e}")
            return None

    def plot_and_save(
        self,
        audio_envelope: np.ndarray,
        all_raw_peaks: np.ndarray,
        analysis_data: Dict,
        final_metrics: Dict,
        output_options: Optional[Dict] = None,
    ):
        """Generates and saves the main analysis plot by calling helper methods."""
        self.time_axis_sec = np.arange(len(audio_envelope)) / self.sample_rate
        self.audio_duration_sec = self.time_axis_sec[-1] if len(self.time_axis_sec) > 0 else 0
        
        # Long-plot optimization: optionally skip heavy debug traces for very long recordings.
        optimize_long_plots = bool(self.params.get("optimize_long_plots", False))
        long_threshold_sec = float(self.params.get("long_plot_duration_threshold_sec", 600.0))
        # Only skip details if the recording is longer than the threshold; shorter files always show full detail.
        self.skip_detailed_debug_traces = optimize_long_plots and self.audio_duration_sec > long_threshold_sec

        time_axis_dt = pd.to_datetime([seconds_to_datetime(t) for t in self.time_axis_sec])

        self._add_line_traces(time_axis_dt, audio_envelope, analysis_data, all_raw_peaks)
        self._add_trough_markers(audio_envelope, analysis_data)
        self._add_peak_traces(
            all_raw_peaks,
            analysis_data.get("beat_debug_info", {}),
            audio_envelope,
            analysis_data.get("trough_indices"),
        )
        self._add_bpm_hrv_traces(
            final_metrics.get("smoothed_bpm"), analysis_data, final_metrics.get("windowed_hrv_df")
        )
        self._add_slope_traces(
            final_metrics.get("major_inclines"),
            final_metrics.get("major_declines"),
            final_metrics.get("peak_recovery_stats"),
            final_metrics.get("peak_exertion_stats"),
        )
        self._add_trapezoid_shapes(final_metrics.get("trapezoids"))
        self._add_annotations_and_summary(
            final_metrics.get("smoothed_bpm"),
            final_metrics.get("hrv_summary"),
            final_metrics.get("hrr_stats"),
            final_metrics.get("peak_recovery_stats"),
        )
        self._prepare_bpm_axis_center(final_metrics)

        self._configure_layout()

        base_name = os.path.basename(os.path.splitext(self.file_name)[0])
        output_html_path = os.path.join(self.output_directory, f"{base_name}_bpm_plot.html")
        output_png_path = os.path.join(self.output_directory, f"{base_name}_bpm_plot.png")
        plot_title = f"Heartbeat Analysis - {os.path.basename(self.file_name)}"
        plot_config = {
            "scrollZoom": True,
            "toImageButtonOptions": {"filename": plot_title, "format": "png", "scale": 2},
            "showTips": False,
        }

        html_requested = True if output_options is None else output_options.get("html", True)
        png_requested = False if output_options is None else output_options.get("png", False)

        if html_requested:
            # Determine whether spectrogram generation is enabled (can be disabled via GUI/output options).
            self.spectrogram_enabled = True
            if output_options is not None:
                self.spectrogram_enabled = output_options.get("spectrogram", True)

            # Generate spectrogram image for optional background overlay (original audio only).
            # Filtered spectrograms are generated later in _generate_custom_html if needed.
            if self.spectrogram_enabled:
                try:
                    spec_path = os.path.join(self.output_directory, f"{base_name}_spectrogram.png")
                    self.spectrogram_original_filename = self._generate_spectrogram_image(
                        self.audio_source_path or self.file_name, spec_path
                    )
                except Exception as e:
                    logging.warning(f"Failed to generate original spectrogram: {e}")
            else:
                logging.info("Skipping original spectrogram generation as requested (spectrogram output disabled).")

            # Generate the base Plotly HTML
            plotly_html = self.fig.to_html(config=plot_config, full_html=False, include_plotlyjs='cdn')

            # Generate custom HTML with audio player and playhead
            custom_html = self._generate_custom_html(plotly_html, plot_title, base_name)

            with open(output_html_path, 'w', encoding='utf-8') as f:
                f.write(custom_html)
            logging.info(f"Interactive plot with audio player saved to {output_html_path}")
        else:
            logging.info("Skipping HTML plot generation as requested.")

        if png_requested:
            # Use a large default canvas so the graph itself is comfortably sized in the PNG.
            opts = output_options or {}
            png_scale = int(opts.get("png_scale", 2) or 2)
            png_width = int(opts.get("png_width") or 2100)
            png_height = int(opts.get("png_height") or 1200)

            try:
                # Note: Kaleido must be installed for write_image() to work.
                write_kwargs = {
                    "format": "png",
                    "scale": png_scale,
                    "width": png_width,
                    "height": png_height,
                }
                self.fig.write_image(output_png_path, **write_kwargs)
                logging.info(f"Plot PNG exported to {output_png_path}")
            except Exception as e:
                logging.warning(f"Failed to export Plot PNG (requires kaleido): {e}")

        if output_options is None or output_options.get("csv", True):
            smoothed_bpm = final_metrics.get("smoothed_bpm")
            bpm_times = final_metrics.get("bpm_times")
            if smoothed_bpm is not None and not smoothed_bpm.empty and bpm_times is not None:
                csv_path = os.path.join(self.output_directory, f"{base_name}_bpm_plot.csv")
                try:
                    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["Time (s)", "Average BPM"])
                        for t, bpm in zip(bpm_times, smoothed_bpm.values):
                            if not np.isnan(bpm):
                                writer.writerow([f"{t:.3f}", f"{bpm:.3f}"])
                    logging.info(f"BPM plot data saved to {csv_path}")
                except Exception as e:
                    logging.error(f"Failed to write BPM plot CSV: {e}")
        else:
            logging.info("Skipping CSV generation as requested.")

        return self.fig

    def _prepare_bpm_axis_center(self, final_metrics: Dict):
        """Use detected BPM stats to keep the BPM axis centered without altering the per-file zoom."""
        hrv_summary = final_metrics.get("hrv_summary") or {}
        avg_bpm = hrv_summary.get("avg_bpm")
        smoothed_bpm = final_metrics.get("smoothed_bpm")
        if avg_bpm is None and smoothed_bpm is not None and not smoothed_bpm.empty:
            avg_bpm = float(smoothed_bpm.mean())
        if avg_bpm is None:
            avg_bpm = float(self.params.get("default_bpm_axis_center", self.bpm_axis_center))
        self.bpm_axis_center = float(avg_bpm)

    def _configure_layout(self):
        """Sets up the plot layout, titles, and axes with custom x-axis tick labels."""
        self.fig.update_layout(
            template="plotly_dark",
            dragmode="pan",
            legend=dict(orientation="h", yanchor="bottom", y=1.06, xanchor="right", x=1),
            margin=dict(t=80, b=100, l=100, r=10),
            hovermode="x unified",
            autosize=True,
            uirevision="layout-stable",
        )

        duration_sec = float(self.time_axis_sec[-1])
        tick_interval_sec = 30
        tick_positions_sec = np.arange(0, duration_sec + 1e-6, tick_interval_sec, dtype=float)
        if tick_positions_sec.size > 0 and tick_positions_sec[-1] < duration_sec:
            tick_positions_sec = np.append(tick_positions_sec, duration_sec)
        tickvals = [seconds_to_datetime(float(s)) for s in tick_positions_sec]
        ticktext = [f"{int(s // 60):02d}:{int(s % 60):02d} ({s:.2f})" for s in tick_positions_sec]

        self.fig.update_xaxes(
            title_text="Time",
            tickvals=tickvals,
            ticktext=ticktext,
            hoverformat="%M:%S.%L",
            automargin=False,
        )

        # Use the audio envelope trace, if present, to scale the amplitude axis.
        robust_upper_limit = 1
        if self.fig.data:
            envelope_values = None
            for trace in self.fig.data:
                if getattr(trace, "name", "") == "Audio Envelope" and hasattr(trace, "y"):
                    try:
                        envelope_values = np.asarray(trace.y, dtype=float)
                    except Exception:
                        envelope_values = None
                    break
            if envelope_values is not None and envelope_values.size > 0:
                robust_upper_limit = float(np.quantile(envelope_values, 0.95))

        amplitude_scale = self.params.get("plot_amplitude_scale_factor", 60.0)
        self.fig.update_yaxes(
            title_text="Signal Amplitude",
            secondary_y=False,
            range=[0, robust_upper_limit * amplitude_scale],
            showgrid=False,
            automargin=False,
        )
        half_span = self.bpm_axis_span / 2.0
        min_bpm = max(self.bpm_axis_center - half_span, 5)
        max_bpm = self.bpm_axis_center + half_span
        self.fig.update_yaxes(
            title_text="BPM / HRV",
            secondary_y=True,
            range=[min_bpm, max_bpm],
            autorange=False,
            automargin=False,
        )

    def _add_line_traces(
        self,
        time_axis_dt: pd.Series,
        audio_envelope: np.ndarray,
        analysis_data: Dict,
        all_raw_peaks: Optional[np.ndarray] = None,
    ):
        """Adds audio envelope and noise floor traces. Downsampling (plot_downsample_factor) applies only here
        to these large arrays; contractility, BPM, HRV and markers are never downsampled.
        Note: Do not use dashed lines (dash=...) for line traces—they cause noticeable lag in the plot."""
        if getattr(self, "skip_detailed_debug_traces", False):
            logging.info("Skipping audio envelope and noise floor traces for long file (optimization enabled).")
            return
        plot_time_axis_dt = time_axis_dt
        plot_envelope = audio_envelope
        plot_noise_floor = analysis_data.get("dynamic_noise_floor_series")

        # Downsample only envelope and noise floor for performance; other traces (contractility, BPM, HRV) use full data
        factor = self.params.get("plot_downsample_factor", 5)
        if factor > 1 and len(audio_envelope) >= factor:
            logging.info(f"Downsampling envelope and noise floor by factor {factor} for plotting.")
            plot_time_axis_dt = time_axis_dt[::factor]
            plot_envelope = audio_envelope[::factor]
            if plot_noise_floor is not None and not plot_noise_floor.empty:
                plot_noise_floor = plot_noise_floor.iloc[::factor]

        self.fig.add_trace(
            go.Scatter(x=plot_time_axis_dt, y=plot_envelope, name="Audio Envelope", line=dict(color="#47a5c4")),
            secondary_y=False,
        )
        if (
            plot_noise_floor is not None
            and not plot_noise_floor.empty
            and len(plot_noise_floor) >= len(plot_time_axis_dt)
        ):
            self.fig.add_trace(
                go.Scatter(
                    x=plot_time_axis_dt,
                    y=plot_noise_floor.values,
                    name="Dynamic Noise Floor",
                    line=dict(color="green", width=1.5),
                    hovertemplate="Noise Floor: %{y:.4f}<extra></extra>",
                    visible="legendonly",
                ),
                secondary_y=False,
            )

        # S1/S2 band energy (continuous) and proportion at peaks (what the algorithm uses).
        s1_band = analysis_data.get("s1_band")
        s2_band = analysis_data.get("s2_band")
        s1_low = self.params.get("s1_band_low_hz", 20)
        s1_high = self.params.get("s1_band_high_hz", 60)
        s2_low = self.params.get("s2_band_low_hz", 60)
        s2_high = self.params.get("s2_band_high_hz", 200)
        if (
            s1_band is not None
            and s2_band is not None
            and len(s1_band) == len(audio_envelope)
            and len(s2_band) == len(audio_envelope)
        ):
            # Continuous band energy traces (raw envelope in each band; may appear temporally smeared).
            plot_s1_band = s1_band[::factor] if factor > 1 and len(s1_band) >= factor else s1_band
            plot_s2_band = s2_band[::factor] if factor > 1 and len(s2_band) >= factor else s2_band
            self.fig.add_trace(
                go.Scatter(
                    x=plot_time_axis_dt,
                    y=plot_s1_band,
                    name=f"S1 band energy ({s1_low:.0f}-{s1_high:.0f} Hz)",
                    line=dict(color="darkorange", width=1.2),
                    hovertemplate="S1 band: %{y:.4f}<extra></extra>",
                    visible="legendonly",
                ),
                secondary_y=False,
            )
            self.fig.add_trace(
                go.Scatter(
                    x=plot_time_axis_dt,
                    y=plot_s2_band,
                    name=f"S2 band energy ({s2_low:.0f}-{s2_high:.0f} Hz)",
                    line=dict(color="purple", width=1.2),
                    hovertemplate="S2 band: %{y:.4f}<extra></extra>",
                    visible="legendonly",
                ),
                secondary_y=False,
            )
        if (
            s1_band is not None
            and s2_band is not None
            and len(s1_band) == len(audio_envelope)
            and len(s2_band) == len(audio_envelope)
            and all_raw_peaks is not None
            and len(all_raw_peaks) > 0
        ):
            eps = 1e-9
            total = s1_band + s2_band + eps
            s1_proportion = s1_band / total
            s2_proportion = s2_band / total
            scale = float(np.max(plot_envelope)) if len(plot_envelope) > 0 else 1.0
            if scale < 1e-9:
                scale = 1.0
            # Sample at peak indices only (same as pairing logic)
            peak_indices = np.asarray(all_raw_peaks)
            in_bounds = (peak_indices >= 0) & (peak_indices < len(s1_proportion))
            peak_indices = peak_indices[in_bounds]
            if len(peak_indices) > 0:
                s1_at_peaks = s1_proportion[peak_indices] * scale
                s2_at_peaks = s2_proportion[peak_indices] * scale
                peak_times_sec = peak_indices.astype(float) / self.sample_rate
                peak_times_dt = pd.to_datetime([seconds_to_datetime(float(t)) for t in peak_times_sec])
                self.fig.add_trace(
                    go.Scatter(
                        x=peak_times_dt,
                        y=s1_at_peaks,
                        mode="markers",
                        name=f"S1 proportion at peaks ({s1_low:.0f}-{s1_high:.0f} Hz)",
                        marker=dict(color="darkorange", size=6, symbol="triangle-up"),
                        hovertemplate="S1 proportion: %{customdata:.3f}<extra></extra>",
                        customdata=s1_proportion[peak_indices],
                        visible="legendonly",
                    ),
                    secondary_y=False,
                )
                self.fig.add_trace(
                    go.Scatter(
                        x=peak_times_dt,
                        y=s2_at_peaks,
                        mode="markers",
                        name=f"S2 proportion at peaks ({s2_low:.0f}-{s2_high:.0f} Hz)",
                        marker=dict(color="purple", size=6, symbol="triangle-down"),
                        hovertemplate="S2 proportion: %{customdata:.3f}<extra></extra>",
                        customdata=s2_proportion[peak_indices],
                        visible="legendonly",
                    ),
                    secondary_y=False,
                )

    def _add_trough_markers(self, audio_envelope: np.ndarray, analysis_data: Dict):
        """Adds trough markers to the plot using original full-resolution data for accuracy."""
        if getattr(self, "skip_detailed_debug_traces", False):
            logging.info("Skipping trough markers for long file (optimization enabled).")
            return
        trough_indices = analysis_data.get("trough_indices")
        if trough_indices is not None and trough_indices.size > 0:
            trough_times_dt = pd.to_datetime(
                [seconds_to_datetime(float(t)) for t in (trough_indices / self.sample_rate)]
            )

            self.fig.add_trace(
                go.Scatter(
                    x=trough_times_dt,
                    y=audio_envelope[trough_indices],
                    mode="markers",
                    name="Troughs",
                    marker=dict(color="green", symbol="circle-open", size=6),
                    visible="legendonly",
                ),
                secondary_y=False,
            )

    def _add_peak_marker_trace(
        self, indices, customdata, name, color, symbol, size, audio_envelope, hovertemplate
    ):
        """Add a single Scatter trace for peak markers (S1, S2, or Noise)."""
        times_dt = pd.to_datetime(
            [seconds_to_datetime(float(t)) for t in (np.array(indices) / self.sample_rate)]
        )
        self.fig.add_trace(
            go.Scatter(
                x=times_dt,
                y=audio_envelope[indices],
                mode="markers",
                name=name,
                marker=dict(color=color, symbol=symbol, size=size),
                customdata=customdata,
                hovertemplate=hovertemplate,
            ),
            secondary_y=False,
        )

    def _add_peak_traces(self, all_raw_peaks, debug_info, audio_envelope, trough_indices=None):
        """Adds S1, S2, and Noise peak markers to the plot with detailed hover info."""
        if getattr(self, "skip_detailed_debug_traces", False):
            logging.info("Skipping S1/S2/Noise peak markers for long file (optimization enabled).")
            return
        s1_peaks = {"indices": [], "customdata": []}
        s2_peaks = {"indices": [], "customdata": []}
        noise_peaks = {"indices": [], "customdata": []}

        classified_indices = set()

        for peak_idx, debug_value in debug_info.items():
            hover_text_parts = []

            peak_type = self._get_peak_type_from_debug(debug_value) or "Unknown Peak"
            hover_text_parts.append(f"<b>Type:</b> {peak_type}")
            hover_text_parts.append(f"<b>Time:</b> {peak_idx / self.sample_rate:.2f}s")
            hover_text_parts.append(f"<b>Amp:</b> {audio_envelope[peak_idx]:.0f}")
            hover_text_parts.append("---")

            formatted_lines = self._format_debug_entry(debug_value)
            if formatted_lines:
                sub_text = "<br>".join(l.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;") for l in formatted_lines)
                hover_text_parts.append(sub_text)

            full_hover_text = "<br>".join(hover_text_parts)
            classified_indices.add(peak_idx)

            if self._PeakType is not None and self._PeakType.is_s1(peak_type):
                s1_peaks["indices"].append(peak_idx)
                s1_peaks["customdata"].append(full_hover_text)
            elif self._PeakType is not None and self._PeakType.is_s2(peak_type):
                s2_peaks["indices"].append(peak_idx)
                s2_peaks["customdata"].append(full_hover_text)
            else:
                noise_peaks["indices"].append(peak_idx)
                noise_peaks["customdata"].append(full_hover_text)

        for peak_idx in all_raw_peaks:
            if peak_idx not in classified_indices:
                hover_text = (
                    f"<b>Type:</b> Unclassified<br>"
                    f"<b>Time:</b> {peak_idx / self.sample_rate:.2f}s<br>"
                    f"<b>Amp:</b> {audio_envelope[peak_idx]:.0f}<br>"
                    "<b>Details:</b> Peak was not evaluated by the classifier."
                )
                noise_peaks["indices"].append(peak_idx)
                noise_peaks["customdata"].append(hover_text)

        hovertemplate = "%{customdata}<extra></extra>"
        for name, peaks, color, symbol, size in (
            ("S1 Beats", s1_peaks, "#e36f6f", "circle", 8),
            ("S2 Beats", s2_peaks, "orange", "circle", 6),
            ("Noise/Rejected", noise_peaks, "grey", "x", 6),
        ):
            if peaks["indices"]:
                self._add_peak_marker_trace(
                    peaks["indices"], peaks["customdata"], name, color, symbol, size,
                    audio_envelope, hovertemplate,
                )

        # Average S1 / S2 contractility traces (prominence-based, averaged over time segments), Analysis Data only
        self._add_s1_s2_amplitude_traces(
            s1_peaks["indices"], s2_peaks["indices"], audio_envelope, trough_indices
        )

    def _average_prominence_by_time_segment(
        self, times_sec: np.ndarray, proms: np.ndarray, segment_sec: float
    ) -> tuple:
        """Bin prominence by fixed-duration time segments; return (segment_center_times, mean_prominence)."""
        times_sec = np.asarray(times_sec, dtype=float)
        proms = np.asarray(proms, dtype=float)
        if len(times_sec) == 0 or len(proms) == 0 or len(times_sec) != len(proms):
            return np.array([]), np.array([])
        t_min, t_max = float(np.min(times_sec)), float(np.max(times_sec))
        t0 = np.floor(t_min / segment_sec) * segment_sec
        segment_centers = []
        segment_means = []
        while t0 <= t_max:
            mask = (times_sec >= t0) & (times_sec < t0 + segment_sec)
            if np.any(mask):
                segment_centers.append(t0 + segment_sec / 2.0)
                segment_means.append(float(np.mean(proms[mask])))
            t0 += segment_sec
        return np.array(segment_centers), np.array(segment_means)

    def _smooth_peak_amplitudes(self, amps: np.ndarray, window_size: int = 3) -> np.ndarray:
        """Moving average over window_size points (current and adjacent). Boundaries use fewer points."""
        n = len(amps)
        if n == 0:
            return amps
        half = max(0, (window_size - 1) // 2)
        smoothed = np.empty(n, dtype=float)
        for i in range(n):
            lo, hi = max(0, i - half), min(n, i + half + 1)
            smoothed[i] = float(np.mean(amps[lo:hi]))
        return smoothed

    def _add_prominence_line_trace(
        self, times_sec, proms, name, color, visible, window_size=1
    ):
        """Add one prominence-based contractility line trace. Use window_size=1 for pre-averaged (e.g. time-segment) data."""
        proms = np.asarray(proms, dtype=float)
        smoothed = self._smooth_peak_amplitudes(proms, window_size=window_size)
        times_dt = pd.to_datetime([seconds_to_datetime(float(t)) for t in times_sec])
        self.fig.add_trace(
            go.Scatter(
                x=times_dt,
                y=smoothed,
                mode="lines",
                name=name,
                line=dict(color=color, width=2),
                visible=visible,
            ),
            secondary_y=False,
        )

    def _add_s1_s2_amplitude_traces(self, s1_indices, s2_indices, audio_envelope, trough_indices=None):
        """Add line traces for Average S1, S2, and combined contractility (prominence-based, averaged over time segments).
        Uses a fixed-duration segment (default 2 s) so trends reflect: long-term contractility vs BPM; short-term S1 vs inhale/exhale."""
        from bpm_analysis import get_peak_prominence_details

        segment_sec = float(self.params.get("contractility_average_window_sec", 2.0))
        troughs = np.array(trough_indices) if trough_indices is not None and len(trough_indices) > 0 else np.array([], dtype=np.intp)

        def prominence_at(peak_idx):
            details = get_peak_prominence_details(peak_idx, audio_envelope, troughs)
            return details["prominence"]

        if s1_indices:
            s1_idx = np.array(s1_indices)
            times_sec = s1_idx.astype(float) / self.sample_rate
            proms = np.array([prominence_at(int(i)) for i in s1_idx])
            t_centers, mean_proms = self._average_prominence_by_time_segment(times_sec, proms, segment_sec)
            if len(t_centers) > 0:
                self._add_prominence_line_trace(
                    t_centers, mean_proms, "Average S1 contractility", "#e36f6f", "legendonly", window_size=1
                )
        if s2_indices:
            s2_idx = np.array(s2_indices)
            times_sec = s2_idx.astype(float) / self.sample_rate
            proms = np.array([prominence_at(int(i)) for i in s2_idx])
            t_centers, mean_proms = self._average_prominence_by_time_segment(times_sec, proms, segment_sec)
            if len(t_centers) > 0:
                self._add_prominence_line_trace(
                    t_centers, mean_proms, "Average S2 contractility", "orange", "legendonly", window_size=1
                )
        if s1_indices or s2_indices:
            times_sec = []
            proms = []
            for indices in (s1_indices or [], s2_indices or []):
                if not indices:
                    continue
                idx = np.array(indices)
                times_sec.extend((idx.astype(float) / self.sample_rate).tolist())
                proms.extend([prominence_at(int(i)) for i in idx])
            times_sec = np.array(times_sec)
            proms = np.array(proms)
            t_centers, mean_proms = self._average_prominence_by_time_segment(times_sec, proms, segment_sec)
            if len(t_centers) > 0:
                self._add_prominence_line_trace(
                    t_centers, mean_proms, "Average contractility", "#aaa", "legendonly", window_size=1
                )

    def _add_bpm_hrv_traces(self, smoothed_bpm, analysis_data, windowed_hrv_df):
        """Adds BPM, BPM trend, and HRV traces."""
        if smoothed_bpm is not None and not smoothed_bpm.empty:
            self.fig.add_trace(
                go.Scatter(
                    x=smoothed_bpm.index, y=smoothed_bpm.values, name="Average BPM", line=dict(color="#4a4a4a", width=3)
                ),
                secondary_y=True,
            )

        if "long_term_bpm_series" in analysis_data and not analysis_data["long_term_bpm_series"].empty:
            lt_series = analysis_data["long_term_bpm_series"]
            lt_times_dt = pd.to_datetime([seconds_to_datetime(float(t)) for t in lt_series.index])
            self.fig.add_trace(
                go.Scatter(
                    x=lt_times_dt,
                    y=lt_series.values,
                    name="BPM Trend (Belief)",
                    line=dict(color="orange", width=2),
                    visible="legendonly",
                ),
                secondary_y=True,
            )
        if (
            windowed_hrv_df is not None
            and not windowed_hrv_df.empty
            and "time" in windowed_hrv_df
            and "rmssdc" in windowed_hrv_df
            and "sdnn" in windowed_hrv_df
        ):
            hrv_times_dt = pd.to_datetime(
                [seconds_to_datetime(float(t)) for t in windowed_hrv_df["time"]]
            )
            self.fig.add_trace(
                go.Scatter(
                    x=hrv_times_dt, y=windowed_hrv_df["rmssdc"], name="RMSSDc", line=dict(color="cyan", width=2), visible="legendonly"
                ),
                secondary_y=True,
            )
            self.fig.add_trace(
                go.Scatter(
                    x=hrv_times_dt, y=windowed_hrv_df["sdnn"], name="SDNN", line=dict(color="magenta", width=2), visible="legendonly"
                ),
                secondary_y=True,
            )
            if "lf_hf_ratio" in windowed_hrv_df.columns:
                self.fig.add_trace(
                    go.Scatter(
                        x=hrv_times_dt,
                        y=windowed_hrv_df["lf_hf_ratio"],
                        name="LF/HF (windowed)",
                        line=dict(color="yellow", width=2),
                        visible="legendonly",
                    ),
                    secondary_y=True,
                )

    def _add_annotations_and_summary(self, smoothed_bpm, hrv_summary, hrr_stats, peak_recovery_stats):
        """Adds min/max BPM annotations on the plot and builds plain-text summary for the HTML Analysis Summary modal."""
        if smoothed_bpm is not None and not smoothed_bpm.empty:
            max_bpm_val = smoothed_bpm.max()
            min_bpm_val = smoothed_bpm.min()
            max_bpm_time = smoothed_bpm.idxmax()
            min_bpm_time = smoothed_bpm.idxmin()

            self.fig.add_annotation(
                x=max_bpm_time,
                y=max_bpm_val,
                text=f"Max: {max_bpm_val:.1f} BPM",
                showarrow=True,
                arrowhead=1,
                ax=20,
                ay=-40,
                font=dict(color="#e36f6f"),
                yref="y2",
            )

            self.fig.add_annotation(
                x=min_bpm_time,
                y=min_bpm_val,
                text=f"Min: {min_bpm_val:.1f} BPM",
                showarrow=True,
                arrowhead=1,
                ax=20,
                ay=40,
                font=dict(color="#a3d194"),
                yref="y2",
            )

        # Build plain-text summary for HTML (Analysis Summary button popup); no longer drawn on plot.
        summary_lines: List[str] = []
        if hrv_summary:
            if hrv_summary.get("avg_bpm") is not None:
                summary_lines.append(
                    f"Avg/Min/Max BPM: {hrv_summary['avg_bpm']:.1f} / {hrv_summary['min_bpm']:.1f} / {hrv_summary['max_bpm']:.1f}"
                )
            if hrr_stats and hrr_stats.get("hrr_value_bpm") is not None:
                summary_lines.append(f"1-Min HRR: {hrr_stats['hrr_value_bpm']:.1f} BPM Drop")
            if peak_recovery_stats and peak_recovery_stats.get("slope_bpm_per_sec") is not None:
                summary_lines.append(f"Peak Recovery Rate: {peak_recovery_stats['slope_bpm_per_sec']:.2f} BPM/sec")
            if hrv_summary.get("avg_rmssdc") is not None:
                summary_lines.append(f"Avg. Corrected RMSSD: {hrv_summary['avg_rmssdc']:.2f}")
            if hrv_summary.get("avg_sdnn") is not None:
                summary_lines.append(f"Avg. Windowed SDNN: {hrv_summary['avg_sdnn']:.2f} ms")
            if hrv_summary.get("avg_lf_hf_ratio") is not None:
                summary_lines.append(f"Avg. LF/HF (windowed): {hrv_summary['avg_lf_hf_ratio']:.2f}")
            global_freq = hrv_summary.get("global_freq") if hrv_summary else None
            if global_freq:
                summary_lines.append(
                    f"VLF/LF/HF (global, ms²): {global_freq.get('vlf_power', 0):.2f} / {global_freq.get('lf_power', 0):.2f} / {global_freq.get('hf_power', 0):.2f} ; LF/HF: {global_freq.get('lf_hf_ratio', 0):.2f}"
                )
        self.analysis_summary_text = "\n".join(summary_lines) if summary_lines else ""

    def _add_slope_traces(self, major_inclines, major_declines, peak_recovery_stats, peak_exertion_stats):
        """Adds traces for major exertion and recovery periods."""
        if major_inclines:
            for i, incline in enumerate(major_inclines):
                c_data = [incline["duration_sec"], incline["bpm_increase"], incline["slope_bpm_per_sec"]]
                self.fig.add_trace(
                    go.Scatter(
                        x=[incline["start_time"], incline["end_time"]],
                        y=[incline["start_bpm"], incline["end_bpm"]],
                        mode="lines",
                        line=dict(color="purple", width=4),
                        name="Exertion",
                        legendgroup="Exertion",
                        showlegend=(i == 0),
                        visible="legendonly",
                        yaxis="y2",
                        hovertemplate="<b>Exertion Period</b><br>Duration: %{customdata[0]:.1f}s<br>BPM Increase: %{customdata[1]:.1f}<br>Slope: %{customdata[2]:.2f} BPM/sec<extra></extra>",
                        customdata=np.array([c_data, c_data]),
                    )
                )

        if major_declines:
            for i, decline in enumerate(major_declines):
                c_data = [decline["duration_sec"], decline["bpm_decrease"], decline["slope_bpm_per_sec"]]
                self.fig.add_trace(
                    go.Scatter(
                        x=[decline["start_time"], decline["end_time"]],
                        y=[decline["start_bpm"], decline["end_bpm"]],
                        mode="lines",
                        line=dict(color="#2ca02c", width=4),
                        name="Recovery",
                        legendgroup="Recovery",
                        showlegend=(i == 0),
                        visible="legendonly",
                        yaxis="y2",
                        hovertemplate="<b>Recovery Period</b><br>Duration: %{customdata[0]:.1f}s<br>BPM Decrease: %{customdata[1]:.1f}<br>Slope: %{customdata[2]:.2f} BPM/sec<extra></extra>",
                        customdata=np.array([c_data, c_data]),
                    )
                )

        if peak_recovery_stats:
            stats = peak_recovery_stats
            self.fig.add_trace(
                go.Scatter(
                    x=[stats["start_time"], stats["end_time"]],
                    y=[stats["start_bpm"], stats["end_bpm"]],
                    mode="lines",
                    line=dict(color="#ff69b4", width=5),
                    name="Peak Recovery Slope",
                    legendgroup="Steepest Slopes",
                    visible="legendonly",
                    yaxis="y2",
                    hovertemplate="<b>Peak Recovery Slope</b><br>Slope: %{customdata[0]:.2f} BPM/sec<br>Duration: %{customdata[1]:.1f}s<extra></extra>",
                    customdata=np.array([[stats["slope_bpm_per_sec"], stats["duration_sec"]]] * 2),
                )
            )

        if peak_exertion_stats:
            stats = peak_exertion_stats
            self.fig.add_trace(
                go.Scatter(
                    x=[stats["start_time"], stats["end_time"]],
                    y=[stats["start_bpm"], stats["end_bpm"]],
                    mode="lines",
                    line=dict(color="#9d32a8", width=5),
                    name="Peak Exertion Slope",
                    legendgroup="Steepest Slopes",
                    visible="legendonly",
                    yaxis="y2",
                    hovertemplate="<b>Peak Exertion Slope</b><br>Slope: +%{customdata[0]:.2f} BPM/sec<br>Duration: %{customdata[1]:.1f}s<extra></extra>",
                    customdata=np.array([[stats["slope_bpm_per_sec"], stats["duration_sec"]]] * 2),
                )
            )

    def _add_trapezoid_shapes(self, trapezoids: Optional[List[Dict]]):
        """Draws trapezoid outlines and markers for detected HR artifacts."""
        if not trapezoids:
            return

        for idx, trap in enumerate(trapezoids, start=1):
            event_sequence = [
                ("Start of rise", trap["t_start_rise"], trap["bpm_start_rise"]),
                ("End of rise", trap["t_end_rise"], trap["bpm_end_rise"]),
                ("Start of fall", trap["t_start_fall"], trap["bpm_start_fall"]),
                ("End of fall", trap["t_end_fall"], trap["bpm_end_fall"]),
            ]
            x_times = [seconds_to_datetime(t) for _, t, _ in event_sequence]
            y_values = [bpm for _, _, bpm in event_sequence]
            customdata = [
                f"<b>{label}</b><br>{t:.3f}s<br>{bpm:.1f} BPM" for label, t, bpm in event_sequence
            ]

            self.fig.add_trace(
                go.Scatter(
                    x=x_times,
                    y=y_values,
                    mode="lines+markers",
                    name="Trapezoid Artifacts",
                    marker=dict(symbol="circle-open", size=8, color="#ffd166"),
                    line=dict(color="#ffd166", width=2),
                    customdata=customdata,
                    hovertemplate="%{customdata}<extra></extra>",
                    legendgroup="Trapezoid Artifacts",
                    showlegend=(idx == 1),
                ),
                secondary_y=True,
            )

    def _generate_custom_html(
        self,
        plotly_html: str,
        plot_title: str,
        base_name: str,
        *,
        pipeline_steps_html: str = "",
    ) -> str:
        """
        Generates custom HTML with audio player, timeline scrubber, and synchronized playhead.
        Fixes audio path issues and adds debugging capabilities.
        """
        audio_file_name = os.path.basename(self.audio_source_path)
        duration_sec = self.audio_duration_sec or 0

        audio_src = ""
        if os.path.exists(self.audio_source_path):
            dest_audio_path = os.path.join(self.output_directory, audio_file_name)
            src_abspath = os.path.abspath(self.audio_source_path)
            dest_abspath = os.path.abspath(dest_audio_path)

            if src_abspath != dest_abspath:
                try:
                    shutil.copy2(self.audio_source_path, dest_audio_path)
                    logging.info(f"✅ Copied audio file to {dest_audio_path}")
                except Exception as e:
                    logging.error(f"❌ Could not copy audio file: {e}")
            audio_src = audio_file_name.replace('\\', '/')
        else:
            logging.error(f"❌ Audio source file does NOT exist: {self.audio_source_path}")
            dest_audio_path = os.path.join(self.output_directory, audio_file_name)
            if os.path.exists(dest_audio_path):
                audio_src = audio_file_name.replace('\\', '/')
                logging.info(f"✅ Found audio file in output directory: {dest_audio_path}")
            else:
                logging.error(f"❌ Audio file not found anywhere: {audio_file_name}")
                audio_src = ""

        filtered_debug_file_name = f"{base_name}_filtered_debug.wav"
        filtered_debug_path = os.path.join(self.output_directory, filtered_debug_file_name)
        filtered_available = os.path.exists(filtered_debug_path)
        filtered_audio_src = filtered_debug_file_name.replace('\\', '/') if filtered_available else ""
        if filtered_available:
            logging.info(f"🎧 Using filtered debug audio: {filtered_debug_path}")

        logging.info(f"🎵 HTML audio source path: '{audio_src}'")
        import urllib.parse
        audio_src_escaped = urllib.parse.quote(audio_src)
        filtered_audio_src_escaped = urllib.parse.quote(filtered_audio_src) if filtered_audio_src else ""

        # Prepare spectrogram filenames (PNGs saved in same directory as HTML; no embedding).
        spectrogram_original_src = ""
        spectrogram_filtered_src = ""
        spectrogram_available_original = "false"
        spectrogram_available_filtered = "false"

        spectrogram_enabled = getattr(self, "spectrogram_enabled", True)

        if spectrogram_enabled:
            # Original spectrogram (precomputed in plot_and_save if possible)
            if getattr(self, "spectrogram_original_filename", None):
                spectrogram_original_src = self.spectrogram_original_filename
                spectrogram_available_original = "true"
            else:
                # Fallback: generate and save to file from the copied audio in the output directory
                try:
                    if audio_src:
                        orig_audio_path_for_spec = os.path.join(self.output_directory, audio_src)
                        spec_path = os.path.join(self.output_directory, f"{base_name}_spectrogram.png")
                        spec_name = self._generate_spectrogram_image(orig_audio_path_for_spec, spec_path)
                        if spec_name:
                            spectrogram_original_src = spec_name
                            spectrogram_available_original = "true"
                except Exception as e:
                    logging.warning(f"Failed to generate on-demand original spectrogram: {e}")

            # Filtered spectrogram (if filtered debug audio exists)
            if filtered_available:
                try:
                    spec_filtered_path = os.path.join(
                        self.output_directory, f"{base_name}_filtered_spectrogram.png"
                    )
                    spec_filtered_name = self._generate_spectrogram_image(
                        filtered_debug_path, spec_filtered_path
                    )
                    if spec_filtered_name:
                        spectrogram_filtered_src = spec_filtered_name
                        spectrogram_available_filtered = "true"
                except Exception as e:
                    logging.warning(f"Failed to generate filtered spectrogram: {e}")
        else:
            logging.info("Spectrogram generation disabled; no spectrogram images generated.")

        audio_source_options = ['<option value="original">Original Audio</option>']
        if filtered_available:
            audio_source_options.append('<option value="filtered">Filtered Debug</option>')
        audio_source_select_html = (
            '<select id="audio-source-select" class="audio-source-select">'
            + "".join(audio_source_options)
            + '</select>'
        )
        
        # Build configuration payload for external interactive_plot.js script
        config_payload = {
            "totalDuration": float(duration_sec),
            "spectrogramSources": {
                "original": spectrogram_original_src,
                "filtered": spectrogram_filtered_src,
            },
            "spectrogramAvailable": {
                "original": spectrogram_available_original == "true",
                "filtered": spectrogram_available_filtered == "true",
            },
            "audioSources": {
                "original": audio_src_escaped,
                "filtered": filtered_audio_src_escaped,
            },
            "audioLabels": {
                "original": audio_file_name,
                "filtered": filtered_debug_file_name if filtered_available else audio_file_name,
            },
            "analysisSummary": getattr(self, "analysis_summary_text", "") or "",
        }
        config_json = json.dumps(config_payload)

        # Ensure interactive_plot.js is available next to the HTML file
        try:
            js_src_path = os.path.join(os.path.dirname(__file__), "assets", "interactive_plot.js")
            js_dest_path = os.path.join(self.output_directory, "interactive_plot.js")
            if os.path.exists(js_src_path):
                shutil.copy2(js_src_path, js_dest_path)
                logging.info(f"Copied interactive_plot.js to {js_dest_path}")
            else:
                logging.error(f"interactive_plot.js not found at {js_src_path}; HTML will reference a missing script.")
        except Exception as e:
            logging.error(f"Failed to copy interactive_plot.js: {e}")

        html_template = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>{plot_title}</title>
    <style>
        * {{
            box-sizing: border-box;
        }}
        body {{
            margin: 0;
            padding: 0;
            background-color: #111;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #e0e0e0;
        }}
        
        /* Main container - full viewport */
        #main-container {{
            width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        /* Timeline Scrubber - compact bar above the graph */
        #timeline-container {{
            background: linear-gradient(180deg, #1e1e2e 0%, #151520 100%);
            border-bottom: 1px solid #333;
            padding: 4px 10px;
            flex-shrink: 0;
        }}
        
        /* Controls row */
        #controls-row {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
            flex-wrap: wrap;
        }}
        
        #current-time {{
            font-size: 12px;
            font-weight: bold;
            color: #00d4ff;
            font-family: 'Consolas', 'Monaco', monospace;
            min-width: 140px;
        }}
        
        #audio-controls {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        #audio-controls button {{
            background: #2a2a3a;
            border: 1px solid #444;
            color: #e0e0e0;
            padding: 3px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 11px;
            transition: all 0.15s;
        }}
        
        #audio-controls button:hover {{
            background: #3a3a4a;
            border-color: #00d4ff;
        }}
        
        #audio-controls button.active {{
            background: #00d4ff;
            color: #111;
        }}

        #grid-controls {{
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 11px;
            color: #aaa;
        }}

        #grid-controls .grid-label {{
            font-size: 11px;
            font-weight: 600;
            color: #cfdcff;
        }}

        .grid-toggle-button {{
            background: #2a2a3a;
            border: 1px solid #444;
            color: #e0e0e0;
            padding: 3px 8px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 11px;
            transition: all 0.15s;
        }}

        .grid-toggle-button:hover {{
            background: #3a3a4a;
            border-color: #00d4ff;
        }}

        .grid-toggle-button.active {{
            background: #00d4ff;
            color: #111;
        }}
        
        #volume-control {{
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 12px;
        }}
        
        #volume-slider {{
            width: 60px;
            height: 3px;
            -webkit-appearance: none;
            background: #333;
            border-radius: 2px;
            outline: none;
        }}
        
        #volume-slider::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 10px;
            height: 10px;
            background: #00d4ff;
            border-radius: 50%;
            cursor: pointer;
        }}

        #audio-source-select {{
            background: #1e1e2e;
            border: 1px solid #333;
            color: #e0e0e0;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 11px;
            font-family: 'Segoe UI', sans-serif;
        }}
        
        #total-time {{
            font-size: 12px;
            color: #888;
            font-family: 'Consolas', 'Monaco', monospace;
        }}
        

        /* Labeling controls - aligned right for visual separation from playback/grid controls */
        #labeling-controls {{
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 11px;
            color: #aaa;
            flex-wrap: wrap;
            margin-left: auto;
        }}

        #label-type-select {{
            background: #1e1e2e;
            border: 1px solid #333;
            color: #e0e0e0;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 11px;
            font-family: 'Segoe UI', sans-serif;
        }}

        #apply-label-btn,
        #download-labels-btn {{
            background: #2a2a3a;
            border: 1px solid #444;
            color: #e0e0e0;
            padding: 3px 8px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 11px;
            transition: all 0.15s;
        }}

        #apply-label-btn:hover,
        #download-labels-btn:hover {{
            background: #3a3a4a;
            border-color: #00d4ff;
        }}
        
        /* Timeline scrubber bar */
        #timeline-scrubber {{
            position: relative;
            height: 18px;
            background: #1a1a2a;
            border-radius: 3px;
            cursor: pointer;
            overflow: hidden;
            border: 1px solid #333;
        }}
        
        #timeline-progress {{
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            background: linear-gradient(90deg, #00d4ff44 0%, #00d4ff22 100%);
            pointer-events: none;
        }}
        
        #timeline-playhead {{
            position: absolute;
            top: 0;
            width: 2px;
            height: 100%;
            background: #00d4ff;
            box-shadow: 0 0 6px #00d4ff;
            pointer-events: none;
        }}
        
        #timeline-ticks {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
        }}
        
        .timeline-tick {{
            position: absolute;
            top: 0;
            width: 1px;
            background: #333;
        }}
        
        .timeline-tick.major {{
            height: 100%;
            background: #444;
        }}
        
        .timeline-tick.minor {{
            height: 40%;
            top: 60%;
        }}
        
        .tick-label {{
            position: absolute;
            top: 1px;
            font-size: 8px;
            color: #666;
            transform: translateX(-50%);
            pointer-events: none;
        }}
        
        /* Chart container - fills remaining space */
        #chart-container {{
            flex: 1;
            position: relative;
            min-height: 0;
            display: flex;
            flex-direction: column;
        }}
        
        /* Chart toolbar - title, audio filename, legend filter */
        #chart-toolbar {{
            flex-shrink: 0;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 4px 8px;
            background: rgba(40, 40, 50, 0.6);
            border-bottom: 1px solid #333;
            font-size: 12px;
        }}
        #chart-toolbar .chart-toolbar-title {{
            color: #aaa;
            white-space: nowrap;
        }}
        #chart-toolbar .chart-toolbar-label {{
            color: #aaa;
            white-space: nowrap;
            margin-left: auto;
        }}
        #chart-toolbar #audio-file-name {{
            font-size: 12px;
            color: #ccc;
            white-space: nowrap;
            flex-shrink: 0;
        }}
        #legend-category-filter {{
            padding: 2px 6px;
            background: #2a2a35;
            color: #ddd;
            border: 1px solid #444;
            border-radius: 3px;
            font-size: 12px;
            cursor: pointer;
        }}
        #legend-category-filter:hover {{
            border-color: #666;
        }}
        
        .plotly-chart-wrapper {{
            position: relative;
            flex: 1;
            min-height: 0;
            width: 100%;
        }}

        #plotly-chart {{
            width: 100%;
            height: 100%;
        }}

        #plotly-chart > div {{
            width: 100% !important;
            height: 100% !important;
        }}
        
        /* Vertical playhead line on chart */
        #chart-playhead {{
            position: absolute;
            top: 0;
            width: 2px;
            height: 100%;
            background: #ff4757;
            box-shadow: 0 0 8px #ff4757;
            pointer-events: none;
            z-index: 100;
            display: none;
        }}
        
        /* Hidden audio element */
        #audio-player {{
            display: none;
        }}
        
        /* Spectrogram overlay */
        #spectrogram-container {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }}
        
        #spectrogram-image {{
            position: absolute;
            height: 100%;
            opacity: 0.4;
            pointer-events: none;
            image-rendering: auto;
            transition: opacity 0.2s ease;
        }}
        
        #spectrogram-image.hidden {{
            opacity: 0;
        }}
        
        /* Keyboard shortcuts hint */
        #shortcuts-hint {{
            position: fixed;
            bottom: 8px;
            right: 8px;
            background: rgba(30, 30, 40, 0.85);
            padding: 6px 10px;
            border-radius: 4px;
            font-size: 10px;
            color: #777;
            z-index: 1000;
        }}
        
        #shortcuts-hint kbd {{
            background: #333;
            padding: 1px 4px;
            border-radius: 2px;
            margin: 0 1px;
            font-size: 9px;
        }}

        /* Analysis Summary modal */
        #analysis-summary-overlay {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, 0.7);
            z-index: 3000;
            align-items: center;
            justify-content: center;
        }}
        #analysis-summary-overlay.visible {{
            display: flex;
        }}
        #analysis-summary-modal {{
            background: #1e1e2e;
            border: 1px solid #444;
            border-radius: 8px;
            padding: 16px;
            max-width: 90%;
            max-height: 80vh;
            display: flex;
            flex-direction: column;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }}
        #analysis-summary-modal h3 {{
            margin: 0 0 10px 0;
            font-size: 14px;
            color: #00d4ff;
        }}
        #analysis-summary-text {{
            width: 480px;
            min-height: 120px;
            max-height: 50vh;
            padding: 10px;
            background: #111;
            border: 1px solid #333;
            border-radius: 4px;
            color: #e0e0e0;
            font-family: Consolas, Monaco, monospace;
            font-size: 12px;
            resize: vertical;
        }}
        #analysis-summary-modal .modal-close {{
            margin-top: 12px;
            align-self: flex-end;
            padding: 6px 14px;
            background: #2a2a3a;
            border: 1px solid #444;
            color: #e0e0e0;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
        }}
        #analysis-summary-modal .modal-close:hover {{
            background: #3a3a4a;
            border-color: #00d4ff;
        }}
    </style>
</head>
<body>
    <div id="main-container">
        <!-- Timeline Scrubber - compact bar above graph -->
        <div id="timeline-container">
            <div id="controls-row">
                <span id="current-time">00:00.000 (0.00s)</span>
                <div id="audio-controls">
                    <button id="play-btn" title="Play/Pause (Space)">▶ Play</button>
                    <button id="stop-btn" title="Stop (S)">⏹ Stop</button>
                    <button id="sync-btn" class="active" title="Sync playhead">🔗</button>
                    <button id="spectrogram-btn" title="Toggle Spectrogram (G)">📊 Spectrogram</button>
                    <div id="spectrogram-controls">
                        <input type="range" id="spectrogram-opacity" min="0.1" max="0.8" step="0.05" value="0.4" title="Spectrogram opacity">
                    </div>
                    <div id="volume-control">
                        <span>🔊</span>
                        <input type="range" id="volume-slider" min="0" max="1" step="0.05" value="1">
                    </div>
                    {audio_source_select_html}
                    <button id="analysis-summary-btn" title="View analysis summary (copy-friendly)">📋 Analysis Summary</button>
                </div>
                <div id="grid-controls">
                    <span class="grid-label">Grid:</span>
                    <button class="grid-toggle-button" data-grid-axis="yaxis" title="Toggle signal amplitude gridlines">Signal</button>
                    <button class="grid-toggle-button active" data-grid-axis="yaxis2" title="Toggle BPM/HRV gridlines">BPM</button>
                </div>
                <div id="labeling-controls">
                    <span class="grid-label">Label:</span>
                    <select id="label-type-select" title="Desired label for nearest peak">
                        <option value="S1">S1</option>
                        <option value="S2">S2</option>
                        <option value="Noise">Noise</option>
                    </select>
                    <button id="apply-label-btn" title="Relabel nearest peak to current playhead time">Apply</button>
                    <button id="flip-labels-right-btn" title="Flip all S1/S2 labels to the right of the playhead">Flip Right</button>
                    <button id="download-labels-btn" title="Download current labels as CSV">Download CSV</button>
                    <button id="import-labels-btn" title="Import manually labeled peaks CSV">Import CSV</button>
                    <input type="file" id="import-labels-input" accept=".csv" style="display:none" />
                </div>
                <span id="total-time">{int(duration_sec // 60):02d}:{int(duration_sec % 60):02d}</span>
            </div>
            <div id="timeline-scrubber">
                <div id="timeline-ticks"></div>
                <div id="timeline-progress"></div>
                <div id="timeline-playhead"></div>
            </div>
        </div>
        
        <!-- Chart container - takes up remaining space -->
        <div id="chart-container">
            <div id="chart-toolbar">
                <span class="chart-toolbar-title">Heartbeat Analysis – </span>
                <span id="audio-file-name" title="{audio_file_name}">{audio_file_name}</span>
                <label for="legend-category-filter" class="chart-toolbar-label">Show:</label>
                <select id="legend-category-filter" title="Filter legend and visible traces by category">
                    <option value="all">All</option>
                    <option value="debug">Debug</option>
                    <option value="analysis">Analysis Data</option>
                </select>
            </div>
            <div id="spectrogram-container">
                <img id="spectrogram-image" class="hidden" src="{spectrogram_original_src}" alt="Spectrogram" />
            </div>
            <div id="chart-playhead"></div>
            <div id="plotly-chart">
                {plotly_html}
            </div>
        </div>
    </div>
    
    <!-- Hidden audio player -->
    <audio id="audio-player" preload="auto">
        Your browser does not support audio playback.
    </audio>
    
    <!-- Analysis Summary modal -->
    <div id="analysis-summary-overlay" aria-hidden="true">
        <div id="analysis-summary-modal">
            <h3>Analysis Summary</h3>
            <textarea id="analysis-summary-text" readonly placeholder="No summary data."></textarea>
            <button type="button" class="modal-close" id="analysis-summary-close">Close</button>
        </div>
    </div>
    
    <!-- Keyboard shortcuts hint -->
    <div id="shortcuts-hint">
        <kbd>Space</kbd> Play &nbsp;
        <kbd>S</kbd> Stop &nbsp;
        <kbd>←→</kbd> Seek &nbsp;
        <kbd>G</kbd> Spectrogram
    </div>
    
    <script>
        window.BPM_ANALYZER_CONFIG = {config_json};
    </script>
    <script src="interactive_plot.js"></script>
</body>
</html>'''
        
        return html_template
