export enum PeakType {
  S1_PAIRED = "S1 (Paired)",
  S2_PAIRED = "S2 (Paired)",
  LONE_S1_VALIDATED = "Lone S1 (Validated)",
  LONE_S1_CASCADE = "Lone S1 (Corrected by Cascade Reset)",
  LONE_S1_LAST = "Lone S1 (Last Peak)",
  NOISE = "Noise/Rejected",
  S1_CORRECTED_GAP = "S1 (Paired - Corrected from Gap)",
  S2_CORRECTED_GAP = "S2 (Paired - Corrected from Gap)",
  S2_CORRECTED_CONFLICT = "S2 (Paired - Corrected from Conflict)"
}

export interface AnalysisParams {
  downsample_factor: number;
  bandpass_freqs: [number, number];
  min_peak_distance_sec: number;
  peak_prominence_quantile: number;
  trough_prominence_quantile: number;
  noise_floor_quantile: number;
  noise_window_sec: number;
  trough_rejection_multiplier: number;
  noise_confidence_threshold: number;
  trough_veto_multiplier: number;
  trough_noise_multiplier: number;
  strong_peak_override_ratio: number;
  pairing_confidence_threshold: number;
  s1_s2_interval_cap_sec: number;
  s1_s2_interval_rr_fraction: number;
  deviation_smoothing_factor: number;
  confidence_deviation_points: number[];
  confidence_curve_low_bpm: number[];
  confidence_curve_high_bpm: number[];
  stability_history_window: number;
  stability_confidence_floor: number;
  stability_confidence_ceiling: number;
  s1_s2_boost_ratio: number;
  boost_amount_min: number;
  boost_amount_max: number;
  penalty_amount_min: number;
  penalty_amount_max: number;
  s2_s1_ratio_low_bpm: number;
  s2_s1_ratio_high_bpm: number;
  contractility_bpm_low: number;
  contractility_bpm_high: number;
  recovery_phase_duration_sec: number;
  interval_penalty_start_factor: number;
  interval_penalty_full_factor: number;
  interval_max_penalty: number;
  kickstart_check_threshold: number;
  kickstart_history_beats: number;
  kickstart_min_s1_candidates: number;
  kickstart_min_matches: number;
  kickstart_override_ratio: number;
  long_term_bpm_learning_rate: number;
  max_bpm_change_per_beat: number;
  min_bpm: number;
  max_bpm: number;
  rr_interval_max_decrease_pct: number;
  rr_interval_max_increase_pct: number;
  lone_s1_min_strength_ratio: number;
  lone_s1_forward_check_pct: number;
  lone_s1_confidence_threshold: number;
  lone_s1_rhythm_weight: number;
  lone_s1_amplitude_weight: number;
  lone_s1_rhythm_deviation_points: number[];
  lone_s1_rhythm_confidence_curve: number[];
  lone_s1_amplitude_ratio_points: number[];
  lone_s1_amplitude_confidence_curve: number[];
  enable_correction_pass: boolean;
  rr_correction_threshold_pct: number;
  rr_correction_long_interval_pct: number;
  penalty_waiver_strength_ratio: number;
  penalty_waiver_max_s2_s1_ratio: number;
  correction_log_level: string;
  output_smoothing_window_sec: number;
  hrv_window_size_beats: number;
  hrv_step_size_beats: number;
  plot_amplitude_scale_factor: number;
  plot_downsample_audio_envelope: boolean;
  plot_downsample_factor: number;
}

export interface PeakInfo {
  index: number;
  time: number;
  amplitude: number;
  type: PeakType;
  reason?: string;
}

export interface AnalysisData {
  dynamic_noise_floor_series: number[];
  trough_indices: number[];
  deviation_series: number[];
  beat_debug_info: Record<number, string>;
  long_term_bpm_series?: number[];
}

export interface HRVSummary {
  mean_rr: number;
  rmssd: number;
  pnn50: number;
  triangular_index: number;
  sample_entropy: number;
}

export interface HRRStats {
  peak_bpm: number;
  peak_time: number;
  recovery_rate_1min: number;
  recovery_rate_2min: number;
  recovery_percentage_1min: number;
  recovery_percentage_2min: number;
}

export interface FinalMetrics {
  smoothed_bpm: number[];
  bpm_times: number[];
  hrv_summary: HRVSummary;
  hrr_stats: HRRStats;
  windowed_hrv_df?: any[];
  major_inclines?: any[];
  major_declines?: any[];
  peak_recovery_stats?: any;
  peak_exertion_stats?: any;
}

export interface AnalysisResult {
  final_peaks: number[];
  all_raw_peaks: number[];
  analysis_data: AnalysisData;
  final_metrics: FinalMetrics;
  audio_envelope: number[];
  sample_rate: number;
}

export interface AnalysisStatus {
  stage: string;
  progress: number;
  message: string;
}