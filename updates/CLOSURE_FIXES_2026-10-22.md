# Whole-paper corrections and Validation Hub checkpoint

## Superseding original-source verification

The later [original datalake verification](DATALAKE_ORIGINAL_SOURCE_VALIDATION_2026-10-22.md) closes the original-data availability/parity and eight-summary-label questions left open by the earlier documentary/CSV-only inspection below. All 101 primary source filenames / 81 distinct byte groups are checksum-verified and strictly loaded; 10240 rows / 296960 field comparisons reproduce without mismatch. The summary difference is modal experiment-winner frequency versus mean efficiency, not a numerical error. All 27 validator tests pass. Earlier outputs remain preserved as historical evidence; no manuscript edit, new experiment, or Q07 rerun occurred during this verification.

## Scope and status

**Later October 22 source-method corrections:** The existing Validation Hub now uses the shared `StateReporting.build_source_master_dataset` contract to preserve and inspect the four original CSV exports in memory. The shared implementation is reused unchanged and its five relevant source files are hash-identified in the executed notebook output. Experimental accounting is reconciled; statistical reporting now describes the actual descriptive outputs. Historical reproducibility is partially resolved by the documentary evidence below, not declared fully certified. Rounding differences alone are not scientific closure blockers.

[Current methods evidence in the existing project Drive mirror](https://drive.google.com/drive/folders/1hzkGPv9cYXUoCAE8n-FoLNFBIQZNPkhi) includes the executed Validation Hub, source/check identities, tests, exact diff and build. The [established Colab notebook](https://colab.research.google.com/github/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb) receives these updates through its normal Git branch. Historical snapshots below remain preserved.

| Export | All model rows | Non-Oracle rows | Oracle rows / source-scoped groups |
|---|---:|---:|---:|
| Hybrid | 4920 | 3936 | 984 |
| CMABs | 1200 | 1000 | 200 |
| iCMABs | 2580 | 2150 | 430 |
| EXP3 | 1540 | 1155 | 385 |
| Total | 10240 | 8241 | 1999 |

All 1999 experiment winner labels agree with non-Oracle reward maxima; no exact reward ties occur. Fifteen unique learned-policy labels occur across the suites. These exported observations are not an independent sample-size count. The contribution and methods now state their units; 552 configurations / 5520 episodes / 380 GPU-hours are no longer presented as executed scope. Source comparisons retain every row and all original CSV text; no data are rewritten or silently deduplicated.

The inspected GA notebook/source/output chain did not establish an executed 10000-resample bootstrap or its sampling unit. Accordingly, that inference claim is removed rather than fabricated. The methods specify descriptive summaries, output-specific CV units, reward-max experiment winners, mean-efficiency evaluator leaders, first-encounter exact ties and the RQ2 displayed-representative win denominator of 82. The accepted medium three-block ranges remain descriptive. Eight Hybrid source/scenario summaries disagree with recomputed mean-efficiency leaders; their exact identities and values are retained in the Validation Hub output. Historical saved winner labels are not silently replaced with current-rule recomputations.

Validation of this later pass: **17/17 tests passed, zero skips**. The independent reviewer reproduced the counts, found an unconditional-PASS defect and contradictory earlier S/CV definitions, then accepted the corrected implementation after rerunning all 17 tests. The semantic negative fixture updates its own input hash and still rejects an invalid winner. The source contract checks raw-text/row conservation and source hashes. Final build: **28 pages, zero undefined references/citations, zero overfull boxes**, with three pre-existing font-substitution warnings. Methods page 6 and context/settings tables on page 28 were visually checked. The added documentary context rows and explicit methods increase the previous 27-page build by one page; the venue-length task remains open. This is bounded methods/accounting review, not final whole-paper acceptance.

Owner-authorized corrections to the October 22 audit, followed by explicit validation of the existing validator. This is **PASS WITH EXPLICIT HOLDS**, not closure of every reviewer item, independent approval of new wording, or submission readiness. Q07/F10 existing-trace diagnosis remains accepted and closed; historical 100-node causality remains unresolved.

The canonical job/evidence record remains the existing `H-MABs_MasterDataset_VerificationHub.ipynb` in `pzg8794/quantum_project`, branch `codex/mq-q04-notebook-execution`. Its final October 22 cells contain executed reconciliation and validator-test outputs. This checkpoint was executed locally, **not in hosted Colab**, and did not execute the historical notebook wholesale.

- [Exact Validation Hub checkpoint in Colab](https://colab.research.google.com/github/pzg8794/quantum_project/blob/9e82d0e1aa42dc607b32052de14e2919017a15a9/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb).
- [Notebook, helper and regression tests at the pushed framework commit](https://github.com/pzg8794/quantum_project/tree/9e82d0e1aa42dc607b32052de14e2919017a15a9/Dynamic_Routing_Eval_Framework/notebooks).
- Validated manuscript source commit: `21ee41bdbdce2f21e13ff4b333340087fb3a2dac`; scientific corrections began at `8bd0214d39449c03c23eb3e857e00148197db998`.
- [Existing project Drive mirror](https://drive.google.com/drive/folders/1B3mo02ruJgq0TQbPH2oaD_gWAWpI5gxr), containing the supporting evidence in the established campaign infrastructure.

The validated notebook and its two support files have also been applied to the established framework `main` (`0712f941`) and `gcp-main` (`40590e47`) branches. Both copies match the validated `9e82d0e1` files byte-for-byte; all 13 regression tests passed on each destination. The existing `gcp-main` Colab link therefore receives these corrections. No unrelated framework branch changes were promoted and the original dirty framework checkout was preserved.

The manuscript changes are promoted to GitHub `main` through a normal fast-forward push, preserving all existing history, including the prior Overleaf update. GitHub is the source for Piter's normal Overleaf pull; that user-operated pull is not a separate engineering blocker. This record does not claim that the Overleaf editor has already pulled. The Drive location above is the existing project mirror, not a new storage system or additional completion gate.

## Changes and evidence

| Audit item | Implemented correction | Evidence and remaining boundary |
|---|---|---|
| RQ3 baseline/switching | State the three-run baseline separately from pooled 3/5-run allocator summaries; correct Adaptive configuration to ThompsonSampling + T, s=1; replace inconsistent switching raster with source-backed vector plot | Existing March 15 snapshots give mean 96.0374395%, floor 92.7832598%; Hybrid master uniquely verifies Adaptive 95.691752%. No new result generation. Selected snapshot efficiencies have three decimals; displayed gains retain one-decimal precision. |
| External aggregation/scope | Distinguish average saved per-configuration percentages from ratio of aggregate rewards; identify Default-only native family slices and mixed reward units | Four native CSVs and existing table-builder semantics. Exact historical source-revision/rounding parity remains open; do not silently replace all old numerical cells. |
| Feedback contract | Replace the universal Bernoulli-only observation assertion with model-specific feedback and an explicit medium appendix reference | Bernoulli success model is not a universal learning target; continuous allocation feedback remains distinct from sampled route feedback. |
| Claim calibration | Remove flagged causal feature/topology/interaction interpretations and an unsupported already-existing switching-controller assertion; correct Stochastic/decoherence and G/EXP-family labels | Conditioned comparisons remain descriptive; validated numerical findings and Q07 limits are preserved. |
| Historical settings | Identify historical predictive warmup, allocator settings and bootstrap/output mapping as pending rather than asserting unverified values | No current-code default is substituted for historical data-producing settings. |
| Readability | RQs ask questions without duplicating result answers; remove two unnecessary forced page breaks | Retain the algorithm-appendix float boundary and reduce the historical floor plot width by 1% to eliminate output-box overflow. Result tables and six accepted medium diagnostic views retained. 27 pages still fails the initial submission-length gate. |

Source owners changed: `ICNP_2026_venue_draft.tex`; `ICNP_VENUE_PREP/{STUDY_DESIGN_VALIDATED_STAGING,RESULTS_VALIDATED_STAGING,RESULTS_VALIDATED_CROSS_TESTBED,APPENDIX_CROSS_TESTBED_TABLES,APPENDIX_DIAGNOSTIC_FIGURES,FUTURE_WORK}.tex`; new `figures/icnp/rq3_switching_reconciled.tex`. The old raster is preserved; only its inclusion is replaced.

## Validator correction

The historical shared helper rounded deltas before deciding status, returned zero relative error for a nonzero discrepancy against zero, and could mark a discrepancy Fixed solely because `solved=True` or an override said so. It now retains raw differences, uses exact equality for arithmetic PASS, reports nonfinite/missing evidence as UNAVAILABLE, and keeps historical disposition in a separate column. Relative error against zero is undefined unless both values are zero. This is arithmetic status, not a judgment that every rounding difference is scientifically significant.

The notebook's first cell explicitly warns that old stored green badges are historical outputs. The shared helper and first markdown cell are updated; all other 121 historical cells and their saved outputs are preserved exactly. Four checkpoint cells append reconciliation and self-test evidence. No historical output is silently relabeled as a fresh run.

Adjacent `reviewer_closure_reconciliation.py` performs read-only checks; `test_reviewer_closure_reconciliation.py` verifies both valid and deliberately invalid inputs. This is support code for the existing notebook, not a replacement execution architecture or dashboard.

## Executed validation

- **13 tests passed, zero failures/errors/skips.** Covers exact match, sub-rounding discrepancy, false solved/override status, missing/nonfinite evidence, zero denominator, all notebook code syntax, source hashes, altered/missing files, wrong manuscript text under Python `-O`, and wrong plotted coordinates. Temporary negative fixtures never alter original sources.
- **Seven pinned CSV hashes match.** Five switching rows and 32 external model/scope summaries are recomputed from saved tables; no simulations or accepted Q07 diagnostics rerun.
- **Seven bounded manuscript checks pass**, including all ten plotted switching/baseline coordinates to their displayed precision. Text checks are regression guards, not proof that every scientific claim is valid.
- Full LaTeX build: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<task-build-directory> ICNP_2026_venue_draft.tex`.
- **27 pages; 92 unique labels; zero undefined source references/citations; 27 referenced raster/vector assets present; zero overfull hboxes/vboxes.** Three existing font-substitution warnings remain. The new switching plot is additionally included as a TeX vector fragment.
- Abstract: 173 whitespace-delimited words; five keywords. Visual review checks the replacement plot at final column size. This is not another whole-paper visual/scientific approval.

Supporting receipts, exact source hashes, full diff and compiled PDF are retained under the existing `research_analysis/REVIEWER_BATCH_2026-10-18/closure_validation_2026-10-22/` evidence area and the existing project Drive mirror. Current status is maintained here in GitHub; the saved evidence records remain historical snapshots. Overleaf obtains the manuscript from GitHub through Piter's normal pull workflow.

## Explicit holds

1. Historical effective allocator cadence, attack settings, training/predictive overrides and external context-to-corpus binding. Documentary evidence recovered below does not close these run-certification holds.

### Bounded documentary recovery, October 22

Read-only evidence inspection; manuscript corrections distinguish recorded headers/constructions from effective run certification. No experiment was rerun.

- GA root: `/Users/pitergarcia/DataScience/Semester4/GA-Work/`. `Validated_Logs/Hybrid_Tests/3Runs/3HybridRuns_S1-2T_all_logs_combined.txt`: lines 46, 132, 227, 322 record stochastic rate 0.0625 and Markov/Adaptive/OnlineAdaptive rates 0.25. Summary line 62 instead prints stochastic X Rate 0.25; use the environment header as documentary evidence, not the summary or a universal certificate.
- Same log: FixedAllocator 45 invocation records, DynamicUCBAllocator 45 (all labelled initial), RandomAllocator 15; observed timesteps are experiment indices 0/1/2. Lines 42/67/92 record fixed allocations (8,10,8,9); 732/757/782 record DynamicUCB (9,9,9,8). These are 35-qubit budgets, distinct from scaled service capacity 6000 at line 736. No within-run continuous adaptation is established.
- Same log: lines 1438/1439 show different Random invocation/environment allocations. Lines 1448–1454 record substitute (21,6,6,2), validated original runner path `framework_state/day_20251204/QuantumExperimentRunner_1_6000-Random_Stochastic_Random-4000_1_(21_6_6_2).pkl`, file size 3681499, pickle loading, equality check True and resume. Line 1455 skips already-stored results. This proves a historical resume trace, not current file availability or fresh execution.
- Notebook root under GA root: `hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/`. `H-MABs_Eval-Testbed-Paper7.ipynb` lines 883–899 define hop count, mean degree and summed distance (missing distance attribute 1.0); saved output 810/814 reports four contexts/paths. `H-MABs_Eval-Testbed-Paper12.ipynb` lines 1302–1315 define topology-derived action counts and repeated three-feature vectors (hop count, normalized mean degree, fusion probability; missing node qubits 5); saved output 830/831 reports four paths and action-vector shape (3,), not one action/path. `H-MABs_Eval-Testbed-Paper2.ipynb` line 1053 returns external_contexts=None; saved output 1416 reports time-based decay. These definitions/outputs are documentary, not exact context-to-result bindings.
- Explicit runtime beta/learner-mode assignments were not recovered in the bounded scan of 253 configuration-log files and saved Hybrid notebook outputs. Printed static dictionaries and mode-labelled filenames do not certify effective nested settings.
- Existing `daqr/config/drive_backup_registry.json` indexes 3788 framework and 13069 model .pkl keys; live Drive availability was not checked. `local_backup_registry.json` indexes 205 framework and 502 model pointers; none of those 707 referenced local files existed at inspection. Counts are registry snapshots, not verified datalake holdings. No pickle was loaded or downloaded during this inspection.
2. Eight historical Hybrid source/scenario summary labels differ from recomputed mean-efficiency leaders. Their original summary/export rule is still unresolved; saved counts must remain explicitly labelled. Small display-rounding differences are not scientific blockers.
3. Experimental accounting is resolved at the exported-record level. Statistical reporting is resolved as descriptive, with explicit output-specific units and winner rules. No bootstrap result is claimed without evidence. Historical missing settings remain under item 1.
4. JSAC length, owner/coauthor approval, independent integration review and human submission fields.
5. Original dirty paper/framework checkouts remain preserved rather than overwritten. Their local uncommitted work is not part of this publication. GitHub main and the established notebook branch contain the task's corrections; Piter can pull the manuscript into Overleaf normally.

No new experiment, accepted-corpus change, F02 reopening, new causal claim, or manuscript submission is part of this checkpoint.
