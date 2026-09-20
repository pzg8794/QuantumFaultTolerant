# Reviewer-C Scale, Claim-Scope, and Evidence-Ladder Decision Record

**Status:** Canonical public handoff for all agents working on the post-ICNP revision  
**Date:** 2026-09-19  
**Applies to:** F-07, F-08, F-09, F-10, and F-14  
**Primary manuscript:** `ICNP_2026_venue_draft.tex`  
**Primary contribution:** the controlled, threat-aware evaluation framework/methodology and the evidence it reveals

> **Mandatory source boundary:** Do not use the current September manuscript to infer what the ICNP reviewers saw. The relevant submission-era source is the May 23, 2026 repository state at commit `b6ebe1daf8f41a285f4db31d43b98d5c22d1a353`. The reviewer text itself is private correspondence and is not reproduced in this public repository. The exact wording is preserved in the private Drive record titled **"PRIVATE — QuantumFaultTolerant Reviewer-C Scale & Claim Decision Record — 2026-09-19."**

## Why this record exists

This decision emerged during the F-07 claim-calibration review when Piter re-read Reviewer C's scale criticism and noticed a crucial word: the reviewer criticized the **primary evaluation**, not the entire framework or every testbed.

That observation led to a source-grounded reconstruction:

1. Re-read the exact July 3, 2026 ICNP reviewer feedback for submission #330.
2. Reconstructed the actual May 23 submission-era manuscript from commit `b6ebe1d`.
3. Re-checked the framework/testbed design and validated cross-testbed evidence.
4. Compared the submission-era rhetoric with the post-F-02 contribution framing.
5. Identified that the submission had allowed a **pursuit/context-aware neural finding** to compete rhetorically with the paper's true contribution: the **controlled evaluation framework**.

The assistant initially made a provenance mistake by using the current revised manuscript to explain an earlier reviewer comment. Piter caught that immediately. All subsequent reasoning was rebuilt against the historical submission snapshot. Future agents must preserve this historical-version discipline.

## What Reviewer C's scale criticism means

**Private source:** ICNP 2026 Review #330C, July 3 decision email, weakness concerning primary-topology scale and the breadth of the pursuit-neural/deployment claim.

Public paraphrase of the reviewer's ask:

- the **primary matched evaluation** uses a 4-node diamond with 4 candidate paths;
- the reviewer regarded that as too small to support broad robustness/deployment claims;
- the reviewer explicitly considered the external 100-node result, so this was **not** a claim that the paper had no larger testbeds;
- the reviewer requested at least one **medium-scale primary-style evaluation** around 15–20 nodes with 10+ paths;
- the reviewer also asked for explanation of the substantial efficiency compression on the 100-node external testbed.

Therefore, the correct distinction is:

**primary matched evidence != heterogeneous external-testbed evidence != hardware/deployment validation**

## What the reviewer actually saw in the May submission

The May 23 submission-era draft repeatedly elevated pursuit-neural results into high-level contribution/generalization/deployment language.

Examples from the public historical source include:

> "Across this controlled grid, pursuit--neural hybrids provide the strongest robustness--efficiency tradeoff..."

The formal contribution list included:

> "Deployment guidance: Pursuit--neural hybrids sustain >=85% worst-case efficiency..."

and:

> "Experimental findings: Pursuit--neural hybrids achieve 87--96% efficiency..."

The Abstract ended with:

> "These results establish that context-aware neural policies paired with appropriate allocators provide deployment-grade robustness..."

Submission-era Discussion/cross-testbed language also described pursuit-informed neural designs as defining the strongest frontier, generalizing beyond the primary network, and defining the overall performance ceiling.

This language explains why Reviewer C reasonably treated pursuit-neural performance as a central claim rather than merely one finding produced by the framework.

## Core interpretation

The paper's contribution is **not** "pursuit algorithms are best."

The paper's contribution is the **controlled threat-aware evaluation framework** that compares policy families under matched threat, allocator, replay-capacity, and routing conditions and reveals when performance is robust, fragile, conditional, or configuration-dependent.

The strong pursuit/context-aware neural performance is a **finding produced by the framework**.

That finding is still scientifically important and should be tested more rigorously. It should not be deleted merely because the original rhetoric overstated it.

## Why F-02 already solved a substantial part of the problem

F-02 restored the correct contribution hierarchy:

- high-level contribution language now centers the controlled evaluation;
- policy-family rankings remain reportable findings;
- the Abstract/Introduction no longer need to read as though pursuit algorithms are the reason the paper exists.

This is a structural correction, not cosmetic wording cleanup.

F-02 does **not** eliminate the scale question. It changes the question from:

> "Can we prove pursuit-neural is deployment-grade?"

to:

> "How does the performance hierarchy exposed by the framework evolve as routing-space complexity changes?"

That is the correct framework-centered research question.

---

# A. F-07 — Claim calibration

## Problem / feedback

The submission used language that jumped from observed simulator results to broader robustness/generalization/deployment claims.

## Possible solution 1: remove pursuit/context-aware findings entirely

**Not recommended.**

Reason: this would discard validated empirical results. The reviewer challenged claim breadth and missing scale evidence, not the existence of the observed ranking.

## Possible solution 2: keep the same pursuit-centered claims and only add qualifiers

Example: add "within the evaluated simulator settings" everywhere.

**Insufficient by itself.**

Reason: it bounds the words but can still leave a winning policy family as the rhetorical center of the paper.

## Recommended solution

- Keep F-02 framework-first contribution positioning.
- Treat policy rankings as **findings**.
- Bound each finding to the evidence level that produced it.
- Distinguish primary matched findings from external-testbed persistence.
- Remove unsupported deployment/hardware/unrestricted-transfer language.
- Avoid universal "appropriate/best allocator" prescriptions.
- Preserve validated values unless a separate evidence audit changes them.

### Current F-07.1 approved wording direction

> "Within these evaluated simulator settings, the strongest observed robustness occurs among context-aware neural policy–allocator configurations, while replay-capacity effects remain threat-dependent."

### Reasoning

This reports an observed configuration-level result without converting it into a new algorithmic contribution or deployment guarantee.

### Follow-up

The surrounding Abstract transition must clearly distinguish:
1. what the primary matched grid establishes, and
2. what the external testbeds show persists or changes.

Removing the phrase "deployment-grade" alone is not enough if the evidence transition remains ambiguous.

---


## Independent review log — Perplexity

**Review stage:** F-07 Abstract transition, independent review before Piter adjudication.

**Outcome:**
- **Sentence 1 — APPROVE.** Perplexity agreed that replacing `persists` with wording that says the hierarchy `remains visible` while absolute efficiency and model separation vary with topology better communicates the external-testbed evidence without implying stable effect magnitude.
- **Sentence 2 — APPROVE scientifically, pending Piter adjudication before implementation.** Perplexity agreed that `Within the primary matched evaluation...` fixes all three identified defects in the live sentence: vague `appropriate allocators`, intrinsic-sounding `achieve the strongest robustness`, and ambiguous `these evaluated simulator settings`.
- Perplexity initially issued **DEFER** on Sentence 2 because the repository still preserved the earlier approved direction. After process clarification, it withdrew that DEFER and accepted that the repository mismatch is an expected artifact of active re-adjudication, not a scientific defect.
- Perplexity also agreed that `the strongest observed robustness occurs among...` is preferable to the more natural `configurations occupy...` because the former keeps the **finding**, rather than the policy family, as the grammatical subject and is therefore more consistent with the F-02 framework-first rhetorical discipline.
- Perplexity accepted the refined interpretation of `persists`: the problem is not that the word necessarily asserts magnitude stability, but that it permits an overly strong reading when the evidence shows substantial compression in absolute efficiency/model separation.
- Perplexity endorsed the manuscript-adjacent interpretation: topology-dependent degradation does not invalidate the framework contribution; it demonstrates why robustness claims require evaluation across multiple operating and complexity regimes.

**Process lesson preserved:** During active wording adjudication, a mismatch between the previously recorded candidate and a newly reviewed candidate should be flagged for provenance, but it should not downgrade the scientific verdict. The canonical record and manuscript are updated only after Piter's explicit approval.

**Current independent-review state:**
- Sentence 1: **APPROVE**
- Sentence 2: **APPROVE scientifically; pending Piter adjudication**
- No manuscript or canonical wording update is authorized by this review alone.

---


## Independent review log — Copilot

**Review stage:** F-07 Abstract transition, independent review before Piter adjudication.

**Overall outcome:** Copilot approves the revision strategy, F-02 contribution-vs-finding distinction, Level I–IV evidence taxonomy, and controlled scale-spectrum plan. It raises two substantive wording refinements for the Abstract.

### Sentence 1 — REVISE

Candidate reviewed:

> "Across four external quantum-network testbeds, the observed performance hierarchy remains visible, although absolute efficiency and model separation vary substantially with topology."

Copilot's valid concerns:
- **"performance hierarchy"** may imply a fuller stable ranking than the external evidence cleanly establishes;
- **"vary substantially with topology"** risks attributing the differences to topology alone even though the external testbeds are heterogeneous in topology, path structure, modeling/physics assumptions, horizons, and other settings.

Evidence check:
- The validated external table shows that **iCPursuitNeuralUCB has the highest average efficiency on all four external testbeds**.
- The ordering and configuration-level win structure below that leader are not invariant; on Paper 8, for example, EXPNeuralUCB has more individual configuration wins.
- Therefore, a claim about a **leading average-efficiency pattern** is better supported than an unrestricted "performance hierarchy" claim.
- Differences should be described as varying **across heterogeneous testbeds**, not causally "with topology" unless a controlled analysis isolates topology.

**Adjudication:** ACCEPT Copilot's concern. Do not automatically adopt its exact replacement yet; carry the issue forward for comparison with other independent reviewers.

### Sentence 2 — REVISE concern accepted; Copilot replacement not adopted

Candidate reviewed:

> "Within the primary matched evaluation, the strongest observed robustness occurs among context-aware neural policy–allocator configurations, while replay-capacity effects remain threat-dependent."

Copilot's valid concern:
- **"robustness"** is broad and could benefit from clearer metric/evidence meaning.

Copilot suggested:
> "In the primary matched evaluation, context-aware neural policy–allocator configurations show the strongest observed robustness..."

and, conditionally, a worst-case-efficiency version.

**Why those exact replacements are not accepted at this stage:**
- Putting **context-aware neural policy–allocator configurations** back in subject position partially reverses the F-02 rhetorical discipline that keeps the finding rather than the winner as the grammatical center.
- Reducing "robustness" to **highest observed worst-case efficiency** is not automatically supported as the intended aggregate claim: the validated RQ2 evidence distinguishes best average efficiency from strongest robustness floor (for example, iCEpsilonGreedy has the strongest floor in the locked adversarial scope while CPursuit leads average efficiency).
- The manuscript's existing high-level claim is closer to a **robustness–efficiency / efficiency–stability profile** than to one single floor metric.

**Adjudication:** ACCEPT the precision concern, but REJECT Copilot's exact replacement as premature. Keep Sentence 2 open for a wording that preserves:
1. explicit **primary matched evaluation** provenance;
2. finding-centered grammar;
3. the correct multi-metric meaning of robustness;
4. the threat-dependent replay-capacity finding.

### Additional design feedback accepted

- Level II must remain explicitly **planned evidence**, not something the manuscript implies already exists.
- Level III supports qualitative/cross-testbed persistence, not causal explanation of the 100-node compression.
- F-08 must control or explicitly track multiple complexity dimensions (node count, candidate-path count, path overlap, context dimensionality, topology structure) so the scale spectrum does not become another heterogeneous-testbed comparison.
- F-10 remains correctly separate from the controlled scale curve.

**Current independent-review state after Copilot:**
- Sentence 1: **REVISE**
- Sentence 2: **REVISE concern accepted; exact replacement unresolved**
- No manuscript change authorized until Piter adjudicates after the independent-review round.

---


### Copilot follow-up confirmation

Copilot accepted the adjudication of its review without further objection:

- Sentence 1 remains **REVISE** to avoid over-attributing external variation to topology and overstating persistence of a complete hierarchy.
- Sentence 2 remains **REVISE** to improve the precision of the robustness wording while preserving F-02 finding-centered grammar and the multi-metric interpretation.
- The Level I–IV evidence taxonomy, controlled scale-spectrum plan, and separate F-10 diagnostic remain supported.
- No manuscript edits are authorized yet.

This closes the Copilot review cycle for this wording package pending Piter's final cross-review adjudication.

---

# B. F-08 — Design medium-scale / controlled scale-spectrum validation

## Problem / feedback

Reviewer C asks for a medium-scale primary-style topology around 15–20 nodes with 10+ candidate paths. Reviewers B/C both question how well the primary findings transfer beyond the small matched topology.

## Existing evidence/infrastructure

The framework was designed so node count and path count are not simply hardcoded as one fixed 4-node case. Existing validated external configurations include approximately:

- Paper 2: 15 nodes / 8 paths;
- Paper 7: 50 nodes / 15 paths;
- Paper 12: 100 nodes / 4 paths.

These external testbeds are scientifically useful but **not a clean node-count scaling curve**, because topology, physics/modeling assumptions, path structure, and other semantics change together.

## Possible solution 1: add one brand-new 15–20 node topology

**Valid but limited.**

It meets the minimum reviewer request but provides only one additional point.

## Possible solution 2: reuse the existing 15-node Paper 2 topology and increase to >=10 paths

**Potentially efficient, subject to design validation.**

It leverages validated infrastructure but still risks becoming only a small-vs-medium comparison.

## Recommended solution

Design a **controlled scale spectrum** within one compatible topology-generation/testbed family, including a mandatory 15–20-node / >=10-path anchor that directly satisfies Reviewer C.

The research question is:

> **How does the performance hierarchy exposed by the primary matched evaluation evolve as routing-space complexity increases?**

This design must be able to reveal persistence, compression, reversal, conditionality, or changing allocator/replay sensitivity.

### F-08 approval requirements

Before any execution, specify:

- compatible topology family;
- node/path-count spectrum;
- reviewer-required medium-scale anchor;
- matched threats/allocators/replay semantics;
- horizons/stopping criteria;
- metrics;
- seeds/repeats;
- compute/readiness estimate;
- canonical config provenance;
- predeclared interpretation rules for persistence/compression/reversal/inconclusive results.

No F-09 execution before F-08 approval.

---

# C. F-09 — Run and validate the controlled scale spectrum

## Problem / feedback

The reviewers need actual scale evidence, not just an architectural statement that the framework can support larger graphs.

## Possible solution

Run only a single medium-scale point.

## Recommended solution

Run the approved F-08 spectrum, with the reviewer-required medium-scale point included, and validate:

- canonical configs;
- logs;
- datasets;
- plots;
- policy-family ranking;
- robustness floors;
- allocator sensitivity;
- replay-capacity behavior;
- regret/convergence where appropriate;
- cross-scale pattern transitions.

## Reasoning

This directly addresses the reviewer and produces richer scientific evidence than a one-off checkbox experiment.

---

# D. F-10 — Diagnose the 100-node efficiency compression

## Problem / feedback

Reviewer C highlighted the existing ~44.1% result on the 100-node external topology and asked why performance compresses so substantially.

## Critical interpretation rule

Do **not** frame this as "why pursuit failed."

The existing cross-testbed evidence indicates broad method compression on that testbed.

## Possible solution 1: explain the result from intuition

**Rejected.**

The current experiments do not isolate a mechanism.

## Recommended solution

Run targeted diagnostics/ablations that separate plausible factors, such as:

- convergence horizon;
- routing/path diversity;
- context/state complexity;
- allocator behavior;
- replay capacity;
- topology/physics constraints.

If the evidence cannot isolate one mechanism, state precisely what remains unresolved.

## Reasoning

This turns a rhetorical vulnerability into a bounded, evidence-backed scale finding.

---

# E. F-14 — Claim–evidence ladder / provenance matrix

## Problem

The ICNP submission blurred:

**primary matched result -> external persistence -> generalization -> deployment**

That made a policy-family finding look like a central algorithmic/deployment claim.

## Possible solution 1: add one limitations paragraph

**Insufficient.**

Readers encounter claims throughout the paper.

## Possible solution 2: revise only Abstract and Conclusion

**Insufficient.**

Results/Discussion transitions can still collapse evidence levels.

## Recommended solution

Maintain a claim-provenance matrix and audit the full narrative:

**Abstract -> Introduction -> Results -> Discussion -> Conclusion**

### Evidence levels

**Level I — Primary matched evidence**  
Controlled policy x threat x allocator x replay/capacity grid.

**Level II — Controlled scale-spectrum evidence**  
Comparable experimental semantics across increasing routing complexity.

**Level III — External cross-testbed evidence**  
Heterogeneous independently structured testbeds.

**Level IV — Hardware/deployment evidence**  
Not currently established.

### Questions every major claim must answer

1. What evidence produced it?
2. At what scope?
3. Did the pattern persist elsewhere?
4. What changed with scale/topology?
5. What does the evidence not establish?

### Starter matrix

| Claim | Evidence origin | Current scope | Follow-up / boundary |
|---|---|---|---|
| Context-aware information is associated with stronger robustness | Primary matched grid | Primary + external observations | Exact scale dependence to be mapped; simulator evidence only |
| Allocator choice materially changes robustness | Matched allocator comparisons | Primary + selected external configurations | No universal best allocator |
| Replay-capacity effects are threat-dependent | Matched replay/capacity experiments | Strongest in primary controlled grid | Cross-scale persistence pending |
| Pursuit/context-aware neural configurations occupy strongest observed tier | Primary matched grid + external rankings | Primary + heterogeneous testbeds | Finding, not contribution; controlled scale bridge pending |
| Efficiency compresses on harder external topology | Cross-testbed evaluation | Heterogeneous environments | Cannot attribute solely to node count; F-10 diagnoses |

---

# Relation to EXPNeuralUCB and the framework's original motivation

A policy can appear broadly strong under one evaluation setup and reveal important conditional weaknesses under a wider matched spectrum.

The current framework does this to comparators such as EXPNeuralUCB by evaluating policies across broader threat, allocator, replay, and context conditions.

Reviewer C effectively applies the same methodological standard back to our strongest observed pursuit/context-aware configurations:

> If this finding matters, test how it behaves when the routing-complexity axis changes.

That is scientifically consistent with the framework's purpose.

The correct response is **not** to defend pursuit at all costs. The correct response is to apply the framework consistently to our own strongest finding.

---

# Target reader logic

The revised paper should support this reasoning chain:

1. **Controlled discovery** — the matched framework exposes a pattern.
2. **Controlled scaling** — we test how the pattern changes with routing complexity.
3. **External validation** — we test whether related behavior persists across heterogeneous testbeds.
4. **Diagnosis** — where performance changes sharply, we investigate why.
5. **Claim boundary** — we state only what the combined evidence supports.

The intended reader reaction is:

> "I see where that finding came from, how it was tested, what persisted, what changed, and why the authors phrase the conclusion at that level."

---

# Decision summary for all agents

## Keep

- F-02 framework-first contribution strategy.
- F-07 wording calibration.
- F-08 design gate.
- F-09 execution only after F-08 approval.
- F-10 separate 100-node diagnosis.
- F-14 claim-evidence ladder/provenance audit.
- reviewer/task-tracker approval workflow.
- 10-hour weekly GA scope.

## Change

- Treat F-02 as a major structural correction, not a cosmetic one.
- Refine F-08 from a single medium-scale checkbox into a controlled scale-spectrum design while still satisfying Reviewer C's minimum request.
- Separate primary matched evidence from external-testbed evidence in wording.
- Audit pursuit/context-aware statements as findings, not as contribution claims.

## Do not

- delete valid pursuit/context-aware findings merely to avoid criticism;
- claim deployment/hardware readiness;
- claim universal best allocator;
- attribute the 100-node result to node count alone;
- run F-09 before F-08 approval;
- use September revised text to infer what the July reviewer saw;
- reopen F-02 without a new evidence-backed reason.

## Next action

Return to the F-07 wording package using:
1. exact private reviewer feedback;
2. May 23 submission-era wording;
3. current post-F-02 paragraph;
4. exact sentence under review;
5. possible solutions;
6. recommended solution and reasoning;
7. explicit Piter approval before manuscript modification.

## Decision attribution

The core conceptual correction came from Piter Garcia's re-reading of the reviewer's use of **primary evaluation**, his recall of the framework's variable-size/testbed design, and his recognition that the ICNP submission had accidentally elevated a pursuit-family **finding** into an apparent central **claim**.

Historical source reconstruction and structured synthesis were completed collaboratively with GPT-5.6 Sol.
