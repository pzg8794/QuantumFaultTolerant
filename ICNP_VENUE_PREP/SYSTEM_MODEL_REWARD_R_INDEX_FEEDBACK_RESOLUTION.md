# System Model Reward Index Feedback Resolution

This note records the original narrow resolution for the reviewer feedback:

```tex
\devroop{define r}
```

## Superseded by broader notation fix

This narrow reward-index note has been superseded by the broader path-index convention note:

```text
ICNP_VENUE_PREP/SYSTEM_MODEL_PATH_INDEX_NOTATION_RESOLUTION.md
```

The broader task resolves route-index consistency across the System Model for:

```tex
r,
r',
P_r,
A_t(r),
q_r(\mathbf{x})
```

and preserves the relevant feedback markers as LaTeX source comments with nearby `SOLVED` explanations.

## Current accepted convention

The ICNP venue draft now defines the convention once in the topology/path notation paragraph:

```tex
We use $r \in \{1,\ldots,|\mathcal{P}|\}$ to index candidate paths, where $P_r$ denotes the $r$th path in $\mathcal{P}$. When needed, $r'$ denotes a dummy path index used for summations or comparisons over $\mathcal{P}$.
% \devroop{define r} -- SOLVED: Defined $r$ in the topology/path notation as the candidate-path index, with $P_r$ denoting the selected path.
```

## Status

Historical note retained for traceability. Use `SYSTEM_MODEL_PATH_INDEX_NOTATION_RESOLUTION.md` as the authoritative documentation for this notation-family fix.
