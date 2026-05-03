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

## Working decision

The ICNP draft should avoid repeating the compressed Background section. Broad quantum-network tutorial material should be minimized, while the gap and contribution framing should remain prominent.

## Conceptual split

### Split 1: Quantum-network motivation

**Role.** Motivate entanglement distribution as a core quantum-Internet primitive and identify why reliable end-to-end entanglement is difficult.

**Decision.** Keep, but compress heavily because the Background section now carries the detailed technical context.

**Accepted reduced piece.**

```tex
Quantum entanglement distribution is a core primitive for the quantum Internet, supporting quantum key distribution, distributed quantum computing, and sensing~\cite{kimble2008quantum,wehner2018quantum,pompili2021realization}. Reliable end-to-end entanglement remains difficult because generation and swapping are probabilistic, quantum states are fragile, and decoherence causes path quality to vary over time~\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}.
```

### Split 2: Routing differs from classical packet switching

**Role.** Explain that quantum routing must establish and consume entanglement under resource and fidelity constraints, coupling path selection with allocation.

**Decision.** Keep the core contrast; remove tutorial-style detail such as extended no-cloning/store-and-forward explanation.

**Accepted reduced piece.**

```tex
Unlike classical packet routing, quantum routing must establish and consume entanglement under limited memory coherence, probabilistic operations, and fidelity loss~\cite{bennett1993teleporting,zukowski1993event}. These constraints couple path selection with qubit allocation: how resources are distributed across candidate paths affects both success probability and the feedback observed by the learner~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

### Split 3: Existing-work gap

**Role.** Identify the matched-threat evaluation gap: prior studies use incompatible assumptions, making robustness comparisons difficult.

**Decision.** Keep. This is the most important Introduction component for ICNP contribution clarity.

**Accepted reduced piece.**

```tex
Existing quantum-routing studies propose online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}, but they are often evaluated under different assumptions about threat processes, topology visibility, allocator policy, and replay or memory semantics~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. This creates a matched-threat evaluation gap: it is unclear when contextual structure is necessary, when adversarial robustness dominates, and how allocator and capacity choices alter apparent routing performance.
```

### Split 4: Our approach and framework

**Role.** State the proposed evaluation framework and connect the figure to the paper story.

**Decision.** Keep and tighten. Avoid repeating all quantitative abstract claims.

**Accepted reduced piece.**

```tex
To address this gap, we introduce a threat-aware evaluation framework that compares stochastic/contextual, adversarial, predictive, and hybrid bandit policies for joint path selection and qubit allocation under matched threat, allocator, and replay-capacity settings. The evaluation pipeline is summarized in \cref{fig:framework}. Across this controlled grid, pursuit--neural hybrids provide the strongest robustness--efficiency tradeoff, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.
```

### Split 5: Contribution list

**Role.** Summarize the paper's main contributions.

**Decision.** Reduce four bullets to three by merging the joint-decision formulation into the framework and allocator/capacity robustness bullets.

**Accepted reduced piece.**

```tex
To summarize, this work makes three contributions:
\begin{itemize}
    \item \descStep{Threat-aware routing evaluation}{We introduce a unified framework for comparing stochastic, contextual, adversarial, predictive, and hybrid bandit policies for joint entanglement path selection and qubit allocation under matched threat conditions.}

    \item \descStep{Allocator--capacity robustness analysis}{We show that routing robustness depends on the interaction among learning model, allocator policy, and replay-capacity semantics, and identify a threat-dependent capacity paradox in which added capacity helps under structured disruption but hurts under adaptive attacks.}

    \item \descStep{Cross-testbed validation}{We validate the main trends across external quantum-network testbeds and derive deployment guidance for selecting model--allocator--capacity combinations under different threat regimes.}
\end{itemize}
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
