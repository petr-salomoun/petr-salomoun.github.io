---
author: Petr Salomoun
categories:
  - audio
  - psychoacoustics
  - signal-processing
date: 2026-08-11 00:00:00+00:00
description: An optimizer that searches synthesis parameter space to engineer the most acoustically unpleasant sound possible, grounded in psychoacoustic principles of roughness, sharpness, inharmonicity, and tonal instability, with optional calibration from your own A/B listening judgments.
excerpt: An optimizer searches synthesis parameters for roughness, sharpness, inharmonicity, and tonal instability to engineer the most unpleasant sound possible, with audio examples for every layer.
github_repo: petr-salomoun/dissonance
layout: post
tags:
  - psychoacoustics
  - audio-synthesis
  - optimization
  - sound-design
  - signal-processing
title: "Dissonance: Engineering the Most Unpleasant Sound Possible"
updated_at: '2026-08-11T00:00:00+00:00'
---

# dissonance — engineering the most unpleasant sound possible

Psychoacoustics has well-studied principles for what makes sound grate on us. This project turns those principles into synthesis algorithms, then runs an optimizer to find the combination that scores highest on a weighted unpleasantness metric. It can also calibrate the scoring weights from your own A/B listening judgments.

---

## Tonal

The literature points to a handful of perceptual properties — roughness, sharpness, inharmonicity, tonal instability. Each is a distinct mechanism. We implement each as its own synthesis layer so we can study and combine them independently.

---

### Roughness

When two frequency components sit close together inside a single *critical band* — the auditory system's native spectral resolution unit — they beat against each other at 20–200 Hz, producing the sensation psychoacousticians call **roughness**. It is the sound of two slightly detuned strings, scaled up to dozens of partials.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/01_roughness.wav"></audio><br>
▶ [examples/01_roughness.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/01_roughness.wav) — unpleasantness score: **0.99**

---

### Sharpness

Energy concentrated above ~3 kHz feels *piercing* in a way that goes beyond loudness. The German psychoacoustician Zwicker formalized this as **sharpness** (Schärfe), weighted toward the top of the audible range. Think dentist drill, not thunder.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/02_sharpness.wav"></audio><br>
▶ [examples/02_sharpness.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/02_sharpness.wav) — unpleasantness score: **0.52**

---

### FM instability

A stable tone is easy for the auditory system to track and suppress. Chaotic pitch fluctuation — where the modulator itself drifts randomly — prevents that adaptation. The brain keeps reaching for a stable percept and finding none.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/03_fm_instability.wav"></audio><br>
▶ [examples/03_fm_instability.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/03_fm_instability.wav) — unpleasantness score: **0.33**

---

### Stick-slip / screech

The chalk-on-blackboard family. Irregular micro-bursts create stochastic amplitude modulation in the roughness band, but with random timing that *blocks habituation* — the ear never gets to stop noticing it. This mechanism is at work in fingernails on glass, squealing brakes, and alarmed primates.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/04_stickslip.wav"></audio><br>
▶ [examples/04_stickslip.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/04_stickslip.wav) — unpleasantness score: **0.90**

---

### Inharmonic partials

Natural sounds — voices, strings, wind instruments — have overtones at integer multiples of the fundamental. Stretch or compress those ratios and the result sounds broken: metallic but not in a good way, like a bell hit by another bell that disagrees with it. Inharmonicity also generates roughness, because non-integer-ratio partials inevitably land inside the same critical band as other partials at odd intervals.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/05_inharmonic.wav"></audio><br>
▶ [examples/05_inharmonic.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/05_inharmonic.wav) — unpleasantness score: **0.31**

---

### Beating tones

Two pure tones a few Hz apart create a slow amplitude oscillation — **beats** — as they cycle in and out of phase. One or two beats can sound like vibrato. Five simultaneous beaters at slightly different beat rates creates something woozy, unmoored, mildly nauseating.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/06_beating.wav"></audio><br>
▶ [examples/06_beating.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/06_beating.wav) — unpleasantness score: **0.17**

---

### Shaped critical-band noise

Broadband noise becomes nastier when focused on the most sensitive hearing range, roughly 2–6 kHz (the frequency range of speech consonants and, evolutionarily, predator/infant cries). Concentrating noise there simultaneously maximizes roughness and sharpness. Adding 70 Hz AM puts temporal flutter on top.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/07_noise_shaped.wav"></audio><br>
▶ [examples/07_noise_shaped.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/07_noise_shaped.wav) — unpleasantness score: **0.98**

---

## Temporal

The curated showcase under `examples/showcase` reflects the current pipeline. Temporal layers form a separate control axis from the tonal layers above: they shape perceptual motion over time, complementing the tonal texture rather than replacing it.

Listen at low volume.

Each item below is a single temporal layer rendered in isolation, with its manifest score from the current heuristic scorer.

### Scream chaos

Two competing voice-like components create biphonic, alarm-like instability that resists tonal lock-in. Their changing relationship keeps the auditory system searching for a coherent source, making the sound feel urgent and threatening over time.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_01_scream_chaos.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_01_scream_chaos.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_01_scream_chaos.wav) — unpleasantness score: **0.12**

### Dread swell

A slow rise in amplitude increases pressure without introducing a new pitch gesture. Because the tension accumulates gradually and offers no clear release, the listener anticipates an event that never quite arrives.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_02_dread_swell.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_02_dread_swell.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_02_dread_swell.wav) — unpleasantness score: **0.88**

### Shepard ascent

Overlapping octave-shifted tones create the illusion of an endlessly rising pitch. The motion continually promises arrival while looping back beneath awareness, producing an unresolved, vertiginous sense of escalation.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_03_shepard_ascent.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_03_shepard_ascent.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_03_shepard_ascent.wav) — unpleasantness score: **0.54**

### Pulse panic

An accelerating pulse drives the sound from regular repetition toward frantic agitation. The shortening intervals increase arousal and reduce the time available for prediction, so the listener experiences mounting alarm rather than a stable rhythm.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_04_pulse_panic.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_04_pulse_panic.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_04_pulse_panic.wav) — unpleasantness score: **0.90**

### Doom throb

Low-frequency, slightly detuned throbs impose a heavy periodic motion on the mix. The slow energy fluctuations are felt as much as heard, pulling the perceptual center downward and creating oppressive bodily tension.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_05_doom_throb.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_05_doom_throb.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_05_doom_throb.wav) — unpleasantness score: **0.04**

### Wobble drift

A slow detune drift continually moves the pitch center away from where the ear expects it to be. This mild but persistent instability prevents a secure tonal reference from forming, making the sound feel seasick and unreliable.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_06_wobble_drift.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_06_wobble_drift.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_06_wobble_drift.wav) — unpleasantness score: **0.07**

### Uncanny morph

Gradually morphing inharmonic components shift the timbre through combinations that resemble familiar sources without settling into one. That unstable identity exploits the perceptual mismatch between recognizable cues and an impossible acoustic body, creating an uncanny effect over time.

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/component_temporal_07_uncanny_morph.wav"></audio><br>
▶ [examples/showcase/audio/component_temporal_07_uncanny_morph.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/component_temporal_07_uncanny_morph.wav) — unpleasantness score: **0.24**

---

## Showcase: latest pipeline assets

These composites combine the tonal layers above (`rough`, `stickslip`, `fm_instab`, `inharmonic`, `beating`, `noise_shaped`) with named temporal layers. The score shown is the current heuristic scorer's output; it is not a universal human unpleasantness claim.

- **predator_clock** — legacy tonal stack + `scream_chaos`, `pulse_panic`, `uncanny_morph`; score **0.88**
  <audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/composite_01_predator_clock.wav"></audio><br>
  ▶ [examples/showcase/audio/composite_01_predator_clock.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/composite_01_predator_clock.wav)
  ▶ [examples/showcase/presets/composite_01_predator_clock.json](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/presets/composite_01_predator_clock.json)

- **escalating_machine** — legacy tonal stack + `dread_swell`, `shepard_ascent`, `doom_throb`, `wobble_drift`; score **0.89**
  <audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/showcase/audio/composite_02_escalating_machine.wav"></audio><br>
  ▶ [examples/showcase/audio/composite_02_escalating_machine.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/audio/composite_02_escalating_machine.wav)
  ▶ [examples/showcase/presets/composite_02_escalating_machine.json](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/showcase/presets/composite_02_escalating_machine.json)

---

## Optimizing for maximum unpleasantness

Each synthesis method has knobs: carrier frequency, number of partials, AM rate, FM chaos depth, and so on. The optimizer searches jointly over these tonal synthesis parameters and the temporal layer activations and parameters, finding the combination that scores highest. Temporal diversity is part of this search: candidates can activate any combination of the seven named temporal layers, each with its own controls, rather than adding temporal processing as a bolt-on afterward.

**The unpleasantness score** is a weighted sum of normalized acoustic features:

| Feature | What it captures |
|---|---|
| roughness | fast AM beating within critical bands |
| sharpness | high-frequency energy concentration |
| dissonance | spectral dissonance between partial pairs |
| crest factor | transient spikiness / impulsiveness |
| band energy 2–4 kHz | energy in the most aversive frequency region |
| AM energy at 70 Hz | strength of roughness-rate modulation |
| roughness × sharpness | interaction (rough *and* sharp is worse than either alone) |

These features are measured on the final rendered mix, so both tonal layers, which shape the base spectrum, and temporal layers, which shape motion and dynamics, contribute to the same score. For example, `dread_swell` and `pulse_panic` affect crest factor and AM energy at 70 Hz, while `scream_chaos` and `shepard_ascent` can increase roughness and dissonance through unstable partials.

The search runs in two phases: seeded random sampling across the full parameter space, then coordinate-descent hill climbing from the top seeds.

The search runs with sensible defaults out of the box; see [HOWTO.md](HOWTO.md) for the full list of CLI flags and how to tune the sampling budget, search phases, and temporal-layer activation window.

By default the sampler activates a handful of the named temporal layers per candidate while exploring their layer-specific parameters alongside the tonal space; the activation window is tunable, see HOWTO.md for details.

Sweep outputs are saved as WAV + `.json` result pairs, and each rendered WAV also gets a `.params.json` sidecar with full layer/global metadata.

---

## Best results

The optimizer consistently lands near a score of **0.95** when all layers are combined. Here are the top results from the actual optimization run:

**#1 — score 0.95**

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/results_best.wav"></audio><br>
▶ [examples/results_best.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/results_best.wav)

**#2 — score 0.95**

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/results_top2.wav"></audio><br>
▶ [examples/results_top2.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/results_top2.wav)

**#3 — score 0.95**

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/results_top3.wav"></audio><br>
▶ [examples/results_top3.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/results_top3.wav)

**#4 — score 0.95**

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/results_top4.wav"></audio><br>
▶ [examples/results_top4.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/results_top4.wav)

**#5 — score 0.95**

<audio controls src="https://raw.githubusercontent.com/petr-salomoun/dissonance/main/examples/results_top5.wav"></audio><br>
▶ [examples/results_top5.wav](https://github.com/petr-salomoun/dissonance/raw/refs/heads/main/examples/results_top5.wav)

What each layer contributes in the winning presets:
- **rough** — anchors the mix in a dense 3 kHz cluster with fast AM pulse
- **stickslip** — irregular transient grit that refuses to let the ear habituate
- **fm_instab** — continuous pitch wobble so the tone never settles
- **inharmonic** — metallic partials that don't line up with anything harmonic
- **beating** — slow queasy oscillation underneath the brighter layers
- **noise_shaped** — fills 2–6 kHz with harsh, modulated noise
- **uncanny_morph** — appears in every top preset; morphing inharmonic timbre that never resolves into something familiar
- **scream_chaos / shepard_ascent / dread_swell / pulse_panic / wobble_drift** — a rotating pair appears in each preset, adding alarm-like instability, endless-rising illusion, mounting tension, frantic pulsing, or pitch-center drift on top of the tonal floor

---

## A/B calibration

The default scoring weights reflect one reasonable guess at what's unpleasant, but you can calibrate your own preferences with pairwise A/B listening tests — you pick which of two candidates sounds worse, and the weights adapt to match your judgments. See [HOWTO.md](HOWTO.md) for installation, full CLI usage, and how the A/B calibration algorithm works under the hood.
