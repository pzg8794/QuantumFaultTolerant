# Whole-paper reviewer-closure audit — October 22, 2026

## Verdict

**NOT READY TO DECLARE ALL FEEDBACK CLOSED.** The framework-first contribution, algorithm/context/allocator explanation, physical-grounding table, accepted medium-scale anchor, bounded diagnosis, and six medium diagnostic figures are present. Remaining inconsistencies in the manuscript prevent complete closure. This audit does not reopen accepted Q07 analysis, authorize experiments, change reported results, or approve new scientific wording.

Audited candidate: `codex/reviewer-closure-20261018`, source commit **`aea91e0003ffc744ae9085cf6374de74d6c03d5c`**. Read the master and all eleven active section/appendix fragments, rather than the unused `main.tex` or commented-out Related Work input. Rebuilt the entire 29-page PDF and inspected all pages as layout contact sheets, with source-level examination of every section and caption. This is a whole-paper consistency/coverage audit, not another independent trace reproduction or a final print-readability certification.

Authority: current `FEEDBACK_TASKS.md`, `EVALUATION_SOURCE_STATUS_2026-10-04.md`, F03/F05, F04, F06 and scale/claim decision records, F14 evidence matrix, August A+C-first roadmap, existing advisor source comments, and historical review backlog. Current acceptance decisions supersede older experiment plans. The roadmap summarizes A/B/C; the complete private A/B reviews and any unexported live Overleaf review-panel comments were not independently retrieved in this pass. Consequently, coverage of the documented feedback is audited, but exhaustive coverage of unseen comments cannot be certified.

## Feedback-to-manuscript closure matrix

| Task / feedback | Present evidence | Audit disposition | Missing closure requirement |
|---|---|---|---|
| F02 — contribution hierarchy (A/C) | Abstract, Introduction contribution list, Discussion, Conclusion foreground the evaluation framework | **Approved foundation retained** | Related Work still says “we employ a stochastic approach”; align that description with evaluation of heterogeneous policies, without reopening the approved high-level wording |
| F03 — reconstructable joint loop (B/C) | Algorithm 1; separate model-specific route/action/update steps; availability, replay and conditional allocator hook | **Implemented, consistency gate open** | Main-body scalar-feedback assertion contradicts the appendix's medium feedback contract; optional interface must remain distinct from historically executed cadence |
| F04 — contexts, training, parameters (B/C) | Allocation-vector equation; 2/3-dimensional primary contexts; medium and Paper8 rows; NeuralUCB/Pursuit specification; 15-policy-plus-Oracle table | **Partial** | Historical effective settings and remaining external encodings are unresolved; state normalization/missing-value handling where applicable; resolve mechanism/family labels and parameter-table scope conflicts |
| F05 — allocator/policy division (B/C) | Inter-route budgets versus within-route action; architecture diagram; conditional update | **Conceptual response implemented; provenance hold** | Historical adaptive execution cadence is not established; do not infer online reallocation from allocator names; qualify Random's distribution from its source rather than interpreting “uniform” as equal fixed budgets |
| F06 — physical grounding (B/C) | Five-regime rationale, q/A separation, domain mapping/citations, parameter and hardware boundaries, pinned medium process | **Conceptual response implemented; residual correction and provenance hold** | RQ1 still calls availability interruption “Stochastic decoherence”; historical exact processes remain pending; coauthor domain validation still needed |
| F07 — calibration (B/C) | Approved Abstract/caption wording; bounded medium/Oracle statements; no active “deployment-grade robustness” | **Locked changes retained; whole-paper sweep incomplete** | Cross-testbed captions and older diagnostics still assert unisolated topology/context causes; Related Work attribution language conflicts with Discussion's statistical boundary |
| F08 — medium design (C/B) | 15 nodes, ten routes, 550 route/action pairs, fixed allocator/replay, explicit comparator contract | **Required medium anchor addressed** | Do not relabel this as the entire proposed controlled scale spectrum |
| F09 — accepted medium execution (C/B) | 75 accepted cells, three blocks, 6,000 frames; table, trajectories and diagnostic appendix | **Accepted execution and manuscript presentation present** | No rerun. Final integration review must preserve exact metric/window and information-interface qualifications |
| F10/Q07 — compression diagnosis (C/B) | Accepted analysis and explicit historical-causality boundary in medium Results, Discussion, Limitations and Conclusion | **Existing-trace diagnosis CLOSED, claim-limited** | Historical 100-node cause remains unresolved. Remove contradictory causal captions; this is not an analysis repair or an instruction for another experiment |
| F11 — B residual-risk audit | Existing concern-to-artifact table and simulation/theory limitations | **Partial final closure** | Resolve this audit's conflicts; reconcile any B-only requirements against the complete original review/coauthor decision. A limitation is not proof that the reviewer accepted it |
| F12 — submission readiness | Journal mode, Letter, one-inch margins, 173-word abstract, five keywords, successful build | **OPEN** | 29 pages versus 13-page initial limit; authors/funding/accounts/ORCIDs/disclosures, artifact access and coauthor approval; reconcile source variants |
| F13 — readability/overload (A) | Details moved to appendices; concise medium summary; bounded Discussion | **PARTIAL** | Repeated answers in RQ section, repeated ranking narratives, substantial float whitespace and excessive length remain; appendix placement alone does not satisfy the page limit |
| F14 — claim/evidence consistency | Explicit primary/medium/external scopes and accepted claim matrix | **Implemented but not closed** | Reconcile historical RQ3 baseline/gain labels, external aggregation definitions, metric notation, remaining causal language and evidence access |

There is no F01 task in the current F02–F14 checklist; this audit does not invent one. The original eight implementation commits establish that work was performed, not that every underlying feedback item is closed.

## Required corrections, in execution order

These are bounded findings under existing tasks, not new research projects. Recommendations are not replacement-prose approvals. Scientific edits still require the established paragraph/evidence/approval workflow.

### 1. Reconcile the RQ3 baseline and switching-gain scope — F14/F04

**Confirmed internal conflict.** `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex:213` labels 96.0% mean / 92.8% floor as a 3-and-5-run-suite mean. Its RQ3a table at line 237 uses those values for the three-run slice. The allocator table at line 340 and switching paragraph at line 359 instead give 95.5% / 88.5% for the stated 3/5-suite baseline.

The switching table at line 365 says gains are relative to that static default, but the printed entries do not reproduce that definition:

| Threat | Displayed static value | Displayed switched value | Arithmetic difference (pp) | Printed gain (pp) |
|---|---:|---:|---:|---:|
| Stochastic | 94.6 | 95.4 | +0.8 | +0.6 |
| Markov | 94.7 | 93.2 | -1.5 | +0.3 |
| Adaptive | 88.5 | 95.7 | +7.2 | +2.9 |

**Recommendation:** recover the existing validated slice IDs and aggregation definitions for each table/figure, then correct the scope/caption/prose consistently. Do not replace the accepted +2.9 pp result with +7.2 pp merely because subtraction exposes the mismatch. Different slices may explain the values; the manuscript currently does not tell the reader which one generated each gain. This blocks a reproducible configuration recommendation, not acceptance of Q07.

### 2. Reconcile external efficiency aggregation and comparator notation — F14/F04

`APPENDIX_CROSS_TESTBED_TABLES.tex:186` defines efficiency as model average reward divided by Oracle average reward. The displayed Paper8 iCP means, 210,419.0 and 300,540.2, yield **70.0136%**, not the printed **67.9%**. This is too large for the displayed reward rounding to explain. A mean of per-configuration ratios can legitimately differ from a ratio of means; the audit does not choose that explanation without the existing source evidence.

**Recommendation:** specify the actual aggregation order, denominators, weights, comparison slice and win rule. The family table's external rows also use different values/counts (e.g., Clayton 41.6%, 26/75 versus 44.1%, 97/300); its note at line 266 does not fully identify the distinct external slice. Preserve values while resolving the definitions.

`STUDY_DESIGN_VALIDATED_STAGING.tex:214` reuses `T` for an efficiency horizon although it already denotes replay capacity, uses `r_t` for reward although the system model uses it for route identity, and leaves `theta*` undefined. Its generic Oracle-gap definition at line 19 does not state direction/units, while the medium appendix correctly uses an absolute continuous-payoff gap and historical tables use percentage-point gaps.

**Recommendation:** give scope-specific outcome/comparator definitions and unambiguous symbols; retain the already-explicit medium ratio-of-sums-per-block followed by equal-block averaging. Define historical regret/normalization where reported rather than implying all corpora share one metric.

### 3. Make the main reward interface agree with Algorithm 1 — F03/F04/F05

`ICNP_2026_venue_draft.tex:351` states that the policy observes **only** realized Bernoulli reward. `APPENDIX_ALGORITHM_SPECIFICATION.tex:60` documents continuous allocation feedback plus distinct route channels for the medium policies. These cannot both be read as a universal executed interface.

**Recommendation:** retain the probabilistic success objective, but scope that model and introduce the model/corpus-specific feedback record in the main body, referencing the appendix. Do not turn the lack of positive Bernoulli draws into absence of useful learner feedback. No code change is needed to resolve the prose contradiction.

### 4. Finish bounded-claim consistency in old prose/captions — F07/F10/F14

| Location | Remaining issue | Recommended resolution |
|---|---|---|
| `ICNP_2026_venue_draft.tex:227` and `:232` | Attribution to policy–allocator–capacity interaction reads more strongly than grouped/conditioned comparisons; “we employ a stochastic approach” misdescribes the heterogeneous evaluation | Describe comparison scope and conditional patterns; no formal interaction or new algorithm claim |
| `RESULTS_VALIDATED_CROSS_TESTBED.tex:6`, `:22`, `:31` | Topology complexity is said to widen gaps/compress model separation, while line 78 explicitly says the heterogeneous evidence does not isolate that cause | Report observed testbed differences and retained average leader, with the existing heterogeneity boundary |
| `APPENDIX_CROSS_TESTBED_TABLES.tex:173` | The fusion topology is said to compress all methods | Retain observed efficiency range; do not identify topology/node count as cause |
| `APPENDIX_DIAGNOSTIC_FIGURES.tex:14` | Path/context information is said to reduce efficiency loss, despite no isolated feature intervention | Describe the compared policy outcomes, not a causal feature effect |
| `RESULTS_VALIDATED_STAGING.tex:221`, `:224`, `:244` | Predictive/context mechanism is treated as isolated; the policy variants may differ in more than that feature | Limit to the observed fixed-setting policy comparison unless the historical source establishes a controlled component intervention |

Descriptive use of “interaction” and genuine fixed-slice comparisons need not be mechanically deleted. The defect is an inference beyond the controlled contrast, not the word itself. Similarly, “deployment” is not automatically prohibited when explicitly simulator-scoped; headings and captions should nevertheless agree with the approved configuration-guidance framing. Historical “structural failure” labels must not be confused with the precisely defined medium structural-zero metric.

### 5. Correct the surviving threat/model-label contradictions — F06/F03/F04

- `ICNP_2026_venue_draft.tex:385` calls the Stochastic setting “decoherence alone,” contradicting the explicit q/A separation and mapping table. Use the already-approved independent-availability interpretation.
- `APPENDIX_CROSS_TESTBED_TABLES.tex:222` puts GNeuralUCB under an **EXP3-based** heading, while the policy table specifies Simple-UCB route selection. If EXP is a dataset/suite name, label it as a corpus grouping, not an algorithmic mechanism. Do not change values or infer a different model roster.
- Study Design's forecasting row (line 100), DynamicUCB lambda/Random epsilon row (lines 201–202), and historical parameter table need consistent status. The appendix labels historical values unverified, but main-body “Options Tested”/mechanism entries can still be read as effective run facts. Verify the existing data-producing provenance or mark the scope explicitly; current defaults are not substitutes.
- The warmup symbol `n` is used in the forecasting row without an active definition; its source comment says it was defined, but the replacement paragraph no longer does so.

### 6. Complete historical reproducibility, without another experiment — F03/F04/F05/F06

Already-recorded holds remain genuine: adaptive allocator cadence/execution; historical Markov/Adaptive/OnlineAdaptive process settings; effective nested learner/training/predictive parameters; external context representations other than Paper8. The verified medium contract does not supply those historical facts. The context specification also should explicitly state normalization and missing-value handling, or inapplicability, from existing implementation evidence rather than leaving the roadmap's requested details implicit.

**Recommendation:** bounded provenance reconciliation against existing archived code/configs/receipts. If unavailable, retain an explicit limitation for owner/coauthor adjudication rather than silently marking replication complete. The mechanism table and conditional architecture remain useful and should not be removed because historical cadence is unresolved.

### 7. Resolve remaining scope/reconstructability questions — F04/F14/F11

- Introduction line 185 reports 8,241 matched tests; Study Design line 208 reports 552 configurations, a target of approximately 5,520 episodes and 380 A100 GPU-hours. These may refer to different units/scopes, but the manuscript does not reconcile them. Identify planned versus executed counts and the underlying corpus scopes without treating either as a new measurement.
- Study Design line 220 reports bootstrap intervals/significance and a >2 pp win rule, whereas Results uses multiple aggregated win shares/counts. Existing decision records acknowledge bootstrap/grouped-comparison code; **this audit does not claim it is absent**. State the resampling unit, relevant outputs, win/tie scope and applicability. Do not let this historical protocol imply significance testing of three-block medium ranges.
- `FUTURE_WORK.tex:18` says a “current heuristic meta-policy” will be replaced. The paper otherwise documents configuration recommendations, not an established evaluated online meta-controller. Link the existing implementation/evidence or remove the implication that such a controller already exists. A forward-looking plan is not a current experiment authorization.
- The Introduction's anonymous artifact link could not be verified through the available web fetch. This is **access unverified**, not proof that the repository is dead. Final reviewers need a reachable, version-pinned source/evidence route; do not publish restricted traces to solve an access problem.

### 8. Close actual readability and submission gates — F13/F12

The active RQ section still answers each research question, although its advisor comment at `ICNP_2026_venue_draft.tex:410` and the historical backlog label that issue solved. This is a concrete unresolved comment and a useful compression target, not a stylistic invention.

The new diagnostic views are present and referenced, with no exact reused graphic file among the 28 external assets. However, the 29-page PDF has an almost empty final-reference page (16), an appendix-introduction-only page (22), and a settings-table-only final page (29); several appendix figures occupy dedicated float pages. Removing avoidable whitespace helps but will not by itself recover the full 16-page excess. The existing main-body summaries, full appendix tables, repeated ranking discussion and old multi-panel diagnostics require an advisor-approved main-paper/supporting-material allocation. Preserve scientific qualifications and evidence; do not shrink required fonts or remove inconvenient results.

[JSAC author guidelines](https://www.comsoc.org/publications/journals/ieee-jsac/policies-guidelines), checked October 22, specify a 13-page initial submission including references and appendices; a 16-page revision allowance does not automatically apply to a rejected conference paper's first journal submission. They also specify a 75–200-word abstract and at most five keywords. The current 173-word/five-keyword candidate passes those two checks. This audit does not assume arbitrary supplementary material is exempt or accepted: confirm the target call's permitted submission package before moving material outside the manuscript.

Human gates remain author order/affiliations/corresponding author, funding/conflicts, ORCIDs/accounts, coauthor physical-model review and final approval, and applicable prior-work/AI-use disclosures. The source still contains `Anonymous Authors` and `[hidden]` funding. These are working placeholders, not a finished journal author sheet. No theoretical guarantee or hardware experiment is newly required by this audit; B's remaining practical/theoretical concern needs an explicit scoped response and coauthor disposition.

## What is scientifically closed and must stay closed

- Q07 accepted existing-trace analysis: **PASS WITH REQUIRED CLAIM LIMITATIONS**; Astra/Sol/final-audit chain retained.
- Medium anchor execution: 75 cells; 15 nodes; ten routes; 6,000 frames; fixed allocator; no new runs requested.
- F10 existing-trace diagnosis: complete. Historical 100-node causality: unresolved limitation, not a hidden experiment assignment.
- Figure integration: all six medium views present; body Figures 9–10, appendix Figures 14–17. Their medium definitions, denominators and qualifications are explicit. This audit found no reason to recompute the accepted data or replace their metrics.
- Approved F02 and exact F07 high-level foundation: retained. Residual inconsistencies in other locations are not a new review of those approved sentences.

## Validation and repository boundaries

Fresh command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=<task-temporary-build> ICNP_2026_venue_draft.tex` using installed MacTeX.

- Build succeeded, **29 pages**, US Letter; all inspected font entries embedded.
- Twelve active TeX files; **92 unique labels**, zero duplicate labels, zero undefined source references/citation keys, zero missing graphic assets, 28 external graphic assets, zero exact duplicate asset paths.
- Zero overfull horizontal boxes. Existing warnings: one 0.95433pt overfull vertical box, page 8 floats-only, three small-cap italic font fallbacks, and underfull boxes.
- Abstract 173 whitespace-delimited words after comment stripping; five comma-separated keywords.
- Source hashes and arithmetic/scope checks are in `FULL_PAPER_FEEDBACK_AUDIT_2026-10-22_CHECKS.json`. Arithmetic checks expose contradictory stated definitions; they do not replace historical data validation.
- All active source and captions were read. Bibliography keys resolve; bibliographic metadata/content support for every reference was not independently re-audited. Thumbnail layout inspection is not proof that every small legacy panel prints accessibly; final-size/grayscale QA remains a release gate.
- No manuscript, figure, experiment, analysis package, or validated result changed in this audit. Only audit/status documentation is updated.

Live GitHub review branch matched `aea91e0`; GitHub main was `0bcc913`. The original paper checkout remains dirty at `70e143e`, one ahead/64 behind origin/main. A read-only remote inspection followed by non-destructive fetch found Overleaf master at **`7561227826d1f65bae9dcf4ab34b23910300e1d4`**, newer than the previously recorded `c304cb8`. That latest Overleaf commit changes four status/decision files, not manuscript source. Overleaf still lacks the review candidate's medium Results/appendix/six figure assets. No merge, reset, stash, original-checkout edit, or Overleaf push occurred. Different Git ancestry is not evidence that all remote commits are distinct manuscript changes.

## Recommended next work

1. Resolve the RQ3 and external aggregation/scope discrepancies using existing evidence; preserve all values until provenance decides the correct labels.
2. Present the bounded reward/threat/claim-label fixes through the established approval workflow, then implement and build.
3. Complete or explicitly adjudicate the historical provenance holds.
4. Agree a venue-compliant main-paper/supporting package and rerun final layout/accessibility checks.
5. Obtain final independent integration/coauthor acceptance and deliberately reconcile the source variants.

Do not declare all reviewer feedback addressed until these gates pass. Do not restart Q07 or the medium experiment to address editorial inconsistencies.
