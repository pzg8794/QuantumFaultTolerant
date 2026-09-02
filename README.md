# QuantumFaultTolerant Paper Workspace

This repository contains the quantum entanglement routing manuscript and the documentation needed to prepare it for conference and journal submission.

## Current Working State

- `ICNP_2026_venue_draft.tex` is the active post-ICNP manuscript source.
- `main.tex` is the original/reference manuscript and is not the primary venue-draft edit target.
- `updates/` contains the concise advisor-facing status page and links to optional supporting evidence.
- `dan-legacy-drafts/` contains Dan/legacy-owned planning drafts that are preserved for historical context and are not part of the active manuscript build.
- `archive/` is reserved for manuscript source checkpoints only.
- `historical-patches/` contains historical patch files, reviewer/Overleaf feedback provenance, and older tracking material.
- `ICNP_VENUE_PREP/` contains the ICNP venue-preparation reference pack.
- `ICNP_RECENT_TOP_PAPERS/` is the staging/reference area for recent ICNP papers used as style and positioning examples.
- `JOURNAL_SUBMISSION_PREP/` contains the checklist for later journal-version preparation.

## Directory Map

- `updates/` - concise advisor-facing progress, schedule, and optional evidence links.
- `ICNP_VENUE_PREP/` - indexed active audit, validation, feedback-resolution, and manuscript staging records.
- `archive/` - dated manuscript source checkpoints only.
- `dan-legacy-drafts/` - Dan/legacy-owned draft material moved out of `archive/` for visibility.
- `historical-patches/` - historical feedback, patch, and tracking provenance.
- `ICNP_RECENT_TOP_PAPERS/` - placeholder/manifest area for recent ICNP reference papers.
- `JOURNAL_SUBMISSION_PREP/` - journal-readiness checklist and planning notes.
- `references/` - source PDFs used for literature and related-work support.
- `sections/` - manuscript sections split out from or used with `main.tex`, where applicable.

## Local-Only Directories

The following directories are intentionally ignored and should remain local-only unless explicitly needed in the remote repository:

- `scripts/`
- `tools/`
- `.auth/`

Generated PDFs and LaTeX build artifacts are also ignored.

## Workflow

1. Pull `origin/main` before starting a paper pass.
2. Read `updates/README.md` for the advisor-facing status and current schedule.
3. Use `ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md` and the linked evidence records for implementation detail.
4. Archive manuscript checkpoints under `archive/manuscript-checkpoints/` before large venue-specific rewrites.
5. Keep superseded reviewer/feedback provenance under `historical-patches/`, not under `archive/`.
6. Leave `dan-legacy-drafts/` content untouched unless Dan or the project owner explicitly requests changes.
7. Keep local helper scripts/tools off the remote branch.
8. Keep generated PDFs local unless a PDF is deliberately restored to Git.
9. Commit focused changes with a message that names the paper workflow step.
