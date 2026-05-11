# ICNP Overleaf/PDF Validation Log

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

### Source-level reference/citation pass

- **Date:** 2026-05-11
- **Scope:** Active venue draft path only: `ICNP_2026_venue_draft.tex`, `02--related_works.tex`, included ICNP staging files, and included appendix files.
- **Purpose:** Catch obvious undefined-reference or missing-bibliography issues before relying on the Overleaf warning panel.

Checked:

- [x] Empty citation placeholders such as `\cite{}` were not found in the active draft path.
- [x] Historical `\Cref{sec:testbed_comparison}` / `\ref{sec:testbed_comparison}` hits were confined to old/reference material, not the active venue draft path.
- [x] Active `\cite{...}` keys inspected during the pass are present in `refs.bib`.
- [x] Active cross-testbed references use the current labels/macros, including `\paperTwo`, `\paperSeven`, `\paperTwelve`, `\paperEight`, `tab:testbed_comparison_full`, and `tab:model_family_comparison_full`.
- [x] No source-level undefined-reference fix was applied in this pass.

Important limitation:

- This is not a replacement for the Overleaf warning panel. LaTeX can still report unresolved references/citations because of aux-file state, package behavior, duplicate labels, or generated-output issues. Any warning from Overleaf should override this source-level preflight.

### Standing tracked metrics

These are not standalone tasks. They are constraints/metrics to keep tracking as the draft changes:

- **Page budget:** main paper must remain within the ICNP main-body limit.
- **Commenting state:** final rendered-marker/source sweep remains blocked until advisors/reviewers are done commenting.
- **Double-blind state:** identifying acknowledgments, public artifact links, and PDF metadata must remain absent from the review submission.

### Current actionable validation checks

The active draft is expected to compile in Overleaf. The useful work now is to inspect the Overleaf warning panel and generated PDF for issues introduced by recent edits:

- [x] Source-level undefined-reference/citation preflight completed; no active-path fix required.
- [ ] Overleaf warning-panel review for undefined references/citations.
- [ ] Missing figure-file warnings.
- [ ] Significant overfull boxes that visibly affect layout.
- [ ] Figure/table float order and page-flow issues in the generated PDF.
- [ ] Appendix float order and page breaks in the generated PDF.
- [ ] Page-budget regression, if recent edits pushed the main body over the tracked limit.
- [ ] PDF font embedding check, if available from the exported PDF.
- [ ] PDF metadata/anonymity check, after the final source sweep.

### Practical Overleaf validation procedure

1. Open the active Overleaf project and confirm it is synced to the current GitHub state.
2. Recompile in Overleaf.
3. Check the Overleaf warning panel for:
   - undefined references;
   - undefined citations;
   - missing graphics;
   - serious overfull boxes.
4. Open the generated PDF and record:
   - whether the main body remains within the already tracked page budget;
   - whether figures/tables land near the claims they support;
   - whether appendix tables/figures overflow or appear in a confusing order.
5. Record findings here only when there is a change, regression, or issue worth tracking.

## Final-gate blocker

The final rendered-marker/source sweep is intentionally blocked until all advisors/reviewers confirm they are done commenting. Do not remove source comments or neutralize feedback macros before that point.
