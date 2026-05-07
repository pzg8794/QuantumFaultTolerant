# System Model Path-Index Notation Resolution

This note records the unified System Model notation fix for route/path index consistency.

## Correct task

Resolve route-index notation consistency across the System Model, including:

```tex
r
r'
P_r
A_t(r)
q_r(\mathbf{x})
```

and the related reviewer feedback markers:

```tex
\devroop{define r}
```

```tex
\shee{Is this supposed to be $P_r$? Define r'}
```

## Unified convention

The ICNP venue draft now defines the convention once in the topology/path notation paragraph:

```tex
We use $r \in \{1,\ldots,|\mathcal{P}|\}$ to index candidate paths, where $P_r$ denotes the $r$th path in $\mathcal{P}$. When needed, $r'$ denotes a dummy path index used for summations or comparisons over $\mathcal{P}$.
% \devroop{define r} -- SOLVED: Defined $r$ in the topology/path notation as the candidate-path index, with $P_r$ denoting the selected path.
% \shee{Is this supposed to be $P_r$? Define r'} -- SOLVED: Clarified that $r'$ is a dummy path index used in comparisons/summations over candidate paths; $P_r$ remains the selected path indexed by $r$.
```

This establishes:

- $r$ indexes candidate paths in $\mathcal{P}$.
- $P_r$ denotes the $r$th candidate path.
- When a selected path is being discussed, $P_r$ is the selected path.
- $r'$ is reserved for dummy comparison/summation indices over the same candidate path set.
- $A_t(r)$ denotes availability for path index $r$ at frame $t$.
- $q_r(\mathbf{x})$ denotes path-success probability for candidate path $P_r$ under allocation $\mathbf{x}$.

## Manuscript updates applied

### 1. Topology/path notation

The venue draft now defines $r$ and $r'$ in the Network Topology and Path Structure subsection, before the reward equation and MAB action-space equation use those symbols.

### 2. Reward equation

Because $r$ is now defined once near the path set, the reward-model sentence is shorter:

```tex
At frame $t$, selecting path $P_r$ with allocation $\mathbf{x}$ yields
\[
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
\]
```

### 3. Policy implementation notation

The adversarial-policy sentence now uses the same path-index range as the rest of the model:

```tex
Adversarial variants maintain path weights or probabilities over $r\in\{1,\ldots,|\mathcal{P}|\}$, then sample or select $r_t$ from these scores before choosing an allocation.
```

## Feedback-marker handling

The original reviewer markers are preserved as LaTeX source comments, with `SOLVED` explanations next to the global convention. They do not render in the paper body but remain traceable in the source.

Resolved markers:

- `\devroop{define r}`
- `\shee{Is this supposed to be $P_r$? Define r'}`

## Relationship to previous notes

This broader note supersedes the narrower reward-index-only note:

```text
ICNP_VENUE_PREP/SYSTEM_MODEL_REWARD_R_INDEX_FEEDBACK_RESOLUTION.md
```

The old note remains as historical process documentation, but the authoritative convention is this file.

## Validation checklist

- [x] $r$ is defined before `Y_t(r,\mathbf{x})`, `A_t(r)`, and `q_r(\mathbf{x})` are used in the reward model.
- [x] $P_r$ is explicitly tied to the candidate path indexed by $r$.
- [x] $r'$ is defined as a dummy path index for comparisons/summations.
- [x] The reward equation remains mathematically unchanged.
- [x] The adversarial-policy path-index range uses $|\mathcal{P}|$ instead of an undefined `R`.
- [x] Named feedback markers are preserved as source comments with nearby `SOLVED` explanations.
