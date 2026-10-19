# F-14 — Claim–evidence integration plan

**Date:** October 18, 2026

**Task:** 1 of the eight owner-requested revision tasks

**Status:** Evidence map and first exact wording package prepared; manuscript integration awaits sentence approval. This is not final F-14 closure.

## Authority and workflow

Piter authorized implementation of the eight-task closure sequence with a separate commit for each task. The existing [wording-review workflow](FEEDBACK_TASKS.md#working-rule) still requires the complete current paragraph, exact proposed change, and owner approval before scientific wording is edited. Commit creation is not wording approval.

The approved F-14 design is section E of the [scale/claim decision record at paper revision 0bcc913](https://github.com/pzg8794/QuantumFaultTolerant/blob/0bcc913bc5a28b1e1116245cf692989a9ec98aae/updates/REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md). It requires claims throughout Abstract, Introduction, Results, Discussion, and Conclusion to identify their evidence origin, scope, persistence, variation, and limits. The present plan adds Limitations because its live topology sentence is already inconsistent with the evaluated evidence.

The accepted [Q-07/F-10 closure](EVALUATION_SOURCE_STATUS_2026-10-04.md#q-07f-10-scientific-analysis-closure) is preserved: **PASS WITH REQUIRED CLAIM LIMITATIONS**. The medium diagnosis is complete; the historical 100-node causal explanation remains unresolved. No new experiment is required by this plan.

## Evidence identities

The analysis directories are referenced, not copied or recomputed. Paths below are relative to the GA-Work root, two levels above this paper repository.

| ID | Existing evidence | Identity and scope |
|---|---|---|
| A | `research_analysis/Q07_MEDIUM_TRACE_2026-10-04/` — `REPORT.md`, `NUMERICAL_TABLES.md`, `SOURCE_AUDIT.md`, tables and figures | `ARTIFACT_SHA256.json`: `3835ec30494d82cb24d17688649e1868d40f6c8953f602e43333049cfce6ef28`; 49 listed files verified unchanged during this task |
| S | `research_analysis/Q07_MEDIUM_TRACE_2026-10-04_SOL_REPRO/` — `SOL_REPRODUCTION_REPORT.md`, `ASTRA_SOL_NUMERIC_DIFF.md`, tables and validation | `ARTIFACT_SHA256.json`: `9116dd2a795fcaa4e5207cab89155be707012953fe5b4f5861a26de379c00276`; 37 listed files verified unchanged during this task |
| Q | `quantum_experiment_evidence/medium-tier1/default-fixed-full-roster-v2/q04-evidence/campaign-receipt.json` | SHA-256 `cfa05be491183597963c6efe3e02de28b8ee13adc01f61cfe91b9d0bbcdd0c21`, verified during this task; execution source `f5ed371ca0e3ddd5af942d9deb992fdd82ce0b08` |
| H | Existing primary and external manuscript evidence, including `tab:model_family_comparison_full` and `tab:testbed_comparison_full` | Historical findings retained; this integration task does not recompute their datasets or assert that the medium implementation generated them |
| R | Current local `EVALUATION_SOURCE_STATUS_2026-10-04.md` | Records final independent audit acceptance and the previously hash-verified private mirror; this task does not reassert a new Drive readback |

Remote review locations: [Astra](https://drive.google.com/drive/folders/10PYZQVKJy8xtXa700uNqZ0QlxcdXFANU), [Sol](https://drive.google.com/drive/folders/1sagYkhj1YNVThaRHfya2AMK2a1ZT-FC9), [accepted inputs](https://drive.google.com/drive/folders/1waWGmnGIBABVpu7XWSWL8UnKTkff71T5), and [75-cell bundles](https://drive.google.com/drive/folders/1C0PCfP8U1hoiAT0EVvEoVPsDKkNXOnP6). Existing restricted permissions remain unchanged.

## Evidence levels after the accepted medium run

| Level | What exists | Permitted interpretation |
|---|---|---|
| I: primary matched evidence | Policy × threat × allocator × replay/capacity comparisons on the primary topology | Strong comparative findings within those conditions; grouped comparisons do not become formal statistical interaction estimates |
| II: scale investigation | One accepted medium anchor: 15 nodes, ten candidate routes, 550 feasible route/action pairs; Default/fixed allocation, one recorded replay setting | Medium-setting findings and bounded comparison with earlier evidence; a complete controlled scale spectrum or node-count effect is not established |
| III: external evidence | Four heterogeneous testbeds | External corroboration and boundary testing; differences cannot be attributed solely to node count or topology |
| IV: hardware/deployment evidence | Not established | No deployment-grade, hardware-readiness, or field-validated claim |

The five-model medium roster is Oracle, GNeuralUCB, EXPNeuralUCB, CPursuitNeuralUCB, and iCPursuitNeuralUCB. It does not replace the historical 15-policy non-Oracle portfolio. The live Abstract already says fifteen; an old thirteen-policy draft is not the baseline for this revision.

## Frozen definitions to carry into the manuscript

- Medium campaign: 75 cells = five models × five threats × three blocks; 6,000 decision frames per cell, 450,000 decision frames and 1.8 million phase records. Phase records are not independent trials.
- Analyzed outcome: continuous selected payoff. Sampled Bernoulli route feedback is a separate recorded channel.
- Efficiency: for each block, threat, and window, 100 × learned continuous-payoff sum / corresponding Oracle sum; then the equal-weight mean of three block ratios. It is neither physical delivery percentage nor a ratio of pooled sums.
- Structural zero: selected action has catalog base payoff exactly zero. Realized zero: selected continuous payoff exactly zero. Availability and structural action quality are separate dimensions that can overlap.
- Early: frames 1–2,000; middle: 2,001–4,000; late: 4,001–6,000. Existing trajectories use twelve disjoint 500-frame bins. No new outcome-selected windows are proposed.
- Oracle has catalog/current-availability information. Reactive histories can depend on each policy's previous choices. Oracle gaps are descriptive; shared seeds do not imply identical reactive exposure.

## Claim–evidence matrix

| ID / finding | Direct evidence and experimental scope | Supported conclusion | Not established | Manuscript owner / action |
|---|---|---|---|---|
| C01: framework contribution | H; matched evaluation design and controls | Controlled evaluation reveals conditional differences and patterns among comparison policies | A new winning algorithm as the paper's central contribution | Active draft Abstract/Introduction: preserve approved F-02 hierarchy |
| C02: historical performance tier | H; primary and external tables | Report the existing 18–24 pp gaps, robustness floors, and configuration-specific efficiencies within their original evidence scopes | Stable superiority across the new medium campaign | Active draft contributions; Discussion opening; Conclusion: attach explicit scope where medium integration makes the existing wording ambiguous |
| C03: capacity paradox | H; existing ThompsonSampling/Tb replay slice and RQ3 evidence | Preserve the recorded 4.4 pp decrease and 6.0 pp recovery and the joint configuration-dependence finding | Medium replay effects, allocator dominance, or an isolated predictability mechanism | Existing RQ3 text/figures retained; medium has no allocator/replay sweep |
| C04: external persistence | H; `tab:testbed_comparison_full` | Historical average leader and configuration winners can differ across four testbeds | Controlled scaling curve or guaranteed transfer | Cross-testbed Results and Conclusion: preserve values and distinguish this evidence from medium results |
| C05: medium compression | A report D; S report D/G and `window_summary.csv`, full window | Learned mean efficiencies are 1.1122–3.8674% outside OnlineAdaptive and 0–0.0662% in OnlineAdaptive under the recorded normalization | Low physical delivery percentages, statistical equivalence of models, or node-count causation | New medium Results subsection and metric definition |
| C06: structural-zero occupancy | A report A; S report A; `windows_by_block.csv` and `window_summary.csv` | Baseline mean structural-zero selection is 87.7167–90.2611% despite full availability; zero-base actions account for many zero-payoff selections | Why those actions are selected, a universal algorithm defect, or a proven corrective intervention | Medium Results and bounded Discussion |
| C07: exposure | A report C; S report C; `actions_by_block.csv`, `routes_by_block.csv` | Baseline learned cells visit all ten routes but only 133–185 of 550 route/action pairs; many high-value actions are unvisited | Sparse route visitation, a requirement to visit every action, or causal proof that catalog size caused poor learning | Medium action-exposure account; detailed census remains supporting evidence |
| C08: within-horizon change | A report B; S report B; `convergence_by_block.csv` | Late continuous payoff exceeds early payoff in 47/48 non-OnlineAdaptive learned cells; convergence is not established | Slower learning than a matched small-scale trajectory, a fitted asymptote, or a guarantee that longer training rescues performance | Medium Results; Limitations; avoid describing all cells as still improving |
| C09: feedback channels | A feedback diagnosis and source audit; S report D and `feedback_signal_scale.csv` | G/EXP/CP have zero positive sampled Bernoulli route-feedback draws over 90,000 frames each; positive continuous allocation updates still occur; iCP has a different route-update channel | No useful learner feedback, a demonstrated code defect, or equivalent feedback semantics across all four models | Algorithm/context appendix and medium diagnostic prose; reconcile in task 3 |
| C10: OnlineAdaptive | A report E; S report E; `onlineadaptive_diagnostics.csv` | Global availability is 8,343/180,000 route-frames = 4.635% per model; all routes are unavailable in 12,868/18,000 frames = 71.4889%; availability and structural-zero selection both constrain realized payoff | Availability alone explains the gap, equal masks from equal aggregate rates, or isolated reactivity/burst effects | Medium Results and comparator limitation |
| C11: conditional rankings | S report F; `rankings.csv`, `block_rankings.csv` | CP leads four full-horizon threat means but only one of three blocks in each; EXP leads OnlineAdaptive full mean with 15 positive-payoff frames; window and metric changes can change leaders | Stable pursuit-family superiority, significant superiority, or global winners from one dashboard block | Medium summary table plus block/window qualification; preserve ranking as a framework finding |
| C12: Oracle gap | A report D/source audit; S report D; `mask_mismatch_vs_oracle.csv` | Large descriptive shortfall from an informed current-catalog/availability comparator | Causal learner deficiency, formal regret guarantees, or a common reactive counterfactual | Metric methods, medium Results, Discussion |
| C13: historical 100-node result | H at pinned paper revision 0bcc913; S report G | Historical efficiencies compress around 43–44% in a different protocol; the medium diagnostics identify observations worth distinguishing | Any medium characteristic caused that historical compression, or node count alone explains it | Limitations and Discussion: causal explanation unresolved; no new experiment currently required |
| C14: deployment | Evidence levels I–III; R closure boundary | Simulator-specific configuration guidance and explicit unresolved hardware questions | Hardware readiness or field validation | Abstract/Conclusion: preserve F-07; review only new scope conflicts |

## Placement plan and eight-task sequence

| Owner task | Concrete output | Current disposition / next gate |
|---|---|---|
| 1 — F-14 | This evidence matrix, provenance identities, and exact paragraph review packages | Planning prepared. First sentence package is [F14_REVIEW_01_TOPOLOGY_SCOPE.md](F14_REVIEW_01_TOPOLOGY_SCOPE.md); no manuscript wording approval inferred |
| 2 — F-08/F-09/Q07/F-10 presentation | Methods paragraph, compact five-threat/four-policy mean table with three-block scope, selected existing diagnostic panels, bounded synthesis | Scientific work remains complete. Prepare artifacts against this matrix, approve exact prose/captions, integrate and build; do not start another run |
| 3 — F-03/F-05 | Corpus-specific execution/feedback contract and allocator-cadence disposition | Existing source/receipt reconciliation before any new implementation; historical adaptive cadence remains open |
| 4 — F-04 | Reported-run parameter/context table with traceable source identities | Exact historical values and other external encodings still require evidence; current defaults cannot fill gaps |
| 5 — F-06 | Threat-process specification associated with each evaluated corpus | Approved physical grounding retained; historical process/parameter provenance remains open |
| 6 — F-13 | Reviewed compression after accepted medium material is placed | Preserve findings and qualifications; move detailed rows to appendix where appropriate; no unsupported numerical target for compression |
| 7 — F-11 | Reviewer B concern-to-section/evidence disposition | Perform after preceding integration; distinguish resolved, bounded limitation, and genuinely unresolved items |
| 8 — F-12 | Journal-format candidate, refreshed submission audit, source/build manifest, coauthor checklist | Exact word/page counts need fresh measurement; author/account confirmations remain human inputs; reconciliation precedes any synchronization claim |

Each task receives its own substantive commit when its authorized deliverable is ready. A blocked task is not marked complete to manufacture eight completed commits. F-02/F-07 and Q-07 acceptance remain closed; new evidence integration is reviewed under F-14. Prototype polish is separate from these eight manuscript/evidence tasks.

## Validation and repository boundary

- Fetched origin and Overleaf without modifying the worktree. Origin/main was read live at `0bcc913bc5a28b1e1116245cf692989a9ec98aae`; Overleaf/master fetched as `c304cb83c50fa9f51302dc59d54829e33a8bdcc1`.
- Local paper main started at `5754af0bc23a627ee0ec7b332e10a05c811ddd5f`, 64 commits behind origin/main, with pre-existing tracked and untracked changes. No merge, reset, stash, or bulk staging is authorized by this task.
- Before changes, the 324 pre-existing tracked/untracked regular files in the paper repository had inventory SHA-256 `5f32c7eef62e6f42966f30427b04b1b9064f78454a13d68f1ae3cd17f93f56f6` (sorted filename/SHA-256 pairs, compact JSON encoding). The new task files are excluded from the post-task preservation comparison.
- Verified all 49 Astra and 37 Sol manifest-listed files and the accepted campaign receipt. This was hash verification and reading accepted reports, not scientific recomputation.
- Scientific thresholds, metrics, windows, and counts above are transcribed from accepted analysis. Historical primary/external results are retained with their existing provenance status.
- Documentation validation must check whitespace, local links, exact current-paragraph equality, and preservation of all pre-existing files before commit. No manuscript build is warranted until manuscript edits occur.
- This task does not synchronize the dirty paper checkout or alter Drive/Overleaf evidence. A local commit must not be reported as remote synchronization.
