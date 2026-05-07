# System Model Reward Index Feedback Resolution

This note records the resolution for the reviewer feedback:

```tex
\devroop{define r}
```

## Problem identified

The ICNP venue draft reward equation used

```tex
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big)
```

and referred to the selected path `P_r`, but the local reward-model paragraph did not explicitly define what the index `r` denotes at the point where the reward equation is introduced.

## Accepted solution

Define `r` immediately before the Bernoulli reward equation and preserve the original feedback marker as a LaTeX source comment with the resolution next to it:

```tex
At frame $t$, let $r \in \{1,\ldots,|\mathcal{P}|\}$ index the selected candidate path $P_r$.
Selecting path $P_r$ with allocation $\mathbf{x}$ yields
% \devroop{define r} -- SOLVED: defined $r$ as the selected candidate path index before the Bernoulli reward equation.
\[
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
\]
```

## Why this resolves the feedback

The definition is placed exactly where the reader first needs it in the reward equation. It introduces no new notation beyond the already defined path set `\mathcal{P}` and candidate paths `P_r`. It also keeps the notation consistent with the later MAB action space:

```tex
\mathcal{A}=\{(r,\mathbf{x}) : P_r\in\mathcal{P},\ \mathbf{x}\in\mathcal{X}_r\}.
```

## Manuscript application status

Applied to `ICNP_2026_venue_draft.tex` under:

```tex
\subsection{Reward Model and Link Success}
```

The feedback marker `\devroop{define r}` is retained in the ICNP venue draft as a LaTeX source comment, with a nearby `SOLVED` explanation. It is not rendered in the paper body, but remains traceable in the source.

The older `main.tex` marker may still remain until a separate safe manuscript-sync pass, because the ICNP venue draft is the active submission working draft.

## Validation checklist

- [x] `r` is defined before `Y_t(r,\mathbf{x})` is introduced.
- [x] The definition refers to the existing candidate path set `\mathcal{P}`.
- [x] The reward equation remains unchanged mathematically.
- [x] The original `\devroop{define r}` marker is preserved as a LaTeX source comment.
- [x] The source comment states what solved the feedback.
