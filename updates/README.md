# Paper Revision Update

**Prepared for:** Dan Krutz

**Last updated:** Wednesday, September 16, 2026

**Reporting period:** August 27--September 10, 2026

**Scope:** Post-ICNP reviewer-feedback revision and resubmission preparation

This page is the concise project-status view. It reports what is complete, what
is underway, what comes next, and when each deliverable is expected. Detailed
working notes remain linked as optional evidence and are not required to follow
the update.

## Current Direction

The revision preserves the controlled evaluation, the separation of routing
policy, allocator, and capacity settings, the cross-testbed evidence, and the
capacity-paradox result recognized positively in the reviews. Reviewer C
supplies the primary revision checklist, and Reviewer B remains the final
residual-risk audit.

**Revision guardrail:** Every revision should make the strengths recognized by
Reviewer A clearer, not weaken or remove them.

## Complexity-Ordered Work Plan

The detailed checklist selects the lowest-complexity task whose dependencies
are satisfied. Work is scheduled in 10-hour weekly blocks rather than assigning
an aggressive date to every task.

| Work block | Status | Expected output |
|---|---|---|
| Contribution positioning | **Complete** | Framework-first wording independently reviewed, implemented, and build-validated across the Abstract, Introduction, contribution list, and Conclusion |
| Claim calibration | **Current** | Evidence-bounded deployment and generalization language using existing results |
| Narrative compression | **Next** | Less repetition and policy/table overload without losing validated evidence |
| Allocator--policy clarification | **Next** | Manuscript-only clarification using existing documented material |
| Reproducibility specification | **Later** | Source-backed decision loop and context/configuration inventory |
| Physical grounding | **Planned** | Cited threat-to-physics mapping with explicit stress-test boundaries |
| Scale evidence | **Pending approved design** | Medium-scale validation and targeted 100-node diagnosis |
| Residual-risk and submission audit | **Final** | Reviewer B closure plus build, evidence, anonymity, venue, and coauthor gates |
| JSAC submission package | **Primary venue** | JSAC-formatted rough draft by Oct. 15; internal submission candidate by Oct. 29; internal submission target Nov. 5 |
| TNET conversion package | **Backup only** | TNET requirements mapped in parallel; no concurrent submission while JSAC is active |

The task-level status, acceptance evidence, and dependencies are maintained in
the [current reviewer-feedback task checklist](FEEDBACK_TASKS.md).

## Work Logged Since August 27

**GA hours:** 10 / 10 for the first weekly block

- Re-established the August reviewer roadmap as the revision source of truth.
- Organized the feedback into an A+C-first checklist with Reviewer B retained
  as the later residual-risk audit.
- Reconciled the major paper, evidence, and repository sources needed to avoid
  restarting from the superseded spring task list.
- Created the advisor-facing update structure and prepared the first
  high-priority feedback task for execution.
- Established the working next-venue checklist and linked its milestones to the
  reviewer-feedback tasks.
- Completed the F-02 contribution-positioning pass and aligned the Abstract,
  Introduction findings preview, formal contribution list, and Conclusion around
  the controlled threat-aware evaluation framework.
- Independently reviewed the approved F-02 wording and build-validated the
  surgical manuscript changes without modifying results, tables, experiments,
  algorithms, configurations, or unrelated prose.

## Completed Foundation

- The matched evaluation framework, validated result set, capacity-paradox
  evidence, and cross-testbed comparison are preserved in the current paper
  workspace.
- Earlier figure, table, caption, terminology, appendix, and build-validation
  passes are recorded in the feedback-resolution log.
- The post-review strategy is fixed: preserve Reviewer A's accepted core,
  address Reviewer C's concrete checklist, and then use Reviewer B as the final
  residual-risk audit.

## Current Work

The contribution-positioning package is complete. The current task is F-07:
calibrating deployment and generalization claims against existing evidence.
Narrative compression and allocator--policy clarification follow. Source
inspection, notebook/dataset work, code, and new experiments remain deferred
until the manuscript-only reviewer fixes are exhausted. The detailed checklist
shows the feedback, problem, exact before state, defensible proposed wording,
reasoning, dependencies, and completion evidence for each task.

## Venue Decision and Delivery Dates

Dan selected the IEEE JSAC Quantum Series as the primary target and IEEE
Transactions on Networking as the backup. Both accept rolling submissions, so
March, July, and November are JSAC planned publication issues rather than
submission deadlines, and neither journal has a conference-registration
deadline.

The current internal targets are a complete JSAC-oriented rough draft for Dan
and coauthors by **October 15**, a submission candidate by **October 29**, and
submission by **November 5**. The TNET conversion package will be ready by
**November 12** as a backup, but the manuscript will not be submitted to both
journals concurrently.

## Current Supporting Detail

- [Current reviewer-feedback task checklist](FEEDBACK_TASKS.md)
- [Primary JSAC Quantum Series checklist](../venues/jsac_quantum_series/SUBMISSION_CHECKLIST.md)
- [Backup TNET checklist](../venues/tnet/SUBMISSION_CHECKLIST.md)
- [Venue strategy and internal milestones](../venues/VENUE_STRATEGY.md)
- [Completed feedback-resolution evidence](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Build and validation record](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Active manuscript source](../ICNP_2026_venue_draft.tex)

These links support the current reviewer-feedback and resubmission checklist.
Historical and superseded planning records are intentionally omitted from this
advisor-facing page.
