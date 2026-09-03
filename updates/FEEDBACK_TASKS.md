# Reviewer-Feedback Execution Checklist

**Baseline date:** Thursday, August 27, 2026

**Execution model updated:** Thursday, September 3, 2026

**Current task:** F-02 — align the central contribution

This is the detailed execution board behind the concise [advisor update](README.md). Tasks are ordered from the easiest ready manuscript work to the hardest evidence-producing work. Reviewer classification remains visible, but priority labels do not determine day-to-day order.

## Working Rule

1. Select the **lowest-complexity unresolved task whose dependencies are met**.
2. The first revision wave is **manuscript-only**: rephrase, add, remove, reorganize, clarify, calibrate, and compress using the current manuscript, reviewer feedback, and already validated/documented evidence.
3. If resolving an item requires source-code inspection, configuration tracing, notebook execution, dataset analysis, debugging, or a new experiment, defer that portion to a later complexity tier and move to the next manuscript-only task.
4. Preserve the strengths already recognized by Reviewer A: controlled evaluation design, policy/allocator/capacity separation, cross-testbed evidence, and the capacity paradox. This is an operating rule, not a separate task.
5. Use Reviewer C's concrete requests as the primary conversion checklist.
6. Use Reviewer B as the final residual-risk audit after overlapping A/C work is complete.
7. Do not manufacture alternatives. Every proposed solution must independently satisfy the reviewer feedback and remain scientifically defensible. If only one defensible revision exists, present one.
8. For wording work, show the **complete current paragraph first**, isolate only the competing/problematic sentence(s), and then resolve **one sentence at a time**. Do not mix paragraph context, sentence identification, and replacement language.
9. Do not edit the manuscript until the proposed wording is explicitly approved when the change affects scientific framing, contribution positioning, interpretation, or claim strength.
10. Add no new task unless it maps directly to documented reviewer feedback or an approved advisor/coauthor/venue requirement.

## Central-Contribution Strategy

The paper's primary contribution is the **controlled, threat-aware evaluation framework/methodology and the evidence revealed by that matched evaluation**. The evaluated bandit families are comparison objects and sources of findings; they are not the paper's claimed new contribution.

In the Abstract, Introduction, formal contribution list, and Conclusion, avoid wording that allows a winning bandit family to become the rhetorical center of the paper. When the same validated result can be stated equivalently, prefer wording that foregrounds what the framework exposes: performance gaps, discrepancies, tradeoffs, interactions, instability, failure modes, or evidence boundaries.

This does **not** prohibit reporting which policy performs best. Results and analysis may identify winners when scientifically relevant. The framing rule is narrower: high-level contribution language must make clear that those rankings are **findings produced by the framework**, not the reason the paper exists.

Preserve all validated numbers and scientific meaning. Reframing a comparison from the winner's perspective to the underperforming side or to the observed gap is acceptable when it expresses the same result; do not distort evidence merely to avoid naming a winner.

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
| 1 | F-02 | Low | Position the central contribution through surgical manuscript wording | **In progress** | None |
| 2 | F-07 | Low | Calibrate deployment/generalization claims using existing evidence | **Queued** | None |
| 3 | F-13 | Low–Medium | Compress the main narrative without losing evidence | **Queued** | F-02 |
| 4 | F-05 | Low if prose-sufficient; later otherwise | Clarify allocator–policy semantics from already documented material | **Queued** | None |
| 5 | F-06 | Medium | Improve threat-to-physics grounding with existing literature/documentation first | **Planned** | None |
| 6 | F-03 | Medium if implementation verification is required | Specify the complete routing decision loop | **Deferred from low-hanging pass if code tracing is required** | F-05 |
| 7 | F-04 | Medium | Document context and hyperparameters | **Deferred from low-hanging pass if config/code tracing is required** | F-03 |
| 8 | F-08 | High | Design medium-scale validation | **Planned later** | F-03–F-06 |
| 9 | F-09 | Very High | Run and validate medium-scale experiment | **Blocked by design** | F-08 approval and compute check |
| 10 | F-10 | Very High | Diagnose 100-node efficiency compression | **Planned later** | F-04, F-05, validated ablation plan |
| 11 | F-11 | Medium, dependency-late | Audit residual Reviewer B risk | **Blocked by earlier tasks** | F-02–F-10 |
| 12 | F-12 | Final integration | Complete venue and submission gates | **Ongoing/final** | Accepted revisions and venue confirmation |

## Task Packages

### F-02 — Align the Central Contribution

- **Feedback addressed:** Reviewer A requests clearer contribution positioning. The August review classification records the required change as: state clearly that the primary novelty is the controlled evaluation methodology and the evidence it reveals, not an unsupported claim of a new bandit family. Reviewer C recognizes the controlled grid as a genuine evaluation-methodology contribution.
- **Problem:** High-level wording can allow a specific bandit family or winner to compete with the controlled framework for narrative priority even when the underlying science is correct.
- **Method:** Work section by section. Show the complete current paragraph, isolate only the competing sentence(s), and resolve one competing sentence at a time. Prefer the smallest wording change that restores the hierarchy: **framework → evidence/findings**, not **winning policy → central story**.
- **Completion evidence:** Abstract, Introduction, formal contribution list, and Conclusion consistently present the controlled threat-aware evaluation as the paper's central contribution while retaining validated findings as evidence of what the framework reveals.

#### F-02.1 — Abstract competing sentence #1

**Current paragraph:**

> Quantum entanglement routing requires joint path selection and qubit allocation under noisy, nonstationary, and adversarial conditions. Existing approaches often assume stationary links, fixed allocation rules, or offline optimization assumptions. When these assumptions fail, routing can degrade end-to-end entanglement quality and waste scarce quantum resources. To address these limitations, we introduce a threat-aware evaluation framework for stochastic, contextual/neural, adversarial, predictive, and hybrid bandit policies for joint quantum path selection and qubit allocation. Unlike previous work that fixes allocator policy and replay semantics, we vary threat regime, allocator policy, and replay capacity as first-class factors, enabling attribution of robustness to the bandit-policy--allocator--capacity interaction. Across thirteen bandit policies and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points (pp) in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks. We also identify a capacity paradox: under \texttt{ThompsonSampling} allocation and $T_b$-type replay anchoring, mean OnlineAdaptive efficiency drops by 4.4 pp from $s{=}1$ to $s{=}1.5$, then recovers by 6.0 pp at $s{=}2$. Our cross-testbed evaluation on four external quantum-network testbeds confirms the main robustness trends while exposing scale- and topology-dependent limits. These results establish that context-aware neural policies paired with appropriate allocators provide deployment-grade robustness, while capacity scaling must be threat-matched to avoid predictability-induced collapse.

**Competing sentence #1 — Before:**

> Across thirteen bandit policies and five threat regimes, neural hybrids outperform non-contextual baselines by 18--24 percentage points (pp) in scenario-aggregated efficiency, sustain worst-case efficiency above 85\% under stochastic threats, and remain more stable than adversarial-first EXP3-style designs under adaptive attacks.

**Approved framing strategy:** Do not make the winning bandit family the subject of the high-level finding. The framework is the contribution, so report the discrepancy/failure-mode evidence that the framework exposes. A comparative result can be stated from the underperforming side or as a performance gap without changing the underlying evidence.

**Approved solution — After:**

> Across thirteen bandit policies and five threat regimes, our controlled evaluation revealed 18--24 percentage-point (pp) performance gaps associated with non-contextual baselines in scenario-aggregated efficiency, while adversarial-first EXP3-style designs exhibited greater instability under adaptive attacks.

**Why this solution is approved:**

- It keeps the controlled evaluation as the source of the finding.
- It removes the winning bandit family from the rhetorical foreground instead of merely moving its name later in the sentence.
- It preserves the validated 18--24 pp comparative evidence by expressing the result as a performance gap rather than as a winner announcement.
- It preserves the adaptive-attack instability finding without turning an alternative policy family into the paper's central contribution.
- It makes the empirical evidence demonstrate the value of the framework: the framework exposes meaningful performance discrepancies and failure modes across matched conditions.
- It is intentionally surgical. It does not rewrite the surrounding abstract or introduce a new scientific claim.

**Status:** **Approved for manuscript implementation.**

#### F-02.2 — Abstract competing sentence #2

**Before:**

> These results establish that context-aware neural policies paired with appropriate allocators provide deployment-grade robustness, while capacity scaling must be threat-matched to avoid predictability-induced collapse.

**Status:** **Next for review. No replacement approved yet.**

### F-07 — Calibrate Claims to Demonstrated Evidence

- **Feedback addressed:** Reviewers B and C question whether deployment and generalization language exceeds the tested topologies and simulators.
- **Problem:** A valid controlled result can still be overstated as unrestricted scalability or real-world deployment proof.
- **Low-hanging pass:** Rephrase or bound claims using existing validated evidence and documented testbed limitations. Do not create a new validation exercise merely to edit wording.
- **Later work if needed:** If a claim cannot be bounded satisfactorily without new evidence, defer that claim to the experimental tier.
- **Completion evidence:** Abstract, Introduction, Discussion, and Conclusion contain no unsupported scale or deployment claim.

### F-13 — Compress the Main Narrative

- **Feedback addressed:** Reviewer A asks to reduce policy/table overload and make the main contribution easier to follow.
- **Problem:** Too many variants or detailed tables can obscure the contribution.
- **Low-hanging pass:** Remove repetition, tighten prose, improve transitions, and relocate secondary detail only when the existing evidence structure already supports doing so.
- **Guardrail:** Do not delete validated evidence merely to shorten the paper. Every removal or relocation receives before/after review.
- **Completion evidence:** A reader can identify the problem, controlled methodology, and principal findings quickly, while supporting evidence remains traceable.

### F-05 — Clarify the Allocator–Policy Relationship

- **Feedback addressed:** Reviewers B and C ask when allocation occurs and how it changes actions and feedback.
- **Problem:** Execution order and ownership of allocation decisions may be ambiguous in the prose.
- **Low-hanging pass:** First determine whether the relationship can be clarified accurately from the manuscript and existing documentation alone. If yes, fix the prose now.
- **Defer condition:** If accurate resolution requires implementation tracing or code inspection, stop and move that portion to a later complexity tier.
- **Completion evidence:** The manuscript explains the relationship accurately without unsupported implementation claims.

### F-06 — Map Threats to Quantum-Network Phenomena

- **Feedback addressed:** Reviewers B and C request physical motivation, parameter justification, and simulation-to-reality boundaries.
- **Problem:** Controlled regimes may be mistaken for literal physical attack models.
- **First pass:** Use existing cited literature and documented rationale to improve wording, analogues, and limitations without new experiments.
- **Later work if needed:** Any unresolved parameter or mechanism requiring new technical validation is deferred.
- **Completion evidence:** Each regime is appropriately motivated and bounded without overstating the simulator.

### F-03 — Specify the Complete Routing Decision Loop

- **Feedback addressed:** Reviewers B and C request a reproducible end-to-end algorithm.
- **Problem:** Context construction, route selection, allocation, feedback, replay, and update order may not be reconstructable from one location.
- **Execution rule:** This is manuscript-low-hanging only to the extent that the loop is already documented authoritatively. If source-code verification is required, it is deferred from the first revision wave.
- **Completion evidence:** The final loop can be followed without source code and is eventually verified against implementation provenance.

### F-04 — Specify Context and Hyperparameters

- **Feedback addressed:** Reviewers B and C request feature definitions, dimensions, preprocessing, missing-value behavior, cadence, and model settings.
- **Problem:** Reproduction is impossible when inputs and settings are implicit.
- **Execution rule:** Add only settings already established in authoritative documentation during the manuscript pass. Any configuration/code tracing belongs to the later technical tier.
- **Completion evidence:** Final feature/configuration descriptions are complete and traceable.

### F-08 — Design Medium-Scale Validation

- **Feedback addressed:** Reviewers B and C question transfer beyond the small topology.
- **Problem:** Existing evidence may not fully answer the scale question.
- **Status:** Later experimental tier. Do not work on this while manuscript-only reviewer fixes remain available.
- **Completion evidence:** Approved reproducible design with controls, metrics, seeds, stopping criteria, and compute-readiness decision.

### F-09 — Run and Validate the Medium-Scale Experiment

- **Feedback addressed:** Reviewers B and C request actual scale evidence.
- **Status:** Later experimental tier; blocked on F-08 approval.
- **Completion evidence:** Canonical logs, validation, plots, configuration provenance, and a bounded cross-scale conclusion.

### F-10 — Diagnose the 100-Node Efficiency Compression

- **Feedback addressed:** Reviewers B and C need an explanation for the existing large-topology compression result.
- **Status:** Later experimental/diagnostic tier. Do not start while manuscript-only reviewer fixes remain available.
- **Completion evidence:** Validated ablations separate the plausible factors, or the manuscript states precisely what remains unresolved.

### F-11 — Complete the Reviewer B Residual-Risk Audit

- **Feedback addressed:** Reviewer B's concerns about system clarity, algorithms, physical grounding, topology realism, and real-world support.
- **Problem:** Overlap with Reviewer C can conceal a B-only residual gap.
- **Execution rule:** Complete after the A/C-aligned revision and evidence tasks so the audit identifies only genuine residual risk rather than duplicating work.
- **Completion evidence:** Every B concern is resolved, bounded as a limitation, or assigned one approved residual action.

### F-12 — Complete Venue and Submission Integration

- **Feedback addressed:** Delivery gate for accepted revisions, not a new scientific claim.
- **Execution rule:** Keep venue/template/anonymity/build requirements separate from scientific revision work and integrate only approved changes.
- **Completion evidence:** Required gates in the [CCWC checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md) pass, subject to venue confirmation.

## Current 10-Hour Work Block

Work through the manuscript-only queue first:

- [x] Establish contribution-positioning strategy for F-02.
- [x] Approve F-02.1 abstract competing sentence #1.
- [ ] Resolve F-02.2 abstract competing sentence #2.
- [ ] Continue identifying and resolving contribution-competing language section by section.
- [ ] Move next to the easiest remaining manuscript-only reviewer task.

Do **not** spend this first-pass time on code tracing, notebooks, datasets, new validation infrastructure, or experiments while manuscript-only reviewer fixes remain available.

## Evidence Drill-Down

Use existing evidence infrastructure only when a specific empirical statement requires checking:

- [Master Dataset Validation Hub](https://github.com/pzg8794/quantum_project/blob/gcp-main/docs/guides/MASTER_DATASET_VALIDATION_HUB_PLAN.md)
- [Detailed active working backlog](../ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md)
- [Completed feedback-resolution log](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Draft-wide audit checklist](../ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md)
- [Build validation log](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Working venue checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md)
