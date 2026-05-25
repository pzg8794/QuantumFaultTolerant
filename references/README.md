# References

This directory stores source PDFs and reference material used while preparing the manuscript.

## Layout

- `pdfs/` - source papers and imported related-work PDFs.
- `pdfs/from_main_tex/` - PDFs imported from citations or references discovered from `main.tex`.

Bibliographic entries used by the active manuscript live in the root `refs.bib`.

## Curation rules

- Keep only literature that supports current manuscript claims, comparisons, or methodology context.
- Prefer canonical publisher or arXiv copies when duplicates exist.
- Use descriptive, stable filenames to avoid ambiguity during reviewer-response cycles.

## Reproducibility note

- When adding a new paper PDF, also confirm the matching citation entry exists (or is queued) in `refs.bib`.
- Remove stale references only when they are no longer cited and no longer needed for venue rebuttal context.
