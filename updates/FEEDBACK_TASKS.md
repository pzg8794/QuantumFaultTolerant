# Reviewer-Feedback Execution Checklist

**Baseline date:** Thursday, August 27, 2026

**Execution model updated:** Thursday, September 10, 2026

**Current task:** F-08 — design the reviewer-required medium-scale validation as a controlled routing-complexity spectrum before any new runs

This is the detailed execution board behind the concise [advisor update](README.md). Tasks are ordered from the easiest ready manuscript work to the hardest evidence-producing work. Reviewer classification remains visible, but priority labels do not determine day-to-day order.

**Mandatory decision record for F-07/F-08/F-09/F-10/F-14:** Read [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md) before proposing or implementing changes. It preserves the May-23 submission boundary, the contribution-vs-finding distinction, the controlled scale-spectrum plan, and the claim-provenance workflow. Exact private reviewer wording remains outside this public repository.

## Working Rule

1. Select the **lowest-complexity unresolved task whose dependencies are met**.
2. The first revision wave is **manuscript-only**: rephrase, add, remove, reorganize, clarify, calibrate, and compress using the current manuscript, reviewer feedback, and already validated/documented evidence.
3. If resolving an item requires source-code inspection, configuration tracing, notebook execution, dataset analysis, debugging, or a new experiment, defer that portion to a later complexity tier and move to the next manuscript-only task.
4. Preserve the strengths already recognized by Reviewer A: controlled evaluation design, policy/allocator/capacity separation, cross-testbed evidence, and the capacity paradox. This is an operating rule, not a separate task.
5. Use Reviewer C's concrete requests as the primary conversion checklist.
6. Use Reviewer B as the final residual-risk audit after overlapping A/C work is complete.
7. Do not manufacture alternatives. Every proposed solution must independently satisfy the reviewer feedback and remain scientifically defensible. If only one defensible revision exists, present one.
8. For wording work, show the **complete current paragraph first**, isolate only the competing/problematic sentence(s), and then resolve **one sentence at a time**. Do not mix paragraph context, sentence identification, and replacement language.
9. Reassess each candidate sentence in the context created by already approved upstream changes. If an earlier surgical edit removes the competition or ambiguity, **do not rewrite an additional sentence merely because it was initially flagged**.
10. Do not edit the manuscript until the proposed wording is explicitly approved when the change affects scientific framing, contribution positioning, interpretation, or claim strength.
11. Add no new task unless it maps directly to documented reviewer feedback or an approved advisor/coauthor/venue requirement.

## Central-Contribution Strategy

The paper's primary contribution is the **controlled, threat-aware evaluation framework/methodology and the evidence revealed by that matched evaluation**. The evaluated bandit families are comparison objects and sources of findings; they are not the paper's claimed new contribution.

In the Abstract, Introduction, formal contribution list, and Conclusion, avoid wording that allows a winning bandit family to become the rhetorical center of the paper. When the same validated result can be stated equivalently, prefer wording that foregrounds what the framework exposes: performance gaps, discrepancies, tradeoffs, interactions, instability, failure modes, or evidence boundaries.

This does **not** prohibit reporting which policy performs best. Results and analysis may identify winners when scientifically relevant. The framing rule is narrower: high-level contribution language must make clear that those rankings are **findings produced by the framework**, not the reason the paper exists.

Preserve all validated numbers and scientific meaning. Reframing a comparison from the winner's perspective to the underperforming side or to the observed gap is acceptable when it expresses the same result; do not distort evidence merely to avoid naming a winner.

A sentence that names a strong policy is not automatically competing. Evaluate its rhetorical function in the full paragraph. If it primarily demonstrates a policy--allocator, policy--threat, or capacity--threat interaction that the controlled framework was designed to expose, it may reinforce the framework rather than compete with it.

## Feedback We Are Addressing

| Reviewer | What the reviewer recognized | Feedback that requires action | How it is used |
|---|---|---|---|
| A — Weak Accept / expert | Controlled evaluation design, policy–allocator–capacity factorization, external-testbed validation, and the capacity paradox | Clarify the central contribution; compress the narrative; reduce visible policy/table overload | Preserve the accepted scientific spine and make the methodology/evidence hierarchy unmistakable |
| C — Weak Reject / nonexpert | The matched-evaluation problem and controlled grid are meaningful | Improve reproducibility, algorithm specification, context definition, allocator semantics, physical grounding, and topology scale | Primary conversion checklist, beginning with manuscript-only clarification where possible |
| B — Reject / expert | Bandit benchmarking for quantum routing is potentially useful | Improve system-model clarity, algorithm definition, physical mapping, topology realism, and theoretical or real-world support | Residual-risk audit after A/C overlap is addressed |

The detailed source classification remains in the [August reviewer roadmap](../../../RESEARCH/RESEARCH/2026-08-04-icnp-review-classification-and-revision-roadmap.md). This checklist paraphrases the actionable feedback rather than reproducing private reviewer text.

## Easiest-to-Hardest Queue

The queue is complexity-based. **Anything requiring code, notebooks, datasets, or experiments is not part of the low-hanging-fruit manuscript pass.** Dependencies still override complexity where necessary.

| Order | ID | Complexity | Feedback focus | Status | Dependency |
|---:|---|---|---|---|---|
| 1 | F-02 | Low | Position the central contribution through surgical manuscript wording | **Done — independently reviewed, implemented, and build-validated** | None |
| 2 | F-07 | Low | Calibrate deployment/generalization claims using existing evidence | **Re-opened for source-correct adjudication; September candidate edits remain pending Piter approval** | None |
| 3 | F-13 | Low–Medium | Compress the main narrative without losing evidence | **Current; first pass complete** | F-02 |
| 4 | F-05 | Medium | Clarify allocator–policy semantics and expose the two-level allocation architecture | **APPROVED design direction; diagram/pseudocode/table implementation package pending; manuscript edit deferred to final batch** | None |
| 5 | F-06 | Medium | Improve threat-to-physics grounding with existing literature/documentation first | **APPROVED conceptual/scientific direction; exact simulator parameters/process rows provenance-pending; manuscript edit deferred to final batch** | None |
| 6 | F-03 | Medium | Specify the complete routing decision loop | **APPROVED jointly with F-05 at the design level; common Algorithm 1 package pending final artifact approval; manuscript edit deferred to final batch** | F-05 |
| 7 | F-04 | Medium | Document context and hyperparameters | **APPROVED conceptual/mechanism direction; exact validated-corpus hyperparameters provenance-pending; manuscript edit deferred to final batch** | F-03 |
| 8 | F-08 | High | Design reviewer-required medium-scale validation as a controlled routing-complexity spectrum | **Planned later; design must include 15–20 nodes and >=10 paths** | F-03–F-06 |
| 9 | F-09 | Very High | Run and validate the approved controlled scale spectrum | **Blocked by design** | F-08 approval and compute check |
| 10 | F-10 | Very High | Diagnose 100-node efficiency compression | **Planned later** | F-04, F-05, validated ablation plan |
| 11 | F-11 | Medium, dependency-late | Audit residual Reviewer B risk | **Blocked by earlier tasks** | F-02–F-10 |
| 12 | F-12 | Final integration | Complete venue and submission gates | **Ongoing/final** | Accepted revisions; JSAC primary and TNET backup confirmed |
| 13 | F-14 | Medium after evidence tasks | Build and audit the claim–evidence ladder / provenance matrix across Abstract → Conclusion | **Planned; starter taxonomy approved, final wording depends on F-09/F-10 evidence** | F-07 now; finalize after F-09/F-10 |

## Task Packages

### F-02 — Align the Central Contribution

- **Feedback addressed:** Reviewer A requests clearer contribution positioning. The August review classification records the required change as: state clearly that the primary novelty is the controlled evaluation methodology and the evidence it reveals, not an unsupported claim of a new bandit family. Reviewer C recognizes the controlled grid as a genuine evaluation-methodology contribution.
- **Problem:** High-level wording can allow a specific bandit family or winner to compete with the controlled framework for narrative priority even when the underlying science is correct.
- **Method:** Work section by section. Show the complete current paragraph, isolate only the competing sentence(s), and resolve one competing sentence at a time. Prefer the smallest wording change that restores the hierarchy: **framework → evidence/findings**, not **winning policy → central story**. After each approved change, reassess the remaining sentences in their new paragraph context before editing anything else.
- **Completion evidence:** Abstract, Introduction, formal contribution list, and Conclusion consistently present the controlled threat-aware evaluation as the paper's central contribution while retaining validated findings as evidence of what the framework reveals.

#### F-02.1 — Abstract competing sentence #1

**Current paragraph:**

> Quantum entanglement routing requires joint path selection and qubit allocation under noisy, nonstationary, and adversarial conditions. Existing approaches often assume stationary links, fixed allocation rules, or offline optimization assumptions. When these assumptions fail, routing can degrade end-to-end entanglement quality and waste scarce quantum resources. To address these limitations, we introduce a threat-aware evaluation framework for stochastic, contextual/neural, adversarial, predictive, and hybrid bandit policies for joint quantum path selection and qubit allocation. Unlike previous work that fixes allocator policy and replay semantics, we vary threat regime, allocator policy, and replay capacity as first-class factors, enabling attribution of robustness to the bandit-policy--allocator--capacity interaction. Across thirteen bandit policies and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points (pp) in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks. We also identify a capacity paradox: under \texttt{ThompsonSampling} allocation and $T_b$-type replay anchoring, mean OnlineAdaptive efficiency drops by 4.4 pp from $s{=}1$ to $s{=}1.5$, then recovers by 6.0 pp at $s{=}2$. Our cross-testbed evaluation on four external quantum-network testbeds confirms the main robustness trends while exposing scale- and topology-dependent limits. These results establish that context-aware neural policies paired with appropriate allocators provide deployment-grade robustness, while capacity scaling must be threat-matched to avoid predictability-induced collapse.

**Competing sentence #1 — Before:**

> Across thirteen bandit policies and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points (pp) in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks.

**Approved framing strategy:** Do not make the winning bandit family the subject of the high-level finding. The framework is the contribution, so report the discrepancy/failure-mode evidence that the framework exposes. A comparative result can be stated from the underperforming side or as a performance gap without changing the underlying evidence.

**Final approved solution — After:**

> Across thirteen bandit policies and five threat regimes, our controlled evaluation revealed 18--24 percentage-point (pp) scenario-aggregated efficiency deficits for non-contextual baselines relative to the leading policy family, identified configurations sustaining worst-case efficiency above 85\% under stochastic threats, and exposed greater instability in adversarial-first EXP3-style designs under adaptive attacks.

**Why this solution is approved:**

- It keeps the controlled evaluation as the grammatical and rhetorical source of all three findings.
- It preserves **all three findings from the original sentence**: the 18--24 pp efficiency difference, the above-85\% worst-case stochastic result, and the adaptive-attack instability result.
- It reports the first result from the underperforming side and refers to the comparator only as **the leading policy family**, avoiding repeated promotion of a named winning family.
- It converts the stochastic result into a configuration-level finding rather than a winner announcement while retaining the same >85\% evidence.
- It keeps the adversarial-first instability result as a failure mode exposed by matched evaluation.
- It therefore demonstrates the value of the framework through the discrepancies and behavior it reveals rather than making a particular bandit family appear to be the contribution.
- It is intentionally surgical and does not introduce a new scientific claim.

**Local-AI review outcome:** The local AI correctly identified that the earlier approved rewrite had dropped the >85\% stochastic finding and that its comparator wording was too implicit. Its initial correction repeatedly named neural hybrids, which would have partially restored the winner-centered narrative. The final wording accepts the evidence-preservation/precision critique while retaining the framework-centered strategy.

**Status:** **Final wording approved for manuscript implementation.**

#### F-02.2 — Abstract sentence initially flagged as competing

**Current sentence:**

> These results establish that context-aware neural policies paired with appropriate allocators provide deployment-grade robustness, while capacity scaling must be threat-matched to avoid predictability-induced collapse.

**Decision:** **Retain as written for F-02 contribution positioning.**

**Why:**

- In the original paragraph, immediately following a winner-centered sentence, this sentence could read as additional promotion of the same winning bandit family.
- After the approved F-02.1 reframing, its rhetorical function changes: it emphasizes that robustness depends on a **policy--allocator pairing** and that capacity must be **matched to the threat regime**.
- Those are exactly the multi-factor interactions the controlled framework was designed to evaluate, so the sentence now supports the framework rather than competing with it.
- No additional rewrite is justified under F-02 merely because the sentence names context-aware neural policies.
- The phrase **“deployment-grade robustness”** may still require separate review under F-07 claim calibration. That is a different reviewer issue and must not be mixed into F-02.

**Status:** **F-02 abstract review complete. No F-02 rewrite required for this sentence.**

#### F-02 Abstract — section status

**Contribution-positioning review:** **Complete.**

**Implementation result:** The final approved F-02.1 sentence was applied and the full revised Abstract was re-read and build-validated with all three findings intact.

**No other Abstract sentence is currently approved for modification under F-02.**

#### F-02.3 — Introduction findings-preview sentence

**Current paragraph:**

> To address this lack of a unified and controlled evaluation framework for quantum-routing strategies, we introduce a threat-aware evaluation framework that compares stochastic/contextual, adversarial, predictive, and hybrid bandit policies for joint path selection and qubit allocation under matched threat, allocator, and replay-capacity settings. The evaluation pipeline is summarized in \cref{fig:framework}. This evaluation provides practical guidance for designing quantum-network controllers that can maintain high entanglement efficiency and robustness under changing network conditions and adversarial disruptions. Across this controlled grid, pursuit--neural hybrids provide the strongest robustness--efficiency tradeoff, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.

**Competing sentence — Before:**

> Across this controlled grid, pursuit--neural hybrids provide the strongest robustness--efficiency tradeoff, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.

**Finding from paragraph-level review:** Reporting a family-level result in the Introduction is appropriate; the issue is not that the sentence previews a strong-performing family. The rhetorical question is whether the sentence makes that family the center of the paper rather than making it a finding produced by the controlled framework.

**Taxonomy finding:** The high-level distinction needed in the Introduction is **context-aware vs. non-context-aware**, not the narrower pursuit mechanism. Repository evidence explicitly distinguishes contextual pursuit models from **neural non-context baselines** and states that context-aware policies define the robustness frontier. Therefore, unqualified **neural hybrids** is too broad because the paper includes neural models that are not context-aware, while **pursuit--neural hybrids** is more mechanism-specific than necessary for this Introduction-level preview. The detailed pursuit lineage and named configurations remain for the Results section.

**Desired rhetorical hierarchy:**

> **controlled framework/evaluation → context-aware family-level finding → capacity-paradox interaction**

The Introduction should connect the controlled evaluation directly to the context-aware performance pattern without digging into pursuit-specific or model-specific details that belong in Results.

**Earlier working wording:**

> Across this controlled grid, our framework reveals neural hybrids as defining the strongest robustness--efficiency tier, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.

**SolM review outcome:** SolM agreed with the framework-first contribution hierarchy and identified one wording defect in the earlier construction: **“reveals neural hybrids as defining”** is rhetorically awkward because a family occupies a performance tier rather than defining it. This led to the improved empirical construction **“our evaluation identifies ... as occupying.”**

**Perplexity continuity review:** Perplexity then identified a substantive taxonomy nuance: the paper's tier/frontier language is consistently tied to contextual/pursuit-aware models, while the broader neural family also contains non-contextual neural baselines. A follow-up evidence check confirmed the exact archived taxonomy: contextual pursuit models outperform non-contextual baselines and separate from **neural non-context baselines**, while the paper states that **context-aware policies define the robustness frontier**. This makes **context-aware neural hybrids** the appropriate Introduction-level abstraction.

**Final approved solution — After:**

> Across this controlled grid, our evaluation identifies context-aware neural hybrids as occupying the strongest robustness--efficiency tier, while replay capacity exhibits a threat-dependent capacity paradox: additional capacity can improve structured-disruption performance yet reduce robustness under adaptive attacks.

**Why this solution is approved:**

- **Our evaluation** remains the grammatical and rhetorical source of the finding, preserving the framework-first contribution hierarchy.
- **Identifies** is measured empirical language and does not imply causal proof.
- **Context-aware** captures the scientifically meaningful distinction supported by the paper's own taxonomy and excludes neural non-context baselines from the claim.
- **Neural hybrids** retains a family-level abstraction suitable for the Introduction without naming the narrower pursuit mechanism.
- **Occupying the strongest robustness--efficiency tier** is consistent with the paper's established descriptive tier/frontier language once the family is correctly qualified as context-aware.
- The capacity-paradox clause remains unchanged and supplies a second interaction-level behavior exposed by the same controlled grid.
- Pursuit-specific and model-specific distinctions remain deferred to Results, where that granularity belongs.

**Independent review convergence:** SolM supports the framework-first construction and the use of **occupying** rather than **defining**; Perplexity independently confirmed that adding **context-aware** resolves the remaining overbreadth/continuity concern and issued **APPROVE F-02.3 INTRODUCTION** with no remaining scientific or rhetorical defect.

**Status:** **Final wording independently confirmed, implemented, and build-validated.**

#### F-02.4 — Formal contribution-list wording

**Deployment guidance — Before:**

> Pursuit--neural hybrids sustain $\geq$85\% worst-case efficiency while allocator choice induces 10--15 pp swings, requiring routing policy and qubit allocation to be selected jointly.

**Deployment guidance — Approved after:**

> Our controlled evaluation identifies context-aware neural hybrids as sustaining $\geq$85\% worst-case efficiency, while allocator choice induces 10--15 pp swings, requiring routing policy and qubit allocation to be selected jointly.

**Experimental findings — Before:**

> Pursuit--neural hybrids achieve 87--96\% efficiency, outperforming non-contextual baselines by 18--24 pp, and sustaining stability under strategic attacks.

**Experimental findings — Approved after:**

> Context-aware neural hybrids achieve 87--96\% efficiency, outperforming non-contextual baselines by 18--24 pp, and sustaining stability under strategic attacks.

**Independent review outcome:** The deployment wording was narrowed after review so it preserves the original $\geq$85\% evidence without adding an unsupported threshold claim about every non-contextual baseline. The experimental-finding wording retains the validated comparison while using the established context-aware family taxonomy.

**Status:** **Both formal contribution-list changes independently reviewed, approved, and implemented.**

#### F-02.5 — Framework-first Conclusion

**Before:** The live Conclusion moved directly from the joint-control result to a winner announcement, then presented adversarial fragility, the capacity paradox, deployment guidance, and external-testbed rankings as largely separate findings.

**Approved after:** The revised Conclusion follows the hierarchy **framework → within-tier hierarchy → adversarial failure mode → capacity interaction → deployment implication → external-testbed validation** while retaining the original model-level and numerical evidence.

**Independent review outcome:** The hierarchy and deployment continuation were approved after explicitly grounding fixed-deployment guidance in both the performance ranking and cross-threat robustness results. The external-testbed sentence was corrected from “extends the framework's matched evaluation across” to “extends the evaluation to” four additional testbeds so it does not imply that every external corpus uses an identical matched grid.

**Status:** **Full Conclusion independently reviewed, approved, and implemented.**

#### F-02 — Completion status

**Complete.** The Abstract, Introduction, formal contribution list, and Conclusion now consistently present the controlled threat-aware evaluation framework as the contribution and model rankings, failure modes, capacity interactions, deployment guidance, and cross-testbed behavior as findings it exposes.

### F-07 — Calibrate Claims to Demonstrated Evidence

- **Mandatory context:** Read [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md) first.
- **Feedback addressed:** Reviewers B and C question whether deployment and generalization language exceeds the tested topologies and simulators.
- **Historical source rule:** Reviewer C evaluated the May 23, 2026 submission-era manuscript (commit `b6ebe1daf8f41a285f4db31d43b98d5c22d1a353`), not the September revised draft. All reviewer interpretation must begin from that historical text, then compare it with current post-F-02 wording.
- **Problem:** The submitted manuscript repeatedly elevated a pursuit/context-aware neural **finding** into high-level robustness/generalization/deployment language, allowing that finding to compete with the paper's true contribution: the controlled evaluation framework.
- **F-02 interaction:** F-02 already repaired a substantial part of this problem by restoring the hierarchy **framework → evidence/findings**. Do not reopen F-02 merely because pursuit/context-aware configurations remain reportable findings.
- **Low-hanging pass:** Rephrase or bound claims using existing validated evidence and documented testbed limitations. Distinguish **primary matched evidence** from **heterogeneous external-testbed evidence** and from unestablished **hardware/deployment evidence**.
- **Later work if needed:** If a claim cannot be bounded satisfactorily without new evidence, defer that empirical question to F-08/F-09/F-10 rather than deleting the finding.
- **Completion evidence:** Abstract, Introduction, Results, Discussion, and Conclusion contain no unsupported scale/deployment claim and preserve a clear contribution-vs-finding hierarchy.
- **Evidence boundary:** The paper supports matched simulator evidence on the primary topology plus four heterogeneous external testbeds. It does not yet establish a controlled scale curve, hardware deployment, unrestricted topology transfer, a universal best allocator, or a causal mechanism for every observed effect.
- **Current adjudication rule:** September SolLight edits are implemented candidates, not automatically approved scientific framing. Review each item using: **exact private reviewer feedback → May-23 submission-era wording → current post-F-02 paragraph → exact sentence under review → possible solutions → recommended solution + reasoning → Piter APPROVE/REVISE/REJECT/DEFER**.
- **Status:** **Re-opened for source-correct adjudication.** F-07.1 wording has an approved direction, but each remaining item must pass the approval workflow before its status is finalized.


#### F-07.1A — Abstract external-testbed sentence

**Before:**

> Across four external quantum-network testbeds, the main performance hierarchy persists while scale- and topology-dependent limits become visible.

**Approved after:**

> Across four heterogeneous external quantum-network testbeds, the external evaluation identifies the same average-efficiency leader, although absolute efficiency, model separation, and configuration-level winners vary across testbeds.

**Decision:** **APPROVED BY PITER.**

**Why:** The external evidence supports the same average-efficiency leader across all four testbeds, but not an invariant full hierarchy or causal attribution of variation to topology/scale alone. The approved wording preserves Level III corroboration while leaving controlled scaling/causal diagnosis to F-08/F-09/F-10.

**Implementation rule:** Queue for the final batched F-07 manuscript edit. **Do not implement sentence-by-sentence.**

**Full provenance:** See [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md), section **F-07.1A — Final Piter adjudication**.


#### F-07.1B — Abstract primary-matched finding

**Before:**

> Within these evaluated simulator settings, context-aware neural policies paired with appropriate allocators achieve the strongest robustness, while replay-capacity effects remain threat-dependent.

**Approved after:**

> Within the primary matched evaluation, the strongest observed robustness--efficiency profiles are associated with context-aware neural policy--allocator configurations, while the effects of classical replay-memory scaling remain threat-dependent.

**Decision:** **APPROVED BY PITER.**

**Why:** The approved wording explicitly scopes the finding to Level I primary matched evidence, keeps the result multi-metric, avoids intrinsic/causal superiority language, makes policy--allocator interaction the comparison unit, and disambiguates classical replay memory from quantum hardware capacity.

**Implementation rule:** Queue for the final batched F-07 manuscript edit. **Do not implement sentence-by-sentence.**

**Full provenance:** See [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md), sections **F-07.1B terminology adjudication** and **F-07.1B — Final Piter adjudication**.


#### F-07.2A — Framework caption, first sentence

**Before:**

> Five matched inputs---topology, threat, policy, allocator, and replay---feed a shared evaluation grid to produce Oracle-normalized metrics, robustness comparisons, and deployment guidance.

**Approved after:**

> Five matched inputs---topology, threat, policy, allocator, and classical replay-memory setting---feed a shared evaluation grid to produce Oracle-normalized metrics, robustness comparisons, and configuration guidance for the evaluated simulator settings.

**Decision:** **APPROVED BY PITER.**

**Implementation rule:** Queue for the final batched F-07 edit. Synchronize the live caption, caption-lock reference, terminology shorthand, and figure-label consistency updates together. **Do not implement sentence-by-sentence.**

**Full provenance:** See [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md), section **F-07.2A — Framework caption, first sentence**.


#### F-07.2B — Framework caption, second sentence

**Before:**

> Matching all five inputs, simultaneously, exposes the policy--allocator--capacity interaction as the controlling robustness factor.

**Approved after:**

> Organizing these inputs in a shared matched grid enables controlled comparisons of measured robustness across bandit policies, allocator configurations, and classical replay-memory settings within common topology and threat conditions.

**Decision:** **SUPER APPROVED BY PITER.**

**Why:** Full source tracing confirmed the framework supports matched cross-factor comparisons, while the analysis does not formally estimate factorial interaction terms and does not establish a singular causal robustness controller. The approved wording states exactly the methodological capability established by the framework without overclaiming causality or statistical interaction estimation.

**Implementation rule:** Queue for the final batched F-07 manuscript edit. **Do not implement sentence-by-sentence.**

**Full provenance:** See [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md), section **F-07.2B — Final Piter adjudication**.


#### F-07.3A — Contribution label

**Before:** `Deployment guidance`

**Approved after:** `Configuration guidance`

**Decision:** **APPROVED BY PITER.** No additional independent-review round required because this is a direct application of the already-approved F-07.2A deployment-vs-configuration evidence boundary.

**Implementation rule:** Queue for the final batched F-07 manuscript edit. **Do not implement sentence-by-sentence.**

**Full provenance:** See [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md), section **F-07.3A — Final Piter adjudication**.

### F-13 — Compress the Main Narrative

- **Feedback addressed:** Reviewer A asks to reduce policy/table overload and make the main contribution easier to follow.
- **Problem:** Too many variants or detailed tables can obscure the contribution.
- **Low-hanging pass:** Remove repetition, tighten prose, improve transitions, and relocate secondary detail only when the existing evidence structure already supports doing so.
- **Guardrail:** Do not delete validated evidence merely to shorten the paper. Every removal or relocation receives before/after review.
- **Completion evidence:** A reader can identify the problem, controlled methodology, and principal findings quickly, while supporting evidence remains traceable.
- **First-pass work completed:** Tightened the Introduction framework/findings preview, removed repetitive cross-testbed synthesis, and compressed repeated model/testbed ranking prose in the Discussion while retaining the evidence pointers and all validated numerical findings.
- **Status:** **Current.** The first surgical compression pass is complete and reduced the compiled draft from 17 to 16 pages. A remaining paragraph-level sweep is still required before this task can be closed.

### F-05 — Clarify the Allocator–Policy Relationship

- **Feedback addressed:** Reviewers B and C ask how the allocator and bandit policy divide responsibility, how allocator choice changes feasible actions and feedback, and how the complete routing/allocation loop can be reconstructed.
- **Resolved architecture:** The allocator and bandit operate at two distinct levels. The allocator performs **inter-route budgeting**, assigning route-level budgets (T_r). Each (T_r) induces a feasible **within-route allocation-action** set (mathcal{X}_r(T_r)) and its reward landscape. The selected bandit model then applies its own algorithm to select a route and a within-route allocation action, observe threat-conditioned reward, and update its model state.
- **Source-backed model contract:** The shared `QuantumModel` architecture supports heterogeneous concrete policies while preserving the common route-selection -> within-route-action-selection -> feedback/update structure. Direct verification established, among others, GNeuralUCB = Simple-UCB + NeuralUCB; EXPNeuralUCB = EXP3 + NeuralUCB; EXPUCB = EXP3 + Linear-UCB; CPursuitNeuralUCB = Pursuit/CMAB + NeuralUCB; iCPursuitNeuralUCB = iCMAB/Pursuit + NeuralUCB with ARIMA/anomaly-aware reward filtering.
- **Allocator effect:** In the primary matched simulator, allocator-selected (T_r) values change both the feasible set (mathcal{X}_r(T_r)) and the reward landscape associated with those actions.
- **Approved revision package:** (1) hierarchical allocator--policy diagram; (2) common Algorithm 1 pseudocode; (3) complete policy-semantics table covering the validated policy corpus plus Oracle; (4) concise prose distinguishing inter-route budgeting from within-route allocation-action selection; (5) conditional feedback arrow from route statistics to the adaptive allocator hook.
- **Adaptive-hook rule:** Represent adaptation as **conditional**: “if allocator update is enabled and due at (t).” The existing 50-frame environment/state transition hook is not the allocator cadence. A configurable adaptive-allocator contract/cadence must be aligned before the pseudocode is finalized as executed-method text.
- **Implementation/alignment follow-up:** Define allocator-update cadence; regenerate (T_r)-dependent action/context/reward structures after reallocation; propagate them to every active model; verify every policy-table row against its concrete class; test the completed loop; preserve the existing validated corpus as the baseline.
- **Decision record:** See [F-05/F-03 Allocator--Policy Architecture Decision Record](F05_F03_ALLOCATOR_POLICY_ARCHITECTURE_DECISION_RECORD.md) for the complete reasoning path and approval provenance.
- **Status:** **APPROVED design direction. No manuscript edit yet; final artifacts remain queued for approval and the final batched manuscript pass.**

### F-06 — Map Threats to Quantum-Network Phenomena

- **Feedback addressed:** Reviewers B and C request physical motivation, parameter justification, and simulation-to-reality boundaries.
- **Resolved conceptual framing:** The five active settings form a **controlled progression in route-availability dependence and reactivity** layered on the probabilistic quantum-success process, not a universal escalation in physical threat severity.
- **Core model distinction:** The reward model separates probabilistic quantum success through \(q_r(\mathbf{x})\) from additional route availability through \(A_t(r)\). Baseline therefore means no added route-level availability disruption, not perfect hardware.
- **Approved five-setting interpretation:** Baseline = reference/no added unavailability; Stochastic = independent route disruption; Markov = temporally correlated/persistent disruption; Adaptive = routing-history-dependent targeting; OnlineAdaptive = continuously reactive targeting.
- **Approved manuscript package:** short taxonomy-rationale paragraph; five-row mapping table with availability process / controlled property / quantum-network interpretation / evidence boundary; explicit \(q_r(\mathbf{x})\) versus \(A_t(r)\) sentence; simulator-parameter boundary; excluded-scope statement.
- **Literature boundary:** Pant supports probabilistic/lossy quantum operation; Li supports node/edge/channel failure robustness; Satoh supports availability-attack motivation but not the exact adaptive rule; Zhang--Zhuang is an optional additional source distinguishing random breakdowns from intentional attacks.
- **Exact-parameter provenance gate:** Current `attack_strategy.py` does not match several manuscript parameter/process statements: current Markov is binary per-path with `p_stay=0.7`; Adaptive defaults to `adaptation_window=100` and `adaptation_strength=0.5`; OnlineAdaptive uses response delay/bursts/recent-path targeting rather than the manuscript's stated gamma/softmax rule. Do not copy either current defaults or manuscript values into the final table until the validated data-producing implementation/configuration is recovered.
- **Active-regime guardrail:** Keep exactly Baseline, Stochastic, Markov, Adaptive, OnlineAdaptive. Do not reintroduce historical `Targeted` without evidence that it belongs to the validated corpus.
- **Decision record:** See [F-06 Threat-Taxonomy Physical-Grounding Decision Record](F06_THREAT_TAXONOMY_PHYSICAL_GROUNDING_DECISION_RECORD.md) for the complete reasoning path, literature-role boundaries, and provenance requirements.
- **Status:** **APPROVED conceptual/scientific direction. Exact parameter/process cells remain provenance-pending. No manuscript edit yet; final insertion is deferred to the batched manuscript pass.**

### F-03 — Specify the Complete Routing Decision Loop

- **Feedback addressed:** Reviewers B and C request a reproducible end-to-end algorithm.
- **Problem:** Context construction, inter-route budgeting, route selection, within-route allocation-action selection, threat-conditioned feedback, replay, and update order are not reconstructable from one manuscript location.
- **Approved design:** F-03 is now coupled to the approved F-05 architecture. Algorithm 1 will express the shared model contract while leaving concrete path/action-selection and update behavior policy-specific.
- **Required Algorithm 1 elements:** primary/global physical-budget input; allocator initialization; (T_r); construction of (mathcal{X}_r(T_r)); context/reward construction; replay configuration; model initialization; model-specific route selection; model-specific within-route allocation-action selection; threat-conditioned reward; policy/replay/route-statistics updates; conditional allocator-update hook; regeneration and propagation of affected action/context/reward structures.
- **Policy-table requirement:** The companion semantics table must be verified row-by-row against the concrete classes represented in the validated corpus; no row may be inferred solely from family resemblance.
- **Decision record:** See [F-05/F-03 Allocator--Policy Architecture Decision Record](F05_F03_ALLOCATOR_POLICY_ARCHITECTURE_DECISION_RECORD.md).
- **Status:** **APPROVED jointly with F-05 at the design level. No manuscript edit yet; final diagram/pseudocode/table/prose package remains queued for approval and the final batched manuscript pass.**

### F-04 — Specify Context and Hyperparameters

- **Feedback addressed:** Reviewers B and C request concrete context/action definitions, dimensions, NeuralUCB architecture/training, Pursuit update semantics, predictive machinery, and reproducible settings.
- **Resolved primary representation:** For route r with h_r links and allocator-assigned budget T_r, the primary matched-evaluation context/action set is `X_r(T_r) = {x in Z_{>=0}^{h_r} : sum_l x_l = T_r}`. Two-hop primary routes therefore use 2-dimensional allocation vectors and three-hop routes use 3-dimensional allocation vectors.
- **Information-role boundary:** Route identity is structural through the route-specific learner/action set; hop count is implicit in h_r/vector dimension; threat availability affects reward feedback rather than being appended to the primary allocation vector; reward history enters learner/replay/update state rather than the instantaneous x.
- **External-context boundary:** Context construction is testbed-specific under a shared model contract. Paper8 currently uses one 8-dimensional path-feature vector per path and one within-path action per path; other external-testbed representations must be verified before insertion.
- **Verified NeuralUCB mechanism:** d_r -> 128 -> 1 ReLU network; learned reward score plus gradient-based confidence; replay-backed updates; Adam; MSE plus squared parameter-drift regularization; verified primary implementation trains after T>K using two 64-sample optimization steps per update. Scope this cadence to the verified implementation unless broader provenance is established.
- **Verified Pursuit mechanism:** uniform initial route probabilities; identify empirical-best arm; update `p_best <- p_best + alpha(1-p_best)` and `p_i <- p_i - alpha p_i` for other arms; sample the next arm from the resulting distribution.
- **Predictive mechanism:** use mechanism-level wording such as ARIMA-based predictive reward modeling with anomaly-aware filtering. Current code uses `auto_arima()` order search; fixed ARIMA(1,0,1) must not be presented as universal without data-producing provenance.
- **Approved manuscript package:** primary X_r(T_r) equation; scope-specific context table; NeuralUCB scoring/architecture/training description; Pursuit equation; integrated policy-semantics table; provenance-aware hyperparameter table; replacement of the current generic universal-context sentence.
- **Provenance rule:** distinguish (1) source-verified mechanism, (2) current-code default, and (3) validated-corpus value. Exact corpus-specific beta/lambda/lr/regularization, Pursuit alpha, predictive warmup/update/order/anomaly settings, replay settings, mode overrides, and testbed-specific overrides remain provenance-pending until tied to the data-producing commit/configuration.
- **NeuralTS guardrail:** do not add NeuralTS to the evaluated-policy table merely because the class exists; current validated-corpus audit does not include it among the evaluated non-Oracle policies.
- **Decision record:** See [F-04 Context and Hyperparameter Documentation Decision Record](F04_CONTEXT_HYPERPARAMETER_DECISION_RECORD.md) for the complete reasoning and S/C/P adjudication path.
- **Status:** **APPROVED conceptual/mechanism direction. Exact validated-corpus hyperparameter values remain provenance-pending. No manuscript edit yet; final insertion is deferred to the batched manuscript pass.**

### F-08 — Design Medium-Scale Validation as a Controlled Scale Spectrum

- **Mandatory context:** Read [Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record](REVIEWER_C_SCALE_CLAIM_DECISION_RECORD.md) first.
- **Feedback addressed:** Reviewers B and C question transfer beyond the small primary topology; Reviewer C specifically requests a primary-style medium-scale case around **15–20 nodes with 10+ candidate paths**.
- **Problem:** The existing 15/50/100-node external testbeds are valuable transfer evidence but are heterogeneous; they do not by themselves form a clean node-count scaling curve because topology, path structure, physics/modeling assumptions, and other semantics vary together.
- **Existing infrastructure clue:** The framework was designed to support variable topology/path sizes, and the existing Paper 2 configuration already provides a validated 15-node / 8-path starting point. F-08 must first determine whether that infrastructure can supply the reviewer-required >=10-path anchor without inventing an unnecessary new testbed.
- **Recommended design objective:** Build a **controlled routing-complexity spectrum**, not merely one checkbox medium-scale point. The mandatory reviewer anchor is 15–20 nodes / >=10 paths; additional small/intermediate/larger points should be included when feasible under comparable semantics.
- **Research question:** **How does the performance hierarchy exposed by the primary matched evaluation evolve as routing-space complexity increases?** Do not design the experiment to prove pursuit/context-aware neural configurations win.
- **Valid outcomes:** persistence, narrowing, reversal, threat-conditional ranking, changing allocator sensitivity, changing replay-capacity effects, or inconclusive behavior are all scientifically useful.
- **Approval gate:** Before execution, document topology family, node/path spectrum, reviewer anchor, threats/allocators/replay semantics, horizons/stopping criteria, metrics, seeds/repeats, compute-readiness, canonical config provenance, and interpretation rules.
- **Status:** Later experimental tier. Do not execute while manuscript-only reviewer fixes remain available.
- **Completion evidence:** Approved reproducible spectrum design with controls, metrics, seeds, stopping criteria, compute-readiness decision, and explicit reviewer-anchor coverage.

### F-09 — Run and Validate the Controlled Scale Spectrum

- **Feedback addressed:** Reviewers B and C request actual scale evidence.
- **Execution rule:** Run only the design approved under F-08. Do not substitute an ad hoc single experiment after approval.
- **Validation scope:** Preserve canonical configs, logs, datasets, plots, policy-family rankings, robustness floors, allocator sensitivity, replay-capacity behavior, regret/convergence where appropriate, and cross-scale pattern transitions.
- **Status:** Later experimental tier; blocked on F-08 approval.
- **Completion evidence:** Canonical validated evidence plus a bounded conclusion describing what persists, compresses, reverses, or remains unresolved across scale.

### F-10 — Diagnose the 100-Node Efficiency Compression

- **Mandatory interpretation:** Do not frame this as "why pursuit failed." The existing external result shows broad method compression on the 100-node testbed.
- **Feedback addressed:** Reviewers B and C need an explanation for the existing large-topology compression result.
- **Problem:** Heterogeneous testbed evidence cannot attribute the ~44.1% result to node count alone.
- **Candidate factors to separate:** convergence horizon, routing/path diversity, context/state complexity, allocator behavior, replay capacity, and topology/physics constraints.
- **Execution rule:** Use targeted validated diagnostics/ablations; do not replace evidence with intuitive causal storytelling.
- **Status:** Later experimental/diagnostic tier. Do not start while manuscript-only reviewer fixes remain available.
- **Completion evidence:** Validated ablations separate plausible factors, or the manuscript states precisely what remains unresolved.

### F-11 — Complete the Reviewer B Residual-Risk Audit

- **Feedback addressed:** Reviewer B's concerns about system clarity, algorithms, physical grounding, topology realism, and real-world support.
- **Problem:** Overlap with Reviewer C can conceal a B-only residual gap.
- **Execution rule:** Complete after the A/C-aligned revision and evidence tasks so the audit identifies only genuine residual risk rather than duplicating work.
- **Completion evidence:** Every B concern is resolved, bounded as a limitation, or assigned one approved residual action.

### F-12 — Complete Venue and Submission Integration

- **Feedback addressed:** Delivery gate for accepted revisions, not a new scientific claim.
- **Advisor decision:** Prepare for the [IEEE JSAC Quantum Series](../venues/jsac_quantum_series/SUBMISSION_CHECKLIST.md) as the primary target and [IEEE Transactions on Networking](../venues/tnet/SUBMISSION_CHECKLIST.md) as the backup.
- **Execution rule:** Keep venue/template/authorship/build requirements separate from scientific revision work and integrate only approved changes. Maintain TNET compatibility, but do not submit concurrently while JSAC is active.
- **Completion evidence:** The JSAC checklist passes for the primary submission; the TNET conversion checklist is ready if the primary route closes. Internal milestones are tracked in the [venue strategy](../venues/VENUE_STRATEGY.md).

### F-14 — Build the Claim–Evidence Ladder / Claim Provenance Matrix

- **Origin:** Approved follow-up from the F-07/Reviewer-C scale analysis. This task directly addresses the documented reviewer problem that submission-era wording blurred primary matched findings, external-testbed persistence, generalization, and deployment.
- **Problem:** A valid finding can become misleading when the manuscript does not make its evidence origin, scope, cross-testbed persistence, and boundary visible.
- **Starter taxonomy:**
  1. **Level I — Primary matched evidence:** controlled policy × threat × allocator × replay/capacity grid.
  2. **Level II — Controlled scale-spectrum evidence:** comparable experimental semantics across increasing routing complexity.
  3. **Level III — External cross-testbed evidence:** heterogeneous independently structured testbeds.
  4. **Level IV — Hardware/deployment evidence:** not currently established.
- **Required questions for every major claim:** What evidence produced it? At what scope? Did the pattern persist elsewhere? What changed with scale/topology? What does the evidence not establish?
- **Execution:** Build a living claim-provenance matrix now using existing evidence; finalize cross-scale claims only after F-09/F-10 evidence exists. Then audit Abstract → Introduction → Results → Discussion → Conclusion for the same evidence progression.
- **Target reader logic:** **controlled discovery → controlled scaling → external validation → diagnosis → bounded claim**.
- **Guardrail:** Policy-family winners remain findings produced by the framework; they do not become the paper's contribution merely because they are repeatedly named.
- **Status:** **Planned; starter taxonomy approved.**
- **Completion evidence:** Every major high-level claim is traceable to an evidence level and carries an explicit scope/boundary consistent across the manuscript.

## Current 10-Hour Work Block

Work through the manuscript-only queue first:

- [x] Establish contribution-positioning strategy for F-02.
- [x] Approve F-02.1 Abstract competing sentence #1.
- [x] Review F-02.1 with the local AI and incorporate the valid evidence-preservation/precision correction without restoring winner-centered framing.
- [x] Reassess F-02.2 in revised context; retain it for contribution positioning.
- [x] Complete F-02 Abstract contribution-positioning review.
- [x] Implement the single final approved Abstract sentence change and re-read the full Abstract.
- [x] Begin F-02 Introduction contribution-positioning review using the same paragraph-first, competing-sentence-only workflow.
- [x] Isolate the Introduction findings-preview sentence and establish the framework-centered, family-level framing strategy.
- [x] Obtain independent SolM review of the F-02.3 Introduction wording.
- [x] Resolve the taxonomy continuity issue by qualifying the family as **context-aware neural hybrids**.
- [x] Obtain final independent Perplexity approval of the context-aware F-02.3 wording.
- [x] Implement the final approved F-02.3 Introduction sentence.
- [x] Independently review and implement the two approved formal contribution-list changes.
- [x] Independently review and implement the approved framework-first Conclusion.
- [x] Build-validate the complete surgical F-02 implementation.
- [x] Complete the manuscript-only F-07 claim-calibration pass and build-validate the bounded wording.
- [x] Complete the first surgical F-13 compression pass without removing validated evidence.
- [x] Clarify the prose-level allocator--policy relationship for F-05 and record the exact source-tracing blocker.
- [x] Audit JSAC/TNET abstract, keyword, template, page, figure-format, account, and disclosure deltas.

Do **not** spend this first-pass time on code tracing, notebooks, datasets, new validation infrastructure, or experiments while manuscript-only reviewer fixes remain available.

## Evidence Drill-Down

Use existing evidence infrastructure only when a specific empirical statement requires checking:

- [Master Dataset Validation Hub](https://github.com/pzg8794/quantum_project/blob/gcp-main/docs/guides/MASTER_DATASET_VALIDATION_HUB_PLAN.md)
- [Detailed active working backlog](../ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md)
- [Completed feedback-resolution log](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Draft-wide audit checklist](../ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md)
- [Build validation log](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Primary JSAC Quantum Series checklist](../venues/jsac_quantum_series/SUBMISSION_CHECKLIST.md)
- [Backup TNET checklist](../venues/tnet/SUBMISSION_CHECKLIST.md)
- [Venue strategy and internal milestones](../venues/VENUE_STRATEGY.md)
