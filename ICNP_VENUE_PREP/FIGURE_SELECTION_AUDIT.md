# ICNP Figure Selection Audit

This note documents the figure-selection pass that replaced temporary PGFPlots placeholders with exported notebook-validated images from:

```text
figures/icnp/
```

The exported images are generated from the verification workflow connected to:

```text
https://github.com/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb
```

and validated against the master-dataset logs in:

```text
https://github.com/pzg8794/GA-Work/tree/main/Validated_Logs
```

## Selection rule

Main paper figures should carry one central claim each. Appendix figures should preserve denser synthesis, diagnostics, and supporting evidence without interrupting the Results narrative.

Figures marked as convergence/regret/TBD in the verification workflow are excluded from the main paper until they are explicitly accepted as source-backed manuscript evidence.

## May 21 image regeneration note

The May 21 image-first cleanup regenerated the manuscript-facing PNGs from the existing source scripts rather than manual PNG edits. The active generators are:

```text
figures/icnp-exported-assets/build_G8_G9.py
figures/icnp_figures/icnp_graphs.py
figures/icnp_graphs/code_and_plots/script.py
```

The pass preserved active figure filenames, improved label visibility, replaced `Paper N` style testbed labels with author/testbed labels, made captioned values visible in the plots, and replaced the duplicate cross-testbed panel in the grouped appendix synthesis with a context-capacity panel.

## Main-body selections

| Claim slot | Selected image | Paper placement | Rationale |
|---|---|---|---|
| Main performance summary | `figures/icnp/ICNP-CODE-033_g9_network_gap_analysis_panel_d_rq1_algorithm_tier_separation_stochastic.png` | RQ1 | Shows algorithm-tier separation under stochastic decoherence, matching the RQ1 claim. |
| Robustness floor | `figures/icnp/ICNP-CODE-040_g2_robustness_floor.png` | RQ2 | Directly supports worst-case floor and robustness-under-threat claims. |
| Capacity paradox | `figures/icnp/ICNP-CODE-039_g1_capacity_paradox.png` | RQ3b | Gives the cleanest main-body visual for replay-capacity paradox behavior. |
| Deployment guidance | `figures/icnp/ICNP-CODE-042_g4_deployment_rules.png` | RQ3d | Matches scenario-to-configuration deployment guidance. |
| Cross-testbed confirmation | `figures/icnp/ICNP-CODE-038_g9_network_gap_analysis_panel_i_cross_testbed_efficiency_oracle_gap_std.png` | Cross-Testbed Validation | Confirms cross-testbed efficiency/gap trends in a compact one-column figure. |

## Appendix selections

### Second-checkpoint claim support

These figures were added after checking the second-checkpoint archive for appendix-worthy support that strengthens the paper's main claims without bloating the main body.

| Appendix image | Rationale |
|---|---|
| `figures/icnp/ICNP-CODE-032_g9_network_gap_analysis_panel_c_oracle_gap_context_vs_exp3_by_scenario_c.png` | Supports the contextual-versus-EXP3 robustness contrast under matched threat/capacity variation. |
| `figures/icnp/ICNP-CODE-053_fig6_context_capacity.png` | Retained standalone context-capacity evidence after the duplicate grouped Panel D was replaced; regenerated with the same Matplotlib style as the former grouped panel. |
| `figures/icnp/ICNP-CODE-056_fig10_threat_rules.png` | Supports scenario-conditioned deployment guidance and threat-rule interpretation. |

### Grouped synthesis and diagnostics

| Appendix image | Rationale |
|---|---|
| `figures/icnp/ICNP-CODE-024_g8_advanced_4panel_grouped_full_figure.png` | Dense synthesis of oracle gaps, capacity effects, allocator efficiency, and replay-configuration sensitivity. |
| `figures/icnp/ICNP-CODE-029_g9_network_gap_analysis_grouped_full_figure.png` | Broad diagnostic suite for path/fidelity, allocator budgets, threat escalation, capacity sensitivity, scenario penalties, allocator risk, and cross-testbed behavior. |
| `figures/icnp/ICNP-CODE-035_g9_network_gap_analysis_panel_f_capacity_paradox_all_6_replay_configs_sc.png` | Source panel folded into grouped synthesis Panel D rather than kept as a standalone appendix duplicate. |
| `figures/icnp/ICNP-CODE-036_g9_network_gap_analysis_panel_g_scenario_penalty_vs_baseline_by_algorith.png` | Detailed support for threat penalty and robustness-floor analysis. |
| `figures/icnp/ICNP-CODE-037_g9_network_gap_analysis_panel_h_allocator_risk_floor_mean_peak_icpursuit.png` | Detailed support for allocator risk and deployment guidance. |
| `figures/icnp/ICNP-CODE-034_g9_network_gap_analysis_panel_e_threat_escalation_heatmap_algo_scenario.png` | Diagnostic heatmap behind threat-escalation claims. |

## Appendix presentation cleanup

The appendix is organized as follows:

```text
Detailed Cross-Testbed and Model-Family Results
  - Full Cross-Testbed Results
  - Full Model-Family Results
Additional Diagnostic Figures
  - Second-Checkpoint Claim Support
  - Grouped Synthesis Diagnostics
```

The full result tables were reformatted with fixed-width columns, tighter spacing, concise testbed descriptors, and takeaway rows to prevent overflow and make the appendix presentable under IEEE layout.

The standalone replay-sensitivity line plot was consolidated on May 22: the grouped synthesis Panel D now carries the replay-configuration sensitivity view, while the standalone Context-Capacity Interaction figure remains as the kept context-capacity evidence.

The appendix support figure was expanded on May 23 to make the capacity-paradox evidence chain more complete. The retained support figure now includes the actual `G13 Capacity Paradox` asset (`ICNP-CODE-008`), `G14 Regret Trajectory` (`ICNP-CODE-009`), and the paired replay-scaling delta panel (`ICNP-CODE-047`). The manifest currently maps `ICNP-CODE-057` to a convergence image, so it remains excluded unless explicitly selected as a convergence diagnostic.

## Excluded from main paper for now

The following figure families are intentionally excluded from the main paper until explicitly accepted as final source-backed evidence:

```text
convergence figures
other regret trajectories not selected for the active appendix figure
figures marked TBD/deferred in the verification workflow
```

Examples include:

```text
ICNP-CODE-043_g5_convergence.png
ICNP-CODE-057_fig13_convergence.png
ICNP-CODE-023_g14_regret.png
```

## Applied code changes

Main-body temporary figure inputs were replaced in:

```text
ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex
ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED.tex
```

Appendix diagnostics are in:

```text
ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex
```

Detailed appendix tables are in:

```text
ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex
```

Both appendix files are included from:

```text
ICNP_2026_venue_draft.tex
```

## Current caveat

This pass is meant to test readability and page flow. If page pressure becomes severe, appendix diagnostics should be the first removable items; main-body claim figures should be kept unless they duplicate a stronger table or final graph selected later.
