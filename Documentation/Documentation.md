# **BPM Analysis documentation**

# Design theory
The goal is to take PCG data recorded via consumer household equipment and convert it into usable data. Normally, clinical PCG data is captured via advanced and expensive equipment that may not be easily accessible to the general public such as digital stethoscopes etc. My goal is to extract information by using a algorithm to compensate for inadequate hardware. 

The script will track bpm over time like a heart rate monitor, but using a recording of a patient's heartbeat instead. The resulting plot should accurately reflect fast changes in heart rate.

I don't like the idea of using a `start_bpm_hint` as a user input since it makes batch processing impossible. I want the algorithm to be automatic and independent. 
In a ideal world, the user should only need to enter a file, press run, and get the data out. All other logic should be handled by the script

> [!say]
> I want to write my code to be "self documenting". I need to decrease the "mental entropy" required to determine if a future change in the code will clash or make previous bits of code redundant or not. Ideally, a lot of these "band aid fixes" that are currently in the code will be replaced with a more robust algorithm if I can come up with the proper solution. 
> 
> To improve maintainability of my codebase, this documentation.md organizes my brainstorming notes. This documentation file will be used to store the entire explanation behind design choices while brief explanations are written in the code as comments. 
> I'm treating the documentation like a developer's journal since I'm currently the only user of the tool. One of the best ways to make my codebase more maintainable is to write documentation to help explain the design decisions that led to the current state of the codebase.



# General knowledge:
**Phonocardiography (PCG)** is a non-invasive technique that records and analyzes heart sounds and murmurs. It uses a sensitive microphone (phonocardiograph) placed on the chest wall to convert acoustic vibrations into electronic signals, which are then displayed as a waveform (phonocardiogram).
**Key points:**
- **Purpose**: Provides a visual representation of heart sounds (S1, S2, S3, S4) and any pathological murmurs, allowing detailed timing and frequency analysis.
- **Advantage**: Unlike auscultation with a stethoscope, PCG creates a permanent, objective record that can be replayed, measured, and compared over time.
- **Applications**: Diagnosing valvular diseases (e.g., stenosis, regurgitation), congenital heart defects, and cardiac arrhythmias; also used in research and teaching.
- **Modern use**: Often integrated with digital systems and can be combined with ECG for precise correlation with the cardiac cycle.
https://youtu.be/3pwZTYIwBks?t=460



**Audio depends on positioning of the heart relative to the recording device:** 
This is relevant when the patient moves their body, rotates their chest, Inhales or exhales. 
As the diaphragm descends, the heart itself shifts slightly in the chest cavity. It can rotate or move downwards, changing its orientation relative to the fixed position of the stethoscope. 
For example, the heart's rotation might simultaneously move the pulmonic valve closer or into a better acoustic alignment with the stethoscope resulting in a S1 being louder or quieter throughout the recording. 







# Explanation of algorithm logic decision making


### Brainstorming:
> [!think]
> the initial bpm I input is not being respected enough.
> `s1_s2_max_interval_sec` is being updated too frequently and with too much sensitivity. `s1_s2_max_interval_sec` should be determined by the bpm, but shouldn't there be two types of bpm being calculated here?
> a instantaneous bpm, and a more averaged out, long term bpm.
> we can use this long term bpm to determine what the expected bpm should be.
> 
> If I input a suggested bpm of 120, then the script calculates the interval between beats to be at 240bpm. then we can obviously conclude that it counted a S2 as a lone S1, it missed the pairing. So we can also use this discrepancy to work with the normal deviation we calculated in the other step, to definitively conclude that the beat is supposed to be S2.
> obviously my starting bpm suggestion should be value for the long term bpm.
> 
the long term bpm should change slowly and within physiological limits. limited by the `max_bpm` the slope 
I input 90bpm as the start, then the `Long-Term BPM` goes from 90 to 176bpm in 18seconds (86bpm/18s)
since everything is based on the `Long-Term BPM`, we need to make sure it's accurate but not reactive.

> [!think] here's my interpretation of the issue
> - **Hinted 90 BPM**: The `s1_s2_max_interval_sec` is set to approximately 0.33 seconds. The logic assumes any two peaks closer than this are an S1-S2 pair within a _single_ heartbeat.
> - **Actual 170 BPM**: The true interval between _separate_ heartbeats is 60/170≈0.35 seconds.
> - **Actual 181 BPM**: The true interval between _separate_ heartbeats is 60/181≈0.33 seconds.
> 
> when the actual interval between two distinct heartbeats ($0.35$s or $0.33$s) becomes equal to or shorter than the set `s1_s2_max_interval_sec` (0.33s), the algorithm misinterprets them. It sees two separate heartbeats, but because their time difference falls within the "S1-S2" window, it incorrectly considers them as components of a single heartbeat and likely discards one of the peaks. This results in an undercounting of the actual heartbeats and an artificially lower BPM calculation.
> #### Proposed Solution:
> we can use this long term bpm to determine what the expected bpm should be. that way, if the script calculates a bpm that's completely off, it should correct itself.
> for example, If I input a suggested bpm of 120, then the script calculates the interval between beats to be at 240bpm. then we can obviously conclude that it counted a S2 as a lone S1, it missed the pairing. So we can also use this discrepancy to work with the normal deviation we calculated in the other step, to definitively conclude that the beat is supposed to be S2.
> obviously my starting bpm suggestion should be value for the long term bpm.

### Code Implementation:
This concept became the **`update_long_term_bpm()`** function and the **`state['long_term_bpm']`** variable in `bpm_analysis.py`. The key insight was that `s1_s2_max_interval_sec` should be calculated from a **stable, slowly-adapting BPM belief** rather than from the instantaneous interval between the last two beats.
The configuration parameter:
```python
"s1_s2_interval_rr_fraction": 0.7,  # The S1-S2 interval cannot be longer than this fraction of the R-R interval.
```

#### Long-Term BPM vs Instantaneous BPM
**Problem:** A mislabeled beat could drastically shrink s1_s2_max_interval, causing all subsequent beats to be misclassified.
**Solution:** Maintain two BPM values:
- `long_term_bpm`: Slowly adapting belief (0.05 learning rate) that stabilizes the S1-S2 window
- `instant_bpm`: Raw calculation from last interval, used only to update the belief
**Why this works:** Allows the algorithm to self-correct. If instant BPM spikes to 240 but long-term is 120, we know we double-counted S2 and can trigger corrective logic.
**Code:** `update_long_term_bpm()`, `PeakClassifier.state['long_term_bpm']`

#### Dynamic S1-S2 Pairing Window
**Problem:** At 90 BPM, true S1-S1 interval is 0.67s. But if s1_s2_max_interval is 0.33s, then at 170 BPM (true interval 0.35s), the algorithm merges separate beats.
**Solution:** `s1_s2_max_interval_sec = min(0.4, expected_rr_interval * 0.6)` where expected_rr comes from long_term_bpm, not last interval.
**Physiological basis:** S1-S2 interval is ~35-50% of total R-R interval and adapts with heart rate.


## As BPM increases, the S1-S2 prominence differential increases
> [!ask]
> At higher bpm, the loudness of S1 is much louder than S2. why is this?
> I'm looking at the waveform of a heartbeat recording and I can't see S2 at all. at 200 bpm, S1 Is very loud and prominent. 

**at extremely high heart rates (like 200 bpm), diastole shortens dramatically more than systole, leading to a much softer S2 and making S1 appear disproportionately loud.**
1. **Dramatic Shortening of Diastole:**
    - The cardiac cycle has two main phases: **Systole** (ventricular contraction/ejection) and **Diastole** (ventricular relaxation/filling).
    - As heart rate increases, both phases shorten, but diastole shortens proportionally much more than systole.
    - **At 200 bpm:**
        - Cycle length = 60 seconds / 200 beats = **0.3 seconds (300 ms) per beat.**
        - **Systole duration** is relatively fixed by contraction/ejection mechanics. Even at high rates, it might be ~150-200 ms.
        - **Diastole duration** = Cycle length - Systole duration = 300 ms - 150-200 ms ≈ 100-150 ms (or less). Diastole becomes extremely brief.
		Studies of maximal exercise show that systole can occupy 50-60% of the cycle at extreme rates. 
2. **Impact on S2 Loudness (Aortic & Pulmonary Valve Closure):**
    - S2 is produced by the closure of the semilunar valves (aortic and pulmonary) at the end of systole.
    - The loudness of S2 depends significantly on the pressure gradient across these valves at the moment of closure.
    - **Very Short Diastole = Reduced Ventricular Filling (Preload),** With diastole compressed to 100-150 ms, the ventricles have drastically less time to fill with blood before the next contraction.
    - **Reduced Filling = Reduced Stroke Volume,** The amount of blood ejected in the next systole (stroke volume) is much lower.
    - **Lower Stroke Volume = Lower Aortic/Pulmonary Pressure & Weaker Valve Closure:**
        - Less blood is ejected into the arteries.
        - Consequently, the pressure difference forcing the aortic and pulmonary valves shut at the end of systole is much smaller.
        - **Result:** The semilunar valves close much more gently and quietly. **S2 becomes very soft or even inaudible.**
		At 200 bpm, because the heart doesn't have time to fill (low preload), it pumps out very little blood (low stroke volume).
		And because the Stroke Volume is tiny, the system pressure generated is low. S2 is caused by the blood in the aorta snapping back against the valve. If there is less pressure pushing back, the "snap" is weak.
		Also the momentum of the blood, the pressure wave generated by the LV, probably becomes more continuous rather than a pulsing force. the discrete packets of blood excreted by the heart blend together into one continuous flow to some extent. 
3. **Impact on S1 Loudness (Mitral & Tricuspid Valve Closure):**
    - S1 is produced by the closure of the atrioventricular valves (mitral and tricuspid) at the beginning of systole.
    - Its loudness depends on:
        - The **position and tautness of the valve leaflets** at the onset of ventricular contraction.
        - The **force and speed of ventricular contraction** slamming the valves shut.
        - The **pressure gradient** across the closed valves immediately after closure.
    - **High Heart Rate & Sympathetic Tone:** Tachycardia at 200 bpm is almost always driven by high sympathetic nervous system activity (stress, exercise, arrhythmia). This **increases myocardial contractility**.
    - **Forceful Contraction:** Despite reduced filling, the sympathetic drive makes the ventricular contraction **more forceful and rapid**.
    - **Result:** The AV valves are slammed shut vigorously by this forceful contraction. **S1 remains loud, or may even become louder** due to the increased contractility.
    *It's important to note:* 
	- The reduced preload (from ultra-short diastole) results in a lower amplitude sound which should offset the increase in amplitude caused by contractility, but my dataset shows a positive correlation with audio amplitude and BPM. 
4. **Proximity of S2 to the Next S1:**
    - With systole taking ~150-200 ms and the total cycle only 300 ms, S2 occurs very close to the next S1.
    - A soft S2 happening just 100-150 ms before a very loud S1 is easily masked by the louder sound. Your ear (and the waveform) simply can't resolve them as separate events; the loud S1 dominates and overshadows the faint S2.
    - **Primary issue is temporal, not intensity**: At 200 bpm, S2's main problem is being **temporally buried** by the adjacent loud S1, not becoming too soft to exist. The acoustic energy of S1 overwhelms the system before S2's waveform can fully resolve.

**Why S2 gets less prominent at higher heart rates:**
-  **Physiologically Soft:** As explained above, S2 is genuinely much quieter due to reduced valve closure force.
- **Masking by S1:** The loud S1 occurring shortly afterward dominates the acoustic energy and visually overshadows the small S2 deflection on the waveform.
- **Temporal Summation:** The sounds are so close together that their waveforms start to overlap, making S2 indistinguishable from the tail end of S1 or the beginning of the next S1.
- **Equipment Limitations:** Recording equipment (microphones, amplifiers, filters) and display settings (gain, time scale) might not be optimized to capture and resolve such a faint, high-frequency sound occurring so close to a much louder one at an extremely rapid rate. S2 often has higher frequency components than S1, which can be harder to record faithfully.

it's also important to note:
- **Normal Heart Rate:** During long diastole, the ventricles fill, pressures equalize, and the mitral valve leaflets float upward, effectively "pre-closing" before the ventricle contracts. The valve only has to close a tiny distance.
- **200 BPM (Short Diastole):** The ventricle is still actively trying to fill when the next contraction starts. The mitral valve leaflets are still fully open due to the rushing blood flow.
- **The Result:** When the ventricle contracts, the valve leaflets have to travel a large distance to slam shut.
This may also be a contributor for why S1 waveform amplitude increases with BPM.


### Code implementation
#### As BPM increases, the S1-S2 prominence differential increases
**Code Location:** `bpm_analysis.py` `adjust_confidence_with_contractility()`
```python
def adjust_confidence_with_contractility(...):
    # BPM-dependent S2/S1 ratio expectations
    expected_max_ratio = np.interp(
        bpm,
        [params["contractility_bpm_low"], params["contractility_bpm_high"]],
        [params["s2_s1_ratio_low_bpm"], params["s2_s1_ratio_high_bpm"]],
    )
```
**How it works:**
- At high BPM (>140), `expected_max_ratio = 1.2`. If S2 is >1.2x S1 amplitude, it's **penalized heavily** because this is physiologically unlikely.
- At low BPM (<120), `expected_max_ratio = 1.6`. A louder S2 is **accepted** because this matches resting physiology.
**config.py setting:**
```python
"contractility_bpm_high": 140.0,        # Above this BPM, expect S2 ≤1.2x S1
"s2_s1_ratio_high_bpm": 1.2,            # This captures the "S2 disappears" reality
```


## Post-Exercise, S1 amplitude remains elevated despite BPM decreasing
> [!ask]
> I'm listening to a audio file and I notice something interesting. This is a recording of the heart during a period exercise and recovery. At rest, the volume of S1 and S2 are very similar, but at higher bpm, S1 is significantly louder than S2. After the workout ends and heart rate decreases but it seems like the contractile force of the heart sill causes S1 to be significantly louder than S2. 
> 
> Then If I compare the audio from 90bpm post workout to 90 bpm before workout, the amplitude difference between S1 and S2 is larger for the heart post workout.
> 
> Is this expected physiology (is this patient's heart behaving as expected) or a byproduct of my recording device? 

Your observation is the **expected physiology**. This may be called "Inotropic-Chronotropic Dissociation", the heart's rate (speed) and the heart's contractility (force) do not return to baseline at the same time.
The persistence of a relatively loud S1 during early recovery at 90 BPM (compared to pre-exercise 90 BPM) is a real phenomenon caused by **residual sympathetic activation**. This is well-documented in phonocardiography studies.
### Key Mechanisms Explaining Post-Exercise S1 Dominance
#### 1. Sympathetic Tone Persists Beyond Heart Rate Normalization
This is the central mechanism. Beta-adrenergic stimulation affects S1 amplitude more than heart rate:
- **Duration mismatch**: Heart rate recovery begins within 30-60 seconds, but sympathetic neurotransmitter (norepinephrine) clearance and receptor downregulation take **5-10 minutes**
- Contractility remains elevated while Heart Rate is largely controlled by nerve signals (electrical). It can change instantly.
- During recovery, contractility remains augmented while rate falls, creating your observed mismatch
#### 2. The "Cool Down" Effect (Systemic Vascular Resistance)
**Vasodilation diminishes S2:**
- **During/Post-Exercise:** Arteries dilate to supply muscles and release heat. This lowers the resistance in the aorta (Afterload).
- **Impact on S2:** If the arteries are dilated and pressure is lower (which is common immediately post-exercise), the "snap" of the aortic valve is softer.
#### 3. AV Valve Position Remains Altered
From [Merck Manual](http://ncbi.nlm.nih.gov/books/NBK333/) and [Healio](https://www.healio.com/cardiology/learn-the-heart/cardiology-review/topic-reviews/heart-sounds):
- **Shorter effective PR interval**: Elevated sympathetic tone accelerates AV conduction, keeping mitral/tricuspid leaflets **wider apart** at end-diastole
- **Rapid valve closure**: The leaflets close from a greater distance with more force, increasing S1 intensity
- **Preload effects**: Post-exercise, venous return may still be elevated, affecting diastolic filling dynamics
#### 4. S2 Intensity Fails to "Catch Up"
While S1 remains augmented, S2 normalization lags because:
- **Aortic/pulmonary pressure gradients** recover more slowly as stroke volume remains elevated
- **Residual vasodilation** in skeletal muscle beds affects systemic vascular resistance
- **Splitting patterns** remain abnormal during early recovery
### Code Implementation:
#### Post-Exercise, S1 amplitude remains elevated despite BPM decreasing
**Physiology:** Sympathetic tone persists after HR normalizes → contractility remains elevated → S1 stays loud.
**Code Location:** `bpm_analysis.py`, `_apply_other_pairing_adjustments()`
```python
# Recovery phase detection
if (peak_bpm_time_sec is not None and 
    recovery_end_time_sec is not None and
    peak_bpm_time_sec <= current_time_sec <= recovery_end_time_sec):
    # Override stability floor during recovery
    recovery_floor = params.get("recovery_phase_stability_floor", 0.90)
```
**How it works:**
- When `current_time` is within 120 seconds after peak BPM (your `recovery_phase_duration_sec`), the algorithm knows "I'm in recovery mode."
- This prevents the algorithm from penalizing valid S1-S2 pairs when S2 is re-emerging faintly during early recovery.
**config.py settings:**
```python
"recovery_phase_duration_sec": 120,     # Sympathetic tone persists ~2 minutes
"recovery_phase_stability_floor": 0.90, # Be lenient about faint S2s during this window
```
#### S2 Re-Emergence After Dropout
**Physiology:** After S2 disappears at high BPM, it reappears faintly as HR drops. Initial faint peaks are easy to miss.
**Code Location:** `bpm_analysis.py`, `_kickstart_check()`
```python
# Detect S1→Noise pattern
if matches >= min_matches:
    override_ratio = params.get("kickstart_override_ratio", 0.60)
    logging.info(f"KICK-START: Found {matches} patterns. Overriding pairing ratio to {override_ratio}.")
    self.state['pairing_ratio_override'] = override_ratio
```
**How it works:**
- If last 4 beats show pattern: **S1 (Lone) → Noise → S1 (Lone) → Noise**, it means S2 is trying to reappear but being rejected as noise.
- Algorithm **temporarily boosts pairing_ratio to 0.60**, giving faint S2 peaks a chance to be paired.
- This is your "get out of Lone S1 mode" mechanism.
**config.py settings:**
```python
"kickstart_check_threshold": 0.3,           # Only run when pairing_ratio is low
"kickstart_override_ratio": 0.60,           # Temporarily accept more pairs
```
#### Contractility vs. Rate Mismatch (Post-Exercise 90 BPM)
**Physiology:** At 90 BPM post-exercise, contractility is still high (loud S1). At 90 BPM pre-exercise, contractility is normal (balanced S1/S2).
**Code Location:** `bpm_analysis.py`, `PeakClassifier.__init__`
```python
# State initialization uses start_bpm_hint
self.state['long_term_bpm'] = float(start_bpm_hint) if start_bpm_hint else 80.0
self.state['long_term_bpm_history'] = []
```
**How it works:**
- The **entire algorithm's expectation** is anchored to `long_term_bpm`, not instantaneous rate.
- After peak exertion at 170 BPM, `long_term_bpm` slowly decays (learning rate 0.05). At 90 BPM post-exercise, `long_term_bpm` might still be 110-120.
- The contractility model (Section 1 above) uses this **higher belief BPM** → expects S1 dominance → doesn't penalize loud S1 at 90 BPM.
**Example timeline:**
1. Peak: 170 BPM → `long_term_bpm = 170`
2. 1 min later: Instant BPM = 90, but `long_term_bpm` ≈ 120 (slow decay)
3. Algorithm still in "high contractility" mode → expects S1 > S2 → correctly processes post-exercise audio
#### S1 Amplitude Floor (Preventing Noise as S1)
**Physiology:** Even at high BPM, S1 must exceed a minimum amplitude to be a real heartbeat.
**Code Location:** `bpm_analysis.py`, `_validate_lone_s1()`
```python
# Absolute prominence guardrail
if len(recent_prominences) >= 5:
    reference_prominence = np.percentile(recent_prominences, 80)
    if prominence_ratio < params['lone_s1_min_prominence_ratio']:  # Default 0.4
        penalty_factor = float(np.clip(prominence_ratio / 0.4, 0.0, 1.0))
        confidence *= penalty_factor
```
**How it works:**
- Tracks top 20% of recent S1 prominences as reference
- Current S1 must be >40% of reference amplitude, or confidence is slashed
- Prevents noise spikes from being mistaken for S1, even if timing is plausible


## S2 disappears and reappears in some recordings
**Problem:**
In some recordings, when bpm increases, S1 becomes so much louder that S2 is not longer audible in the recording at all. 
When bpm decreases again post exertion, S2 becomes visible again

The mechanism behind this is unclear, but it's a reoccurring trend in my dataset. 
It must be the recording mythology used to capture the data or the position of the stethoscope during exercise etc. 

right now, the pairing history shows 0% pairs made after bpm starts to decrease which is true, but this also causes the current stability adjust logic to tank the confidence making it unlikely to pair S1-S2 afterwards.
Kick-Start Recovery Mechanism feels like a band aid fix to this issue. A more robust solution should be used instead

### Kick-Start Recovery Mechanism
**Problem:** When paring ratio reaches, 0 it's very difficult to begin paring again since lack of pairing decreases pairing ratio. This is a negative feedback loop. 
During recovery, S2 disappears. The algorithm enters a "Lone S1 only" mode and can't exit even when S2 reappears.
**Solution:** Scan last 4 beats. If pattern is S1→Noise repeated 3+ times, temporarily boost pairing ratio to 0.60.
**Why this works:** S2 re-emerges as faint peaks that fail normal confidence thresholds. Kick-start gives them a chance to anchor the rhythm again.
**Code:** `_kickstart_check()`, `kickstart_override_ratio`




## Explanation of prominence calculation
### Peak Prominence Calculation
**Purpose:** Prominence measures how much a peak stands above its local background, making it robust against global volume changes and temporary noise.
Initially, I only compared peaks by their amplitudes but background noise (the noise floor) needed to be accounted for. 
When noise inflates trough heights, prominence will decrease.

**How it's calculated:**
1. **Find adjacent troughs:** For a given peak at index `i`, locate the nearest trough to the left (`i-1`) and right (`i+1`) using the pre-computed `trough_indices`.
2. **Determine key col:** The key col is the **higher** of the two trough amplitudes (the "shoulder" of the peak).
3. **Calculate prominence:** `prominence = peak_amplitude - key_col_amplitude`

**Code:** `get_peak_prominence_details()` in `bpm_analysis.py`
**parameters In `config.py`:**
```python
    "trough_prominence_quantile": 0.1,   # How much a dip must stand out to be considered a 'trough'.
    "trough_rejection_multiplier": 10.0,    # A trough N-times higher than the draft noise floor is rejected.
```

### Trough Sanitization
**Problem:** Temporary noise creates high troughs that inflate the noise floor, reducing prominence of valid peaks that occur after noise ends.
*Temporary noise deviates from the noise floor:*
[![|756x182](https://i.imgur.com/iDTD90X.jpeg)
This specific scenario shown above also creates two "Trapezoid Artifacts" since S1 S2 labeling swaps twice resulting in the correct labeling after. I guess two wrongs do make a right...

**Solution:** During noise floor calculation, reject troughs that exceed 10x the draft floor value. This keeps loud transient noise from affecting the calculated prominence of our peaks during a brief moment of noise. 
**Limitation:** Does not handle noise that occurs between S1 and S2 peaks during the pairing phase.


### Important to note
It's important to note that prominence is calculated against the troughs adjacent to the current peak and not against the noise floor.

> [!think]
> Is it a good idea to have it implemented in this way? I find it a bit questionable but I have no proof that it causes any issues so I'll leave a developer's note here





## Trapezoid Artifacts
### Trapezoid Artifact Detection
**Problem:** A single noise peak causes S1/S2 swap, then another noise swap flips them back. BPM graph shows characteristic "notch."
**This is what It looks like:**
https://github.com/WolfExplode/bpm_analysis/blob/main/Examples/R18%E5%BF%83%E9%9F%B31_bpm_plot.html
![|716x195](https://imgur.com/sIfPq8w.jpg)
![|716x195](https://imgur.com/b7TKFmS.jpg)
**It is caused by these failure modes:**
trapezoid artifact #1
![|422x267](https://imgur.com/jRHjahH.jpg)
trapezoid artifact #2
![|422x246](https://imgur.com/jTFakMB.jpg)
In this case, this file contains two Trapezoid Artifacts. the first one was caused by some noise or PVC during a period where S1 and S2 prominence is similar.
This causes the labeling of S1 and S2 to switch until S1 and S2 prominence deviates enough for the algorithm to correct the mistake resulting in the second trapezoid artifact.
the second trapezoid artifact is caused by peaks labeled LoneS1 followed by S1.

**Solution:**
📌The solution of this issue is only half implemented. I only implemented a way to identify trapezoid artifacts but not a way to use them to make the script more robust

The human eye can easily identify errors in the BPM/time graph so I implemented a function to allow the script to identify them automatically.
Detects trapezoid-shaped discontinuities in the average BPM series that are characteristic of a brief extra-beat artifact:
  - A very fast rise
  - A sustained plateau
  - A very fast fall that returns to baseline
**Code:** `detect_trapezoid_discontinuities()`


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


## Known Limitations & Edge Cases
### Cold Start Problem
**Issue:** First 4 seconds often misclassified because long_term_bpm hasn't stabilized.
**Workaround:** Provide `start_bpm_hint` when possible. The `_kickstart_check` helps but isn't perfect.

**Example of Failure mode:**
![|968x178](https://imgur.com/6BK2wQk.jpg)
![|968x190](https://imgur.com/XEYt7r4.jpg)
In this case, the very first peak was mislabeled as Lone S1 while it was S2. Since this is the first peak of the recording, it's impossible to determine if it's S1 or S2 without scanning backwards and using future knowledge

Ideally, we should have a way to scan backwards to fix errors that occurred before.


### Noisy audio
There's no real way to solve this issue... just don't input noisy audio I guess

### Heartbeat audio with Arrhythmia/PVCs
**Issue:** This software isn't built to detect PVCs or Arrhythmia
**Future idea:** I plan to support this in the future but I haven't come up with a idea yet

### S1/S2 Swapping During Breathing
**Issue:** During inhalation, S1-S2 amplitude difference decreases. Can cause temporary S2→S1 misclassification, especially if timing aligns poorly.
**Current mitigation:** Contractility model helps but doesn't fully solve it. The `penalty_waiver` logic for ideal deviation range catches some cases.
**Future idea:** Track a rolling history of S1-S2 deviation. If deviation suddenly drops without BPM increase, suspect breathing inversion rather than true contractility change.






### Missing S2 in High BPM
**Issue:** Above ~180 BPM, S2 may be physically absent from waveform due to temporal merging with next S1.
**Current solution:** Algorithm gracefully degrades to Lone S1 mode when pairing fails consistently.
**Future:** Could add a "S2 dropout detection" that disables pairing entirely when consecutive Lone S1s exceed threshold at high BPM.


### Trapezoidal waveforms causes the middle of the sound to not be the peak amplitude
I've noticed from the peak detection algorithm, It places the peak at the highest point, but sometimes a wave might look like a cut mountain and sometimes slanted. we basically need to capture the middle of the peak of a trapezoidal wave. 
[![|508x155](https://i.imgur.com/xkhzAQS.png)]
From this example, we can see how the placement of the detected peak is not center with the mass of the waveform resulting in a very small inaccuracy.

![|398x161](Y1rGxdpPAq4.png)
would it be difficult to implement a fix for this? would it even make the results more accurate? Is this even a issue?


## Optimizations:
60% of the script's runtime is conversion time, which is fundamentally unavoidable because it's dominated by FFmpeg decoding the compressed MP4 audio stream
Attempting to optimize the remaining 40% of our script's runtime seems kinda silly in comparison...
**Decode time dominates because:**
- MP4 audio is compressed with complex psychoacoustic models (AAC=O(n²) decode)
- 18 minutes of 44.1kHz stereo AAC = ~120 MB → ~1.9 GB PCM
- FFmpeg must decode every frame sequentially




## Notes about the current state of my codebase
So far, our code has
**Technical debt**: 
If I can find a better solution these band aid fixes would not be here: (e.g., "kick-start" recovery mechanisms, cascade resets)

**Architectural Debt:**
- **Deep call stacks**: 6-stage pipeline with shared state dictionaries makes debugging challenging

**Code Quality:**
- Sparse inline comments in complex logic (e.g., `classify_peaks` loop)

**Redundant Logic:**
There are bits of logic that I implemented to the script that likely do not need to be there. I come up with a idea to solve a problem, then later I come up with a better idea but left the initial solution in the code. Therefore there may be redundancy in logic that's still being used in the code but from a practical standpoint the logic is redundant. 

Right now, I can't name anything off the top of my head but I get the feeling this issue exists.








### Other remarks
The code has several issues that don't fundamentally change the bpm estimation:
- There might be recordings where the stethoscope is removed resulting in no heartbeats at all, do we have a case for this?
	- Well, if the user of this tool inputs garbage then they should get garbage out. Not my fault and not my problem to fix. User error. 


## Unimplemented/Incomplete Ideas:

> [!think]
> Should use **Kalman filter**?

> [!think]
> Should we add a **deque** for sliding windows instead of `params['stability_history_window']` manual slicing? Would that simplify my code?

> [!think]
> I might add parameter presets for simple configuration to the end user. so maybe a config for noisy files, one for if the file has PVCs, arrhythmia, If the file was recorded from the aortic or pulmonary auscultation areas (S1 might be louder or quieter than other files). 


> [!think]
what if we have a interactive way for the user to correct the peak labeling output from the script. then re input the data back into the script. This will allow the user to work together with the algorithm to arrive at the correct answer

> [!think]
> I've noticed that the BPM Trend (Belief) seems to be shifted to the right compared to the calculated Average BPM graph
> is this a issue? there a better way to calculate BPM Trend (Belief) that doesn't result in this happening?

> [!think]
> Research phase-rectified signal averaging for noise reduction






### The S1-S2 interval changes post exertion
I'm listening to another audio file and I make another observation. This is a recording the heart during a period exertion and recovery

The S1-S2 interval is the time between S1 and S2, Systolic Time Interval (STI). This should logically decrease as heart rate increases. 
From what we know about Heart Rate Kinetics, contractility remains elevated post exertion despite a drop in heart rate. We previously spoke about this but we never considered the impact of exertion on the temporal aspect, the  S1-S2 interval. 

I've noticed that after exercise, the S1-S2 interval rapidly decreases and stays low. The S1-S2 interval is much lower for the same bpm than compared to before exertion. 
For example, before exertion, the S1_S2_interval was ~0.195s but after exertion, the S1_S2_interval decreased to between 0.145s and 0.160s. 

The **S1-S2 interval** represents **systolic ejection time**, the period from mitral/tricuspid valve closure (S1) to aortic/pulmonary valve closure (S2). This interval is determined by:
1. **Contractility** (how forcefully the ventricle contracts)
2. **Afterload** (pressure the ventricle pumps against)
3. **Preload** (ventricular filling volume)
4. **Heart rate** (via force-frequency relationship)

**This is caused by both increased cardiac contractility and reduced afterload.**
Residual adrenaline increases the rate of calcium cycling within the cells which causes the muscle to contract faster. This "lag" exists because the electrical pacemaker (SA Node) recovers faster than the chemical removal of adrenaline from the blood.
Post-exercise vasodilation in skeletal muscle beds decreases systemic vascular resistance. This reduces afterload (decreased aortic pressure during ejection). This allows for a faster, shorter ejection. 

In clinical cardiology, this specific measurement (shortening of the QS2 interval or LVET) is sometimes used as a sensitive marker for "adrenergic drive." QS2 Index is often used in stress testing for this purpose. 

> [!think]
> With precise timing data, we can calculate the S1-S2 / Cycle Length ratio (the Duty Cycle of the heart). This would show what percentage of time the heart spends "working" vs "resting" at that specific post-workout moment.

> [!think]
> I want to make our software output the heartbeat labels and timestamps so I can further gather evidence to see if this physiology exists in my dataset. I will make a script that can import the bpm/time graph. Then the S1-S2-S1 interval data and make a correlation. 






### Trapezoid Artifacts
I was considering this but I can no longer find a example of the issue this is describing, This might be because I directly or indirectly solved the issue via other methods. I will document the idea here regardless
> [!say]
> The script kinda flips between S1 and S2 when this event occurs:
> when inhaling, the amplitude difference between S1 and S2 decrease, at this moment, there can be a chance that S2 becomes louder than S1. If the timing is just right, the script can start to mark S2 as S1. 
> 
> two conditions should be fulfilled:
> - A trapezoidal discontinuity around that moment. or the bpm just suddenly increases a lot 
> 	- maybe we should have a secondary tracker for BPM increase? 
> 		I've been very conservative with the rhythm gaiting. basically, I made the script detect if the bpm is "impossible" then tank the confidence. but what if we make the script track how off the R-R interval is from the expected interval and then boos the confidence that S1 and S2 has switched places? This should probably be done in the correction pass
> - the amplitudes between S1 and S2 get closer together. so how do we detect this?
> 	- We should store a history of highest S1 peaks and lowest S2 peaks and then get a idea of the maximum deviation between them. then we can do the same with the lowest...
> 
> We need to calculate a history of the lowest 25% quartile of S2 peaks. so we track the past 50 S2 getting the lowest 25% quartile
- [ ] Implemented




### Find a way to input more data into the algorithm to help it identify S1 and S2
> [!say]
> I wonder, is it possible to record a spectral fingerprint for S1 and S2 heart sounds?
> Like, each recording has a different audio characteristic
> But within the file, every S1 should sound similar
> And be distinct from S2
> If this is true, there must be a way to exploit this
- [ ] Implemented

> [!think]
> S2's higher frequency components (up to 250 Hz) are different S1's lower frequencies. I think there should be a way to exploit this. I need to confirm whether or not this frequency separation exists in my dataset before I try to isolate it. 


Each beat, S1 and S2 should have a distinct sound that gives it its unique "profile".  

> [!think]
> Looking at `Test4_bpm_plot.html`,
> I wonder, Is it possible make a profile for S1 and S2 heart sounds? that data would be very large. I'm thinking of a way to compress/express this profile data in a easy to parse way.
> what If we apply different EQ band filters for ever 100 hz or something. This will generate different amplitude peaks for each peak. Then we can get the difference and compare.
> 
>So far, we haven't needed to compress the input data because the peak detection algorithm naturally outputs simple and easily parsable data. The additional data I plan to input input to the algorithm will not be easily parsable so I need to find a way to "compress the info" into a more "parsable" format. 
>
> I'm just trying to get a way to make the algorithm understand what S1 and S2 *sounds* like. currently, The algorithm knows what S1 and S2 *look* like from a point wise perspective. (there's no logic for trapezoidal shaped waveforms yet). The current data being fed into the algorithm is very minimal which means the current algorithm has to make many educated guesses. If I can find a way to efficiently compress beat "profile" data and feed it into the algorithm, then I should be able to make it substantially more robust. 


> [!think]
> Right now, the algorithms confidence is artificially boosted
> If we look at the input data the algorithm is receiving. There are many instances where logically there should be no way the algorithm can determine a answer. 
> But right now it does
> I've done this intentionally as a band aid fix. I wanted more labeling but I must acknowledge that many peaks are being labeled correctly because the algorithm is simply making a lucky guess





















### Breathing:

#### How Heavy Breathing Modifies Heart Sounds
**During Inspiration:**
- Increased venous return causes right ventricular preload to increase
- RV stroke volume increases causes pulmonary flow to increase
- S2 splitting widens (P2 delayed)
- S1 may soften slightly as increased lung volume dampens transmission
	- [ ] Is this observed in our dataset? 
**During Expiration:**
- Decreased venous return results in a drop in RV preload
- S2 becomes single (A2-P2 fuse)
- Heart shifts position to be closer to chest wall, potentially amplifying sounds
	- [ ] is this observed in our dataset? 

#### Respiratory Sinus Arrhythmia (RSA)
Heart rate increases during inspiration
Heart rate decreases during expiration
- [ ] Is this observed in our dataset? 

Breathing, Lung sounds (bronchial airflow) should create high-frequency noise (100-1000 Hz)
- [ ] Is this observed in our dataset? 





#### unimplemented
I want a way to identify breathing from the audio

graph the temporary noise by taking the troughs and comparing to the noise floor. then graphing that value
the idea is, temporary noise might be from breathing so by doing this, we might be able to visualize breathing. 
What if we do a different EQ filter on the initial audio to scan for breathing sounds instead?


Normal breathing causes physiological splitting of S2, can we use this to our advantage?
first, we need to be able to determine if our dataset contains this phenomenon 

#### unimplemented
Let's brainstorm based on some patterns that we can observe from the data. Take a look at how S1 is substantially louder than S2, but then there is some temporary noise that's spread out. When the noise increases, S1 amplitude decreases. 
we can also observe the inverse for S2. when noise increases S2 increases as well. At first I thought this was because the amplitude of S2 was "riding on top of" the noise but since S1 was decreasing this doesn't make sense.

Then I realized the noise must be from breathing since it's gradual fade in and out. 
Let's try to understand the heart's function and how the audio is being recorded. S1 must be decreasing since the stethoscope is further away from the chest at that time. but then why does S2 increase instead? the `trough-S2-trough` distance increases during breathing?
Is this normal physiology?

**Positional Shift:** As the diaphragm descends, the heart itself shifts slightly in the chest cavity. It can rotate or move downwards, changing its orientation relative to the fixed position of the stethoscope.
The heart's rotation might simultaneously move the pulmonic valve closer or into a better acoustic alignment with the stethoscope.

[![|1069x171](https://i.imgur.com/IFUuykq.png)]
By looking at the noise floor and toughs, we can clearly see the affect of breathing in the waveform:
[![|1667x96](https://i.imgur.com/HuYGxhi.png)
> [!think]
> how can we apply these observations to make our script more robust?



### Modeling Heart contractility
Regarding The idea of contractile force, what if we could display how hard the heart contracts by examining the amplitude deviation between S1 and S2 and mapping a trend.

Nah but that depends on how the audio is recorded. just because S1 is louder than S2 in this recording, doesn't specifically mean that the heart is contracting strongly. 
but there must be a positive correlation with total audio amplitude and contractile force. obviously heart contractility correlates with bpm, but my idea is to further identify when the contractility of the heart is seemingly misaligned with bpm. Such as Post-Exercise S1 Dominance as documented previously. 





### heartbeat_labeler.py
> [!say] regarding my heartbeat_labeler.py
> I originally made this script to label sections of data, but now I want to use it to label a entire audio file. Let's make this tool more usable for labeling entire files.
> Right now, the too close warning is based on the grouping logic, but since there's only going to be one group now, the warning pops up for sections where the bpm is just fast.
> We could fix this by appling auto groups every 10 seconds regardless of how many labels are in each group. just a pure time based grouping.
> the Time Range Analysis feature will be made redundant.
> 
> 
> I've been doing this manual data labeling for a while now, but why don't we find a way to export the labeling data directly from my script. then write a software that allows me to fix/edit those labels. this will speed up my labeling workflow immensely





























``` title:"Mermaid diagram for algorithm's logic flow"
flowchart TD
    %% Input Stage
    A[Input Audio File] --> B[Is .wav?]
    B -- NO --> C[Convert to WAV]
    B -- YES --> D
    C --> D

    %% Stage 1: Preprocessing
    subgraph Stage1[Stage 1: Preprocessing]
        D[Preprocess Audio] --> E[Calculate Audio Envelope]
        E --> F[Find All Potential Troughs]
        
        %% Fallback for insufficient troughs
        F --> G[Enough troughs?
>= 5 troughs]
        G -- YES --> G1[Calculate Dynamic Noise Floor 
& Sanitize Troughs]
        G -- NO --> G2["Use Static Noise Floor
(Fallback)"]
        G1 --> H
        G2 --> H
        
        H[Find Raw Peaks Above Noise Floor]
    end

    H --> I

    %% Stage 2: Preliminary Pass
    subgraph Stage2[Stage 2: Preliminary Pass]
        I[Run Preliminary Pass
with High-Confidence Threshold] --> I1[High-Confidence PeakClassifier]
        I1 --> I2["Extract Anchor Beats
(S1 peaks from pass)"]
        
        %% Fallback for insufficient anchor beats
        I2 --> I3[Anchor beats >= 10?]
        I3 -- YES --> I4[Estimate Global BPM from Median RR]
        I3 -- NO --> I5["Use Default BPM = 80.0
(Fallback)"]
        
        I4 --> I6[Detect Peak Time & Recovery Phase Boundaries]
        I5 --> I6
        I6 --> J
    end

    %% Stage 3: Main Classification Loop
    subgraph Stage3[Stage 3: Main Classification Loop]
        J[Initialize Main PeakClassifier] --> K[Begin Main Classification Loop
loop_idx = 0]
        
        %% Kickstart check is per-iteration
        K --> L[Per-Iteration Kickstart Check
Override Pairing Ratio if Stuck]
        L --> M[More Peaks Remain?]
        M -- NO --> ZZ[Return: s1_peaks, all_raw_peaks, analysis_data]
        M -- YES --> N[Get Current and Next Peak]
        
        N --> O["Check for Weak Middle Peak?
(lookahead enabled)"]
        O -- YES --> O1[Evaluate Middle Peak Prominence & Interval]
        O1 -- YES --> O2[Skip Middle: Pair Peaks, Mark as Noise]
        O2 --> M
        O1 -- NO --> P
        O -- NO --> P
        
        P[Attempt S1-S2 Pairing] --> P1[Check Minimum Interval Constraint]
        P1 --> P2[Calculate Base Confidence]
        P2 --> P3[Adjust for Contractility]
        P3 --> P4[Apply Stability & Other Adjustments]
        P4 --> P5[Apply Interval & Forward-Look Penalties]
        P5 --> Q[Pairing Confidence High Enough?]
        
        Q -- YES --> R[Label as Paired S1 and S2]
        Q -- NO --> S[Classify Lone Peak]
        
        S --> T[Validate Lone S1
- Rhythm check
- Amplitude check
- Forward check]
        T --> U[Is Valid Lone S1?
 >= threshold]
        
        U -- YES --> V[Label Validated Lone S1]
        U -- NO --> W[Cascade Reset Triggered?
consecutive rejections >= 3]
        W -- YES --> X[Label Cascade Lone S1]
        W -- NO --> Y[Label as Noise]
        
        R --> Z[Update Long-Term BPM]
        V --> Z
        X --> Z
        Y --> Z
        Z --> M
    end

    %% Transition to Stage 4
    ZZ -- "Proceed to Stage 4
with returned data" --> AA

    %% Stage 4: Correction & Refinement
    subgraph Stage4[Stage 4: Correction & Refinement]
        AA[Rhythm-Based Correction] --> AA1[Resolve Adjacent S1 Conflicts
Keep Stronger Amplitude]
        AA1 --> BB[Fix Rhythmic Discontinuities]
        
        BB --> BB1["Pass 1: Find Long Gaps
(missed beats)"]
        BB1 --> BB2[Search for Missed S1-S2 Pairs
in noise-labeled peaks]
        BB2 --> BB3[Relabel Corrected Gaps]
        
        BB3 --> BB4["Pass 2: Find Short Conflicts
(adjacent S1s)"]
        BB4 --> BB5[Resolve Short Conflicts
remove weaker peak]
        
        BB5 --> BB6["More Corrections Made?
(max 5 iterations)"]
        BB6 -- YES --> BB1
        BB6 -- NO --> CC[Final Corrected S1 Peaks & Debug Info]
    end

    CC --> DD

    %% Stage 5: Final Metrics & Output
    subgraph Stage5[Stage 5: Final Metrics & Output]
        DD[Calculate Final Metrics] --> EE[Calculate BPM Series]
        EE --> FF[Detect Trapezoid Artifacts]
        FF --> GG[Calculate Windowed HRV]
        GG --> HH[Find HR Inclines and Declines]
        
        %% Split HRR calculations
        HH --> II1["Calculate Standard HRR
(fixed interval)"]
        II1 --> II2["Calculate Peak Recovery Rate
(steepest slope)"]
        
        II2 --> JJ[Generate Summary Statistics]
        
        JJ --> KK[Generate Interactive Plot]
        KK --> LL[Generate Reports: CSV, Summary, Debug Log, BPM Text]
    end
```
