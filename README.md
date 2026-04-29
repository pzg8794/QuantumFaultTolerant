# QuantumFaultTolerant Paper Workspace

This repository contains the quantum entanglement routing manuscript, review workflow notes, venue-preparation material, and local tooling used to prepare the paper for submission.

## Current Working State

- `main.tex` is the active ICNP venue-paper working draft.
- `archive/manuscript-checkpoints/pre-venue-main-2026-04-28/main.tex` preserves the pre-heavy-edit manuscript checkpoint.
- `docs/venue/icnp_2026/` is the primary venue-preparation folder for ICNP 2026.
- `docs/tracking/PAPER-CHANGES-TRACKER.md` is the canonical paper-change log.
- `feedback/` stores reviewer-feedback work items and Overleaf crawler review queues.

## Directory Map

- `archive/` - historical snapshots, old drafts, and applied patch records.
- `docs/` - venue prep, tracking, templates, and workflow documentation.
- `feedback/` - review-comment work items, crawler output queues, and mapping notes.
- `references/` - source PDFs used for literature and related-work support.
- `scripts/` - paper-support scripts, including the read-only Overleaf feedback crawler.
- `sections/` - manuscript sections split out of `main.tex`.
- `tools/` - manuscript table/reference utilities.

## Workflow

1. Pull `origin/main` before starting a paper pass.
2. Archive `main.tex` before large venue-specific rewrites.
3. Record reviewer or venue-prep decisions in `docs/tracking/PAPER-CHANGES-TRACKER.md`.
4. Keep generated browser state and raw crawler output out of Git.
5. Keep generated PDFs local; `*.pdf` files are ignored unless deliberately restored to Git.
6. Commit focused changes with a message that names the paper workflow step.
