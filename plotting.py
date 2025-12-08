import os
import datetime
import logging
import csv
import base64
import shutil
import io
from typing import Dict, Optional, List

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import librosa
import librosa.display
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

from bpm_analysis import _get_peak_type_from_debug, format_debug_entry, PeakType


class Plotter:
    """Handles the creation and generation of the final analysis plot."""

    def __init__(self, file_name: str, params: Dict, sample_rate: int, output_directory: str):
        self.file_name = file_name
        self.params = params
        self.sample_rate = sample_rate
        self.output_directory = output_directory
        self.fig = make_subplots(specs=[[{"secondary_y": True}]])
        self.audio_duration_sec = None  # Will be set during plot_and_save
        self.spectrogram_base64 = None  # Will be set when generating spectrogram

    def _generate_spectrogram_image(self) -> Optional[str]:
        """
        Generate a spectrogram image from the audio file and return as base64 PNG.
        The spectrogram is rendered with a transparent background for overlay.
        """
        try:
            # Load audio at a reasonable sample rate for spectrogram
            audio_data, sr = librosa.load(self.file_name, sr=22050, mono=True)
            
            if audio_data is None or len(audio_data) == 0:
                logging.warning("Could not load audio for spectrogram generation")
                return None
            
            # Compute mel spectrogram for better visual representation
            n_fft = 2048
            hop_length = 512
            n_mels = 128
            
            # Generate mel spectrogram
            S = librosa.feature.melspectrogram(
                y=audio_data, sr=sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels
            )
            
            # Convert to dB scale
            S_dB = librosa.power_to_db(S, ref=np.max)
            
            # Calculate figure dimensions based on audio duration
            duration = len(audio_data) / sr
            # Width should be proportional to duration, height fixed
            fig_width = max(20, duration / 10)  # Scale width with duration
            fig_height = 6
            
            # Create figure with transparent background
            fig, ax = plt.subplots(figsize=(fig_width, fig_height))
            fig.patch.set_alpha(0)
            ax.patch.set_alpha(0)
            
            # Display spectrogram with a colormap that works well as background
            img = librosa.display.specshow(
                S_dB, sr=sr, hop_length=hop_length, x_axis='time', y_axis='mel',
                ax=ax, cmap='magma'
            )
            
            # Remove axes, labels, and all decorations for clean overlay
            ax.axis('off')
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title('')
            
            # Remove all margins
            plt.tight_layout(pad=0)
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
            
            # Save to buffer as PNG with transparency
            buf = io.BytesIO()
            fig.savefig(buf, format='png', transparent=True, dpi=100, 
                       bbox_inches='tight', pad_inches=0)
            buf.seek(0)
            
            # Encode to base64
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            
            plt.close(fig)
            buf.close()
            
            logging.info("Generated spectrogram image for background overlay")
            return img_base64
            
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
        
        time_axis_dt = pd.to_datetime(
            [datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t) for t in self.time_axis_sec]
        )

        self._add_line_traces(time_axis_dt, audio_envelope, analysis_data)
        self._add_trough_markers(audio_envelope, analysis_data)
        self._add_peak_traces(all_raw_peaks, analysis_data.get("beat_debug_info", {}), audio_envelope)
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

        self._configure_layout()

        base_name = os.path.basename(os.path.splitext(self.file_name)[0])
        output_html_path = os.path.join(self.output_directory, f"{base_name}_bpm_plot.html")
        plot_title = f"Heartbeat Analysis - {os.path.basename(self.file_name)}"
        plot_config = {"scrollZoom": True, "toImageButtonOptions": {"filename": plot_title, "format": "png", "scale": 2}}
        
        # Generate spectrogram image for background overlay
        self.spectrogram_base64 = self._generate_spectrogram_image()
        
        # Generate the base Plotly HTML
        plotly_html = self.fig.to_html(config=plot_config, full_html=False, include_plotlyjs='cdn')
        
        # Generate custom HTML with audio player and playhead
        custom_html = self._generate_custom_html(plotly_html, plot_title, base_name)
        
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(custom_html)
        logging.info(f"Interactive plot with audio player saved to {output_html_path}")

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

    def _configure_layout(self):
        """Sets up the plot layout, titles, and axes with custom x-axis tick labels."""
        plot_title = f"Heartbeat Analysis - {os.path.basename(self.file_name)}"

        self.fig.update_layout(
            template="plotly_dark",
            title_text=plot_title,
            dragmode="pan",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(t=140, b=100),
            hovermode="x unified",
        )

        tick_positions_sec = np.linspace(0, self.time_axis_sec[-1], num=10)
        epoch = datetime.datetime.fromtimestamp(0)

        tickvals = [epoch + datetime.timedelta(seconds=s) for s in tick_positions_sec]
        ticktext = [f"{int(s // 60):02d}:{int(s % 60):02d} ({s:.2f})" for s in tick_positions_sec]

        self.fig.update_xaxes(
            title_text="Time", tickvals=tickvals, ticktext=ticktext, hoverformat="%M:%S.%L"
        )

        robust_upper_limit = np.quantile(self.fig.data[0].y, 0.95) if self.fig.data else 1
        amplitude_scale = self.params.get("plot_amplitude_scale_factor", 60.0)
        self.fig.update_yaxes(
            title_text="Signal Amplitude", secondary_y=False, range=[0, robust_upper_limit * amplitude_scale]
        )
        self.fig.update_yaxes(title_text="BPM / HRV", secondary_y=True, range=[50, 200])

    def _add_line_traces(self, time_axis_dt: pd.Series, audio_envelope: np.ndarray, analysis_data: Dict):
        """Adds downsampled audio envelope and noise floor traces for performance."""
        plot_time_axis_dt = time_axis_dt
        plot_envelope = audio_envelope
        plot_noise_floor = analysis_data.get("dynamic_noise_floor_series")

        factor = self.params.get("plot_downsample_factor", 5)
        if factor > 1 and len(audio_envelope) >= factor:
            logging.info(f"Downsampling line traces by a factor of {factor} for plotting.")
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
                    line=dict(color="green", dash="dot", width=1.5),
                    hovertemplate="Noise Floor: %{y:.4f}<extra></extra>",
                ),
                secondary_y=False,
            )

    def _add_trough_markers(self, audio_envelope: np.ndarray, analysis_data: Dict):
        """Adds trough markers to the plot using original full-resolution data for accuracy."""
        trough_indices = analysis_data.get("trough_indices")
        if trough_indices is not None and trough_indices.size > 0:
            trough_times_dt = pd.to_datetime(
                [datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t) for t in (trough_indices / self.sample_rate)]
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

    def _add_peak_traces(self, all_raw_peaks, debug_info, audio_envelope):
        """Adds S1, S2, and Noise peak markers to the plot with detailed hover info."""
        s1_peaks = {"indices": [], "customdata": []}
        s2_peaks = {"indices": [], "customdata": []}
        noise_peaks = {"indices": [], "customdata": []}

        classified_indices = set()

        for peak_idx, debug_value in debug_info.items():
            hover_text_parts = []

            peak_type = _get_peak_type_from_debug(debug_value) or "Unknown Peak"
            hover_text_parts.append(f"<b>Type:</b> {peak_type}")
            hover_text_parts.append(f"<b>Time:</b> {peak_idx / self.sample_rate:.2f}s")
            hover_text_parts.append(f"<b>Amp:</b> {audio_envelope[peak_idx]:.0f}")
            hover_text_parts.append("---")

            formatted_lines = format_debug_entry(debug_value)
            if formatted_lines:
                sub_text = "<br>".join(l.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;") for l in formatted_lines)
                hover_text_parts.append(sub_text)

            full_hover_text = "<br>".join(hover_text_parts)
            classified_indices.add(peak_idx)

            if PeakType.is_s1(peak_type):
                s1_peaks["indices"].append(peak_idx)
                s1_peaks["customdata"].append(full_hover_text)
            elif PeakType.is_s2(peak_type):
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

        if s1_peaks["indices"]:
            times_dt = pd.to_datetime(
                [
                    datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t)
                    for t in (np.array(s1_peaks["indices"]) / self.sample_rate)
                ]
            )
            self.fig.add_trace(
                go.Scatter(
                    x=times_dt,
                    y=audio_envelope[s1_peaks["indices"]],
                    mode="markers",
                    name="S1 Beats",
                    marker=dict(color="#e36f6f", size=8, symbol="diamond"),
                    customdata=s1_peaks["customdata"],
                    hovertemplate=hovertemplate,
                ),
                secondary_y=False,
            )

        if s2_peaks["indices"]:
            times_dt = pd.to_datetime(
                [
                    datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t)
                    for t in (np.array(s2_peaks["indices"]) / self.sample_rate)
                ]
            )
            self.fig.add_trace(
                go.Scatter(
                    x=times_dt,
                    y=audio_envelope[s2_peaks["indices"]],
                    mode="markers",
                    name="S2 Beats",
                    marker=dict(color="orange", symbol="circle", size=6),
                    customdata=s2_peaks["customdata"],
                    hovertemplate=hovertemplate,
                ),
                secondary_y=False,
            )

        if noise_peaks["indices"]:
            times_dt = pd.to_datetime(
                [
                    datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t)
                    for t in (np.array(noise_peaks["indices"]) / self.sample_rate)
                ]
            )
            self.fig.add_trace(
                go.Scatter(
                    x=times_dt,
                    y=audio_envelope[noise_peaks["indices"]],
                    mode="markers",
                    name="Noise/Rejected",
                    marker=dict(color="grey", symbol="x", size=6),
                    customdata=noise_peaks["customdata"],
                    hovertemplate=hovertemplate,
                ),
                secondary_y=False,
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
            start_datetime = datetime.datetime.fromtimestamp(0)
            lt_times_dt = pd.to_datetime([start_datetime + datetime.timedelta(seconds=t) for t in lt_series.index])
            self.fig.add_trace(
                go.Scatter(
                    x=lt_times_dt,
                    y=lt_series.values,
                    name="BPM Trend (Belief)",
                    line=dict(color="orange", width=2, dash="dot"),
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
                [datetime.datetime.fromtimestamp(0) + datetime.timedelta(seconds=t) for t in windowed_hrv_df["time"]]
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

    def _add_annotations_and_summary(self, smoothed_bpm, hrv_summary, hrr_stats, peak_recovery_stats):
        """Adds min/max BPM annotations and the main summary box."""
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

        if hrv_summary:
            annotation_text = "<b>Analysis Summary</b><br>"
            if hrv_summary.get("avg_bpm") is not None:
                annotation_text += (
                    f"Avg/Min/Max BPM: {hrv_summary['avg_bpm']:.1f} / {hrv_summary['min_bpm']:.1f} / {hrv_summary['max_bpm']:.1f}<br>"
                )
            if hrr_stats and hrr_stats.get("hrr_value_bpm") is not None:
                annotation_text += f"<b>1-Min HRR: {hrr_stats['hrr_value_bpm']:.1f} BPM Drop</b><br>"
            if peak_recovery_stats and peak_recovery_stats.get("slope_bpm_per_sec") is not None:
                annotation_text += f"<b>Peak Recovery Rate: {peak_recovery_stats['slope_bpm_per_sec']:.2f} BPM/sec</b><br>"
            if hrv_summary.get("avg_rmssdc") is not None:
                annotation_text += f"Avg. Corrected RMSSD: {hrv_summary['avg_rmssdc']:.2f}<br>"
            if hrv_summary.get("avg_sdnn") is not None:
                annotation_text += f"Avg. Windowed SDNN: {hrv_summary['avg_sdnn']:.2f} ms"

            self.fig.add_annotation(
                text=annotation_text,
                align="left",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.02,
                y=0.98,
                bordercolor="black",
                borderwidth=1,
                bgcolor="rgba(255, 253, 231, 0.4)",
            )

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
                        line=dict(color="purple", width=4, dash="dash"),
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
                        line=dict(color="#2ca02c", width=4, dash="dash"),
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
                    line=dict(color="#ff69b4", width=5, dash="solid"),
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
                    line=dict(color="#9d32a8", width=5, dash="solid"),
                    name="Peak Exertion Slope",
                    legendgroup="Steepest Slopes",
                    visible="legendonly",
                    yaxis="y2",
                    hovertemplate="<b>Peak Exertion Slope</b><br>Slope: +%{customdata[0]:.2f} BPM/sec<br>Duration: %{customdata[1]:.1f}s<extra></extra>",
                    customdata=np.array([[stats["slope_bpm_per_sec"], stats["duration_sec"]]] * 2),
                )
            )

    def _seconds_to_datetime(self, seconds: float) -> datetime.datetime:
        """Converts elapsed seconds since epoch to timezone-naive datetime."""
        epoch = datetime.datetime.fromtimestamp(0)
        return epoch + datetime.timedelta(seconds=seconds)

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
            x_times = [self._seconds_to_datetime(t) for _, t, _ in event_sequence]
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
                    line=dict(color="#ffd166", dash="dot", width=2),
                    customdata=customdata,
                    hovertemplate="%{customdata}<extra></extra>",
                    legendgroup="Trapezoid Artifacts",
                    showlegend=(idx == 1),
                ),
                secondary_y=True,
            )

    def _generate_custom_html(self, plotly_html: str, plot_title: str, base_name: str) -> str:
        """
        Generates custom HTML with audio player, timeline scrubber, and synchronized playhead.
        Similar to DaVinci Resolve's timeline functionality.
        """
        # Get the audio file name for the HTML
        audio_file_name = os.path.basename(self.file_name)
        duration_sec = self.audio_duration_sec or 0
        
        # Copy audio file to output directory if it exists
        audio_src = ""
        if os.path.exists(self.file_name):
            dest_audio_path = os.path.join(self.output_directory, audio_file_name)
            if os.path.abspath(self.file_name) != os.path.abspath(dest_audio_path):
                try:
                    shutil.copy2(self.file_name, dest_audio_path)
                    audio_src = audio_file_name
                    logging.info(f"Copied audio file to {dest_audio_path}")
                except Exception as e:
                    logging.warning(f"Could not copy audio file: {e}")
                    audio_src = self.file_name  # Use original path as fallback
            else:
                audio_src = audio_file_name
        
        # Prepare spectrogram data
        spectrogram_src = ""
        spectrogram_available = "false"
        if self.spectrogram_base64:
            spectrogram_src = f"data:image/png;base64,{self.spectrogram_base64}"
            spectrogram_available = "true"
        
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
        
        #total-time {{
            font-size: 12px;
            color: #888;
            font-family: 'Consolas', 'Monaco', monospace;
        }}
        
        #audio-file-name {{
            font-size: 10px;
            color: #666;
            margin-left: auto;
            max-width: 300px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
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
        
        /* Spectrogram toggle button */
        #spectrogram-btn {{
            background: #2a2a3a;
            border: 1px solid #444;
            color: #e0e0e0;
            padding: 3px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 11px;
            transition: all 0.15s;
        }}
        
        #spectrogram-btn:hover {{
            background: #3a3a4a;
            border-color: #ff9f43;
        }}
        
        #spectrogram-btn.active {{
            background: #ff9f43;
            color: #111;
        }}
        
        /* Spectrogram opacity slider */
        #spectrogram-controls {{
            display: flex;
            align-items: center;
            gap: 4px;
            font-size: 11px;
            color: #888;
        }}
        
        #spectrogram-opacity {{
            width: 50px;
            height: 3px;
            -webkit-appearance: none;
            background: #333;
            border-radius: 2px;
            outline: none;
        }}
        
        #spectrogram-opacity::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 10px;
            height: 10px;
            background: #ff9f43;
            border-radius: 50%;
            cursor: pointer;
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
                </div>
                <span id="total-time">{int(duration_sec // 60):02d}:{int(duration_sec % 60):02d}</span>
                <span id="audio-file-name" title="{audio_file_name}">{audio_file_name}</span>
            </div>
            <div id="timeline-scrubber">
                <div id="timeline-ticks"></div>
                <div id="timeline-progress"></div>
                <div id="timeline-playhead"></div>
            </div>
        </div>
        
        <!-- Chart container - takes up remaining space -->
        <div id="chart-container">
            <div id="spectrogram-container">
                <img id="spectrogram-image" class="hidden" src="{spectrogram_src}" alt="Spectrogram" />
            </div>
            <div id="chart-playhead"></div>
            <div id="plotly-chart">
                {plotly_html}
            </div>
        </div>
    </div>
    
    <!-- Hidden audio player -->
    <audio id="audio-player" preload="auto">
        <source src="{audio_src}" type="audio/wav">
        <source src="{audio_src}" type="audio/mpeg">
        <source src="{audio_src}" type="audio/ogg">
        Your browser does not support audio playback.
    </audio>
    
    <!-- Keyboard shortcuts hint -->
    <div id="shortcuts-hint">
        <kbd>Space</kbd> Play &nbsp;
        <kbd>S</kbd> Stop &nbsp;
        <kbd>←→</kbd> Seek &nbsp;
        <kbd>G</kbd> Spectrogram
    </div>
    
    <script>
        // Configuration
        const TOTAL_DURATION = {duration_sec};
        const EPOCH = new Date(0);
        const SPECTROGRAM_AVAILABLE = {spectrogram_available};
        
        // DOM Elements
        const audio = document.getElementById('audio-player');
        const playBtn = document.getElementById('play-btn');
        const stopBtn = document.getElementById('stop-btn');
        const syncBtn = document.getElementById('sync-btn');
        const spectrogramBtn = document.getElementById('spectrogram-btn');
        const spectrogramOpacity = document.getElementById('spectrogram-opacity');
        const spectrogramContainer = document.getElementById('spectrogram-container');
        const spectrogramImage = document.getElementById('spectrogram-image');
        const volumeSlider = document.getElementById('volume-slider');
        const currentTimeEl = document.getElementById('current-time');
        const timelineScrubber = document.getElementById('timeline-scrubber');
        const timelineProgress = document.getElementById('timeline-progress');
        const timelinePlayhead = document.getElementById('timeline-playhead');
        const timelineTicks = document.getElementById('timeline-ticks');
        const chartPlayhead = document.getElementById('chart-playhead');
        const chartContainer = document.getElementById('chart-container');
        
        // State
        let isPlaying = false;
        let isSynced = true;
        let isSpectrogramVisible = false;
        let plotlyGraphDiv = null;
        let xAxisRange = null;
        let fullXAxisRange = null;  // Store the full x-axis range for spectrogram positioning
        
        // Format time as MM:SS.mmm (seconds)
        function formatTime(seconds) {{
            const mins = Math.floor(seconds / 60);
            const secs = Math.floor(seconds % 60);
            const ms = Math.floor((seconds % 1) * 1000);
            return `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}.${{String(ms).padStart(3, '0')}} (${{seconds.toFixed(2)}}s)`;
        }}
        
        // Convert seconds to datetime (epoch + seconds)
        function secondsToDatetime(seconds) {{
            return new Date(EPOCH.getTime() + seconds * 1000);
        }}
        
        // Get x-axis position for a given time
        function getXPositionForTime(seconds) {{
            if (!plotlyGraphDiv || !xAxisRange) return null;
            
            const datetime = secondsToDatetime(seconds);
            const xMin = new Date(xAxisRange[0]).getTime();
            const xMax = new Date(xAxisRange[1]).getTime();
            const xTime = datetime.getTime();
            
            // Calculate position within the plot area
            const plotArea = plotlyGraphDiv._fullLayout;
            if (!plotArea) return null;
            
            const xaxis = plotArea.xaxis;
            if (!xaxis) return null;
            
            const plotLeft = xaxis._offset;
            const plotWidth = xaxis._length;
            
            const ratio = (xTime - xMin) / (xMax - xMin);
            return plotLeft + ratio * plotWidth;
        }}
        
        // Initialize timeline ticks
        function initTimelineTicks() {{
            timelineTicks.innerHTML = '';
            const numMajorTicks = 10;
            const numMinorTicks = 50;
            
            // Major ticks with labels
            for (let i = 0; i <= numMajorTicks; i++) {{
                const percent = (i / numMajorTicks) * 100;
                const time = (i / numMajorTicks) * TOTAL_DURATION;
                
                const tick = document.createElement('div');
                tick.className = 'timeline-tick major';
                tick.style.left = percent + '%';
                timelineTicks.appendChild(tick);
                
                const label = document.createElement('div');
                label.className = 'tick-label';
                label.style.left = percent + '%';
                label.textContent = `${{Math.floor(time / 60)}}:${{String(Math.floor(time % 60)).padStart(2, '0')}}`;
                timelineTicks.appendChild(label);
            }}
            
            // Minor ticks
            for (let i = 0; i < numMinorTicks; i++) {{
                if (i % (numMinorTicks / numMajorTicks) === 0) continue;
                const percent = (i / numMinorTicks) * 100;
                
                const tick = document.createElement('div');
                tick.className = 'timeline-tick minor';
                tick.style.left = percent + '%';
                timelineTicks.appendChild(tick);
            }}
        }}
        
        // Update playhead positions
        function updatePlayhead(currentTime) {{
            const percent = (currentTime / TOTAL_DURATION) * 100;
            
            // Update timeline
            timelineProgress.style.width = percent + '%';
            timelinePlayhead.style.left = percent + '%';
            
            // Update time display
            currentTimeEl.textContent = formatTime(currentTime);
            
            // Update chart playhead if synced
            if (isSynced && plotlyGraphDiv) {{
                const xPos = getXPositionForTime(currentTime);
                if (xPos !== null) {{
                    chartPlayhead.style.display = 'block';
                    chartPlayhead.style.left = xPos + 'px';
                }} else {{
                    chartPlayhead.style.display = 'none';
                }}
            }}
        }}
        
        // Seek to position
        function seekTo(seconds) {{
            audio.currentTime = Math.max(0, Math.min(seconds, TOTAL_DURATION));
            updatePlayhead(audio.currentTime);
        }}
        
        // Play/Pause toggle
        function togglePlay() {{
            if (isPlaying) {{
                audio.pause();
                playBtn.textContent = '▶ Play';
                playBtn.classList.remove('active');
            }} else {{
                audio.play().catch(e => console.log('Audio play error:', e));
                playBtn.textContent = '⏸ Pause';
                playBtn.classList.add('active');
            }}
            isPlaying = !isPlaying;
        }}
        
        // Stop playback
        function stopPlayback() {{
            audio.pause();
            audio.currentTime = 0;
            isPlaying = false;
            playBtn.textContent = '▶ Play';
            playBtn.classList.remove('active');
            updatePlayhead(0);
        }}
        
        // Toggle sync
        function toggleSync() {{
            isSynced = !isSynced;
            syncBtn.classList.toggle('active', isSynced);
            if (!isSynced) {{
                chartPlayhead.style.display = 'none';
            }} else {{
                updatePlayhead(audio.currentTime);
            }}
        }}
        
        // Toggle spectrogram visibility
        function toggleSpectrogram() {{
            if (!SPECTROGRAM_AVAILABLE) {{
                alert('Spectrogram not available for this file.');
                return;
            }}
            isSpectrogramVisible = !isSpectrogramVisible;
            spectrogramBtn.classList.toggle('active', isSpectrogramVisible);
            spectrogramImage.classList.toggle('hidden', !isSpectrogramVisible);
            if (isSpectrogramVisible) {{
                updateSpectrogramPosition();
            }}
        }}
        
        // Update spectrogram opacity
        function updateSpectrogramOpacity(value) {{
            spectrogramImage.style.opacity = value;
        }}
        
        // Update spectrogram position and scale based on current view
        function updateSpectrogramPosition() {{
            if (!plotlyGraphDiv || !isSpectrogramVisible || !SPECTROGRAM_AVAILABLE) return;
            
            const plotArea = plotlyGraphDiv._fullLayout;
            if (!plotArea) return;
            
            const xaxis = plotArea.xaxis;
            const yaxis = plotArea.yaxis;
            if (!xaxis || !yaxis) return;
            
            // Get plot area dimensions
            const plotLeft = xaxis._offset;
            const plotWidth = xaxis._length;
            const plotTop = yaxis._offset;
            const plotHeight = yaxis._length;
            
            // Get current view range
            const viewXMin = new Date(xAxisRange[0]).getTime();
            const viewXMax = new Date(xAxisRange[1]).getTime();
            
            // Get full data range (0 to total duration)
            const fullXMin = EPOCH.getTime();
            const fullXMax = EPOCH.getTime() + TOTAL_DURATION * 1000;
            
            // Calculate what portion of the full data is visible
            const visibleStartRatio = (viewXMin - fullXMin) / (fullXMax - fullXMin);
            const visibleEndRatio = (viewXMax - fullXMin) / (fullXMax - fullXMin);
            const visibleRatio = visibleEndRatio - visibleStartRatio;
            
            // Calculate spectrogram dimensions
            // The spectrogram should stretch to cover the full data range
            const spectrogramFullWidth = plotWidth / visibleRatio;
            const spectrogramLeft = plotLeft - (visibleStartRatio * spectrogramFullWidth);
            
            // Position the spectrogram container to match plot area
            spectrogramContainer.style.left = plotLeft + 'px';
            spectrogramContainer.style.top = plotTop + 'px';
            spectrogramContainer.style.width = plotWidth + 'px';
            spectrogramContainer.style.height = plotHeight + 'px';
            
            // Position the spectrogram image
            spectrogramImage.style.left = (spectrogramLeft - plotLeft) + 'px';
            spectrogramImage.style.width = spectrogramFullWidth + 'px';
            spectrogramImage.style.height = plotHeight + 'px';
            spectrogramImage.style.top = '0px';
        }}
        
        // Event Listeners
        playBtn.addEventListener('click', togglePlay);
        stopBtn.addEventListener('click', stopPlayback);
        syncBtn.addEventListener('click', toggleSync);
        spectrogramBtn.addEventListener('click', toggleSpectrogram);
        
        spectrogramOpacity.addEventListener('input', (e) => {{
            updateSpectrogramOpacity(parseFloat(e.target.value));
        }});
        
        volumeSlider.addEventListener('input', (e) => {{
            audio.volume = parseFloat(e.target.value);
        }});
        
        // Timeline scrubber click/drag
        let isDragging = false;
        
        function handleTimelineInteraction(e) {{
            const rect = timelineScrubber.getBoundingClientRect();
            const percent = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
            seekTo(percent * TOTAL_DURATION);
        }}
        
        timelineScrubber.addEventListener('mousedown', (e) => {{
            isDragging = true;
            handleTimelineInteraction(e);
        }});
        
        document.addEventListener('mousemove', (e) => {{
            if (isDragging) {{
                handleTimelineInteraction(e);
            }}
        }});
        
        document.addEventListener('mouseup', () => {{
            isDragging = false;
        }});
        
        // Audio time update
        audio.addEventListener('timeupdate', () => {{
            updatePlayhead(audio.currentTime);
        }});
        
        audio.addEventListener('ended', () => {{
            isPlaying = false;
            playBtn.textContent = '▶ Play';
            playBtn.classList.remove('active');
        }});
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {{
            // Don't trigger if typing in an input
            if (e.target.tagName === 'INPUT') return;
            
            switch(e.code) {{
                case 'Space':
                    e.preventDefault();
                    togglePlay();
                    break;
                case 'KeyS':
                    stopPlayback();
                    break;
                case 'ArrowLeft':
                    e.preventDefault();
                    seekTo(audio.currentTime - 5);
                    break;
                case 'ArrowRight':
                    e.preventDefault();
                    seekTo(audio.currentTime + 5);
                    break;
                case 'Home':
                    e.preventDefault();
                    seekTo(0);
                    break;
                case 'End':
                    e.preventDefault();
                    seekTo(TOTAL_DURATION);
                    break;
                case 'KeyG':
                    toggleSpectrogram();
                    break;
            }}
        }});
        
        // Initialize Plotly integration after chart loads
        function initPlotlyIntegration() {{
            // Find the Plotly graph div
            const graphDivs = document.querySelectorAll('.plotly-graph-div');
            if (graphDivs.length > 0) {{
                plotlyGraphDiv = graphDivs[0];
                
                // Get initial axis range
                function updateAxisRange() {{
                    if (plotlyGraphDiv._fullLayout && plotlyGraphDiv._fullLayout.xaxis) {{
                        xAxisRange = plotlyGraphDiv._fullLayout.xaxis.range;
                        // Store full range on first load
                        if (!fullXAxisRange) {{
                            fullXAxisRange = [...xAxisRange];
                        }}
                    }}
                }}
                
                updateAxisRange();
                
                // Listen for zoom/pan changes
                plotlyGraphDiv.on('plotly_relayout', function(eventdata) {{
                    updateAxisRange();
                    updatePlayhead(audio.currentTime);
                    updateSpectrogramPosition();
                }});
                
                // Also listen for plotly_afterplot for initial render
                plotlyGraphDiv.on('plotly_afterplot', function() {{
                    updateAxisRange();
                    updateSpectrogramPosition();
                }});
                
                // Update on window resize
                window.addEventListener('resize', () => {{
                    updateAxisRange();
                    updatePlayhead(audio.currentTime);
                    updateSpectrogramPosition();
                    // Resize Plotly chart to fit container
                    Plotly.Plots.resize(plotlyGraphDiv);
                }});
                
                // Click on chart to seek
                plotlyGraphDiv.on('plotly_click', function(data) {{
                    if (data.points && data.points.length > 0) {{
                        const point = data.points[0];
                        if (point.x) {{
                            // Convert datetime back to seconds
                            const clickTime = new Date(point.x);
                            const seconds = (clickTime.getTime() - EPOCH.getTime()) / 1000;
                            seekTo(seconds);
                        }}
                    }}
                }});
                
                // Initial spectrogram position update
                setTimeout(updateSpectrogramPosition, 100);
            }} else {{
                // Retry after a short delay
                setTimeout(initPlotlyIntegration, 100);
            }}
        }}
        
        // Initialize spectrogram controls based on availability
        function initSpectrogramControls() {{
            if (!SPECTROGRAM_AVAILABLE) {{
                spectrogramBtn.style.opacity = '0.5';
                spectrogramBtn.style.cursor = 'not-allowed';
                spectrogramOpacity.disabled = true;
                spectrogramOpacity.style.opacity = '0.5';
            }}
        }}
        
        // Initialize
        initTimelineTicks();
        initSpectrogramControls();
        setTimeout(initPlotlyIntegration, 500);
    </script>
</body>
</html>'''
        
        return html_template
