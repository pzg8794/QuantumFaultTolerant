# Historical datalake run/context reconciliation — October 23, 2026

## Disposition

More of the requested evidence is present in the datalake than the earlier filename-index checks established. This pass reads actual preserved evaluator, runner and model objects through the existing loader, checks original bytes against provider size/MD5/SHA-256, and compares recorded results. It does not rerun a simulation, accepted Q07 analysis, or manuscript build. No manuscript text or original data changed.

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
