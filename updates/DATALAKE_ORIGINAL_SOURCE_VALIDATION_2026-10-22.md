# Original datalake source verification — October 22, 2026

## Scope and disposition

The original data are present. Earlier CSV-only checks were not original-source validation, and an unavailable connected Drive account did not establish that the datalake was unavailable. This pass uses the existing configured `GoogleDriveBackupManager`, its existing exact-filename indices, and the established `state_analysis.extract_data_from_state_file` exporter. No loader, experiment runner, storage system, or dashboard was replaced.

**Primary historical exports: ORIGINAL-SOURCE PARITY VERIFIED.** All 101 referenced framework-state filenames were retrieved from the existing datalake and checked against provider byte length, MD5 and SHA-256. They comprise 81 distinct byte groups; identical snapshot aliases are retained as provenance, not counted as independent replications. Strict original-object loading succeeded. All 10240 exported model-result rows reproduce across all 29 compared columns: **296960 field comparisons, zero mismatches** (numeric tolerance: relative `1e-12`, absolute `1e-9`). Original source filenames identify the comparisons and are separately bound to provider metadata rather than numerically compared.

| Historical export | Original-backed rows | Non-Oracle | Oracle |
|---|---:|---:|---:|
| Hybrid | 4920 | 3936 | 984 |
| CMABs | 1200 | 1000 | 200 |
| iCMABs | 2580 | 2150 | 430 |
| EXP3 | 1540 | 1155 | 385 |
| Total | 10240 | 8241 | 1999 |

These are exported observations, not independent episode counts. No source object or CSV was edited, filtered, renamed, or deduplicated. Temporary downloaded copies are removed only after checksum verification and retention of exact receipts; canonical datalake objects remain unchanged.

## Eight apparent winner discrepancies — resolved

The original older states lack stored scenario aggregates. The existing exporter therefore uses the **modal per-experiment winner**, with first-encounter ordering for equal win counts. The earlier check compared that label to a **mean-efficiency leader**. Those are different defined statistics and need not agree.

All eight flagged cases reproduce the original modal-winner fallback exactly. Their original labels and mean-efficiency calculations are preserved. No numerical correction, new experiment, or unresolved data-discrepancy task is justified by this difference. The receipt records the source/scenario identities, original win counts, fallback label, and mean-efficiency leader.

## What this closes, and what it does not

- **Closed:** Original-source availability for these primary exports; original-to-export result/metadata parity; exported-record accounting; the eight alleged scenario-summary inconsistencies.
- **Already resolved and retained:** Descriptive statistical units, explicit winner/tie definitions and denominators; unsupported bootstrap inference is not claimed.
- **Not implied by an endpoint match:** Every historical source-code revision or every nested learner/allocator parameter. Saved model snapshots must be matched to the actual result by identity/trajectory, not by filename similarity or current defaults. This is a specific source-binding question, not missing original results.
- **Unchanged:** Q07/F10 existing-trace scientific acceptance and its required claim limits; no causal explanation of the historical 100-node result; no new experiment required by this verification.
- **Separate release gates:** Manuscript length, final scientific integration review, owner/coauthor and human submission fields. No manuscript text was changed in this pass.

## Evidence and validation

The existing [project Drive evidence area](https://drive.google.com/drive/folders/1hzkGPv9cYXUoCAE8n-FoLNFBIQZNPkhi) retains original-source receipts, provider identities/checksums, reproducible loader/exporter invocation, validator outputs, settings-binding evidence and the updated Validation Hub. Exact private object identities remain in that existing evidence location, not in public GitHub.

The canonical job/evidence record remains the [existing Validation Hub](https://colab.research.google.com/github/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb). The new original-source checkpoint supersedes its earlier CSV-only scope and unresolved-summary annotation; historical cells/outputs remain unchanged. Local execution is identified as local, not hosted Colab execution. No scientific experiment, accepted Q07 analysis, or manuscript build was rerun.

## External original-source reconciliation

| Native export | Original-backed scope | Disposition |
|---|---|---|
| Paper2 | 12 original objects / 1500 rows | All 29 common exporter columns match. Original recorded external contexts are `None`, not a claimed universal feature vector. |
| Paper12 | 12 original objects / 1500 rows | Result fields match. Differences are 300 Oracle summary placeholders (`0` versus absent/null) and 375 repeated runtime fields; neither changes a reward/efficiency finding. Original contexts contain four route sets with five three-feature actions each. |
| Paper8 | 12 source occurrences / all 300 rows | Original base, rate-only and balanced source objects uniquely reproduce the three occurrences per allocator. The legacy export collapses these different source-mode filenames into one displayed filename; the binding receipt restores exact identities without altering any CSV row. The only remaining matched-row differences are 60 Oracle summary placeholders (`0` versus absent/null). |
| Paper7 | 12 indexed candidates checked against 1500 rows | **HOLD — these candidates do not reproduce this native export.** The independently checked representative retains the same 50-node topology but four contextual routes instead of the export's fifteen; rewards and efficiencies also differ. Do not replace the native export with this differently configured run. |

The independent Paper7 lookup checked the two exact representative names, their direct parent paths and the returned revision history in the configured shared drive. It found no matching original in that bounded scope. This is a **specific source-version/configuration binding gap**, not proof that all original data are absent from the datalake or other archives.

Extra native metadata columns not produced by the historical exporter are explicitly outside its scalar parity check; context fields above are separately read from the original objects. Several Paper8 contexts survive only as truncated array strings containing ellipses. Those strings do not reconstruct complete action catalogs or certify an eight-feature context for every historical native run. The source receipt preserves this boundary rather than guessing a shape.

## Original model snapshots and effective settings

Three original model snapshots were checksum-verified and their complete reward, regret and route/action trajectories matched to the corresponding original framework results: CP to the `T` MARKOV/1 result; G and iCP to the `Tb` MARKOV/1 results. These are actual retained-result bindings, not filename-only associations.

Recovered serialized fields include CP/iCP Pursuit learning rate `0.1`, top-level beta `1.0`, and iCP warmup `50` / ARIMA update interval `200` for their specifically matched snapshots. The fitted iCP model retains ARIMA order `(0,0,0)`; that does not imply a universal fixed order or recover the original order-search settings. Exact object paths, result seeds and trajectory hashes remain in the private receipt. These values must not be promoted to every historical run or to omitted nested NeuralUCB settings.

The inspected snapshots do **not** serialize the nested neural networks/optimizers, complete replay state or every training parameter. Consequently, hidden-layer/optimizer/cadence claims cannot be certified from these particular objects alone. Current defaults are not substituted. CMAB/iCMAB mode labels describe the routing layer, not evidence that within-route neural learning was absent.

## Final bounded validation

**27/27 validator tests pass**, including malformed receipt containers/booleans/digests/counts, missing-versus-null original fields, missing/altered evidence, duplicate identities, contradictory modal counts/ties, and unsafe/invalid context expressions. Independent review reproduced the primary counts and modal explanations and required the fail-closed corrections before acceptance. The exact final review and source-binding evidence are retained in the existing evidence mirror.

Original dirty local manuscript/framework work remains preserved. This verification changes the Validation Hub, its support checks and status/provenance records only; no manuscript source, original dataset or experiment code is changed.
