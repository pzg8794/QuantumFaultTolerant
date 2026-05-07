# System Model Threat Taxonomy Reduction Audit

This document records the accepted reduction for the System Model mini-section `Adversarial Threat Taxonomy`.

## Process requirements applied

The mini-section was treated as its own section. Each idea was checked against completed sections: Abstract, Introduction, Background, Related Work, and the already-staged System Model opening/topology/reward content.

ICNP constraints were checked explicitly: page pressure, formal clarity, blind-submission hygiene, figure/table usefulness, and whether repeated ideas should become cross-references instead of deletions.

## Table decision

A compact table was considered for the five regimes, but rejected. In IEEE two-column format, a table would likely cost more vertical space because of the caption, rules, row padding, and float spacing. Since this mini-section only needs to define how the availability vector behaves under five regimes, compact prose is cleaner and more space-efficient.

## Mini-section role

The threat taxonomy should define how the availability vector from the reward model evolves across regimes. It should not re-teach adversarial bandits or repeat the general motivation already covered by Background and Related Work.

## Split-level decisions

### Split 1: Five-regime scope

The original text introduced five escalating regimes: no-disruption operation, independent stochastic failures, temporally correlated disruption, targeted failures, and adaptive adversarial interference.

- **Overlap:** medium with Abstract, Introduction, Background, and Related Work; high with the Reward Model, which introduces $A_t(r)$ and says the threat taxonomy specifies its evolution.
- **Decision:** keep and connect directly to the Reward Model.

Accepted reduction:

```tex
We evaluate five threat regimes that specify the availability vector $\mathbf{A}_t$ introduced in \cref{subsec:reward}.
```

### Split 2: Regime-selection rationale

Dan's feedback asked why these regimes were selected and requested clearer rationale/citation support. The previous wording said only that the regimes form a controlled escalation, which is correct but can still look under-motivated.

- **Overlap:** medium with earlier motivation, but the rationale is useful here to prevent the taxonomy from looking arbitrary.
- **Decision:** keep the rationale, but make it shorter than the earlier proposed wording and remove the phrase "rather than to exhaustively model every quantum-network failure mode" because it reads defensive and costs space.

Accepted reduction:

```tex
They isolate distinct routing difficulties: Baseline separates routing and allocation from path unavailability; Stochastic captures independent random failures; Markov captures temporally correlated outages; Targeted tests fixed or localized disruption; and Adaptive/OnlineAdaptive test whether policies remain stable when disruption responds to recent or current routing behavior~\cite{auer2002nonstochastic,bubeck2012regret,lattimore2020bandit}.
```

### Split 3: Escalation and attribution rationale

The original text explained that the regimes form a controlled escalation from normal operation to structured and strategic disruption.

- **Overlap:** medium with earlier motivation.
- **Feedback check:** Devroop's Item 045 flagged the word `benign` because Baseline already names the no-disruption condition. Using both `Baseline` and `benign` locally can make readers wonder whether `benign` is a separate regime or a synonym.
- **Decision:** keep one compact sentence tying the escalation to attribution under matched evaluation conditions, but use `no-disruption operation` instead of `benign operation` so Baseline remains the only local term for the no-attack regime.

Accepted reduction:

```tex
Together, they form a controlled escalation from no-disruption operation to structured and reactive disruption, helping attribute robustness differences to the policy--allocator--capacity interaction.
```

### Split 4: Concrete regime semantics

The original text used longer prose to explain how each regime affects availability.

- **Overlap:** low for the formal semantics, high for extended motivation.
- **Decision:** keep as one compact prose sentence instead of a table.

Accepted reduction:

```tex
Concretely, Baseline keeps all paths available; Stochastic independently disrupts paths with fixed probability; Markov introduces temporally correlated on/off availability; Targeted disrupts selected paths according to fixed attack preference; Adaptive reacts to recent routing behavior; and OnlineAdaptive updates disruptions online in response to current routing behavior.
```

## Accepted reduced mini-section

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We evaluate five threat regimes that specify the availability vector $\mathbf{A}_t$ introduced in \cref{subsec:reward}. They isolate distinct routing difficulties: Baseline separates routing and allocation from path unavailability; Stochastic captures independent random failures; Markov captures temporally correlated outages; Targeted tests fixed or localized disruption; and Adaptive/OnlineAdaptive test whether policies remain stable when disruption responds to recent or current routing behavior~\cite{auer2002nonstochastic,bubeck2012regret,lattimore2020bandit}. Together, they form a controlled escalation from no-disruption operation to structured and reactive disruption, helping attribute robustness differences to the policy--allocator--capacity interaction.

Concretely, Baseline keeps all paths available; Stochastic independently disrupts paths with fixed probability; Markov introduces temporally correlated on/off availability; Targeted disrupts selected paths according to fixed attack preference; Adaptive reacts to recent routing behavior; and OnlineAdaptive updates disruptions online in response to current routing behavior.
```

## Feedback-marker requirement

If the original source contains Dan's feedback marker:

```tex
\dan{Why were these regimes selected? Give a rationale, citations etc...}
```

keep the marker during the working-review pass and place the following traceability marker next to it:

```tex
% SOLVED: Added a compact regime-selection rationale that maps each threat class to the routing difficulty it isolates, with adversarial-bandit citations supporting adaptive/reactive disruption.
```

If the original source contains Devroop's Item 045 marker:

```tex
\devroop{choose a different word since you have mentioned benign in the basline}
```

keep the marker during the working-review pass and place the following traceability marker next to it:

```tex
% SOLVED: Replaced "benign operation" with "no-disruption operation" so Baseline remains the only local term for the no-attack regime.
```

## Status

Accepted by audit discussion. The intended staging point is immediately after `Reward Model and Link Success` in `ICNP_2026_venue_draft.tex`.
