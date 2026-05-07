# Results Table Relocation Plan

This note records the pass that moved oversized Results tables out of the main flow while preserving the claims and audit trail.

## Scope

The oversized cross-testbed and model-family tables were removed from the main Cross-Testbed Validation subsection and moved to an appendix.

Original body labels were replaced by appendix labels:

```tex
\label{tab:testbed_comparison_full}
\label{tab:model_family_comparison_full}
```

## Main-body replacements

The Results body now keeps concise claim-supporting tables:

```tex
\label{tab:testbed_comparison_summary}
\label{tab:model_family_comparison_summary}
```

These summary tables preserve the claims needed in the paper body:

- iCPursuitNeuralUCB is the strongest average cross-testbed performer.
- Dense/topology-dependent settings can change win structure.
- PaperTwelve shows the topology-complexity penalty.
- PaperEight shows that average efficiency and per-configuration win dominance can diverge.
- Hybrid pursuit--neural policies define the overall performance ceiling.

## Appendix location

The full tables now live in:

```tex
ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex
```

and are included after the conclusion via:

```tex
\appendices
\input{ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES}
```

## Validation checklist

- [x] Main Results flow keeps concise evidence only.
- [x] Full detailed tables are preserved in an appendix instead of deleted.
- [x] Main-body claims reference nearby summary tables.
- [x] Summary tables reference the full appendix tables.
- [x] Cross-testbed graph placeholder remains in the main Results flow.
- [x] Appendix labels are distinct from main-body summary labels.
