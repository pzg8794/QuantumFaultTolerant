# System Model MAB Formulation Reduction Audit

This document records the accepted reduction for the System Model mini-section `Multi-Armed Bandit Formulation`.

## Process requirements applied

The mini-section was treated as its own section. Each idea was checked against completed sections: Abstract, Introduction, Background, Related Work, and the already-staged System Model opening/topology/reward/threat taxonomy content.

ICNP constraints were checked explicitly: page pressure, formal clarity, blind-submission hygiene, figure/table usefulness, and whether repeated ideas should become cross-references instead of deletions.

## Mini-section role

The MAB formulation should bind the already-defined topology, allocation space, reward, and threat availability process into a compact decision interface. It should not re-teach bandits because Background and Related Work already explain the model families and regret regimes.

## Split-level decisions

### Paragraph 1: Action space and decision loop

- **Bandit action definition:** medium/high overlap with Abstract, Introduction, Background, and the staged System Model opening. Kept as a formal connective sentence that uses the prior topology and reward definitions.
- **Action-space equation:** kept. This is core formal content.
- **Per-frame selection and feedback:** kept and connected to the reward model through `\cref{subsec:reward}`.

Accepted paragraph:

```tex
\smallTitle{Joint action space}
Using the topology and reward definitions above, each bandit action is a joint routing-allocation pair:
\[
\mathcal{A}=\{(r,\mathbf{x}) : P_r\in\mathcal{P},\ \mathbf{x}\in\mathcal{X}_r\}.
\]
At frame $t$, the policy selects $a_t=(r_t,\mathbf{x}_t)\in\mathcal{A}$ and observes only the realized reward $Y_t(r_t,\mathbf{x}_t)$ from \cref{subsec:reward}.
```

### Paragraph 2: Policy families under the same interface

- **Common interface:** high overlap with Abstract, Introduction, Background, and Related Work. Converted into a cross-reference to the already-audited taxonomy rather than repeated.
- **Contextual input:** kept because it explains what context means in this formal system.
- **Non-contextual/adversarial/predictive variants:** kept compactly, explaining that all variants consume the same stream but differ in scoring/exploration/update rules.

Accepted paragraph:

```tex
\smallTitle{Policy interface}
This interface instantiates the policy-family taxonomy introduced in \cref{sec:Background,sec:RelatedWork}: algorithms differ in how they estimate or sample action value, not in the underlying routing task. For contextual or neural policies, the context vector is derived from path identity, hop count, allocation vector, recent reward history, and threat/availability state when available. Non-contextual, adversarial, predictive, and hybrid variants consume the same action/reward stream but apply different scoring, exploration, or update rules.
```

### Paragraph 3: Objective

- **Objective:** kept. It defines the common empirical optimization target.
- **Evaluation caveat:** high overlap with Related Work, where the paper already says it does not derive new regret guarantees. Kept as a short boundary statement to avoid reviewers expecting a new regret theorem from this section.

Accepted paragraph:

```tex
\smallTitle{Objective}
The learner seeks to maximize cumulative expected success,
\[
\max_{\pi}\ \mathbb{E}_{\pi}\!\left[\sum_{t=1}^{T}Y_t(r_t,\mathbf{x}_t)\right],
\]
under the threat process and allocator semantics fixed for that evaluation run. We use this objective as the common empirical decision interface; regret analysis is not the contribution of this work.
```

## Accepted reduced mini-section

```tex
\subsection{Multi-Armed Bandit Formulation}
\label{subsec:mab}

\smallTitle{Joint action space}
Using the topology and reward definitions above, each bandit action is a joint routing-allocation pair:
\[
\mathcal{A}=\{(r,\mathbf{x}) : P_r\in\mathcal{P},\ \mathbf{x}\in\mathcal{X}_r\}.
\]
At frame $t$, the policy selects $a_t=(r_t,\mathbf{x}_t)\in\mathcal{A}$ and observes only the realized reward $Y_t(r_t,\mathbf{x}_t)$ from \cref{subsec:reward}.

\smallTitle{Policy interface}
This interface instantiates the policy-family taxonomy introduced in \cref{sec:Background,sec:RelatedWork}: algorithms differ in how they estimate or sample action value, not in the underlying routing task. For contextual or neural policies, the context vector is derived from path identity, hop count, allocation vector, recent reward history, and threat/availability state when available. Non-contextual, adversarial, predictive, and hybrid variants consume the same action/reward stream but apply different scoring, exploration, or update rules.

\smallTitle{Objective}
The learner seeks to maximize cumulative expected success,
\[
\max_{\pi}\ \mathbb{E}_{\pi}\!\left[\sum_{t=1}^{T}Y_t(r_t,\mathbf{x}_t)\right],
\]
under the threat process and allocator semantics fixed for that evaluation run. We use this objective as the common empirical decision interface; regret analysis is not the contribution of this work.
```

## Status

Accepted by audit discussion. The intended staging point is immediately after `Adversarial Threat Taxonomy` in `ICNP_2026_venue_draft.tex`.
