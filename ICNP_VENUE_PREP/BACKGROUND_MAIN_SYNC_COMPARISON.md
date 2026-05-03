# Background Section Sync Comparison

This note documents the comparison between the full Background section in `main.tex` and the reduced Background section staged in `ICNP_2026_venue_draft.tex`.

## Source sections compared

- `main.tex`: full manuscript Background section with four subsections.
- `ICNP_2026_venue_draft.tex`: accepted ICNP Background section with the subsection titles removed and the accepted reductions collapsed into four compact paragraphs.

## Structural change

`main.tex` currently uses:

```tex
\section{Background}
\label{sec:Background}

\subsection{Quantum Networks and Entanglement Routing}
...
\subsection{The Multi-Armed Bandit Abstraction}
...
\subsection{Allocation and Capacity Semantics}
...
\subsection{Problem Scope}
...
```

The ICNP draft uses:

```tex
\section{Background}
\label{sec:Background}

<compact paragraph on quantum networks and routing>

<compact paragraph on bandit taxonomy>

<compact paragraph on allocation and capacity semantics>

<compact paragraph on problem scope>
```

## Main reductions

1. Removed four subsection headings from the rendered ICNP draft to save vertical space.
2. Reduced the quantum-network explanation from multiple explanatory paragraphs to one compact paragraph.
3. Removed tutorial-style detail on teleportation and entanglement swapping while retaining citations.
4. Collapsed the MAB taxonomy from a paragraph plus bullet list into one paragraph.
5. Reduced allocator/capacity semantics from two paragraphs to one paragraph.
6. Reduced Problem Scope to a single crisp thesis sentence.
7. Preserved the conceptual chain: quantum routing uncertainty, bandit abstraction, allocator/capacity coupling, and robustness as a joint model--allocator--capacity--threat property.

## Accepted ICNP Background text

```tex
\section{Background}
\label{sec:Background}

Quantum networks distribute entanglement across repeaters and end-nodes to support long-distance quantum communication, distributed quantum computing, and sensing~\cite{wehner2018quantum,kimble2008quantum}. Unlike classical packet routing, quantum routing must operate with fragile states, probabilistic entanglement generation and swapping, decoherence, and fidelity loss~\cite{briegel1998quantum,dahlberg2021netsquid,bennett1993teleporting,zukowski1993event}. Across multi-hop paths, these effects make routing a repeated decision problem under uncertainty, where path choices must adapt to noisy outcomes and changing link conditions. Prior routing approaches often assume stable topology knowledge or fixed allocation rules, assumptions that weaken under online learning, demand variability, and disruptive or strategic interference~\cite{li2025multipath,wang2025learning,huang2024quantum}.

A multi-armed bandit (MAB) models online routing as repeated action selection under partial feedback, where a learner chooses candidate paths or allocation actions and updates from reward signals such as entanglement success or routing efficiency~\cite{lattimore2020bandit,bubeck2012regret}. We use this taxonomy to distinguish the routing assumptions made by each model family: stochastic methods assume stable rewards~\cite{auer2002finite}, contextual and neural methods exploit predictive side information or nonlinear reward structure~\cite{chu2011contextual,zhou2020neuralucb}, adversarial methods handle non-stationary or strategic rewards~\cite{auer2002nonstochastic}, and predictive/informed methods incorporate forecasts~\cite{kar2024icmab}. This distinction matters for quantum routing because benign noise, topology-dependent feedback, and adaptive disruption favor different forms of learning robustness~\cite{huang2024quantum}.

Quantum routing couples path choice with resource allocation: the learner must decide both which route to use and how many qubits or attempts to assign within each decision epoch. These allocator choices shape the feedback observed by the bandit learner and the predictability of routing behavior under disruption. Replay or capacity semantics, including bounded histories, windowed updates, and capped experience buffers, further affect stability under nonstationarity and vulnerability to adaptive attacks. We therefore evaluate routing policies jointly with allocator strategy and capacity semantics, rather than treating them as independent implementation details.

We study routing robustness as a joint function of learning model, allocator design, replay-capacity configuration, and threat regime, rather than as a property of the bandit policy alone.
```

## Intended main.tex sync

The accepted ICNP Background text above should replace the rendered `main.tex` Background section from `\section{Background}` through the line immediately before `\section{System Model}`. Historical commented-out planning material may be removed or left commented depending on cleanup policy, but it should not render in the submission draft.

## Status

- Accepted and staged in `ICNP_2026_venue_draft.tex`.
- Documented in `ICNP_VENUE_PREP/BACKGROUND_REDUCTION_AUDIT.md`.
- This comparison note records the intended `main.tex` sync target.
