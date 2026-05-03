# Related Work Reduction Audit for ICNP Draft

This document records the Related Work reduction process for the ICNP venue draft.

## Venue-aware structure decision

For the ICNP draft, `Background` is placed before `Related Work`. This keeps the minimum conceptual vocabulary before the literature comparison, allowing `Related Work` to focus on prior methods, assumptions, and gaps rather than re-teaching quantum-network or bandit background.

This choice supports the venue constraints tracked in `ICNP_DRAFT_AUDIT_TODO.md`, especially the 10-page main-body target, concise presentation, and the need to keep core claims in the main body.

## Required audit method

For each Related Work paragraph:

1. identify the paragraph's role;
2. split it into conceptual pieces;
3. mark overlap with the reduced Background;
4. preserve ICNP-relevant prior-work comparison and closest-work contrast;
5. reduce each split;
6. recombine accepted reduced content;
7. document removed overlap and why it was removed.

## Opening reduction: former Literature Selection Methodology

### Original structure

The original Related Work opened with:

```tex
\subsection{Literature Selection Methodology}
```

followed by two paragraphs explaining MAB positioning, quantum-routing stress-test motivation, literature strands, review years, and inclusion criteria.

### Decision

Remove the `Literature Selection Methodology` subsection heading and replace the two original paragraphs with one compact opening paragraph.

### Removed overlap and rationale

The original opening reintroduced MABs as uncertainty-aware sequential decision rules and described quantum entanglement routing as a stress test shaped by stochastic noise, structured disruption, and resource constraints. These ideas are already covered in the reduced Background: the MAB paragraph defines bandits as repeated routing decisions under partial feedback, and the allocation/capacity plus Problem Scope paragraphs state that robustness depends jointly on learning model, allocator design, replay-capacity configuration, and threat regime.

The original second paragraph also listed inclusion criteria that duplicate the roadmap and the following subsection structure. Instead of keeping a survey-methodology paragraph, the ICNP draft preserves a shorter review-scope sentence so reviewers can see that the literature review spans quantum routing, entanglement distribution, and bandit-based online decision-making.

### Accepted reduced opening

```tex
\section{Related Work}
\label{sec:RelatedWork}

We organize prior work by the assumptions that shape routing robustness: stochastic and adversarial regret regimes, contextual and neural structure, hybrid robust designs, predictive context, and quantum-routing applications. Our targeted review spans quantum routing, entanglement distribution, and bandit-based online decision-making, emphasizing work that defines robustness assumptions, exploits structured context, adds forecasting, combines mechanisms across regimes, or adapts online decisions to resource-constrained settings. This framing lets us compare routing methods by deployment role, threat model, and resource-control assumptions rather than by algorithm family alone.
```

## Foundational Bandits and Regret Regimes

### Original role

This subsection positioned stochastic and adversarial bandits as canonical baseline families and explained why quantum-routing evaluation should distinguish natural noise from coordinated disruption.

### Split-level reduction

- **Foundational tradeoff:** reduce. Background already introduces the bandit taxonomy, so Related Work does not need a regret tutorial.
- **Stochastic baselines:** keep. UCB and Thompson sampling are important baselines and must be cited for evaluation credibility.
- **Adversarial baselines:** keep. EXP3 supports the paper's threat-regime framing.
- **Natural noise versus coordinated disruption:** merge into the baseline framing. The reduced Background already explains that benign noise and adaptive disruption favor different learning robustness assumptions.
- **Our contrast:** keep. ICNP reviewers need to know that the paper evaluates established families under matched routing conditions rather than claiming new regret theory.

### Removed overlap and rationale

The original paragraph explained the exploration--exploitation tradeoff, regret guarantees, and the distinction between stochastic and adversarial learning regimes. The reduced Background already states that stochastic methods assume stable rewards and adversarial methods handle non-stationary or strategic rewards. Therefore, the Related Work version removes tutorial-style explanation and keeps only the prior-work positioning needed to justify the baseline families.

### Accepted reduced text

```tex
\subsection{Foundational Bandits and Regret Regimes}

Foundational bandit results motivate the stochastic and adversarial baselines used in our evaluation. UCB-style optimism and Thompson-style posterior sampling provide canonical baselines under i.i.d. reward assumptions~\cite{auer2002finite,thompson1933likelihood}, while EXP3 provides an adversarial baseline without stochastic assumptions~\cite{auer2002nonstochastic}. Rather than deriving new regret guarantees, our study evaluates these families under the same quantum-routing threat taxonomy, allocator policies, and replay/capacity settings.
```

## Current staged status

- `Background` now appears before `Related Work` in `ICNP_2026_venue_draft.tex`.
- The former Literature Selection Methodology subsection is collapsed into the compact opening above.
- `Foundational Bandits and Regret Regimes` is reduced and staged.
- Remaining Related Work subsections are pending paragraph-level audit.
