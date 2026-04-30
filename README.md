# QuantumFaultTolerant Paper Workspace

This repository contains the quantum entanglement routing manuscript and the documentation needed to prepare it for conference and journal submission.

## Current Working State

- `main.tex` is the active manuscript working draft.
- `dan-legacy-drafts/` contains Dan/legacy-owned planning drafts that are preserved for historical context and are not part of the active manuscript build.
- `archive/` is reserved for manuscript source checkpoints only.
- `historical-patches/` contains historical patch files, reviewer/Overleaf feedback provenance, and older tracking material.
- `ICNP_VENUE_PREP/` contains the ICNP venue-preparation reference pack.
- `ICNP_RECENT_TOP_PAPERS/` is the staging/reference area for recent ICNP papers used as style and positioning examples.
- `JOURNAL_SUBMISSION_PREP/` contains the checklist for later journal-version preparation.

## Directory Map

- `archive/` - dated manuscript source checkpoints only.
- `dan-legacy-drafts/` - Dan/legacy-owned draft material moved out of `archive/` for visibility.
- `historical-patches/` - historical feedback, patch, and tracking provenance.
- `ICNP_VENUE_PREP/` - ICNP requirements, submission notes, venue-fit guidance, and conversion checklists.
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
2. Archive `main.tex` before large venue-specific rewrites using a dated path under `archive/manuscript-checkpoints/`.
3. Keep reviewer/feedback provenance under `historical-patches/`, not under `archive/`.
4. Leave `dan-legacy-drafts/` content untouched unless Dan or the project owner explicitly requests changes.
5. Keep local helper scripts/tools off the remote branch.
6. Keep generated PDFs local unless a PDF is deliberately restored to Git.
7. Commit focused changes with a message that names the paper workflow step.
