
### Long-Term BPM vs Instantaneous BPM
**Problem:** A single misidentified beat could catastrophically shrink s1_s2_max_interval, causing all subsequent beats to be misclassified.

**Solution:** Maintain two BPM values:
- `long_term_bpm`: Slowly adapting belief (0.05 learning rate) that stabilizes the S1-S2 window
- `instant_bpm`: Raw calculation from last interval, used only to update the belief

**Why this works:** Allows the algorithm to self-correct. If instant BPM spikes to 240 but long-term is 120, we know we double-counted S2 and can trigger corrective logic.

**Code:** `update_long_term_bpm()`, `PeakClassifier.state['long_term_bpm']`

### Dynamic S1-S2 Pairing Window
**Problem:** At 90 BPM, true S1-S1 interval is 0.67s. But if s1_s2_max_interval is 0.33s, then at 170 BPM (true interval 0.35s), the algorithm merges separate beats.

**Solution:** `s1_s2_max_interval_sec = min(0.4, expected_rr_interval * 0.6)` where expected_rr comes from long_term_bpm, not last interval.

**Physiological basis:** S1-S2 interval is ~35-50% of total R-R interval and adapts with heart rate.

### Kick-Start Recovery Mechanism
**Problem:** During recovery, S2 disappears. The algorithm enters a "Lone S1 only" mode and can't exit even when S2 reappears.

**Solution:** Scan last 4 beats. If pattern is S1→Noise repeated 3+ times, temporarily boost pairing ratio to 0.60.

**Why this works:** S2 re-emerges as faint peaks that fail normal confidence thresholds. Kick-start gives them a chance to anchor the rhythm again.

**Code:** `_kickstart_check()`, `kickstart_override_ratio`

### Contractility-Based Amplitude Expectations
**Problem:** At low BPM, S2 can be louder than S1 due to breathing or stethoscope position. At high BPM, S1 dominates. Static rules fail.

**Solution:** Use long_term_bpm as proxy for contractility:
- Low BPM (&lt;120): Allow S2 up to 1.6x S1 amplitude
- High BPM (&gt;140): Expect S2 ≤1.2x S1
- Transition zone: Linear interpolation

**Physiological basis:** Sympathetic tone increases both HR and contractility. Higher contractility → louder S1 relative to S2.

**Code:** `adjust_confidence_with_contractility()`, `s2_s1_ratio_low_bpm`, `s2_s1_ratio_high_bpm`

### Recovery Phase Awareness
**Problem:** After exercise, BPM drops but contractile force remains elevated (S1 still loud). Algorithm incorrectly applies low-BPM amplitude rules.

**Solution:** Track peak BPM time. For 120 seconds after peak, use forgiving stability floor (0.90 vs 0.85).

**Code:** `_apply_other_pairing_adjustments()`, `recovery_phase_stability_floor`

### Lookahead Skipping
**Problem:** S2 can ride on the tail of S1, creating three peaks where there should be two (S1-Middle-S2). The middle is noise.

**Solution:** When middle peak is weak AND creates impossible S2→S1 interval, skip it and pair current + next_next.

**Logic chain:** 
1. Check middle prominence &lt; 0.35x S1
2. Check S2→S1 interval would be &lt; min_s1_s2_interval
3. Verify alternative S1→S2' interval is plausible

**Code:** `_process_peak_pair()` lookahead section

### Trapezoid Artifact Detection
**Problem:** A single noise peak causes S1/S2 swap, then another noise swap flips them back. BPM graph shows characteristic "notch."

**Solution:** Post-processing pass identifies trapezoid shapes in smoothed BPM:
- Fast rise (&gt;7 BPM/s)
- Sustained plateau (1.5-15s)
- Fast fall returning to baseline

**Why this works:** Real HR changes are exponential curves, not trapezoids. Trapezoids indicate misclassification, not physiology.

**Code:** `detect_trapezoid_discontinuities()`

---

## Parameter Tuning Rationale

### Noise Floor Parameters
- `trough_rejection_multiplier=4.0`: Reject troughs &gt;4x draft floor. Calibrated to keep physiological troughs while rejecting movement artifacts.
- `noise_window_sec=4`: Rolling window for noise floor. Long enough to smooth out temporary noise, short enough to track gradual changes in background noise.

### Confidence Thresholds
- `pairing_confidence_threshold=0.55`: Empirically determined. Lower values increase false pairs; higher values miss faint S2s.
- `lone_s1_confidence_threshold=0.50`: Must be strong enough to avoid noise, but lenient enough to catch valid single beats when S2 is absent.

### Lookahead Parameters
- `noise_prominence_threshold=0.35`: Middle peak must be &lt;35% of S1 prominence to be considered skippable. Prevents skipping valid S2s.
- `enable_lookahead_skipping=True`: Master switch because lookahead is aggressive. Can be disabled for clean recordings.

---

## Known Limitations & Edge Cases

### Cold Start Problem
**Issue:** First 4 seconds often misclassified because long_term_bpm hasn't stabilized.

**Workaround:** Provide `start_bpm_hint` when possible. The `_kickstart_check` helps but isn't perfect.

**Future:** Could add a "burn-in" pre-pass that analyzes first 10 seconds at higher sensitivity.

### S1/S2 Swapping During Breathing
**Issue:** During inhalation, S1-S2 amplitude difference decreases. Can cause temporary S2→S1 misclassification, especially if timing aligns poorly.

**Current mitigation:** Contractility model helps but doesn't fully solve it. The `penalty_waiver` logic for ideal deviation range catches some cases.

**Future idea:** Track a rolling history of S1-S2 deviation. If deviation suddenly drops without BPM increase, suspect breathing inversion rather than true contractility change.

### Missing S2 in High BPM
**Issue:** Above ~180 BPM, S2 may be physically absent from waveform due to temporal merging with next S1.

**Current solution:** Algorithm gracefully degrades to Lone S1 mode when pairing fails consistently.

**Future:** Could add a "S2 dropout detection" that disables pairing entirely when consecutive Lone S1s exceed threshold at high BPM.

---

## Optimizations:
60% of the script's runtime is conversion time, which is fundamentally unavoidable because it's dominated by FFmpeg decoding the compressed MP4 audio stream
Attempting to optimize the remaining 40% of our script's runtime seems kinda silly in comparison...
**Decode time dominates because:**
- MP4 audio is compressed with complex psychoacoustic models (AAC=O(n²) decode)
- 18 minutes of 44.1kHz stereo AAC = ~120 MB → ~1.9 GB PCM
- FFmpeg must decode every frame sequentially

---

## Future Roadmap

### High-Priority
- [ ] Replace kick-start with more robust "rhythm re-acquisition" model
- [ ] Add breathing detection to improve low-BPM amplitude handling
- [ ] Implement adaptive threshold for `trough_rejection_multiplier` based on signal variance

### Medium-Priority
- [ ] Export intermediate data (peak classifications, confidence scores) for debugging
- [ ] Add "aggressiveness" preset that bundles related parameters
- [ ] Parallelize batch processing (currently uses simple threading loop)

### Low-Priority / Ideas
- [ ] Try machine learning for peak classification (need labeled dataset)
- [ ] Implement spectral fingerprinting for S1/S2 distinction
- [ ] Add phase-rectified signal averaging for noise reduction

