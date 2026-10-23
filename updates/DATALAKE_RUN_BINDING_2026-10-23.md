# Historical datalake run/context reconciliation — October 23, 2026

## Disposition

More of the requested evidence is present in the datalake than the earlier filename-index checks established. This pass reads actual preserved evaluator, runner and model objects through the existing loader, checks original bytes against provider size/MD5/SHA-256, and compares recorded results. It does not rerun a simulation, accepted Q07 analysis, or manuscript build. No manuscript text or original data changed.

## Shared-drive identity and full-directory recheck

### Later component consolidation — verified storage copies

Piter authorized four component drives with the existing Rochester/RIT Managers
and framework service-account Content manager, without public/domain sharing:

| Component | Consolidated copy | Unique files verified |
|---|---|---:|
| Notebooks | [ai_quantum_notebooks](https://drive.google.com/drive/folders/0AGbQ6E7AidVNUk9PVA) | 192 |
| Framework state/support | [ai_quantum_framework_state](https://drive.google.com/drive/folders/0AMEB9SU4Raw3Uk9PVA) | 4,627 |
| Model state | [ai_quantum_model_state](https://drive.google.com/drive/folders/0AIxNGjMWQME3Uk9PVA) | 15,305 |
| Execution logs | [ai_quantum_logs](https://drive.google.com/drive/folders/0AEPPet33IkCtUk9PVA) | 650 |

The copy represents 21,659 original source identities with 20,774 unique files
and 885 exact-content aliases. Original filenames/paths, source IDs and checksums
remain recorded; different contents are not merged. Fresh destination size,
SHA-256 and MD5 readback passes for every file. All four permission lists match
the approved three members. The current original component inventory has no
added/removed/changed files during the closing comparison. Originals were retained.

The [private consolidation record](https://drive.google.com/drive/folders/1d7T-9kOTbC0n45gvw4tPWMlNFO4IC-9B)
contains source/destination inventories, receipts, code, 21 passing positive/negative
tests and `SOURCE_LOCATION_REGISTER.json`, including 181 explicit Paper7
source-to-copy mappings. `SOURCE_MANIFEST.json` SHA-256:
`12fedbf89a29f0f78385c5b57bf2216a2d64bc3cbb4e577584527ab41b1dfbce`.
The existing Validation Hub now names both original Drive roots, the local log and
notebook sources, and all four new destinations and validates this copy record.
The [published Validation Hub](https://github.com/pzg8794/quantum_project/blob/5967bbd01737307f45c45f8afd8d8b11a6127089/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb)
preserves all 141 prior cells and adds the source-register and executed component
validation cells. The same notebook bytes are published on `gcp-main` and mirrored
to the notebooks component drive under `notebooks/current/`.

This is **completed component-copy consolidation**, not production-loader cutover
or a new scientific run-binding result. Existing writers/loaders remain configured
to their previous root; historical registries retain original IDs. No manuscript,
experiment, Q07 acceptance or the source-to-export comparisons below were changed.
Files outside the four requested components remain at their registered sources.

### Earlier source-recovery snapshot

The configured source is the owner's [ai_quantum_project shared drive](https://drive.google.com/drive/folders/0AK0VchnNyM-xUk9PVA). A fresh, explicitly drive-scoped enumeration returned 20,779 live items across 46 complete pages. All 94 original objects read in the preceding run-binding pass are in this exact drive and retain their recorded SHA-256 checksums. The enumeration includes 4,058 Paper7-related objects; none has an ID absent from the previous expanded inventory.

The source paths are `quantum_data_lake/framework_state/` and `quantum_data_lake/model_state/`. The general account-based Drive connector and the framework's authorized service-account connection have different visibility. The framework connection successfully reads this drive. Its `in_share_drive=False` setting on the Mac selects API retrieval rather than a mounted Colab workspace; it does not select a different remote root.

The twelve short-run Paper7 aggregate objects each expose one retained Drive revision. The expanded per-experiment check reads all 387 current Paper7 runner objects whose names identify observation horizons of 50, 100, 150, 200 or 250 frames, across every allocator, using exact provider IDs and byte checksums. The resulting 330 matched native rows and 1,170 unmatched rows describe this source-to-export comparison, not missing files or an inaccessible datalake. The unmatched count must not be presented as evidence that no corresponding source exists anywhere in the archive.

The exact query, root/ancestry checks, revision IDs, candidate results and targeted Validation Hub receipt are retained with the existing private source evidence. No storage root, source object, experiment or manuscript is changed by this check.

## Local logs and saved notebooks: required source coverage

The owner identified organized local experiment logs and saved notebook outputs as additional evidence. The source search must cover these alongside stored experiment and learner objects. The read-only follow-up finds 77 Paper7 text logs across the local log tree and two Paper7 notebooks, including the organized `Paper7-Testbed-Results` folder. Before mirroring, 21 logs had identical bytes in the current shared-drive listing; the other 56 local paths represented 50 distinct contents absent from that listing. Both notebooks match their existing GitHub versions and need no duplicate publication.

The audit parses 4,991 recorded learned-model reward lines under their allocator, scenario, experiment number, frame horizon and replay scale. There are 84 individual native-row reward matches at logged precision, but no complete four-learned-model reward vector matches under all those keys. Individual coincident values are not substituted for complete run identity. These logs are useful historical evidence, including seed, attack-rate, capacity and setup-allocation records; this comparison does not certify an unrecorded within-episode allocator cadence or a complete learner configuration.

The saved output of **both** Paper7 notebooks refers to historical shared-drive ID `0APT9hcMpvuHYUk9PVA`. In cell 3, output 0 (zero-based), line 53 says `Looking for 'backup_registry.json' in Drive folder: 0APT9hcMpvuHYUk9PVA`; line 39 records `/content/drive/Shareddrives/ai_quantum_computing/quantum_data_lake`. The initial 404s came from connections without access. **The access problem is corrected:** the signed-in Rochester account can read the historical drive, as can its existing archived framework service connection. No new permissions were granted. The full historical-root API enumeration returns 483 live items across two pages, including 22 Paper7 aggregate objects representing 20 distinct contents; thirteen of those contents are absent from the current-root inventory. The earlier access-unresolved statement is superseded by this verified recovery.

The historical [framework-state folder](https://drive.google.com/drive/u/4/folders/19HqR0SnAC-LidQtyAvvIAY8Gl1MH8vxq) and [model-state folder](https://drive.google.com/drive/u/4/folders/1NPWB7X-ir2m_ym4GC137FmdYRUBDs4rw) remain valid sources. `HISTORICAL_DRIVE_INVENTORY_2026-10-23.json` pins the original file IDs and provider hashes; `HISTORICAL_PAPER7_SOURCE_CHECK_2026-10-23.json` records actual downloads, strict original loading, extracted result rows and native-export comparisons. Python 3.13's `pathlib._local` serialization name is mapped to the concrete standard-library `pathlib` module on the local Python 3.12 reader; no dummy classes or scientific algorithm substitutions are allowed. Original objects are unchanged. The temporary authentication copy is excluded from evidence and removed after retrieval.

**Actual validation result:** all 22 historical Paper7 object identities are accounted for: 20 distinct payloads were downloaded, checksum-verified and strictly loaded; two duplicate objects have identical provider hashes to those payloads. The established exporter recovers 1,965 model-result rows. They span 4,000–12,000 frames and do not match the native 50–250-frame export; all 60 allocator/source-slice endpoint comparisons report zero complete row matches. Three historical backup registries were also read and hash-verified and contain no Paper7 references. This closes the historical-drive access/search gap and identifies thirteen distinct Paper7 contents absent from the current-root inventory. It does not replace the native dataset or falsely close its remaining exact-run associations. The prior 330 matched native result rows remain valid.

The notebook sources are already published at the verified framework commit `5e4c2602ee51eb9fc0a0318dab115cfdb545c699`:

- [Paper7 notebook](https://github.com/pzg8794/quantum_project/blob/5e4c2602ee51eb9fc0a0318dab115cfdb545c699/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper7.ipynb), SHA-256 `0ad4fa14ab51df39e26a7aba71ad88d2bfbf76a118bf38e2e0809b9a053738eb`.
- [Standardized Paper7 notebook](https://github.com/pzg8794/quantum_project/blob/5e4c2602ee51eb9fc0a0318dab115cfdb545c699/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper7-StandardizedRunConfig.ipynb), SHA-256 `8fbb7263bcdec0b8045dbd55effa5d8ec939eebed0da3021cfb744b635d6aebd`.

**Preservation completed:** all 77 local log paths now have downloaded-byte-verified shared-drive counterparts. Fifty missing unique log contents were uploaded under the existing `quantum_logs` area; identical contents were reused with alias mappings. Existing different files were never overwritten; same-name conflicts use a documented `local-snapshots-20261023` child. The organized [Paper7 log folder](https://drive.google.com/drive/folders/1lqZXpNKlrj2mcpiF4IzBTwTRV-ooZlr3) and the full path-to-file-ID map in `PAPER7_LOCAL_LOG_MIRROR_2026-10-23.json` preserve retrieval. Permissions were not changed.

The source register and Validation Hub explicitly list the current and historical roots, exact notebook references/hashes, local logs and mirror status. `PAPER7_SOURCE_LOCATION_REGISTER_2026-10-23.json` is retained with the other source receipts; the notebook distinguishes recovered access, verified original bytes and actual source-to-export comparisons. It does not treat a directory listing or a checksum alone as a result match.

**Required discovery behavior:** use the retained local log inventory, exact notebook revisions and both authenticated Drive roots before declaring evidence unavailable. A 404 from one account is not an absence check. Keep row-level source comparisons separate from directory access and mirror coverage. Do not reopen accepted Q07 analysis or generate replacement experiments merely because a historical association is not established.

## Historical threat settings: direct result bindings recovered

Four original Default-allocator first-experiment runners at 4000 frames match the five-run primary evaluator's complete reward, regret and route/action trajectories for all five models. This is **20 matched result records, including 16 learned-policy records**, not a filename-only association.

| Historical setting | Fields actually serialized in the matched runner |
|---|---|
| Stochastic | attack rate `0.0625` |
| Markov | attack rate `0.25`; `k_attacks=1`; transition and initial-distribution overrides stored as `None` |
| Adaptive | attack rate `0.25`; sticky probability `0.7`; memory window `50` |
| OnlineAdaptive | attack rate `0.25`; sticky probability `0.7`; memory window `50`; `k=1`; decay and temperature overrides stored as `None` |

These values belong to the identified historical Default/five-run/first-experiment source, not every historical run or the accepted medium campaign. Null overrides do not reveal the unrecorded generator default; do not infer an exact transition matrix, decay coefficient or softmax rule from them. This closes the broad claim that no historical threat-parameter evidence is available, while keeping the remaining process-specific boundary explicit.

The separately checked Dynamic runner contains allocator state but was not trajectory-bound to the inspected evaluator results. Its empty allocation-history field does not prove a universal execution cadence or that reallocation never occurred. Do not use it to manufacture a cadence statement.

## Paper7: original result backing recovered for 330 rows

The original per-experiment objects preserve evidence that the later same-name aggregate snapshots did not reproduce. Seventy identified fifteen-route Random-runner originals were checked without excluding nonmatching candidates. **66 of 75 Random experiment groups, covering 330 of the native export's 1500 rows,** have matching:

- the complete five-model frame/reward/regret/average-reward vector;
- original experiment ID and threat label;
- topology metadata, declared context catalog and reward catalog.

The contexts in those source records contain fifteen declared three-feature route vectors, consistent with the export. These are original configuration metadata, not automatically the effective catalog consumed by every learner. Runtime/winner summaries and every exporter column are not certified by this narrower result-field comparison. The original and native files remain unchanged; no rows are removed or pooled with Q07.

**Remaining precise Paper7 boundary:** 45 Random rows and 1125 Default/Dynamic/Thompson rows are not bound by this recovered subset. None of the 50 retained five-model result maps checked in the inspected Default aggregate contains the target first-Baseline five-model result vector. This is not a claim that all original Paper7 data are missing: a substantial original-backed subset is now identified, and the preserved export remains available.

## External context catalogs: actual model evidence recovered

Three original Paper8 GNeuralUCB snapshots match all three complete trajectories and final rewards of their Default/Baseline results in the base, rate-only and balanced source modes. Their **saved model catalogs** contain eight route-specific sets with:

- action counts: `5, 56, 210, 252, 5, 1, 5, 15`;
- feature dimensions: `2, 4, 7, 6, 2, 1, 2, 3`.

They are not eight-dimensional, one-action-per-route catalogs. The source notebook's declared eight-feature construction and the saved learner's catalog are distinct evidence objects; their equivalence must not be assumed. The current appendix's Paper8 row and its exemption from historical encoding holds require scoped wording review. This is a concrete documentation issue, not evidence that validated numerical results are invalid or that another experiment is required.

A Paper2 GNeuralUCB snapshot also matches the complete trajectories of its identified Default/Baseline result and contains eight one-action, one-feature route sets. The checked Paper12 and Paper7 model candidates did not match the selected original result trajectories; their saved shapes are retained as nonmatching candidates, not promoted to those runs.

**Recommended next wording adjudication, not implemented:** distinguish source-notebook constructions from trajectory-bound saved model catalogs; remove the unsupported universal Paper8 encoding exception; describe verified catalogs with their exact policy/mode/allocator/scenario scope. Preserve remaining unverified links explicitly. No manuscript approval is inferred from this source check.

## Newly published source-master scope

The newly published source-master file is provider-checksum verified and passes its pinned revision check. That specific revision enumerates nine artifacts and 335 experiment contexts; it is not a manifest of every historical manuscript source. Its raw-original references and the older datalake objects remain separate from the accepted medium evidence. No preparation pipeline or shared implementation was modified in this pass.

## Evidence, validation and unchanged gates

Exact object IDs, byte checksums, full trajectory hashes, all matching/nonmatching candidates, source-master revision, scripts and Validation Hub outputs are retained in the existing [original-source evidence area](https://drive.google.com/drive/folders/16-y5VdX7JWc6OdMuGIXF0H-s6FeZJBWV). The established Validation Hub remains the canonical job/evidence record; this is not a replacement validator or storage system.

Q07/F10 existing-trace acceptance remains closed with its required claim limits. Historical 100-node causality is not inferred. No new experiment is required by this source recovery. Final manuscript integration approval, journal length and human submission fields remain separate gates.
