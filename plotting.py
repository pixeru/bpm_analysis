import os
import datetime
import logging
import csv
from typing import Dict, Optional, List

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from bpm_analysis import _get_peak_type_from_debug, format_debug_entry, PeakType


class Plotter:
    """Handles the creation and generation of the final analysis plot."""

    def __init__(self, file_name: str, params: Dict, sample_rate: int, output_directory: str):
        self.file_name = file_name
        self.params = params
        self.sample_rate = sample_rate
        self.output_directory = output_directory
        self.fig = make_subplots(specs=[[{"secondary_y": True}]])

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
        self.fig.write_html(output_html_path, config=plot_config)
        logging.info(f"Interactive plot saved to {output_html_path}")

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
