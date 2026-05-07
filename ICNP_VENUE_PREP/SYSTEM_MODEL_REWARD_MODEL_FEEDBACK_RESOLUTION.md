# System Model Reward Model Feedback Resolution

This note records how we resolved the reviewer feedback attached to the reward-model subsection, especially the inline request:

```tex
\devroop{Define $p_\ell$}
```

## Problem identified

The feedback pointed to a real formal-clarity issue in the original `main.tex` reward model. The draft introduced the equation

```tex
p_\ell(x_\ell) = 1 - (1 - p_e^{(\ell)})^{x_\ell}
```

but did not clearly define `p_\ell(x_\ell)` before using it. The same subsection also reused `h_r` in two incompatible ways:

1. `h_r` meant the hop count of path `P_r`.
2. `h_r(\mathbf{x})` was later used as the path-level success probability.

That overload makes the reward model harder to read and risks confusing hop count with success probability.

## Solution

The accepted solution is to separate the link, path, and reward quantities cleanly:

- Keep `p_e^{(\ell)}` as the per-attempt entanglement success probability of link `\ell`.
- Define `p_\ell(x_\ell)` as the link-level success probability after allocating `x_\ell` qubits/attempts to link `\ell` during one frame.
- Keep `h_r` only as the hop count of path `P_r`.
- Introduce `q_r(\mathbf{x})` as the path-level success probability under allocation `\mathbf{x}`.
- Use `q_r(\mathbf{x})A_t(r)` inside the Bernoulli reward model.

The corrected equations are:

```tex
p_\ell(x_\ell)=1-(1-p_e^{(\ell)})^{x_\ell}.
```

```tex
q_r(\mathbf{x})=\prod_{\ell=1}^{h_r}p_\ell(x_\ell).
```

```tex
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
```

## Why this resolves the feedback

The feedback asked us to define `p_\ell`. The revised prose defines it before the equation as the link-level success probability induced by allocating `x_\ell` attempts/qubits to link `\ell` during a decision frame.

The notation cleanup also fixes the adjacent issue discovered while solving the feedback: `h_r` should not mean both hop count and path success. The path-success term is now `q_r(\mathbf{x})`, which keeps the System Model internally consistent.

## Manuscript application status

The corrected reward-model text is already present in `ICNP_2026_venue_draft.tex` under:

```tex
\subsection{Reward Model and Link Success}
```

That venue draft defines `p_\ell(x_\ell)`, uses `q_r(\mathbf{x})` for path success, and updates the Bernoulli reward equation accordingly.

The older `main.tex` subsection still contains the original inline feedback marker. We should sync `main.tex` in a separate safe manuscript-sync pass because the current GitHub connector only supports whole-file replacement, and `main.tex` is large enough that the fetched payload is truncated in this environment. The source of truth for the ICNP reduction remains the venue draft and the audit notes under `ICNP_VENUE_PREP/`.

## Validation checklist

- [x] `p_\ell(x_\ell)` is defined before use in the ICNP venue draft.
- [x] `h_r` remains reserved for hop count.
- [x] `q_r(\mathbf{x})` is used for path-level success probability.
- [x] The Bernoulli reward model uses `q_r(\mathbf{x})A_t(r)`.
- [x] The reasoning is recorded in the ICNP venue-preparation directory.
