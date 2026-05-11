# ICNP Build Validation Log

This log records non-destructive Overleaf/PDF validation for `ICNP_2026_venue_draft.tex`.

## Validation pass: source-level preflight after feedback cleanup

- **Date:** 2026-05-11
- **Active draft:** `ICNP_2026_venue_draft.tex`
- **Relevant recent commits:**
  - `ac5ceb609842cc6220639fb73ce5883ac822b6d4` — omitted rendered acknowledgments for double-blind review.
  - `bde8c9b99ae15a87b6b06b4309f3ed1cd7ec1b88` — documented blind-review acknowledgment cleanup.
- **Validation type:** Source-level preflight plus Overleaf/PDF validation checklist. Overleaf is the expected compile environment.

### What was checked from source

- [x] Active draft uses IEEE conference mode: `\documentclass[10pt,conference]{IEEEtran}`.
- [x] Active draft uses anonymous author block: `\author{Anonymous Authors}`.
- [x] Rendered acknowledgments section was removed from the blind-review draft path.
- [x] A source-only note remains for camera-ready acknowledgment restoration after acceptance.
- [x] `refs.bib` exists in the repository and contains bibliography entries used by the draft.
- [x] The active draft still wires in the expected staging files:
  - `02--related_works`
  - `ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex`
  - `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`
  - `ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED`
  - `ICNP_VENUE_PREP/DISCUSSION`
  - `ICNP_VENUE_PREP/FUTURE_WORK`
  - `ICNP_VENUE_PREP/CONCLUSION`
  - appendix files under `ICNP_VENUE_PREP/`.

### What remains to check in Overleaf/PDF output

The active draft is expected to compile in Overleaf. The remaining task is not "make LaTeX compile"; it is to inspect the Overleaf output and exported PDF for submission risks:

- [ ] Main-body page count.
- [ ] Overleaf warnings for undefined references/citations.
- [ ] Overleaf warnings for missing figure files.
- [ ] Significant overfull boxes that visibly affect layout.
- [ ] Figure/table float order and page-flow issues in the generated PDF.
- [ ] Appendix float order and page breaks in the generated PDF.
- [ ] PDF font embedding check, if available from the exported PDF.
- [ ] PDF metadata/anonymity check, after the final source sweep.

### Practical Overleaf validation procedure

1. Open the active Overleaf project and confirm it is synced to the current GitHub state.
2. Recompile.
3. Check the Overleaf warning panel for:
   - undefined references;
   - undefined citations;
   - missing graphics;
   - serious overfull boxes.
4. Open the generated PDF and record:
   - main-body page count before references/appendices;
   - whether figures/tables land near the claims they support;
   - whether appendix tables/figures overflow or appear in a confusing order.
5. Record the findings in this file.

## Final-gate blocker

The final rendered-marker/source sweep is intentionally blocked until all advisors/reviewers confirm they are done commenting. Do not remove source comments or neutralize feedback macros before that point.
