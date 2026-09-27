# Medium-scale execution preparation — September 26, 2026

**State:** F-08 engineering preparation documented; scientific design and execution remain gated. No new routing experiment, F-09 campaign, F-10 diagnosis, or manuscript result was produced by this pass.

## Later September 26 scientific adjudication — proposed, not approved

**PROPOSED SCIENTIFIC CONTRACT — PITER APPROVAL REQUIRED BEFORE SUBSTANTIAL EXECUTION.** The proposed F-08 anchor is a controlled `layered-primary-form-v1` synthetic family: source → seven first-layer relays → six second-layer relays → destination (15 nodes), with ten distinct seeded three-hop routes covering every node. A fixed nine-qubit budget per route gives 90 total qubits and 55 within-route nonnegative integer allocations per route (550 route–action pairs). This intentionally holds hop count and per-route budget fixed; it is not a geometric-network realism result or a causal comparison with the four-route/35-qubit diamond. The historical fixture must stay byte/behavior equivalent. The matched Tier-2 proposal uses 7/4, 11/7, and 15/10 node/route members of the same family; 19/13 is deferred. Node and route counts co-vary; route overlap is a catalog descriptor, not a physical robustness mechanism in the current reward/mask model.

Preserve the primary implementation's route-local per-hop effective rates, `entanglement_success_factor=100` product-form expected payoff, within-route allocation actions, and selected-route availability gate. Assign **ten distinct three-hop rate profiles**, the unordered length-three multisets of the inherited `{1e-4,1.5e-4,2e-4}` parameter values, one per route by a frozen seeded rank. This avoids two identical arm types masquerading as ten meaningful choices; within-route heterogeneity is a disclosed medium extension, and all ten route maxima must be checked distinct. Shared graph edges do not currently impose shared rates, failures, or contention. The proposed run compares mask-aware privileged Oracle, CEpsilonGreedy, and explicit `EXPNeuralUCB(mode='hybrid')` across the **complete approved scenario set resolved from the canonical experiment configuration**; fixed `T_b,s=2` replay capacity 12,000; 6,000 frames; and three predeclared paired topology/scenario/model seed blocks. **No scenario count or subset is owned by the scale layer.** Scale and scenario are independent experimental axes. The launch manifest must materialize the resolved scenario IDs and parameters and derive total unit counts from that configuration. A block is complete only when every approved policy role has run under every resolved scenario for that block. If any configured scenario is not technically faithful, that is an explicit preflight hold/incomplete execution condition, not a reason to silently reduce the scenario axis. Three blocks are exploratory. The two learners have different internal update signals, so results compare configured implementations, not one isolated common-feedback algorithm. Pursuit-branch claims and broad policy-family rankings remain outside this slice pending code/provenance checks.

Two source discrepancies are now explicit preflight holds: current pursuit-named default configs use `mode='neural'` even though pursuit/informed branches use `cmab`/`icmab`, and the current manuscript's Bernoulli/`x` reward wording differs from the primary code's continuous accumulated payoff and `100*x` exponent. This record **does not amend manuscript claims or invalidate historical data**; reconcile data-producing provenance before new evidence is used in the paper. Disable performance-triggered retries/best-attempt selection, retain valid zero/poor runs, use domain-separated deterministic seeds rather than Python `hash`, and require exact config/topology/route/code/attempt hashes before reusing a completed run. The seed root must exclude later queue expansion so Tier-2 cells do not reseed existing Tier-1 identities. No exact mid-frame resume is claimed.

**Next engineering action:** implement the route-metadata-driven primary catalog/context/reward path and four-route plus 15-node/10-route invariant tests; then validate policy modes, masks, seeds, passive logs and completion identity. Piter/F-08 approval and passing technical preflight remain necessary before F-09 execution. F-10 remains separate.

## Authority and scope

The [Reviewer-C scale decision record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md#b-f-08--design-medium-scale--controlled-scale-spectrum-validation) remains the scientific authority. The required anchor is a primary-style topology around **15–20 nodes with at least ten distinct candidate routes**, preferably within an approved controlled routing-complexity spectrum. Heterogeneous external testbeds remain transfer evidence; node/path counts alone do not establish comparable scale semantics.

The [Quantum engineering record](https://github.com/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/docs/guides/MEDIUM_SCALE_EXECUTION_PREPARATION.md) identifies modules, tests, instrumentation, reproducibility, notebooks, and the technical preflight. Its code inspection is preparation for F-08/F-09, not approval of scientific settings or a change to validated manuscript claims.

## Current preparation findings

- The existing variable-size topology generators are useful building blocks. The Paper2 15-node/eight-path configuration is a candidate starting point, not an approved medium design.
- The default primary environment assigns action dimensions by route index and returns four reward lists. A metadata-driven route/action/reward generalization and preservation of the small-primary regression fixture are required before a ten-route primary-style run.
- Paper2 dummy single-action contexts and Paper8 one-action/eight-feature contexts must not silently replace the primary allocation-action semantics.
- Candidate route validation must reject missing, duplicate, invalid, or insufficient paths; allocation/action checks must enforce feasibility, budget conservation, dimensions, and reward/context alignment.
- Immutable raw logging needs topology/route identities, pre-decision observations, actions, actual outcome semantics, separate seed domains, attempt lineage, and completion hashes.
- Existing seed derivation, performance-dependent retry behavior, legacy resume identity, and live-progress interface require targeted qualification. The engineering record distinguishes observed source behavior from untested execution readiness.
- Minimal resume means exact hash-verified completed-run reuse and deterministic restart of an interrupted attempt. Exact mid-frame continuation is not established.

## F-08/F-09/F-10 status

| Item | Current state | Required next evidence |
|---|---|---|
| F-08 design | Engineering plan recorded; scientific manifest unresolved | Compatible topology/reward family, route-generation rule, controlled points, policy/threat/allocator/replay settings, seeds/horizon, metrics, interpretation rules, runtime budget and GO/RESIZE/STOP decisions |
| F-09 execution | Not started in this pass; held pending F-08 approval and technical preflight | Approved reproducible manifest, validated instrumentation and bounded runtime estimate before separate execution authorization |
| F-10 diagnosis | Separate later diagnostic tier; unchanged | Approved targeted diagnostics for broad 100-node compression; no causal claim from intuition or node count alone |

## Scientific decisions and next action

**SCIENTIFIC DECISIONS RESERVED FOR SOL:** exact topology and primary-style physical/reward semantics; candidate-route strategy and endpoints; scale-spectrum points; policy/threat subsets; allocator/update cadence and physical budget; replay semantics; seed count; horizon; retry/inclusion policy; metrics and uncertainty; Tier-1 breadth; Tier-2 expansion; scientific GO/RESIZE/STOP thresholds.

Next action: resolve that scientific manifest against the engineering findings, then implement the selected topology/action/logging path and run the documented regression → topology/action → trace/resume → bounded technical preflight sequence. F-09 execution requires its own go decision. Existing provenance holds for the deployed manuscript specification remain in force.

## Evidence and publication boundary

Execution source is `pzg8794/quantum_project`, `gcp-main`, inspected at `284746944e4ed4e3e95ae545925ff159d51dcc93`. Decision sources were recovered from this manuscript repository's `origin/main` at `07b1d47ce773f2be405cdee1d9f89ca264b05007`, rather than inferred from an older checkout. This is a public-safe engineering/status record. It adds no results, deployment claim, reviewer correspondence, or manuscript text.
