# Abstract Reduction Audit for ICNP Draft

This document records the paragraph-by-paragraph abstract reduction for the ICNP venue draft.

## Venue requirement

ICNP submission tracking requires the abstract to be under 250 words and suitable for double-blind review. The original draft abstract was too long and included artifact links plus a rendered reviewer comment.

## Required audit method

For the abstract, the same paragraph-split process is used:

1. identify the original paragraph role;
2. split that paragraph into internal ideas;
3. reduce each split;
4. recombine the reduced paragraph;
5. explicitly document removed paragraphs and why they were removed.

## Paragraph 1: Problem and motivation

### Original role

Establish the quantum-routing problem and explain why brittle assumptions matter.

### Splits and reductions

- **Routing requires joint online decisions:** reduced to `Quantum entanglement routing requires joint path selection and qubit allocation under noisy, nonstationary, and adversarial conditions.`
- **Existing approaches rely on fragile assumptions:** reduced to `Existing approaches often assume stationary links, fixed allocation rules, or offline optimization assumptions.`
- **Why this matters:** reduced to `When these assumptions fail, routing can degrade end-to-end entanglement quality and waste scarce quantum resources.`

### Accepted recombined paragraph

```tex
Quantum entanglement routing requires joint path selection and qubit allocation under noisy, nonstationary, and adversarial conditions. Existing approaches often assume stationary links, fixed allocation rules, or offline optimization assumptions. When these assumptions fail, routing can degrade end-to-end entanglement quality and waste scarce quantum resources.
```

## Paragraph 2: Framework and contribution

### Original role

Introduce the threat-aware framework, the model families, and the algorithm--allocator--capacity interaction.

### Splits and reductions

- **Framework:** reduced to `We introduce a threat-aware evaluation framework for comparing stochastic, contextual/neural, adversarial, predictive, and hybrid bandit policies.`
- **Joint routing task:** reduced to `for joint quantum path selection and qubit allocation.`
- **What prior work fixes:** reduced to `Unlike work that fixes allocator policy and replay semantics,`
- **What our framework varies:** reduced to `we vary threat regime, allocator policy, and replay capacity as first-class factors.`
- **Why that matters:** reduced to `This enables attribution of robustness to the algorithm--allocator--capacity interaction.`

### Accepted recombined paragraph

```tex
We introduce a threat-aware evaluation framework for comparing stochastic, contextual/neural, adversarial, predictive, and hybrid bandit policies for joint quantum path selection and qubit allocation. Unlike work that fixes allocator policy and replay semantics, we vary threat regime, allocator policy, and replay capacity as first-class factors, enabling attribution of robustness to the algorithm--allocator--capacity interaction.
```

## Paragraph 3: Main quantitative results and capacity paradox

### Original role

Report the strongest quantitative findings and the threat-dependent capacity paradox.

### Splits and reductions

- **Overall hybrid performance:** reduced to `Across thirteen algorithms and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points in scenario-aggregated efficiency.`
- **Robustness floor:** reduced to `They sustain worst-case efficiency above 85\% under stochastic threats.`
- **Adaptive attack stability:** reduced to `They remain more stable than adversarial-first EXP3-style designs under adaptive attacks.`
- **Capacity paradox:** reduced to `We also identify a threat-dependent capacity paradox: increasing replay capacity improves efficiency under structured Markov disruption but can induce 22--30 percentage-point efficiency drops under adaptive adversaries.`
- **Interpretation:** reduced to `This shows that resource predictability, not raw capacity, can dominate robustness.`

### Accepted recombined paragraph

```tex
Across thirteen algorithms and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks. We also identify a threat-dependent capacity paradox: increasing replay capacity improves efficiency under structured Markov disruption but can induce 22--30 percentage-point efficiency drops under adaptive adversaries. This shows that resource predictability, not raw capacity, can dominate robustness.
```

## Paragraph 4: Cross-testbed validation

### Original role

State cross-testbed validation and the limits exposed.

### Splits and reductions

- **Validation setting:** reduced to `Cross-testbed evaluation on three external quantum-network simulators confirms the main robustness trends.`
- **Limitation exposed:** reduced to `It also exposes scale- and physics-dependent limits.`

### Accepted recombined paragraph

```tex
Cross-testbed evaluation on three external quantum-network simulators confirms the main robustness trends while exposing scale- and physics-dependent limits.
```

## Paragraph 5: Artifact links and reviewer comment

### Original role

The original fifth paragraph listed public code/data artifact links and included a rendered reviewer note (`\shee{...}`).

### Decision

Remove Paragraph 5 from the ICNP abstract.

### Explicit rationale

This paragraph was removed because artifact links and reviewer/editor comments are submission-hygiene content, not abstract content. The public GitHub and Drive links can also break double-blind review, and rendered reviewer comments must not appear in a submission draft. Reproducibility information should be handled in a separate artifacts/reproducibility section or in a camera-ready version after anonymization, not in the blind abstract.

## Accepted reduced abstract

```tex
\begin{abstract}
Quantum entanglement routing requires joint path selection and qubit allocation under noisy, nonstationary, and adversarial conditions. Existing approaches often assume stationary links, fixed allocation rules, or offline optimization assumptions. When these assumptions fail, routing can degrade end-to-end entanglement quality and waste scarce quantum resources.

We introduce a threat-aware evaluation framework for comparing stochastic, contextual/neural, adversarial, predictive, and hybrid bandit policies for joint quantum path selection and qubit allocation. Unlike work that fixes allocator policy and replay semantics, we vary threat regime, allocator policy, and replay capacity as first-class factors, enabling attribution of robustness to the algorithm--allocator--capacity interaction.

Across thirteen algorithms and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks. We also identify a threat-dependent capacity paradox: increasing replay capacity improves efficiency under structured Markov disruption but can induce 22--30 percentage-point efficiency drops under adaptive adversaries. This shows that resource predictability, not raw capacity, can dominate robustness.

Cross-testbed evaluation on three external quantum-network simulators confirms the main robustness trends while exposing scale- and physics-dependent limits.
\end{abstract}
```

## Status

- Accepted by audit discussion.
- Paragraph 5 removal explicitly documented.
- Pending/paired draft update: replace the abstract in `ICNP_2026_venue_draft.tex`.
