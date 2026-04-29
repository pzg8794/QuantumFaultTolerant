# ICNP Venue Preparation

This directory is the central reference area for preparing the quantum routing paper for the IEEE International Conference on Network Protocols (ICNP).

The goal is to keep all ICNP-specific requirements, examples, deadlines, reviewer-expectation notes, and manuscript-conversion decisions in one place so `main.tex` can be revised toward a submission-ready ICNP draft without losing track of venue constraints.

## Fast status

Last assembled: 2026-04-28.

Primary target: ICNP 2026.

Official 2026 pages to verify before final submission:

- Main ICNP series page: https://www.ieee-icnp.org/
- ICNP 2026 CFP: https://icnp26.cs.ucr.edu/cfp.html
- ICNP 2026 submission page: https://icnp26.cs.ucr.edu/submission.html

## High-confidence working facts

Based on the official ICNP 2026 CFP/submission pages and recent ICNP pages:

- Title/abstract registration: May 15, 2026, Anywhere on Earth (AoE).
- Full-paper deadline: May 22, 2026, AoE.
- Notification: July 21, 2026.
- Camera-ready deadline: August 25, 2026.
- Format: IEEE conference style, US Letter, 10-point, two-column.
- Main paper length: 10 pages, excluding references.
- Review: double-blind.
- Appendices: ICNP 2025/2026 pages allow well-marked appendices outside the main 10 pages, but core claims should remain in the main paper.
- Artifacts: public artifact release is encouraged after acceptance; for double-blind submission, public repo/Drive links should be removed or anonymized.

## Files

- `EXECUTIVE_SUMMARY.md` - fast venue-fit summary and critical decisions.
- `OFFICIAL_GUIDELINES.md` - deadlines, format rules, anonymity, artifacts, and recent-year comparison.
- `AUTHOR_KIT_AND_FORMATTING.md` - IEEE class/template guidance and LaTeX conversion notes.
- `RECENT_PAPERS_AND_EXAMPLES.md` - accepted/best-paper examples relevant to this manuscript.
- `MAIN_TEX_TO_ICNP_CHECKLIST.md` - concrete conversion checklist for `main.tex`.
- `PITFALLS_REVIEWER_EXPECTATIONS.md` - likely reviewer expectations and avoidable failure modes.
- `TIMELINE_AND_GIT_WORKFLOW.md` - sprint timeline and recommended git workflow.
- `SOURCES_AND_LINKS.md` - official links and example-paper links.

## Current repo state

The pre-heavy-edit manuscript state was archived at:

```text
archive/pre-venue-main-2026-04-28/main.tex
```

Use `main.tex` as the active ICNP working draft after this point.

## Most important warning

The current paper includes public reproducibility links in the abstract/contribution/appendix. ICNP uses double-blind review, and recent ICNP CFPs encourage artifact release only upon acceptance to preserve anonymity. Before submission, remove or anonymize public GitHub/Drive links from the blind build.
