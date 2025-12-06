import os
import logging
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
import librosa

try:
    from pydub import AudioSegment
except ImportError:
    logging.warning("Pydub library not found. Install with 'pip install pydub'.")
    AudioSegment = None

try:
    import pyPCG
    import pyPCG.preprocessing as preproc
    PYPCG_AVAILABLE = True
except ImportError:
    logging.warning("pyPCG-toolbox not installed. Install with: pip install pyPCG-toolbox")
    PYPCG_AVAILABLE = False
    preproc = None


def convert_to_wav(file_path: str, target_path: str) -> bool:
    """Converts a given audio file to WAV format."""
    if not AudioSegment:
        raise ImportError("Pydub/FFmpeg is required for audio conversion.")

    logging.info(f"Converting {os.path.basename(file_path)} to WAV format...")
    try:
        sound = AudioSegment.from_file(file_path)
        sound = sound.set_channels(1)
        sound.export(target_path, format="wav")
        return True
    except Exception as e:
        logging.error(f"Could not convert file {file_path}. Error: {e}")
        return False


def _apply_pypcg_denoising(audio_data: np.ndarray, sample_rate: int, params: Dict) -> np.ndarray:
    """Apply pyPCG denoising with tunable strength."""
    if params.get("denoising_method") is None or not PYPCG_AVAILABLE:
        return audio_data

    try:
        sig = pyPCG.pcg_signal(audio_data, sample_rate)
        method = params["denoising_method"]

        if method.startswith("wavelet"):
            import pywt

            wt_family = params.get("wt_family", "coif4")
            wt_level = params.get("wt_level", 5)

            coeffs = pywt.wavedec(sig.data, wt_family, level=wt_level)

            if method == "wavelet_auto":
                thresholded_coeffs = []
                for i, coeff in enumerate(coeffs):
                    if i == 0:
                        thresholded_coeffs.append(coeff)
                        continue

                    mad = np.median(np.abs(coeff - np.median(coeff)))
                    sigma = mad / 0.6745
                    tau = sigma * np.sqrt(2) * params.get("wavelet_threshold_multiplier", 1.0)

                    thresholded_coeffs.append(pywt.threshold(coeff, tau, mode="soft"))
            else:  # wavelet_manual
                manual_th = params.get("wavelet_threshold", 0.2)
                thresholded_coeffs = [
                    coeff if i == 0 else pywt.threshold(coeff, manual_th * np.max(np.abs(coeff)))
                    for i, coeff in enumerate(coeffs)
                ]

            denoised_data = pywt.waverec(thresholded_coeffs, wt_family)
            logging.info(
                "✓ Applied wavelet denoising (family=%s, level=%s, multiplier=%s)",
                wt_family,
                wt_level,
                params.get("wavelet_threshold_multiplier", 1.0),
            )
            return denoised_data

        elif method == "emd_savgol":
            denoised = preproc.emd_denoise_savgol(
                sig, window=params.get("emd_window", 10), poly=params.get("emd_poly", 3)
            )
            logging.info(
                "✓ Applied EMD denoising (window=%s, poly=%s)",
                params.get("emd_window"),
                params.get("emd_poly"),
            )
            return denoised.data

        else:
            logging.warning("Unknown denoising method: %s", method)
            return audio_data

    except ImportError as e:
        logging.error("❌ pyPCG-toolbox not installed. Install with: pip install pyPCG-toolbox")
        logging.error("Import error: %s", e)
        return audio_data
    except Exception as e:
        logging.error("❌ Denoising failed: %s", e)
        return audio_data


def preprocess_audio(
    file_path: str, params: Dict, output_directory: str, output_options: Optional[Dict] = None
) -> Tuple[np.ndarray, int]:
    if output_options is None:
        output_options = {
            "html": True,
            "csv": True,
            "summary": True,
            "debug": True,
            "settings": True,
            "filtered_wav": True,
        }

    save_debug_file = params["save_filtered_wav"] and output_options.get("filtered_wav", True)
    target_sample_rate = 500
    try:
        audio_downsampled, new_sample_rate = librosa.load(file_path, sr=target_sample_rate, mono=True)
    except Exception as e:
        logging.error("Librosa failed to load file: %s", e)
        raise

    audio_downsampled = _apply_pypcg_denoising(audio_downsampled, new_sample_rate, params)

    lowcut, highcut = 20, 150
    nyquist = 0.5 * new_sample_rate
    low, high = lowcut / nyquist, highcut / nyquist

    if high >= 1.0:
        raise ValueError(f"Cannot create a {highcut}Hz filter. The sample rate of {new_sample_rate}Hz is too low.")

    b, a = butter(2, [low, high], btype="band")
    audio_filtered = filtfilt(b, a, audio_downsampled)

    if save_debug_file:
        base_name = os.path.basename(os.path.splitext(file_path)[0])
        debug_path = os.path.join(output_directory, f"{base_name}_filtered_debug.wav")
        normalized_audio = np.int16(audio_filtered / np.max(np.abs(audio_filtered)) * 32767)
        wavfile.write(debug_path, new_sample_rate, normalized_audio)
        logging.info("Saved filtered audio WAV file as requested.")
    elif params["save_filtered_wav"] and not output_options.get("filtered_wav", True):
        logging.info("Skipping filtered audio WAV generation as requested.")

    audio_abs = np.abs(audio_filtered)
    window_size = new_sample_rate // 10
    audio_envelope = pd.Series(audio_abs).rolling(window=window_size, min_periods=1, center=True).mean().values

    return audio_envelope, new_sample_rate

