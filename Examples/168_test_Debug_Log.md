# Chronological Debug Log for 168_test.wav
Analysis performed on: 2025-12-09 17:47:03

## Time: `0.1040s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.031, S2/S1=22.86 (Expected max 1.48 at 126 BPM)
    - Contractility Penalty: -5.06 (S2 too prominent for BPM; prominence ratio 22.86 > expected 1.48) -> 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Validated Lone S1: First beat (no prior rhythm to compare).
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `0.1920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `0.2900s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.027, S2/S1=0.87 (Expected max 1.48 at 126 BPM)
    - Contractility Neutral: prominence ratio 0.87 within expected range for 126 BPM, confidence unchanged
    - Interval penalty by 0.31 (Interval 0.388s > Max 0.333s)
    - Final Score: 0.29 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.00: interval 0.186s vs expected 0.476s (deviation 61%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 19.62x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.00 x 0.65) + (Amplitude 1.00 x 0.35) = 0.350
    - Outcome: Rejected Lone S1 (score 0.35 < threshold 0.50)
- **Raw Amp**: `0.032`
- **Noise Floor**: `0.001`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `0.5500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `0.6780s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.026, S2/S1=0.97 (Expected max 1.48 at 126 BPM)
    - Contractility Neutral: prominence ratio 0.97 within expected range for 126 BPM, confidence unchanged
    - Interval penalty by 0.20 (Interval 0.368s > Max 0.333s)
    - Final Score: 0.40 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.71: interval 0.574s vs expected 0.476s (deviation 21%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 17.21x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.71 x 0.65) + (Amplitude 1.00 x 0.35) = 0.812
    - Outcome: Validated Lone S1 (score 0.81 >= threshold 0.50)
- **Raw Amp**: `0.028`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.3`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `0.9020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.3`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `1.0460s`
**Lone S1.**
- S1-S2 pairing decision:
    - Impossible: S1-S2 interval 0.104s < min 0.110s (implies 288 BPM vs assumed 125 BPM)
- Lone S1 decision:
    - Rhythm Fit 0.67: interval 0.368s vs expected 0.480s (deviation 23%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 1.05x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.67 x 0.65) + (Amplitude 1.00 x 0.35) = 0.783
    - Outcome: Validated Lone S1 (score 0.78 >= threshold 0.50)
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `126.6`


## Time: `1.1260s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `126.6`


## Time: `1.1500s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.025, S2/S1=18.16 (Expected max 1.48 at 126 BPM)
    - Contractility Penalty: -3.95 (S2 too prominent for BPM; prominence ratio 18.16 > expected 1.48) -> 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.00: interval 0.104s vs expected 0.476s (deviation 78%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.15: strength ratio 0.15x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.00 x 0.65) + (Amplitude 0.15 x 0.35) = 0.053
    - Outcome: Rejected Lone S1 (score 0.05 < threshold 0.50)
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `126.6`


## Time: `1.2720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `126.6`


## Time: `1.4180s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.002, S2/S1=0.07 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 1.418s (amp 0.029), key col 0.003
    -       Left trough: idx=636 (1.272s), amp=0.001
    -       Right trough: idx=747 (1.494s), amp=0.003
    - S2: prom 0.002, peak @ 1.536s (amp 0.005), key col 0.003
    -       Left trough: idx=747 (1.494s), amp=0.003
    -       Right trough: idx=825 (1.650s), amp=0.001
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.2`
- **Long-Term BPM (Belief)**: `128.3`


## Time: `1.4940s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.2`
- **Long-Term BPM (Belief)**: `128.3`


## Time: `1.5360s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.002, S2/S1=0.07 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 1.418s (amp 0.029), key col 0.003
    -       Left trough: idx=636 (1.272s), amp=0.001
    -       Right trough: idx=747 (1.494s), amp=0.003
    - S2: prom 0.002, peak @ 1.536s (amp 0.005), key col 0.003
    -       Left trough: idx=747 (1.494s), amp=0.003
    -       Right trough: idx=825 (1.650s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.2`
- **Long-Term BPM (Belief)**: `128.3`


## Time: `1.6500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.2`
- **Long-Term BPM (Belief)**: `128.3`


## Time: `1.7800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.003, S2/S1=0.09 (Expected max 1.43 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.09) -> 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 1.780s (amp 0.034), key col 0.001
    -       Left trough: idx=825 (1.650s), amp=0.001
    -       Right trough: idx=1006 (2.012s), amp=0.001
    - S2: prom 0.003, peak @ 1.896s (amp 0.004), key col 0.001
    -       Left trough: idx=825 (1.650s), amp=0.001
    -       Right trough: idx=1006 (2.012s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.5`
- **Long-Term BPM (Belief)**: `129.4`


## Time: `1.8960s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.003, S2/S1=0.09 (Expected max 1.43 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.09) -> 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 1.780s (amp 0.034), key col 0.001
    -       Left trough: idx=825 (1.650s), amp=0.001
    -       Right trough: idx=1006 (2.012s), amp=0.001
    - S2: prom 0.003, peak @ 1.896s (amp 0.004), key col 0.001
    -       Left trough: idx=825 (1.650s), amp=0.001
    -       Right trough: idx=1006 (2.012s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.5`
- **Long-Term BPM (Belief)**: `129.4`


## Time: `2.0120s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.5`
- **Long-Term BPM (Belief)**: `129.4`


## Time: `2.1460s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.035, S2/S1=0.97 (Expected max 1.41 at 129 BPM)
    - Contractility Neutral: prominence ratio 0.97 within expected range for 129 BPM, confidence unchanged
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.60
    - Interval penalty by 0.25 (Interval 0.368s > Max 0.325s)
    - Final Score: 0.35 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.70: interval 0.366s vs expected 0.464s (deviation 21%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 1.09x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.70 x 0.65) + (Amplitude 1.00 x 0.35) = 0.807
    - Outcome: Validated Lone S1 (score 0.81 >= threshold 0.50)
- **Raw Amp**: `0.037`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `159.0`
- **Long-Term BPM (Belief)**: `130.5`


## Time: `2.3760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `159.0`
- **Long-Term BPM (Belief)**: `130.5`


## Time: `2.5140s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.031, S2/S1=0.88 (Expected max 1.39 at 130 BPM)
    - Contractility Neutral: prominence ratio 0.88 within expected range for 130 BPM, confidence unchanged
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.60
    - Interval penalty by 0.23 (Interval 0.362s > Max 0.322s)
    - Final Score: 0.37 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.72: interval 0.368s vs expected 0.460s (deviation 20%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.97: strength ratio 0.97x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.72 x 0.65) + (Amplitude 0.97 x 0.35) = 0.809
    - Outcome: Validated Lone S1 (score 0.81 >= threshold 0.50)
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `159.6`
- **Long-Term BPM (Belief)**: `131.6`


## Time: `2.7280s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `159.6`
- **Long-Term BPM (Belief)**: `131.6`


## Time: `2.8760s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.024, S2/S1=0.76 (Expected max 1.37 at 132 BPM)
    - Contractility Neutral: prominence ratio 0.76 within expected range for 132 BPM, confidence unchanged
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.60
    - Interval penalty by 0.25 (Interval 0.362s > Max 0.319s)
    - Final Score: 0.35 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.71: interval 0.362s vs expected 0.456s (deviation 21%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.89: strength ratio 0.89x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.71 x 0.65) + (Amplitude 0.89 x 0.35) = 0.772
    - Outcome: Validated Lone S1 (score 0.77 >= threshold 0.50)
- **Raw Amp**: `0.032`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.0`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `3.0960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.0`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `3.2380s`
**Lone S1.**
- S1-S2 pairing decision:
    - Impossible: S1-S2 interval 0.100s < min 0.104s (implies 300 BPM vs assumed 133 BPM)
- Lone S1 decision:
    - Rhythm Fit 0.72: interval 0.362s vs expected 0.452s (deviation 20%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.78: strength ratio 0.78x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.72 x 0.65) + (Amplitude 0.78 x 0.35) = 0.742
    - Outcome: Validated Lone S1 (score 0.74 >= threshold 0.50)
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.6`
- **Long-Term BPM (Belief)**: `134.3`


## Time: `3.3380s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.003, S2=0.026, S2/S1=8.29 (Expected max 1.32 at 134 BPM)
    - Contractility Penalty: -1.84 (S2 too prominent for BPM; prominence ratio 8.29 > expected 1.32) -> 0.00
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.00: interval 0.100s vs expected 0.449s (deviation 78%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.17: strength ratio 0.17x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.00 x 0.65) + (Amplitude 0.17 x 0.35) = 0.058
    - Outcome: Rejected Lone S1 (score 0.06 < threshold 0.50)
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.6`
- **Long-Term BPM (Belief)**: `134.3`


## Time: `3.5080s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.6`
- **Long-Term BPM (Belief)**: `134.3`


## Time: `3.6080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.002, S2/S1=0.07 (Expected max 1.30 at 135 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 135 BPM; prominence ratio 0.07) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 3.608s (amp 0.030), key col 0.003
    -       Left trough: idx=1754 (3.508s), amp=0.002
    -       Right trough: idx=1841 (3.682s), amp=0.003
    - S2: prom 0.002, peak @ 3.734s (amp 0.005), key col 0.003
    -       Left trough: idx=1841 (3.682s), amp=0.003
    -       Right trough: idx=1905 (3.810s), amp=0.002
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.9`
- **Long-Term BPM (Belief)**: `136.0`


## Time: `3.6820s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.9`
- **Long-Term BPM (Belief)**: `136.0`


## Time: `3.7340s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.002, S2/S1=0.07 (Expected max 1.30 at 135 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 135 BPM; prominence ratio 0.07) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 3.608s (amp 0.030), key col 0.003
    -       Left trough: idx=1754 (3.508s), amp=0.002
    -       Right trough: idx=1841 (3.682s), amp=0.003
    - S2: prom 0.002, peak @ 3.734s (amp 0.005), key col 0.003
    -       Left trough: idx=1841 (3.682s), amp=0.003
    -       Right trough: idx=1905 (3.810s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.9`
- **Long-Term BPM (Belief)**: `136.0`


## Time: `3.8100s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.9`
- **Long-Term BPM (Belief)**: `136.0`


## Time: `3.9620s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.001, S2/S1=0.04 (Expected max 1.28 at 136 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 136 BPM; prominence ratio 0.04) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 3.962s (amp 0.040), key col 0.004
    -       Left trough: idx=1905 (3.810s), amp=0.002
    -       Right trough: idx=2024 (4.048s), amp=0.004
    - S2: prom 0.001, peak @ 4.144s (amp 0.005), key col 0.004
    -       Left trough: idx=2024 (4.048s), amp=0.004
    -       Right trough: idx=2114 (4.228s), amp=0.003
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `137.0`


## Time: `4.0480s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `137.0`


## Time: `4.1440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.001, S2/S1=0.04 (Expected max 1.28 at 136 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 136 BPM; prominence ratio 0.04) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 3.962s (amp 0.040), key col 0.004
    -       Left trough: idx=1905 (3.810s), amp=0.002
    -       Right trough: idx=2024 (4.048s), amp=0.004
    - S2: prom 0.001, peak @ 4.144s (amp 0.005), key col 0.004
    -       Left trough: idx=2024 (4.048s), amp=0.004
    -       Right trough: idx=2114 (4.228s), amp=0.003
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `137.0`


## Time: `4.2280s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `137.0`


## Time: `4.3280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.001, S2/S1=0.03 (Expected max 1.26 at 137 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 137 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 4.328s (amp 0.041), key col 0.003
    -       Left trough: idx=2114 (4.228s), amp=0.003
    -       Right trough: idx=2204 (4.408s), amp=0.003
    - S2: prom 0.001, peak @ 4.460s (amp 0.004), key col 0.003
    -       Left trough: idx=2204 (4.408s), amp=0.003
    -       Right trough: idx=2281 (4.562s), amp=0.001
- **Raw Amp**: `0.041`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `4.4080s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `4.4600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.001, S2/S1=0.03 (Expected max 1.26 at 137 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 137 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 4.328s (amp 0.041), key col 0.003
    -       Left trough: idx=2114 (4.228s), amp=0.003
    -       Right trough: idx=2204 (4.408s), amp=0.003
    - S2: prom 0.001, peak @ 4.460s (amp 0.004), key col 0.003
    -       Left trough: idx=2204 (4.408s), amp=0.003
    -       Right trough: idx=2281 (4.562s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `4.5620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.6`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `4.6880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.050, S2=0.002, S2/S1=0.04 (Expected max 1.24 at 138 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 138 BPM; prominence ratio 0.04) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.050, peak @ 4.688s (amp 0.052), key col 0.002
    -       Left trough: idx=2281 (4.562s), amp=0.001
    -       Right trough: idx=2389 (4.778s), amp=0.002
    - S2: prom 0.002, peak @ 4.826s (amp 0.004), key col 0.002
    -       Left trough: idx=2389 (4.778s), amp=0.002
    -       Right trough: idx=2475 (4.950s), amp=0.001
- **Raw Amp**: `0.052`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.7`
- **Long-Term BPM (Belief)**: `139.2`


## Time: `4.7780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.7`
- **Long-Term BPM (Belief)**: `139.2`


## Time: `4.8260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.050, S2=0.002, S2/S1=0.04 (Expected max 1.24 at 138 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 138 BPM; prominence ratio 0.04) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.050, peak @ 4.688s (amp 0.052), key col 0.002
    -       Left trough: idx=2281 (4.562s), amp=0.001
    -       Right trough: idx=2389 (4.778s), amp=0.002
    - S2: prom 0.002, peak @ 4.826s (amp 0.004), key col 0.002
    -       Left trough: idx=2389 (4.778s), amp=0.002
    -       Right trough: idx=2475 (4.950s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.7`
- **Long-Term BPM (Belief)**: `139.2`


## Time: `4.9500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.7`
- **Long-Term BPM (Belief)**: `139.2`


## Time: `5.0520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.002, S2/S1=0.03 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 5.052s (amp 0.054), key col 0.001
    -       Left trough: idx=2475 (4.950s), amp=0.001
    -       Right trough: idx=2569 (5.138s), amp=0.001
    - S2: prom 0.002, peak @ 5.228s (amp 0.003), key col 0.001
    -       Left trough: idx=2569 (5.138s), amp=0.001
    -       Right trough: idx=2640 (5.280s), amp=0.001
- **Raw Amp**: `0.054`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `167.0`
- **Long-Term BPM (Belief)**: `140.3`


## Time: `5.1380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `167.0`
- **Long-Term BPM (Belief)**: `140.3`


## Time: `5.2280s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.002, S2/S1=0.03 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 5.052s (amp 0.054), key col 0.001
    -       Left trough: idx=2475 (4.950s), amp=0.001
    -       Right trough: idx=2569 (5.138s), amp=0.001
    - S2: prom 0.002, peak @ 5.228s (amp 0.003), key col 0.001
    -       Left trough: idx=2569 (5.138s), amp=0.001
    -       Right trough: idx=2640 (5.280s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `167.0`
- **Long-Term BPM (Belief)**: `140.3`


## Time: `5.2800s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `167.0`
- **Long-Term BPM (Belief)**: `140.3`


## Time: `5.4180s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 5.418s (amp 0.048), key col 0.001
    -       Left trough: idx=2640 (5.280s), amp=0.001
    -       Right trough: idx=2827 (5.654s), amp=0.001
    - S2: prom 0.001, peak @ 5.546s (amp 0.002), key col 0.001
    -       Left trough: idx=2640 (5.280s), amp=0.001
    -       Right trough: idx=2827 (5.654s), amp=0.001
- **Raw Amp**: `0.048`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `141.4`


## Time: `5.5460s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 5.418s (amp 0.048), key col 0.001
    -       Left trough: idx=2640 (5.280s), amp=0.001
    -       Right trough: idx=2827 (5.654s), amp=0.001
    - S2: prom 0.001, peak @ 5.546s (amp 0.002), key col 0.001
    -       Left trough: idx=2640 (5.280s), amp=0.001
    -       Right trough: idx=2827 (5.654s), amp=0.001
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `141.4`


## Time: `5.6540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `141.4`


## Time: `5.7780s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 141 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 141 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 5.778s (amp 0.043), key col 0.002
    -       Left trough: idx=2827 (5.654s), amp=0.001
    -       Right trough: idx=2928 (5.856s), amp=0.002
    - S2: prom 0.001, peak @ 5.880s (amp 0.003), key col 0.002
    -       Left trough: idx=2928 (5.856s), amp=0.002
    -       Right trough: idx=2998 (5.996s), amp=0.001
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `5.8560s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `5.8800s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 141 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 141 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 5.778s (amp 0.043), key col 0.002
    -       Left trough: idx=2827 (5.654s), amp=0.001
    -       Right trough: idx=2928 (5.856s), amp=0.002
    - S2: prom 0.001, peak @ 5.880s (amp 0.003), key col 0.002
    -       Left trough: idx=2928 (5.856s), amp=0.002
    -       Right trough: idx=2998 (5.996s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `5.9960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `6.1300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.002, S2/S1=0.06 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.06) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 6.130s (amp 0.042), key col 0.001
    -       Left trough: idx=2998 (5.996s), amp=0.001
    -       Right trough: idx=3181 (6.362s), amp=0.001
    - S2: prom 0.002, peak @ 6.240s (amp 0.004), key col 0.001
    -       Left trough: idx=2998 (5.996s), amp=0.001
    -       Right trough: idx=3181 (6.362s), amp=0.001
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `143.5`


## Time: `6.2400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.002, S2/S1=0.06 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.06) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 6.130s (amp 0.042), key col 0.001
    -       Left trough: idx=2998 (5.996s), amp=0.001
    -       Right trough: idx=3181 (6.362s), amp=0.001
    - S2: prom 0.002, peak @ 6.240s (amp 0.004), key col 0.001
    -       Left trough: idx=2998 (5.996s), amp=0.001
    -       Right trough: idx=3181 (6.362s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `143.5`


## Time: `6.3620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `143.5`


## Time: `6.4900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 144 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 144 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 6.490s (amp 0.045), key col 0.003
    -       Left trough: idx=3181 (6.362s), amp=0.001
    -       Right trough: idx=3283 (6.566s), amp=0.003
    - S2: prom 0.001, peak @ 6.614s (amp 0.004), key col 0.003
    -       Left trough: idx=3283 (6.566s), amp=0.003
    -       Right trough: idx=3357 (6.714s), amp=0.001
- **Raw Amp**: `0.045`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `144.6`


## Time: `6.5660s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `144.6`


## Time: `6.6140s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 144 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 144 BPM; prominence ratio 0.03) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 6.490s (amp 0.045), key col 0.003
    -       Left trough: idx=3181 (6.362s), amp=0.001
    -       Right trough: idx=3283 (6.566s), amp=0.003
    - S2: prom 0.001, peak @ 6.614s (amp 0.004), key col 0.003
    -       Left trough: idx=3283 (6.566s), amp=0.003
    -       Right trough: idx=3357 (6.714s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `144.6`


## Time: `6.7140s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `144.6`


## Time: `6.8520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.002, S2/S1=0.06 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.06) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 6.852s (amp 0.039), key col 0.002
    -       Left trough: idx=3357 (6.714s), amp=0.001
    -       Right trough: idx=3460 (6.920s), amp=0.002
    - S2: prom 0.002, peak @ 6.986s (amp 0.004), key col 0.002
    -       Left trough: idx=3460 (6.920s), amp=0.002
    -       Right trough: idx=3545 (7.090s), amp=0.001
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `145.7`


## Time: `6.9200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `145.7`


## Time: `6.9860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.002, S2/S1=0.06 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.06) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 6.852s (amp 0.039), key col 0.002
    -       Left trough: idx=3357 (6.714s), amp=0.001
    -       Right trough: idx=3460 (6.920s), amp=0.002
    - S2: prom 0.002, peak @ 6.986s (amp 0.004), key col 0.002
    -       Left trough: idx=3460 (6.920s), amp=0.002
    -       Right trough: idx=3545 (7.090s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `145.7`


## Time: `7.0900s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.3`
- **Long-Term BPM (Belief)**: `145.7`


## Time: `7.1880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.02) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 7.188s (amp 0.051), key col 0.002
    -       Left trough: idx=3545 (7.090s), amp=0.001
    -       Right trough: idx=3639 (7.278s), amp=0.002
    - S2: prom 0.001, peak @ 7.308s (amp 0.003), key col 0.002
    -       Left trough: idx=3639 (7.278s), amp=0.002
    -       Right trough: idx=3728 (7.456s), amp=0.001
- **Raw Amp**: `0.051`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `146.7`


## Time: `7.2780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `146.7`


## Time: `7.3080s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.02) -> 0.75
    - Stability Adjust: x1.00 (Pairing Ratio: 50%, Floor: 0.70) → 0.75
    - Final Score: 0.75 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 7.188s (amp 0.051), key col 0.002
    -       Left trough: idx=3545 (7.090s), amp=0.001
    -       Right trough: idx=3639 (7.278s), amp=0.002
    - S2: prom 0.001, peak @ 7.308s (amp 0.003), key col 0.002
    -       Left trough: idx=3639 (7.278s), amp=0.002
    -       Right trough: idx=3728 (7.456s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `146.7`


## Time: `7.4560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.1`
- **Long-Term BPM (Belief)**: `146.7`


## Time: `7.5760s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.16 (Pairing Ratio: 65%, Floor: 0.90) → 0.87
    - Final Score: 0.87 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 7.576s (amp 0.053), key col 0.002
    -       Left trough: idx=3728 (7.456s), amp=0.001
    -       Right trough: idx=3831 (7.662s), amp=0.002
    - S2: prom 0.001, peak @ 7.698s (amp 0.003), key col 0.002
    -       Left trough: idx=3831 (7.662s), amp=0.002
    -       Right trough: idx=3889 (7.778s), amp=0.002
- **Raw Amp**: `0.053`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.5`
- **Long-Term BPM (Belief)**: `147.1`


## Time: `7.6620s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.5`
- **Long-Term BPM (Belief)**: `147.1`


## Time: `7.6980s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.16 (Pairing Ratio: 65%, Floor: 0.90) → 0.87
    - Final Score: 0.87 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 7.576s (amp 0.053), key col 0.002
    -       Left trough: idx=3728 (7.456s), amp=0.001
    -       Right trough: idx=3831 (7.662s), amp=0.002
    - S2: prom 0.001, peak @ 7.698s (amp 0.003), key col 0.002
    -       Left trough: idx=3831 (7.662s), amp=0.002
    -       Right trough: idx=3889 (7.778s), amp=0.002
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.5`
- **Long-Term BPM (Belief)**: `147.1`


## Time: `7.7780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `166.5`
- **Long-Term BPM (Belief)**: `147.1`


## Time: `7.9380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.056, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.18 (Pairing Ratio: 70%, Floor: 0.90) → 0.89
    - Final Score: 0.89 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.056, peak @ 7.938s (amp 0.058), key col 0.002
    -       Left trough: idx=3889 (7.778s), amp=0.002
    -       Right trough: idx=4010 (8.020s), amp=0.002
    - S2: prom 0.001, peak @ 8.060s (amp 0.003), key col 0.002
    -       Left trough: idx=4010 (8.020s), amp=0.002
    -       Right trough: idx=4080 (8.160s), amp=0.001
- **Raw Amp**: `0.058`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.2`
- **Long-Term BPM (Belief)**: `148.0`


## Time: `8.0200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.2`
- **Long-Term BPM (Belief)**: `148.0`


## Time: `8.0600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.056, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.18 (Pairing Ratio: 70%, Floor: 0.90) → 0.89
    - Final Score: 0.89 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.056, peak @ 7.938s (amp 0.058), key col 0.002
    -       Left trough: idx=3889 (7.778s), amp=0.002
    -       Right trough: idx=4010 (8.020s), amp=0.002
    - S2: prom 0.001, peak @ 8.060s (amp 0.003), key col 0.002
    -       Left trough: idx=4010 (8.020s), amp=0.002
    -       Right trough: idx=4080 (8.160s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.2`
- **Long-Term BPM (Belief)**: `148.0`


## Time: `8.1600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `165.2`
- **Long-Term BPM (Belief)**: `148.0`


## Time: `8.3020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 148 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 148 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.20 (Pairing Ratio: 75%, Floor: 0.90) → 0.90
    - Final Score: 0.90 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 8.302s (amp 0.055), key col 0.002
    -       Left trough: idx=4080 (8.160s), amp=0.001
    -       Right trough: idx=4199 (8.398s), amp=0.002
    - S2: prom 0.003, peak @ 8.492s (amp 0.004), key col 0.002
    -       Left trough: idx=4199 (8.398s), amp=0.002
    -       Right trough: idx=4273 (8.546s), amp=0.002
- **Raw Amp**: `0.055`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.5`
- **Long-Term BPM (Belief)**: `148.8`


## Time: `8.3980s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.5`
- **Long-Term BPM (Belief)**: `148.8`


## Time: `8.4920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 148 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 148 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.20 (Pairing Ratio: 75%, Floor: 0.90) → 0.90
    - Final Score: 0.90 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 8.302s (amp 0.055), key col 0.002
    -       Left trough: idx=4080 (8.160s), amp=0.001
    -       Right trough: idx=4199 (8.398s), amp=0.002
    - S2: prom 0.003, peak @ 8.492s (amp 0.004), key col 0.002
    -       Left trough: idx=4199 (8.398s), amp=0.002
    -       Right trough: idx=4273 (8.546s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.5`
- **Long-Term BPM (Belief)**: `148.8`


## Time: `8.5460s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `164.5`
- **Long-Term BPM (Belief)**: `148.8`


## Time: `8.6560s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 149 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 149 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 8.656s (amp 0.053), key col 0.003
    -       Left trough: idx=4273 (8.546s), amp=0.002
    -       Right trough: idx=4366 (8.732s), amp=0.003
    - S2: prom 0.003, peak @ 8.790s (amp 0.006), key col 0.003
    -       Left trough: idx=4366 (8.732s), amp=0.003
    -       Right trough: idx=4457 (8.914s), amp=0.002
- **Raw Amp**: `0.053`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `162.3`
- **Long-Term BPM (Belief)**: `149.9`


## Time: `8.7320s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `162.3`
- **Long-Term BPM (Belief)**: `149.9`


## Time: `8.7900s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 149 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 149 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 8.656s (amp 0.053), key col 0.003
    -       Left trough: idx=4273 (8.546s), amp=0.002
    -       Right trough: idx=4366 (8.732s), amp=0.003
    - S2: prom 0.003, peak @ 8.790s (amp 0.006), key col 0.003
    -       Left trough: idx=4366 (8.732s), amp=0.003
    -       Right trough: idx=4457 (8.914s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `162.3`
- **Long-Term BPM (Belief)**: `149.9`


## Time: `8.9140s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `162.3`
- **Long-Term BPM (Belief)**: `149.9`


## Time: `9.0220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 150 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 150 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 9.022s (amp 0.057), key col 0.003
    -       Left trough: idx=4457 (8.914s), amp=0.002
    -       Right trough: idx=4555 (9.110s), amp=0.003
    - S2: prom 0.003, peak @ 9.178s (amp 0.006), key col 0.003
    -       Left trough: idx=4555 (9.110s), amp=0.003
    -       Right trough: idx=4641 (9.282s), amp=0.001
- **Raw Amp**: `0.057`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `161.7`
- **Long-Term BPM (Belief)**: `150.6`


## Time: `9.1100s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `161.7`
- **Long-Term BPM (Belief)**: `150.6`


## Time: `9.1780s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 150 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 150 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 9.022s (amp 0.057), key col 0.003
    -       Left trough: idx=4457 (8.914s), amp=0.002
    -       Right trough: idx=4555 (9.110s), amp=0.003
    - S2: prom 0.003, peak @ 9.178s (amp 0.006), key col 0.003
    -       Left trough: idx=4555 (9.110s), amp=0.003
    -       Right trough: idx=4641 (9.282s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `161.7`
- **Long-Term BPM (Belief)**: `150.6`


## Time: `9.2820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `161.7`
- **Long-Term BPM (Belief)**: `150.6`


## Time: `9.3880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 151 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 151 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 9.388s (amp 0.054), key col 0.002
    -       Left trough: idx=4641 (9.282s), amp=0.001
    -       Right trough: idx=4734 (9.468s), amp=0.002
    - S2: prom 0.004, peak @ 9.548s (amp 0.006), key col 0.002
    -       Left trough: idx=4734 (9.468s), amp=0.002
    -       Right trough: idx=4822 (9.644s), amp=0.002
- **Raw Amp**: `0.054`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.6`
- **Long-Term BPM (Belief)**: `151.2`


## Time: `9.4680s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.6`
- **Long-Term BPM (Belief)**: `151.2`


## Time: `9.5480s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 151 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 151 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.22 (Pairing Ratio: 80%, Floor: 0.90) → 0.92
    - Final Score: 0.92 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 9.388s (amp 0.054), key col 0.002
    -       Left trough: idx=4641 (9.282s), amp=0.001
    -       Right trough: idx=4734 (9.468s), amp=0.002
    - S2: prom 0.004, peak @ 9.548s (amp 0.006), key col 0.002
    -       Left trough: idx=4734 (9.468s), amp=0.002
    -       Right trough: idx=4822 (9.644s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.6`
- **Long-Term BPM (Belief)**: `151.2`


## Time: `9.6440s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `160.6`
- **Long-Term BPM (Belief)**: `151.2`


## Time: `9.7400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.070, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 151 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 151 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.070, peak @ 9.740s (amp 0.072), key col 0.002
    -       Left trough: idx=4822 (9.644s), amp=0.002
    -       Right trough: idx=4920 (9.840s), amp=0.001
    - S2: prom 0.002, peak @ 9.888s (amp 0.004), key col 0.001
    -       Left trough: idx=4920 (9.840s), amp=0.001
    -       Right trough: idx=4994 (9.988s), amp=0.001
- **Raw Amp**: `0.072`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `9.8400s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `9.8880s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.070, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 151 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 151 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.070, peak @ 9.740s (amp 0.072), key col 0.002
    -       Left trough: idx=4822 (9.644s), amp=0.002
    -       Right trough: idx=4920 (9.840s), amp=0.001
    - S2: prom 0.002, peak @ 9.888s (amp 0.004), key col 0.001
    -       Left trough: idx=4920 (9.840s), amp=0.001
    -       Right trough: idx=4994 (9.988s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `9.9880s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `10.1500s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 10.150s (amp 0.054), key col 0.002
    -       Left trough: idx=4994 (9.988s), amp=0.001
    -       Right trough: idx=5121 (10.242s), amp=0.002
    - S2: prom 0.001, peak @ 10.286s (amp 0.003), key col 0.002
    -       Left trough: idx=5121 (10.242s), amp=0.002
    -       Right trough: idx=5193 (10.386s), amp=0.001
- **Raw Amp**: `0.054`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `151.9`


## Time: `10.2420s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `151.9`


## Time: `10.2860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 10.150s (amp 0.054), key col 0.002
    -       Left trough: idx=4994 (9.988s), amp=0.001
    -       Right trough: idx=5121 (10.242s), amp=0.002
    - S2: prom 0.001, peak @ 10.286s (amp 0.003), key col 0.002
    -       Left trough: idx=5121 (10.242s), amp=0.002
    -       Right trough: idx=5193 (10.386s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `151.9`


## Time: `10.3860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `158.9`
- **Long-Term BPM (Belief)**: `151.9`


## Time: `10.5320s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 10.532s (amp 0.048), key col 0.002
    -       Left trough: idx=5193 (10.386s), amp=0.001
    -       Right trough: idx=5311 (10.622s), amp=0.002
    - S2: prom 0.001, peak @ 10.652s (amp 0.004), key col 0.002
    -       Left trough: idx=5311 (10.622s), amp=0.002
    -       Right trough: idx=5376 (10.752s), amp=0.001
- **Raw Amp**: `0.048`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.5`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `10.6220s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.5`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `10.6520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 10.532s (amp 0.048), key col 0.002
    -       Left trough: idx=5193 (10.386s), amp=0.001
    -       Right trough: idx=5311 (10.622s), amp=0.002
    - S2: prom 0.001, peak @ 10.652s (amp 0.004), key col 0.002
    -       Left trough: idx=5311 (10.622s), amp=0.002
    -       Right trough: idx=5376 (10.752s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.5`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `10.7520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `157.5`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `10.9540s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.002, S2/S1=0.05 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 10.954s (amp 0.047), key col 0.003
    -       Left trough: idx=5376 (10.752s), amp=0.001
    -       Right trough: idx=5518 (11.036s), amp=0.003
    - S2: prom 0.002, peak @ 11.066s (amp 0.005), key col 0.003
    -       Left trough: idx=5518 (11.036s), amp=0.003
    -       Right trough: idx=5591 (11.182s), amp=0.002
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `151.7`


## Time: `11.0360s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `151.7`


## Time: `11.0660s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.002, S2/S1=0.05 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 10.954s (amp 0.047), key col 0.003
    -       Left trough: idx=5376 (10.752s), amp=0.001
    -       Right trough: idx=5518 (11.036s), amp=0.003
    - S2: prom 0.002, peak @ 11.066s (amp 0.005), key col 0.003
    -       Left trough: idx=5518 (11.036s), amp=0.003
    -       Right trough: idx=5591 (11.182s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `151.7`


## Time: `11.1820s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.6`
- **Long-Term BPM (Belief)**: `151.7`


## Time: `11.3300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.004, S2/S1=0.07 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 11.330s (amp 0.055), key col 0.002
    -       Left trough: idx=5591 (11.182s), amp=0.002
    -       Right trough: idx=5707 (11.414s), amp=0.002
    - S2: prom 0.004, peak @ 11.512s (amp 0.005), key col 0.002
    -       Left trough: idx=5707 (11.414s), amp=0.002
    -       Right trough: idx=5786 (11.572s), amp=0.001
- **Raw Amp**: `0.055`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `11.4140s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `11.5120s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.004, S2/S1=0.07 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 11.330s (amp 0.055), key col 0.002
    -       Left trough: idx=5591 (11.182s), amp=0.002
    -       Right trough: idx=5707 (11.414s), amp=0.002
    - S2: prom 0.004, peak @ 11.512s (amp 0.005), key col 0.002
    -       Left trough: idx=5707 (11.414s), amp=0.002
    -       Right trough: idx=5786 (11.572s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `11.5720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `11.7280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.004, S2/S1=0.06 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 11.728s (amp 0.056), key col 0.002
    -       Left trough: idx=5786 (11.572s), amp=0.001
    -       Right trough: idx=5903 (11.806s), amp=0.002
    - S2: prom 0.004, peak @ 11.896s (amp 0.005), key col 0.002
    -       Left trough: idx=5903 (11.806s), amp=0.002
    -       Right trough: idx=5983 (11.966s), amp=0.001
- **Raw Amp**: `0.056`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.7`
- **Long-Term BPM (Belief)**: `152.0`


## Time: `11.8060s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.7`
- **Long-Term BPM (Belief)**: `152.0`


## Time: `11.8960s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.004, S2/S1=0.06 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 11.728s (amp 0.056), key col 0.002
    -       Left trough: idx=5786 (11.572s), amp=0.001
    -       Right trough: idx=5903 (11.806s), amp=0.002
    - S2: prom 0.004, peak @ 11.896s (amp 0.005), key col 0.002
    -       Left trough: idx=5903 (11.806s), amp=0.002
    -       Right trough: idx=5983 (11.966s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.7`
- **Long-Term BPM (Belief)**: `152.0`


## Time: `11.9660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.7`
- **Long-Term BPM (Belief)**: `152.0`


## Time: `12.1100s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 12.110s (amp 0.057), key col 0.002
    -       Left trough: idx=5983 (11.966s), amp=0.001
    -       Right trough: idx=6097 (12.194s), amp=0.002
    - S2: prom 0.003, peak @ 12.290s (amp 0.005), key col 0.002
    -       Left trough: idx=6097 (12.194s), amp=0.002
    -       Right trough: idx=6200 (12.400s), amp=0.002
- **Raw Amp**: `0.057`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.1940s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.2900s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 12.110s (amp 0.057), key col 0.002
    -       Left trough: idx=5983 (11.966s), amp=0.001
    -       Right trough: idx=6097 (12.194s), amp=0.002
    - S2: prom 0.003, peak @ 12.290s (amp 0.005), key col 0.002
    -       Left trough: idx=6097 (12.194s), amp=0.002
    -       Right trough: idx=6200 (12.400s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.4000s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.5000s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.083, S2=0.002, S2/S1=0.02 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.083, peak @ 12.500s (amp 0.085), key col 0.002
    -       Left trough: idx=6200 (12.400s), amp=0.002
    -       Right trough: idx=6289 (12.578s), amp=0.002
    - S2: prom 0.002, peak @ 12.620s (amp 0.004), key col 0.002
    -       Left trough: idx=6289 (12.578s), amp=0.002
    -       Right trough: idx=6360 (12.720s), amp=0.001
- **Raw Amp**: `0.085`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.4`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.5780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.4`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.6200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.083, S2=0.002, S2/S1=0.02 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.083, peak @ 12.500s (amp 0.085), key col 0.002
    -       Left trough: idx=6200 (12.400s), amp=0.002
    -       Right trough: idx=6289 (12.578s), amp=0.002
    - S2: prom 0.002, peak @ 12.620s (amp 0.004), key col 0.002
    -       Left trough: idx=6289 (12.578s), amp=0.002
    -       Right trough: idx=6360 (12.720s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.4`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.7200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.4`
- **Long-Term BPM (Belief)**: `152.3`


## Time: `12.9040s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.025, S2/S1=0.46 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.46) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Interval penalty by 0.75 (Interval 0.392s > Max 0.276s)
    - Final Score: 0.23 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.97: interval 0.404s vs expected 0.394s (deviation 3%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.66: strength ratio 0.66x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.97 x 0.65) + (Amplitude 0.66 x 0.35) = 0.858
    - Outcome: Validated Lone S1 (score 0.86 >= threshold 0.50)
- **Raw Amp**: `0.056`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.2`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `13.1800s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.2`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `13.2960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.003, S2/S1=0.10 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 13.296s (amp 0.027), key col 0.002
    -       Left trough: idx=6590 (13.180s), amp=0.001
    -       Right trough: idx=6684 (13.368s), amp=0.002
    - S2: prom 0.003, peak @ 13.454s (amp 0.004), key col 0.002
    -       Left trough: idx=6684 (13.368s), amp=0.002
    -       Right trough: idx=6774 (13.548s), amp=0.001
- **Raw Amp**: `0.027`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.4`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `13.3680s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.4`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `13.4540s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.003, S2/S1=0.10 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 13.296s (amp 0.027), key col 0.002
    -       Left trough: idx=6590 (13.180s), amp=0.001
    -       Right trough: idx=6684 (13.368s), amp=0.002
    - S2: prom 0.003, peak @ 13.454s (amp 0.004), key col 0.002
    -       Left trough: idx=6684 (13.368s), amp=0.002
    -       Right trough: idx=6774 (13.548s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.4`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `13.5480s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.4`
- **Long-Term BPM (Belief)**: `152.2`


## Time: `13.6960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 13.696s (amp 0.051), key col 0.003
    -       Left trough: idx=6774 (13.548s), amp=0.001
    -       Right trough: idx=6884 (13.768s), amp=0.003
    - S2: prom 0.003, peak @ 13.856s (amp 0.006), key col 0.003
    -       Left trough: idx=6884 (13.768s), amp=0.003
    -       Right trough: idx=6979 (13.958s), amp=0.002
- **Raw Amp**: `0.051`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.9`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `13.7680s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.9`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `13.8560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 13.696s (amp 0.051), key col 0.003
    -       Left trough: idx=6774 (13.548s), amp=0.001
    -       Right trough: idx=6884 (13.768s), amp=0.003
    - S2: prom 0.003, peak @ 13.856s (amp 0.006), key col 0.003
    -       Left trough: idx=6884 (13.768s), amp=0.003
    -       Right trough: idx=6979 (13.958s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.9`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `13.9580s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.9`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `14.1080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.005, S2/S1=0.11 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 14.108s (amp 0.047), key col 0.004
    -       Left trough: idx=6979 (13.958s), amp=0.002
    -       Right trough: idx=7089 (14.178s), amp=0.004
    - S2: prom 0.005, peak @ 14.262s (amp 0.009), key col 0.004
    -       Left trough: idx=7089 (14.178s), amp=0.004
    -       Right trough: idx=7189 (14.378s), amp=0.003
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.1`
- **Long-Term BPM (Belief)**: `151.8`


## Time: `14.1780s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.1`
- **Long-Term BPM (Belief)**: `151.8`


## Time: `14.2620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.005, S2/S1=0.11 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 14.108s (amp 0.047), key col 0.004
    -       Left trough: idx=6979 (13.958s), amp=0.002
    -       Right trough: idx=7089 (14.178s), amp=0.004
    - S2: prom 0.005, peak @ 14.262s (amp 0.009), key col 0.004
    -       Left trough: idx=7089 (14.178s), amp=0.004
    -       Right trough: idx=7189 (14.378s), amp=0.003
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.1`
- **Long-Term BPM (Belief)**: `151.8`


## Time: `14.3780s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.1`
- **Long-Term BPM (Belief)**: `151.8`


## Time: `14.4880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.004, S2/S1=0.09 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 14.488s (amp 0.044), key col 0.003
    -       Left trough: idx=7189 (14.378s), amp=0.003
    -       Right trough: idx=7284 (14.568s), amp=0.003
    - S2: prom 0.004, peak @ 14.652s (amp 0.007), key col 0.003
    -       Left trough: idx=7284 (14.568s), amp=0.003
    -       Right trough: idx=7367 (14.734s), amp=0.001
- **Raw Amp**: `0.044`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.5`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `14.5680s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.5`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `14.6520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.004, S2/S1=0.09 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 14.488s (amp 0.044), key col 0.003
    -       Left trough: idx=7189 (14.378s), amp=0.003
    -       Right trough: idx=7284 (14.568s), amp=0.003
    - S2: prom 0.004, peak @ 14.652s (amp 0.007), key col 0.003
    -       Left trough: idx=7284 (14.568s), amp=0.003
    -       Right trough: idx=7367 (14.734s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.5`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `14.7340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.5`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `14.8640s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.062, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.062, peak @ 14.864s (amp 0.064), key col 0.002
    -       Left trough: idx=7367 (14.734s), amp=0.001
    -       Right trough: idx=7477 (14.954s), amp=0.002
    - S2: prom 0.002, peak @ 15.008s (amp 0.004), key col 0.002
    -       Left trough: idx=7477 (14.954s), amp=0.002
    -       Right trough: idx=7556 (15.112s), amp=0.000
- **Raw Amp**: `0.064`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.2`
- **Long-Term BPM (Belief)**: `152.4`


## Time: `14.9540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.2`
- **Long-Term BPM (Belief)**: `152.4`


## Time: `15.0080s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.062, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.062, peak @ 14.864s (amp 0.064), key col 0.002
    -       Left trough: idx=7367 (14.734s), amp=0.001
    -       Right trough: idx=7477 (14.954s), amp=0.002
    - S2: prom 0.002, peak @ 15.008s (amp 0.004), key col 0.002
    -       Left trough: idx=7477 (14.954s), amp=0.002
    -       Right trough: idx=7556 (15.112s), amp=0.000
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.2`
- **Long-Term BPM (Belief)**: `152.4`


## Time: `15.1120s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.2`
- **Long-Term BPM (Belief)**: `152.4`


## Time: `15.2460s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.068, S2=0.058, S2/S1=0.86 (Expected max 1.20 at 152 BPM)
    - Contractility Neutral: prominence ratio 0.86 within expected range for 152 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.77
    - Interval penalty by 0.70 (Interval 0.378s > Max 0.276s)
    - Final Score: 0.07 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.96: interval 0.382s vs expected 0.394s (deviation 3%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 1.05x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.96 x 0.65) + (Amplitude 1.00 x 0.35) = 0.974
    - Outcome: Validated Lone S1 (score 0.97 >= threshold 0.50)
- **Raw Amp**: `0.068`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.8`
- **Long-Term BPM (Belief)**: `152.7`


## Time: `15.4880s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.8`
- **Long-Term BPM (Belief)**: `152.7`


## Time: `15.6240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.058, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.058, peak @ 15.624s (amp 0.060), key col 0.002
    -       Left trough: idx=7744 (15.488s), amp=0.000
    -       Right trough: idx=7846 (15.692s), amp=0.002
    - S2: prom 0.002, peak @ 15.742s (amp 0.004), key col 0.002
    -       Left trough: idx=7846 (15.692s), amp=0.002
    -       Right trough: idx=7921 (15.842s), amp=0.001
- **Raw Amp**: `0.060`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.3`
- **Long-Term BPM (Belief)**: `153.0`


## Time: `15.6920s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.3`
- **Long-Term BPM (Belief)**: `153.0`


## Time: `15.7420s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.058, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.058, peak @ 15.624s (amp 0.060), key col 0.002
    -       Left trough: idx=7744 (15.488s), amp=0.000
    -       Right trough: idx=7846 (15.692s), amp=0.002
    - S2: prom 0.002, peak @ 15.742s (amp 0.004), key col 0.002
    -       Left trough: idx=7846 (15.692s), amp=0.002
    -       Right trough: idx=7921 (15.842s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.3`
- **Long-Term BPM (Belief)**: `153.0`


## Time: `15.8420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `154.3`
- **Long-Term BPM (Belief)**: `153.0`


## Time: `15.9940s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 15.994s (amp 0.051), key col 0.005
    -       Left trough: idx=7921 (15.842s), amp=0.001
    -       Right trough: idx=8042 (16.084s), amp=0.005
    - S2: prom 0.003, peak @ 16.148s (amp 0.008), key col 0.005
    -       Left trough: idx=8042 (16.084s), amp=0.005
    -       Right trough: idx=8119 (16.238s), amp=0.002
- **Raw Amp**: `0.051`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.4`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.0840s`
**Trough Detected**
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.4`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.1480s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.003, S2/S1=0.06 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 15.994s (amp 0.051), key col 0.005
    -       Left trough: idx=7921 (15.842s), amp=0.001
    -       Right trough: idx=8042 (16.084s), amp=0.005
    - S2: prom 0.003, peak @ 16.148s (amp 0.008), key col 0.005
    -       Left trough: idx=8042 (16.084s), amp=0.005
    -       Right trough: idx=8119 (16.238s), amp=0.002
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.4`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.2380s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.4`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.3960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.004, S2/S1=0.12 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 16.396s (amp 0.040), key col 0.005
    -       Left trough: idx=8119 (16.238s), amp=0.002
    -       Right trough: idx=8231 (16.462s), amp=0.005
    - S2: prom 0.004, peak @ 16.540s (amp 0.009), key col 0.005
    -       Left trough: idx=8231 (16.462s), amp=0.005
    -       Right trough: idx=8339 (16.678s), amp=0.002
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.9`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `16.4620s`
**Trough Detected**
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.9`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `16.5400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.004, S2/S1=0.12 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 16.396s (amp 0.040), key col 0.005
    -       Left trough: idx=8119 (16.238s), amp=0.002
    -       Right trough: idx=8231 (16.462s), amp=0.005
    - S2: prom 0.004, peak @ 16.540s (amp 0.009), key col 0.005
    -       Left trough: idx=8231 (16.462s), amp=0.005
    -       Right trough: idx=8339 (16.678s), amp=0.002
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.9`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `16.6780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `155.9`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `16.7800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.054, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.054, peak @ 16.780s (amp 0.057), key col 0.003
    -       Left trough: idx=8339 (16.678s), amp=0.002
    -       Right trough: idx=8433 (16.866s), amp=0.003
    - S2: prom 0.002, peak @ 16.926s (amp 0.004), key col 0.003
    -       Left trough: idx=8433 (16.866s), amp=0.003
    -       Right trough: idx=8527 (17.054s), amp=0.001
- **Raw Amp**: `0.057`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.1`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.8660s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.1`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `16.9260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.054, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.054, peak @ 16.780s (amp 0.057), key col 0.003
    -       Left trough: idx=8339 (16.678s), amp=0.002
    -       Right trough: idx=8433 (16.866s), amp=0.003
    - S2: prom 0.002, peak @ 16.926s (amp 0.004), key col 0.003
    -       Left trough: idx=8433 (16.866s), amp=0.003
    -       Right trough: idx=8527 (17.054s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `156.1`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `17.0540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `156.1`
- **Long-Term BPM (Belief)**: `153.4`


## Time: `17.1740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.064, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.064, peak @ 17.174s (amp 0.066), key col 0.002
    -       Left trough: idx=8527 (17.054s), amp=0.001
    -       Right trough: idx=8626 (17.252s), amp=0.002
    - S2: prom 0.001, peak @ 17.320s (amp 0.004), key col 0.002
    -       Left trough: idx=8626 (17.252s), amp=0.002
    -       Right trough: idx=8699 (17.398s), amp=0.002
- **Raw Amp**: `0.066`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `156.4`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `17.2520s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `156.4`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `17.3200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.064, S2=0.001, S2/S1=0.02 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.064, peak @ 17.174s (amp 0.066), key col 0.002
    -       Left trough: idx=8527 (17.054s), amp=0.001
    -       Right trough: idx=8626 (17.252s), amp=0.002
    - S2: prom 0.001, peak @ 17.320s (amp 0.004), key col 0.002
    -       Left trough: idx=8626 (17.252s), amp=0.002
    -       Right trough: idx=8699 (17.398s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `156.4`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `17.3980s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `156.4`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `17.5440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.058, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.058, peak @ 17.544s (amp 0.060), key col 0.002
    -       Left trough: idx=8699 (17.398s), amp=0.002
    -       Right trough: idx=8822 (17.644s), amp=0.002
    - S2: prom 0.002, peak @ 17.760s (amp 0.004), key col 0.002
    -       Left trough: idx=8822 (17.644s), amp=0.002
    -       Right trough: idx=8931 (17.862s), amp=0.002
- **Raw Amp**: `0.060`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `154.7`
- **Long-Term BPM (Belief)**: `153.8`


## Time: `17.6440s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `154.7`
- **Long-Term BPM (Belief)**: `153.8`


## Time: `17.7600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.058, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.058, peak @ 17.544s (amp 0.060), key col 0.002
    -       Left trough: idx=8699 (17.398s), amp=0.002
    -       Right trough: idx=8822 (17.644s), amp=0.002
    - S2: prom 0.002, peak @ 17.760s (amp 0.004), key col 0.002
    -       Left trough: idx=8822 (17.644s), amp=0.002
    -       Right trough: idx=8931 (17.862s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `154.7`
- **Long-Term BPM (Belief)**: `153.8`


## Time: `17.8620s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `154.7`
- **Long-Term BPM (Belief)**: `153.8`


## Time: `17.9660s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.059, S2=0.052, S2/S1=0.88 (Expected max 1.20 at 154 BPM)
    - Contractility Neutral: prominence ratio 0.88 within expected range for 154 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.76
    - Interval penalty by 0.58 (Interval 0.358s > Max 0.273s)
    - Final Score: 0.17 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.89: interval 0.422s vs expected 0.390s (deviation 8%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 1.02x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.89 x 0.65) + (Amplitude 1.00 x 0.35) = 0.929
    - Outcome: Validated Lone S1 (score 0.93 >= threshold 0.50)
- **Raw Amp**: `0.061`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `18.1820s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `153.3`
- **Long-Term BPM (Belief)**: `153.2`


## Time: `18.3240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 18.324s (amp 0.054), key col 0.002
    -       Left trough: idx=9091 (18.182s), amp=0.002
    -       Right trough: idx=9204 (18.408s), amp=0.002
    - S2: prom 0.003, peak @ 18.472s (amp 0.005), key col 0.002
    -       Left trough: idx=9204 (18.408s), amp=0.002
    -       Right trough: idx=9274 (18.548s), amp=0.002
- **Raw Amp**: `0.054`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.1`
- **Long-Term BPM (Belief)**: `153.9`


## Time: `18.4080s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.1`
- **Long-Term BPM (Belief)**: `153.9`


## Time: `18.4720s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 18.324s (amp 0.054), key col 0.002
    -       Left trough: idx=9091 (18.182s), amp=0.002
    -       Right trough: idx=9204 (18.408s), amp=0.002
    - S2: prom 0.003, peak @ 18.472s (amp 0.005), key col 0.002
    -       Left trough: idx=9204 (18.408s), amp=0.002
    -       Right trough: idx=9274 (18.548s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.1`
- **Long-Term BPM (Belief)**: `153.9`


## Time: `18.5480s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `152.1`
- **Long-Term BPM (Belief)**: `153.9`


## Time: `18.7080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.069, S2=0.005, S2/S1=0.07 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.069, peak @ 18.708s (amp 0.071), key col 0.002
    -       Left trough: idx=9274 (18.548s), amp=0.002
    -       Right trough: idx=9403 (18.806s), amp=0.002
    - S2: prom 0.005, peak @ 18.890s (amp 0.007), key col 0.002
    -       Left trough: idx=9403 (18.806s), amp=0.002
    -       Right trough: idx=9505 (19.010s), amp=0.002
- **Raw Amp**: `0.071`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.4`
- **Long-Term BPM (Belief)**: `154.0`


## Time: `18.8060s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.4`
- **Long-Term BPM (Belief)**: `154.0`


## Time: `18.8900s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.069, S2=0.005, S2/S1=0.07 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.069, peak @ 18.708s (amp 0.071), key col 0.002
    -       Left trough: idx=9274 (18.548s), amp=0.002
    -       Right trough: idx=9403 (18.806s), amp=0.002
    - S2: prom 0.005, peak @ 18.890s (amp 0.007), key col 0.002
    -       Left trough: idx=9403 (18.806s), amp=0.002
    -       Right trough: idx=9505 (19.010s), amp=0.002
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.4`
- **Long-Term BPM (Belief)**: `154.0`


## Time: `19.0100s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.4`
- **Long-Term BPM (Belief)**: `154.0`


## Time: `19.1140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.063, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.063, peak @ 19.114s (amp 0.065), key col 0.002
    -       Left trough: idx=9505 (19.010s), amp=0.002
    -       Right trough: idx=9594 (19.188s), amp=0.002
    - S2: prom 0.003, peak @ 19.256s (amp 0.005), key col 0.002
    -       Left trough: idx=9594 (19.188s), amp=0.002
    -       Right trough: idx=9690 (19.380s), amp=0.001
- **Raw Amp**: `0.065`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.5`
- **Long-Term BPM (Belief)**: `153.7`


## Time: `19.1880s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.5`
- **Long-Term BPM (Belief)**: `153.7`


## Time: `19.2560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.063, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.063, peak @ 19.114s (amp 0.065), key col 0.002
    -       Left trough: idx=9505 (19.010s), amp=0.002
    -       Right trough: idx=9594 (19.188s), amp=0.002
    - S2: prom 0.003, peak @ 19.256s (amp 0.005), key col 0.002
    -       Left trough: idx=9594 (19.188s), amp=0.002
    -       Right trough: idx=9690 (19.380s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.5`
- **Long-Term BPM (Belief)**: `153.7`


## Time: `19.3800s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `150.5`
- **Long-Term BPM (Belief)**: `153.7`


## Time: `19.4840s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.068, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.068, peak @ 19.484s (amp 0.069), key col 0.001
    -       Left trough: idx=9690 (19.380s), amp=0.001
    -       Right trough: idx=9793 (19.586s), amp=0.001
    - S2: prom 0.003, peak @ 19.640s (amp 0.004), key col 0.001
    -       Left trough: idx=9793 (19.586s), amp=0.001
    -       Right trough: idx=9897 (19.794s), amp=0.001
- **Raw Amp**: `0.069`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `148.7`
- **Long-Term BPM (Belief)**: `154.1`


## Time: `19.5860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `148.7`
- **Long-Term BPM (Belief)**: `154.1`


## Time: `19.6400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.068, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.068, peak @ 19.484s (amp 0.069), key col 0.001
    -       Left trough: idx=9690 (19.380s), amp=0.001
    -       Right trough: idx=9793 (19.586s), amp=0.001
    - S2: prom 0.003, peak @ 19.640s (amp 0.004), key col 0.001
    -       Left trough: idx=9793 (19.586s), amp=0.001
    -       Right trough: idx=9897 (19.794s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `148.7`
- **Long-Term BPM (Belief)**: `154.1`


## Time: `19.7940s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `148.7`
- **Long-Term BPM (Belief)**: `154.1`


## Time: `19.9200s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 19.920s (amp 0.057), key col 0.002
    -       Left trough: idx=9897 (19.794s), amp=0.001
    -       Right trough: idx=10007 (20.014s), amp=0.002
    - S2: prom 0.002, peak @ 20.052s (amp 0.004), key col 0.002
    -       Left trough: idx=10007 (20.014s), amp=0.002
    -       Right trough: idx=10074 (20.148s), amp=0.001
- **Raw Amp**: `0.057`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `146.2`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `20.0140s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `146.2`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `20.0520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 154 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 154 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 19.920s (amp 0.057), key col 0.002
    -       Left trough: idx=9897 (19.794s), amp=0.001
    -       Right trough: idx=10007 (20.014s), amp=0.002
    - S2: prom 0.002, peak @ 20.052s (amp 0.004), key col 0.002
    -       Left trough: idx=10007 (20.014s), amp=0.002
    -       Right trough: idx=10074 (20.148s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `146.2`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `20.1480s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `146.2`
- **Long-Term BPM (Belief)**: `153.3`


## Time: `20.3520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.060, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.060, peak @ 20.352s (amp 0.064), key col 0.005
    -       Left trough: idx=10074 (20.148s), amp=0.001
    -       Right trough: idx=10219 (20.438s), amp=0.005
    - S2: prom 0.002, peak @ 20.482s (amp 0.006), key col 0.005
    -       Left trough: idx=10219 (20.438s), amp=0.005
    -       Right trough: idx=10290 (20.580s), amp=0.001
- **Raw Amp**: `0.064`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `143.0`
- **Long-Term BPM (Belief)**: `152.6`


## Time: `20.4380s`
**Trough Detected**
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `143.0`
- **Long-Term BPM (Belief)**: `152.6`


## Time: `20.4820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.060, S2=0.002, S2/S1=0.03 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.060, peak @ 20.352s (amp 0.064), key col 0.005
    -       Left trough: idx=10074 (20.148s), amp=0.001
    -       Right trough: idx=10219 (20.438s), amp=0.005
    - S2: prom 0.002, peak @ 20.482s (amp 0.006), key col 0.005
    -       Left trough: idx=10219 (20.438s), amp=0.005
    -       Right trough: idx=10290 (20.580s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `143.0`
- **Long-Term BPM (Belief)**: `152.6`


## Time: `20.5800s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `143.0`
- **Long-Term BPM (Belief)**: `152.6`


## Time: `20.7740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.005, S2/S1=0.09 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 20.774s (amp 0.060), key col 0.003
    -       Left trough: idx=10290 (20.580s), amp=0.001
    -       Right trough: idx=10429 (20.858s), amp=0.003
    - S2: prom 0.005, peak @ 20.912s (amp 0.008), key col 0.003
    -       Left trough: idx=10429 (20.858s), amp=0.003
    -       Right trough: idx=10506 (21.012s), amp=0.001
- **Raw Amp**: `0.060`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `142.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `20.8580s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `142.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `20.9120s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.005, S2/S1=0.09 (Expected max 1.20 at 153 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 153 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.24 (Pairing Ratio: 85%, Floor: 0.90) → 0.93
    - Final Score: 0.93 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 20.774s (amp 0.060), key col 0.003
    -       Left trough: idx=10290 (20.580s), amp=0.001
    -       Right trough: idx=10429 (20.858s), amp=0.003
    - S2: prom 0.005, peak @ 20.912s (amp 0.008), key col 0.003
    -       Left trough: idx=10429 (20.858s), amp=0.003
    -       Right trough: idx=10506 (21.012s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `142.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `21.0120s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `142.1`
- **Long-Term BPM (Belief)**: `152.1`


## Time: `21.2000s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 21.200s (amp 0.050), key col 0.002
    -       Left trough: idx=10506 (21.012s), amp=0.001
    -       Right trough: idx=10642 (21.284s), amp=0.002
    - S2: prom 0.004, peak @ 21.338s (amp 0.006), key col 0.002
    -       Left trough: idx=10642 (21.284s), amp=0.002
    -       Right trough: idx=10753 (21.506s), amp=0.001
- **Raw Amp**: `0.050`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.5`
- **Long-Term BPM (Belief)**: `151.5`


## Time: `21.2840s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.5`
- **Long-Term BPM (Belief)**: `151.5`


## Time: `21.3380s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 21.200s (amp 0.050), key col 0.002
    -       Left trough: idx=10506 (21.012s), amp=0.001
    -       Right trough: idx=10642 (21.284s), amp=0.002
    - S2: prom 0.004, peak @ 21.338s (amp 0.006), key col 0.002
    -       Left trough: idx=10642 (21.284s), amp=0.002
    -       Right trough: idx=10753 (21.506s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.5`
- **Long-Term BPM (Belief)**: `151.5`


## Time: `21.5060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.5`
- **Long-Term BPM (Belief)**: `151.5`


## Time: `21.6460s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 21.646s (amp 0.047), key col 0.002
    -       Left trough: idx=10753 (21.506s), amp=0.001
    -       Right trough: idx=10867 (21.734s), amp=0.002
    - S2: prom 0.002, peak @ 21.818s (amp 0.004), key col 0.002
    -       Left trough: idx=10867 (21.734s), amp=0.002
    -       Right trough: idx=10939 (21.878s), amp=0.001
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `150.3`


## Time: `21.7340s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `150.3`


## Time: `21.8180s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 152 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 152 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 21.646s (amp 0.047), key col 0.002
    -       Left trough: idx=10753 (21.506s), amp=0.001
    -       Right trough: idx=10867 (21.734s), amp=0.002
    - S2: prom 0.002, peak @ 21.818s (amp 0.004), key col 0.002
    -       Left trough: idx=10867 (21.734s), amp=0.002
    -       Right trough: idx=10939 (21.878s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `150.3`


## Time: `21.8780s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `150.3`


## Time: `21.9780s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.045, S2/S1=82.85 (Expected max 1.20 at 151 BPM)
    - Contractility Penalty: -23.82 (S2 too prominent for BPM; prominence ratio 82.85 > expected 1.20) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.77: interval 0.332s vs expected 0.398s (deviation 17%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.02: strength ratio 0.02x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.77 x 0.65) + (Amplitude 0.02 x 0.35) = 0.512
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.160s < 0.175s (45% of expected RR) and strength ratio 0.05x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~375 BPM.
    - Confidence penalized 0.52x -> 0.51 to 0.27.
    - Outcome: Rejected Lone S1 (score 0.27 < threshold 0.50)
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `150.3`


## Time: `22.1380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 150 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 150 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 22.138s (amp 0.047), key col 0.002
    -       Left trough: idx=10939 (21.878s), amp=0.001
    -       Right trough: idx=11115 (22.230s), amp=0.002
    - S2: prom 0.001, peak @ 22.250s (amp 0.003), key col 0.002
    -       Left trough: idx=11115 (22.230s), amp=0.002
    -       Right trough: idx=11180 (22.360s), amp=0.001
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.1`
- **Long-Term BPM (Belief)**: `148.5`


## Time: `22.2300s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.1`
- **Long-Term BPM (Belief)**: `148.5`


## Time: `22.2500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.001, S2/S1=0.03 (Expected max 1.20 at 150 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 150 BPM; prominence ratio 0.03) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 22.138s (amp 0.047), key col 0.002
    -       Left trough: idx=10939 (21.878s), amp=0.001
    -       Right trough: idx=11115 (22.230s), amp=0.002
    - S2: prom 0.001, peak @ 22.250s (amp 0.003), key col 0.002
    -       Left trough: idx=11115 (22.230s), amp=0.002
    -       Right trough: idx=11180 (22.360s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.1`
- **Long-Term BPM (Belief)**: `148.5`


## Time: `22.3600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.1`
- **Long-Term BPM (Belief)**: `148.5`


## Time: `22.6240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 148 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 148 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 22.624s (amp 0.045), key col 0.002
    -       Left trough: idx=11180 (22.360s), amp=0.001
    -       Right trough: idx=11356 (22.712s), amp=0.002
    - S2: prom 0.004, peak @ 22.752s (amp 0.006), key col 0.002
    -       Left trough: idx=11356 (22.712s), amp=0.002
    -       Right trough: idx=11431 (22.862s), amp=0.001
- **Raw Amp**: `0.045`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.5`
- **Long-Term BPM (Belief)**: `147.2`


## Time: `22.7120s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.5`
- **Long-Term BPM (Belief)**: `147.2`


## Time: `22.7520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.004, S2/S1=0.08 (Expected max 1.20 at 148 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 148 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 22.624s (amp 0.045), key col 0.002
    -       Left trough: idx=11180 (22.360s), amp=0.001
    -       Right trough: idx=11356 (22.712s), amp=0.002
    - S2: prom 0.004, peak @ 22.752s (amp 0.006), key col 0.002
    -       Left trough: idx=11356 (22.712s), amp=0.002
    -       Right trough: idx=11431 (22.862s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.5`
- **Long-Term BPM (Belief)**: `147.2`


## Time: `22.8620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.5`
- **Long-Term BPM (Belief)**: `147.2`


## Time: `23.0800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.005, S2/S1=0.16 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 23.080s (amp 0.034), key col 0.003
    -       Left trough: idx=11431 (22.862s), amp=0.001
    -       Right trough: idx=11585 (23.170s), amp=0.003
    - S2: prom 0.005, peak @ 23.228s (amp 0.008), key col 0.003
    -       Left trough: idx=11585 (23.170s), amp=0.003
    -       Right trough: idx=11698 (23.396s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.9`
- **Long-Term BPM (Belief)**: `146.4`


## Time: `23.1700s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.9`
- **Long-Term BPM (Belief)**: `146.4`


## Time: `23.2280s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.005, S2/S1=0.16 (Expected max 1.20 at 147 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 147 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 23.080s (amp 0.034), key col 0.003
    -       Left trough: idx=11431 (22.862s), amp=0.001
    -       Right trough: idx=11585 (23.170s), amp=0.003
    - S2: prom 0.005, peak @ 23.228s (amp 0.008), key col 0.003
    -       Left trough: idx=11585 (23.170s), amp=0.003
    -       Right trough: idx=11698 (23.396s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.9`
- **Long-Term BPM (Belief)**: `146.4`


## Time: `23.3960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.9`
- **Long-Term BPM (Belief)**: `146.4`


## Time: `23.5180s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.005, S2/S1=0.12 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 23.518s (amp 0.039), key col 0.002
    -       Left trough: idx=11698 (23.396s), amp=0.001
    -       Right trough: idx=11800 (23.600s), amp=0.002
    - S2: prom 0.005, peak @ 23.678s (amp 0.006), key col 0.002
    -       Left trough: idx=11800 (23.600s), amp=0.002
    -       Right trough: idx=11894 (23.788s), amp=0.000
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.4`
- **Long-Term BPM (Belief)**: `146.0`


## Time: `23.6000s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.4`
- **Long-Term BPM (Belief)**: `146.0`


## Time: `23.6780s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.005, S2/S1=0.12 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.26 (Pairing Ratio: 90%, Floor: 0.90) → 0.95
    - Final Score: 0.95 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 23.518s (amp 0.039), key col 0.002
    -       Left trough: idx=11698 (23.396s), amp=0.001
    -       Right trough: idx=11800 (23.600s), amp=0.002
    - S2: prom 0.005, peak @ 23.678s (amp 0.006), key col 0.002
    -       Left trough: idx=11800 (23.600s), amp=0.002
    -       Right trough: idx=11894 (23.788s), amp=0.000
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.4`
- **Long-Term BPM (Belief)**: `146.0`


## Time: `23.7880s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.4`
- **Long-Term BPM (Belief)**: `146.0`


## Time: `23.9580s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.003, S2/S1=0.08 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 23.958s (amp 0.047), key col 0.001
    -       Left trough: idx=11894 (23.788s), amp=0.000
    -       Right trough: idx=12021 (24.042s), amp=0.001
    - S2: prom 0.003, peak @ 24.098s (amp 0.004), key col 0.001
    -       Left trough: idx=12021 (24.042s), amp=0.001
    -       Right trough: idx=12107 (24.214s), amp=0.001
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.5`
- **Long-Term BPM (Belief)**: `145.5`


## Time: `24.0420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.5`
- **Long-Term BPM (Belief)**: `145.5`


## Time: `24.0980s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.003, S2/S1=0.08 (Expected max 1.20 at 146 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 146 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 23.958s (amp 0.047), key col 0.001
    -       Left trough: idx=11894 (23.788s), amp=0.000
    -       Right trough: idx=12021 (24.042s), amp=0.001
    - S2: prom 0.003, peak @ 24.098s (amp 0.004), key col 0.001
    -       Left trough: idx=12021 (24.042s), amp=0.001
    -       Right trough: idx=12107 (24.214s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.5`
- **Long-Term BPM (Belief)**: `145.5`


## Time: `24.2140s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.5`
- **Long-Term BPM (Belief)**: `145.5`


## Time: `24.4160s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 24.416s (amp 0.050), key col 0.002
    -       Left trough: idx=12107 (24.214s), amp=0.001
    -       Right trough: idx=12269 (24.538s), amp=0.002
    - S2: prom 0.002, peak @ 24.640s (amp 0.004), key col 0.002
    -       Left trough: idx=12269 (24.538s), amp=0.002
    -       Right trough: idx=12421 (24.842s), amp=0.001
- **Raw Amp**: `0.050`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.0`
- **Long-Term BPM (Belief)**: `144.7`


## Time: `24.5380s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.0`
- **Long-Term BPM (Belief)**: `144.7`


## Time: `24.6400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 24.416s (amp 0.050), key col 0.002
    -       Left trough: idx=12107 (24.214s), amp=0.001
    -       Right trough: idx=12269 (24.538s), amp=0.002
    - S2: prom 0.002, peak @ 24.640s (amp 0.004), key col 0.002
    -       Left trough: idx=12269 (24.538s), amp=0.002
    -       Right trough: idx=12421 (24.842s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.0`
- **Long-Term BPM (Belief)**: `144.7`


## Time: `24.8420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.0`
- **Long-Term BPM (Belief)**: `144.7`


## Time: `24.9660s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.004, S2/S1=0.13 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 24.966s (amp 0.036), key col 0.004
    -       Left trough: idx=12421 (24.842s), amp=0.001
    -       Right trough: idx=12519 (25.038s), amp=0.004
    - S2: prom 0.004, peak @ 25.086s (amp 0.008), key col 0.004
    -       Left trough: idx=12519 (25.038s), amp=0.004
    -       Right trough: idx=12604 (25.208s), amp=0.003
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.8`
- **Long-Term BPM (Belief)**: `143.1`


## Time: `25.0380s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.8`
- **Long-Term BPM (Belief)**: `143.1`


## Time: `25.0860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.004, S2/S1=0.13 (Expected max 1.20 at 145 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 145 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 24.966s (amp 0.036), key col 0.004
    -       Left trough: idx=12421 (24.842s), amp=0.001
    -       Right trough: idx=12519 (25.038s), amp=0.004
    - S2: prom 0.004, peak @ 25.086s (amp 0.008), key col 0.004
    -       Left trough: idx=12519 (25.038s), amp=0.004
    -       Right trough: idx=12604 (25.208s), amp=0.003
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.8`
- **Long-Term BPM (Belief)**: `143.1`


## Time: `25.2080s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.8`
- **Long-Term BPM (Belief)**: `143.1`


## Time: `25.4220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.005, S2/S1=0.13 (Expected max 1.20 at 143 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 143 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 25.422s (amp 0.043), key col 0.003
    -       Left trough: idx=12604 (25.208s), amp=0.003
    -       Right trough: idx=12773 (25.546s), amp=0.002
    - S2: prom 0.005, peak @ 25.610s (amp 0.007), key col 0.002
    -       Left trough: idx=12773 (25.546s), amp=0.002
    -       Right trough: idx=12876 (25.752s), amp=0.001
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `25.5460s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `25.6100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.005, S2/S1=0.13 (Expected max 1.20 at 143 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 143 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 25.422s (amp 0.043), key col 0.003
    -       Left trough: idx=12604 (25.208s), amp=0.003
    -       Right trough: idx=12773 (25.546s), amp=0.002
    - S2: prom 0.005, peak @ 25.610s (amp 0.007), key col 0.002
    -       Left trough: idx=12773 (25.546s), amp=0.002
    -       Right trough: idx=12876 (25.752s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `25.7520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `142.5`


## Time: `25.8980s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.007, S2/S1=0.16 (Expected max 1.20 at 143 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 143 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 25.898s (amp 0.044), key col 0.001
    -       Left trough: idx=12876 (25.752s), amp=0.001
    -       Right trough: idx=12992 (25.984s), amp=0.001
    - S2: prom 0.007, peak @ 26.082s (amp 0.008), key col 0.001
    -       Left trough: idx=12992 (25.984s), amp=0.001
    -       Right trough: idx=13077 (26.154s), amp=0.001
- **Raw Amp**: `0.044`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.1`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `25.9840s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.1`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.0820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.007, S2/S1=0.16 (Expected max 1.20 at 143 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 143 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 25.898s (amp 0.044), key col 0.001
    -       Left trough: idx=12876 (25.752s), amp=0.001
    -       Right trough: idx=12992 (25.984s), amp=0.001
    - S2: prom 0.007, peak @ 26.082s (amp 0.008), key col 0.001
    -       Left trough: idx=12992 (25.984s), amp=0.001
    -       Right trough: idx=13077 (26.154s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.1`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.1540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.1`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.3200s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.005, S2/S1=0.10 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 26.320s (amp 0.048), key col 0.001
    -       Left trough: idx=13077 (26.154s), amp=0.001
    -       Right trough: idx=13204 (26.408s), amp=0.001
    - S2: prom 0.005, peak @ 26.462s (amp 0.006), key col 0.001
    -       Left trough: idx=13204 (26.408s), amp=0.001
    -       Right trough: idx=13316 (26.632s), amp=0.001
- **Raw Amp**: `0.048`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.4080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.4620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.005, S2/S1=0.10 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 26.320s (amp 0.048), key col 0.001
    -       Left trough: idx=13077 (26.154s), amp=0.001
    -       Right trough: idx=13204 (26.408s), amp=0.001
    - S2: prom 0.005, peak @ 26.462s (amp 0.006), key col 0.001
    -       Left trough: idx=13204 (26.408s), amp=0.001
    -       Right trough: idx=13316 (26.632s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.6320s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `26.7500s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 26.750s (amp 0.059), key col 0.003
    -       Left trough: idx=13316 (26.632s), amp=0.001
    -       Right trough: idx=13423 (26.846s), amp=0.003
    - S2: prom 0.002, peak @ 26.932s (amp 0.005), key col 0.003
    -       Left trough: idx=13423 (26.846s), amp=0.003
    -       Right trough: idx=13517 (27.034s), amp=0.001
- **Raw Amp**: `0.059`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.2`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `26.8460s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.2`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `26.9320s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.002, S2/S1=0.04 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 26.750s (amp 0.059), key col 0.003
    -       Left trough: idx=13316 (26.632s), amp=0.001
    -       Right trough: idx=13423 (26.846s), amp=0.003
    - S2: prom 0.002, peak @ 26.932s (amp 0.005), key col 0.003
    -       Left trough: idx=13423 (26.846s), amp=0.003
    -       Right trough: idx=13517 (27.034s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.2`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.0340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.2`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.1720s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 27.172s (amp 0.058), key col 0.001
    -       Left trough: idx=13517 (27.034s), amp=0.001
    -       Right trough: idx=13626 (27.252s), amp=0.001
    - S2: prom 0.003, peak @ 27.294s (amp 0.004), key col 0.001
    -       Left trough: idx=13626 (27.252s), amp=0.001
    -       Right trough: idx=13714 (27.428s), amp=0.000
- **Raw Amp**: `0.058`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.2520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.2940s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.003, S2/S1=0.05 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 27.172s (amp 0.058), key col 0.001
    -       Left trough: idx=13517 (27.034s), amp=0.001
    -       Right trough: idx=13626 (27.252s), amp=0.001
    - S2: prom 0.003, peak @ 27.294s (amp 0.004), key col 0.001
    -       Left trough: idx=13626 (27.252s), amp=0.001
    -       Right trough: idx=13714 (27.428s), amp=0.000
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.4280s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.5960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.061, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.061, peak @ 27.596s (amp 0.063), key col 0.002
    -       Left trough: idx=13714 (27.428s), amp=0.000
    -       Right trough: idx=13839 (27.678s), amp=0.002
    - S2: prom 0.003, peak @ 27.726s (amp 0.005), key col 0.002
    -       Left trough: idx=13839 (27.678s), amp=0.002
    -       Right trough: idx=13913 (27.826s), amp=0.001
- **Raw Amp**: `0.063`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.6780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.7260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.061, S2=0.003, S2/S1=0.04 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.061, peak @ 27.596s (amp 0.063), key col 0.002
    -       Left trough: idx=13714 (27.428s), amp=0.000
    -       Right trough: idx=13839 (27.678s), amp=0.002
    - S2: prom 0.003, peak @ 27.726s (amp 0.005), key col 0.002
    -       Left trough: idx=13839 (27.678s), amp=0.002
    -       Right trough: idx=13913 (27.826s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.8260s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `141.6`


## Time: `27.9980s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.007, S2/S1=0.19 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 27.998s (amp 0.042), key col 0.003
    -       Left trough: idx=13913 (27.826s), amp=0.001
    -       Right trough: idx=14049 (28.098s), amp=0.003
    - S2: prom 0.007, peak @ 28.162s (amp 0.011), key col 0.003
    -       Left trough: idx=14049 (28.098s), amp=0.003
    -       Right trough: idx=14139 (28.278s), amp=0.002
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `142.0`


## Time: `28.0980s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `142.0`


## Time: `28.1620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.007, S2/S1=0.19 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 27.998s (amp 0.042), key col 0.003
    -       Left trough: idx=13913 (27.826s), amp=0.001
    -       Right trough: idx=14049 (28.098s), amp=0.003
    - S2: prom 0.007, peak @ 28.162s (amp 0.011), key col 0.003
    -       Left trough: idx=14049 (28.098s), amp=0.003
    -       Right trough: idx=14139 (28.278s), amp=0.002
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `142.0`


## Time: `28.2780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.4`
- **Long-Term BPM (Belief)**: `142.0`


## Time: `28.4280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.008, S2/S1=0.22 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 28.428s (amp 0.038), key col 0.003
    -       Left trough: idx=14139 (28.278s), amp=0.002
    -       Right trough: idx=14261 (28.522s), amp=0.003
    - S2: prom 0.008, peak @ 28.596s (amp 0.011), key col 0.003
    -       Left trough: idx=14261 (28.522s), amp=0.003
    -       Right trough: idx=14367 (28.734s), amp=0.001
- **Raw Amp**: `0.038`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.1`
- **Long-Term BPM (Belief)**: `141.9`


## Time: `28.5220s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.1`
- **Long-Term BPM (Belief)**: `141.9`


## Time: `28.5960s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.008, S2/S1=0.22 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 28.428s (amp 0.038), key col 0.003
    -       Left trough: idx=14139 (28.278s), amp=0.002
    -       Right trough: idx=14261 (28.522s), amp=0.003
    - S2: prom 0.008, peak @ 28.596s (amp 0.011), key col 0.003
    -       Left trough: idx=14261 (28.522s), amp=0.003
    -       Right trough: idx=14367 (28.734s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.1`
- **Long-Term BPM (Belief)**: `141.9`


## Time: `28.7340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.1`
- **Long-Term BPM (Belief)**: `141.9`


## Time: `28.8380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.15 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 28.838s (amp 0.040), key col 0.003
    -       Left trough: idx=14367 (28.734s), amp=0.001
    -       Right trough: idx=14473 (28.946s), amp=0.003
    - S2: prom 0.006, peak @ 29.014s (amp 0.008), key col 0.003
    -       Left trough: idx=14473 (28.946s), amp=0.003
    -       Right trough: idx=14583 (29.166s), amp=0.001
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `142.1`


## Time: `28.9460s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `142.1`


## Time: `29.0140s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.15 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 28.838s (amp 0.040), key col 0.003
    -       Left trough: idx=14367 (28.734s), amp=0.001
    -       Right trough: idx=14473 (28.946s), amp=0.003
    - S2: prom 0.006, peak @ 29.014s (amp 0.008), key col 0.003
    -       Left trough: idx=14473 (28.946s), amp=0.003
    -       Right trough: idx=14583 (29.166s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `142.1`


## Time: `29.1660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `142.1`


## Time: `29.2880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 29.288s (amp 0.050), key col 0.001
    -       Left trough: idx=14583 (29.166s), amp=0.001
    -       Right trough: idx=14690 (29.380s), amp=0.001
    - S2: prom 0.003, peak @ 29.434s (amp 0.005), key col 0.001
    -       Left trough: idx=14690 (29.380s), amp=0.001
    -       Right trough: idx=14767 (29.534s), amp=0.000
- **Raw Amp**: `0.050`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.3800s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.4340s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.049, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.049, peak @ 29.288s (amp 0.050), key col 0.001
    -       Left trough: idx=14583 (29.166s), amp=0.001
    -       Right trough: idx=14690 (29.380s), amp=0.001
    - S2: prom 0.003, peak @ 29.434s (amp 0.005), key col 0.001
    -       Left trough: idx=14690 (29.380s), amp=0.001
    -       Right trough: idx=14767 (29.534s), amp=0.000
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.5340s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.7120s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 29.712s (amp 0.044), key col 0.001
    -       Left trough: idx=14767 (29.534s), amp=0.000
    -       Right trough: idx=14902 (29.804s), amp=0.001
    - S2: prom 0.003, peak @ 29.854s (amp 0.004), key col 0.001
    -       Left trough: idx=14902 (29.804s), amp=0.001
    -       Right trough: idx=14987 (29.974s), amp=0.001
- **Raw Amp**: `0.044`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.8040s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.8540s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 29.712s (amp 0.044), key col 0.001
    -       Left trough: idx=14767 (29.534s), amp=0.000
    -       Right trough: idx=14902 (29.804s), amp=0.001
    - S2: prom 0.003, peak @ 29.854s (amp 0.004), key col 0.001
    -       Left trough: idx=14902 (29.804s), amp=0.001
    -       Right trough: idx=14987 (29.974s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `29.9740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.3`
- **Long-Term BPM (Belief)**: `141.7`


## Time: `30.1680s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.003, S2/S1=0.08 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 30.168s (amp 0.042), key col 0.003
    -       Left trough: idx=14987 (29.974s), amp=0.001
    -       Right trough: idx=15121 (30.242s), amp=0.003
    - S2: prom 0.003, peak @ 30.310s (amp 0.006), key col 0.003
    -       Left trough: idx=15121 (30.242s), amp=0.003
    -       Right trough: idx=15192 (30.384s), amp=0.003
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.2420s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.3100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.003, S2/S1=0.08 (Expected max 1.20 at 142 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 142 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 30.168s (amp 0.042), key col 0.003
    -       Left trough: idx=14987 (29.974s), amp=0.001
    -       Right trough: idx=15121 (30.242s), amp=0.003
    - S2: prom 0.003, peak @ 30.310s (amp 0.006), key col 0.003
    -       Left trough: idx=15121 (30.242s), amp=0.003
    -       Right trough: idx=15192 (30.384s), amp=0.003
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.3840s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.4640s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.002, S2=0.042, S2/S1=24.93 (Expected max 1.20 at 141 BPM)
    - Contractility Penalty: -6.92 (S2 too prominent for BPM; prominence ratio 24.93 > expected 1.20) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.55: interval 0.296s vs expected 0.425s (deviation 30%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.10: strength ratio 0.10x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.55 x 0.65) + (Amplitude 0.10 x 0.35) = 0.396
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.150s < 0.187s (45% of expected RR) and strength ratio 0.12x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~400 BPM.
    - Confidence penalized 0.52x -> 0.40 to 0.21.
    - Outcome: Rejected Lone S1 (score 0.21 < threshold 0.50)
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.5240s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `140.9`


## Time: `30.6140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 141 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 141 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 30.614s (amp 0.045), key col 0.004
    -       Left trough: idx=15262 (30.524s), amp=0.004
    -       Right trough: idx=15348 (30.696s), amp=0.002
    - S2: prom 0.003, peak @ 30.786s (amp 0.005), key col 0.002
    -       Left trough: idx=15348 (30.696s), amp=0.002
    -       Right trough: idx=15493 (30.986s), amp=0.001
- **Raw Amp**: `0.045`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.5`
- **Long-Term BPM (Belief)**: `140.4`


## Time: `30.6960s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.5`
- **Long-Term BPM (Belief)**: `140.4`


## Time: `30.7860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.003, S2/S1=0.07 (Expected max 1.20 at 141 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 141 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 30.614s (amp 0.045), key col 0.004
    -       Left trough: idx=15262 (30.524s), amp=0.004
    -       Right trough: idx=15348 (30.696s), amp=0.002
    - S2: prom 0.003, peak @ 30.786s (amp 0.005), key col 0.002
    -       Left trough: idx=15348 (30.696s), amp=0.002
    -       Right trough: idx=15493 (30.986s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.5`
- **Long-Term BPM (Belief)**: `140.4`


## Time: `30.9860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.5`
- **Long-Term BPM (Belief)**: `140.4`


## Time: `31.0860s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.003, S2/S1=0.12 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 31.086s (amp 0.030), key col 0.002
    -       Left trough: idx=15493 (30.986s), amp=0.001
    -       Right trough: idx=15590 (31.180s), amp=0.002
    - S2: prom 0.003, peak @ 31.280s (amp 0.006), key col 0.002
    -       Left trough: idx=15590 (31.180s), amp=0.002
    -       Right trough: idx=15685 (31.370s), amp=0.002
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `139.7`


## Time: `31.1800s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `139.7`


## Time: `31.2800s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.003, S2/S1=0.12 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 31.086s (amp 0.030), key col 0.002
    -       Left trough: idx=15493 (30.986s), amp=0.001
    -       Right trough: idx=15590 (31.180s), amp=0.002
    - S2: prom 0.003, peak @ 31.280s (amp 0.006), key col 0.002
    -       Left trough: idx=15590 (31.180s), amp=0.002
    -       Right trough: idx=15685 (31.370s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `139.7`


## Time: `31.3700s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `139.7`


## Time: `31.5540s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.002, S2/S1=0.05 (Expected max 1.21 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 31.554s (amp 0.044), key col 0.004
    -       Left trough: idx=15685 (31.370s), amp=0.002
    -       Right trough: idx=15824 (31.648s), amp=0.004
    - S2: prom 0.002, peak @ 31.728s (amp 0.006), key col 0.004
    -       Left trough: idx=15824 (31.648s), amp=0.004
    -       Right trough: idx=15909 (31.818s), amp=0.002
- **Raw Amp**: `0.044`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.9`
- **Long-Term BPM (Belief)**: `139.1`


## Time: `31.6480s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.9`
- **Long-Term BPM (Belief)**: `139.1`


## Time: `31.7280s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.002, S2/S1=0.05 (Expected max 1.21 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 31.554s (amp 0.044), key col 0.004
    -       Left trough: idx=15685 (31.370s), amp=0.002
    -       Right trough: idx=15824 (31.648s), amp=0.004
    - S2: prom 0.002, peak @ 31.728s (amp 0.006), key col 0.004
    -       Left trough: idx=15824 (31.648s), amp=0.004
    -       Right trough: idx=15909 (31.818s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.9`
- **Long-Term BPM (Belief)**: `139.1`


## Time: `31.8180s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `136.9`
- **Long-Term BPM (Belief)**: `139.1`


## Time: `31.9920s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.008, S2/S1=0.18 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 31.992s (amp 0.049), key col 0.004
    -       Left trough: idx=15909 (31.818s), amp=0.002
    -       Right trough: idx=16028 (32.056s), amp=0.004
    - S2: prom 0.008, peak @ 32.136s (amp 0.012), key col 0.004
    -       Left trough: idx=16028 (32.056s), amp=0.004
    -       Right trough: idx=16118 (32.236s), amp=0.004
- **Raw Amp**: `0.049`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.5`
- **Long-Term BPM (Belief)**: `139.0`


## Time: `32.0560s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.5`
- **Long-Term BPM (Belief)**: `139.0`


## Time: `32.1360s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.008, S2/S1=0.18 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 31.992s (amp 0.049), key col 0.004
    -       Left trough: idx=15909 (31.818s), amp=0.002
    -       Right trough: idx=16028 (32.056s), amp=0.004
    - S2: prom 0.008, peak @ 32.136s (amp 0.012), key col 0.004
    -       Left trough: idx=16028 (32.056s), amp=0.004
    -       Right trough: idx=16118 (32.236s), amp=0.004
- **Raw Amp**: `0.012`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.5`
- **Long-Term BPM (Belief)**: `139.0`


## Time: `32.2360s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.5`
- **Long-Term BPM (Belief)**: `139.0`


## Time: `32.3900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.006, S2/S1=0.15 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 32.390s (amp 0.047), key col 0.004
    -       Left trough: idx=16118 (32.236s), amp=0.004
    -       Right trough: idx=16245 (32.490s), amp=0.004
    - S2: prom 0.006, peak @ 32.590s (amp 0.011), key col 0.004
    -       Left trough: idx=16245 (32.490s), amp=0.004
    -       Right trough: idx=16356 (32.712s), amp=0.002
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.1`
- **Long-Term BPM (Belief)**: `139.6`


## Time: `32.4900s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.1`
- **Long-Term BPM (Belief)**: `139.6`


## Time: `32.5900s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.006, S2/S1=0.15 (Expected max 1.22 at 139 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 139 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 32.390s (amp 0.047), key col 0.004
    -       Left trough: idx=16118 (32.236s), amp=0.004
    -       Right trough: idx=16245 (32.490s), amp=0.004
    - S2: prom 0.006, peak @ 32.590s (amp 0.011), key col 0.004
    -       Left trough: idx=16245 (32.490s), amp=0.004
    -       Right trough: idx=16356 (32.712s), amp=0.002
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.1`
- **Long-Term BPM (Belief)**: `139.6`


## Time: `32.7120s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.1`
- **Long-Term BPM (Belief)**: `139.6`


## Time: `32.8100s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.006, S2/S1=0.18 (Expected max 1.21 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 32.810s (amp 0.036), key col 0.002
    -       Left trough: idx=16356 (32.712s), amp=0.002
    -       Right trough: idx=16464 (32.928s), amp=0.001
    - S2: prom 0.006, peak @ 33.022s (amp 0.008), key col 0.001
    -       Left trough: idx=16464 (32.928s), amp=0.001
    -       Right trough: idx=16547 (33.094s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.0`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `32.9280s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.0`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `33.0220s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.006, S2/S1=0.18 (Expected max 1.21 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 32.810s (amp 0.036), key col 0.002
    -       Left trough: idx=16356 (32.712s), amp=0.002
    -       Right trough: idx=16464 (32.928s), amp=0.001
    - S2: prom 0.006, peak @ 33.022s (amp 0.008), key col 0.001
    -       Left trough: idx=16464 (32.928s), amp=0.001
    -       Right trough: idx=16547 (33.094s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.0`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `33.0940s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.0`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `33.2340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.005, S2/S1=0.13 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 33.234s (amp 0.041), key col 0.001
    -       Left trough: idx=16547 (33.094s), amp=0.001
    -       Right trough: idx=16668 (33.336s), amp=0.001
    - S2: prom 0.005, peak @ 33.392s (amp 0.006), key col 0.001
    -       Left trough: idx=16668 (33.336s), amp=0.001
    -       Right trough: idx=16762 (33.524s), amp=0.000
- **Raw Amp**: `0.041`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `139.9`


## Time: `33.3360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `139.9`


## Time: `33.3920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.005, S2/S1=0.13 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 33.234s (amp 0.041), key col 0.001
    -       Left trough: idx=16547 (33.094s), amp=0.001
    -       Right trough: idx=16668 (33.336s), amp=0.001
    - S2: prom 0.005, peak @ 33.392s (amp 0.006), key col 0.001
    -       Left trough: idx=16668 (33.336s), amp=0.001
    -       Right trough: idx=16762 (33.524s), amp=0.000
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `139.9`


## Time: `33.5240s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `139.9`


## Time: `33.6700s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.11 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 33.670s (amp 0.035), key col 0.001
    -       Left trough: idx=16762 (33.524s), amp=0.000
    -       Right trough: idx=16884 (33.768s), amp=0.001
    - S2: prom 0.004, peak @ 33.812s (amp 0.005), key col 0.001
    -       Left trough: idx=16884 (33.768s), amp=0.001
    -       Right trough: idx=17028 (34.056s), amp=0.000
- **Raw Amp**: `0.035`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `33.7680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `33.8120s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.11 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 33.670s (amp 0.035), key col 0.001
    -       Left trough: idx=16762 (33.524s), amp=0.000
    -       Right trough: idx=16884 (33.768s), amp=0.001
    - S2: prom 0.004, peak @ 33.812s (amp 0.005), key col 0.001
    -       Left trough: idx=16884 (33.768s), amp=0.001
    -       Right trough: idx=17028 (34.056s), amp=0.000
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `34.0560s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `139.8`


## Time: `34.2340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.002, S2/S1=0.10 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 34.234s (amp 0.026), key col 0.001
    -       Left trough: idx=17028 (34.056s), amp=0.000
    -       Right trough: idx=17159 (34.318s), amp=0.001
    - S2: prom 0.002, peak @ 34.376s (amp 0.003), key col 0.001
    -       Left trough: idx=17159 (34.318s), amp=0.001
    -       Right trough: idx=17331 (34.662s), amp=0.000
- **Raw Amp**: `0.026`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.8`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `34.3180s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.8`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `34.3760s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.002, S2/S1=0.10 (Expected max 1.20 at 140 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 140 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 34.234s (amp 0.026), key col 0.001
    -       Left trough: idx=17028 (34.056s), amp=0.000
    -       Right trough: idx=17159 (34.318s), amp=0.001
    - S2: prom 0.002, peak @ 34.376s (amp 0.003), key col 0.001
    -       Left trough: idx=17159 (34.318s), amp=0.001
    -       Right trough: idx=17331 (34.662s), amp=0.000
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.8`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `34.6620s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.8`
- **Long-Term BPM (Belief)**: `138.1`


## Time: `34.8080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.001, S2/S1=0.06 (Expected max 1.24 at 138 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 138 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 34.808s (amp 0.021), key col 0.002
    -       Left trough: idx=17331 (34.662s), amp=0.000
    -       Right trough: idx=17448 (34.896s), amp=0.002
    - S2: prom 0.001, peak @ 34.936s (amp 0.003), key col 0.002
    -       Left trough: idx=17448 (34.896s), amp=0.002
    -       Right trough: idx=17594 (35.188s), amp=0.000
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `123.4`
- **Long-Term BPM (Belief)**: `136.4`


## Time: `34.8960s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `123.4`
- **Long-Term BPM (Belief)**: `136.4`


## Time: `34.9360s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.001, S2/S1=0.06 (Expected max 1.24 at 138 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 138 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 34.808s (amp 0.021), key col 0.002
    -       Left trough: idx=17331 (34.662s), amp=0.000
    -       Right trough: idx=17448 (34.896s), amp=0.002
    - S2: prom 0.001, peak @ 34.936s (amp 0.003), key col 0.002
    -       Left trough: idx=17448 (34.896s), amp=0.002
    -       Right trough: idx=17594 (35.188s), amp=0.000
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `123.4`
- **Long-Term BPM (Belief)**: `136.4`


## Time: `35.1880s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `123.4`
- **Long-Term BPM (Belief)**: `136.4`


## Time: `35.3800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.08 (Expected max 1.27 at 136 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 136 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 35.380s (amp 0.021), key col 0.000
    -       Left trough: idx=17594 (35.188s), amp=0.000
    -       Right trough: idx=17843 (35.686s), amp=0.000
    - S2: prom 0.002, peak @ 35.520s (amp 0.002), key col 0.000
    -       Left trough: idx=17594 (35.188s), amp=0.000
    -       Right trough: idx=17843 (35.686s), amp=0.000
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `134.8`


## Time: `35.5200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.08 (Expected max 1.27 at 136 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 136 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 35.380s (amp 0.021), key col 0.000
    -       Left trough: idx=17594 (35.188s), amp=0.000
    -       Right trough: idx=17843 (35.686s), amp=0.000
    - S2: prom 0.002, peak @ 35.520s (amp 0.002), key col 0.000
    -       Left trough: idx=17594 (35.188s), amp=0.000
    -       Right trough: idx=17843 (35.686s), amp=0.000
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `134.8`


## Time: `35.6860s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `134.8`


## Time: `35.9360s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.001, S2/S1=0.09 (Expected max 1.30 at 135 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 135 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 35.936s (amp 0.016), key col 0.001
    -       Left trough: idx=17843 (35.686s), amp=0.000
    -       Right trough: idx=18096 (36.192s), amp=0.001
    - S2: prom 0.001, peak @ 36.084s (amp 0.002), key col 0.001
    -       Left trough: idx=17843 (35.686s), amp=0.000
    -       Right trough: idx=18096 (36.192s), amp=0.001
- **Raw Amp**: `0.016`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.0`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `36.0840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.001, S2/S1=0.09 (Expected max 1.30 at 135 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 135 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 35.936s (amp 0.016), key col 0.001
    -       Left trough: idx=17843 (35.686s), amp=0.000
    -       Right trough: idx=18096 (36.192s), amp=0.001
    - S2: prom 0.001, peak @ 36.084s (amp 0.002), key col 0.001
    -       Left trough: idx=17843 (35.686s), amp=0.000
    -       Right trough: idx=18096 (36.192s), amp=0.001
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.0`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `36.1920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `120.0`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `36.4600s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.004, S2/S1=0.25 (Expected max 1.33 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 36.460s (amp 0.019), key col 0.002
    -       Left trough: idx=18096 (36.192s), amp=0.001
    -       Right trough: idx=18278 (36.556s), amp=0.002
    - S2: prom 0.004, peak @ 36.644s (amp 0.007), key col 0.002
    -       Left trough: idx=18278 (36.556s), amp=0.002
    -       Right trough: idx=18370 (36.740s), amp=0.002
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `121.9`
- **Long-Term BPM (Belief)**: `132.5`


## Time: `36.5560s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `121.9`
- **Long-Term BPM (Belief)**: `132.5`


## Time: `36.6440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.004, S2/S1=0.25 (Expected max 1.33 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 36.460s (amp 0.019), key col 0.002
    -       Left trough: idx=18096 (36.192s), amp=0.001
    -       Right trough: idx=18278 (36.556s), amp=0.002
    - S2: prom 0.004, peak @ 36.644s (amp 0.007), key col 0.002
    -       Left trough: idx=18278 (36.556s), amp=0.002
    -       Right trough: idx=18370 (36.740s), amp=0.002
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `121.9`
- **Long-Term BPM (Belief)**: `132.5`


## Time: `36.7400s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `121.9`
- **Long-Term BPM (Belief)**: `132.5`


## Time: `36.9460s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.004, S2/S1=0.30 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 36.946s (amp 0.014), key col 0.002
    -       Left trough: idx=18370 (36.740s), amp=0.002
    -       Right trough: idx=18508 (37.016s), amp=0.002
    - S2: prom 0.004, peak @ 37.126s (amp 0.006), key col 0.002
    -       Left trough: idx=18508 (37.016s), amp=0.002
    -       Right trough: idx=18605 (37.210s), amp=0.002
- **Raw Amp**: `0.014`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.9`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `37.0160s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.9`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `37.1260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.004, S2/S1=0.30 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 36.946s (amp 0.014), key col 0.002
    -       Left trough: idx=18370 (36.740s), amp=0.002
    -       Right trough: idx=18508 (37.016s), amp=0.002
    - S2: prom 0.004, peak @ 37.126s (amp 0.006), key col 0.002
    -       Left trough: idx=18508 (37.016s), amp=0.002
    -       Right trough: idx=18605 (37.210s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.9`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `37.2100s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.000`
- **Average BPM (Smoothed)**: `124.9`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `37.4040s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.001, S2/S1=0.02 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 37.404s (amp 0.046), key col 0.003
    -       Left trough: idx=18605 (37.210s), amp=0.002
    -       Right trough: idx=18753 (37.506s), amp=0.003
    - S2: prom 0.001, peak @ 37.564s (amp 0.004), key col 0.003
    -       Left trough: idx=18753 (37.506s), amp=0.003
    -       Right trough: idx=18850 (37.700s), amp=0.002
- **Raw Amp**: `0.046`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.0`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `37.5060s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.0`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `37.5640s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.043, S2=0.001, S2/S1=0.02 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.043, peak @ 37.404s (amp 0.046), key col 0.003
    -       Left trough: idx=18605 (37.210s), amp=0.002
    -       Right trough: idx=18753 (37.506s), amp=0.003
    - S2: prom 0.001, peak @ 37.564s (amp 0.004), key col 0.003
    -       Left trough: idx=18753 (37.506s), amp=0.003
    -       Right trough: idx=18850 (37.700s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.0`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `37.7000s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.0`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `37.8520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.002, S2/S1=0.05 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 37.852s (amp 0.036), key col 0.002
    -       Left trough: idx=18850 (37.700s), amp=0.002
    -       Right trough: idx=18974 (37.948s), amp=0.001
    - S2: prom 0.002, peak @ 38.044s (amp 0.004), key col 0.002
    -       Left trough: idx=18974 (37.948s), amp=0.001
    -       Right trough: idx=19041 (38.082s), amp=0.002
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.2`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `37.9480s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.2`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `38.0440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.002, S2/S1=0.05 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 37.852s (amp 0.036), key col 0.002
    -       Left trough: idx=18850 (37.700s), amp=0.002
    -       Right trough: idx=18974 (37.948s), amp=0.001
    - S2: prom 0.002, peak @ 38.044s (amp 0.004), key col 0.002
    -       Left trough: idx=18974 (37.948s), amp=0.001
    -       Right trough: idx=19041 (38.082s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.2`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `38.0820s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.2`
- **Long-Term BPM (Belief)**: `132.1`


## Time: `38.2940s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.003, S2/S1=0.05 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 38.294s (amp 0.058), key col 0.006
    -       Left trough: idx=19041 (38.082s), amp=0.002
    -       Right trough: idx=19199 (38.398s), amp=0.006
    - S2: prom 0.003, peak @ 38.440s (amp 0.009), key col 0.006
    -       Left trough: idx=19199 (38.398s), amp=0.006
    -       Right trough: idx=19288 (38.576s), amp=0.003
- **Raw Amp**: `0.058`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `132.3`


## Time: `38.3980s`
**Trough Detected**
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `132.3`


## Time: `38.4400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.052, S2=0.003, S2/S1=0.05 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.052, peak @ 38.294s (amp 0.058), key col 0.006
    -       Left trough: idx=19041 (38.082s), amp=0.002
    -       Right trough: idx=19199 (38.398s), amp=0.006
    - S2: prom 0.003, peak @ 38.440s (amp 0.009), key col 0.006
    -       Left trough: idx=19199 (38.398s), amp=0.006
    -       Right trough: idx=19288 (38.576s), amp=0.003
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `132.3`


## Time: `38.5760s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `132.3`


## Time: `38.6780s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.008, S2/S1=0.18 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 38.678s (amp 0.044), key col 0.003
    -       Left trough: idx=19288 (38.576s), amp=0.003
    -       Right trough: idx=19401 (38.802s), amp=0.002
    - S2: prom 0.008, peak @ 38.902s (amp 0.009), key col 0.002
    -       Left trough: idx=19401 (38.802s), amp=0.002
    -       Right trough: idx=19477 (38.954s), amp=0.002
- **Raw Amp**: `0.044`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `38.8020s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `38.9020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.008, S2/S1=0.18 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 38.678s (amp 0.044), key col 0.003
    -       Left trough: idx=19288 (38.576s), amp=0.003
    -       Right trough: idx=19401 (38.802s), amp=0.002
    - S2: prom 0.008, peak @ 38.902s (amp 0.009), key col 0.002
    -       Left trough: idx=19401 (38.802s), amp=0.002
    -       Right trough: idx=19477 (38.954s), amp=0.002
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `38.9540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `39.1180s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.007, S2/S1=0.13 (Expected max 1.33 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 39.118s (amp 0.056), key col 0.002
    -       Left trough: idx=19477 (38.954s), amp=0.002
    -       Right trough: idx=19608 (39.216s), amp=0.001
    - S2: prom 0.007, peak @ 39.282s (amp 0.008), key col 0.001
    -       Left trough: idx=19608 (39.216s), amp=0.001
    -       Right trough: idx=19712 (39.424s), amp=0.001
- **Raw Amp**: `0.056`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `133.6`


## Time: `39.2160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `133.6`


## Time: `39.2820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.055, S2=0.007, S2/S1=0.13 (Expected max 1.33 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.055, peak @ 39.118s (amp 0.056), key col 0.002
    -       Left trough: idx=19477 (38.954s), amp=0.002
    -       Right trough: idx=19608 (39.216s), amp=0.001
    - S2: prom 0.007, peak @ 39.282s (amp 0.008), key col 0.001
    -       Left trough: idx=19608 (39.216s), amp=0.001
    -       Right trough: idx=19712 (39.424s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `133.6`


## Time: `39.4240s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `133.6`


## Time: `39.5300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.003, S2/S1=0.05 (Expected max 1.33 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 39.530s (amp 0.059), key col 0.001
    -       Left trough: idx=19712 (39.424s), amp=0.001
    -       Right trough: idx=19818 (39.636s), amp=0.001
    - S2: prom 0.003, peak @ 39.684s (amp 0.004), key col 0.001
    -       Left trough: idx=19818 (39.636s), amp=0.001
    -       Right trough: idx=19901 (39.802s), amp=0.001
- **Raw Amp**: `0.059`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.3`
- **Long-Term BPM (Belief)**: `134.2`


## Time: `39.6360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.3`
- **Long-Term BPM (Belief)**: `134.2`


## Time: `39.6840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.057, S2=0.003, S2/S1=0.05 (Expected max 1.33 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.057, peak @ 39.530s (amp 0.059), key col 0.001
    -       Left trough: idx=19712 (39.424s), amp=0.001
    -       Right trough: idx=19818 (39.636s), amp=0.001
    - S2: prom 0.003, peak @ 39.684s (amp 0.004), key col 0.001
    -       Left trough: idx=19818 (39.636s), amp=0.001
    -       Right trough: idx=19901 (39.802s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.3`
- **Long-Term BPM (Belief)**: `134.2`


## Time: `39.8020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.3`
- **Long-Term BPM (Belief)**: `134.2`


## Time: `40.0280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.003, S2/S1=0.08 (Expected max 1.32 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 40.028s (amp 0.042), key col 0.001
    -       Left trough: idx=19901 (39.802s), amp=0.001
    -       Right trough: idx=20068 (40.136s), amp=0.001
    - S2: prom 0.003, peak @ 40.194s (amp 0.005), key col 0.001
    -       Left trough: idx=20068 (40.136s), amp=0.001
    -       Right trough: idx=20275 (40.550s), amp=0.001
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.1`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `40.1360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.1`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `40.1940s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.003, S2/S1=0.08 (Expected max 1.32 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 40.028s (amp 0.042), key col 0.001
    -       Left trough: idx=19901 (39.802s), amp=0.001
    -       Right trough: idx=20068 (40.136s), amp=0.001
    - S2: prom 0.003, peak @ 40.194s (amp 0.005), key col 0.001
    -       Left trough: idx=20068 (40.136s), amp=0.001
    -       Right trough: idx=20275 (40.550s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.1`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `40.5500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.1`
- **Long-Term BPM (Belief)**: `133.5`


## Time: `40.8900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.09 (Expected max 1.33 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 40.890s (amp 0.034), key col 0.003
    -       Left trough: idx=20275 (40.550s), amp=0.001
    -       Right trough: idx=20496 (40.992s), amp=0.003
    - S2: prom 0.003, peak @ 41.062s (amp 0.005), key col 0.003
    -       Left trough: idx=20496 (40.992s), amp=0.003
    -       Right trough: idx=20727 (41.454s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.5`
- **Long-Term BPM (Belief)**: `130.9`


## Time: `40.9920s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.5`
- **Long-Term BPM (Belief)**: `130.9`


## Time: `41.0620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.09 (Expected max 1.33 at 134 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 134 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 40.890s (amp 0.034), key col 0.003
    -       Left trough: idx=20275 (40.550s), amp=0.001
    -       Right trough: idx=20496 (40.992s), amp=0.003
    - S2: prom 0.003, peak @ 41.062s (amp 0.005), key col 0.003
    -       Left trough: idx=20496 (40.992s), amp=0.003
    -       Right trough: idx=20727 (41.454s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.5`
- **Long-Term BPM (Belief)**: `130.9`


## Time: `41.4540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.5`
- **Long-Term BPM (Belief)**: `130.9`


## Time: `41.5580s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.005, S2/S1=0.16 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 41.558s (amp 0.035), key col 0.002
    -       Left trough: idx=20727 (41.454s), amp=0.001
    -       Right trough: idx=20833 (41.666s), amp=0.002
    - S2: prom 0.005, peak @ 41.732s (amp 0.007), key col 0.002
    -       Left trough: idx=20833 (41.666s), amp=0.002
    -       Right trough: idx=20982 (41.964s), amp=0.000
- **Raw Amp**: `0.035`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `41.6660s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `41.7320s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.005, S2/S1=0.16 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 41.558s (amp 0.035), key col 0.002
    -       Left trough: idx=20727 (41.454s), amp=0.001
    -       Right trough: idx=20833 (41.666s), amp=0.002
    - S2: prom 0.005, peak @ 41.732s (amp 0.007), key col 0.002
    -       Left trough: idx=20833 (41.666s), amp=0.002
    -       Right trough: idx=20982 (41.964s), amp=0.000
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `41.9640s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `42.1460s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.21 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 42.146s (amp 0.023), key col 0.002
    -       Left trough: idx=20982 (41.964s), amp=0.000
    -       Right trough: idx=21127 (42.254s), amp=0.002
    - S2: prom 0.004, peak @ 42.304s (amp 0.006), key col 0.002
    -       Left trough: idx=21127 (42.254s), amp=0.002
    -       Right trough: idx=21237 (42.474s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.1`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `42.2540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.1`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `42.3040s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.21 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 42.146s (amp 0.023), key col 0.002
    -       Left trough: idx=20982 (41.964s), amp=0.000
    -       Right trough: idx=21127 (42.254s), amp=0.002
    - S2: prom 0.004, peak @ 42.304s (amp 0.006), key col 0.002
    -       Left trough: idx=21127 (42.254s), amp=0.002
    -       Right trough: idx=21237 (42.474s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.1`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `42.4740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.1`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `42.7120s`
**S1 (Paired).**
- LOOKAHEAD SUCCESS: Skipped intermediate weak peak (middle prominence 0.004 < 0.35 × S1 prominence 0.037 and next candidate prominence 0.007 > middle)
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.007, S2/S1=0.19 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Interval penalty by 0.11 (Interval 0.348s > Max 0.329s)
    - Final Score: 0.87 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 42.712s (amp 0.039), key col 0.002
    -       Left trough: idx=21237 (42.474s), amp=0.001
    -       Right trough: idx=21410 (42.820s), amp=0.002
    - S2: prom 0.007, peak @ 43.060s (amp 0.009), key col 0.002
    -       Left trough: idx=21482 (42.964s), amp=0.002
    -       Right trough: idx=21614 (43.228s), amp=0.001
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `42.8200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `42.8820s`
**Noise/Rejected.**
- Middle peak treated as noise due to weak prominence (0.004 < 0.35 × S1 prominence 0.037) and the following candidate is stronger (next prominence 0.007).
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `42.9640s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `43.0600s`
**S2 (Paired).**
- LOOKAHEAD SUCCESS: Skipped intermediate weak peak (middle prominence 0.004 < 0.35 × S1 prominence 0.037 and next candidate prominence 0.007 > middle)
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.007, S2/S1=0.19 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Interval penalty by 0.11 (Interval 0.348s > Max 0.329s)
    - Final Score: 0.87 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 42.712s (amp 0.039), key col 0.002
    -       Left trough: idx=21237 (42.474s), amp=0.001
    -       Right trough: idx=21410 (42.820s), amp=0.002
    - S2: prom 0.007, peak @ 43.060s (amp 0.009), key col 0.002
    -       Left trough: idx=21482 (42.964s), amp=0.002
    -       Right trough: idx=21614 (43.228s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `43.2280s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.9`
- **Long-Term BPM (Belief)**: `126.5`


## Time: `43.3400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.005, S2/S1=0.12 (Expected max 1.47 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 43.340s (amp 0.042), key col 0.003
    -       Left trough: idx=21614 (43.228s), amp=0.001
    -       Right trough: idx=21715 (43.430s), amp=0.003
    - S2: prom 0.005, peak @ 43.474s (amp 0.007), key col 0.003
    -       Left trough: idx=21715 (43.430s), amp=0.003
    -       Right trough: idx=21887 (43.774s), amp=0.001
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.1`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `43.4300s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.1`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `43.4740s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.005, S2/S1=0.12 (Expected max 1.47 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 43.340s (amp 0.042), key col 0.003
    -       Left trough: idx=21614 (43.228s), amp=0.001
    -       Right trough: idx=21715 (43.430s), amp=0.003
    - S2: prom 0.005, peak @ 43.474s (amp 0.007), key col 0.003
    -       Left trough: idx=21715 (43.430s), amp=0.003
    -       Right trough: idx=21887 (43.774s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.1`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `43.7740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.1`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `43.9480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.004, S2/S1=0.13 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 43.948s (amp 0.033), key col 0.003
    -       Left trough: idx=21887 (43.774s), amp=0.001
    -       Right trough: idx=22020 (44.040s), amp=0.003
    - S2: prom 0.004, peak @ 44.120s (amp 0.007), key col 0.003
    -       Left trough: idx=22020 (44.040s), amp=0.003
    -       Right trough: idx=22170 (44.340s), amp=0.001
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `44.0400s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `44.1200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.004, S2/S1=0.13 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 43.948s (amp 0.033), key col 0.003
    -       Left trough: idx=21887 (43.774s), amp=0.001
    -       Right trough: idx=22020 (44.040s), amp=0.003
    - S2: prom 0.004, peak @ 44.120s (amp 0.007), key col 0.003
    -       Left trough: idx=22020 (44.040s), amp=0.003
    -       Right trough: idx=22170 (44.340s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `44.3400s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `44.4900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.19 (Expected max 1.53 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 44.490s (amp 0.024), key col 0.002
    -       Left trough: idx=22170 (44.340s), amp=0.001
    -       Right trough: idx=22292 (44.584s), amp=0.002
    - S2: prom 0.004, peak @ 44.662s (amp 0.006), key col 0.002
    -       Left trough: idx=22292 (44.584s), amp=0.002
    -       Right trough: idx=22419 (44.838s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `115.7`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `44.5840s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `115.7`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `44.6620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.19 (Expected max 1.53 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 44.490s (amp 0.024), key col 0.002
    -       Left trough: idx=22170 (44.340s), amp=0.001
    -       Right trough: idx=22292 (44.584s), amp=0.002
    - S2: prom 0.004, peak @ 44.662s (amp 0.006), key col 0.002
    -       Left trough: idx=22292 (44.584s), amp=0.002
    -       Right trough: idx=22419 (44.838s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `115.7`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `44.8380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `115.7`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `44.9640s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.15 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 44.964s (amp 0.038), key col 0.002
    -       Left trough: idx=22419 (44.838s), amp=0.001
    -       Right trough: idx=22538 (45.076s), amp=0.002
    - S2: prom 0.006, peak @ 45.180s (amp 0.007), key col 0.002
    -       Left trough: idx=22538 (45.076s), amp=0.002
    -       Right trough: idx=22671 (45.342s), amp=0.001
- **Raw Amp**: `0.038`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `123.2`


## Time: `45.0760s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `123.2`


## Time: `45.1800s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.15 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 44.964s (amp 0.038), key col 0.002
    -       Left trough: idx=22419 (44.838s), amp=0.001
    -       Right trough: idx=22538 (45.076s), amp=0.002
    - S2: prom 0.006, peak @ 45.180s (amp 0.007), key col 0.002
    -       Left trough: idx=22538 (45.076s), amp=0.002
    -       Right trough: idx=22671 (45.342s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `123.2`


## Time: `45.3420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.6`
- **Long-Term BPM (Belief)**: `123.2`


## Time: `45.4660s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.001, S2/S1=0.04 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 45.466s (amp 0.043), key col 0.005
    -       Left trough: idx=22671 (45.342s), amp=0.001
    -       Right trough: idx=22784 (45.568s), amp=0.005
    - S2: prom 0.001, peak @ 45.618s (amp 0.006), key col 0.005
    -       Left trough: idx=22784 (45.568s), amp=0.005
    -       Right trough: idx=22907 (45.814s), amp=0.002
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.6`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `45.5680s`
**Trough Detected**
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.6`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `45.6180s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.001, S2/S1=0.04 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 45.466s (amp 0.043), key col 0.005
    -       Left trough: idx=22671 (45.342s), amp=0.001
    -       Right trough: idx=22784 (45.568s), amp=0.005
    - S2: prom 0.001, peak @ 45.618s (amp 0.006), key col 0.005
    -       Left trough: idx=22784 (45.568s), amp=0.005
    -       Right trough: idx=22907 (45.814s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.6`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `45.8140s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.6`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `45.9100s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.002, S2/S1=0.05 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 45.910s (amp 0.051), key col 0.003
    -       Left trough: idx=22907 (45.814s), amp=0.002
    -       Right trough: idx=22992 (45.984s), amp=0.003
    - S2: prom 0.002, peak @ 46.070s (amp 0.005), key col 0.003
    -       Left trough: idx=22992 (45.984s), amp=0.003
    -       Right trough: idx=23138 (46.276s), amp=0.002
- **Raw Amp**: `0.051`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `45.9840s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `46.0700s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.048, S2=0.002, S2/S1=0.05 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.048, peak @ 45.910s (amp 0.051), key col 0.003
    -       Left trough: idx=22907 (45.814s), amp=0.002
    -       Right trough: idx=22992 (45.984s), amp=0.003
    - S2: prom 0.002, peak @ 46.070s (amp 0.005), key col 0.003
    -       Left trough: idx=22992 (45.984s), amp=0.003
    -       Right trough: idx=23138 (46.276s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `46.2760s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `123.6`


## Time: `46.3740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.004, S2/S1=0.10 (Expected max 1.53 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 46.374s (amp 0.040), key col 0.002
    -       Left trough: idx=23138 (46.276s), amp=0.002
    -       Right trough: idx=23233 (46.466s), amp=0.002
    - S2: prom 0.004, peak @ 46.556s (amp 0.006), key col 0.002
    -       Left trough: idx=23233 (46.466s), amp=0.002
    -       Right trough: idx=23308 (46.616s), amp=0.001
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.9`
- **Long-Term BPM (Belief)**: `123.9`


## Time: `46.4660s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.9`
- **Long-Term BPM (Belief)**: `123.9`


## Time: `46.5560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.004, S2/S1=0.10 (Expected max 1.53 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 46.374s (amp 0.040), key col 0.002
    -       Left trough: idx=23138 (46.276s), amp=0.002
    -       Right trough: idx=23233 (46.466s), amp=0.002
    - S2: prom 0.004, peak @ 46.556s (amp 0.006), key col 0.002
    -       Left trough: idx=23233 (46.466s), amp=0.002
    -       Right trough: idx=23308 (46.616s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.9`
- **Long-Term BPM (Belief)**: `123.9`


## Time: `46.6160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.9`
- **Long-Term BPM (Belief)**: `123.9`


## Time: `46.8220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.002, S2/S1=0.08 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 46.822s (amp 0.034), key col 0.004
    -       Left trough: idx=23308 (46.616s), amp=0.001
    -       Right trough: idx=23446 (46.892s), amp=0.004
    - S2: prom 0.002, peak @ 46.970s (amp 0.007), key col 0.004
    -       Left trough: idx=23446 (46.892s), amp=0.004
    -       Right trough: idx=23534 (47.068s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `46.8920s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `46.9700s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.002, S2/S1=0.08 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 46.822s (amp 0.034), key col 0.004
    -       Left trough: idx=23308 (46.616s), amp=0.001
    -       Right trough: idx=23446 (46.892s), amp=0.004
    - S2: prom 0.002, peak @ 46.970s (amp 0.007), key col 0.004
    -       Left trough: idx=23446 (46.892s), amp=0.004
    -       Right trough: idx=23534 (47.068s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `47.0680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `47.2200s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.003, S2/S1=0.07 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 47.220s (amp 0.047), key col 0.003
    -       Left trough: idx=23534 (47.068s), amp=0.001
    -       Right trough: idx=23664 (47.328s), amp=0.003
    - S2: prom 0.003, peak @ 47.380s (amp 0.006), key col 0.003
    -       Left trough: idx=23664 (47.328s), amp=0.003
    -       Right trough: idx=23754 (47.508s), amp=0.001
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.7`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `47.3280s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.7`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `47.3800s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.003, S2/S1=0.07 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 47.220s (amp 0.047), key col 0.003
    -       Left trough: idx=23534 (47.068s), amp=0.001
    -       Right trough: idx=23664 (47.328s), amp=0.003
    - S2: prom 0.003, peak @ 47.380s (amp 0.006), key col 0.003
    -       Left trough: idx=23664 (47.328s), amp=0.003
    -       Right trough: idx=23754 (47.508s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.7`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `47.5080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `134.7`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `47.6620s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.06 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 47.662s (amp 0.055), key col 0.002
    -       Left trough: idx=23754 (47.508s), amp=0.001
    -       Right trough: idx=23875 (47.750s), amp=0.002
    - S2: prom 0.003, peak @ 47.802s (amp 0.005), key col 0.002
    -       Left trough: idx=23875 (47.750s), amp=0.002
    -       Right trough: idx=23988 (47.976s), amp=0.001
- **Raw Amp**: `0.055`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.7`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `47.7500s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.7`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `47.8020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.06 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 47.662s (amp 0.055), key col 0.002
    -       Left trough: idx=23754 (47.508s), amp=0.001
    -       Right trough: idx=23875 (47.750s), amp=0.002
    - S2: prom 0.003, peak @ 47.802s (amp 0.005), key col 0.002
    -       Left trough: idx=23875 (47.750s), amp=0.002
    -       Right trough: idx=23988 (47.976s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.7`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `47.9760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.7`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `48.0820s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.054, S2=0.002, S2/S1=0.04 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.054, peak @ 48.082s (amp 0.055), key col 0.001
    -       Left trough: idx=23988 (47.976s), amp=0.001
    -       Right trough: idx=24091 (48.182s), amp=0.001
    - S2: prom 0.002, peak @ 48.262s (amp 0.003), key col 0.001
    -       Left trough: idx=24091 (48.182s), amp=0.001
    -       Right trough: idx=24153 (48.306s), amp=0.001
- **Raw Amp**: `0.055`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `126.9`


## Time: `48.1820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `126.9`


## Time: `48.2620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.054, S2=0.002, S2/S1=0.04 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.054, peak @ 48.082s (amp 0.055), key col 0.001
    -       Left trough: idx=23988 (47.976s), amp=0.001
    -       Right trough: idx=24091 (48.182s), amp=0.001
    - S2: prom 0.002, peak @ 48.262s (amp 0.003), key col 0.001
    -       Left trough: idx=24091 (48.182s), amp=0.001
    -       Right trough: idx=24153 (48.306s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `126.9`


## Time: `48.3060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.7`
- **Long-Term BPM (Belief)**: `126.9`


## Time: `48.5260s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.050, S2=0.002, S2/S1=0.05 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.050, peak @ 48.526s (amp 0.052), key col 0.002
    -       Left trough: idx=24153 (48.306s), amp=0.001
    -       Right trough: idx=24304 (48.608s), amp=0.002
    - S2: prom 0.002, peak @ 48.706s (amp 0.004), key col 0.002
    -       Left trough: idx=24304 (48.608s), amp=0.002
    -       Right trough: idx=24375 (48.750s), amp=0.001
- **Raw Amp**: `0.052`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.9`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `48.6080s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.9`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `48.7060s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.050, S2=0.002, S2/S1=0.05 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.050, peak @ 48.526s (amp 0.052), key col 0.002
    -       Left trough: idx=24153 (48.306s), amp=0.001
    -       Right trough: idx=24304 (48.608s), amp=0.002
    - S2: prom 0.002, peak @ 48.706s (amp 0.004), key col 0.002
    -       Left trough: idx=24304 (48.608s), amp=0.002
    -       Right trough: idx=24375 (48.750s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.9`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `48.7500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.9`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `48.9540s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.003, S2/S1=0.07 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 48.954s (amp 0.047), key col 0.002
    -       Left trough: idx=24375 (48.750s), amp=0.001
    -       Right trough: idx=24526 (49.052s), amp=0.002
    - S2: prom 0.003, peak @ 49.146s (amp 0.005), key col 0.002
    -       Left trough: idx=24526 (49.052s), amp=0.002
    -       Right trough: idx=24646 (49.292s), amp=0.002
- **Raw Amp**: `0.047`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.1`
- **Long-Term BPM (Belief)**: `128.0`


## Time: `49.0520s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.1`
- **Long-Term BPM (Belief)**: `128.0`


## Time: `49.1460s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.003, S2/S1=0.07 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 48.954s (amp 0.047), key col 0.002
    -       Left trough: idx=24375 (48.750s), amp=0.001
    -       Right trough: idx=24526 (49.052s), amp=0.002
    - S2: prom 0.003, peak @ 49.146s (amp 0.005), key col 0.002
    -       Left trough: idx=24526 (49.052s), amp=0.002
    -       Right trough: idx=24646 (49.292s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.1`
- **Long-Term BPM (Belief)**: `128.0`


## Time: `49.2920s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `139.1`
- **Long-Term BPM (Belief)**: `128.0`


## Time: `49.4060s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.09 (Expected max 1.44 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 49.406s (amp 0.039), key col 0.003
    -       Left trough: idx=24646 (49.292s), amp=0.002
    -       Right trough: idx=24751 (49.502s), amp=0.003
    - S2: prom 0.003, peak @ 49.572s (amp 0.006), key col 0.003
    -       Left trough: idx=24751 (49.502s), amp=0.003
    -       Right trough: idx=24837 (49.674s), amp=0.001
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.5`
- **Long-Term BPM (Belief)**: `128.2`


## Time: `49.5020s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.5`
- **Long-Term BPM (Belief)**: `128.2`


## Time: `49.5720s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.09 (Expected max 1.44 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 49.406s (amp 0.039), key col 0.003
    -       Left trough: idx=24646 (49.292s), amp=0.002
    -       Right trough: idx=24751 (49.502s), amp=0.003
    - S2: prom 0.003, peak @ 49.572s (amp 0.006), key col 0.003
    -       Left trough: idx=24751 (49.502s), amp=0.003
    -       Right trough: idx=24837 (49.674s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.5`
- **Long-Term BPM (Belief)**: `128.2`


## Time: `49.6740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `140.5`
- **Long-Term BPM (Belief)**: `128.2`


## Time: `49.8440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.005, S2/S1=0.17 (Expected max 1.44 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 49.844s (amp 0.029), key col 0.002
    -       Left trough: idx=24837 (49.674s), amp=0.001
    -       Right trough: idx=24968 (49.936s), amp=0.002
    - S2: prom 0.005, peak @ 49.992s (amp 0.006), key col 0.002
    -       Left trough: idx=24968 (49.936s), amp=0.002
    -       Right trough: idx=25083 (50.166s), amp=0.002
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `128.7`


## Time: `49.9360s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `128.7`


## Time: `49.9920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.005, S2/S1=0.17 (Expected max 1.44 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 49.844s (amp 0.029), key col 0.002
    -       Left trough: idx=24837 (49.674s), amp=0.001
    -       Right trough: idx=24968 (49.936s), amp=0.002
    - S2: prom 0.005, peak @ 49.992s (amp 0.006), key col 0.002
    -       Left trough: idx=24968 (49.936s), amp=0.002
    -       Right trough: idx=25083 (50.166s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `128.7`


## Time: `50.1660s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `128.7`


## Time: `50.2680s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.004, S2/S1=0.13 (Expected max 1.43 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 50.268s (amp 0.030), key col 0.002
    -       Left trough: idx=25083 (50.166s), amp=0.002
    -       Right trough: idx=25182 (50.364s), amp=0.002
    - S2: prom 0.004, peak @ 50.424s (amp 0.005), key col 0.002
    -       Left trough: idx=25182 (50.364s), amp=0.002
    -       Right trough: idx=25267 (50.534s), amp=0.001
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.3`


## Time: `50.3640s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.3`


## Time: `50.4240s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.004, S2/S1=0.13 (Expected max 1.43 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 50.268s (amp 0.030), key col 0.002
    -       Left trough: idx=25083 (50.166s), amp=0.002
    -       Right trough: idx=25182 (50.364s), amp=0.002
    - S2: prom 0.004, peak @ 50.424s (amp 0.005), key col 0.002
    -       Left trough: idx=25182 (50.364s), amp=0.002
    -       Right trough: idx=25267 (50.534s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.3`


## Time: `50.5340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.3`


## Time: `50.7020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.001, S2/S1=0.02 (Expected max 1.41 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 50.702s (amp 0.049), key col 0.003
    -       Left trough: idx=25267 (50.534s), amp=0.001
    -       Right trough: idx=25400 (50.800s), amp=0.003
    - S2: prom 0.001, peak @ 50.820s (amp 0.004), key col 0.003
    -       Left trough: idx=25400 (50.800s), amp=0.003
    -       Right trough: idx=25460 (50.920s), amp=0.001
- **Raw Amp**: `0.049`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.7`


## Time: `50.8000s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.7`


## Time: `50.8200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.047, S2=0.001, S2/S1=0.02 (Expected max 1.41 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.02) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.047, peak @ 50.702s (amp 0.049), key col 0.003
    -       Left trough: idx=25267 (50.534s), amp=0.001
    -       Right trough: idx=25400 (50.800s), amp=0.003
    - S2: prom 0.001, peak @ 50.820s (amp 0.004), key col 0.003
    -       Left trough: idx=25400 (50.800s), amp=0.003
    -       Right trough: idx=25460 (50.920s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.7`


## Time: `50.9200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.5`
- **Long-Term BPM (Belief)**: `129.7`


## Time: `51.1240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.003, S2/S1=0.06 (Expected max 1.41 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 51.124s (amp 0.048), key col 0.003
    -       Left trough: idx=25460 (50.920s), amp=0.001
    -       Right trough: idx=25605 (51.210s), amp=0.003
    - S2: prom 0.003, peak @ 51.244s (amp 0.005), key col 0.003
    -       Left trough: idx=25605 (51.210s), amp=0.003
    -       Right trough: idx=25684 (51.368s), amp=0.001
- **Raw Amp**: `0.048`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.9`
- **Long-Term BPM (Belief)**: `130.4`


## Time: `51.2100s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.9`
- **Long-Term BPM (Belief)**: `130.4`


## Time: `51.2440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.045, S2=0.003, S2/S1=0.06 (Expected max 1.41 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.045, peak @ 51.124s (amp 0.048), key col 0.003
    -       Left trough: idx=25460 (50.920s), amp=0.001
    -       Right trough: idx=25605 (51.210s), amp=0.003
    - S2: prom 0.003, peak @ 51.244s (amp 0.005), key col 0.003
    -       Left trough: idx=25605 (51.210s), amp=0.003
    -       Right trough: idx=25684 (51.368s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.9`
- **Long-Term BPM (Belief)**: `130.4`


## Time: `51.3680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.9`
- **Long-Term BPM (Belief)**: `130.4`


## Time: `51.5260s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.002, S2/S1=0.05 (Expected max 1.39 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 51.526s (amp 0.049), key col 0.003
    -       Left trough: idx=25684 (51.368s), amp=0.001
    -       Right trough: idx=25819 (51.638s), amp=0.003
    - S2: prom 0.002, peak @ 51.680s (amp 0.006), key col 0.003
    -       Left trough: idx=25819 (51.638s), amp=0.003
    -       Right trough: idx=25894 (51.788s), amp=0.002
- **Raw Amp**: `0.049`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.7`
- **Long-Term BPM (Belief)**: `131.3`


## Time: `51.6380s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.7`
- **Long-Term BPM (Belief)**: `131.3`


## Time: `51.6800s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.002, S2/S1=0.05 (Expected max 1.39 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 51.526s (amp 0.049), key col 0.003
    -       Left trough: idx=25684 (51.368s), amp=0.001
    -       Right trough: idx=25819 (51.638s), amp=0.003
    - S2: prom 0.002, peak @ 51.680s (amp 0.006), key col 0.003
    -       Left trough: idx=25819 (51.638s), amp=0.003
    -       Right trough: idx=25894 (51.788s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.7`
- **Long-Term BPM (Belief)**: `131.3`


## Time: `51.7880s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.7`
- **Long-Term BPM (Belief)**: `131.3`


## Time: `51.9940s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.003, S2/S1=0.10 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 51.994s (amp 0.037), key col 0.002
    -       Left trough: idx=25894 (51.788s), amp=0.002
    -       Right trough: idx=26042 (52.084s), amp=0.002
    - S2: prom 0.003, peak @ 52.186s (amp 0.005), key col 0.002
    -       Left trough: idx=26042 (52.084s), amp=0.002
    -       Right trough: idx=26120 (52.240s), amp=0.002
- **Raw Amp**: `0.037`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `52.0840s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `52.1860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.003, S2/S1=0.10 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 51.994s (amp 0.037), key col 0.002
    -       Left trough: idx=25894 (51.788s), amp=0.002
    -       Right trough: idx=26042 (52.084s), amp=0.002
    - S2: prom 0.003, peak @ 52.186s (amp 0.005), key col 0.002
    -       Left trough: idx=26042 (52.084s), amp=0.002
    -       Right trough: idx=26120 (52.240s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `52.2400s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.8`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `52.4340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.007, S2/S1=0.19 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 52.434s (amp 0.039), key col 0.004
    -       Left trough: idx=26120 (52.240s), amp=0.002
    -       Right trough: idx=26266 (52.532s), amp=0.004
    - S2: prom 0.007, peak @ 52.626s (amp 0.010), key col 0.004
    -       Left trough: idx=26266 (52.532s), amp=0.004
    -       Right trough: idx=26377 (52.754s), amp=0.002
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `52.5320s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `52.6260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.007, S2/S1=0.19 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 52.434s (amp 0.039), key col 0.004
    -       Left trough: idx=26120 (52.240s), amp=0.002
    -       Right trough: idx=26266 (52.532s), amp=0.004
    - S2: prom 0.007, peak @ 52.626s (amp 0.010), key col 0.004
    -       Left trough: idx=26266 (52.532s), amp=0.004
    -       Right trough: idx=26377 (52.754s), amp=0.002
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `52.7540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.1`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `52.8540s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.004, S2/S1=0.12 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 52.854s (amp 0.035), key col 0.002
    -       Left trough: idx=26377 (52.754s), amp=0.002
    -       Right trough: idx=26475 (52.950s), amp=0.002
    - S2: prom 0.004, peak @ 53.050s (amp 0.006), key col 0.002
    -       Left trough: idx=26475 (52.950s), amp=0.002
    -       Right trough: idx=26577 (53.154s), amp=0.002
- **Raw Amp**: `0.035`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `138.2`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `52.9500s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.2`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `53.0500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.004, S2/S1=0.12 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 52.854s (amp 0.035), key col 0.002
    -       Left trough: idx=26377 (52.754s), amp=0.002
    -       Right trough: idx=26475 (52.950s), amp=0.002
    - S2: prom 0.004, peak @ 53.050s (amp 0.006), key col 0.002
    -       Left trough: idx=26475 (52.950s), amp=0.002
    -       Right trough: idx=26577 (53.154s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.2`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `53.1540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `138.2`
- **Long-Term BPM (Belief)**: `132.0`


## Time: `53.2840s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.06 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 53.284s (amp 0.056), key col 0.003
    -       Left trough: idx=26577 (53.154s), amp=0.002
    -       Right trough: idx=26691 (53.382s), amp=0.003
    - S2: prom 0.003, peak @ 53.404s (amp 0.006), key col 0.003
    -       Left trough: idx=26691 (53.382s), amp=0.003
    -       Right trough: idx=26788 (53.576s), amp=0.001
- **Raw Amp**: `0.056`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `53.3820s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `53.4040s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.053, S2=0.003, S2/S1=0.06 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.053, peak @ 53.284s (amp 0.056), key col 0.003
    -       Left trough: idx=26577 (53.154s), amp=0.002
    -       Right trough: idx=26691 (53.382s), amp=0.003
    - S2: prom 0.003, peak @ 53.404s (amp 0.006), key col 0.003
    -       Left trough: idx=26691 (53.382s), amp=0.003
    -       Right trough: idx=26788 (53.576s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.002`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `53.5760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `137.0`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `53.7180s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.002, S2/S1=0.04 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 53.718s (amp 0.048), key col 0.002
    -       Left trough: idx=26788 (53.576s), amp=0.001
    -       Right trough: idx=26905 (53.810s), amp=0.002
    - S2: prom 0.002, peak @ 53.844s (amp 0.004), key col 0.002
    -       Left trough: idx=26905 (53.810s), amp=0.002
    -       Right trough: idx=27027 (54.054s), amp=0.001
- **Raw Amp**: `0.048`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.8`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `53.8100s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.8`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `53.8440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.046, S2=0.002, S2/S1=0.04 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.046, peak @ 53.718s (amp 0.048), key col 0.002
    -       Left trough: idx=26788 (53.576s), amp=0.001
    -       Right trough: idx=26905 (53.810s), amp=0.002
    - S2: prom 0.002, peak @ 53.844s (amp 0.004), key col 0.002
    -       Left trough: idx=26905 (53.810s), amp=0.002
    -       Right trough: idx=27027 (54.054s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.8`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.0540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `135.8`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.1680s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.004, S2/S1=0.11 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 54.168s (amp 0.045), key col 0.003
    -       Left trough: idx=27027 (54.054s), amp=0.001
    -       Right trough: idx=27126 (54.252s), amp=0.003
    - S2: prom 0.004, peak @ 54.304s (amp 0.007), key col 0.003
    -       Left trough: idx=27126 (54.252s), amp=0.003
    -       Right trough: idx=27254 (54.508s), amp=0.001
- **Raw Amp**: `0.045`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.2520s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.3040s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.004, S2/S1=0.11 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 54.168s (amp 0.045), key col 0.003
    -       Left trough: idx=27027 (54.054s), amp=0.001
    -       Right trough: idx=27126 (54.252s), amp=0.003
    - S2: prom 0.004, peak @ 54.304s (amp 0.007), key col 0.003
    -       Left trough: idx=27126 (54.252s), amp=0.003
    -       Right trough: idx=27254 (54.508s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.5080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `133.5`
- **Long-Term BPM (Belief)**: `132.7`


## Time: `54.6300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.08 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 54.630s (amp 0.039), key col 0.003
    -       Left trough: idx=27254 (54.508s), amp=0.001
    -       Right trough: idx=27365 (54.730s), amp=0.003
    - S2: prom 0.003, peak @ 54.836s (amp 0.005), key col 0.003
    -       Left trough: idx=27365 (54.730s), amp=0.003
    -       Right trough: idx=27470 (54.940s), amp=0.001
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.5`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `54.7300s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.5`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `54.8360s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.08 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 54.630s (amp 0.039), key col 0.003
    -       Left trough: idx=27254 (54.508s), amp=0.001
    -       Right trough: idx=27365 (54.730s), amp=0.003
    - S2: prom 0.003, peak @ 54.836s (amp 0.005), key col 0.003
    -       Left trough: idx=27365 (54.730s), amp=0.003
    -       Right trough: idx=27470 (54.940s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.5`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `54.9400s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `132.5`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `55.0520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.005, S2/S1=0.14 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 55.052s (amp 0.036), key col 0.002
    -       Left trough: idx=27470 (54.940s), amp=0.001
    -       Right trough: idx=27593 (55.186s), amp=0.002
    - S2: prom 0.005, peak @ 55.244s (amp 0.007), key col 0.002
    -       Left trough: idx=27593 (55.186s), amp=0.002
    -       Right trough: idx=27680 (55.360s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.9`
- **Long-Term BPM (Belief)**: `133.0`


## Time: `55.1860s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.9`
- **Long-Term BPM (Belief)**: `133.0`


## Time: `55.2440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.005, S2/S1=0.14 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 55.052s (amp 0.036), key col 0.002
    -       Left trough: idx=27470 (54.940s), amp=0.001
    -       Right trough: idx=27593 (55.186s), amp=0.002
    - S2: prom 0.005, peak @ 55.244s (amp 0.007), key col 0.002
    -       Left trough: idx=27593 (55.186s), amp=0.002
    -       Right trough: idx=27680 (55.360s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.9`
- **Long-Term BPM (Belief)**: `133.0`


## Time: `55.3600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `131.9`
- **Long-Term BPM (Belief)**: `133.0`


## Time: `55.5340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.002, S2/S1=0.07 (Expected max 1.34 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 55.534s (amp 0.036), key col 0.001
    -       Left trough: idx=27680 (55.360s), amp=0.001
    -       Right trough: idx=27819 (55.638s), amp=0.001
    - S2: prom 0.002, peak @ 55.714s (amp 0.004), key col 0.001
    -       Left trough: idx=27819 (55.638s), amp=0.001
    -       Right trough: idx=27943 (55.886s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `55.6380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `55.7140s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.002, S2/S1=0.07 (Expected max 1.34 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 55.534s (amp 0.036), key col 0.001
    -       Left trough: idx=27680 (55.360s), amp=0.001
    -       Right trough: idx=27819 (55.638s), amp=0.001
    - S2: prom 0.002, peak @ 55.714s (amp 0.004), key col 0.001
    -       Left trough: idx=27819 (55.638s), amp=0.001
    -       Right trough: idx=27943 (55.886s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `55.8860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `132.6`


## Time: `55.9960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.002, S2/S1=0.06 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 55.996s (amp 0.040), key col 0.001
    -       Left trough: idx=27943 (55.886s), amp=0.001
    -       Right trough: idx=28050 (56.100s), amp=0.001
    - S2: prom 0.002, peak @ 56.166s (amp 0.004), key col 0.002
    -       Left trough: idx=28050 (56.100s), amp=0.001
    -       Right trough: idx=28130 (56.260s), amp=0.002
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.1000s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.1660s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.002, S2/S1=0.06 (Expected max 1.35 at 133 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 133 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 55.996s (amp 0.040), key col 0.001
    -       Left trough: idx=27943 (55.886s), amp=0.001
    -       Right trough: idx=28050 (56.100s), amp=0.001
    - S2: prom 0.002, peak @ 56.166s (amp 0.004), key col 0.002
    -       Left trough: idx=28050 (56.100s), amp=0.001
    -       Right trough: idx=28130 (56.260s), amp=0.002
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.2600s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.3120s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.002, S2=0.015, S2/S1=8.96 (Expected max 1.35 at 132 BPM)
    - Contractility Penalty: -1.97 (S2 too prominent for BPM; prominence ratio 8.96 > expected 1.35) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.56: interval 0.316s vs expected 0.453s (deviation 30%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.06: strength ratio 0.06x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.56 x 0.65) + (Amplitude 0.06 x 0.35) = 0.381
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.170s < 0.199s (45% of expected RR) and strength ratio 0.20x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~353 BPM.
    - Confidence penalized 0.52x -> 0.38 to 0.20.
    - Outcome: Rejected Lone S1 (score 0.20 < threshold 0.50)
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.3820s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.6`
- **Long-Term BPM (Belief)**: `132.4`


## Time: `56.4820s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.26 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 56.482s (amp 0.017), key col 0.002
    -       Left trough: idx=28191 (56.382s), amp=0.002
    -       Right trough: idx=28287 (56.574s), amp=0.002
    - S2: prom 0.004, peak @ 56.672s (amp 0.006), key col 0.002
    -       Left trough: idx=28287 (56.574s), amp=0.002
    -       Right trough: idx=28378 (56.756s), amp=0.001
- **Raw Amp**: `0.017`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.4`
- **Long-Term BPM (Belief)**: `131.9`


## Time: `56.5740s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.4`
- **Long-Term BPM (Belief)**: `131.9`


## Time: `56.6720s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.26 (Expected max 1.35 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 56.482s (amp 0.017), key col 0.002
    -       Left trough: idx=28191 (56.382s), amp=0.002
    -       Right trough: idx=28287 (56.574s), amp=0.002
    - S2: prom 0.004, peak @ 56.672s (amp 0.006), key col 0.002
    -       Left trough: idx=28287 (56.574s), amp=0.002
    -       Right trough: idx=28378 (56.756s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.4`
- **Long-Term BPM (Belief)**: `131.9`


## Time: `56.7560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.4`
- **Long-Term BPM (Belief)**: `131.9`


## Time: `56.9920s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.002, S2/S1=0.09 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 56.992s (amp 0.029), key col 0.007
    -       Left trough: idx=28378 (56.756s), amp=0.001
    -       Right trough: idx=28546 (57.092s), amp=0.007
    - S2: prom 0.002, peak @ 57.106s (amp 0.009), key col 0.007
    -       Left trough: idx=28546 (57.092s), amp=0.007
    -       Right trough: idx=28630 (57.260s), amp=0.001
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `57.0920s`
**Trough Detected**
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `57.1060s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.002, S2/S1=0.09 (Expected max 1.36 at 132 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 132 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 56.992s (amp 0.029), key col 0.007
    -       Left trough: idx=28378 (56.756s), amp=0.001
    -       Right trough: idx=28546 (57.092s), amp=0.007
    - S2: prom 0.002, peak @ 57.106s (amp 0.009), key col 0.007
    -       Left trough: idx=28546 (57.092s), amp=0.007
    -       Right trough: idx=28630 (57.260s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `57.2600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.7`
- **Long-Term BPM (Belief)**: `131.2`


## Time: `57.4540s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.007, S2/S1=0.25 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 57.454s (amp 0.031), key col 0.002
    -       Left trough: idx=28630 (57.260s), amp=0.001
    -       Right trough: idx=28777 (57.554s), amp=0.002
    - S2: prom 0.007, peak @ 57.660s (amp 0.009), key col 0.002
    -       Left trough: idx=28777 (57.554s), amp=0.002
    -       Right trough: idx=28903 (57.806s), amp=0.001
- **Raw Amp**: `0.031`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `57.5540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `57.6600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.007, S2/S1=0.25 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 57.454s (amp 0.031), key col 0.002
    -       Left trough: idx=28630 (57.260s), amp=0.001
    -       Right trough: idx=28777 (57.554s), amp=0.002
    - S2: prom 0.007, peak @ 57.660s (amp 0.009), key col 0.002
    -       Left trough: idx=28777 (57.554s), amp=0.002
    -       Right trough: idx=28903 (57.806s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `57.8060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.2`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `57.9140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.10 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 57.914s (amp 0.033), key col 0.002
    -       Left trough: idx=28903 (57.806s), amp=0.001
    -       Right trough: idx=29010 (58.020s), amp=0.002
    - S2: prom 0.003, peak @ 58.118s (amp 0.005), key col 0.002
    -       Left trough: idx=29010 (58.020s), amp=0.002
    -       Right trough: idx=29093 (58.186s), amp=0.001
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.6`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `58.0200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.6`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `58.1180s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.10 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 57.914s (amp 0.033), key col 0.002
    -       Left trough: idx=28903 (57.806s), amp=0.001
    -       Right trough: idx=29010 (58.020s), amp=0.002
    - S2: prom 0.003, peak @ 58.118s (amp 0.005), key col 0.002
    -       Left trough: idx=29010 (58.020s), amp=0.002
    -       Right trough: idx=29093 (58.186s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.6`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `58.1860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.6`
- **Long-Term BPM (Belief)**: `131.1`


## Time: `58.3520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.003, S2/S1=0.07 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 58.352s (amp 0.037), key col 0.003
    -       Left trough: idx=29093 (58.186s), amp=0.001
    -       Right trough: idx=29237 (58.474s), amp=0.003
    - S2: prom 0.003, peak @ 58.532s (amp 0.005), key col 0.003
    -       Left trough: idx=29237 (58.474s), amp=0.003
    -       Right trough: idx=29389 (58.778s), amp=0.001
- **Raw Amp**: `0.037`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.7`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `58.4740s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.7`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `58.5320s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.003, S2/S1=0.07 (Expected max 1.38 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 58.352s (amp 0.037), key col 0.003
    -       Left trough: idx=29093 (58.186s), amp=0.001
    -       Right trough: idx=29237 (58.474s), amp=0.003
    - S2: prom 0.003, peak @ 58.532s (amp 0.005), key col 0.003
    -       Left trough: idx=29237 (58.474s), amp=0.003
    -       Right trough: idx=29389 (58.778s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.7`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `58.7780s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.7`
- **Long-Term BPM (Belief)**: `131.4`


## Time: `58.9360s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.004, S2/S1=0.09 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 58.936s (amp 0.046), key col 0.004
    -       Left trough: idx=29389 (58.778s), amp=0.001
    -       Right trough: idx=29516 (59.032s), amp=0.004
    - S2: prom 0.004, peak @ 59.096s (amp 0.007), key col 0.004
    -       Left trough: idx=29516 (59.032s), amp=0.004
    -       Right trough: idx=29605 (59.210s), amp=0.001
- **Raw Amp**: `0.046`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.4`
- **Long-Term BPM (Belief)**: `129.9`


## Time: `59.0320s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.4`
- **Long-Term BPM (Belief)**: `129.9`


## Time: `59.0960s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.042, S2=0.004, S2/S1=0.09 (Expected max 1.37 at 131 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 131 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.042, peak @ 58.936s (amp 0.046), key col 0.004
    -       Left trough: idx=29389 (58.778s), amp=0.001
    -       Right trough: idx=29516 (59.032s), amp=0.004
    - S2: prom 0.004, peak @ 59.096s (amp 0.007), key col 0.004
    -       Left trough: idx=29516 (59.032s), amp=0.004
    -       Right trough: idx=29605 (59.210s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.4`
- **Long-Term BPM (Belief)**: `129.9`


## Time: `59.2100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.4`
- **Long-Term BPM (Belief)**: `129.9`


## Time: `59.4100s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.005, S2/S1=0.11 (Expected max 1.40 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 59.410s (amp 0.042), key col 0.002
    -       Left trough: idx=29605 (59.210s), amp=0.001
    -       Right trough: idx=29757 (59.514s), amp=0.002
    - S2: prom 0.005, peak @ 59.604s (amp 0.007), key col 0.002
    -       Left trough: idx=29757 (59.514s), amp=0.002
    -       Right trough: idx=29853 (59.706s), amp=0.001
- **Raw Amp**: `0.042`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `129.8`


## Time: `59.5140s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `129.8`


## Time: `59.6040s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.005, S2/S1=0.11 (Expected max 1.40 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 59.410s (amp 0.042), key col 0.002
    -       Left trough: idx=29605 (59.210s), amp=0.001
    -       Right trough: idx=29757 (59.514s), amp=0.002
    - S2: prom 0.005, peak @ 59.604s (amp 0.007), key col 0.002
    -       Left trough: idx=29757 (59.514s), amp=0.002
    -       Right trough: idx=29853 (59.706s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `129.8`


## Time: `59.7060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `129.8`


## Time: `59.8920s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.27 (Expected max 1.40 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 59.892s (amp 0.025), key col 0.001
    -       Left trough: idx=29853 (59.706s), amp=0.001
    -       Right trough: idx=29997 (59.994s), amp=0.001
    - S2: prom 0.006, peak @ 60.090s (amp 0.008), key col 0.001
    -       Left trough: idx=29997 (59.994s), amp=0.001
    -       Right trough: idx=30088 (60.176s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.5`
- **Long-Term BPM (Belief)**: `129.5`


## Time: `59.9940s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.5`
- **Long-Term BPM (Belief)**: `129.5`


## Time: `60.0900s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.27 (Expected max 1.40 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 59.892s (amp 0.025), key col 0.001
    -       Left trough: idx=29853 (59.706s), amp=0.001
    -       Right trough: idx=29997 (59.994s), amp=0.001
    - S2: prom 0.006, peak @ 60.090s (amp 0.008), key col 0.001
    -       Left trough: idx=29997 (59.994s), amp=0.001
    -       Right trough: idx=30088 (60.176s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.5`
- **Long-Term BPM (Belief)**: `129.5`


## Time: `60.1760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.5`
- **Long-Term BPM (Belief)**: `129.5`


## Time: `60.3760s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.004, S2/S1=0.10 (Expected max 1.41 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 60.376s (amp 0.043), key col 0.001
    -       Left trough: idx=30088 (60.176s), amp=0.001
    -       Right trough: idx=30241 (60.482s), amp=0.001
    - S2: prom 0.004, peak @ 60.536s (amp 0.005), key col 0.001
    -       Left trough: idx=30241 (60.482s), amp=0.001
    -       Right trough: idx=30321 (60.642s), amp=0.001
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `129.2`


## Time: `60.4820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `129.2`


## Time: `60.5360s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.004, S2/S1=0.10 (Expected max 1.41 at 130 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 130 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 60.376s (amp 0.043), key col 0.001
    -       Left trough: idx=30088 (60.176s), amp=0.001
    -       Right trough: idx=30241 (60.482s), amp=0.001
    - S2: prom 0.004, peak @ 60.536s (amp 0.005), key col 0.001
    -       Left trough: idx=30241 (60.482s), amp=0.001
    -       Right trough: idx=30321 (60.642s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `129.2`


## Time: `60.6420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `129.2`


## Time: `60.8520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.003, S2/S1=0.08 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 60.852s (amp 0.043), key col 0.003
    -       Left trough: idx=30321 (60.642s), amp=0.001
    -       Right trough: idx=30473 (60.946s), amp=0.003
    - S2: prom 0.003, peak @ 61.060s (amp 0.006), key col 0.003
    -       Left trough: idx=30473 (60.946s), amp=0.003
    -       Right trough: idx=30595 (61.190s), amp=0.002
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `129.1`


## Time: `60.9460s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `129.1`


## Time: `61.0600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.040, S2=0.003, S2/S1=0.08 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.040, peak @ 60.852s (amp 0.043), key col 0.003
    -       Left trough: idx=30321 (60.642s), amp=0.001
    -       Right trough: idx=30473 (60.946s), amp=0.003
    - S2: prom 0.003, peak @ 61.060s (amp 0.006), key col 0.003
    -       Left trough: idx=30473 (60.946s), amp=0.003
    -       Right trough: idx=30595 (61.190s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `129.1`


## Time: `61.1900s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `129.1`


## Time: `61.3280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.003, S2/S1=0.10 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 61.328s (amp 0.032), key col 0.002
    -       Left trough: idx=30595 (61.190s), amp=0.002
    -       Right trough: idx=30729 (61.458s), amp=0.002
    - S2: prom 0.003, peak @ 61.556s (amp 0.005), key col 0.002
    -       Left trough: idx=30729 (61.458s), amp=0.002
    -       Right trough: idx=30860 (61.720s), amp=0.002
- **Raw Amp**: `0.032`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `61.4580s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `61.5560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.003, S2/S1=0.10 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 61.328s (amp 0.032), key col 0.002
    -       Left trough: idx=30595 (61.190s), amp=0.002
    -       Right trough: idx=30729 (61.458s), amp=0.002
    - S2: prom 0.003, peak @ 61.556s (amp 0.005), key col 0.002
    -       Left trough: idx=30729 (61.458s), amp=0.002
    -       Right trough: idx=30860 (61.720s), amp=0.002
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `61.7200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `128.9`


## Time: `61.9020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.16 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 61.902s (amp 0.032), key col 0.002
    -       Left trough: idx=30860 (61.720s), amp=0.002
    -       Right trough: idx=31002 (62.004s), amp=0.002
    - S2: prom 0.005, peak @ 62.058s (amp 0.007), key col 0.002
    -       Left trough: idx=31002 (62.004s), amp=0.002
    -       Right trough: idx=31121 (62.242s), amp=0.001
- **Raw Amp**: `0.032`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.5`
- **Long-Term BPM (Belief)**: `127.7`


## Time: `62.0040s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.5`
- **Long-Term BPM (Belief)**: `127.7`


## Time: `62.0580s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.16 (Expected max 1.42 at 129 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 129 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 61.902s (amp 0.032), key col 0.002
    -       Left trough: idx=30860 (61.720s), amp=0.002
    -       Right trough: idx=31002 (62.004s), amp=0.002
    - S2: prom 0.005, peak @ 62.058s (amp 0.007), key col 0.002
    -       Left trough: idx=31002 (62.004s), amp=0.002
    -       Right trough: idx=31121 (62.242s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.5`
- **Long-Term BPM (Belief)**: `127.7`


## Time: `62.2420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.5`
- **Long-Term BPM (Belief)**: `127.7`


## Time: `62.3760s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.005, S2/S1=0.18 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 62.376s (amp 0.030), key col 0.002
    -       Left trough: idx=31121 (62.242s), amp=0.001
    -       Right trough: idx=31238 (62.476s), amp=0.002
    - S2: prom 0.005, peak @ 62.550s (amp 0.007), key col 0.002
    -       Left trough: idx=31238 (62.476s), amp=0.002
    -       Right trough: idx=31324 (62.648s), amp=0.001
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `62.4760s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `62.5500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.005, S2/S1=0.18 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 62.376s (amp 0.030), key col 0.002
    -       Left trough: idx=31121 (62.242s), amp=0.001
    -       Right trough: idx=31238 (62.476s), amp=0.002
    - S2: prom 0.005, peak @ 62.550s (amp 0.007), key col 0.002
    -       Left trough: idx=31238 (62.476s), amp=0.002
    -       Right trough: idx=31324 (62.648s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `62.6480s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.0`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `62.8520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.004, S2/S1=0.25 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 62.852s (amp 0.020), key col 0.002
    -       Left trough: idx=31324 (62.648s), amp=0.001
    -       Right trough: idx=31476 (62.952s), amp=0.002
    - S2: prom 0.004, peak @ 63.010s (amp 0.006), key col 0.002
    -       Left trough: idx=31476 (62.952s), amp=0.002
    -       Right trough: idx=31601 (63.202s), amp=0.001
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.2`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `62.9520s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.2`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `63.0100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.004, S2/S1=0.25 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.25) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 62.852s (amp 0.020), key col 0.002
    -       Left trough: idx=31324 (62.648s), amp=0.001
    -       Right trough: idx=31476 (62.952s), amp=0.002
    - S2: prom 0.004, peak @ 63.010s (amp 0.006), key col 0.002
    -       Left trough: idx=31476 (62.952s), amp=0.002
    -       Right trough: idx=31601 (63.202s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.2`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `63.2020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.2`
- **Long-Term BPM (Belief)**: `127.6`


## Time: `63.3380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.11 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 63.338s (amp 0.035), key col 0.001
    -       Left trough: idx=31601 (63.202s), amp=0.001
    -       Right trough: idx=31719 (63.438s), amp=0.001
    - S2: prom 0.004, peak @ 63.482s (amp 0.005), key col 0.001
    -       Left trough: idx=31719 (63.438s), amp=0.001
    -       Right trough: idx=31791 (63.582s), amp=0.001
- **Raw Amp**: `0.035`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `63.4380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `63.4820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.11 (Expected max 1.45 at 128 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 128 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 63.338s (amp 0.035), key col 0.001
    -       Left trough: idx=31601 (63.202s), amp=0.001
    -       Right trough: idx=31719 (63.438s), amp=0.001
    - S2: prom 0.004, peak @ 63.482s (amp 0.005), key col 0.001
    -       Left trough: idx=31719 (63.438s), amp=0.001
    -       Right trough: idx=31791 (63.582s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `63.5820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `63.8280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.002, S2/S1=0.06 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 63.828s (amp 0.037), key col 0.002
    -       Left trough: idx=31791 (63.582s), amp=0.001
    -       Right trough: idx=31966 (63.932s), amp=0.002
    - S2: prom 0.002, peak @ 63.968s (amp 0.004), key col 0.002
    -       Left trough: idx=31966 (63.932s), amp=0.002
    -       Right trough: idx=32103 (64.206s), amp=0.001
- **Raw Amp**: `0.037`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `63.9320s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `63.9680s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.002, S2/S1=0.06 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 63.828s (amp 0.037), key col 0.002
    -       Left trough: idx=31791 (63.582s), amp=0.001
    -       Right trough: idx=31966 (63.932s), amp=0.002
    - S2: prom 0.002, peak @ 63.968s (amp 0.004), key col 0.002
    -       Left trough: idx=31966 (63.932s), amp=0.002
    -       Right trough: idx=32103 (64.206s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `64.2060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.6`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `64.3940s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.003, S2/S1=0.07 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 64.394s (amp 0.041), key col 0.003
    -       Left trough: idx=32103 (64.206s), amp=0.001
    -       Right trough: idx=32247 (64.494s), amp=0.003
    - S2: prom 0.003, peak @ 64.530s (amp 0.006), key col 0.003
    -       Left trough: idx=32247 (64.494s), amp=0.003
    -       Right trough: idx=32411 (64.822s), amp=0.001
- **Raw Amp**: `0.041`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `64.4940s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `64.5300s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.003, S2/S1=0.07 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 64.394s (amp 0.041), key col 0.003
    -       Left trough: idx=32103 (64.206s), amp=0.001
    -       Right trough: idx=32247 (64.494s), amp=0.003
    - S2: prom 0.003, peak @ 64.530s (amp 0.006), key col 0.003
    -       Left trough: idx=32247 (64.494s), amp=0.003
    -       Right trough: idx=32411 (64.822s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `64.8220s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `64.9060s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.004, S2/S1=0.17 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 64.906s (amp 0.026), key col 0.002
    -       Left trough: idx=32411 (64.822s), amp=0.001
    -       Right trough: idx=32510 (65.020s), amp=0.002
    - S2: prom 0.004, peak @ 65.084s (amp 0.006), key col 0.002
    -       Left trough: idx=32510 (65.020s), amp=0.002
    -       Right trough: idx=32610 (65.220s), amp=0.001
- **Raw Amp**: `0.026`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `65.0200s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `65.0840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.004, S2/S1=0.17 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 64.906s (amp 0.026), key col 0.002
    -       Left trough: idx=32411 (64.822s), amp=0.001
    -       Right trough: idx=32510 (65.020s), amp=0.002
    - S2: prom 0.004, peak @ 65.084s (amp 0.006), key col 0.002
    -       Left trough: idx=32510 (65.020s), amp=0.002
    -       Right trough: idx=32610 (65.220s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `65.2200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `65.4140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.27 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 65.414s (amp 0.025), key col 0.001
    -       Left trough: idx=32610 (65.220s), amp=0.001
    -       Right trough: idx=32753 (65.506s), amp=0.001
    - S2: prom 0.006, peak @ 65.598s (amp 0.008), key col 0.001
    -       Left trough: idx=32753 (65.506s), amp=0.001
    -       Right trough: idx=32849 (65.698s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.0`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `65.5060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.0`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `65.5980s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.27 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 65.414s (amp 0.025), key col 0.001
    -       Left trough: idx=32610 (65.220s), amp=0.001
    -       Right trough: idx=32753 (65.506s), amp=0.001
    - S2: prom 0.006, peak @ 65.598s (amp 0.008), key col 0.001
    -       Left trough: idx=32753 (65.506s), amp=0.001
    -       Right trough: idx=32849 (65.698s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.0`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `65.6980s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.0`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `65.8680s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.003, S2/S1=0.10 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 65.868s (amp 0.033), key col 0.002
    -       Left trough: idx=32849 (65.698s), amp=0.001
    -       Right trough: idx=32989 (65.978s), amp=0.002
    - S2: prom 0.003, peak @ 66.076s (amp 0.005), key col 0.002
    -       Left trough: idx=32989 (65.978s), amp=0.002
    -       Right trough: idx=33115 (66.230s), amp=0.001
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `65.9780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.0760s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.003, S2/S1=0.10 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 65.868s (amp 0.033), key col 0.002
    -       Left trough: idx=32849 (65.698s), amp=0.001
    -       Right trough: idx=32989 (65.978s), amp=0.002
    - S2: prom 0.003, peak @ 66.076s (amp 0.005), key col 0.002
    -       Left trough: idx=32989 (65.978s), amp=0.002
    -       Right trough: idx=33115 (66.230s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.2300s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.3480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.002, S2/S1=0.05 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 66.348s (amp 0.034), key col 0.001
    -       Left trough: idx=33115 (66.230s), amp=0.001
    -       Right trough: idx=33226 (66.452s), amp=0.001
    - S2: prom 0.002, peak @ 66.502s (amp 0.003), key col 0.001
    -       Left trough: idx=33226 (66.452s), amp=0.001
    -       Right trough: idx=33304 (66.608s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.4520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.5020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.002, S2/S1=0.05 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 66.348s (amp 0.034), key col 0.001
    -       Left trough: idx=33115 (66.230s), amp=0.001
    -       Right trough: idx=33226 (66.452s), amp=0.001
    - S2: prom 0.002, peak @ 66.502s (amp 0.003), key col 0.001
    -       Left trough: idx=33226 (66.452s), amp=0.001
    -       Right trough: idx=33304 (66.608s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.6080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.1`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `66.8520s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.003, S2/S1=0.10 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 66.852s (amp 0.036), key col 0.002
    -       Left trough: idx=33304 (66.608s), amp=0.001
    -       Right trough: idx=33468 (66.936s), amp=0.002
    - S2: prom 0.003, peak @ 67.008s (amp 0.006), key col 0.002
    -       Left trough: idx=33468 (66.936s), amp=0.002
    -       Right trough: idx=33646 (67.292s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.5`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `66.9360s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.5`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `67.0080s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.033, S2=0.003, S2/S1=0.10 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.033, peak @ 66.852s (amp 0.036), key col 0.002
    -       Left trough: idx=33304 (66.608s), amp=0.001
    -       Right trough: idx=33468 (66.936s), amp=0.002
    - S2: prom 0.003, peak @ 67.008s (amp 0.006), key col 0.002
    -       Left trough: idx=33468 (66.936s), amp=0.002
    -       Right trough: idx=33646 (67.292s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.5`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `67.2920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.5`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `67.4060s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.18 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 67.406s (amp 0.031), key col 0.002
    -       Left trough: idx=33646 (67.292s), amp=0.001
    -       Right trough: idx=33753 (67.506s), amp=0.002
    - S2: prom 0.005, peak @ 67.556s (amp 0.007), key col 0.002
    -       Left trough: idx=33753 (67.506s), amp=0.002
    -       Right trough: idx=33843 (67.686s), amp=0.001
- **Raw Amp**: `0.031`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `67.5060s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `67.5560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.18 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 67.406s (amp 0.031), key col 0.002
    -       Left trough: idx=33646 (67.292s), amp=0.001
    -       Right trough: idx=33753 (67.506s), amp=0.002
    - S2: prom 0.005, peak @ 67.556s (amp 0.007), key col 0.002
    -       Left trough: idx=33753 (67.506s), amp=0.002
    -       Right trough: idx=33843 (67.686s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `67.6860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `122.7`
- **Long-Term BPM (Belief)**: `124.4`


## Time: `67.9140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.24 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 67.914s (amp 0.024), key col 0.002
    -       Left trough: idx=33843 (67.686s), amp=0.001
    -       Right trough: idx=34006 (68.012s), amp=0.002
    - S2: prom 0.005, peak @ 68.064s (amp 0.008), key col 0.002
    -       Left trough: idx=34006 (68.012s), amp=0.002
    -       Right trough: idx=34082 (68.164s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.8`
- **Long-Term BPM (Belief)**: `124.1`


## Time: `68.0120s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.8`
- **Long-Term BPM (Belief)**: `124.1`


## Time: `68.0640s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.24 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 67.914s (amp 0.024), key col 0.002
    -       Left trough: idx=33843 (67.686s), amp=0.001
    -       Right trough: idx=34006 (68.012s), amp=0.002
    - S2: prom 0.005, peak @ 68.064s (amp 0.008), key col 0.002
    -       Left trough: idx=34006 (68.012s), amp=0.002
    -       Right trough: idx=34082 (68.164s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.8`
- **Long-Term BPM (Belief)**: `124.1`


## Time: `68.1640s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.8`
- **Long-Term BPM (Belief)**: `124.1`


## Time: `68.3780s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.15 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 68.378s (amp 0.026), key col 0.002
    -       Left trough: idx=34082 (68.164s), amp=0.001
    -       Right trough: idx=34239 (68.478s), amp=0.002
    - S2: prom 0.004, peak @ 68.540s (amp 0.005), key col 0.002
    -       Left trough: idx=34239 (68.478s), amp=0.002
    -       Right trough: idx=34334 (68.668s), amp=0.001
- **Raw Amp**: `0.026`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.0`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `68.4780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.0`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `68.5400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.15 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 68.378s (amp 0.026), key col 0.002
    -       Left trough: idx=34082 (68.164s), amp=0.001
    -       Right trough: idx=34239 (68.478s), amp=0.002
    - S2: prom 0.004, peak @ 68.540s (amp 0.005), key col 0.002
    -       Left trough: idx=34239 (68.478s), amp=0.002
    -       Right trough: idx=34334 (68.668s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.0`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `68.6680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.0`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `68.8480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.002, S2/S1=0.07 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 68.848s (amp 0.030), key col 0.002
    -       Left trough: idx=34334 (68.668s), amp=0.001
    -       Right trough: idx=34475 (68.950s), amp=0.002
    - S2: prom 0.002, peak @ 69.012s (amp 0.004), key col 0.002
    -       Left trough: idx=34475 (68.950s), amp=0.002
    -       Right trough: idx=34558 (69.116s), amp=0.001
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.9`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `68.9500s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.9`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.0120s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.002, S2/S1=0.07 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 68.848s (amp 0.030), key col 0.002
    -       Left trough: idx=34334 (68.668s), amp=0.001
    -       Right trough: idx=34475 (68.950s), amp=0.002
    - S2: prom 0.002, peak @ 69.012s (amp 0.004), key col 0.002
    -       Left trough: idx=34475 (68.950s), amp=0.002
    -       Right trough: idx=34558 (69.116s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.9`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.1160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.9`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.3300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.001, S2/S1=0.06 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 69.330s (amp 0.023), key col 0.002
    -       Left trough: idx=34558 (69.116s), amp=0.001
    -       Right trough: idx=34704 (69.408s), amp=0.002
    - S2: prom 0.001, peak @ 69.458s (amp 0.003), key col 0.002
    -       Left trough: idx=34704 (69.408s), amp=0.002
    -       Right trough: idx=34848 (69.696s), amp=0.000
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.1`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.4080s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.1`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.4580s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.001, S2/S1=0.06 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 69.330s (amp 0.023), key col 0.002
    -       Left trough: idx=34558 (69.116s), amp=0.001
    -       Right trough: idx=34704 (69.408s), amp=0.002
    - S2: prom 0.001, peak @ 69.458s (amp 0.003), key col 0.002
    -       Left trough: idx=34704 (69.408s), amp=0.002
    -       Right trough: idx=34848 (69.696s), amp=0.000
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.1`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.6960s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `126.1`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.8120s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.08 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 69.812s (amp 0.021), key col 0.001
    -       Left trough: idx=34848 (69.696s), amp=0.000
    -       Right trough: idx=34955 (69.910s), amp=0.001
    - S2: prom 0.002, peak @ 69.992s (amp 0.003), key col 0.001
    -       Left trough: idx=34955 (69.910s), amp=0.001
    -       Right trough: idx=35077 (70.154s), amp=0.001
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.7`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.9100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.7`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `69.9920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.08 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 69.812s (amp 0.021), key col 0.001
    -       Left trough: idx=34848 (69.696s), amp=0.000
    -       Right trough: idx=34955 (69.910s), amp=0.001
    - S2: prom 0.002, peak @ 69.992s (amp 0.003), key col 0.001
    -       Left trough: idx=34955 (69.910s), amp=0.001
    -       Right trough: idx=35077 (70.154s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.7`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `70.1540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.7`
- **Long-Term BPM (Belief)**: `124.5`


## Time: `70.2760s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.005, S2/S1=0.24 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 70.276s (amp 0.024), key col 0.003
    -       Left trough: idx=35077 (70.154s), amp=0.001
    -       Right trough: idx=35184 (70.368s), amp=0.003
    - S2: prom 0.005, peak @ 70.464s (amp 0.008), key col 0.003
    -       Left trough: idx=35184 (70.368s), amp=0.003
    -       Right trough: idx=35276 (70.552s), amp=0.002
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `124.7`


## Time: `70.3680s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `124.7`


## Time: `70.4640s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.005, S2/S1=0.24 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 70.276s (amp 0.024), key col 0.003
    -       Left trough: idx=35077 (70.154s), amp=0.001
    -       Right trough: idx=35184 (70.368s), amp=0.003
    - S2: prom 0.005, peak @ 70.464s (amp 0.008), key col 0.003
    -       Left trough: idx=35184 (70.368s), amp=0.003
    -       Right trough: idx=35276 (70.552s), amp=0.002
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `124.7`


## Time: `70.5520s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.5`
- **Long-Term BPM (Belief)**: `124.7`


## Time: `70.7220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.007, S2/S1=0.27 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 70.722s (amp 0.028), key col 0.003
    -       Left trough: idx=35276 (70.552s), amp=0.002
    -       Right trough: idx=35407 (70.814s), amp=0.003
    - S2: prom 0.007, peak @ 70.920s (amp 0.010), key col 0.003
    -       Left trough: idx=35407 (70.814s), amp=0.003
    -       Right trough: idx=35519 (71.038s), amp=0.002
- **Raw Amp**: `0.028`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `70.8140s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `70.9200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.007, S2/S1=0.27 (Expected max 1.51 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.27) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 70.722s (amp 0.028), key col 0.003
    -       Left trough: idx=35276 (70.552s), amp=0.002
    -       Right trough: idx=35407 (70.814s), amp=0.003
    - S2: prom 0.007, peak @ 70.920s (amp 0.010), key col 0.003
    -       Left trough: idx=35407 (70.814s), amp=0.003
    -       Right trough: idx=35519 (71.038s), amp=0.002
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `71.0380s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `130.8`
- **Long-Term BPM (Belief)**: `125.2`


## Time: `71.1400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.16 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 71.140s (amp 0.033), key col 0.003
    -       Left trough: idx=35519 (71.038s), amp=0.002
    -       Right trough: idx=35631 (71.262s), amp=0.003
    - S2: prom 0.005, peak @ 71.350s (amp 0.008), key col 0.003
    -       Left trough: idx=35631 (71.262s), amp=0.003
    -       Right trough: idx=35719 (71.438s), amp=0.002
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.2`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `71.2620s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.2`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `71.3500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.16 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.16) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 71.140s (amp 0.033), key col 0.003
    -       Left trough: idx=35519 (71.038s), amp=0.002
    -       Right trough: idx=35631 (71.262s), amp=0.003
    - S2: prom 0.005, peak @ 71.350s (amp 0.008), key col 0.003
    -       Left trough: idx=35631 (71.262s), amp=0.003
    -       Right trough: idx=35719 (71.438s), amp=0.002
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.2`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `71.4380s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `129.2`
- **Long-Term BPM (Belief)**: `126.1`


## Time: `71.6060s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.006, S2/S1=0.24 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 71.606s (amp 0.027), key col 0.002
    -       Left trough: idx=35719 (71.438s), amp=0.002
    -       Right trough: idx=35849 (71.698s), amp=0.002
    - S2: prom 0.006, peak @ 71.786s (amp 0.008), key col 0.002
    -       Left trough: idx=35849 (71.698s), amp=0.002
    -       Right trough: idx=35954 (71.908s), amp=0.001
- **Raw Amp**: `0.027`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `71.6980s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `71.7860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.006, S2/S1=0.24 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 71.606s (amp 0.027), key col 0.002
    -       Left trough: idx=35719 (71.438s), amp=0.002
    -       Right trough: idx=35849 (71.698s), amp=0.002
    - S2: prom 0.006, peak @ 71.786s (amp 0.008), key col 0.002
    -       Left trough: idx=35849 (71.698s), amp=0.002
    -       Right trough: idx=35954 (71.908s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `71.9080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `72.0140s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.005, S2/S1=0.11 (Expected max 1.47 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 72.014s (amp 0.043), key col 0.001
    -       Left trough: idx=35954 (71.908s), amp=0.001
    -       Right trough: idx=36064 (72.128s), amp=0.001
    - S2: prom 0.005, peak @ 72.198s (amp 0.006), key col 0.001
    -       Left trough: idx=36064 (72.128s), amp=0.001
    -       Right trough: idx=36152 (72.304s), amp=0.001
- **Raw Amp**: `0.043`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `72.1280s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `72.1980s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.041, S2=0.005, S2/S1=0.11 (Expected max 1.47 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.041, peak @ 72.014s (amp 0.043), key col 0.001
    -       Left trough: idx=35954 (71.908s), amp=0.001
    -       Right trough: idx=36064 (72.128s), amp=0.001
    - S2: prom 0.005, peak @ 72.198s (amp 0.006), key col 0.001
    -       Left trough: idx=36064 (72.128s), amp=0.001
    -       Right trough: idx=36152 (72.304s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `72.3040s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.1`
- **Long-Term BPM (Belief)**: `127.3`


## Time: `72.4800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.003, S2/S1=0.06 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 72.480s (amp 0.046), key col 0.002
    -       Left trough: idx=36152 (72.304s), amp=0.001
    -       Right trough: idx=36295 (72.590s), amp=0.002
    - S2: prom 0.003, peak @ 72.684s (amp 0.004), key col 0.002
    -       Left trough: idx=36295 (72.590s), amp=0.002
    -       Right trough: idx=36387 (72.774s), amp=0.001
- **Raw Amp**: `0.046`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `72.5900s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `72.6840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.044, S2=0.003, S2/S1=0.06 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.044, peak @ 72.480s (amp 0.046), key col 0.002
    -       Left trough: idx=36152 (72.304s), amp=0.001
    -       Right trough: idx=36295 (72.590s), amp=0.002
    - S2: prom 0.003, peak @ 72.684s (amp 0.004), key col 0.002
    -       Left trough: idx=36295 (72.590s), amp=0.002
    -       Right trough: idx=36387 (72.774s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `72.7740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `128.3`
- **Long-Term BPM (Belief)**: `127.4`


## Time: `72.9740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.001, S2/S1=0.04 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 72.974s (amp 0.030), key col 0.002
    -       Left trough: idx=36387 (72.774s), amp=0.001
    -       Right trough: idx=36537 (73.074s), amp=0.002
    - S2: prom 0.001, peak @ 73.124s (amp 0.003), key col 0.002
    -       Left trough: idx=36537 (73.074s), amp=0.002
    -       Right trough: idx=36651 (73.302s), amp=0.001
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `73.0740s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `73.1240s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.001, S2/S1=0.04 (Expected max 1.45 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 72.974s (amp 0.030), key col 0.002
    -       Left trough: idx=36387 (72.774s), amp=0.001
    -       Right trough: idx=36537 (73.074s), amp=0.002
    - S2: prom 0.001, peak @ 73.124s (amp 0.003), key col 0.002
    -       Left trough: idx=36537 (73.074s), amp=0.002
    -       Right trough: idx=36651 (73.302s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `73.3020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.8`
- **Long-Term BPM (Belief)**: `127.1`


## Time: `73.5160s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.002, S2/S1=0.06 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 73.516s (amp 0.040), key col 0.003
    -       Left trough: idx=36651 (73.302s), amp=0.001
    -       Right trough: idx=36811 (73.622s), amp=0.003
    - S2: prom 0.002, peak @ 73.648s (amp 0.005), key col 0.003
    -       Left trough: idx=36811 (73.622s), amp=0.003
    -       Right trough: idx=36975 (73.950s), amp=0.001
- **Raw Amp**: `0.040`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.2`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `73.6220s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.2`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `73.6480s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.002, S2/S1=0.06 (Expected max 1.46 at 127 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 127 BPM; prominence ratio 0.06) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 73.516s (amp 0.040), key col 0.003
    -       Left trough: idx=36651 (73.302s), amp=0.001
    -       Right trough: idx=36811 (73.622s), amp=0.003
    - S2: prom 0.002, peak @ 73.648s (amp 0.005), key col 0.003
    -       Left trough: idx=36811 (73.622s), amp=0.003
    -       Right trough: idx=36975 (73.950s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.2`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `73.9500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `127.2`
- **Long-Term BPM (Belief)**: `126.3`


## Time: `74.0480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.006, S2/S1=0.36 (Expected max 1.47 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 74.048s (amp 0.018), key col 0.002
    -       Left trough: idx=36975 (73.950s), amp=0.001
    -       Right trough: idx=37074 (74.148s), amp=0.002
    - S2: prom 0.006, peak @ 74.224s (amp 0.008), key col 0.002
    -       Left trough: idx=37074 (74.148s), amp=0.002
    -       Right trough: idx=37164 (74.328s), amp=0.002
- **Raw Amp**: `0.018`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.1480s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.2240s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.006, S2/S1=0.36 (Expected max 1.47 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 74.048s (amp 0.018), key col 0.002
    -       Left trough: idx=36975 (73.950s), amp=0.001
    -       Right trough: idx=37074 (74.148s), amp=0.002
    - S2: prom 0.006, peak @ 74.224s (amp 0.008), key col 0.002
    -       Left trough: idx=37074 (74.148s), amp=0.002
    -       Right trough: idx=37164 (74.328s), amp=0.002
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.3280s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `124.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.5220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.22 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 74.522s (amp 0.024), key col 0.003
    -       Left trough: idx=37164 (74.328s), amp=0.002
    -       Right trough: idx=37320 (74.640s), amp=0.003
    - S2: prom 0.005, peak @ 74.716s (amp 0.007), key col 0.003
    -       Left trough: idx=37320 (74.640s), amp=0.003
    -       Right trough: idx=37409 (74.818s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.6400s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.7160s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.22 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 74.522s (amp 0.024), key col 0.003
    -       Left trough: idx=37164 (74.328s), amp=0.002
    -       Right trough: idx=37320 (74.640s), amp=0.003
    - S2: prom 0.005, peak @ 74.716s (amp 0.007), key col 0.003
    -       Left trough: idx=37320 (74.640s), amp=0.003
    -       Right trough: idx=37409 (74.818s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `74.8180s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `121.2`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `75.0080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.11 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 75.008s (amp 0.024), key col 0.001
    -       Left trough: idx=37409 (74.818s), amp=0.001
    -       Right trough: idx=37558 (75.116s), amp=0.001
    - S2: prom 0.003, peak @ 75.200s (amp 0.004), key col 0.001
    -       Left trough: idx=37558 (75.116s), amp=0.001
    -       Right trough: idx=37639 (75.278s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.9`
- **Long-Term BPM (Belief)**: `125.5`


## Time: `75.1160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.9`
- **Long-Term BPM (Belief)**: `125.5`


## Time: `75.2000s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.11 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 75.008s (amp 0.024), key col 0.001
    -       Left trough: idx=37409 (74.818s), amp=0.001
    -       Right trough: idx=37558 (75.116s), amp=0.001
    - S2: prom 0.003, peak @ 75.200s (amp 0.004), key col 0.001
    -       Left trough: idx=37558 (75.116s), amp=0.001
    -       Right trough: idx=37639 (75.278s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.9`
- **Long-Term BPM (Belief)**: `125.5`


## Time: `75.2780s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.9`
- **Long-Term BPM (Belief)**: `125.5`


## Time: `75.4820s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.002, S2/S1=0.07 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 75.482s (amp 0.031), key col 0.001
    -       Left trough: idx=37639 (75.278s), amp=0.001
    -       Right trough: idx=37791 (75.582s), amp=0.001
    - S2: prom 0.002, peak @ 75.630s (amp 0.003), key col 0.001
    -       Left trough: idx=37791 (75.582s), amp=0.001
    -       Right trough: idx=37874 (75.748s), amp=0.000
- **Raw Amp**: `0.031`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.4`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `75.5820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.4`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `75.6300s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.002, S2/S1=0.07 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 75.482s (amp 0.031), key col 0.001
    -       Left trough: idx=37639 (75.278s), amp=0.001
    -       Right trough: idx=37791 (75.582s), amp=0.001
    - S2: prom 0.002, peak @ 75.630s (amp 0.003), key col 0.001
    -       Left trough: idx=37791 (75.582s), amp=0.001
    -       Right trough: idx=37874 (75.748s), amp=0.000
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.4`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `75.7480s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.4`
- **Long-Term BPM (Belief)**: `125.6`


## Time: `75.9440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.08 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 75.944s (amp 0.019), key col 0.000
    -       Left trough: idx=37874 (75.748s), amp=0.000
    -       Right trough: idx=38142 (76.284s), amp=0.000
    - S2: prom 0.002, peak @ 76.110s (amp 0.002), key col 0.000
    -       Left trough: idx=37874 (75.748s), amp=0.000
    -       Right trough: idx=38142 (76.284s), amp=0.000
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.1`
- **Long-Term BPM (Belief)**: `125.8`


## Time: `76.1100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.08 (Expected max 1.49 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 75.944s (amp 0.019), key col 0.000
    -       Left trough: idx=37874 (75.748s), amp=0.000
    -       Right trough: idx=38142 (76.284s), amp=0.000
    - S2: prom 0.002, peak @ 76.110s (amp 0.002), key col 0.000
    -       Left trough: idx=37874 (75.748s), amp=0.000
    -       Right trough: idx=38142 (76.284s), amp=0.000
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.1`
- **Long-Term BPM (Belief)**: `125.8`


## Time: `76.2840s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.1`
- **Long-Term BPM (Belief)**: `125.8`


## Time: `76.4880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.001, S2/S1=0.08 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 76.488s (amp 0.017), key col 0.001
    -       Left trough: idx=38142 (76.284s), amp=0.000
    -       Right trough: idx=38296 (76.592s), amp=0.001
    - S2: prom 0.001, peak @ 76.662s (amp 0.002), key col 0.001
    -       Left trough: idx=38296 (76.592s), amp=0.001
    -       Right trough: idx=38408 (76.816s), amp=0.000
- **Raw Amp**: `0.017`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.0`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `76.5920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.0`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `76.6620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.001, S2/S1=0.08 (Expected max 1.48 at 126 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 126 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 76.488s (amp 0.017), key col 0.001
    -       Left trough: idx=38142 (76.284s), amp=0.000
    -       Right trough: idx=38296 (76.592s), amp=0.001
    - S2: prom 0.001, peak @ 76.662s (amp 0.002), key col 0.001
    -       Left trough: idx=38296 (76.592s), amp=0.001
    -       Right trough: idx=38408 (76.816s), amp=0.000
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.0`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `76.8160s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.0`
- **Long-Term BPM (Belief)**: `125.0`


## Time: `77.0420s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.010, S2=0.001, S2/S1=0.10 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.010, peak @ 77.042s (amp 0.011), key col 0.001
    -       Left trough: idx=38408 (76.816s), amp=0.000
    -       Right trough: idx=38578 (77.156s), amp=0.001
    - S2: prom 0.001, peak @ 77.250s (amp 0.002), key col 0.001
    -       Left trough: idx=38578 (77.156s), amp=0.001
    -       Right trough: idx=38726 (77.452s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `124.2`


## Time: `77.1560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `124.2`


## Time: `77.2500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.010, S2=0.001, S2/S1=0.10 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.010, peak @ 77.042s (amp 0.011), key col 0.001
    -       Left trough: idx=38408 (76.816s), amp=0.000
    -       Right trough: idx=38578 (77.156s), amp=0.001
    - S2: prom 0.001, peak @ 77.250s (amp 0.002), key col 0.001
    -       Left trough: idx=38578 (77.156s), amp=0.001
    -       Right trough: idx=38726 (77.452s), amp=0.001
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `124.2`


## Time: `77.4520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `118.5`
- **Long-Term BPM (Belief)**: `124.2`


## Time: `77.5960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.007, S2=0.001, S2/S1=0.14 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.007, peak @ 77.596s (amp 0.008), key col 0.001
    -       Left trough: idx=38726 (77.452s), amp=0.001
    -       Right trough: idx=38849 (77.698s), amp=0.001
    - S2: prom 0.001, peak @ 77.794s (amp 0.002), key col 0.001
    -       Left trough: idx=38849 (77.698s), amp=0.001
    -       Right trough: idx=38980 (77.960s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `77.6980s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `77.7940s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.007, S2=0.001, S2/S1=0.14 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.007, peak @ 77.596s (amp 0.008), key col 0.001
    -       Left trough: idx=38726 (77.452s), amp=0.001
    -       Right trough: idx=38849 (77.698s), amp=0.001
    - S2: prom 0.001, peak @ 77.794s (amp 0.002), key col 0.001
    -       Left trough: idx=38849 (77.698s), amp=0.001
    -       Right trough: idx=38980 (77.960s), amp=0.001
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `77.9600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `119.8`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `78.1200s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.001, S2/S1=0.14 (Expected max 1.53 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 78.120s (amp 0.011), key col 0.001
    -       Left trough: idx=38980 (77.960s), amp=0.001
    -       Right trough: idx=39110 (78.220s), amp=0.001
    - S2: prom 0.001, peak @ 78.320s (amp 0.002), key col 0.001
    -       Left trough: idx=39110 (78.220s), amp=0.001
    -       Right trough: idx=39262 (78.524s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `78.2200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `78.3200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.001, S2/S1=0.14 (Expected max 1.53 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 78.120s (amp 0.011), key col 0.001
    -       Left trough: idx=38980 (77.960s), amp=0.001
    -       Right trough: idx=39110 (78.220s), amp=0.001
    - S2: prom 0.001, peak @ 78.320s (amp 0.002), key col 0.001
    -       Left trough: idx=39110 (78.220s), amp=0.001
    -       Right trough: idx=39262 (78.524s), amp=0.001
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `78.5240s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `123.0`


## Time: `78.6240s`
**Lone S1.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.010, S2=0.016, S2/S1=1.55 (Expected max 1.54 at 123 BPM)
    - Contractility Penalty: -0.00 (S2 too prominent for BPM; prominence ratio 1.55 > expected 1.54) -> 0.60
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.78
    - Interval penalty by 0.73 (Interval 0.474s > Max 0.342s)
    - Final Score: 0.05 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.96: interval 0.504s vs expected 0.488s (deviation 3%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 1.00: strength ratio 1.06x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.96 x 0.65) + (Amplitude 1.00 x 0.35) = 0.972
    - Outcome: Validated Lone S1 (score 0.97 >= threshold 0.50)
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `122.8`


## Time: `78.8680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `120.8`
- **Long-Term BPM (Belief)**: `122.8`


## Time: `79.0980s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.003, S2/S1=0.20 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 79.098s (amp 0.017), key col 0.001
    -       Left trough: idx=39434 (78.868s), amp=0.001
    -       Right trough: idx=39722 (79.444s), amp=0.001
    - S2: prom 0.003, peak @ 79.232s (amp 0.004), key col 0.001
    -       Left trough: idx=39434 (78.868s), amp=0.001
    -       Right trough: idx=39722 (79.444s), amp=0.001
- **Raw Amp**: `0.017`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `122.9`


## Time: `79.2320s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.003, S2/S1=0.20 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 79.098s (amp 0.017), key col 0.001
    -       Left trough: idx=39434 (78.868s), amp=0.001
    -       Right trough: idx=39722 (79.444s), amp=0.001
    - S2: prom 0.003, peak @ 79.232s (amp 0.004), key col 0.001
    -       Left trough: idx=39434 (78.868s), amp=0.001
    -       Right trough: idx=39722 (79.444s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `122.9`


## Time: `79.4440s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.1`
- **Long-Term BPM (Belief)**: `122.9`


## Time: `79.5740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.004, S2/S1=0.23 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.23) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 79.574s (amp 0.020), key col 0.004
    -       Left trough: idx=39722 (79.444s), amp=0.001
    -       Right trough: idx=39841 (79.682s), amp=0.004
    - S2: prom 0.004, peak @ 79.762s (amp 0.008), key col 0.004
    -       Left trough: idx=39841 (79.682s), amp=0.004
    -       Right trough: idx=39970 (79.940s), amp=0.002
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `79.6820s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `79.7620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.004, S2/S1=0.23 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.23) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 79.574s (amp 0.020), key col 0.004
    -       Left trough: idx=39722 (79.444s), amp=0.001
    -       Right trough: idx=39841 (79.682s), amp=0.004
    - S2: prom 0.004, peak @ 79.762s (amp 0.008), key col 0.004
    -       Left trough: idx=39841 (79.682s), amp=0.004
    -       Right trough: idx=39970 (79.940s), amp=0.002
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `79.9400s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `80.0400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.001, S2/S1=0.04 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 80.040s (amp 0.028), key col 0.002
    -       Left trough: idx=39970 (79.940s), amp=0.002
    -       Right trough: idx=40073 (80.146s), amp=0.002
    - S2: prom 0.001, peak @ 80.188s (amp 0.003), key col 0.002
    -       Left trough: idx=40073 (80.146s), amp=0.002
    -       Right trough: idx=40179 (80.358s), amp=0.001
- **Raw Amp**: `0.028`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `80.1460s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `80.1880s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.001, S2/S1=0.04 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.04) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 80.040s (amp 0.028), key col 0.002
    -       Left trough: idx=39970 (79.940s), amp=0.002
    -       Right trough: idx=40073 (80.146s), amp=0.002
    - S2: prom 0.001, peak @ 80.188s (amp 0.003), key col 0.002
    -       Left trough: idx=40073 (80.146s), amp=0.002
    -       Right trough: idx=40179 (80.358s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `80.3580s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `125.0`
- **Long-Term BPM (Belief)**: `123.4`


## Time: `80.4800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.002, S2/S1=0.05 (Expected max 1.53 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 80.480s (amp 0.034), key col 0.002
    -       Left trough: idx=40179 (80.358s), amp=0.001
    -       Right trough: idx=40302 (80.604s), amp=0.002
    - S2: prom 0.002, peak @ 80.640s (amp 0.004), key col 0.002
    -       Left trough: idx=40302 (80.604s), amp=0.002
    -       Right trough: idx=40418 (80.836s), amp=0.001
- **Raw Amp**: `0.034`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.0`
- **Long-Term BPM (Belief)**: `124.0`


## Time: `80.6040s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.0`
- **Long-Term BPM (Belief)**: `124.0`


## Time: `80.6400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.002, S2/S1=0.05 (Expected max 1.53 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.05) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 80.480s (amp 0.034), key col 0.002
    -       Left trough: idx=40179 (80.358s), amp=0.001
    -       Right trough: idx=40302 (80.604s), amp=0.002
    - S2: prom 0.002, peak @ 80.640s (amp 0.004), key col 0.002
    -       Left trough: idx=40302 (80.604s), amp=0.002
    -       Right trough: idx=40418 (80.836s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.0`
- **Long-Term BPM (Belief)**: `124.0`


## Time: `80.8360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.0`
- **Long-Term BPM (Belief)**: `124.0`


## Time: `80.9440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.13 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 80.944s (amp 0.036), key col 0.002
    -       Left trough: idx=40418 (80.836s), amp=0.001
    -       Right trough: idx=40532 (81.064s), amp=0.002
    - S2: prom 0.004, peak @ 81.156s (amp 0.006), key col 0.002
    -       Left trough: idx=40532 (81.064s), amp=0.002
    -       Right trough: idx=40615 (81.230s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.9`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `81.0640s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.9`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `81.1560s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.004, S2/S1=0.13 (Expected max 1.52 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 80.944s (amp 0.036), key col 0.002
    -       Left trough: idx=40418 (80.836s), amp=0.001
    -       Right trough: idx=40532 (81.064s), amp=0.002
    - S2: prom 0.004, peak @ 81.156s (amp 0.006), key col 0.002
    -       Left trough: idx=40532 (81.064s), amp=0.002
    -       Right trough: idx=40615 (81.230s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.9`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `81.2300s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `123.9`
- **Long-Term BPM (Belief)**: `124.3`


## Time: `81.3920s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.006, S2/S1=0.18 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 81.392s (amp 0.036), key col 0.001
    -       Left trough: idx=40615 (81.230s), amp=0.001
    -       Right trough: idx=40759 (81.518s), amp=0.001
    - S2: prom 0.006, peak @ 81.572s (amp 0.008), key col 0.001
    -       Left trough: idx=40759 (81.518s), amp=0.001
    -       Right trough: idx=40829 (81.658s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.9`
- **Long-Term BPM (Belief)**: `124.8`


## Time: `81.5180s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.9`
- **Long-Term BPM (Belief)**: `124.8`


## Time: `81.5720s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.006, S2/S1=0.18 (Expected max 1.51 at 124 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 124 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 81.392s (amp 0.036), key col 0.001
    -       Left trough: idx=40615 (81.230s), amp=0.001
    -       Right trough: idx=40759 (81.518s), amp=0.001
    - S2: prom 0.006, peak @ 81.572s (amp 0.008), key col 0.001
    -       Left trough: idx=40759 (81.518s), amp=0.001
    -       Right trough: idx=40829 (81.658s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.9`
- **Long-Term BPM (Belief)**: `124.8`


## Time: `81.6580s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `117.9`
- **Long-Term BPM (Belief)**: `124.8`


## Time: `81.8640s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.004, S2/S1=0.11 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 81.864s (amp 0.039), key col 0.001
    -       Left trough: idx=40829 (81.658s), amp=0.001
    -       Right trough: idx=40995 (81.990s), amp=0.001
    - S2: prom 0.004, peak @ 82.092s (amp 0.005), key col 0.001
    -       Left trough: idx=40995 (81.990s), amp=0.001
    -       Right trough: idx=41143 (82.286s), amp=0.000
- **Raw Amp**: `0.039`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.8`
- **Long-Term BPM (Belief)**: `124.9`


## Time: `81.9900s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.8`
- **Long-Term BPM (Belief)**: `124.9`


## Time: `82.0920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.038, S2=0.004, S2/S1=0.11 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.038, peak @ 81.864s (amp 0.039), key col 0.001
    -       Left trough: idx=40829 (81.658s), amp=0.001
    -       Right trough: idx=40995 (81.990s), amp=0.001
    - S2: prom 0.004, peak @ 82.092s (amp 0.005), key col 0.001
    -       Left trough: idx=40995 (81.990s), amp=0.001
    -       Right trough: idx=41143 (82.286s), amp=0.000
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.8`
- **Long-Term BPM (Belief)**: `124.9`


## Time: `82.2860s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.8`
- **Long-Term BPM (Belief)**: `124.9`


## Time: `82.5440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.09 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 82.544s (amp 0.038), key col 0.002
    -       Left trough: idx=41143 (82.286s), amp=0.000
    -       Right trough: idx=41301 (82.602s), amp=0.002
    - S2: prom 0.003, peak @ 82.702s (amp 0.005), key col 0.002
    -       Left trough: idx=41301 (82.602s), amp=0.002
    -       Right trough: idx=41642 (83.284s), amp=0.001
- **Raw Amp**: `0.038`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.6`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `82.6020s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.6`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `82.7020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.036, S2=0.003, S2/S1=0.09 (Expected max 1.50 at 125 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 125 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.036, peak @ 82.544s (amp 0.038), key col 0.002
    -       Left trough: idx=41143 (82.286s), amp=0.000
    -       Right trough: idx=41301 (82.602s), amp=0.002
    - S2: prom 0.003, peak @ 82.702s (amp 0.005), key col 0.002
    -       Left trough: idx=41301 (82.602s), amp=0.002
    -       Right trough: idx=41642 (83.284s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.6`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `83.2840s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.6`
- **Long-Term BPM (Belief)**: `123.1`


## Time: `83.4740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.007, S2/S1=0.19 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 83.474s (amp 0.038), key col 0.002
    -       Left trough: idx=41642 (83.284s), amp=0.001
    -       Right trough: idx=41789 (83.578s), amp=0.002
    - S2: prom 0.007, peak @ 83.642s (amp 0.009), key col 0.002
    -       Left trough: idx=41789 (83.578s), amp=0.002
    -       Right trough: idx=41975 (83.950s), amp=0.002
- **Raw Amp**: `0.038`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `83.5780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `83.6420s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.035, S2=0.007, S2/S1=0.19 (Expected max 1.54 at 123 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 123 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.035, peak @ 83.474s (amp 0.038), key col 0.002
    -       Left trough: idx=41642 (83.284s), amp=0.001
    -       Right trough: idx=41789 (83.578s), amp=0.002
    - S2: prom 0.007, peak @ 83.642s (amp 0.009), key col 0.002
    -       Left trough: idx=41789 (83.578s), amp=0.002
    -       Right trough: idx=41975 (83.950s), amp=0.002
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `83.9500s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `84.0440s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.011, S2/S1=10.61 (Expected max 1.59 at 120 BPM)
    - Contractility Penalty: -1.98 (S2 too prominent for BPM; prominence ratio 10.61 > expected 1.59) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.81: interval 0.570s vs expected 0.499s (deviation 14%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.05: strength ratio 0.05x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.81 x 0.65) + (Amplitude 0.05 x 0.35) = 0.544
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.172s < 0.219s (45% of expected RR) and strength ratio 0.20x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~349 BPM.
    - Confidence penalized 0.52x -> 0.54 to 0.28.
    - Outcome: Rejected Lone S1 (score 0.28 < threshold 0.50)
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `84.1120s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.8`
- **Long-Term BPM (Belief)**: `118.9`


## Time: `84.2160s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.011, S2=0.006, S2/S1=0.54 (Expected max 1.60 at 117 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 117 BPM; prominence ratio 0.54) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.011, peak @ 84.216s (amp 0.013), key col 0.001
    -       Left trough: idx=42056 (84.112s), amp=0.001
    -       Right trough: idx=42179 (84.358s), amp=0.001
    - S2: prom 0.006, peak @ 84.416s (amp 0.008), key col 0.001
    -       Left trough: idx=42179 (84.358s), amp=0.001
    -       Right trough: idx=42357 (84.714s), amp=0.001
- **Raw Amp**: `0.013`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `115.7`


## Time: `84.3580s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `115.7`


## Time: `84.4160s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.011, S2=0.006, S2/S1=0.54 (Expected max 1.60 at 117 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 117 BPM; prominence ratio 0.54) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.011, peak @ 84.216s (amp 0.013), key col 0.001
    -       Left trough: idx=42056 (84.112s), amp=0.001
    -       Right trough: idx=42179 (84.358s), amp=0.001
    - S2: prom 0.006, peak @ 84.416s (amp 0.008), key col 0.001
    -       Left trough: idx=42179 (84.358s), amp=0.001
    -       Right trough: idx=42357 (84.714s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `115.7`


## Time: `84.7140s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `115.7`


## Time: `84.9240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.28 (Expected max 1.60 at 116 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 116 BPM; prominence ratio 0.28) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 84.924s (amp 0.016), key col 0.001
    -       Left trough: idx=42357 (84.714s), amp=0.001
    -       Right trough: idx=42531 (85.062s), amp=0.001
    - S2: prom 0.004, peak @ 85.140s (amp 0.005), key col 0.001
    -       Left trough: idx=42531 (85.062s), amp=0.001
    -       Right trough: idx=42653 (85.306s), amp=0.001
- **Raw Amp**: `0.016`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.6`
- **Long-Term BPM (Belief)**: `114.1`


## Time: `85.0620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.6`
- **Long-Term BPM (Belief)**: `114.1`


## Time: `85.1400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.28 (Expected max 1.60 at 116 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 116 BPM; prominence ratio 0.28) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 84.924s (amp 0.016), key col 0.001
    -       Left trough: idx=42357 (84.714s), amp=0.001
    -       Right trough: idx=42531 (85.062s), amp=0.001
    - S2: prom 0.004, peak @ 85.140s (amp 0.005), key col 0.001
    -       Left trough: idx=42531 (85.062s), amp=0.001
    -       Right trough: idx=42653 (85.306s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.6`
- **Long-Term BPM (Belief)**: `114.1`


## Time: `85.3060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.6`
- **Long-Term BPM (Belief)**: `114.1`


## Time: `85.6380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.002, S2/S1=0.09 (Expected max 1.60 at 114 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 114 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 85.638s (amp 0.028), key col 0.001
    -       Left trough: idx=42653 (85.306s), amp=0.001
    -       Right trough: idx=42904 (85.808s), amp=0.001
    - S2: prom 0.002, peak @ 85.858s (amp 0.003), key col 0.001
    -       Left trough: idx=42904 (85.808s), amp=0.001
    -       Right trough: idx=42986 (85.972s), amp=0.000
- **Raw Amp**: `0.028`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.4`
- **Long-Term BPM (Belief)**: `112.6`


## Time: `85.8080s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.4`
- **Long-Term BPM (Belief)**: `112.6`


## Time: `85.8580s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.002, S2/S1=0.09 (Expected max 1.60 at 114 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 114 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 85.638s (amp 0.028), key col 0.001
    -       Left trough: idx=42653 (85.306s), amp=0.001
    -       Right trough: idx=42904 (85.808s), amp=0.001
    - S2: prom 0.002, peak @ 85.858s (amp 0.003), key col 0.001
    -       Left trough: idx=42904 (85.808s), amp=0.001
    -       Right trough: idx=42986 (85.972s), amp=0.000
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.4`
- **Long-Term BPM (Belief)**: `112.6`


## Time: `85.9720s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `79.4`
- **Long-Term BPM (Belief)**: `112.6`


## Time: `86.4340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 113 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 113 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 86.434s (amp 0.024), key col 0.002
    -       Left trough: idx=42986 (85.972s), amp=0.000
    -       Right trough: idx=43289 (86.578s), amp=0.002
    - S2: prom 0.003, peak @ 86.662s (amp 0.005), key col 0.002
    -       Left trough: idx=43289 (86.578s), amp=0.002
    -       Right trough: idx=43467 (86.934s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.3`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `86.5780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.3`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `86.6620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 113 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 113 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 86.434s (amp 0.024), key col 0.002
    -       Left trough: idx=42986 (85.972s), amp=0.000
    -       Right trough: idx=43289 (86.578s), amp=0.002
    - S2: prom 0.003, peak @ 86.662s (amp 0.005), key col 0.002
    -       Left trough: idx=43289 (86.578s), amp=0.002
    -       Right trough: idx=43467 (86.934s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.3`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `86.9340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.3`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `87.1900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.005, S2/S1=0.20 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 87.190s (amp 0.025), key col 0.002
    -       Left trough: idx=43467 (86.934s), amp=0.001
    -       Right trough: idx=43671 (87.342s), amp=0.002
    - S2: prom 0.005, peak @ 87.392s (amp 0.006), key col 0.002
    -       Left trough: idx=43671 (87.342s), amp=0.002
    -       Right trough: idx=43819 (87.638s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `87.3420s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `87.3920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.005, S2/S1=0.20 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 87.190s (amp 0.025), key col 0.002
    -       Left trough: idx=43467 (86.934s), amp=0.001
    -       Right trough: idx=43671 (87.342s), amp=0.002
    - S2: prom 0.005, peak @ 87.392s (amp 0.006), key col 0.002
    -       Left trough: idx=43671 (87.342s), amp=0.002
    -       Right trough: idx=43819 (87.638s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `87.6380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `87.8780s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.20 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 87.878s (amp 0.022), key col 0.002
    -       Left trough: idx=43819 (87.638s), amp=0.001
    -       Right trough: idx=44002 (88.004s), amp=0.002
    - S2: prom 0.004, peak @ 88.058s (amp 0.006), key col 0.002
    -       Left trough: idx=44002 (88.004s), amp=0.002
    -       Right trough: idx=44179 (88.358s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.9`
- **Long-Term BPM (Belief)**: `108.1`


## Time: `88.0040s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.9`
- **Long-Term BPM (Belief)**: `108.1`


## Time: `88.0580s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.20 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 87.878s (amp 0.022), key col 0.002
    -       Left trough: idx=43819 (87.638s), amp=0.001
    -       Right trough: idx=44002 (88.004s), amp=0.002
    - S2: prom 0.004, peak @ 88.058s (amp 0.006), key col 0.002
    -       Left trough: idx=44002 (88.004s), amp=0.002
    -       Right trough: idx=44179 (88.358s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.9`
- **Long-Term BPM (Belief)**: `108.1`


## Time: `88.3580s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `94.9`
- **Long-Term BPM (Belief)**: `108.1`


## Time: `88.4860s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.013, S2=0.005, S2/S1=0.34 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.34) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.013, peak @ 88.486s (amp 0.015), key col 0.001
    -       Left trough: idx=44179 (88.358s), amp=0.001
    -       Right trough: idx=44303 (88.606s), amp=0.001
    - S2: prom 0.005, peak @ 88.674s (amp 0.006), key col 0.001
    -       Left trough: idx=44303 (88.606s), amp=0.001
    -       Right trough: idx=44383 (88.766s), amp=0.001
- **Raw Amp**: `0.015`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.9`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `88.6060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.9`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `88.6740s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.013, S2=0.005, S2/S1=0.34 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.34) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.013, peak @ 88.486s (amp 0.015), key col 0.001
    -       Left trough: idx=44179 (88.358s), amp=0.001
    -       Right trough: idx=44303 (88.606s), amp=0.001
    - S2: prom 0.005, peak @ 88.674s (amp 0.006), key col 0.001
    -       Left trough: idx=44303 (88.606s), amp=0.001
    -       Right trough: idx=44383 (88.766s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.9`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `88.7660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.9`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `89.0400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 89.040s (amp 0.022), key col 0.001
    -       Left trough: idx=44383 (88.766s), amp=0.001
    -       Right trough: idx=44584 (89.168s), amp=0.001
    - S2: prom 0.003, peak @ 89.252s (amp 0.004), key col 0.001
    -       Left trough: idx=44584 (89.168s), amp=0.001
    -       Right trough: idx=44667 (89.334s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.8`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `89.1680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.8`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `89.2520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 89.040s (amp 0.022), key col 0.001
    -       Left trough: idx=44383 (88.766s), amp=0.001
    -       Right trough: idx=44584 (89.168s), amp=0.001
    - S2: prom 0.003, peak @ 89.252s (amp 0.004), key col 0.001
    -       Left trough: idx=44584 (89.168s), amp=0.001
    -       Right trough: idx=44667 (89.334s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.8`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `89.3340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.8`
- **Long-Term BPM (Belief)**: `107.6`


## Time: `89.5760s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.002, S2/S1=0.09 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 89.576s (amp 0.025), key col 0.001
    -       Left trough: idx=44667 (89.334s), amp=0.001
    -       Right trough: idx=44848 (89.696s), amp=0.001
    - S2: prom 0.002, peak @ 89.750s (amp 0.004), key col 0.001
    -       Left trough: idx=44848 (89.696s), amp=0.001
    -       Right trough: idx=44983 (89.966s), amp=0.000
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `104.7`
- **Long-Term BPM (Belief)**: `107.9`


## Time: `89.6960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `104.7`
- **Long-Term BPM (Belief)**: `107.9`


## Time: `89.7500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.002, S2/S1=0.09 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.09) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 89.576s (amp 0.025), key col 0.001
    -       Left trough: idx=44667 (89.334s), amp=0.001
    -       Right trough: idx=44848 (89.696s), amp=0.001
    - S2: prom 0.002, peak @ 89.750s (amp 0.004), key col 0.001
    -       Left trough: idx=44848 (89.696s), amp=0.001
    -       Right trough: idx=44983 (89.966s), amp=0.000
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `104.7`
- **Long-Term BPM (Belief)**: `107.9`


## Time: `89.9660s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `104.7`
- **Long-Term BPM (Belief)**: `107.9`


## Time: `90.1020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.003, S2/S1=0.15 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 90.102s (amp 0.019), key col 0.002
    -       Left trough: idx=44983 (89.966s), amp=0.000
    -       Right trough: idx=45103 (90.206s), amp=0.002
    - S2: prom 0.003, peak @ 90.306s (amp 0.004), key col 0.002
    -       Left trough: idx=45103 (90.206s), amp=0.002
    -       Right trough: idx=45234 (90.468s), amp=0.001
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `109.7`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.2060s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `109.7`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.3060s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.003, S2/S1=0.15 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.15) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 90.102s (amp 0.019), key col 0.002
    -       Left trough: idx=44983 (89.966s), amp=0.000
    -       Right trough: idx=45103 (90.206s), amp=0.002
    - S2: prom 0.003, peak @ 90.306s (amp 0.004), key col 0.002
    -       Left trough: idx=45103 (90.206s), amp=0.002
    -       Right trough: idx=45234 (90.468s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `109.7`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.4680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `109.7`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.6560s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.12 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 90.656s (amp 0.025), key col 0.002
    -       Left trough: idx=45234 (90.468s), amp=0.001
    -       Right trough: idx=45385 (90.770s), amp=0.002
    - S2: prom 0.003, peak @ 90.834s (amp 0.005), key col 0.002
    -       Left trough: idx=45385 (90.770s), amp=0.002
    -       Right trough: idx=45535 (91.070s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.7700s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `90.8340s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.003, S2/S1=0.12 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.28 (Pairing Ratio: 95%, Floor: 0.90) → 0.96
    - Final Score: 0.96 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 90.656s (amp 0.025), key col 0.002
    -       Left trough: idx=45234 (90.468s), amp=0.001
    -       Right trough: idx=45385 (90.770s), amp=0.002
    - S2: prom 0.003, peak @ 90.834s (amp 0.005), key col 0.002
    -       Left trough: idx=45385 (90.770s), amp=0.002
    -       Right trough: idx=45535 (91.070s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `91.0700s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `108.2`


## Time: `91.1800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.006, S2/S1=0.32 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.32) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 91.180s (amp 0.019), key col 0.001
    -       Left trough: idx=45535 (91.070s), amp=0.001
    -       Right trough: idx=45647 (91.294s), amp=0.001
    - S2: prom 0.006, peak @ 91.350s (amp 0.007), key col 0.001
    -       Left trough: idx=45647 (91.294s), amp=0.001
    -       Right trough: idx=45732 (91.464s), amp=0.001
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.3`
- **Long-Term BPM (Belief)**: `108.5`


## Time: `91.2940s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.3`
- **Long-Term BPM (Belief)**: `108.5`


## Time: `91.3500s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.006, S2/S1=0.32 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.32) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 91.180s (amp 0.019), key col 0.001
    -       Left trough: idx=45535 (91.070s), amp=0.001
    -       Right trough: idx=45647 (91.294s), amp=0.001
    - S2: prom 0.006, peak @ 91.350s (amp 0.007), key col 0.001
    -       Left trough: idx=45647 (91.294s), amp=0.001
    -       Right trough: idx=45732 (91.464s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.3`
- **Long-Term BPM (Belief)**: `108.5`


## Time: `91.4640s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.3`
- **Long-Term BPM (Belief)**: `108.5`


## Time: `91.6820s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.21 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 91.682s (amp 0.024), key col 0.001
    -       Left trough: idx=45732 (91.464s), amp=0.001
    -       Right trough: idx=45893 (91.786s), amp=0.001
    - S2: prom 0.005, peak @ 91.846s (amp 0.006), key col 0.001
    -       Left trough: idx=45893 (91.786s), amp=0.001
    -       Right trough: idx=46022 (92.044s), amp=0.000
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `91.7860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `91.8460s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.21 (Expected max 1.60 at 108 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 108 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 91.682s (amp 0.024), key col 0.001
    -       Left trough: idx=45732 (91.464s), amp=0.001
    -       Right trough: idx=45893 (91.786s), amp=0.001
    - S2: prom 0.005, peak @ 91.846s (amp 0.006), key col 0.001
    -       Left trough: idx=45893 (91.786s), amp=0.001
    -       Right trough: idx=46022 (92.044s), amp=0.000
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `92.0440s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.8`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `92.1620s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.10 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 92.162s (amp 0.033), key col 0.001
    -       Left trough: idx=46022 (92.044s), amp=0.000
    -       Right trough: idx=46137 (92.274s), amp=0.001
    - S2: prom 0.003, peak @ 92.340s (amp 0.004), key col 0.001
    -       Left trough: idx=46137 (92.274s), amp=0.001
    -       Right trough: idx=46244 (92.488s), amp=0.000
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `109.8`


## Time: `92.2740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `109.8`


## Time: `92.3400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.031, S2=0.003, S2/S1=0.10 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.031, peak @ 92.162s (amp 0.033), key col 0.001
    -       Left trough: idx=46022 (92.044s), amp=0.000
    -       Right trough: idx=46137 (92.274s), amp=0.001
    - S2: prom 0.003, peak @ 92.340s (amp 0.004), key col 0.001
    -       Left trough: idx=46137 (92.274s), amp=0.001
    -       Right trough: idx=46244 (92.488s), amp=0.000
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `109.8`


## Time: `92.4880s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `109.8`


## Time: `92.6480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.002, S2/S1=0.08 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 92.648s (amp 0.030), key col 0.001
    -       Left trough: idx=46244 (92.488s), amp=0.000
    -       Right trough: idx=46383 (92.766s), amp=0.001
    - S2: prom 0.002, peak @ 92.862s (amp 0.004), key col 0.001
    -       Left trough: idx=46383 (92.766s), amp=0.001
    -       Right trough: idx=46521 (93.042s), amp=0.000
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.9`
- **Long-Term BPM (Belief)**: `110.5`


## Time: `92.7660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.9`
- **Long-Term BPM (Belief)**: `110.5`


## Time: `92.8620s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.002, S2/S1=0.08 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.08) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 92.648s (amp 0.030), key col 0.001
    -       Left trough: idx=46244 (92.488s), amp=0.000
    -       Right trough: idx=46383 (92.766s), amp=0.001
    - S2: prom 0.002, peak @ 92.862s (amp 0.004), key col 0.001
    -       Left trough: idx=46383 (92.766s), amp=0.001
    -       Right trough: idx=46521 (93.042s), amp=0.000
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.9`
- **Long-Term BPM (Belief)**: `110.5`


## Time: `93.0420s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `114.9`
- **Long-Term BPM (Belief)**: `110.5`


## Time: `93.2260s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.10 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 93.226s (amp 0.024), key col 0.003
    -       Left trough: idx=46521 (93.042s), amp=0.000
    -       Right trough: idx=46672 (93.344s), amp=0.003
    - S2: prom 0.002, peak @ 93.376s (amp 0.005), key col 0.003
    -       Left trough: idx=46672 (93.344s), amp=0.003
    -       Right trough: idx=46848 (93.696s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.1`
- **Long-Term BPM (Belief)**: `110.2`


## Time: `93.3440s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.1`
- **Long-Term BPM (Belief)**: `110.2`


## Time: `93.3760s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.10 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 93.226s (amp 0.024), key col 0.003
    -       Left trough: idx=46521 (93.042s), amp=0.000
    -       Right trough: idx=46672 (93.344s), amp=0.003
    - S2: prom 0.002, peak @ 93.376s (amp 0.005), key col 0.003
    -       Left trough: idx=46672 (93.344s), amp=0.003
    -       Right trough: idx=46848 (93.696s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.1`
- **Long-Term BPM (Belief)**: `110.2`


## Time: `93.6960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.1`
- **Long-Term BPM (Belief)**: `110.2`


## Time: `93.8040s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.26 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 93.804s (amp 0.022), key col 0.001
    -       Left trough: idx=46848 (93.696s), amp=0.001
    -       Right trough: idx=46955 (93.910s), amp=0.001
    - S2: prom 0.005, peak @ 94.014s (amp 0.007), key col 0.001
    -       Left trough: idx=46955 (93.910s), amp=0.001
    -       Right trough: idx=47046 (94.092s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.7`
- **Long-Term BPM (Belief)**: `109.9`


## Time: `93.9100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.7`
- **Long-Term BPM (Belief)**: `109.9`


## Time: `94.0140s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.26 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 93.804s (amp 0.022), key col 0.001
    -       Left trough: idx=46848 (93.696s), amp=0.001
    -       Right trough: idx=46955 (93.910s), amp=0.001
    - S2: prom 0.005, peak @ 94.014s (amp 0.007), key col 0.001
    -       Left trough: idx=46955 (93.910s), amp=0.001
    -       Right trough: idx=47046 (94.092s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.7`
- **Long-Term BPM (Belief)**: `109.9`


## Time: `94.0920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `116.7`
- **Long-Term BPM (Belief)**: `109.9`


## Time: `94.3380s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.26 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 94.338s (amp 0.022), key col 0.001
    -       Left trough: idx=47046 (94.092s), amp=0.001
    -       Right trough: idx=47223 (94.446s), amp=0.001
    - S2: prom 0.005, peak @ 94.538s (amp 0.007), key col 0.001
    -       Left trough: idx=47223 (94.446s), amp=0.001
    -       Right trough: idx=47316 (94.632s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `94.4460s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `94.5380s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.005, S2/S1=0.26 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 94.338s (amp 0.022), key col 0.001
    -       Left trough: idx=47046 (94.092s), amp=0.001
    -       Right trough: idx=47223 (94.446s), amp=0.001
    - S2: prom 0.005, peak @ 94.538s (amp 0.007), key col 0.001
    -       Left trough: idx=47223 (94.446s), amp=0.001
    -       Right trough: idx=47316 (94.632s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `94.6320s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `113.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `94.8260s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.21 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 94.826s (amp 0.021), key col 0.002
    -       Left trough: idx=47316 (94.632s), amp=0.001
    -       Right trough: idx=47456 (94.912s), amp=0.002
    - S2: prom 0.004, peak @ 94.988s (amp 0.007), key col 0.002
    -       Left trough: idx=47456 (94.912s), amp=0.002
    -       Right trough: idx=47563 (95.126s), amp=0.001
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.8`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `94.9120s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.8`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `94.9880s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.21 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.21) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 94.826s (amp 0.021), key col 0.002
    -       Left trough: idx=47316 (94.632s), amp=0.001
    -       Right trough: idx=47456 (94.912s), amp=0.002
    - S2: prom 0.004, peak @ 94.988s (amp 0.007), key col 0.002
    -       Left trough: idx=47456 (94.912s), amp=0.002
    -       Right trough: idx=47563 (95.126s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.8`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `95.1260s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.8`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `95.3280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.002, S2/S1=0.07 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 95.328s (amp 0.033), key col 0.001
    -       Left trough: idx=47563 (95.126s), amp=0.001
    -       Right trough: idx=47721 (95.442s), amp=0.001
    - S2: prom 0.002, peak @ 95.498s (amp 0.004), key col 0.001
    -       Left trough: idx=47721 (95.442s), amp=0.001
    -       Right trough: idx=47792 (95.584s), amp=0.001
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.4`
- **Long-Term BPM (Belief)**: `111.1`


## Time: `95.4420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.4`
- **Long-Term BPM (Belief)**: `111.1`


## Time: `95.4980s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.032, S2=0.002, S2/S1=0.07 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.07) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.032, peak @ 95.328s (amp 0.033), key col 0.001
    -       Left trough: idx=47563 (95.126s), amp=0.001
    -       Right trough: idx=47721 (95.442s), amp=0.001
    - S2: prom 0.002, peak @ 95.498s (amp 0.004), key col 0.001
    -       Left trough: idx=47721 (95.442s), amp=0.001
    -       Right trough: idx=47792 (95.584s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.4`
- **Long-Term BPM (Belief)**: `111.1`


## Time: `95.5840s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.4`
- **Long-Term BPM (Belief)**: `111.1`


## Time: `95.8300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.003, S2/S1=0.11 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 95.830s (amp 0.027), key col 0.002
    -       Left trough: idx=47792 (95.584s), amp=0.001
    -       Right trough: idx=47987 (95.974s), amp=0.002
    - S2: prom 0.003, peak @ 96.074s (amp 0.004), key col 0.002
    -       Left trough: idx=47987 (95.974s), amp=0.002
    -       Right trough: idx=48075 (96.150s), amp=0.001
- **Raw Amp**: `0.027`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.9`
- **Long-Term BPM (Belief)**: `111.5`


## Time: `95.9740s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.9`
- **Long-Term BPM (Belief)**: `111.5`


## Time: `96.0740s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.003, S2/S1=0.11 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.11) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 95.830s (amp 0.027), key col 0.002
    -       Left trough: idx=47792 (95.584s), amp=0.001
    -       Right trough: idx=47987 (95.974s), amp=0.002
    - S2: prom 0.003, peak @ 96.074s (amp 0.004), key col 0.002
    -       Left trough: idx=47987 (95.974s), amp=0.002
    -       Right trough: idx=48075 (96.150s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.9`
- **Long-Term BPM (Belief)**: `111.5`


## Time: `96.1500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `111.9`
- **Long-Term BPM (Belief)**: `111.5`


## Time: `96.4620s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.18 (Expected max 1.60 at 112 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 112 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 96.462s (amp 0.025), key col 0.002
    -       Left trough: idx=48075 (96.150s), amp=0.001
    -       Right trough: idx=48284 (96.568s), amp=0.002
    - S2: prom 0.004, peak @ 96.616s (amp 0.006), key col 0.002
    -       Left trough: idx=48284 (96.568s), amp=0.002
    -       Right trough: idx=48358 (96.716s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.2`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `96.5680s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.2`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `96.6160s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.18 (Expected max 1.60 at 112 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 112 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 96.462s (amp 0.025), key col 0.002
    -       Left trough: idx=48075 (96.150s), amp=0.001
    -       Right trough: idx=48284 (96.568s), amp=0.002
    - S2: prom 0.004, peak @ 96.616s (amp 0.006), key col 0.002
    -       Left trough: idx=48284 (96.568s), amp=0.002
    -       Right trough: idx=48358 (96.716s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.2`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `96.7160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `112.2`
- **Long-Term BPM (Belief)**: `110.7`


## Time: `97.0300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.008, S2/S1=0.42 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 97.030s (amp 0.020), key col 0.001
    -       Left trough: idx=48358 (96.716s), amp=0.001
    -       Right trough: idx=48581 (97.162s), amp=0.001
    - S2: prom 0.008, peak @ 97.218s (amp 0.009), key col 0.001
    -       Left trough: idx=48581 (97.162s), amp=0.001
    -       Right trough: idx=48715 (97.430s), amp=0.001
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.6`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.1620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.6`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.2180s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.008, S2/S1=0.42 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 97.030s (amp 0.020), key col 0.001
    -       Left trough: idx=48358 (96.716s), amp=0.001
    -       Right trough: idx=48581 (97.162s), amp=0.001
    - S2: prom 0.008, peak @ 97.218s (amp 0.009), key col 0.001
    -       Left trough: idx=48581 (97.162s), amp=0.001
    -       Right trough: idx=48715 (97.430s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.6`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.4300s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `110.6`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.5720s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.006, S2/S1=0.33 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.33) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 97.572s (amp 0.019), key col 0.001
    -       Left trough: idx=48715 (97.430s), amp=0.001
    -       Right trough: idx=48850 (97.700s), amp=0.001
    - S2: prom 0.006, peak @ 97.792s (amp 0.007), key col 0.001
    -       Left trough: idx=48850 (97.700s), amp=0.001
    -       Right trough: idx=48991 (97.982s), amp=0.001
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `108.3`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.7000s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `108.3`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.7920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.006, S2/S1=0.33 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.33) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 97.572s (amp 0.019), key col 0.001
    -       Left trough: idx=48715 (97.430s), amp=0.001
    -       Right trough: idx=48850 (97.700s), amp=0.001
    - S2: prom 0.006, peak @ 97.792s (amp 0.007), key col 0.001
    -       Left trough: idx=48850 (97.700s), amp=0.001
    -       Right trough: idx=48991 (97.982s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `108.3`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `97.9820s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `108.3`
- **Long-Term BPM (Belief)**: `110.4`


## Time: `98.0800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.006, S2/S1=0.38 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.38) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 98.080s (amp 0.018), key col 0.001
    -       Left trough: idx=48991 (97.982s), amp=0.001
    -       Right trough: idx=49108 (98.216s), amp=0.001
    - S2: prom 0.006, peak @ 98.264s (amp 0.008), key col 0.001
    -       Left trough: idx=49108 (98.216s), amp=0.001
    -       Right trough: idx=49182 (98.364s), amp=0.001
- **Raw Amp**: `0.018`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `110.8`


## Time: `98.2160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `110.8`


## Time: `98.2640s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.006, S2/S1=0.38 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.38) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 98.080s (amp 0.018), key col 0.001
    -       Left trough: idx=48991 (97.982s), amp=0.001
    -       Right trough: idx=49108 (98.216s), amp=0.001
    - S2: prom 0.006, peak @ 98.264s (amp 0.008), key col 0.001
    -       Left trough: idx=49108 (98.216s), amp=0.001
    -       Right trough: idx=49182 (98.364s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `110.8`


## Time: `98.3640s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `107.1`
- **Long-Term BPM (Belief)**: `110.8`


## Time: `98.6460s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 98.646s (amp 0.025), key col 0.004
    -       Left trough: idx=49182 (98.364s), amp=0.001
    -       Right trough: idx=49382 (98.764s), amp=0.004
    - S2: prom 0.004, peak @ 98.788s (amp 0.007), key col 0.004
    -       Left trough: idx=49382 (98.764s), amp=0.004
    -       Right trough: idx=49488 (98.976s), amp=0.001
- **Raw Amp**: `0.025`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.7`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `98.7640s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.7`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `98.7880s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 98.646s (amp 0.025), key col 0.004
    -       Left trough: idx=49182 (98.364s), amp=0.001
    -       Right trough: idx=49382 (98.764s), amp=0.004
    - S2: prom 0.004, peak @ 98.788s (amp 0.007), key col 0.004
    -       Left trough: idx=49382 (98.764s), amp=0.004
    -       Right trough: idx=49488 (98.976s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.7`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `98.9760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.7`
- **Long-Term BPM (Belief)**: `110.6`


## Time: `99.2580s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.006, S2/S1=0.18 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 99.258s (amp 0.036), key col 0.002
    -       Left trough: idx=49488 (98.976s), amp=0.001
    -       Right trough: idx=49689 (99.378s), amp=0.002
    - S2: prom 0.006, peak @ 99.478s (amp 0.008), key col 0.002
    -       Left trough: idx=49689 (99.378s), amp=0.002
    -       Right trough: idx=49826 (99.652s), amp=0.001
- **Raw Amp**: `0.036`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `99.3780s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `99.4780s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.034, S2=0.006, S2/S1=0.18 (Expected max 1.60 at 111 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 111 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.034, peak @ 99.258s (amp 0.036), key col 0.002
    -       Left trough: idx=49488 (98.976s), amp=0.001
    -       Right trough: idx=49689 (99.378s), amp=0.002
    - S2: prom 0.006, peak @ 99.478s (amp 0.008), key col 0.002
    -       Left trough: idx=49689 (99.378s), amp=0.002
    -       Right trough: idx=49826 (99.652s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `99.6520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.9`
- **Long-Term BPM (Belief)**: `110.0`


## Time: `99.8440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.007, S2/S1=0.36 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 99.844s (amp 0.021), key col 0.001
    -       Left trough: idx=49826 (99.652s), amp=0.001
    -       Right trough: idx=49980 (99.960s), amp=0.001
    - S2: prom 0.007, peak @ 100.040s (amp 0.009), key col 0.001
    -       Left trough: idx=49980 (99.960s), amp=0.001
    -       Right trough: idx=50075 (100.150s), amp=0.001
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.7`
- **Long-Term BPM (Belief)**: `109.6`


## Time: `99.9600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.7`
- **Long-Term BPM (Belief)**: `109.6`


## Time: `100.0400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.007, S2/S1=0.36 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 99.844s (amp 0.021), key col 0.001
    -       Left trough: idx=49826 (99.652s), amp=0.001
    -       Right trough: idx=49980 (99.960s), amp=0.001
    - S2: prom 0.007, peak @ 100.040s (amp 0.009), key col 0.001
    -       Left trough: idx=49980 (99.960s), amp=0.001
    -       Right trough: idx=50075 (100.150s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.7`
- **Long-Term BPM (Belief)**: `109.6`


## Time: `100.1500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.7`
- **Long-Term BPM (Belief)**: `109.6`


## Time: `100.3960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.004, S2/S1=0.49 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.49) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 100.396s (amp 0.011), key col 0.002
    -       Left trough: idx=50075 (100.150s), amp=0.001
    -       Right trough: idx=50249 (100.498s), amp=0.002
    - S2: prom 0.004, peak @ 100.596s (amp 0.007), key col 0.002
    -       Left trough: idx=50249 (100.498s), amp=0.002
    -       Right trough: idx=50336 (100.672s), amp=0.002
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.8`
- **Long-Term BPM (Belief)**: `109.5`


## Time: `100.4980s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.8`
- **Long-Term BPM (Belief)**: `109.5`


## Time: `100.5960s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.004, S2/S1=0.49 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.49) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 100.396s (amp 0.011), key col 0.002
    -       Left trough: idx=50075 (100.150s), amp=0.001
    -       Right trough: idx=50249 (100.498s), amp=0.002
    - S2: prom 0.004, peak @ 100.596s (amp 0.007), key col 0.002
    -       Left trough: idx=50249 (100.498s), amp=0.002
    -       Right trough: idx=50336 (100.672s), amp=0.002
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.8`
- **Long-Term BPM (Belief)**: `109.5`


## Time: `100.6720s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `106.8`
- **Long-Term BPM (Belief)**: `109.5`


## Time: `100.9600s`
**S1 (Paired).**
- LOOKAHEAD INTERVAL: Reinterpreted middle peak as noise because the implied S2→S1 interval 0.120s is below the minimum 0.126s for BPM 110, and the middle peak is weak (0.002 < 0.35 × S1 0.019) while the next candidate is stronger (0.002 > 0.002).
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.12 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 100.960s (amp 0.022), key col 0.003
    -       Left trough: idx=50336 (100.672s), amp=0.002
    -       Right trough: idx=50541 (101.082s), amp=0.003
    - S2: prom 0.002, peak @ 101.254s (amp 0.006), key col 0.004
    -       Left trough: idx=50601 (101.202s), amp=0.004
    -       Right trough: idx=50674 (101.348s), amp=0.002
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.0820s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.1340s`
**Noise/Rejected.**
- Middle peak treated as noise due to impossible S2→S1 interval (0.120s < 0.126s), weak prominence (0.002 < 0.35 × S1 0.019), and a stronger following candidate (0.002 > 0.002).
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.2020s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.2540s`
**S2 (Paired).**
- LOOKAHEAD INTERVAL: Reinterpreted middle peak as noise because the implied S2→S1 interval 0.120s is below the minimum 0.126s for BPM 110, and the middle peak is weak (0.002 < 0.35 × S1 0.019) while the next candidate is stronger (0.002 > 0.002).
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.002, S2/S1=0.12 (Expected max 1.60 at 110 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 110 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 100.960s (amp 0.022), key col 0.003
    -       Left trough: idx=50336 (100.672s), amp=0.002
    -       Right trough: idx=50541 (101.082s), amp=0.003
    - S2: prom 0.002, peak @ 101.254s (amp 0.006), key col 0.004
    -       Left trough: idx=50601 (101.202s), amp=0.004
    -       Right trough: idx=50674 (101.348s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.3480s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.9`
- **Long-Term BPM (Belief)**: `109.4`


## Time: `101.5260s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.005, S2/S1=0.31 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 101.526s (amp 0.020), key col 0.003
    -       Left trough: idx=50674 (101.348s), amp=0.002
    -       Right trough: idx=50831 (101.662s), amp=0.003
    - S2: prom 0.005, peak @ 101.702s (amp 0.008), key col 0.003
    -       Left trough: idx=50831 (101.662s), amp=0.003
    -       Right trough: idx=50945 (101.890s), amp=0.001
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.0`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `101.6620s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.0`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `101.7020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.005, S2/S1=0.31 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 101.526s (amp 0.020), key col 0.003
    -       Left trough: idx=50674 (101.348s), amp=0.002
    -       Right trough: idx=50831 (101.662s), amp=0.003
    - S2: prom 0.005, peak @ 101.702s (amp 0.008), key col 0.003
    -       Left trough: idx=50831 (101.662s), amp=0.003
    -       Right trough: idx=50945 (101.890s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.0`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `101.8900s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `105.0`
- **Long-Term BPM (Belief)**: `109.2`


## Time: `102.1020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.008, S2/S1=0.28 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.28) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 102.102s (amp 0.029), key col 0.002
    -       Left trough: idx=50945 (101.890s), amp=0.001
    -       Right trough: idx=51118 (102.236s), amp=0.002
    - S2: prom 0.008, peak @ 102.286s (amp 0.010), key col 0.002
    -       Left trough: idx=51118 (102.236s), amp=0.002
    -       Right trough: idx=51227 (102.454s), amp=0.001
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.7`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `102.2360s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.7`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `102.2860s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.027, S2=0.008, S2/S1=0.28 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.28) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.027, peak @ 102.102s (amp 0.029), key col 0.002
    -       Left trough: idx=50945 (101.890s), amp=0.001
    -       Right trough: idx=51118 (102.236s), amp=0.002
    - S2: prom 0.008, peak @ 102.286s (amp 0.010), key col 0.002
    -       Left trough: idx=51118 (102.236s), amp=0.002
    -       Right trough: idx=51227 (102.454s), amp=0.001
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.7`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `102.4540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.7`
- **Long-Term BPM (Belief)**: `109.0`


## Time: `102.6400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.009, S2/S1=0.82 (Expected max 1.60 at 109 BPM)
    - Contractility Neutral: prominence ratio 0.82 within expected range for 109 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 102.640s (amp 0.012), key col 0.001
    -       Left trough: idx=51227 (102.454s), amp=0.001
    -       Right trough: idx=51379 (102.758s), amp=0.001
    - S2: prom 0.009, peak @ 102.874s (amp 0.010), key col 0.001
    -       Left trough: idx=51379 (102.758s), amp=0.001
    -       Right trough: idx=51510 (103.020s), amp=0.001
- **Raw Amp**: `0.012`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.9`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `102.7580s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.9`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `102.8740s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.009, S2/S1=0.82 (Expected max 1.60 at 109 BPM)
    - Contractility Neutral: prominence ratio 0.82 within expected range for 109 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 102.640s (amp 0.012), key col 0.001
    -       Left trough: idx=51227 (102.454s), amp=0.001
    -       Right trough: idx=51379 (102.758s), amp=0.001
    - S2: prom 0.009, peak @ 102.874s (amp 0.010), key col 0.001
    -       Left trough: idx=51379 (102.758s), amp=0.001
    -       Right trough: idx=51510 (103.020s), amp=0.001
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.9`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.0200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `103.9`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.1860s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.006, S2/S1=0.30 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 103.186s (amp 0.022), key col 0.002
    -       Left trough: idx=51510 (103.020s), amp=0.001
    -       Right trough: idx=51666 (103.332s), amp=0.002
    - S2: prom 0.006, peak @ 103.384s (amp 0.008), key col 0.002
    -       Left trough: idx=51666 (103.332s), amp=0.002
    -       Right trough: idx=51773 (103.546s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.5`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.3320s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.5`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.3840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.006, S2/S1=0.30 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 103.186s (amp 0.022), key col 0.002
    -       Left trough: idx=51510 (103.020s), amp=0.001
    -       Right trough: idx=51666 (103.332s), amp=0.002
    - S2: prom 0.006, peak @ 103.384s (amp 0.008), key col 0.002
    -       Left trough: idx=51666 (103.332s), amp=0.002
    -       Right trough: idx=51773 (103.546s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.5`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.5460s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.5`
- **Long-Term BPM (Belief)**: `109.1`


## Time: `103.7980s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.24 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 103.798s (amp 0.024), key col 0.002
    -       Left trough: idx=51773 (103.546s), amp=0.001
    -       Right trough: idx=51969 (103.938s), amp=0.002
    - S2: prom 0.005, peak @ 104.040s (amp 0.007), key col 0.002
    -       Left trough: idx=51969 (103.938s), amp=0.002
    -       Right trough: idx=52151 (104.302s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.2`
- **Long-Term BPM (Belief)**: `108.6`


## Time: `103.9380s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.2`
- **Long-Term BPM (Belief)**: `108.6`


## Time: `104.0400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.24 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 103.798s (amp 0.024), key col 0.002
    -       Left trough: idx=51773 (103.546s), amp=0.001
    -       Right trough: idx=51969 (103.938s), amp=0.002
    - S2: prom 0.005, peak @ 104.040s (amp 0.007), key col 0.002
    -       Left trough: idx=51969 (103.938s), amp=0.002
    -       Right trough: idx=52151 (104.302s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.2`
- **Long-Term BPM (Belief)**: `108.6`


## Time: `104.3020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `102.2`
- **Long-Term BPM (Belief)**: `108.6`


## Time: `104.4920s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.26 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 104.492s (amp 0.026), key col 0.003
    -       Left trough: idx=52151 (104.302s), amp=0.001
    -       Right trough: idx=52319 (104.638s), amp=0.003
    - S2: prom 0.006, peak @ 104.684s (amp 0.009), key col 0.003
    -       Left trough: idx=52319 (104.638s), amp=0.003
    -       Right trough: idx=52465 (104.930s), amp=0.001
- **Raw Amp**: `0.026`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.9`
- **Long-Term BPM (Belief)**: `107.5`


## Time: `104.6380s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.9`
- **Long-Term BPM (Belief)**: `107.5`


## Time: `104.6840s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.006, S2/S1=0.26 (Expected max 1.60 at 109 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 109 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 104.492s (amp 0.026), key col 0.003
    -       Left trough: idx=52151 (104.302s), amp=0.001
    -       Right trough: idx=52319 (104.638s), amp=0.003
    - S2: prom 0.006, peak @ 104.684s (amp 0.009), key col 0.003
    -       Left trough: idx=52319 (104.638s), amp=0.003
    -       Right trough: idx=52465 (104.930s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.9`
- **Long-Term BPM (Belief)**: `107.5`


## Time: `104.9300s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `101.9`
- **Long-Term BPM (Belief)**: `107.5`


## Time: `105.1600s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.009, S2/S1=0.23 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.23) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 105.160s (amp 0.041), key col 0.002
    -       Left trough: idx=52465 (104.930s), amp=0.001
    -       Right trough: idx=52644 (105.288s), amp=0.002
    - S2: prom 0.009, peak @ 105.352s (amp 0.011), key col 0.002
    -       Left trough: idx=52644 (105.288s), amp=0.002
    -       Right trough: idx=52744 (105.488s), amp=0.001
- **Raw Amp**: `0.041`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.4`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `105.2880s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.4`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `105.3520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.039, S2=0.009, S2/S1=0.23 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.23) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.039, peak @ 105.160s (amp 0.041), key col 0.002
    -       Left trough: idx=52465 (104.930s), amp=0.001
    -       Right trough: idx=52644 (105.288s), amp=0.002
    - S2: prom 0.009, peak @ 105.352s (amp 0.011), key col 0.002
    -       Left trough: idx=52644 (105.288s), amp=0.002
    -       Right trough: idx=52744 (105.488s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.4`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `105.4880s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.4`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `105.7340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.007, S2/S1=0.42 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 105.734s (amp 0.017), key col 0.001
    -       Left trough: idx=52744 (105.488s), amp=0.001
    -       Right trough: idx=52928 (105.856s), amp=0.001
    - S2: prom 0.007, peak @ 105.960s (amp 0.008), key col 0.001
    -       Left trough: idx=52928 (105.856s), amp=0.001
    -       Right trough: idx=53033 (106.066s), amp=0.001
- **Raw Amp**: `0.017`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `105.8560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `105.9600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.007, S2/S1=0.42 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 105.734s (amp 0.017), key col 0.001
    -       Left trough: idx=52744 (105.488s), amp=0.001
    -       Right trough: idx=52928 (105.856s), amp=0.001
    - S2: prom 0.007, peak @ 105.960s (amp 0.008), key col 0.001
    -       Left trough: idx=52928 (105.856s), amp=0.001
    -       Right trough: idx=53033 (106.066s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `106.0660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `106.2840s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 106 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 106 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 106.284s (amp 0.024), key col 0.001
    -       Left trough: idx=53033 (106.066s), amp=0.001
    -       Right trough: idx=53209 (106.418s), amp=0.001
    - S2: prom 0.004, peak @ 106.526s (amp 0.005), key col 0.001
    -       Left trough: idx=53209 (106.418s), amp=0.001
    -       Right trough: idx=53336 (106.672s), amp=0.001
- **Raw Amp**: `0.024`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `106.4180s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `106.5260s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.023, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 106 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 106 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.023, peak @ 106.284s (amp 0.024), key col 0.001
    -       Left trough: idx=53033 (106.066s), amp=0.001
    -       Right trough: idx=53209 (106.418s), amp=0.001
    - S2: prom 0.004, peak @ 106.526s (amp 0.005), key col 0.001
    -       Left trough: idx=53209 (106.418s), amp=0.001
    -       Right trough: idx=53336 (106.672s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `106.6720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.5`
- **Long-Term BPM (Belief)**: `106.6`


## Time: `106.8640s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.004, S2/S1=0.19 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 106.864s (amp 0.019), key col 0.001
    -       Left trough: idx=53336 (106.672s), amp=0.001
    -       Right trough: idx=53503 (107.006s), amp=0.001
    - S2: prom 0.004, peak @ 107.106s (amp 0.005), key col 0.001
    -       Left trough: idx=53503 (107.006s), amp=0.001
    -       Right trough: idx=53708 (107.416s), amp=0.001
- **Raw Amp**: `0.019`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.6`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `107.0060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.6`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `107.1060s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.018, S2=0.004, S2/S1=0.19 (Expected max 1.60 at 107 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 107 BPM; prominence ratio 0.19) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.018, peak @ 106.864s (amp 0.019), key col 0.001
    -       Left trough: idx=53336 (106.672s), amp=0.001
    -       Right trough: idx=53503 (107.006s), amp=0.001
    - S2: prom 0.004, peak @ 107.106s (amp 0.005), key col 0.001
    -       Left trough: idx=53503 (107.006s), amp=0.001
    -       Right trough: idx=53708 (107.416s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.6`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `107.4160s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.6`
- **Long-Term BPM (Belief)**: `106.5`


## Time: `107.5620s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.17 (Expected max 1.60 at 106 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 106 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 107.562s (amp 0.032), key col 0.002
    -       Left trough: idx=53708 (107.416s), amp=0.001
    -       Right trough: idx=53850 (107.700s), amp=0.002
    - S2: prom 0.005, peak @ 107.752s (amp 0.007), key col 0.002
    -       Left trough: idx=53850 (107.700s), amp=0.002
    -       Right trough: idx=53961 (107.922s), amp=0.001
- **Raw Amp**: `0.032`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.1`
- **Long-Term BPM (Belief)**: `105.4`


## Time: `107.7000s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.1`
- **Long-Term BPM (Belief)**: `105.4`


## Time: `107.7520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.17 (Expected max 1.60 at 106 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 106 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 107.562s (amp 0.032), key col 0.002
    -       Left trough: idx=53708 (107.416s), amp=0.001
    -       Right trough: idx=53850 (107.700s), amp=0.002
    - S2: prom 0.005, peak @ 107.752s (amp 0.007), key col 0.002
    -       Left trough: idx=53850 (107.700s), amp=0.002
    -       Right trough: idx=53961 (107.922s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.1`
- **Long-Term BPM (Belief)**: `105.4`


## Time: `107.9220s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.1`
- **Long-Term BPM (Belief)**: `105.4`


## Time: `108.1940s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.009, S2/S1=0.31 (Expected max 1.60 at 105 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 105 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 108.194s (amp 0.030), key col 0.001
    -       Left trough: idx=53961 (107.922s), amp=0.001
    -       Right trough: idx=54174 (108.348s), amp=0.001
    - S2: prom 0.009, peak @ 108.448s (amp 0.010), key col 0.001
    -       Left trough: idx=54174 (108.348s), amp=0.001
    -       Right trough: idx=54298 (108.596s), amp=0.001
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.3`
- **Long-Term BPM (Belief)**: `104.9`


## Time: `108.3480s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.3`
- **Long-Term BPM (Belief)**: `104.9`


## Time: `108.4480s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.029, S2=0.009, S2/S1=0.31 (Expected max 1.60 at 105 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 105 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.029, peak @ 108.194s (amp 0.030), key col 0.001
    -       Left trough: idx=53961 (107.922s), amp=0.001
    -       Right trough: idx=54174 (108.348s), amp=0.001
    - S2: prom 0.009, peak @ 108.448s (amp 0.010), key col 0.001
    -       Left trough: idx=54174 (108.348s), amp=0.001
    -       Right trough: idx=54298 (108.596s), amp=0.001
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.3`
- **Long-Term BPM (Belief)**: `104.9`


## Time: `108.5960s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.3`
- **Long-Term BPM (Belief)**: `104.9`


## Time: `108.8040s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.004, S2/S1=0.24 (Expected max 1.60 at 105 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 105 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 108.804s (amp 0.017), key col 0.002
    -       Left trough: idx=54298 (108.596s), amp=0.001
    -       Right trough: idx=54451 (108.902s), amp=0.002
    - S2: prom 0.004, peak @ 109.002s (amp 0.006), key col 0.002
    -       Left trough: idx=54451 (108.902s), amp=0.002
    -       Right trough: idx=54548 (109.096s), amp=0.002
- **Raw Amp**: `0.017`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `108.9020s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `109.0020s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.016, S2=0.004, S2/S1=0.24 (Expected max 1.60 at 105 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 105 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.016, peak @ 108.804s (amp 0.017), key col 0.002
    -       Left trough: idx=54298 (108.596s), amp=0.001
    -       Right trough: idx=54451 (108.902s), amp=0.002
    - S2: prom 0.004, peak @ 109.002s (amp 0.006), key col 0.002
    -       Left trough: idx=54451 (108.902s), amp=0.002
    -       Right trough: idx=54548 (109.096s), amp=0.002
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `109.0960s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `109.1600s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.003, S2=0.022, S2/S1=8.01 (Expected max 1.60 at 105 BPM)
    - Contractility Penalty: -1.40 (S2 too prominent for BPM; prominence ratio 8.01 > expected 1.60) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.43: interval 0.356s vs expected 0.574s (deviation 38%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.23: strength ratio 0.23x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.43 x 0.65) + (Amplitude 0.23 x 0.35) = 0.362
    - Outcome: Rejected Lone S1 (score 0.36 < threshold 0.50)
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `109.2700s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `87.6`
- **Long-Term BPM (Belief)**: `104.4`


## Time: `109.5300s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.003, S2/S1=0.12 (Expected max 1.60 at 104 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 104 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 109.530s (amp 0.023), key col 0.001
    -       Left trough: idx=54635 (109.270s), amp=0.001
    -       Right trough: idx=54833 (109.666s), amp=0.001
    - S2: prom 0.003, peak @ 109.722s (amp 0.003), key col 0.001
    -       Left trough: idx=54833 (109.666s), amp=0.001
    -       Right trough: idx=54962 (109.924s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.0`
- **Long-Term BPM (Belief)**: `103.2`


## Time: `109.6660s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.0`
- **Long-Term BPM (Belief)**: `103.2`


## Time: `109.7220s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.003, S2/S1=0.12 (Expected max 1.60 at 104 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 104 BPM; prominence ratio 0.12) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 109.530s (amp 0.023), key col 0.001
    -       Left trough: idx=54635 (109.270s), amp=0.001
    -       Right trough: idx=54833 (109.666s), amp=0.001
    - S2: prom 0.003, peak @ 109.722s (amp 0.003), key col 0.001
    -       Left trough: idx=54833 (109.666s), amp=0.001
    -       Right trough: idx=54962 (109.924s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.0`
- **Long-Term BPM (Belief)**: `103.2`


## Time: `109.9240s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.0`
- **Long-Term BPM (Belief)**: `103.2`


## Time: `110.4240s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.005, S2/S1=0.24 (Expected max 1.60 at 103 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 103 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 110.424s (amp 0.021), key col 0.001
    -       Left trough: idx=54962 (109.924s), amp=0.001
    -       Right trough: idx=55286 (110.572s), amp=0.001
    - S2: prom 0.005, peak @ 110.634s (amp 0.006), key col 0.001
    -       Left trough: idx=55286 (110.572s), amp=0.001
    -       Right trough: idx=55480 (110.960s), amp=0.000
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.9`
- **Long-Term BPM (Belief)**: `101.4`


## Time: `110.5720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.9`
- **Long-Term BPM (Belief)**: `101.4`


## Time: `110.6340s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.005, S2/S1=0.24 (Expected max 1.60 at 103 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 103 BPM; prominence ratio 0.24) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 110.424s (amp 0.021), key col 0.001
    -       Left trough: idx=54962 (109.924s), amp=0.001
    -       Right trough: idx=55286 (110.572s), amp=0.001
    - S2: prom 0.005, peak @ 110.634s (amp 0.006), key col 0.001
    -       Left trough: idx=55286 (110.572s), amp=0.001
    -       Right trough: idx=55480 (110.960s), amp=0.000
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.9`
- **Long-Term BPM (Belief)**: `101.4`


## Time: `110.9600s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.9`
- **Long-Term BPM (Belief)**: `101.4`


## Time: `111.1660s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.006, S2/S1=0.34 (Expected max 1.60 at 101 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 101 BPM; prominence ratio 0.34) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 111.166s (amp 0.018), key col 0.001
    -       Left trough: idx=55480 (110.960s), amp=0.000
    -       Right trough: idx=55655 (111.310s), amp=0.001
    - S2: prom 0.006, peak @ 111.410s (amp 0.006), key col 0.001
    -       Left trough: idx=55655 (111.310s), amp=0.001
    -       Right trough: idx=55801 (111.602s), amp=0.000
- **Raw Amp**: `0.018`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.1`
- **Long-Term BPM (Belief)**: `100.4`


## Time: `111.3100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.1`
- **Long-Term BPM (Belief)**: `100.4`


## Time: `111.4100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.017, S2=0.006, S2/S1=0.34 (Expected max 1.60 at 101 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 101 BPM; prominence ratio 0.34) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.017, peak @ 111.166s (amp 0.018), key col 0.001
    -       Left trough: idx=55480 (110.960s), amp=0.000
    -       Right trough: idx=55655 (111.310s), amp=0.001
    - S2: prom 0.006, peak @ 111.410s (amp 0.006), key col 0.001
    -       Left trough: idx=55655 (111.310s), amp=0.001
    -       Right trough: idx=55801 (111.602s), amp=0.000
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.1`
- **Long-Term BPM (Belief)**: `100.4`


## Time: `111.6020s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.1`
- **Long-Term BPM (Belief)**: `100.4`


## Time: `111.8680s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.20 (Expected max 1.60 at 100 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 100 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 111.868s (amp 0.020), key col 0.001
    -       Left trough: idx=55801 (111.602s), amp=0.000
    -       Right trough: idx=56012 (112.024s), amp=0.001
    - S2: prom 0.004, peak @ 112.120s (amp 0.005), key col 0.001
    -       Left trough: idx=56012 (112.024s), amp=0.001
    -       Right trough: idx=56226 (112.452s), amp=0.001
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `81.6`
- **Long-Term BPM (Belief)**: `99.6`


## Time: `112.0240s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `81.6`
- **Long-Term BPM (Belief)**: `99.6`


## Time: `112.1200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.20 (Expected max 1.60 at 100 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 100 BPM; prominence ratio 0.20) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 111.868s (amp 0.020), key col 0.001
    -       Left trough: idx=55801 (111.602s), amp=0.000
    -       Right trough: idx=56012 (112.024s), amp=0.001
    - S2: prom 0.004, peak @ 112.120s (amp 0.005), key col 0.001
    -       Left trough: idx=56012 (112.024s), amp=0.001
    -       Right trough: idx=56226 (112.452s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `81.6`
- **Long-Term BPM (Belief)**: `99.6`


## Time: `112.4520s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `81.6`
- **Long-Term BPM (Belief)**: `99.6`


## Time: `112.5740s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.10 (Expected max 1.60 at 100 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 100 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 112.574s (amp 0.022), key col 0.001
    -       Left trough: idx=56226 (112.452s), amp=0.001
    -       Right trough: idx=56367 (112.734s), amp=0.001
    - S2: prom 0.002, peak @ 112.838s (amp 0.003), key col 0.001
    -       Left trough: idx=56367 (112.734s), amp=0.001
    -       Right trough: idx=56516 (113.032s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.2`
- **Long-Term BPM (Belief)**: `98.9`


## Time: `112.7340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.2`
- **Long-Term BPM (Belief)**: `98.9`


## Time: `112.8380s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.002, S2/S1=0.10 (Expected max 1.60 at 100 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 100 BPM; prominence ratio 0.10) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 112.574s (amp 0.022), key col 0.001
    -       Left trough: idx=56226 (112.452s), amp=0.001
    -       Right trough: idx=56367 (112.734s), amp=0.001
    - S2: prom 0.002, peak @ 112.838s (amp 0.003), key col 0.001
    -       Left trough: idx=56367 (112.734s), amp=0.001
    -       Right trough: idx=56516 (113.032s), amp=0.001
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.2`
- **Long-Term BPM (Belief)**: `98.9`


## Time: `113.0320s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `83.2`
- **Long-Term BPM (Belief)**: `98.9`


## Time: `113.3020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.17 (Expected max 1.60 at 99 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 99 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 113.302s (amp 0.038), key col 0.001
    -       Left trough: idx=56516 (113.032s), amp=0.001
    -       Right trough: idx=56725 (113.450s), amp=0.001
    - S2: prom 0.006, peak @ 113.518s (amp 0.008), key col 0.001
    -       Left trough: idx=56725 (113.450s), amp=0.001
    -       Right trough: idx=56818 (113.636s), amp=0.001
- **Raw Amp**: `0.038`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.2`
- **Long-Term BPM (Belief)**: `97.7`


## Time: `113.4500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.2`
- **Long-Term BPM (Belief)**: `97.7`


## Time: `113.5180s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.037, S2=0.006, S2/S1=0.17 (Expected max 1.60 at 99 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 99 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.037, peak @ 113.302s (amp 0.038), key col 0.001
    -       Left trough: idx=56516 (113.032s), amp=0.001
    -       Right trough: idx=56725 (113.450s), amp=0.001
    - S2: prom 0.006, peak @ 113.518s (amp 0.008), key col 0.001
    -       Left trough: idx=56725 (113.450s), amp=0.001
    -       Right trough: idx=56818 (113.636s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.2`
- **Long-Term BPM (Belief)**: `97.7`


## Time: `113.6360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.2`
- **Long-Term BPM (Belief)**: `97.7`


## Time: `113.7400s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.009, S2/S1=16.41 (Expected max 1.60 at 98 BPM)
    - Contractility Penalty: -3.24 (S2 too prominent for BPM; prominence ratio 16.41 > expected 1.60) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.59: interval 0.438s vs expected 0.612s (deviation 28%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.02: strength ratio 0.02x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.59 x 0.65) + (Amplitude 0.02 x 0.35) = 0.388
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.248s < 0.269s (45% of expected RR) and strength ratio 0.15x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~242 BPM.
    - Confidence penalized 0.52x -> 0.39 to 0.20.
    - Outcome: Rejected Lone S1 (score 0.20 < threshold 0.50)
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.2`
- **Long-Term BPM (Belief)**: `97.7`


## Time: `113.9880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.006, S2/S1=0.69 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.69) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 113.988s (amp 0.010), key col 0.001
    -       Left trough: idx=56818 (113.636s), amp=0.001
    -       Right trough: idx=57067 (114.134s), amp=0.001
    - S2: prom 0.006, peak @ 114.220s (amp 0.007), key col 0.001
    -       Left trough: idx=57067 (114.134s), amp=0.001
    -       Right trough: idx=57160 (114.320s), amp=0.001
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.5`
- **Long-Term BPM (Belief)**: `96.8`


## Time: `114.1340s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.5`
- **Long-Term BPM (Belief)**: `96.8`


## Time: `114.2200s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.009, S2=0.006, S2/S1=0.69 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.69) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.009, peak @ 113.988s (amp 0.010), key col 0.001
    -       Left trough: idx=56818 (113.636s), amp=0.001
    -       Right trough: idx=57067 (114.134s), amp=0.001
    - S2: prom 0.006, peak @ 114.220s (amp 0.007), key col 0.001
    -       Left trough: idx=57067 (114.134s), amp=0.001
    -       Right trough: idx=57160 (114.320s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.5`
- **Long-Term BPM (Belief)**: `96.8`


## Time: `114.3200s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.5`
- **Long-Term BPM (Belief)**: `96.8`


## Time: `114.6280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.26 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 114.628s (amp 0.015), key col 0.001
    -       Left trough: idx=57160 (114.320s), amp=0.001
    -       Right trough: idx=57392 (114.784s), amp=0.001
    - S2: prom 0.004, peak @ 114.848s (amp 0.005), key col 0.001
    -       Left trough: idx=57392 (114.784s), amp=0.001
    -       Right trough: idx=57473 (114.946s), amp=0.001
- **Raw Amp**: `0.015`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.1`
- **Long-Term BPM (Belief)**: `96.6`


## Time: `114.7840s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.1`
- **Long-Term BPM (Belief)**: `96.6`


## Time: `114.8480s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.015, S2=0.004, S2/S1=0.26 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.015, peak @ 114.628s (amp 0.015), key col 0.001
    -       Left trough: idx=57160 (114.320s), amp=0.001
    -       Right trough: idx=57392 (114.784s), amp=0.001
    - S2: prom 0.004, peak @ 114.848s (amp 0.005), key col 0.001
    -       Left trough: idx=57392 (114.784s), amp=0.001
    -       Right trough: idx=57473 (114.946s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.1`
- **Long-Term BPM (Belief)**: `96.6`


## Time: `114.9460s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.1`
- **Long-Term BPM (Belief)**: `96.6`


## Time: `115.3080s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 115.308s (amp 0.021), key col 0.001
    -       Left trough: idx=57473 (114.946s), amp=0.001
    -       Right trough: idx=57731 (115.462s), amp=0.001
    - S2: prom 0.003, peak @ 115.530s (amp 0.004), key col 0.001
    -       Left trough: idx=57731 (115.462s), amp=0.001
    -       Right trough: idx=57836 (115.672s), amp=0.001
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.7`
- **Long-Term BPM (Belief)**: `96.2`


## Time: `115.4620s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.7`
- **Long-Term BPM (Belief)**: `96.2`


## Time: `115.5300s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.003, S2/S1=0.13 (Expected max 1.60 at 97 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 97 BPM; prominence ratio 0.13) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 115.308s (amp 0.021), key col 0.001
    -       Left trough: idx=57473 (114.946s), amp=0.001
    -       Right trough: idx=57731 (115.462s), amp=0.001
    - S2: prom 0.003, peak @ 115.530s (amp 0.004), key col 0.001
    -       Left trough: idx=57731 (115.462s), amp=0.001
    -       Right trough: idx=57836 (115.672s), amp=0.001
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.7`
- **Long-Term BPM (Belief)**: `96.2`


## Time: `115.6720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.7`
- **Long-Term BPM (Belief)**: `96.2`


## Time: `116.0980s`
**S1 (Paired).**
- LOOKAHEAD SUCCESS: Skipped intermediate weak peak (middle prominence 0.001 < 0.35 × S1 prominence 0.026 and next candidate prominence 0.008 > middle)
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.008, S2/S1=0.31 (Expected max 1.60 at 96 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 96 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 116.098s (amp 0.029), key col 0.003
    -       Left trough: idx=57836 (115.672s), amp=0.001
    -       Right trough: idx=58134 (116.268s), amp=0.003
    - S2: prom 0.008, peak @ 116.370s (amp 0.011), key col 0.003
    -       Left trough: idx=58134 (116.268s), amp=0.003
    -       Right trough: idx=58327 (116.654s), amp=0.001
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.5`
- **Long-Term BPM (Belief)**: `95.2`


## Time: `116.2100s`
**Noise/Rejected.**
- Middle peak treated as noise due to weak prominence (0.001 < 0.35 × S1 prominence 0.026) and the following candidate is stronger (next prominence 0.008).
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.5`
- **Long-Term BPM (Belief)**: `95.2`


## Time: `116.2680s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.5`
- **Long-Term BPM (Belief)**: `95.2`


## Time: `116.3700s`
**S2 (Paired).**
- LOOKAHEAD SUCCESS: Skipped intermediate weak peak (middle prominence 0.001 < 0.35 × S1 prominence 0.026 and next candidate prominence 0.008 > middle)
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.008, S2/S1=0.31 (Expected max 1.60 at 96 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 96 BPM; prominence ratio 0.31) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 116.098s (amp 0.029), key col 0.003
    -       Left trough: idx=57836 (115.672s), amp=0.001
    -       Right trough: idx=58134 (116.268s), amp=0.003
    - S2: prom 0.008, peak @ 116.370s (amp 0.011), key col 0.003
    -       Left trough: idx=58134 (116.268s), amp=0.003
    -       Right trough: idx=58327 (116.654s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.5`
- **Long-Term BPM (Belief)**: `95.2`


## Time: `116.6540s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.5`
- **Long-Term BPM (Belief)**: `95.2`


## Time: `116.7640s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.008, S2=0.008, S2/S1=0.97 (Expected max 1.60 at 95 BPM)
    - Contractility Neutral: prominence ratio 0.97 within expected range for 95 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.008, peak @ 116.764s (amp 0.010), key col 0.002
    -       Left trough: idx=58327 (116.654s), amp=0.001
    -       Right trough: idx=58430 (116.860s), amp=0.002
    - S2: prom 0.008, peak @ 117.034s (amp 0.012), key col 0.004
    -       Left trough: idx=58430 (116.860s), amp=0.002
    -       Right trough: idx=58572 (117.144s), amp=0.004
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.2`
- **Long-Term BPM (Belief)**: `94.9`


## Time: `116.8600s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.2`
- **Long-Term BPM (Belief)**: `94.9`


## Time: `117.0340s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.008, S2=0.008, S2/S1=0.97 (Expected max 1.60 at 95 BPM)
    - Contractility Neutral: prominence ratio 0.97 within expected range for 95 BPM, confidence unchanged
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.008, peak @ 116.764s (amp 0.010), key col 0.002
    -       Left trough: idx=58327 (116.654s), amp=0.001
    -       Right trough: idx=58430 (116.860s), amp=0.002
    - S2: prom 0.008, peak @ 117.034s (amp 0.012), key col 0.004
    -       Left trough: idx=58430 (116.860s), amp=0.002
    -       Right trough: idx=58572 (117.144s), amp=0.004
- **Raw Amp**: `0.012`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.2`
- **Long-Term BPM (Belief)**: `94.9`


## Time: `117.1440s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.2`
- **Long-Term BPM (Belief)**: `94.9`


## Time: `117.3480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.009, S2/S1=0.74 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.74) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 117.348s (amp 0.016), key col 0.004
    -       Left trough: idx=58572 (117.144s), amp=0.004
    -       Right trough: idx=58767 (117.534s), amp=0.003
    - S2: prom 0.009, peak @ 117.640s (amp 0.012), key col 0.003
    -       Left trough: idx=58767 (117.534s), amp=0.003
    -       Right trough: idx=58872 (117.744s), amp=0.002
- **Raw Amp**: `0.016`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `95.3`


## Time: `117.5340s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `95.3`


## Time: `117.6400s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.012, S2=0.009, S2/S1=0.74 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.74) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.012, peak @ 117.348s (amp 0.016), key col 0.004
    -       Left trough: idx=58572 (117.144s), amp=0.004
    -       Right trough: idx=58767 (117.534s), amp=0.003
    - S2: prom 0.009, peak @ 117.640s (amp 0.012), key col 0.003
    -       Left trough: idx=58767 (117.534s), amp=0.003
    -       Right trough: idx=58872 (117.744s), amp=0.002
- **Raw Amp**: `0.012`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `95.3`


## Time: `117.7440s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.4`
- **Long-Term BPM (Belief)**: `95.3`


## Time: `117.9340s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.013, S2=0.005, S2/S1=0.42 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.013, peak @ 117.934s (amp 0.015), key col 0.002
    -       Left trough: idx=58872 (117.744s), amp=0.002
    -       Right trough: idx=59035 (118.070s), amp=0.002
    - S2: prom 0.005, peak @ 118.168s (amp 0.007), key col 0.002
    -       Left trough: idx=59035 (118.070s), amp=0.002
    -       Right trough: idx=59192 (118.384s), amp=0.001
- **Raw Amp**: `0.015`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.0`
- **Long-Term BPM (Belief)**: `95.7`


## Time: `118.0700s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.0`
- **Long-Term BPM (Belief)**: `95.7`


## Time: `118.1680s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.013, S2=0.005, S2/S1=0.42 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.42) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.013, peak @ 117.934s (amp 0.015), key col 0.002
    -       Left trough: idx=58872 (117.744s), amp=0.002
    -       Right trough: idx=59035 (118.070s), amp=0.002
    - S2: prom 0.005, peak @ 118.168s (amp 0.007), key col 0.002
    -       Left trough: idx=59035 (118.070s), amp=0.002
    -       Right trough: idx=59192 (118.384s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.0`
- **Long-Term BPM (Belief)**: `95.7`


## Time: `118.3840s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.0`
- **Long-Term BPM (Belief)**: `95.7`


## Time: `118.7020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.22 (Expected max 1.60 at 96 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 96 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 118.702s (amp 0.023), key col 0.001
    -       Left trough: idx=59192 (118.384s), amp=0.001
    -       Right trough: idx=59418 (118.836s), amp=0.001
    - S2: prom 0.005, peak @ 118.922s (amp 0.006), key col 0.001
    -       Left trough: idx=59418 (118.836s), amp=0.001
    -       Right trough: idx=59628 (119.256s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `118.8360s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `118.9220s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.005, S2/S1=0.22 (Expected max 1.60 at 96 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 96 BPM; prominence ratio 0.22) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 118.702s (amp 0.023), key col 0.001
    -       Left trough: idx=59192 (118.384s), amp=0.001
    -       Right trough: idx=59418 (118.836s), amp=0.001
    - S2: prom 0.005, peak @ 118.922s (amp 0.006), key col 0.001
    -       Left trough: idx=59418 (118.836s), amp=0.001
    -       Right trough: idx=59628 (119.256s), amp=0.001
- **Raw Amp**: `0.006`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `119.2560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `85.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `119.5900s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.003, S2/S1=0.14 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 119.590s (amp 0.021), key col 0.002
    -       Left trough: idx=59628 (119.256s), amp=0.001
    -       Right trough: idx=59896 (119.792s), amp=0.002
    - S2: prom 0.003, peak @ 119.882s (amp 0.005), key col 0.002
    -       Left trough: idx=59896 (119.792s), amp=0.002
    -       Right trough: idx=60047 (120.094s), amp=0.001
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.5`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `119.7920s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.5`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `119.8820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.003, S2/S1=0.14 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.14) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 119.590s (amp 0.021), key col 0.002
    -       Left trough: idx=59628 (119.256s), amp=0.001
    -       Right trough: idx=59896 (119.792s), amp=0.002
    - S2: prom 0.003, peak @ 119.882s (amp 0.005), key col 0.002
    -       Left trough: idx=59896 (119.792s), amp=0.002
    -       Right trough: idx=60047 (120.094s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.5`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `120.0940s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `86.5`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `120.4320s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.009, S2/S1=0.45 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.45) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 120.432s (amp 0.021), key col 0.001
    -       Left trough: idx=60047 (120.094s), amp=0.001
    -       Right trough: idx=60305 (120.610s), amp=0.001
    - S2: prom 0.009, peak @ 120.710s (amp 0.010), key col 0.001
    -       Left trough: idx=60305 (120.610s), amp=0.001
    -       Right trough: idx=60493 (120.986s), amp=0.000
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.9`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `120.6100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.9`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `120.7100s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.009, S2/S1=0.45 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.45) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 120.432s (amp 0.021), key col 0.001
    -       Left trough: idx=60047 (120.094s), amp=0.001
    -       Right trough: idx=60305 (120.610s), amp=0.001
    - S2: prom 0.009, peak @ 120.710s (amp 0.010), key col 0.001
    -       Left trough: idx=60305 (120.610s), amp=0.001
    -       Right trough: idx=60493 (120.986s), amp=0.000
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.9`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `120.9860s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `88.9`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `121.1400s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.007, S2/S1=0.26 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 121.140s (amp 0.029), key col 0.001
    -       Left trough: idx=60493 (120.986s), amp=0.000
    -       Right trough: idx=60646 (121.292s), amp=0.001
    - S2: prom 0.007, peak @ 121.388s (amp 0.008), key col 0.001
    -       Left trough: idx=60646 (121.292s), amp=0.001
    -       Right trough: idx=60751 (121.502s), amp=0.001
- **Raw Amp**: `0.029`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.0`
- **Long-Term BPM (Belief)**: `92.0`


## Time: `121.2920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.0`
- **Long-Term BPM (Belief)**: `92.0`


## Time: `121.3880s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.028, S2=0.007, S2/S1=0.26 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.26) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.028, peak @ 121.140s (amp 0.029), key col 0.001
    -       Left trough: idx=60493 (120.986s), amp=0.000
    -       Right trough: idx=60646 (121.292s), amp=0.001
    - S2: prom 0.007, peak @ 121.388s (amp 0.008), key col 0.001
    -       Left trough: idx=60646 (121.292s), amp=0.001
    -       Right trough: idx=60751 (121.502s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.0`
- **Long-Term BPM (Belief)**: `92.0`


## Time: `121.5020s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `90.0`
- **Long-Term BPM (Belief)**: `92.0`


## Time: `121.7480s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.014, S2=0.007, S2/S1=0.47 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.47) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.014, peak @ 121.748s (amp 0.015), key col 0.001
    -       Left trough: idx=60751 (121.502s), amp=0.001
    -       Right trough: idx=60955 (121.910s), amp=0.001
    - S2: prom 0.007, peak @ 122.000s (amp 0.008), key col 0.001
    -       Left trough: idx=60955 (121.910s), amp=0.001
    -       Right trough: idx=61055 (122.110s), amp=0.001
- **Raw Amp**: `0.015`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.1`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `121.9100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.1`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `122.0000s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.014, S2=0.007, S2/S1=0.47 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.47) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.014, peak @ 121.748s (amp 0.015), key col 0.001
    -       Left trough: idx=60751 (121.502s), amp=0.001
    -       Right trough: idx=60955 (121.910s), amp=0.001
    - S2: prom 0.007, peak @ 122.000s (amp 0.008), key col 0.001
    -       Left trough: idx=60955 (121.910s), amp=0.001
    -       Right trough: idx=61055 (122.110s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.1`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `122.1100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.1`
- **Long-Term BPM (Belief)**: `92.3`


## Time: `122.3420s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 122.342s (amp 0.026), key col 0.001
    -       Left trough: idx=61055 (122.110s), amp=0.001
    -       Right trough: idx=61246 (122.492s), amp=0.001
    - S2: prom 0.004, peak @ 122.600s (amp 0.005), key col 0.001
    -       Left trough: idx=61246 (122.492s), amp=0.001
    -       Right trough: idx=61386 (122.772s), amp=0.001
- **Raw Amp**: `0.026`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.0`
- **Long-Term BPM (Belief)**: `92.7`


## Time: `122.4920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.0`
- **Long-Term BPM (Belief)**: `92.7`


## Time: `122.6000s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.024, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 92 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 92 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.024, peak @ 122.342s (amp 0.026), key col 0.001
    -       Left trough: idx=61055 (122.110s), amp=0.001
    -       Right trough: idx=61246 (122.492s), amp=0.001
    - S2: prom 0.004, peak @ 122.600s (amp 0.005), key col 0.001
    -       Left trough: idx=61246 (122.492s), amp=0.001
    -       Right trough: idx=61386 (122.772s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.0`
- **Long-Term BPM (Belief)**: `92.7`


## Time: `122.7720s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `98.0`
- **Long-Term BPM (Belief)**: `92.7`


## Time: `122.9020s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 122.902s (amp 0.023), key col 0.002
    -       Left trough: idx=61386 (122.772s), amp=0.001
    -       Right trough: idx=61526 (123.052s), amp=0.002
    - S2: prom 0.004, peak @ 123.122s (amp 0.005), key col 0.002
    -       Left trough: idx=61526 (123.052s), amp=0.002
    -       Right trough: idx=61669 (123.338s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.2`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `123.0520s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.2`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `123.1220s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.004, S2/S1=0.17 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.17) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 122.902s (amp 0.023), key col 0.002
    -       Left trough: idx=61386 (122.772s), amp=0.001
    -       Right trough: idx=61526 (123.052s), amp=0.002
    - S2: prom 0.004, peak @ 123.122s (amp 0.005), key col 0.002
    -       Left trough: idx=61526 (123.052s), amp=0.002
    -       Right trough: idx=61669 (123.338s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.2`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `123.3380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `96.2`
- **Long-Term BPM (Belief)**: `93.4`


## Time: `123.4420s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.010, S2=0.005, S2/S1=0.49 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.49) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.010, peak @ 123.442s (amp 0.013), key col 0.002
    -       Left trough: idx=61669 (123.338s), amp=0.001
    -       Right trough: idx=61765 (123.530s), amp=0.002
    - S2: prom 0.005, peak @ 123.632s (amp 0.007), key col 0.002
    -       Left trough: idx=61765 (123.530s), amp=0.002
    -       Right trough: idx=61946 (123.892s), amp=0.001
- **Raw Amp**: `0.013`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.3`
- **Long-Term BPM (Belief)**: `94.3`


## Time: `123.5300s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.3`
- **Long-Term BPM (Belief)**: `94.3`


## Time: `123.6320s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.010, S2=0.005, S2/S1=0.49 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.49) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.010, peak @ 123.442s (amp 0.013), key col 0.002
    -       Left trough: idx=61669 (123.338s), amp=0.001
    -       Right trough: idx=61765 (123.530s), amp=0.002
    - S2: prom 0.005, peak @ 123.632s (amp 0.007), key col 0.002
    -       Left trough: idx=61765 (123.530s), amp=0.002
    -       Right trough: idx=61946 (123.892s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.3`
- **Long-Term BPM (Belief)**: `94.3`


## Time: `123.8920s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `99.3`
- **Long-Term BPM (Belief)**: `94.3`


## Time: `124.0220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.011, S2/S1=0.36 (Expected max 1.60 at 94 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 94 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 124.022s (amp 0.031), key col 0.001
    -       Left trough: idx=61946 (123.892s), amp=0.001
    -       Right trough: idx=62078 (124.156s), amp=0.001
    - S2: prom 0.011, peak @ 124.258s (amp 0.012), key col 0.001
    -       Left trough: idx=62078 (124.156s), amp=0.001
    -       Right trough: idx=62237 (124.474s), amp=0.001
- **Raw Amp**: `0.031`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `124.1560s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `124.2580s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.011, S2/S1=0.36 (Expected max 1.60 at 94 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 94 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 124.022s (amp 0.031), key col 0.001
    -       Left trough: idx=61946 (123.892s), amp=0.001
    -       Right trough: idx=62078 (124.156s), amp=0.001
    - S2: prom 0.011, peak @ 124.258s (amp 0.012), key col 0.001
    -       Left trough: idx=62078 (124.156s), amp=0.001
    -       Right trough: idx=62237 (124.474s), amp=0.001
- **Raw Amp**: `0.012`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `124.4740s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `97.3`
- **Long-Term BPM (Belief)**: `94.8`


## Time: `124.5860s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.008, S2/S1=0.43 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.43) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 124.586s (amp 0.021), key col 0.001
    -       Left trough: idx=62237 (124.474s), amp=0.001
    -       Right trough: idx=62371 (124.742s), amp=0.001
    - S2: prom 0.008, peak @ 124.824s (amp 0.010), key col 0.001
    -       Left trough: idx=62371 (124.742s), amp=0.001
    -       Right trough: idx=62604 (125.208s), amp=0.000
- **Raw Amp**: `0.021`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.9`
- **Long-Term BPM (Belief)**: `95.4`


## Time: `124.7420s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.9`
- **Long-Term BPM (Belief)**: `95.4`


## Time: `124.8240s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.008, S2/S1=0.43 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.43) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 124.586s (amp 0.021), key col 0.001
    -       Left trough: idx=62237 (124.474s), amp=0.001
    -       Right trough: idx=62371 (124.742s), amp=0.001
    - S2: prom 0.008, peak @ 124.824s (amp 0.010), key col 0.001
    -       Left trough: idx=62371 (124.742s), amp=0.001
    -       Right trough: idx=62604 (125.208s), amp=0.000
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.9`
- **Long-Term BPM (Belief)**: `95.4`


## Time: `125.2080s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `93.9`
- **Long-Term BPM (Belief)**: `95.4`


## Time: `125.3160s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.18 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 125.316s (amp 0.033), key col 0.003
    -       Left trough: idx=62604 (125.208s), amp=0.000
    -       Right trough: idx=62714 (125.428s), amp=0.003
    - S2: prom 0.005, peak @ 125.522s (amp 0.008), key col 0.003
    -       Left trough: idx=62714 (125.428s), amp=0.003
    -       Right trough: idx=62830 (125.660s), amp=0.001
- **Raw Amp**: `0.033`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `125.4280s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `125.5220s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.030, S2=0.005, S2/S1=0.18 (Expected max 1.60 at 95 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 95 BPM; prominence ratio 0.18) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.030, peak @ 125.316s (amp 0.033), key col 0.003
    -       Left trough: idx=62604 (125.208s), amp=0.000
    -       Right trough: idx=62714 (125.428s), amp=0.003
    - S2: prom 0.005, peak @ 125.522s (amp 0.008), key col 0.003
    -       Left trough: idx=62714 (125.428s), amp=0.003
    -       Right trough: idx=62830 (125.660s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `125.6600s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `125.9840s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.021, S2/S1=18.57 (Expected max 1.60 at 95 BPM)
    - Contractility Penalty: -3.71 (S2 too prominent for BPM; prominence ratio 18.57 > expected 1.60) -> 0.00
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.93: interval 0.668s vs expected 0.634s (deviation 5%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.04: strength ratio 0.04x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.93 x 0.65) + (Amplitude 0.04 x 0.35) = 0.615
    - Forward check failed: next peak arrives too quickly for a true S1.
    - Interval 0.212s < 0.279s (45% of expected RR) and strength ratio 0.08x < 1.69x.
    - This pattern suggests the current peak is S2; accepting it would imply ~283 BPM.
    - Confidence penalized 0.52x -> 0.62 to 0.32.
    - Outcome: Rejected Lone S1 (score 0.32 < threshold 0.50)
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `126.0860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `91.2`
- **Long-Term BPM (Belief)**: `94.4`


## Time: `126.1960s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.006, S2/S1=0.30 (Expected max 1.60 at 94 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 94 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 126.196s (amp 0.023), key col 0.002
    -       Left trough: idx=63043 (126.086s), amp=0.001
    -       Right trough: idx=63177 (126.354s), amp=0.002
    - S2: prom 0.006, peak @ 126.460s (amp 0.008), key col 0.002
    -       Left trough: idx=63177 (126.354s), amp=0.002
    -       Right trough: idx=63369 (126.738s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.4`
- **Long-Term BPM (Belief)**: `92.8`


## Time: `126.3540s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.4`
- **Long-Term BPM (Belief)**: `92.8`


## Time: `126.4600s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.006, S2/S1=0.30 (Expected max 1.60 at 94 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 94 BPM; prominence ratio 0.30) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 126.196s (amp 0.023), key col 0.002
    -       Left trough: idx=63043 (126.086s), amp=0.001
    -       Right trough: idx=63177 (126.354s), amp=0.002
    - S2: prom 0.006, peak @ 126.460s (amp 0.008), key col 0.002
    -       Left trough: idx=63177 (126.354s), amp=0.002
    -       Right trough: idx=63369 (126.738s), amp=0.001
- **Raw Amp**: `0.008`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.4`
- **Long-Term BPM (Belief)**: `92.8`


## Time: `126.7380s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `84.4`
- **Long-Term BPM (Belief)**: `92.8`


## Time: `127.0280s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.008, S2/S1=0.36 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 127.028s (amp 0.022), key col 0.001
    -       Left trough: idx=63369 (126.738s), amp=0.001
    -       Right trough: idx=63593 (127.186s), amp=0.001
    - S2: prom 0.008, peak @ 127.252s (amp 0.009), key col 0.001
    -       Left trough: idx=63593 (127.186s), amp=0.001
    -       Right trough: idx=63822 (127.644s), amp=0.001
- **Raw Amp**: `0.022`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `80.6`
- **Long-Term BPM (Belief)**: `91.8`


## Time: `127.1860s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `80.6`
- **Long-Term BPM (Belief)**: `91.8`


## Time: `127.2520s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.021, S2=0.008, S2/S1=0.36 (Expected max 1.60 at 93 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 93 BPM; prominence ratio 0.36) -> 0.75
    - Recovery Phase Adjust: floor 0.70 → 0.90 (peak at 7.6s)
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.90) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.021, peak @ 127.028s (amp 0.022), key col 0.001
    -       Left trough: idx=63369 (126.738s), amp=0.001
    -       Right trough: idx=63593 (127.186s), amp=0.001
    - S2: prom 0.008, peak @ 127.252s (amp 0.009), key col 0.001
    -       Left trough: idx=63593 (127.186s), amp=0.001
    -       Right trough: idx=63822 (127.644s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `80.6`
- **Long-Term BPM (Belief)**: `91.8`


## Time: `127.6440s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `80.6`
- **Long-Term BPM (Belief)**: `91.8`


## Time: `127.7880s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.006, S2=0.006, S2/S1=1.01 (Expected max 1.60 at 92 BPM)
    - Contractility Neutral: prominence ratio 1.01 within expected range for 92 BPM, confidence unchanged
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.006, peak @ 127.788s (amp 0.007), key col 0.001
    -       Left trough: idx=63822 (127.644s), amp=0.001
    -       Right trough: idx=63972 (127.944s), amp=0.001
    - S2: prom 0.006, peak @ 128.044s (amp 0.007), key col 0.001
    -       Left trough: idx=63972 (127.944s), amp=0.001
    -       Right trough: idx=64195 (128.390s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.3`
- **Long-Term BPM (Belief)**: `91.1`


## Time: `127.9440s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.3`
- **Long-Term BPM (Belief)**: `91.1`


## Time: `128.0440s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.006, S2=0.006, S2/S1=1.01 (Expected max 1.60 at 92 BPM)
    - Contractility Neutral: prominence ratio 1.01 within expected range for 92 BPM, confidence unchanged
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.78
    - Final Score: 0.78 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.006, peak @ 127.788s (amp 0.007), key col 0.001
    -       Left trough: idx=63822 (127.644s), amp=0.001
    -       Right trough: idx=63972 (127.944s), amp=0.001
    - S2: prom 0.006, peak @ 128.044s (amp 0.007), key col 0.001
    -       Left trough: idx=63972 (127.944s), amp=0.001
    -       Right trough: idx=64195 (128.390s), amp=0.001
- **Raw Amp**: `0.007`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.3`
- **Long-Term BPM (Belief)**: `91.1`


## Time: `128.3900s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.3`
- **Long-Term BPM (Belief)**: `91.1`


## Time: `128.5440s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.005, S2/S1=0.18 (Expected max 1.60 at 91 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 91 BPM; prominence ratio 0.18) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 128.544s (amp 0.027), key col 0.001
    -       Left trough: idx=64195 (128.390s), amp=0.001
    -       Right trough: idx=64353 (128.706s), amp=0.001
    - S2: prom 0.005, peak @ 128.792s (amp 0.005), key col 0.001
    -       Left trough: idx=64353 (128.706s), amp=0.001
    -       Right trough: idx=64432 (128.864s), amp=0.000
- **Raw Amp**: `0.027`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `75.7`
- **Long-Term BPM (Belief)**: `90.5`


## Time: `128.7060s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `75.7`
- **Long-Term BPM (Belief)**: `90.5`


## Time: `128.7920s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.026, S2=0.005, S2/S1=0.18 (Expected max 1.60 at 91 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 91 BPM; prominence ratio 0.18) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.026, peak @ 128.544s (amp 0.027), key col 0.001
    -       Left trough: idx=64195 (128.390s), amp=0.001
    -       Right trough: idx=64353 (128.706s), amp=0.001
    - S2: prom 0.005, peak @ 128.792s (amp 0.005), key col 0.001
    -       Left trough: idx=64353 (128.706s), amp=0.001
    -       Right trough: idx=64432 (128.864s), amp=0.000
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `75.7`
- **Long-Term BPM (Belief)**: `90.5`


## Time: `128.8640s`
**Trough Detected**
- **Raw Amp**: `0.000`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `75.7`
- **Long-Term BPM (Belief)**: `90.5`


## Time: `129.3220s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.21 (Expected max 1.60 at 91 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 91 BPM; prominence ratio 0.21) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 129.322s (amp 0.020), key col 0.001
    -       Left trough: idx=64432 (128.864s), amp=0.000
    -       Right trough: idx=64734 (129.468s), amp=0.001
    - S2: prom 0.004, peak @ 129.572s (amp 0.005), key col 0.001
    -       Left trough: idx=64734 (129.468s), amp=0.001
    -       Right trough: idx=64825 (129.650s), amp=0.001
- **Raw Amp**: `0.020`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `129.4680s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `129.5720s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.019, S2=0.004, S2/S1=0.21 (Expected max 1.60 at 91 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 91 BPM; prominence ratio 0.21) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.019, peak @ 129.322s (amp 0.020), key col 0.001
    -       Left trough: idx=64432 (128.864s), amp=0.000
    -       Right trough: idx=64734 (129.468s), amp=0.001
    - S2: prom 0.004, peak @ 129.572s (amp 0.005), key col 0.001
    -       Left trough: idx=64734 (129.468s), amp=0.001
    -       Right trough: idx=64825 (129.650s), amp=0.001
- **Raw Amp**: `0.005`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `129.6500s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `129.7500s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.001, S2=0.022, S2/S1=16.50 (Expected max 1.60 at 90 BPM)
    - Contractility Penalty: -3.26 (S2 too prominent for BPM; prominence ratio 16.50 > expected 1.60) -> 0.00
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.00
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.47: interval 0.428s vs expected 0.668s (deviation 36%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.10: strength ratio 0.10x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.47 x 0.65) + (Amplitude 0.10 x 0.35) = 0.336
    - Outcome: Rejected Lone S1 (score 0.34 < threshold 0.50)
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `129.9400s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.6`
- **Long-Term BPM (Belief)**: `89.5`


## Time: `130.1100s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.009, S2/S1=0.42 (Expected max 1.60 at 89 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 89 BPM; prominence ratio 0.42) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 130.110s (amp 0.023), key col 0.001
    -       Left trough: idx=64970 (129.940s), amp=0.001
    -       Right trough: idx=65138 (130.276s), amp=0.001
    - S2: prom 0.009, peak @ 130.378s (amp 0.011), key col 0.001
    -       Left trough: idx=65138 (130.276s), amp=0.001
    -       Right trough: idx=65316 (130.632s), amp=0.001
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.5`
- **Long-Term BPM (Belief)**: `88.6`


## Time: `130.2760s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.5`
- **Long-Term BPM (Belief)**: `88.6`


## Time: `130.3780s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.022, S2=0.009, S2/S1=0.42 (Expected max 1.60 at 89 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 89 BPM; prominence ratio 0.42) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.022, peak @ 130.110s (amp 0.023), key col 0.001
    -       Left trough: idx=64970 (129.940s), amp=0.001
    -       Right trough: idx=65138 (130.276s), amp=0.001
    - S2: prom 0.009, peak @ 130.378s (amp 0.011), key col 0.001
    -       Left trough: idx=65138 (130.276s), amp=0.001
    -       Right trough: idx=65316 (130.632s), amp=0.001
- **Raw Amp**: `0.011`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.5`
- **Long-Term BPM (Belief)**: `88.6`


## Time: `130.6320s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.5`
- **Long-Term BPM (Belief)**: `88.6`


## Time: `130.8800s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.007, S2/S1=0.28 (Expected max 1.60 at 89 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 89 BPM; prominence ratio 0.28) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 130.880s (amp 0.027), key col 0.002
    -       Left trough: idx=65316 (130.632s), amp=0.001
    -       Right trough: idx=65521 (131.042s), amp=0.002
    - S2: prom 0.007, peak @ 131.116s (amp 0.009), key col 0.002
    -       Left trough: idx=65521 (131.042s), amp=0.002
    -       Right trough: idx=65605 (131.210s), amp=0.001
- **Raw Amp**: `0.027`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.3`
- **Long-Term BPM (Belief)**: `88.0`


## Time: `131.0420s`
**Trough Detected**
- **Raw Amp**: `0.002`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.3`
- **Long-Term BPM (Belief)**: `88.0`


## Time: `131.1160s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.025, S2=0.007, S2/S1=0.28 (Expected max 1.60 at 89 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 89 BPM; prominence ratio 0.28) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.025, peak @ 130.880s (amp 0.027), key col 0.002
    -       Left trough: idx=65316 (130.632s), amp=0.001
    -       Right trough: idx=65521 (131.042s), amp=0.002
    - S2: prom 0.007, peak @ 131.116s (amp 0.009), key col 0.002
    -       Left trough: idx=65521 (131.042s), amp=0.002
    -       Right trough: idx=65605 (131.210s), amp=0.001
- **Raw Amp**: `0.009`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.3`
- **Long-Term BPM (Belief)**: `88.0`


## Time: `131.2100s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `77.3`
- **Long-Term BPM (Belief)**: `88.0`


## Time: `131.6160s`
**S1 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.011, S2/S1=0.54 (Expected max 1.60 at 88 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 88 BPM; prominence ratio 0.54) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 131.616s (amp 0.023), key col 0.003
    -       Left trough: idx=65605 (131.210s), amp=0.001
    -       Right trough: idx=65891 (131.782s), amp=0.003
    - S2: prom 0.011, peak @ 131.882s (amp 0.015), key col 0.004
    -       Left trough: idx=65891 (131.782s), amp=0.003
    -       Right trough: idx=65974 (131.948s), amp=0.004
- **Raw Amp**: `0.023`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `131.7820s`
**Trough Detected**
- **Raw Amp**: `0.003`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `131.8820s`
**S2 (Paired).**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.020, S2=0.011, S2/S1=0.54 (Expected max 1.60 at 88 BPM)
    - Contractility Boost: +0.15 (S1 >> S2 at 88 BPM; prominence ratio 0.54) -> 0.75
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.98
    - Final Score: 0.98 vs Threshold 0.50 -> Paired
- Prominence context:
    - S1: prom 0.020, peak @ 131.616s (amp 0.023), key col 0.003
    -       Left trough: idx=65605 (131.210s), amp=0.001
    -       Right trough: idx=65891 (131.782s), amp=0.003
    - S2: prom 0.011, peak @ 131.882s (amp 0.015), key col 0.004
    -       Left trough: idx=65891 (131.782s), amp=0.003
    -       Right trough: idx=65974 (131.948s), amp=0.004
- **Raw Amp**: `0.015`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `131.9480s`
**Trough Detected**
- **Raw Amp**: `0.004`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `132.0100s`
**Noise/Rejected.**
- S1-S2 pairing decision:
    - Base Conf: 0.60
    - Prominence: S1=0.006, S2=0.029, S2/S1=4.96 (Expected max 1.60 at 88 BPM)
    - Contractility Penalty: -0.73 (S2 too prominent for BPM; prominence ratio 4.96 > expected 1.60) -> 0.00
    - Stability Adjust: x1.30 (Pairing Ratio: 100%, Floor: 0.70) → 0.00
    - Interval penalty by 0.22 (Interval 0.446s > Max 0.400s)
    - Final Score: 0.00 vs Threshold 0.50 -> Not Paired
- Lone S1 decision:
    - Rhythm Fit 0.35: interval 0.394s vs expected 0.684s (deviation 42%; map 0/15/30/50% -> 1.00/0.80/0.40/0.00)
    - Amplitude Fit 0.42: strength ratio 0.42x (map 0/0.4/0.7/1.0 -> 0/0.4/0.8/1.0)
    - Weighted Score: (Rhythm 0.35 x 0.65) + (Amplitude 0.42 x 0.35) = 0.376
    - Outcome: Rejected Lone S1 (score 0.38 < threshold 0.50)
- **Raw Amp**: `0.010`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `132.2880s`
**Trough Detected**
- **Raw Amp**: `0.001`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `87.6`


## Time: `132.4560s`
**Lone S1 (Last Peak).**
- **Raw Amp**: `0.030`
- **Noise Floor**: `0.001`
- **Average BPM (Smoothed)**: `76.8`
- **Long-Term BPM (Belief)**: `86.6`


