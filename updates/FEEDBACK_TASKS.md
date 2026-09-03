# Reviewer-Feedback Execution Checklist

**Baseline date:** Thursday, August 27, 2026

**Execution model updated:** Thursday, September 3, 2026

**Current task:** F-01 — preserve and reconcile the accepted contribution

This is the detailed execution board behind the concise
[advisor update](README.md). Tasks are ordered from the easiest ready work to
the hardest experimental work. Reviewer classification remains visible, but
priority labels no longer determine day-to-day order.

## Working Rule

1. Select the **lowest-complexity unresolved task whose dependencies are met**.
2. Preserve Reviewer A's accepted core throughout every change.
3. Use Reviewer C's concrete requests as the primary revision checklist.
4. Use Reviewer B as the final residual-risk audit after overlapping work is complete.
5. Do not edit manuscript text until the task's proposed solution and evidence
   sources have been reviewed.
6. Move a task to **Done** only when its acceptance evidence is verified.
7. Add no new task unless it maps directly to documented feedback, required
   validation, or an approved venue gate.

Dependencies override complexity. For example, the residual-risk audit is not
hard to write, but it cannot be completed until the evidence-producing tasks
it audits are finished.

## Feedback We Are Addressing

| Reviewer | What the reviewer recognized | Feedback that requires action | How it is used |
|---|---|---|---|
| A — Weak Accept / expert | Controlled evaluation design, policy--allocator--capacity factorization, external-testbed validation, and the capacity paradox | Clarify the central contribution; compress the narrative; reduce visible policy/table overload | Preserve the accepted scientific spine and improve how quickly readers can understand it |
| C — Weak Reject / nonexpert | The matched-evaluation problem and controlled grid are meaningful | Improve reproducibility, algorithm specification, context definition, allocator semantics, physical grounding, and topology scale | Primary conversion checklist, progressing from specification to new evidence |
| B — Reject / expert | Bandit benchmarking for quantum routing is potentially useful | Improve system-model clarity, algorithm definition, physical mapping, topology realism, and theoretical or real-world support | Residual-risk audit after A/C overlap is addressed |

The detailed source classification remains in the
[August reviewer roadmap](../../../RESEARCH/RESEARCH/2026-08-04-icnp-review-classification-and-revision-roadmap.md).
This checklist paraphrases the actionable feedback rather than reproducing
private reviewer text.

## Easiest-to-Hardest Queue

Human-effort ranges are planning estimates, not promises; experiment runtime is
excluded. Work is planned in 10-hour weekly blocks.

| Order | ID | Complexity | Feedback focus | Status | Human effort | Dependency |
|---:|---|---|---|---|---:|---|
| 1 | F-01 | Low | Preserve the accepted core and reconcile it with current evidence | **In progress** | 2--3 h | None |
| 2 | F-02 | Low | Position the central contribution | **Queued** | 2--3 h | F-01 |
| 3 | F-05 | Low | Explain allocator--policy semantics | **Queued** | 2--3 h | F-01 |
| 4 | F-07 | Low | Calibrate deployment/generalization claims | **Queued** | 1.5--2 h | F-01 |
| 5 | F-13 | Low--Medium | Compress the main narrative without losing evidence | **Planned** | 3--4 h | F-02 |
| 6 | F-03 | Low--Medium | Specify the complete routing decision loop | **Planned** | 3--5 h | F-05 |
| 7 | F-04 | Medium | Document context and hyperparameters | **Planned** | 4--6 h | F-03 |
| 8 | F-06 | Medium | Ground threats in physical phenomena | **Planned** | 4--6 h | F-01 |
| 9 | F-08 | High | Design medium-scale validation | **Planned** | 4--6 h | F-03--F-06 |
| 10 | F-09 | Very High | Run and validate medium-scale experiment | **Blocked by design** | 8--15+ h | F-08 approval and compute check |
| 11 | F-10 | Very High | Diagnose 100-node efficiency compression | **Planned** | 8--15+ h | F-04, F-05, validated ablation plan |
| 12 | F-11 | Medium, dependency-late | Audit residual Reviewer B risk | **Blocked by evidence tasks** | 2--4 h | F-02--F-10 |
| 13 | F-12 | Final integration | Complete venue and submission gates | **Ongoing/final** | Separate venue plan | Accepted revisions and venue confirmation |

## Task Packages

### F-01 — Preserve and Reconcile the Accepted Contribution

- **Feedback addressed:** Reviewer A positively identifies the controlled
  evaluation, policy--allocator--capacity factorization, cross-testbed evidence,
  and capacity paradox; Reviewers B and C identify gaps around that accepted core.
- **Problem:** Editing before reconciliation risks repeating completed work,
  removing validated strengths, or creating tasks from assumptions rather than feedback.
- **Possible solutions:** (1) restart every request from scratch; or (2) build a
  feedback/current-status matrix from the manuscript, validation artifacts,
  configurations, and completed-resolution logs.
- **Recommended solution and why:** Use option 2. It credits existing work and
  converts only verified gaps into edits or experiments.
- **Completion evidence:** Every accepted strength is frozen in a claim-to-evidence
  map, and every feedback category has a current status, evidence path, remaining
  gap, and next action.

### F-02 — Align the Central Contribution

- **Feedback addressed:** Reviewer A asks for clearer contribution positioning;
  Reviewer C recognizes the controlled grid as a methodology contribution.
- **Problem:** The paper can appear to claim a new bandit family when its strongest
  novelty is the controlled threat-aware evaluation and resulting evidence.
- **Possible solutions:** (1) position a specific policy as the novelty; or (2)
  position the matched evaluation and no more than three validated findings centrally.
- **Recommended solution and why:** Use option 2 because it matches the positive
  review and evidence without unsupported algorithmic novelty.
- **Completion evidence:** Abstract, introduction, contribution list, and
  conclusion use one compatible contribution statement linked to evidence.

### F-05 — Clarify the Allocator--Policy Relationship

- **Feedback addressed:** Reviewers B and C ask when allocation occurs and how it
  changes actions and feedback.
- **Problem:** Execution order and ownership of allocation decisions are ambiguous.
- **Possible solutions:** (1) add prose only; or (2) add a compact interface
  contract/diagram plus concise prose defining inputs, outputs, and ordering.
- **Recommended solution and why:** Use option 2. A contract is easier to verify
  against code and easier to follow than dispersed prose.
- **Completion evidence:** One source-backed contract identifies path selection,
  allocation timing, feasible actions, reward observation, and update order.

### F-07 — Calibrate Claims to Demonstrated Evidence

- **Feedback addressed:** Reviewers B and C question whether deployment and
  generalization language exceeds the tested topologies and simulators.
- **Problem:** A valid controlled result can still be overstated as unrestricted
  scalability or real-world deployment proof.
- **Possible solutions:** (1) remove all deployment implications; or (2) retain
  practical implications while bounding them to validated testbeds and stress tests.
- **Recommended solution and why:** Use option 2. It preserves the paper's value
  while making the evidence boundary explicit.
- **Completion evidence:** Abstract, introduction, discussion, and conclusion
  claims map to validated evidence and contain no unsupported scale claim.

### F-13 — Compress the Main Narrative

- **Feedback addressed:** Reviewer A asks to reduce policy/table overload and
  make the main contribution easier to follow.
- **Problem:** Too many variants or detailed tables obscure the contribution.
- **Possible solutions:** (1) delete secondary evidence; or (2) keep representative
  evidence in the main body and relocate traceable detail to supporting material.
- **Recommended solution and why:** Use option 2. It improves readability without
  losing validated evidence or reproducibility.
- **Completion evidence:** A nonexpert reader can identify the problem, method,
  and three findings from the abstract/introduction; relocated evidence stays referenced.
- **Guardrail:** No removal occurs without an explicit before/after review.

### F-03 — Specify the Complete Routing Decision Loop

- **Feedback addressed:** Reviewers B and C request a reproducible end-to-end algorithm.
- **Problem:** Context construction, route selection, allocation, feedback,
  replay, and update order cannot be reconstructed from one location.
- **Possible solutions:** (1) expand dispersed prose; or (2) add one source-backed
  algorithm/pseudocode block with a short interface explanation.
- **Recommended solution and why:** Use option 2. It directly answers the request
  and permits line-by-line implementation verification.
- **Completion evidence:** The loop can be followed without source code, and
  each step has code/config provenance.

### F-04 — Specify Context and Hyperparameters

- **Feedback addressed:** Reviewers B and C request feature definitions,
  dimensions, preprocessing, missing-value behavior, cadence, and model settings.
- **Problem:** Reproduction is impossible when inputs and settings are implicit.
- **Possible solutions:** (1) summarize selected settings in prose; or (2) build
  source-backed context-feature and reproducibility/configuration tables.
- **Recommended solution and why:** Use option 2. Tables expose omissions and
  retain traceability without bloating the algorithm narrative.
- **Completion evidence:** Features, dimensions, normalization, missing values,
  cadence, pursuit, NeuralUCB, and Thompson settings are traced.

### F-06 — Map Threats to Quantum-Network Phenomena

- **Feedback addressed:** Reviewers B and C request physical motivation,
  parameter justification, and simulation-to-reality boundaries.
- **Problem:** Controlled regimes may be mistaken for literal physical models.
- **Possible solutions:** (1) present each as a direct attack model; or (2) map
  each to plausible phenomena and label unmatched parts as controlled stress tests.
- **Recommended solution and why:** Use option 2. It strengthens grounding without
  overstating the simulator.
- **Completion evidence:** Every regime has an analogue, rationale, citation,
  stress-test status, and claim boundary; coauthor review is recorded.

### F-08 — Design Medium-Scale Validation

- **Feedback addressed:** Reviewers B and C question transfer beyond the small topology.
- **Problem:** An unplanned run could consume compute without answering the scale question.
- **Possible solutions:** (1) jump to another 100-node run; or (2) specify a
  controlled 15--20-node topology with at least 10 paths, controls, metrics,
  seeds, stopping criteria, and compute estimates.
- **Recommended solution and why:** Use option 2. Medium scale is interpretable
  and bridges the existing endpoints.
- **Completion evidence:** Approved reproducible specification, acceptance
  criteria, storage estimate, and compute-readiness decision.

### F-09 — Run and Validate the Medium-Scale Experiment

- **Feedback addressed:** Reviewers B and C request actual scale evidence.
- **Problem:** Current evidence cannot show what transfers to a richer route set.
- **Possible solutions:** (1) retain only existing endpoints; or (2) execute the
  approved design and compare efficiency, stability, regret, allocator behavior,
  and capacity sensitivity.
- **Recommended solution and why:** Use option 2 only after F-08 approval.
- **Completion evidence:** Canonical logs, notebook validation, plots,
  configuration provenance, and a bounded cross-scale conclusion.

### F-10 — Diagnose the 100-Node Efficiency Compression

- **Feedback addressed:** Reviewers B and C need an explanation for the existing
  approximately 44.1% large-topology result.
- **Problem:** Horizon, state size, route diversity, allocation, and replay causes
  have not been separated.
- **Possible solutions:** (1) leave it unexplained; or (2) run targeted,
  pre-registered ablations and report a diagnosis or bounded limitation.
- **Recommended solution and why:** Use option 2, while accepting a documented
  limitation if no single cause is isolated rather than inventing a mechanism.
- **Completion evidence:** Validated ablations separate the factors, or the paper
  states precisely what remains unresolved.

### F-11 — Complete the Reviewer B Residual-Risk Audit

- **Feedback addressed:** Reviewer B's concerns about system clarity, algorithms,
  physical grounding, topology realism, and real-world support.
- **Problem:** Overlap with Reviewer C can conceal a B-only residual gap.
- **Possible solutions:** (1) duplicate all B work now; or (2) map every B concern
  to completed A/C evidence and isolate only residual gaps afterward.
- **Recommended solution and why:** Use option 2. It avoids duplicate work while
  showing that the reject review was addressed fully.
- **Completion evidence:** Every B concern is resolved, bounded as a limitation,
  or assigned one approved residual action.

### F-12 — Complete Venue and Submission Integration

- **Feedback addressed:** Delivery gate for accepted revisions, not a new claim.
- **Problem:** Correct revisions can still fail through template, anonymity,
  page-budget, evidence, build, or coordination errors.
- **Possible solutions:** (1) leave preparation to the final day; or (2) maintain
  venue gates separately and integrate only approved, validated revisions.
- **Recommended solution and why:** Use option 2 to keep science and compliance
  separate but traceable.
- **Completion evidence:** Required gates in the
  [CCWC checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md) pass, subject to venue confirmation.

## First 10-Hour Work Block

- [ ] Complete F-01 accepted-core claim/evidence and feedback-status matrix (2--3 h).
- [ ] Draft F-02 contribution alignment package for review (2--3 h).
- [ ] Trace F-05 allocator-interface semantics to source (2--3 h).
- [ ] Use remaining time to begin the F-07 claim-boundary audit.

This is a capacity-aware plan, not a promise to finish every low-complexity task
in one week. AI-assisted preparation does not count as logged GA work unless the
user separately performs and records the substantive review/validation work.

## Evidence Drill-Down

- [Detailed active working backlog](../ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md)
- [Completed feedback-resolution log](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Draft-wide audit checklist](../ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md)
- [Build validation log](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Working venue checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md)
