# ICNP Graph Placeholder Plan

This note records the staged placeholder plan for reserving realistic graph space before final graph polishing.

## Candidate graph set

The graph set should strengthen the paper's central claims without turning the venue draft into a figure dump:

1. Framework / evaluation pipeline
2. Main performance summary
3. Robustness floor
4. Capacity paradox
5. Deployment guidance
6. Optional cross-testbed confirmation

## First inserted placeholder

### Capacity paradox

Inserted in:

```tex
ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex
```

Location:

```tex
\subsection{RQ3b: Replay Capacity Scaling \& Paradox}
```

Placement decision:

The placeholder is inserted immediately after the paragraph that introduces the replay-scaling isolation setup and before the capacity-scaling table/result explanation. This reserves page space before final graph generation and lets the Results section reveal whether the paper can absorb the most important empirical figure.

Inserted label:

```tex
\label{fig:capacity_paradox_placeholder}
```

Placeholder intent:

```text
Diverging bar chart by threat scenario
Y-axis: replay-capacity effect in percentage points
Zero baseline included
Positive = added replay capacity helps
Negative = added replay capacity hurts
```

## Rationale

The capacity paradox is the most memorable RQ3 empirical claim: replay capacity is not a monotonic good. It can improve efficiency in some threat settings while reducing robustness under adaptive disruption. Reserving this space now helps evaluate final ICNP page pressure before final plot polishing.

## Next placeholder

Next recommended insertion:

```tex
\label{fig:robustness_floor_placeholder}
```

Likely location:

```tex
\subsection{RQ2: Robustness Under Adaptive Threats}
```

Candidate placement: after the RQ2 evidence-slice paragraph and before the RQ2 adversarial-scope table, unless later layout checks show it fits better after the table.

## Status

Capacity-paradox placeholder inserted into the active compiled venue path through `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`, which is included by `ICNP_2026_venue_draft.tex`.
