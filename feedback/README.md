# Feedback Workspace

This directory stores reviewer-feedback artifacts used to turn Overleaf comments and review notes into concrete paper edits.

## File Types

- `item_*.md` - individual feedback tickets.
- `overleaf_feedback_*mapping*.md` - mapping notes between Overleaf feedback and manuscript source text.
- `overleaf_feedback_*review*.md` - working review queues produced or refined from crawler output.

## Local Generated Files

The crawler may generate:

- `overleaf_feedback_raw.json`
- `overleaf_feedback_queue.md`

Raw JSON output is ignored by Git. Markdown review queues may be committed only after they have been reviewed and are useful as paper-workflow records.
