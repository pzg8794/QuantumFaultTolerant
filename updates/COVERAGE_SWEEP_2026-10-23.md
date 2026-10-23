# Post-consolidation coverage and reviewer-closure sweep

## Verdict

**Component-copy coverage and access: PASS. Overall reviewer/submission closure:
NOT YET COMPLETE.** The remaining work is not a claim that the datalake or Paper7
logs/notebooks are missing. Storage integrity, historical run identity, manuscript
accuracy and submission readiness are separate checks.

This sweep rechecks the existing evidence and current source; it does not rerun
experiments, accepted Q07 analysis or a manuscript build. The unchanged source is
compared with the latest retained build receipt. The older 27-page status is
superseded by that receipt's **28 pages**.

## Storage and validator checks

- Fresh enumeration rechecks all **20,774 copied payloads**, including size,
  SHA-256 and MD5, representing **21,659 original identities** with 885 exact
  aliases. Counts remain notebooks 192, framework state 4,627, model state 15,305
  and logs 650. No missing or changed destination payload is found.
- All four drives retain exactly the approved Rochester/RIT Managers and service
  account Content manager. No permission changes occur during this sweep.
- The current original-drive component inventory has **zero additions, removals
  or changes** since the closing copy inventory. Local discovery finds no new or
  removed component files; 862 local files and 112 commit-pinned Git blobs match.
  The sole changed local source is the intentionally updated Validation Hub,
  already published separately under `notebooks/current/`; its historical copy
  remains intact.
- All 45 manifest-listed evidence files, 51 prior Drive publications and six
  pinned GitHub file versions pass readback. Four downloaded payload spot checks
  also match. Full-file integrity for every destination is checked using provider
  checksums, not by claiming that all 96 GB were downloaded again.
- The historical root's complete retained inventory and selected copied payloads
  remain verified; that original root is not newly enumerated in this sweep.
  Its recovered access and exact identity remain registered, not marked missing.
- **21 component-validator tests and 27 reviewer-validator tests pass.** The
  reviewer suite runs with all required existing inputs configured, with no skips.
  The first unconfigured invocation failed on missing environment configuration;
  the corrected invocation and both logs are retained, not silently relabelled.
- The existing Verification Hub remains the job/evidence record. Its new sweep
  entry checks hash-pinned receipts and records actual local execution. This is
  not a full hosted-Colab run or a replacement validation system.

Private reproducible checks, live inventories, readbacks and execution logs:
[post-copy sweep evidence](https://drive.google.com/drive/folders/1mdoq3nKmNpTloZhtiGUJZmc0XJgjG8lx).
Original copy manifest and source-to-copy mapping:
[component consolidation evidence](https://drive.google.com/drive/folders/1d7T-9kOTbC0n45gvw4tPWMlNFO4IC-9B).

## Reviewer requirement to current disposition

| Tasks / feedback | Implemented and evidenced | What still closes the item |
|---|---|---|
| F02/F07: contribution and overclaiming | Framework-first contribution, bounded primary/external findings and corrected feedback/causal wording retained | Final integrated manuscript review; no reopening of approved sentences |
| F03/F05: reconstructable algorithm and allocator relationship | Diagram, Algorithm 1, 15-policy-plus-Oracle table, two allocation levels and model-specific feedback contract present | Exact historical adaptive execution/cadence must remain scoped to source evidence; an optional hook is not proof it executed |
| F04: contexts and learner settings | Primary/medium context and mechanism definitions; recovered original learners/settings and result-bound external catalogs | Correct the Paper8 source-notebook-versus-saved-model scope in the appendix; bind any claimed historical settings to their actual runs rather than asserting universal values |
| F06: physical grounding and threat semantics | q/A distinction, five-setting domain mapping and pinned medium processes present; 20 historical result records now have direct parameter/trajectory bindings | Incorporate recovered historical values only at that exact scope; unrecorded transition/default details are not inferred |
| F08/F09: reviewer-required medium case | Accepted 15-node/ten-route, five-model/five-threat, three-block, 75-cell campaign; evidence and six diagnostic views integrated | Medium-anchor work is complete. This does not say the whole proposed multi-point spectrum ran and does not authorize further runs |
| F10/Q07: diagnosis and scale interpretation | Analysis and independent reproduction accepted: PASS WITH REQUIRED CLAIM LIMITATIONS | Closed for existing-trace diagnosis. Historical 100-node cause remains a stated limitation, not an outstanding experiment assignment |
| Methods and evaluation accounting | 10,240 exported rows = 8,241 learned + 1,999 Oracle; winner units and modal-versus-mean distinction reconciled; unsupported bootstrap inference removed | Preserve these definitions through final editing; no numerical repair or new dataset is required by this sweep |
| F14: claim provenance | Claim matrix and primary/medium/external integration exist | Final artifact-level review must approve the integrated claims and current context corrections; this is no longer merely a planning task |
| F11: Reviewer B residual risk | Concern-to-response map exists with explicit simulator/hardware and evidence boundaries | Final independent/coauthor disposition of the remaining scoped issues, not a new hardware study |
| F13/F12: readability and submission | Journal candidate, five keywords, 173-word abstract and detailed supporting evidence present | 28-page retained build exceeds the 13-page initial limit; agree the permitted main-paper/supporting package, then build/layout review and human author/account/disclosure approval |

## Specific documentation issue confirmed, not guessed

`ICNP_VENUE_PREP/APPENDIX_ALGORITHM_SPECIFICATION.tex`, table
`tab:context_representation`, still labels Paper8 as eight-dimensional with one
action per path, and later exempts Paper8 from external-encoding holds. The
[original-source record](DATALAKE_RUN_BINDING_2026-10-23.md#external-context-catalogs-actual-model-evidence-recovered)
already distinguishes the notebook's declared construction from three
trajectory-bound GNeuralUCB Default/Baseline catalogs in base/rate-only/balanced
modes. Their action counts are `5,56,210,252,5,1,5,15`, with dimensions
`2,4,7,6,2,1,2,3`. The task tracker now reflects that distinction instead of
repeating a universal encoding claim. Exact manuscript wording remains an
approval/integration step; no scientific text is changed by this sweep.

The same evidence already records Paper2's bound G catalog and 330 Paper7 native
rows matched to original per-run result fields. The remaining 1,170 Paper7 row
associations are **not certified by that comparison**, not missing exported data
or inaccessible storage. All referenced primary exports reproduce. Preserve the
originals, the matched subset and the nonmatches; do not invent bindings.

## Status corrections made by this sweep

The task-level F08/F09/F10/F14 and compression status entries are brought into
agreement with their current top-level accepted status. Historical design and
decision records remain preserved. The source register no longer describes all
historical threat values as absent or Paper8 as a universally verified exception.
The advisor-facing README now points to this current disposition.

## Separate infrastructure follow-up

**Copy consolidation is complete; production routing to the four new component
roots is not deployed.** Existing writers/loaders still use the original root and
historical registries retain original IDs. A later bounded routing change needs
the existing CRISP-DM/OOP design gate and save/load compatibility tests. This is
not a reviewer requirement, missing-data finding, or authorization to change
experiment semantics. New producer writes will need a new manifest delta until
that cutover exists.

## Submission boundary and next action

The [official JSAC guidelines](https://www.comsoc.org/publications/journals/ieee-jsac/policies-guidelines),
rechecked October 23, still limit initial submissions to 13 pages including
references and appendices. The source-linked prior build is 28 pages; no new
compilation or submission occurred. Do not move evidence to an assumed exempt
supplement without confirming the target package.

Next bounded reviewer action: review and approve the specific F04 context-scope
correction using the already-recovered catalogs, then integrate scoped provenance
wording and complete the final reviewer/coauthor and venue checks. Do not restart
Q07, request another experiment, or treat minor rounding as a scientific blocker.

Original dirty GA, manuscript and framework checkouts remain preserved. Only
current status documentation and the existing validator record are updated;
GitHub publication and private evidence readback are recorded separately. Overleaf
receives GitHub changes when Piter performs the normal pull; no browser pull is
claimed here.
