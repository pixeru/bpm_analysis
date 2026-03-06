"""
PCG (Phonocardiogram) Analysis Script
=====================================
Comprehensive heart sound analysis including heart rate, R-R intervals, and HRV metrics.

Author: Generated for PCG Analysis by Kimi K2.5 Agent
Requirements: numpy, scipy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, find_peaks, spectrogram, hilbert, decimate
from scipy.fft import fft, fftfreq
from scipy.ndimage import gaussian_filter1d
from scipy.signal import lombscargle
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURATION PARAMETERS
# ============================================================================

# Filter parameters
LOWCUT = 25          # Lower cutoff frequency (Hz)
HIGHCUT = 150        # Upper cutoff frequency (Hz)
FILTER_ORDER = 4     # Butterworth filter order

# Peak detection parameters
MIN_BPM = 150        # Minimum expected heart rate
MAX_BPM = 200        # Maximum expected heart rate
PEAK_THRESHOLD = 0.15  # Normalized amplitude threshold
PEAK_PROMINENCE = 0.1  # Minimum peak prominence

# R-R interval validation
MIN_RR_SEC = 0.25    # Minimum valid R-R interval (100 bpm max)
MAX_RR_SEC = 0.60    # Maximum valid R-R interval (240 bpm max)

# Output settings
OUTPUT_DIR = './pcg_output/'
DPI = 150

# ============================================================================
# STEP 1: DATA LOADING
# ============================================================================

def load_pcg_data(file_path):
    """
    Load PCG audio file and prepare for analysis.
    
    WHY: PCG recordings can be in various formats (mono/stereo).
    We normalize to mono and float format for consistent processing.
    """
    print(f"Loading: {file_path}")
    sample_rate, audio_data = wavfile.read(file_path)
    
    # Convert stereo to mono if needed
    if len(audio_data.shape) > 1:
        audio_data = np.mean(audio_data, axis=1)
        print("  → Converted stereo to mono")
    
    # Convert to float and normalize
    audio_data = audio_data.astype(np.float64)
    audio_data = audio_data / np.max(np.abs(audio_data))
    
    duration = len(audio_data) / sample_rate
    time = np.linspace(0, duration, len(audio_data))
    
    print(f"  → Sample Rate: {sample_rate} Hz")
    print(f"  → Duration: {duration:.2f} seconds")
    print(f"  → Total Samples: {len(audio_data):,}")
    
    return sample_rate, audio_data, time, duration


# ============================================================================
# STEP 2: SIGNAL PREPROCESSING
# ============================================================================

def create_bandpass_filter(lowcut, highcut, fs, order=4):
    """
    Create Butterworth bandpass filter coefficients.
    
    WHY: Heart sounds (S1, S2) contain energy primarily in 20-200 Hz range.
    We use a bandpass filter to remove:
    - Low frequency noise (< 20 Hz): breathing, body movement
    - High frequency noise (> 200 Hz): electrical interference, muscle noise
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    
    # Ensure valid frequency range
    low = max(0.001, min(low, 0.999))
    high = max(0.001, min(high, 0.999))
    
    if low >= high:
        low = 0.001
        high = 0.1
    
    b, a = butter(order, [low, high], btype='band')
    return b, a


def apply_bandpass_filter(signal, lowcut, highcut, fs, order=4):
    """Apply bandpass filter to signal using filtfilt for zero-phase distortion."""
    b, a = create_bandpass_filter(lowcut, highcut, fs, order)
    return filtfilt(b, a, signal)


def extract_envelope(signal, fs, smoothing_window_ms=50):
    """
    Extract signal envelope using Hilbert transform.
    
    WHY: Heart sounds are amplitude-modulated signals. The envelope captures
    the energy variations that correspond to cardiac cycles, making peak
    detection much more reliable than using the raw signal.
    
    The Hilbert transform gives us the analytic signal, and its magnitude
    represents the instantaneous amplitude (envelope).
    """
    # Hilbert transform for analytic signal
    analytic_signal = hilbert(signal)
    envelope = np.abs(analytic_signal)
    
    # Smooth with moving average (50ms window)
    window_samples = int(smoothing_window_ms / 1000 * fs)
    envelope_smooth = np.convolve(envelope, 
                                   np.ones(window_samples)/window_samples, 
                                   mode='same')
    
    # Normalize
    envelope_smooth = envelope_smooth / np.max(envelope_smooth)
    
    return envelope_smooth


# ============================================================================
# STEP 3: PEAK DETECTION
# ============================================================================

def detect_heartbeats(envelope, fs, min_bpm=150, max_bpm=200, 
                      threshold=0.15, prominence=0.1):
    """
    Detect heartbeats from the signal envelope.
    
    WHY: Peak detection is the critical step for identifying cardiac cycles.
    We use scipy's find_peaks with multiple constraints:
    
    1. distance: Ensures minimum time between peaks (prevents double-counting)
    2. height: Amplitude threshold to filter noise
    3. prominence: Ensures peaks are truly local maxima
    
    For 158-192 bpm, R-R interval is 0.31-0.38s, so we set:
    - min_distance for 200 bpm (0.30s) - catches fast rates
    - max validation for 100 bpm (0.60s) - filters artifacts
    """
    # Calculate minimum distance between peaks
    min_distance = int((60 / max_bpm) * fs)
    max_distance = int((60 / min_bpm) * fs)
    
    print(f"\nPeak Detection Parameters:")
    print(f"  → Min distance: {min_distance} samples ({60/max_bpm:.3f}s)")
    print(f"  → Max distance: {max_distance} samples ({60/min_bpm:.3f}s)")
    print(f"  → Threshold: {threshold}")
    print(f"  → Prominence: {prominence}")
    
    # Find peaks
    peaks, properties = find_peaks(envelope, 
                                    distance=min_distance,
                                    height=threshold,
                                    prominence=prominence)
    
    peak_times = peaks / fs
    print(f"  → Detected {len(peaks)} peaks")
    
    return peaks, peak_times, properties


def validate_rr_intervals(peak_times, min_rr=0.25, max_rr=0.60):
    """
    Filter out physiologically implausible R-R intervals.
    
    WHY: Not all detected peaks are true heartbeats. Artifacts, noise, or
    missed beats can create invalid intervals. We filter to the physiological
    range of 100-240 bpm (0.25-0.60s).
    """
    rr_intervals = np.diff(peak_times)
    
    # Create mask for valid intervals
    valid_mask = (rr_intervals >= min_rr) & (rr_intervals <= max_rr)
    
    valid_rr = rr_intervals[valid_mask]
    valid_rr_ms = valid_rr * 1000
    
    print(f"\nR-R Interval Validation:")
    print(f"  → Total intervals: {len(rr_intervals)}")
    print(f"  → Valid intervals: {len(valid_rr)}")
    print(f"  → Rejected: {len(rr_intervals) - len(valid_rr)}")
    
    return valid_rr, valid_rr_ms, valid_mask


# ============================================================================
# STEP 4: HRV CALCULATIONS
# ============================================================================

def calculate_time_domain_hrv(rr_intervals_ms):
    """
    Calculate time-domain HRV metrics.
    
    WHY: Time-domain metrics are the most straightforward HRV measures:
    
    - SDNN: Standard deviation of NN (normal-to-normal) intervals.
      Reflects overall HRV, influenced by both sympathetic and parasympathetic.
    
    - RMSSD: Root mean square of successive differences.
      Primarily reflects short-term, high-frequency variations (parasympathetic).
    
    - pNN50: Percentage of intervals differing by >50ms.
      Another parasympathetic indicator.
    """
    # SDNN - Standard deviation of all R-R intervals
    sdnn = np.std(rr_intervals_ms)
    
    # RMSSD - Root mean square of successive differences
    successive_diffs = np.diff(rr_intervals_ms)
    rmssd = np.sqrt(np.mean(successive_diffs**2))
    
    # NN50 - Number of intervals differing by >50ms
    nn50 = np.sum(np.abs(successive_diffs) > 50)
    pnn50 = (nn50 / len(successive_diffs)) * 100 if len(successive_diffs) > 0 else 0
    
    # Coefficient of variation
    cv = (sdnn / np.mean(rr_intervals_ms)) * 100
    
    return {
        'SDNN': sdnn,
        'RMSSD': rmssd,
        'NN50': nn50,
        'pNN50': pnn50,
        'CV': cv,
        'mean_rr': np.mean(rr_intervals_ms),
        'std_rr': np.std(rr_intervals_ms)
    }


def calculate_frequency_domain_hrv(peak_times, rr_intervals_ms, valid_mask):
    """
    Calculate frequency-domain HRV using Lomb-Scargle periodogram.
    
    WHY: Frequency analysis reveals the autonomic nervous system contributions:
    
    - VLF (0.003-0.04 Hz): Very low frequency, long-term regulation
    - LF (0.04-0.15 Hz): Low frequency, sympathetic + parasympathetic
    - HF (0.15-0.4 Hz): High frequency, primarily parasympathetic (vagal)
    - LF/HF ratio: Balance between sympathetic and parasympathetic
    
    We use Lomb-Scargle instead of FFT because R-R intervals are unevenly
    sampled in time (the time between samples varies).
    """
    # Use valid peak times and intervals
    valid_times = peak_times[:-1][valid_mask]
    
    # Frequency range for analysis
    freqs = np.linspace(0.001, 0.5, 1000)
    angular_freqs = 2 * np.pi * freqs
    
    # Lomb-Scargle periodogram
    periodogram = lombscargle(valid_times, rr_intervals_ms, angular_freqs, normalize=True)
    
    # Define frequency bands
    ulf_mask = freqs < 0.003
    vlf_mask = (freqs >= 0.003) & (freqs < 0.04)
    lf_mask = (freqs >= 0.04) & (freqs < 0.15)
    hf_mask = (freqs >= 0.15) & (freqs < 0.4)
    
    # Calculate power in each band
    ulf_power = np.trapz(periodogram[ulf_mask], freqs[ulf_mask]) if np.any(ulf_mask) else 0
    vlf_power = np.trapz(periodogram[vlf_mask], freqs[vlf_mask]) if np.any(vlf_mask) else 0
    lf_power = np.trapz(periodogram[lf_mask], freqs[lf_mask]) if np.any(lf_mask) else 0
    hf_power = np.trapz(periodogram[hf_mask], freqs[hf_mask]) if np.any(hf_mask) else 0
    
    total_power = ulf_power + vlf_power + lf_power + hf_power
    lf_hf_ratio = lf_power / hf_power if hf_power > 0 else 0
    
    return {
        'frequencies': freqs,
        'periodogram': periodogram,
        'ULF_power': ulf_power,
        'VLF_power': vlf_power,
        'LF_power': lf_power,
        'HF_power': hf_power,
        'total_power': total_power,
        'LF_HF_ratio': lf_hf_ratio
    }


# ============================================================================
# STEP 5: VISUALIZATION
# ============================================================================

def create_comprehensive_plots(sample_rate, time, audio_data, filtered_signal,
                               envelope, peaks, peak_times, valid_rr, valid_rr_ms,
                               valid_mask, hrv_time, hrv_freq, output_dir='./'):
    """
    Create comprehensive visualization of PCG analysis.
    
    This function generates multiple figures showing the complete analysis pipeline.
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    colors = {
        'primary': '#2E86AB',
        'secondary': '#A23B72',
        'accent': '#F18F01',
        'success': '#C73E1D',
        'neutral': '#6B7280'
    }
    
    duration = len(audio_data) / sample_rate
    
    # =====================================================================
    # FIGURE 1: Signal Processing
    # =====================================================================
    fig1, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Raw signal (first 5s)
    ax = axes[0, 0]
    plot_samples = int(5 * sample_rate)
    ax.plot(time[:plot_samples], audio_data[:plot_samples], 
            color=colors['primary'], linewidth=0.5)
    ax.set_title('1. Raw PCG Signal (First 5s)', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, alpha=0.3)
    
    # Filtered signal
    ax = axes[0, 1]
    ax.plot(time[:plot_samples], filtered_signal[:plot_samples],
            color=colors['secondary'], linewidth=0.5)
    ax.set_title('2. Bandpass Filtered (25-150 Hz)', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid(True, alpha=0.3)
    
    # Envelope with peaks (first 10s)
    ax = axes[1, 0]
    plot_samples = int(10 * sample_rate)
    peaks_in_range = peaks[peaks < plot_samples]
    ax.plot(time[:plot_samples], envelope[:plot_samples],
            color=colors['primary'], linewidth=1.5)
    ax.scatter(peaks_in_range/sample_rate, envelope[peaks_in_range],
               color=colors['success'], s=30, zorder=5)
    ax.axhline(y=PEAK_THRESHOLD, color=colors['accent'], linestyle='--', alpha=0.7)
    ax.set_title('3. Envelope with Detected Peaks', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Normalized Amplitude')
    ax.grid(True, alpha=0.3)
    
    # Full recording
    ax = axes[1, 1]
    ax.plot(time, envelope, color=colors['primary'], linewidth=0.5, alpha=0.7)
    ax.scatter(peak_times, envelope[peaks], color=colors['success'], s=5)
    ax.set_title(f'4. Full Recording ({len(peaks)} peaks)', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Normalized Amplitude')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/pcg_analysis_signals.png', dpi=DPI, facecolor='white')
    plt.close()
    
    # =====================================================================
    # FIGURE 2: Heart Rate Analysis
    # =====================================================================
    fig2, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Calculate instantaneous HR
    instantaneous_hr = 60 / valid_rr
    hr_time = peak_times[:-1][valid_mask] + valid_rr / 2
    
    # Heart rate over time
    ax = axes[0, 0]
    ax.plot(hr_time, instantaneous_hr, color=colors['primary'], 
            linewidth=1.5, marker='o', markersize=3)
    ax.axhline(y=np.mean(instantaneous_hr), color=colors['accent'], 
               linestyle='--', label=f'Mean: {np.mean(instantaneous_hr):.1f} bpm')
    ax.fill_between(hr_time, instantaneous_hr, alpha=0.3, color=colors['primary'])
    ax.set_title('5. Heart Rate Over Time', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Heart Rate (bpm)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # R-R Tachogram
    ax = axes[0, 1]
    ax.plot(peak_times[:-1][valid_mask], valid_rr_ms, 
            color=colors['secondary'], linewidth=1.5, marker='o', markersize=3)
    ax.axhline(y=np.mean(valid_rr_ms), color=colors['accent'], 
               linestyle='--', label=f'Mean: {np.mean(valid_rr_ms):.1f} ms')
    ax.fill_between(peak_times[:-1][valid_mask], valid_rr_ms, alpha=0.3, color=colors['secondary'])
    ax.set_title('6. R-R Interval Tachogram', fontweight='bold')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('R-R Interval (ms)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # R-R Histogram
    ax = axes[1, 0]
    ax.hist(valid_rr_ms, bins=25, color=colors['primary'], 
            edgecolor='white', alpha=0.8)
    ax.axvline(x=np.mean(valid_rr_ms), color=colors['success'], 
               linestyle='-', linewidth=2, label=f'Mean: {np.mean(valid_rr_ms):.1f} ms')
    ax.set_title('7. R-R Interval Distribution', fontweight='bold')
    ax.set_xlabel('R-R Interval (ms)')
    ax.set_ylabel('Frequency')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    # Poincaré plot
    ax = axes[1, 1]
    rr_n = valid_rr_ms[:-1]
    rr_n1 = valid_rr_ms[1:]
    ax.scatter(rr_n, rr_n1, c=colors['secondary'], alpha=0.6, s=20)
    min_val = min(np.min(rr_n), np.min(rr_n1))
    max_val = max(np.max(rr_n), np.max(rr_n1))
    ax.plot([min_val, max_val], [min_val, max_val], 'k--', alpha=0.5)
    ax.set_title('8. Poincaré Plot (RR(n) vs RR(n+1))', fontweight='bold')
    ax.set_xlabel('R-R Interval n (ms)')
    ax.set_ylabel('R-R Interval n+1 (ms)')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/pcg_analysis_hr.png', dpi=DPI, facecolor='white')
    plt.close()
    
    # =====================================================================
    # FIGURE 3: HRV Frequency Domain
    # =====================================================================
    fig3, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Lomb-Scargle periodogram
    ax = axes[0]
    freqs = hrv_freq['frequencies']
    periodogram = hrv_freq['periodogram']
    ax.plot(freqs, periodogram, color=colors['primary'], linewidth=1.5)
    ax.fill_between(freqs, periodogram, alpha=0.3, color=colors['primary'])
    ax.axvspan(0.003, 0.04, alpha=0.2, color='green', label='VLF')
    ax.axvspan(0.04, 0.15, alpha=0.2, color='blue', label='LF')
    ax.axvspan(0.15, 0.4, alpha=0.2, color='red', label='HF')
    ax.set_title('9. HRV Frequency Domain', fontweight='bold')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power Spectral Density')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.5)
    
    # Power distribution pie chart
    ax = axes[1]
    powers = [hrv_freq['VLF_power'], hrv_freq['LF_power'], hrv_freq['HF_power']]
    labels = [f'VLF\n{hrv_freq["VLF_power"]:.4f}', 
              f'LF\n{hrv_freq["LF_power"]:.4f}',
              f'HF\n{hrv_freq["HF_power"]:.4f}']
    colors_pie = ['#22C55E', '#3B82F6', '#EF4444']
    ax.pie(powers, labels=labels, autopct='%1.1f%%', colors=colors_pie,
           explode=(0.02, 0.02, 0.02))
    ax.set_title('10. Power Distribution by Band', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/pcg_analysis_hrv_freq.png', dpi=DPI, facecolor='white')
    plt.close()
    
    print(f"\nPlots saved to {output_dir}/")


# ============================================================================
# MAIN ANALYSIS PIPELINE
# ============================================================================

def analyze_pcg(file_path, output_dir='./pcg_output/'):
    """
    Main function to run complete PCG analysis.
    """
    print("=" * 60)
    print("           PCG (PHONOCARDIOGRAM) ANALYSIS")
    print("=" * 60)
    
    # Step 1: Load data
    print("\n" + "-" * 40)
    print("STEP 1: Loading PCG Data")
    print("-" * 40)
    sample_rate, audio_data, time, duration = load_pcg_data(file_path)
    
    # Step 2: Preprocessing
    print("\n" + "-" * 40)
    print("STEP 2: Signal Preprocessing")
    print("-" * 40)
    filtered_signal = apply_bandpass_filter(audio_data, LOWCUT, HIGHCUT, 
                                            sample_rate, FILTER_ORDER)
    envelope = extract_envelope(filtered_signal, sample_rate)
    print("  → Bandpass filter applied (25-150 Hz)")
    print("  → Envelope extracted using Hilbert transform")
    
    # Step 3: Peak detection
    print("\n" + "-" * 40)
    print("STEP 3: Peak Detection")
    print("-" * 40)
    peaks, peak_times, properties = detect_heartbeats(
        envelope, sample_rate, MIN_BPM, MAX_BPM, 
        PEAK_THRESHOLD, PEAK_PROMINENCE
    )
    
    # Step 4: R-R interval validation
    print("\n" + "-" * 40)
    print("STEP 4: R-R Interval Validation")
    print("-" * 40)
    valid_rr, valid_rr_ms, valid_mask = validate_rr_intervals(peak_times)
    
    # Step 5: Calculate HRV metrics
    print("\n" + "-" * 40)
    print("STEP 5: HRV Analysis")
    print("-" * 40)
    
    # Time domain
    hrv_time = calculate_time_domain_hrv(valid_rr_ms)
    print(f"\nTime-Domain HRV:")
    print(f"  → SDNN: {hrv_time['SDNN']:.2f} ms")
    print(f"  → RMSSD: {hrv_time['RMSSD']:.2f} ms")
    print(f"  → pNN50: {hrv_time['pNN50']:.2f}%")
    print(f"  → Mean R-R: {hrv_time['mean_rr']:.1f} ms")
    
    # Frequency domain
    hrv_freq = calculate_frequency_domain_hrv(peak_times, valid_rr_ms, valid_mask)
    print(f"\nFrequency-Domain HRV:")
    print(f"  → VLF Power: {hrv_freq['VLF_power']:.4f} ms²")
    print(f"  → LF Power: {hrv_freq['LF_power']:.4f} ms²")
    print(f"  → HF Power: {hrv_freq['HF_power']:.4f} ms²")
    print(f"  → LF/HF Ratio: {hrv_freq['LF_HF_ratio']:.2f}")
    
    # Step 6: Calculate heart rate statistics
    instantaneous_hr = 60 / valid_rr
    print(f"\nHeart Rate Statistics:")
    print(f"  → Mean HR: {np.mean(instantaneous_hr):.1f} bpm")
    print(f"  → HR Range: {np.min(instantaneous_hr):.1f} - {np.max(instantaneous_hr):.1f} bpm")
    print(f"  → HR Std Dev: {np.std(instantaneous_hr):.1f} bpm")
    
    # Step 7: Create visualizations
    print("\n" + "-" * 40)
    print("STEP 6: Generating Visualizations")
    print("-" * 40)
    create_comprehensive_plots(sample_rate, time, audio_data, filtered_signal,
                               envelope, peaks, peak_times, valid_rr, valid_rr_ms,
                               valid_mask, hrv_time, hrv_freq, output_dir)
    
    # Final summary
    print("\n" + "=" * 60)
    print("              ANALYSIS COMPLETE")
    print("=" * 60)
    
    return {
        'sample_rate': sample_rate,
        'duration': duration,
        'num_beats': len(peaks),
        'mean_hr': np.mean(instantaneous_hr),
        'hr_std': np.std(instantaneous_hr),
        'hrv_time': hrv_time,
        'hrv_freq': hrv_freq
    }


# ============================================================================
# RUN ANALYSIS
# ============================================================================

if __name__ == "__main__":
    # Replace with your file path
    FILE_PATH = "运动后超激烈的心跳声（158~192bpm）评论区有心率分析.wav"
    
    results = analyze_pcg(FILE_PATH)
    
    print("\nSummary:")
    print(f"  Mean Heart Rate: {results['mean_hr']:.1f} bpm")
    print(f"  HRV (SDNN): {results['hrv_time']['SDNN']:.2f} ms")
    print(f"  LF/HF Ratio: {results['hrv_freq']['LF_HF_ratio']:.2f}")