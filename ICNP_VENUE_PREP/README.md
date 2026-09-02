# ICNP Revision Evidence Index

This directory contains the detailed working evidence behind the concise
[advisor update](../updates/README.md) and the
[current reviewer-feedback tasks](../updates/FEEDBACK_TASKS.md). Start with the
status records below; open section-specific audits only when the corresponding
task requires them.

## Current Status

- [High-priority review backlog](HIGH_PRIORITY_REVIEW_BACKLOG.md) - detailed active working board.
- [Active feedback resolution log](ACTIVE_FEEDBACK_RESOLUTION_LOG.md) - completed changes and validation evidence.
- [Draft audit checklist](ICNP_DRAFT_AUDIT_TODO.md) - full manuscript and submission checklist.
- [Build validation log](BUILD_VALIDATION_LOG.md) - compile, reference, PDF, and checker results.

## Active Manuscript Components

- `STUDY_DESIGN_VALIDATED_STAGING.tex`
- `RESULTS_VALIDATED_STAGING.tex`
- `RESULTS_VALIDATED_CROSS_TESTBED.tex`
- `DISCUSSION.tex`
- `FUTURE_WORK.tex`
- `CONCLUSION.tex`
- `APPENDIX_CROSS_TESTBED_TABLES.tex`
- `APPENDIX_DIAGNOSTIC_FIGURES.tex`

The root `ICNP_2026_venue_draft.tex` controls their inclusion order.

## Evidence and Presentation

- [Figure selection audit](FIGURE_SELECTION_AUDIT.md)
- [Figure accessibility note](FIGURE_COLOR_ACCESSIBILITY_NOTE.md)
- [Results graph evidence layout](RESULTS_GRAPH_EVIDENCE_LAYOUT_PLAN.md)
- [Results table relocation plan](RESULTS_TABLE_RELOCATION_PLAN.md)
- [Space-recovery candidates](SPACE_RECOVERY_CANDIDATE_SWEEP.md)
- [Caption locks](CAPTION_LOCKS.md)
- [Text locks](TEXT_LOCKS.md)
- [Bandit terminology consistency](BANDIT_TERMINOLOGY_CONSISTENCY.md)

## Section Audits

Section-specific audit files are grouped by filename prefix:

- `ABSTRACT_*`, `INTRODUCTION_*`, `BACKGROUND_*`, and `RELATED_WORK_*` - front-matter and positioning audits.
- `SYSTEM_MODEL_*` - topology, reward, threat, notation, and policy-interface audits.
- `STUDY_DESIGN_*` - research questions, experiment design, configurations, and reproducibility audits.
- `RESULTS_*_AUDIT.md` - RQ-specific result and claim audits.

These files preserve the rationale for prior decisions. They are supporting
evidence, not separate active task lists.

## Venue Requirements

- [Official requirements used during ICNP preparation](OFFICIAL_GUIDELINES.md)
- [Formatting and bold-text reduction record](FORMATTING_BOLD_TEXT_REDUCTION.md)

Current venue selection and retargeting records live in `../venues/`. The
[CCWC 2027 submission checklist](../venues/ccwc_2027/SUBMISSION_CHECKLIST.md)
maps venue gates directly to the current feedback-task IDs.

## Documentation Rule

- Put advisor-readable status in `../updates/README.md`.
- Put active tasks in `HIGH_PRIORITY_REVIEW_BACKLOG.md`.
- Put completed implementation evidence in `ACTIVE_FEEDBACK_RESOLUTION_LOG.md`.
- Put compile and rendered-output evidence in `BUILD_VALIDATION_LOG.md`.
- Do not create a new tracker when one of these records already owns the information.
