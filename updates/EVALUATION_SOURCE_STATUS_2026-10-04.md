# Evaluation Source Status — October 4, 2026

This register identifies the current authoritative sources for evaluating the
post-ICNP revision and medium-scale experiment. It separates artifact integrity
from scientific interpretation and prevents stale planning text from being used
as evidence of current completion.

## Current source hierarchy

**Later original-object recovery:** Four separately stored NeuralUCB learners contain their actual networks, Adam optimizer state/settings and replay buffers; original bytes match provider size, MD5 and SHA-256. Those fields are available in the datalake, not absent because the top-level model snapshots omit them. The expanded inventory retains 7097 provider IDs and 153 duplicate filenames. Parent-run binding remains a separate check; Paper7's inspected runner/model still differs from its native export. [Exact recovered values and boundary](DATALAKE_ORIGINAL_SOURCE_VALIDATION_2026-10-22.md#later-source-recovery-correction--separately-saved-learners). This supersedes broad missing-neural-state language below without reopening Q07.

| Purpose | Authoritative source | Current status |
|---|---|---|
| Campaign SDLC and task acceptance | [Canonical medium-scale execution board](https://github.com/pzg8794/Fall-2026-Semester-Master-Plan/blob/e4f00e5/CAMPAIGNS/2026-09-26-MEDIUM-SCALE/SDLC-EXECUTION-BOARD-2026-09-27.md) | Linked commit is the earlier campaign checkpoint; local Q-07 scientific closure is recorded below, without claiming that the remote board was updated |
| Frozen execution implementation | [Quantum source revision `f5ed371c`](https://github.com/pzg8794/quantum_project/tree/f5ed371ca0e3ddd5af942d9deb992fdd82ce0b08) | Source revision used by the fresh 75-cell campaign |
| Independent result review | [Q-05 Default/fixed result review at `38e17b5c`](https://github.com/pzg8794/quantum_project/blob/38e17b5c4189479e3670d37036c10921863effb0/Dynamic_Routing_Eval_Framework/docs/guides/MQ_Q05_DEFAULT_FIXED_RESULT_REVIEW.md) | Historical artifact-acceptance checkpoint; Q-07 diagnosis and final claim-limited scientific review are recorded below |
| Manuscript implementation | [`ICNP_2026_venue_draft.tex`](../ICNP_2026_venue_draft.tex) and included section/appendix sources | Current paper source; do not infer experimental acceptance from manuscript prose |
| Reviewer task status | [`FEEDBACK_TASKS.md`](FEEDBACK_TASKS.md) | Local tracker distinguishes completed execution and Q-07 analysis, unresolved historical 100-node causality, and provenance holds |
| Primary venue requirements | [JSAC Quantum Series checklist](../venues/jsac_quantum_series/SUBMISSION_CHECKLIST.md) | Primary route; official call permits submission at any time |
| Backup venue requirements | [TNET checklist](../venues/tnet/SUBMISSION_CHECKLIST.md) | Rolling backup; no concurrent submission while JSAC is active |

## Accepted medium-scale execution identity

- Matrix: 3 blocks × 5 threats × 5 models = **75 cells**.
- Models: `Oracle`, `GNeuralUCB`, `EXPNeuralUCB`,
  `CPursuitNeuralUCB`, and `iCPursuitNeuralUCB`.
- Horizon: **6,000 frames per cell**.
- Allocator: **Default/fixed**, with ten route budgets of nine qubits.
- Source notebook SHA-256:
  `82fe9f6d557a3fe8666fff364f51c1f45032746b91a111e75f6ceaf7b4cd1436`.
- Executed notebook SHA-256:
  `2f56ce51faa588f93f379adca8c3ec3261b94cc5fba04c950535a883e3953103`.
- Campaign receipt SHA-256:
  `cfa05be491183597963c6efe3e02de28b8ee13adc01f61cfe91b9d0bbcdd0c21`.
- Validation: 75/75 complete, 1.8 million ordered event records, no failed
  cells, no technical retries, no performance reruns, and maximum aggregate
  recomputation delta **0.0**.
- Isolation: the superseded 45-cell diagnostic remains immutable and was not
  pooled into the accepted campaign.

## Interpretation boundary

The accepted traces and completed Q-07 analysis support bounded descriptive
findings, not a causal explanation of the historical 100-node result or an
unreviewed manuscript claim. F-14 must integrate the claim--evidence boundary
before manuscript wording changes. No rerun, favorable-result filtering, or
replacement run is authorized by this register.

## Q-07/F-10 scientific-analysis closure

- **Disposition:** Q-07 existing-trace diagnosis **COMPLETE and independently accepted**. Final independent scientific audit: **PASS WITH REQUIRED CLAIM LIMITATIONS**. Astra completed the primary analysis; Sol independently reproduced it from accepted traces with zero material numerical mismatches. No analysis repair, provenance blocker, or experiment rerun remains.
- **F-10 boundary:** The medium-scale diagnosis is complete, but the historical 100-node efficiency-compression cause remains **UNRESOLVED**. Observed structural-zero occupancy, sparse within-route action exposure, continued change through 6,000 frames without established convergence, weak sampled Bernoulli route feedback for G/EXP/CP despite continuous allocation feedback, severe OnlineAdaptive availability constraints, threat/block/window/metric-dependent rankings, and a large descriptive gap to a privileged Oracle are not isolated causes of that historical result. Node count alone is not an established explanation. No new experiment is currently required; later diagnostics depend on advisor/reviewer evidence needs.
- **Next separate task:** F-14 claim--evidence integration/planning, then the remaining reviewer/manuscript queue. This administrative closure does not edit or approve manuscript wording.

### Accepted restricted evidence

| Evidence | Private Drive location | Identity / verification |
|---|---|---|
| Astra primary Q-07 analysis | [Astra Q-07 folder](https://drive.google.com/drive/folders/10PYZQVKJy8xtXa700uNqZ0QlxcdXFANU) | Manifest SHA-256 `3835ec30494d82cb24d17688649e1868d40f6c8953f602e43333049cfce6ef28`; 49/49 mirrored files matched |
| Sol independent reproduction | [Sol reproduction folder](https://drive.google.com/drive/folders/1sagYkhj1YNVThaRHfya2AMK2a1ZT-FC9) | Manifest SHA-256 `9116dd2a795fcaa4e5207cab89155be707012953fe5b4f5861a26de379c00276`; 37/37 mirrored files matched |
| Accepted Q-05/Q-06 input evidence | [Campaign input folder](https://drive.google.com/drive/folders/1waWGmnGIBABVpu7XWSWL8UnKTkff71T5) and [75-cell trace bundles](https://drive.google.com/drive/folders/1C0PCfP8U1hoiAT0EVvEoVPsDKkNXOnP6) | Campaign receipt SHA-256 `cfa05be491183597963c6efe3e02de28b8ee13adc01f61cfe91b9d0bbcdd0c21`; 828/828 hashed inputs matched; all 75 cells present with 11 files each |
| Pre-closure control snapshots | [Restricted control-snapshot folder](https://drive.google.com/drive/folders/1OUDSgpu6pTngDKNmzbCpLpKQ0YxnxPX8) | Evidence snapshots only; they do not contain this later local status closure |

The accepted mirror uploaded 935/935 files under unchanged restricted/owner-only
permissions. These are prior mirror-verification results, not a new upload or
permission change by this status update.

## Open provenance items

**Current narrowed source boundary:** Original result fields reproduce for Paper2, Paper12 and all Paper8 source occurrences; Paper8 base/rate-only/balanced identities are restored in the retained receipt. CP/G/iCP model snapshots are trajectory-matched and their specifically stored settings recovered. The actual outstanding external binding is Paper7: same-named indexed candidates use different route configurations/results. Complete neural-training fields are absent from the inspected snapshot dictionaries, and some saved context strings are truncated. Do not conflate these specific limits with missing original results or silently substitute differently configured objects. [Full original-source verification](DATALAKE_ORIGINAL_SOURCE_VALIDATION_2026-10-22.md). Earlier generic bullets below remain historical scope descriptions, not a new assertion of data unavailability.

**Latest October 22 original-source correction:** All 101 source filenames referenced by the four primary historical exports are present in the actual datalake and their original bytes have been provider-checksum verified. All 10240 exported rows / 296960 field comparisons reproduce with zero mismatches. The eight flagged Hybrid summary labels reproduce the original modal-winner fallback; they are not erroneous mean-efficiency labels. [Exact verification scope and source-binding limits](DATALAKE_ORIGINAL_SOURCE_VALIDATION_2026-10-22.md). Earlier CSV-only availability checks below are historical, not a claim that original data are missing. No manuscript, accepted medium data, or Q07 analysis was changed.

**October 22 bounded follow-up:** Exported-record accounting and descriptive statistical definitions are reconciled in the existing Validation Hub using the unchanged shared `StateReporting` source contract. All 1999 experiment winners reproduce; eight Hybrid source/scenario summary labels differ from mean-efficiency leaders and remain traceable in the new output. Historical log header rates and saved external notebook definitions have been recovered without treating them as full effective-run certificates. [Current evidence and remaining boundary](CLOSURE_FIXES_2026-10-22.md). This does not reopen accepted Q07 or authorize an experiment.

- Exact adaptive allocator execution cadence in the data-producing workflow.
- Historical attack-strategy parameters used for the validated manuscript corpus.
- Validated-run hyperparameters not already tied to immutable run evidence.
- External-testbed context encodings other than the verified Paper8 representation.
- Random, DynamicUCB, and ThompsonSampling allocator qualification remains outside
  the accepted Default/fixed Tier-1 campaign.

## Repository-state boundary

The active local manuscript checkout contained pre-existing tracked and untracked
work and was behind GitHub when this register was prepared. Those files were
preserved; no reset, stash, force synchronization, or manuscript edit was used to
manufacture parity. GitHub, local manuscript, and Overleaf state must therefore be
reconciled deliberately before any future publication release is declared synced.
