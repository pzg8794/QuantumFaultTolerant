# Introduction Reduction Audit for ICNP Draft

This document records the reduction process for Item 022: Introduction reduction.

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 4:47 pm  
**Feedback:**

> Intro will need to be cut down by 1/3rd or so -- too much background information.

## Goal

Reduce the Introduction by roughly one-third while preserving:

1. quantum-network motivation;
2. the routing/resource-allocation problem;
3. the matched-threat evaluation gap;
4. the paper's threat-aware evaluation approach;
5. the main result preview;
6. contribution statements.

## Required reduction method

For this ICNP reduction pass, each paragraph is treated as a mini-section:

1. identify the paragraph's role;
2. split it into conceptual pieces;
3. reduce each split;
4. recombine the reduced pieces;
5. apply a further compression pass when it improves space without hurting clarity;
6. only then stage the accepted text in `ICNP_2026_venue_draft.tex`.

## Working decision

The ICNP draft should avoid repeating the compressed Background section. Broad quantum-network tutorial material should be minimized, while the gap and contribution framing should remain prominent.

## Paragraph 1: Quantum-network motivation

### Original role

Motivate entanglement distribution as a core quantum-Internet primitive, identify why reliable end-to-end entanglement is difficult, and prepare the routing problem.

### Split-level reduction

- **Quantum-Internet motivation:** keep, but short.
- **Reliability challenge:** keep because it explains why routing is nontrivial.
- **Sequential decision framing:** merge into later material because Background and System Model already carry the formal decision framing.

### Recombined reduced paragraph

```tex
Quantum entanglement distribution is a core primitive for the quantum Internet, supporting quantum key distribution, distributed quantum computing, and sensing~\cite{kimble2008quantum,wehner2018quantum,pompili2021realization}. Reliable end-to-end entanglement remains difficult because generation and swapping are probabilistic, quantum states are fragile, and decoherence causes path quality to vary over time~\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}.
```

### Further compressed accepted paragraph

```tex
Quantum entanglement distribution is a core primitive for the quantum Internet, supporting quantum key distribution, distributed quantum computing, and sensing~\cite{kimble2008quantum,wehner2018quantum,pompili2021realization}. Reliable end-to-end entanglement is difficult because generation and swapping are probabilistic, quantum states are fragile, and decoherence makes path quality time-varying~\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}.
```

## Paragraph 2: Quantum routing differs from classical routing

### Original role

Explain why quantum routing is not classical packet routing and why path selection is coupled with qubit allocation.

### Split-level reduction

- **Difference from classical routing:** keep, but remove extended no-cloning/store-and-forward tutorial detail.
- **Coupling of path selection and allocation:** keep because it is central to the paper.
- **Prior-work connection:** preserve citations while avoiding repeated joint-decision explanation.

### Recombined reduced paragraph

```tex
Unlike classical packet routing, quantum routing must establish and consume entanglement under limited memory coherence, probabilistic operations, and fidelity loss~\cite{bennett1993teleporting,zukowski1993event}. These constraints couple path selection with qubit allocation because resource placement affects both success probability and the feedback observed by the learner, motivating routing, allocation, and learning as linked design choices~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

### Further compressed accepted paragraph

```tex
Unlike classical packet routing, quantum routing must establish and consume entanglement under limited memory coherence, probabilistic operations, and fidelity loss~\cite{bennett1993teleporting,zukowski1993event}. These constraints couple path selection with qubit allocation, since resource placement affects both success probability and learner feedback~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

## Paragraph 3: Existing-work gap

### Original role

State the core gap: existing studies are useful but difficult to compare because they vary threat, topology, allocator, and replay assumptions.

### Split-level reduction

- **Prior work exists:** keep to position the paper in the literature.
- **Evaluation assumptions differ:** keep because this is the main gap.
- **Matched-threat evaluation gap:** keep and compress.

### Recombined reduced paragraph

```tex
Existing quantum-routing studies propose online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}. However, they are often evaluated under different assumptions about threat processes, topology visibility, allocator policy, and replay or memory semantics~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. This creates a matched-threat evaluation gap: it is unclear when contextual structure is necessary, when adversarial robustness dominates, and how allocator and capacity choices alter apparent routing performance.
```

### Further compressed accepted paragraph

```tex
Existing quantum-routing studies propose online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}, but they are often evaluated under different threat, topology, allocator, and replay assumptions~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. This creates a matched-threat evaluation gap: it is unclear when contextual structure is necessary, when adversarial robustness dominates, and how allocator and capacity choices alter apparent routing performance.
```

## Paragraph 4: Our approach and result preview

### Original role

Introduce the framework, reference the figure, preview the strongest model family, and state the capacity paradox.

### Split-level reduction

- **Framework:** keep as the paper's approach sentence.
- **Figure reference:** keep because the figure anchors the pipeline.
- **Main result preview:** keep, but avoid repeating detailed abstract numbers.
- **Capacity paradox:** keep because it is a signature finding.

### Recombined accepted paragraph

```tex
To address this gap, we introduce a threat-aware evaluation framework that compares stochastic/contextual, adversarial, predictive, and hybrid bandit policies for joint path selection and qubit allocation under matched threat, allocator, and replay-capacity settings. The evaluation pipeline is summarized in \cref{fig:framework}. Across this controlled grid, pursuit--neural hybrids provide the strongest robustness--efficiency tradeoff, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.
```

### Further compression decision

A semicolon-compressed version was considered but rejected because it made the approach paragraph too dense. The recombined paragraph is the accepted version.

## Paragraph 5: Contributions

### Original role

Summarize the paper's main contributions.

### Split-level reduction

- **Threat-aware evaluation framework:** keep.
- **Allocator/capacity robustness:** keep and merge with the joint-decision formulation.
- **Cross-testbed validation:** keep.
- **List formatting:** convert from an `itemize` list into a compact paragraph to save vertical space.

### Recombined reduced list considered

```tex
To summarize, this work makes three contributions:
\begin{itemize}
    \item \descStep{Threat-aware routing evaluation}{We introduce a unified framework for comparing stochastic, contextual, adversarial, predictive, and hybrid bandit policies for joint entanglement path selection and qubit allocation under matched threat conditions.}

    \item \descStep{Allocator--capacity robustness analysis}{We show that routing robustness depends on the interaction among learning model, allocator policy, and replay-capacity semantics, and identify a threat-dependent capacity paradox in which added capacity helps under structured disruption but hurts under adaptive attacks.}

    \item \descStep{Cross-testbed validation}{We validate the main trends across external quantum-network testbeds and derive deployment guidance for selecting model--allocator--capacity combinations under different threat regimes.}
\end{itemize}
```

### Further compressed accepted paragraph

```tex
This work makes three contributions. First, we introduce a unified threat-aware routing evaluation framework for comparing stochastic, contextual, adversarial, predictive, and hybrid bandit policies for joint entanglement path selection and qubit allocation under matched threat conditions. Second, we show that routing robustness depends on the interaction among learning model, allocator policy, and replay-capacity semantics, identifying a threat-dependent capacity paradox in which added capacity helps under structured disruption but hurts under adaptive attacks. Third, we validate the main trends across external quantum-network testbeds and derive deployment guidance for selecting model--allocator--capacity combinations under different threat regimes.
```

## Figure-color decision

The framework figure in `ICNP_2026_venue_draft.tex` was updated to use the same color coding as the System Model figure language defined in `main.tex`:

- `networkblue` for network topology;
- `envgreen` for threat/environment regimes;
- `algorange` for bandit policy/model families;
- `allocpurple` for allocator and replay/capacity semantics.

This keeps the architecture figure visually aligned with the rest of the manuscript.

## Status

Accepted and staged in `ICNP_2026_venue_draft.tex`.
