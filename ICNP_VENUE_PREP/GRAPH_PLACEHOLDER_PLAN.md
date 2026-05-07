# ICNP Graph Placeholder Plan

This note records the staged placeholder plan for reserving realistic graph space before final graph polishing.

## Current graph status

Final graph creation and final graph replacement are blocked until Piter decides which graph forms to use. Placeholder insertion and text-space preparation may continue.

Blocked item:

```text
H / Blocked -- Create or replace final result graphs
Reason: Piter is deciding which graph forms to use first.
```

Blocked final graph choices include:

```text
capacity paradox graph
robustness floor graph
main performance summary graph
deployment guidance graph
cross-testbed confirmation graph
```

## Inserted placeholders

The following actual LaTeX placeholder figure blocks are inserted into the active compiled ICNP path.

| Placeholder | Label | File | Placement |
|---|---|---|---|
| Framework / evaluation pipeline | `fig:framework` | `ICNP_2026_venue_draft.tex` | Already present as the real framework figure in the Introduction |
| Main performance summary | `fig:main_performance_summary_placeholder` | `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex` | RQ1, after the evidence-slice paragraph and before the RQ1 table |
| Robustness floor | `fig:robustness_floor_placeholder` | `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex` | RQ2, after the evidence-slice paragraph and before the RQ2 table |
| Capacity paradox | `fig:capacity_paradox_placeholder` | `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex` | RQ3b, after the replay-scaling setup and before the RQ3b table |
| Deployment guidance | `fig:deployment_guidance_placeholder` | `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex` | RQ3d, after the deployment-rules setup and before the RQ3d table |
| Optional cross-testbed confirmation | `fig:cross_testbed_confirmation_placeholder` | `ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED.tex` | Cross-Testbed Validation, immediately after the subsection heading and before the first cross-testbed table |

## Candidate graph set

The graph set should strengthen the paper's central claims without turning the venue draft into a figure dump:

1. Framework / evaluation pipeline -- already represented by `fig:framework` in the Introduction
2. Main performance summary -- placeholder inserted
3. Robustness floor -- placeholder inserted
4. Capacity paradox -- placeholder inserted
5. Deployment guidance -- placeholder inserted
6. Optional cross-testbed confirmation -- placeholder inserted

## Rationale

The placeholders reserve realistic page space before final graph generation. They allow the team to judge page pressure and decide which final graphs are worth keeping without pretending the final graph design has been chosen.

## Status

Placeholder insertion is complete for the currently discussed graph set. Final graph creation/replacement remains blocked until graph forms are selected.
