# Whole-paper corrections and Validation Hub checkpoint

## Scope and status

Owner-authorized corrections to the October 22 audit, followed by explicit validation of the existing validator. This is **PASS WITH EXPLICIT HOLDS**, not closure of every reviewer item, independent approval of new wording, or submission readiness. Q07/F10 existing-trace diagnosis remains accepted and closed; historical 100-node causality remains unresolved.

The canonical job/evidence record remains the existing `H-MABs_MasterDataset_VerificationHub.ipynb` in `pzg8794/quantum_project`, branch `codex/mq-q04-notebook-execution`. Its final October 22 cells contain executed reconciliation and validator-test outputs. This checkpoint was executed locally, **not in hosted Colab**, and did not execute the historical notebook wholesale.

- [Exact Validation Hub checkpoint in Colab](https://colab.research.google.com/github/pzg8794/quantum_project/blob/9e82d0e1aa42dc607b32052de14e2919017a15a9/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb).
- [Notebook, helper and regression tests at the pushed framework commit](https://github.com/pzg8794/quantum_project/tree/9e82d0e1aa42dc607b32052de14e2919017a15a9/Dynamic_Routing_Eval_Framework/notebooks).
- Validated manuscript source commit: `21ee41bdbdce2f21e13ff4b333340087fb3a2dac`; scientific corrections began at `8bd0214d39449c03c23eb3e857e00148197db998`.
- [Restricted checkpoint mirror](https://drive.google.com/drive/folders/1B3mo02ruJgq0TQbPH2oaD_gWAWpI5gxr); its synchronization receipt distinguishes upload/readback from byte-level verification.

Use the pinned notebook above, not an older `gcp-main` Colab link. This checkpoint does not merge branches or overwrite the original dirty framework checkout.

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

Private supporting receipts, exact source hashes, full diff and compiled PDF are retained under the existing `research_analysis/REVIEWER_BATCH_2026-10-18/closure_validation_2026-10-22/` evidence area and mirrored within the existing restricted campaign infrastructure. Destination-specific links and synchronization receipt accompany the handoff; do not infer Overleaf parity from a Git push.

## Explicit holds

1. Historical effective allocator cadence, attack settings, training/predictive overrides and some external context definitions.
2. Exact old table/source revision parity: for example the current native Paper8 all-allocator saved percentage mean is 67.84637%, while the manuscript prints 67.9%. Correct aggregation wording does not certify that rounding discrepancy. Old winner-count differences also require original-output provenance.
3. Executed-unit crosswalk for 8,241 tests versus planned 552 configurations / 5,520 episodes / 380 GPU-hours; bootstrap resampling units and winner/tie conventions per output.
4. JSAC length, owner/coauthor approval, independent integration review and human submission fields.
5. Original dirty paper/framework checkouts and divergent Overleaf remain preserved, not synchronized or overwritten. Work is on the isolated review and framework worktrees; there is no automatic replacement of the owner's active manuscript.

No new experiment, accepted-corpus change, F02 reopening, new causal claim, or manuscript submission is part of this checkpoint.
