# Paper Revision Update

**Prepared for:** Dan Krutz

**Last updated:** September 2, 2026

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

## Guidance Requested

- Confirm whether the proposed revision order matches the preferred coauthor
  review sequence.
- Confirm whether a coauthor checkpoint should occur after the specification
  work (Sep. 9) or after the threat-grounding pass (Sep. 11).
- Confirm whether the realistic submission path should prioritize the next
  conference opportunity or a longer journal revision after the scale evidence
  is complete.

## Optional Detail

- [High-priority working backlog](../ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md)
- [Completed feedback-resolution evidence](../ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md)
- [Full draft audit checklist](../ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md)
- [Build and validation record](../ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md)
- [Active manuscript source](../ICNP_2026_venue_draft.tex)

The detailed files above are supporting records. This page remains the primary
advisor-facing status summary.
