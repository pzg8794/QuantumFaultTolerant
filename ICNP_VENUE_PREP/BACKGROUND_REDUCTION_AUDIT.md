# Background Reduction Audit for ICNP Draft

This document records the reduction method used for the Background section before changes are copied into `main.tex`.

## Purpose

The ICNP submission version needs a tighter Background section. The goal is not to delete context blindly, but to identify the essential role of each subsection, split it into smaller conceptual units, and preserve only the minimal material needed for a network-protocols audience.

## Working files

- `main.tex` remains the active full manuscript until a reduction is approved.
- `ICNP_2026_venue_draft.tex` is the runnable IEEE conference draft used to stage accepted reductions.
- This audit document records how each reduction was produced.

## Reduction method

For each Background subsection:

1. Copy the original subsection title and current text from `main.tex`.
2. Split the subsection into conceptual micro-sections.
3. For each micro-section, identify:
   - what role it plays;
   - whether it is essential for ICNP reviewers;
   - what can be removed because it is repeated elsewhere;
   - what must be preserved for citations, motivation, or transition.
4. Write a reduced candidate that keeps only the highest-value material.
5. Review the candidate with the project owner.
6. Add only approved reduced text to `ICNP_2026_venue_draft.tex`.
7. Later, after the full reduced flow is accepted, copy approved text back into `main.tex`.

## Current status

| Subsection | Status | Draft action |
|---|---|---|
| Quantum Networks and Entanglement Routing | Reduced and accepted for draft staging | Added to `ICNP_2026_venue_draft.tex` |
| The Multi-Armed Bandit Abstraction | Under review | Not yet added to draft |
| Allocation and Capacity Semantics | Pending | Placeholder only |
| Problem Scope | Pending | Not yet audited |

## Audit 1: Quantum Networks and Entanglement Routing

### Original role

This subsection explains why quantum routing differs from classical routing and why routing naturally becomes a sequential decision problem under uncertainty.

### Conceptual split

1. Quantum networks distribute entanglement across repeaters and end-nodes.
2. Quantum routing differs from classical packet routing because states are fragile and entanglement operations are probabilistic.
3. Multi-hop paths involve entanglement generation, swapping, decoherence, and fidelity loss.
4. Existing routing assumptions such as stable topology knowledge or fixed allocation rules weaken under online learning and disruption.

### Reduction decision

Keep all four ideas, but compress them into one paragraph. Remove detailed explanation of teleportation and entanglement swapping because those details are already covered implicitly by citations and are not the central contribution.

### Accepted reduced text

```tex
\subsection{Quantum Networks and Entanglement Routing}

Quantum networks distribute entanglement across repeaters and end-nodes to support long-distance quantum communication, distributed quantum computing, and sensing~\cite{wehner2018quantum,kimble2008quantum}. Unlike classical packet routing, quantum routing must operate with fragile states, probabilistic entanglement generation and swapping, decoherence, and fidelity loss~\cite{briegel1998quantum,dahlberg2021netsquid,bennett1993teleporting,zukowski1993event}. Across multi-hop paths, these effects make routing a repeated decision problem under uncertainty, where path choices must adapt to noisy outcomes and changing link conditions. Prior routing approaches often assume stable topology knowledge or fixed allocation rules, assumptions that weaken under online learning, demand variability, and disruptive or strategic interference~\cite{li2025multipath,wang2025learning,huang2024quantum}.
```

## Audit 2: The Multi-Armed Bandit Abstraction

Status: proposed below; not yet accepted into the draft.

### Original role

This subsection defines the bandit abstraction and explains why different bandit families correspond to different quantum-routing assumptions and threat models.

### Conceptual split

1. MAB formalization: action selection, reward observation, regret minimization.
2. Exploration--exploitation trade-off.
3. Stochastic bandits for stationary reward distributions.
4. Contextual and neural contextual bandits for predictive side information and nonlinear reward structure.
5. Adversarial bandits for non-stationary or strategic reward sequences.
6. Predictive/informed bandits for forecast-augmented decisions.
7. Bridge back to quantum routing: benign stochastic noise motivates contextual modeling; strategic disruption motivates adversarial robustness.

### Reduction guidance

The original list is clear but long. For ICNP, the definitions should be compressed because the paper is not a bandit tutorial. Keep the taxonomy only insofar as it supports why the evaluated model families differ.

### Proposed reduced text

```tex
\subsection{The Multi-Armed Bandit Abstraction}

A multi-armed bandit (MAB) models online routing as repeated action selection under partial feedback: at each round, the learner selects a candidate path or allocation action, observes a reward signal such as entanglement success or routing efficiency, and balances exploration against exploitation~\cite{lattimore2020bandit,bubeck2012regret}. Different bandit families capture different routing assumptions: stochastic methods such as UCB assume stable reward distributions~\cite{auer2002finite}, contextual and neural contextual methods use side information or nonlinear reward models when topology or load features are predictive~\cite{chu2011contextual,zhou2020neuralucb}, adversarial methods such as EXP3 target non-stationary or strategic reward sequences~\cite{auer2002nonstochastic}, and predictive/informed methods incorporate forecasts of future conditions~\cite{kar2024icmab}. This taxonomy is useful for quantum routing because benign noise motivates contextual modeling, while adaptive disruption motivates adversarial robustness~\cite{huang2024quantum}.
```

### Open decision

Decide whether the proposed reduced version should be added to `ICNP_2026_venue_draft.tex`.
