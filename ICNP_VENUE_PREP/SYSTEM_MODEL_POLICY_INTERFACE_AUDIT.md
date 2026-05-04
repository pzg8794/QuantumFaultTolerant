# System Model Policy Implementation Interface Reduction Audit

This document records the accepted reduction for the System Model mini-section originally titled `Algorithmic Framework`.

## Process requirements applied

The mini-section was treated as its own section. Each paragraph was split into internal ideas, checked against completed sections (Abstract, Introduction, Background, Related Work, and the already-staged System Model mini-sections), and checked against ICNP constraints: page pressure, formal clarity, blind-submission hygiene, figure/table usefulness, notation consistency, and whether repeated ideas should become cross-references instead of deletions.

## Title decision

### Original title

```tex
\subsection{Algorithmic Framework}
```

### Accepted title

```tex
\subsection{Policy Implementation Interface}
```

### Rationale

`Algorithmic Framework` sounded too broad and could imply that the paper is centered on a single algorithmic stack. `Policy Implementation Interface` better matches the role of this System Model mini-section: to explain how the evaluated policy families instantiate the already-defined action/reward interface.

## Mini-section role

This mini-section should explain how stochastic, contextual/neural, adversarial, predictive, and hybrid policies fit into the common MAB interface from `\cref{subsec:mab}`. It should not re-teach EXP3, NeuralUCB, pursuit learning, or informed bandits, because those are already handled in Background and Related Work.

## Split-level decisions

### Paragraph 1: Shared interface and hybrid structure

- **Dual-layer/routing-stack statement:** high overlap with Abstract, Introduction, Background, Related Work, and the MAB mini-section. Reduced into a shared-interface statement.
- **EXP3 path layer + Neural/Pursuit allocation layer:** high overlap with Related Work. Kept only as a compact description of how hybrid policies instantiate the interface.

Accepted paragraph:

```tex
The evaluated policies share the joint action/reward interface in \cref{subsec:mab} but differ in how they score paths, allocate qubits, and update from feedback. Hybrid policies instantiate this interface with a path-level selection rule, such as adversarial weighting or pursuit, and an allocation-level contextual scorer.
```

### Paragraph 2: Adversarial variants

- **Path weights/probabilities:** kept and generalized.
- **Sampling/selection from scores:** kept compactly.
- **Robustness to adversarial reward sequences:** high overlap with Background and Related Work. User requested this not be removed entirely; it is retained as a brief cross-reference connecting the algorithmic mechanism to the previously defined threat taxonomy.

Accepted paragraph:

```tex
Adversarial variants maintain path weights or probabilities over $r\in\{1,\ldots,R\}$, then sample or select $r_t$ from these scores before choosing an allocation. This briefly connects the update mechanism to the adversarial-feedback setting in \cref{subsec:threats}, without repeating the adversarial-bandit rationale from \cref{sec:Background,sec:RelatedWork}.
```

## Paragraph 3: Allocation-level contextual scorer

- **Allocation-level scoring:** kept because it explains implementation under the common action interface.
- **Argmax equation:** kept but updated from `\widehat{h}` to `\widehat{q}` to remain consistent with the reward-model notation, where `h_r` is hop count and `q_r(\mathbf{x})` is path success probability.

Accepted paragraph:

```tex
Given $r_t$, contextual or neural policies score feasible allocations $\mathbf{x}\in\mathcal{X}_{r_t}$ using reward estimates and uncertainty, e.g.,
\[
\mathbf{x}_t \in \arg\max_{\mathbf{x}\in\mathcal{X}_{r_t}}
\left[\widehat{q}_{r_t}(\mathbf{x})+\beta_t U_{r_t}(\mathbf{x})\right].
\]
```

## Paragraph 4: Informed variants

- **History-derived predictive context:** high overlap with Background and Related Work, but useful as a formal interface statement. Kept and connected to the context vector from the MAB mini-section.
- **Improving stability under structured/nonstationary disruption:** removed as a result-like claim; replaced with a System Model-appropriate statement that informed variants leave the environment, action space, and allocator interface unchanged.

Accepted paragraph:

```tex
Informed variants augment the context vector from \cref{subsec:mab} with history-derived predictive features while leaving the environment, action space, and allocator interface unchanged.
```

## Accepted reduced mini-section

```tex
\subsection{Policy Implementation Interface}
\label{subsec:framework}

The evaluated policies share the joint action/reward interface in \cref{subsec:mab} but differ in how they score paths, allocate qubits, and update from feedback. Hybrid policies instantiate this interface with a path-level selection rule, such as adversarial weighting or pursuit, and an allocation-level contextual scorer.

Adversarial variants maintain path weights or probabilities over $r\in\{1,\ldots,R\}$, then sample or select $r_t$ from these scores before choosing an allocation. This briefly connects the update mechanism to the adversarial-feedback setting in \cref{subsec:threats}, without repeating the adversarial-bandit rationale from \cref{sec:Background,sec:RelatedWork}.

Given $r_t$, contextual or neural policies score feasible allocations $\mathbf{x}\in\mathcal{X}_{r_t}$ using reward estimates and uncertainty, e.g.,
\[
\mathbf{x}_t \in \arg\max_{\mathbf{x}\in\mathcal{X}_{r_t}}
\left[\widehat{q}_{r_t}(\mathbf{x})+\beta_t U_{r_t}(\mathbf{x})\right].
\]

Informed variants augment the context vector from \cref{subsec:mab} with history-derived predictive features while leaving the environment, action space, and allocator interface unchanged.
```

## Status

Accepted by audit discussion. The intended staging point is immediately after `Multi-Armed Bandit Formulation` in `ICNP_2026_venue_draft.tex`.
