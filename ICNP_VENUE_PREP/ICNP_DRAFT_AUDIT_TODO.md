# ICNP Draft Audit TODO Tracker

This checklist ties the content-reduction audit to the ICNP venue-preparation requirements. Update it as each section is reviewed and accepted into `ICNP_2026_venue_draft.tex`.

## Draft mechanics

- [x] Create a runnable ICNP draft file separate from `main.tex`.
- [x] Keep `main.tex` untouched while section reductions are being audited.
- [x] Copy the current abstract into the runnable draft for context.
- [x] Stage accepted Background reductions in `ICNP_2026_venue_draft.tex`.
- [x] Add the framework figure to the draft for early figure/caption/layout review.
- [ ] Add remaining figure environments from `main.tex` as their sections are reached in the audit.
- [ ] Confirm the draft compiles in IEEE conference mode.
- [ ] Confirm page count once enough sections are staged.

## ICNP compliance checks to handle during audit

- [ ] Abstract under 250 words.
- [ ] Double-blind author block; remove names, affiliations, acknowledgments that identify authors, and other identifying metadata for the review version.
- [ ] Remove or anonymize public GitHub/Drive artifact links from the blind submission draft.
- [ ] Remove rendered author/reviewer comments such as `\shee{}`, `\todo{}`, `\dan{}`, `\devroop{}`, and `\piter{}` before submission.
- [ ] Ensure IEEE conference mode remains active.
- [ ] Use US Letter page size with the required IEEE conference style.
- [ ] Keep main body within 10 pages excluding references.
- [ ] Keep core claims in the main body, not only in appendix/supplement.
- [ ] Ensure all fonts are embedded in the PDF.
- [ ] Ensure the PDF displays and prints correctly with standard tools and printers.
- [ ] Ensure all figures are readable in one-column/two-column ICNP layout.
- [ ] Ensure all figure captions are concise and takeaway-oriented.
- [ ] Use color when helpful, but never rely on color alone; plots and graphs must remain distinguishable when printed on black-and-white printers.
- [ ] Check no overfull figure/table content crosses columns.

## Background audit status

- [x] Quantum Networks and Entanglement Routing — split, reduced, documented, added to draft.
- [x] The Multi-Armed Bandit Abstraction — split, reduced, documented, added to draft.
- [ ] Allocation and Capacity Semantics — pending split/reduction.
- [ ] Problem Scope — pending split/reduction.

## Figure audit status

- [x] `fig:framework` — copied to draft for visual review.
- [x] `fig:network_topology` — restored color coding plus line-style redundancy for black-and-white readability.
- [x] Result placeholder figures — color restored with redundant encodings in generated PGFPlots files.
- [ ] Replace temporary generated PGFPlots with final notebook-exported image plots once graph choices are finalized.

## Notes

Use this tracker alongside:

- `ICNP_VENUE_PREP/BACKGROUND_REDUCTION_AUDIT.md`
- `ICNP_VENUE_PREP/MAIN_TEX_TO_ICNP_CHECKLIST.md`
- `ICNP_VENUE_PREP/FIGURE_COLOR_ACCESSIBILITY_NOTE.md`
