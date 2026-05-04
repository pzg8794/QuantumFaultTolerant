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
We evaluate five threat regimes that specify the availability vector $\mathbf{A}_t$ introduced in \cref{subsec:reward}: no disruption, independent stochastic failures, temporally correlated disruption, targeted failures, and adaptive interference.
```

### Split 2: Escalation rationale

The original text explained that the regimes form a controlled escalation from normal operation to structured and strategic disruption.

- **Overlap:** medium with earlier motivation, but the rationale is useful here to prevent the taxonomy from looking arbitrary.
- **Decision:** keep and tighten.

Accepted reduction:

```tex
Together, they form a controlled escalation from normal operation to increasingly structured and strategic path unavailability.
```

### Split 3: Adaptive/adversarial rationale

The original rationale connected adaptive regimes to adversarial-bandit settings where rewards or losses may be strategically selected.

- **Overlap:** high with Background and Related Work.
- **Decision:** convert to a cross-reference rather than repeating adversarial-bandit tutorial content.

Accepted reduction:

```tex
The adaptive regimes instantiate the adversarial-feedback setting discussed in \cref{sec:Background,sec:RelatedWork} by coupling path unavailability to routing behavior.
```

### Split 4: Concrete regime semantics

The original text used longer prose to explain how each regime affects availability.

- **Overlap:** low for the formal semantics, high for extended motivation.
- **Decision:** keep as one compact prose sentence instead of a table.

Accepted reduction:

```tex
Concretely, Baseline keeps all paths available; Stochastic independently disrupts paths with fixed probability; Markov introduces temporally correlated on/off availability; Targeted disrupts selected paths according to fixed attack preference; and OnlineAdaptive updates disruptions online in response to recent or current routing behavior.
```

## Accepted reduced mini-section

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We evaluate five threat regimes that specify the availability vector $\mathbf{A}_t$ introduced in \cref{subsec:reward}: no disruption, independent stochastic failures, temporally correlated disruption, targeted failures, and adaptive interference. Together, they form a controlled escalation from normal operation to increasingly structured and strategic path unavailability. The adaptive regimes instantiate the adversarial-feedback setting discussed in \cref{sec:Background,sec:RelatedWork} by coupling path unavailability to routing behavior.

Concretely, Baseline keeps all paths available; Stochastic independently disrupts paths with fixed probability; Markov introduces temporally correlated on/off availability; Targeted disrupts selected paths according to fixed attack preference; and OnlineAdaptive updates disruptions online in response to recent or current routing behavior.
```

## Status

Accepted by audit discussion. The intended staging point is immediately after `Reward Model and Link Success` in `ICNP_2026_venue_draft.tex`.
