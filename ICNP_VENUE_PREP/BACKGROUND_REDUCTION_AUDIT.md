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
| The Multi-Armed Bandit Abstraction | Reduced and accepted for draft staging | Added to `ICNP_2026_venue_draft.tex` |
| Allocation and Capacity Semantics | Reduced and accepted for draft staging | Added to `ICNP_2026_venue_draft.tex` |
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

### Original role

This subsection defines the bandit abstraction and explains why different bandit families correspond to different quantum-routing assumptions and threat models.

### Conceptual split

1. Basic MAB setup: repeated action selection under partial feedback.
2. Exploration/exploitation: the learner must test uncertain paths while using apparently reliable paths.
3. Stochastic bandits: stationary or benign reward assumptions.
4. Contextual and neural contextual bandits: side information and nonlinear reward structure.
5. Adversarial bandits: non-stationary or strategic reward sequences.
6. Predictive/informed bandits: forecast-augmented decisions.
7. Bridge back to quantum routing: different quantum-network conditions motivate different learning families.

### Reduction decision

Keep the taxonomy, but compress it aggressively. ICNP reviewers do not need a bandit tutorial; they need to know why these model families correspond to different routing assumptions.

### Accepted aggressive reduced text

```tex
\subsection{The Multi-Armed Bandit Abstraction}

A multi-armed bandit (MAB) models online routing as repeated action selection under partial feedback, where a learner chooses candidate paths or allocation actions and updates from reward signals such as entanglement success or routing efficiency~\cite{lattimore2020bandit,bubeck2012regret}. We use this taxonomy to distinguish the routing assumptions made by each model family: stochastic methods assume stable rewards~\cite{auer2002finite}, contextual and neural methods exploit predictive side information or nonlinear reward structure~\cite{chu2011contextual,zhou2020neuralucb}, adversarial methods handle non-stationary or strategic rewards~\cite{auer2002nonstochastic}, and predictive/informed methods incorporate forecasts~\cite{kar2024icmab}. This distinction matters for quantum routing because benign noise, topology-dependent feedback, and adaptive disruption favor different forms of learning robustness~\cite{huang2024quantum}.
```

## Audit 3: Allocation and Capacity Semantics

### Original role

This subsection explains why the paper treats allocation and replay/capacity semantics as first-class design variables rather than background implementation details.

### Original text from `main.tex`

```tex
\subsection{Allocation and Capacity Semantics}

In addition to choosing routes, practical quantum routing must manage resource allocation decisions (\eg how many attempts or qubits to allocate across competing paths within a decision epoch). Allocation policies can materially change performance even for the same underlying bandit learner, because they shape both the information collected and the predictability of routing behavior under disruption.

Many learning-based routing implementations also impose finite-memory or replay semantics (\eg bounded histories, windowed updates, or capped experience buffers) that affect stability under nonstationarity and vulnerability under strategic adaptation. These design choices motivate evaluating routing policies jointly with allocator strategy and capacity semantics, rather than treating them as independent knobs.
```

### Conceptual split

1. Path selection is not enough: routing also involves resource allocation.
2. Allocator policy changes learner behavior: allocation shapes feedback and predictability.
3. Replay/capacity semantics affect stability: bounded histories, windows, and buffers matter under nonstationarity.
4. Joint evaluation motivation: allocator and capacity must be evaluated with the routing policy, not as independent knobs.

### Split-level reduction decisions

#### Split 3.1: Path selection is not enough

**Role.** Establishes that the problem is not only route choice, but route choice plus qubit/attempt allocation.

**Decision.** Keep. This supports the paper's protocol/control framing for ICNP.

#### Split 3.2: Allocator policy changes learner behavior

**Role.** Explains why the same bandit learner can behave differently under different allocators.

**Decision.** Keep. This is a major differentiator of the evaluation framework.

#### Split 3.3: Replay/capacity semantics affect stability

**Role.** Introduces the mechanisms behind the later capacity paradox: finite memory, replay windows, and capped buffers.

**Decision.** Keep, but concise.

#### Split 3.4: Joint evaluation motivation

**Role.** Bridges Background into the experimental design by justifying joint evaluation.

**Decision.** Keep as the payoff sentence.

### Accepted aggressive reduced text

```tex
\subsection{Allocation and Capacity Semantics}

Quantum routing couples path choice with resource allocation: the learner must decide both which route to use and how many qubits or attempts to assign within each decision epoch. These allocator choices shape the feedback observed by the bandit learner and the predictability of routing behavior under disruption. Replay or capacity semantics, including bounded histories, windowed updates, and capped experience buffers, further affect stability under nonstationarity and vulnerability to adaptive attacks. We therefore evaluate routing policies jointly with allocator strategy and capacity semantics, rather than treating them as independent implementation details.
```
