# F-14 review 01 — Topology scope in Limitations

**Status:** PROPOSED — awaiting Piter's exact wording decision.

**Owner:** `ICNP_VENUE_PREP/FUTURE_WORK.tex`, Limitations paragraph.

**Parent task:** [F-14 claim–evidence integration](F14_CLAIM_EVIDENCE_INTEGRATION_2026-10-18.md).

**Scope:** One problematic sentence; all other sentences remain unchanged at this step.

## 1. Reviewer requirement

Reviewer C #4 requested at least one 15–20-node topology with ten or more candidate paths in a primary-style evaluation and challenged the scope of deployment/generalization claims. The reviewer explicitly knew of the external 100-node testbed. The issue is the scope of matched evidence, not a claim that the entire framework only supports four nodes.

The accepted medium campaign now satisfies the requested node/path anchor with 15 nodes and ten routes. The manuscript must identify that evidence without presenting heterogeneous experiments as a controlled node-count curve.

## 2. Issue and evidence boundary

The current sentence says **all experiments** use a 4-node, 4-path internal topology. That description excludes both the four external testbeds and the accepted medium campaign. It must be narrowed to the primary matched grid.

The accepted medium campaign supports 15 nodes, ten routes, 550 feasible route/action pairs, Default/fixed allocation, five models, five threats, three blocks, and 6,000 frames per cell. It does not supply an allocator/replay sweep or isolate node count as the cause of a performance change. The four external testbeds remain heterogeneous evidence. This correction preserves the primary design and does not reopen F-02.

Evidence: Sol `SOL_REPRODUCTION_REPORT.md`, sections Source identity, Methods, and G; Astra `SOURCE_AUDIT.md`; the [accepted source status](EVALUATION_SOURCE_STATUS_2026-10-04.md). Exact package identities are in the parent matrix.

## 3. Complete current paragraph

The following is the live uncommented paragraph, copied verbatim. The owning file SHA-256 is `fe1021b3f6edddf8d9665fdd24ca02578f219d3254ef2e45986283989164b96d`; its bytes match origin/main at `0bcc913bc5a28b1e1116245cf692989a9ec98aae`.

```tex
The main limitations of this study are \textit{topology scale}, \textit{testbed fidelity}, \textit{replay-capacity} coverage, and \textit{forecasting scope}. While these constraints enable rigorous controlled experiments, they bound the generality of results and motivate validation across larger, more heterogeneous quantum-network testbeds. \textit{First}, all experiments use a controlled 4-node, 4-path internal topology with mid-range horizons, which enables clean attribution of algorithm, allocator, and replay-capacity effects but may not capture behavior in larger or more heterogeneous quantum-network testbeds. \textit{Second}, the current software-defined testbeds abstract away control-plane latency, node-level scheduling delays, memory contention, and timing-dependent decoherence effects, so deployment-level conclusions require further validation across higher-fidelity and more diverse testbeds. \textit{Third}, replay capacity is evaluated using two anchoring rules (\texttt{Tb}, \texttt{T}) and three scale factors ($s \in \{1,1.5,2\}$), which exposes the \texttt{capacity paradox} and motivates broader tail-risk characterization at larger horizons and topologies. \textit{Lastly}, predictive context currently uses ARIMA-based forecasting; more expressive temporal models (\eg RNNs and Transformers) with calibrated uncertainty quantification remain future work.
```

## 4. Exact sentence and proposed replacement

**Before:**

```tex
\textit{First}, all experiments use a controlled 4-node, 4-path internal topology with mid-range horizons, which enables clean attribution of algorithm, allocator, and replay-capacity effects but may not capture behavior in larger or more heterogeneous quantum-network testbeds.
```

**Recommended after:**

```tex
\textit{First}, the primary matched policy--allocator--replay grid uses a controlled 4-node, 4-path topology; a separate Default/fixed campaign evaluates a 15-node topology with ten candidate routes, each providing 55 feasible within-route allocation actions (550 route/action pairs in total). Together with the four heterogeneous external testbeds, these evaluations delimit the observed findings but do not establish a controlled node-count scaling curve.
```

## 5. Recommendation and reasoning

Recommend this replacement. It identifies each evidence scope, retains the role of the controlled primary grid, and adds the completed medium anchor without suggesting that the medium run repeats every allocator/replay combination. It also states the limit of the scale comparison at the point where the reader needs it.

Replacing only “all experiments” with “the primary experiments” would correct the narrow factual error but leave the completed medium evidence absent from the limitation. No alternative is manufactured merely for style.

The 550 count is the total catalog across ten routes, not 550 actions per route. The proposed wording explicitly preserves the ten route-specific sets of 55 actions and their total denominator.

## 6. Decision and application gate

Piter: **APPROVE**, **REVISE**, **REJECT / RESTORE**, or **DEFER** this exact replacement.

After approval, apply this sentence only, re-read the complete paragraph, add the medium methods/results references during task 2, compile the assembled manuscript, and record validation. Do not treat this proposal or its commit as manuscript approval. The other limitation sentences and future-work commitments require their own review if subsequent integration reveals a real conflict.

The current task commits the integration plan and review package. The manuscript remains untouched until the exact wording is approved under FEEDBACK_TASKS.md Working Rule 10.
