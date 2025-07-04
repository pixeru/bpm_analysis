import { AnalysisParams } from './types';

export const DEFAULT_PARAMS: AnalysisParams = {
  // General & Preprocessing Settings
  downsample_factor: 300,
  bandpass_freqs: [20, 150],

  // Signal Feature Detection
  min_peak_distance_sec: 0.05,
  peak_prominence_quantile: 0.1,
  trough_prominence_quantile: 0.1,

  // Noise Estimation & Rejection
  noise_floor_quantile: 0.20,
  noise_window_sec: 10,
  trough_rejection_multiplier: 4.0,
  noise_confidence_threshold: 0.6,
  trough_veto_multiplier: 2.1,
  trough_noise_multiplier: 3.0,
  strong_peak_override_ratio: 6.0,

  // S1/S2 Pairing & Confidence Engine
  pairing_confidence_threshold: 0.50,
  s1_s2_interval_cap_sec: 0.4,
  s1_s2_interval_rr_fraction: 0.7,
  deviation_smoothing_factor: 0.05,
  confidence_deviation_points: [0.0, 0.25, 0.40, 0.80, 1.0],
  confidence_curve_low_bpm: [0.9, 0.9, 0.7, 0.1, 0.1],
  confidence_curve_high_bpm: [0.1, 0.5, 0.75, 0.65, 0],

  // Physiology-Based Confidence Adjustment
  stability_history_window: 20,
  stability_confidence_floor: 0.60,
  stability_confidence_ceiling: 1.25,
  s1_s2_boost_ratio: 1.2,
  boost_amount_min: 0.10,
  boost_amount_max: 0.35,
  penalty_amount_min: 0.10,
  penalty_amount_max: 0.30,
  s2_s1_ratio_low_bpm: 1.5,
  s2_s1_ratio_high_bpm: 1.1,
  contractility_bpm_low: 120.0,
  contractility_bpm_high: 140.0,
  recovery_phase_duration_sec: 120,

  // Interval-Based Confidence Penalty
  interval_penalty_start_factor: 1.0,
  interval_penalty_full_factor: 1.4,
  interval_max_penalty: 0.75,

  // Kick-Start Mechanism
  kickstart_check_threshold: 0.3,
  kickstart_history_beats: 4,
  kickstart_min_s1_candidates: 3,
  kickstart_min_matches: 3,
  kickstart_override_ratio: 0.60,

  // Rhythm Plausibility & Validation
  long_term_bpm_learning_rate: 0.05,
  max_bpm_change_per_beat: 3.0,
  min_bpm: 40,
  max_bpm: 240,
  rr_interval_max_decrease_pct: 0.45,
  rr_interval_max_increase_pct: 0.70,
  lone_s1_min_strength_ratio: 0.30,
  lone_s1_forward_check_pct: 0.50,

  // Lone S1 Gradient Confidence Engine
  lone_s1_confidence_threshold: 0.50,
  lone_s1_rhythm_weight: 0.65,
  lone_s1_amplitude_weight: 0.35,
  lone_s1_rhythm_deviation_points: [0.0, 0.15, 0.30, 0.50],
  lone_s1_rhythm_confidence_curve: [1.0, 0.8, 0.4, 0.0],
  lone_s1_amplitude_ratio_points: [0.0, 0.4, 0.7, 1.0],
  lone_s1_amplitude_confidence_curve: [0.0, 0.4, 0.8, 1.0],

  // Post-Processing Correction Pass
  enable_correction_pass: false,
  rr_correction_threshold_pct: 0.40,
  rr_correction_long_interval_pct: 1.70,
  penalty_waiver_strength_ratio: 4.0,
  penalty_waiver_max_s2_s1_ratio: 2.5,
  correction_log_level: "DEBUG",

  // Output, HRV & Reporting
  output_smoothing_window_sec: 5,
  hrv_window_size_beats: 40,
  hrv_step_size_beats: 5,
  plot_amplitude_scale_factor: 250.0,
  plot_downsample_audio_envelope: true,
  plot_downsample_factor: 5,
};