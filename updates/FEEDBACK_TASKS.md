# Current Reviewer-Feedback Task Checklist

**Baseline date:** Thursday, August 27, 2026

**Revision order:** preserve Reviewer A's accepted core, complete Reviewer C's
concrete checklist, then run Reviewer B as a residual-risk audit.

This is the current execution checklist behind the concise
[advisor update](README.md). It records task-level status and completion
evidence without reproducing private reviewer text.

## Status Definitions

- **Done:** completion evidence exists in the current manuscript or repository.
- **In progress:** work is actively underway.
- **Next:** queued immediately after the active item.
- **Planned:** sequenced work with a working target date.
- **Pending validation:** implementation is not complete until its stated
  evidence check passes.

## Feedback-Derived Tasks

| ID | Priority | Reviewer need | Current action | Status | Completion evidence | Target |
|---|---:|---|---|---|---|---:|
| F-01 | P0 | Reconcile requested revisions with the manuscript before editing | Build the reviewer-request/current-status matrix and credit work already present | **In progress** | Every feedback item has a status, evidence path, remaining gap, and next action | Sep. 3 |
| F-02 | P0 | Make the paper's contribution unmistakable | Align the abstract, introduction, contributions, and conclusion around controlled threat-aware evaluation and its validated findings | **Next** | Four sections use compatible framing without unsupported novelty claims | Sep. 4 |
| F-03 | P0 | Explain the complete routing decision process | Add or repair end-to-end pseudocode covering context construction, path selection, allocation, feedback, replay, and policy update | **Next** | The algorithm can be followed without consulting source code | Sep. 7 |
| F-04 | P0 | Fully specify contextual inputs and model settings | Trace context features, dimensions, normalization, missing values, cadence, and major hyperparameters to implementation/configuration sources | **Planned** | Complete source-backed context and configuration inventory | Sep. 9 |
| F-05 | P0 | Clarify the allocator-policy relationship | Document inputs, outputs, action order, and how allocation affects the action/feedback interface | **Planned** | Interface diagram or contract table plus consistent manuscript explanation | Sep. 9 |
| F-06 | P1 | Connect controlled threats to quantum-network phenomena | Build a sourced threat-to-physics mapping and label controlled stress tests explicitly | **Planned** | Each regime has a physical analogue, parameter rationale, source, and claim boundary | Sep. 11 |
| F-07 | P1 | Keep deployment claims within demonstrated evidence | Audit abstract, discussion, and conclusion language against validated topologies and testbeds | **Planned** | No claim exceeds the evidence boundary; all changed claims trace to validation | Sep. 11 |
| F-08 | P1 | Add medium-scale topology evidence | Specify a 15--20-node topology with at least 10 candidate paths, controls, metrics, seeds, and stopping criteria | **Planned** | Reproducible experiment specification and compute-readiness check | Sep. 15 |
| F-09 | P1 | Validate whether findings transfer at medium scale | Run the approved configuration and validate logs, plots, and comparisons | **Planned; pending F-08** | Reproducible results package and bounded cross-scale conclusion | Initial result target: Sep. 22 |
| F-10 | P1 | Explain the existing 100-node efficiency compression | Run targeted ablations for horizon, state size, routing diversity, allocator, and replay effects | **Planned** | Evidence-backed diagnosis or explicit bounded limitation | Sep. 29 |
| F-11 | P2 | Close any Reviewer B concerns not resolved through A+C work | Map each concern to completed evidence and isolate genuine residual gaps | **Planned; pending F-02--F-10** | Residual-risk matrix with every item resolved or bounded | Oct. 1 |
| F-12 | P0 | Prepare the revised paper for the working venue | Integrate accepted revisions, validate the paper, and complete the linked venue gates | **Planned** | All P0/P1 items in the [CCWC checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md) pass | Submission candidate: Oct. 30 |

## Work Completed During the First Weekly Block

- [x] Established the post-review A+C-first revision order.
- [x] Preserved the validated evaluation framework, cross-testbed evidence, and
  capacity-paradox result as the revision core.
- [x] Organized the current task sequence and established task-level completion
  evidence.
- [x] Created an advisor-readable update layer separate from implementation
  logs and historical records.
- [x] Prepared F-01 as the first active task.

## Execution Rule

Work begins with the first unresolved task in priority order. A task moves to
**Done** only after its completion evidence is verified. New work is added only
when it maps directly to reviewer feedback, required validation, or the current
venue submission checklist.

## Evidence Drill-Down

- [Detailed active working backlog](../ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md)
- [Completed feedback-resolution log](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Draft-wide audit checklist](../ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md)
- [Build validation log](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
