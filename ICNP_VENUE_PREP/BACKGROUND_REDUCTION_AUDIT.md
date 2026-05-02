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

### Original role

This subsection defines the bandit abstraction and explains why different bandit families correspond to different quantum-routing assumptions and threat models.

### Original text from `main.tex`

```tex
\subsection{The Multi-Armed Bandit Abstraction}

A multi-armed bandit (MAB) formalizes online routing as follows: at each time step $t$, an agent selects one of $K$ candidate actions (\eg paths or allocation decisions), observes a reward signal (\eg entanglement success/failure or efficiency proxy), and aims to minimize regret relative to an oracle policy~\cite{lattimore2020bandit}. The central challenge is the exploration--exploitation trade-off: learning which actions are reliable while maintaining high routing performance~\cite{bubeck2012regret}.

Several bandit variants align with different quantum-network assumptions and threat models:
\begin{itemize}[leftmargin=2em]
\item \textbf{Classical (stochastic) bandits} assume stationary reward distributions (\eg UCB-style methods)~\cite{auer2002finite}.
\item \textbf{Contextual bandits} incorporate observable side information (\eg topology features or load indicators) to improve decisions when context is predictive~\cite{chu2011contextual}.
\item \textbf{Neural contextual bandits} use function approximation to model nonlinear reward while preserving principled exploration via uncertainty-aware decision rules~\cite{zhou2020neuralucb}.
\item \textbf{Adversarial bandits} guard against worst-case or non-stochastic reward sequences (\eg EXP3 algorithm)~\cite{auer2002nonstochastic}.
\item \textbf{Predictive/informed bandits} augment decisions with forecasts of future conditions~\cite{kar2024icmab}.
\end{itemize}

This taxonomy provides a natural lens for quantum routing: stochastic noise motivates contextual/neural modeling, while strategic disruption motivates adversarial robustness~\cite{huang2024quantum}.
```

### Conceptual split

1. Basic MAB setup: repeated action selection under partial feedback.
2. Exploration/exploitation: the learner must test uncertain paths while using apparently reliable paths.
3. Stochastic bandits: stationary or benign reward assumptions.
4. Contextual and neural contextual bandits: side information and nonlinear reward structure.
5. Adversarial bandits: non-stationary or strategic reward sequences.
6. Predictive/informed bandits: forecast-augmented decisions.
7. Bridge back to quantum routing: different quantum-network conditions motivate different learning families.

### Split-level reduction decisions

#### Split 2.1: Basic MAB setup

**Role.** Defines the learning abstraction: the learner repeatedly selects an action and observes feedback.

**Decision.** Keep, but remove the full regret/oracle wording because System Model and Results handle oracle-normalized metrics later.

**Reduced piece.**

```tex
A multi-armed bandit (MAB) models online routing as repeated action selection under partial feedback, where a learner chooses candidate paths or allocation actions and updates from reward signals such as entanglement success or routing efficiency~\cite{lattimore2020bandit,bubeck2012regret}.
```

#### Split 2.2: Exploration/exploitation

**Role.** Explains the basic learning tension.

**Decision.** Keep implicitly rather than as a standalone explanation, because ICNP readers do not need a bandit tutorial.

**Reduced piece.** Included in the phrase "updates from reward signals" and in the model-family distinction.

#### Split 2.3: Stochastic bandits

**Role.** Introduces stationary/no-benign-threat baseline assumptions.

**Decision.** Keep as a short clause.

**Reduced piece.**

```tex
stochastic methods assume stable rewards~\cite{auer2002finite}
```

#### Split 2.4: Contextual and neural contextual bandits

**Role.** Introduces side-information and nonlinear reward models.

**Decision.** Keep, but merge contextual and neural contextual families into one clause to save space.

**Reduced piece.**

```tex
contextual and neural methods exploit predictive side information or nonlinear reward structure~\cite{chu2011contextual,zhou2020neuralucb}
```

#### Split 2.5: Adversarial bandits

**Role.** Connects learning model choice to strategic/non-stationary threat regimes.

**Decision.** Keep because adversarial robustness is central to the paper.

**Reduced piece.**

```tex
adversarial methods handle non-stationary or strategic rewards~\cite{auer2002nonstochastic}
```

#### Split 2.6: Predictive/informed bandits

**Role.** Explains forecast-augmented model families.

**Decision.** Keep as a short clause while predictive/informed methods remain in the evaluated family set.

**Reduced piece.**

```tex
predictive/informed methods incorporate forecasts~\cite{kar2024icmab}
```

#### Split 2.7: Bridge back to quantum routing

**Role.** Prevents the subsection from feeling like generic bandit background by tying taxonomy to quantum-routing conditions.

**Decision.** Keep and make it the closing sentence.

**Reduced piece.**

```tex
This distinction matters for quantum routing because benign noise, topology-dependent feedback, and adaptive disruption favor different forms of learning robustness~\cite{huang2024quantum}.
```

### Accepted aggressive reduced text

```tex
\subsection{The Multi-Armed Bandit Abstraction}

A multi-armed bandit (MAB) models online routing as repeated action selection under partial feedback, where a learner chooses candidate paths or allocation actions and updates from reward signals such as entanglement success or routing efficiency~\cite{lattimore2020bandit,bubeck2012regret}. We use this taxonomy to distinguish the routing assumptions made by each model family: stochastic methods assume stable rewards~\cite{auer2002finite}, contextual and neural methods exploit predictive side information or nonlinear reward structure~\cite{chu2011contextual,zhou2020neuralucb}, adversarial methods handle non-stationary or strategic rewards~\cite{auer2002nonstochastic}, and predictive/informed methods incorporate forecasts~\cite{kar2024icmab}. This distinction matters for quantum routing because benign noise, topology-dependent feedback, and adaptive disruption favor different forms of learning robustness~\cite{huang2024quantum}.
```
