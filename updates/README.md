# Paper Revision Update

**Prepared for:** Dan Krutz

**Last updated:** Thursday, August 27, 2026

**Reporting period:** August 27--September 2, 2026

**Scope:** Post-ICNP reviewer-feedback revision and resubmission preparation

This page is the concise project-status view. It reports what is complete, what
is underway, what comes next, and when each deliverable is expected. Detailed
working notes remain linked as optional evidence and are not required to follow
the update.

## Current Direction

The revision preserves the controlled policy--allocator--capacity evaluation,
cross-testbed evidence, and capacity-paradox result recognized positively in
the reviews. The current work prioritizes the concrete reproducibility,
interface, physical-grounding, and scale requests before a final residual-risk
audit and venue decision.

## Revision Schedule

Dates below are working targets. Experimental dates will be refined after the
configuration and compute requirements are validated.

| Work item | Status | Completed / expected output | Target |
|---|---|---|---:|
| Reconcile reviewer feedback with the current manuscript | **In progress** | One evidence-backed matrix identifying completed work and genuine remaining gaps | Sep. 3 |
| Align the paper's central contribution | **Next** | Consistent framing in the abstract, introduction, contributions, and conclusion | Sep. 4 |
| Specify the complete routing decision loop | **Next** | Reviewer-traceable pseudocode covering context, route selection, allocation, feedback, replay, and update order | Sep. 7 |
| Complete the context and configuration inventory | **Planned** | Context features, dimensions, normalization, training cadence, allocator settings, replay semantics, and major hyperparameters traced to code/configuration sources | Sep. 9 |
| Ground threats and calibrate claims | **Planned** | Threat-to-physics mapping, parameter rationale, citations, and bounded deployment language | Sep. 11 |
| Design the medium-scale validation | **Planned** | Reproducible 15--20-node experiment design with at least 10 candidate paths and explicit acceptance criteria | Sep. 15 |
| Run and validate the medium-scale experiment | **Planned; estimate pending design check** | Logs, analysis, plots, and comparison with the current small topology | Initial result target: Sep. 22 |
| Diagnose the existing 100-node result | **Planned** | Ablations separating horizon, state size, path diversity, allocator, and replay-capacity effects | Sep. 29 |
| Complete the final reviewer-risk and submission audit | **Planned** | Residual Reviewer B mapping plus build, evidence, anonymity, venue, and coauthor checks | Oct. 2 |

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

The immediate deliverable is the reviewer-feedback/current-status matrix. It
will prevent completed work from being repeated and will make every remaining
paper edit or experiment traceable to a reviewer request and supporting
evidence.

## Coordination Checks

The revision direction and immediate work are established. Feedback is welcome
on these coordination points while work continues:

- Whether the proposed sequence aligns with the preferred coauthor review
  cadence.
- Whether the first coauthor checkpoint is most useful after the specification
  work on Sep. 9 or after the threat-grounding pass on Sep. 11.
- Whether IEEE CCWC 2027 should remain the working conference target or the
  completed revision should move directly to the longer journal route.

## Current Supporting Detail

- [Current reviewer-feedback task checklist](FEEDBACK_TASKS.md)
- [CCWC 2027 submission checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md)
- [Completed feedback-resolution evidence](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Build and validation record](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Active manuscript source](../ICNP_2026_venue_draft.tex)

These links support the current reviewer-feedback and resubmission checklist.
Historical and superseded planning records are intentionally omitted from this
advisor-facing page.
