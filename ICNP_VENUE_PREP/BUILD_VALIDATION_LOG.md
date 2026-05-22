# ICNP Overleaf/PDF Validation Log

This log records non-destructive Overleaf/PDF validation for `ICNP_2026_venue_draft.tex`.

## Validation pass: May 21 image-first graph cleanup

- **Date:** 2026-05-22
- **Active draft:** `ICNP_2026_venue_draft.tex`
- **Purpose:** Validate the source-regenerated image batch requested from the May 21 meeting transcript without reopening broad formatting or page-flow work.

What was checked:

- [x] Python figure generators compile in the `.quantum` environment:
  - `figures/icnp-exported-assets/build_G8_G9.py`
  - `figures/icnp_figures/icnp_graphs.py`
  - `figures/icnp_graphs/code_and_plots/script.py`
- [x] Affected manuscript-facing PNGs were regenerated from source scripts, preserving existing active LaTeX include paths.
- [x] Regenerated figures were visually checked for captioned-value visibility and label alignment.
- [x] Full draft compiled locally with `latexmk -pdf -interaction=nonstopmode -halt-on-error ICNP_2026_venue_draft.tex`.
- [x] Generated PDF remains 18 pages total.
- [x] Conclusion remains on page 10 and References begin on page 11.
- [x] PDF spot-check pages 5--10 were rendered and visually inspected for affected main-body figures.

Observed outcome:

- The image batch did not introduce missing-graphic errors or LaTeX build failures.
- Figures 3, 4, 5, 6A, 6B, 7B, 8A, 8B, 10, and 13 now better expose the values or labels used by their captions.
- A surgical follow-up corrected the Figure 5 legend placement and mean-label side, restored the Figure 6A drop/recovery shadows, cleaned the Contextual-vs-EXP3 numeric labels, and removed Figure 13C bar numbers while adding A--D panel subtitles.
- Remaining LaTeX warnings are consistent with existing draft noise: underfull/overfull boxes, duplicate PDF-destination warnings, and appendix/floating behavior. No broad formatting fix was attempted in this image-first pass.

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

### Figure-resolution refresh for manuscript-facing PNG assets

- **Date:** 2026-05-11
- **Scope:** Active ICNP draft figure assets under `figures/icnp/` that were still being exported from Plotly at the default `700x500` size.
- **Root cause:** Several paper-facing Plotly figures were being written with Plotly's default raster export size, which left them at roughly `200 dpi` when placed at `\columnwidth` or `0.48\textwidth` in the draft.
- **Fix applied:** Updated the owning Plotly exporters to route all PNG writes through a shared `EXPORT_SCALE` setting (`ICNP_PLOT_SCALE`, default `3`) so the same figure layout is exported at higher pixel density without changing the visual design.

Owning source files updated:

- `figures/icnp_figures/icnp_graphs.py`
- `figures/icnp_graphs/code_and_plots/script.py`

Manuscript-facing assets refreshed from regenerated source outputs:

- `figures/icnp/ICNP-CODE-039_g1_capacity_paradox.png`
- `figures/icnp/ICNP-CODE-040_g2_robustness_floor.png`
- `figures/icnp/ICNP-CODE-041_g3_family_summary.png`
- `figures/icnp/ICNP-CODE-042_g4_deployment_rules.png`
- `figures/icnp/ICNP-CODE-053_fig6_context_capacity.png`
- `figures/icnp/ICNP-CODE-056_fig10_threat_rules.png`

Measured result:

- Previous raster size for each affected asset: `700x500`
- New raster size for each affected asset: `2100x1500`
- Effective print density after refresh:
  - about `600 dpi` at `\columnwidth`
  - about `611 dpi` at `0.48\textwidth`

Validation performed:

- [x] Regenerated the owning Plotly outputs after the exporter change.
- [x] Confirmed regenerated outputs are `2100x1500`.
- [x] Replaced the active draft asset files at the same paths so no LaTeX include path changes were required.

Remaining recommended check:

- [ ] Recompile the active Overleaf project and visually inspect the PDF to confirm the refreshed raster assets render sharply in the manuscript.

### Full-paper source/PDF spot-check after image refresh

- **Date:** 2026-05-11
- **Active draft:** `ICNP_2026_venue_draft.tex`
- **Purpose:** Confirm that the full draft still compiles after the image refresh, remove any still-rendered feedback markers from the active draft path, and visually spot-check the compiled PDF pages that contain refreshed figures.

What was checked:

- [x] The active draft compiled locally via `latexmk -pdf`.
- [x] The generated PDF remained at 15 pages.
- [x] No missing-graphics warnings were reported for the active draft build.
- [x] The refreshed manuscript-facing PNGs were present in the compiled PDF.
- [x] A rendered feedback-marker leak in the cross-testbed caption was removed from the active draft path.
- [x] Additional uncommented reviewer markers in the active appendix/Results fragments were converted to source comments or resolved prose so they no longer render in the PDF.
- [x] Rendered PDF spot-check pages containing refreshed figures were reviewed after recompilation.

Observed outcome:

- The refreshed figures render sharply in the compiled PDF pages spot-checked from the active draft.
- The previously visible red reviewer note in the cross-testbed figure caption no longer appears in the PDF.
- The remaining compile noise is from pre-existing layout/reference behavior, including duplicate PDF destination warnings, underfull/overfull box warnings, and `h` to `ht` float adjustments; no new image-pipeline regression was introduced by this pass.

Follow-up still expected outside this local validation pass:

- [ ] Recompile/sync in Overleaf and confirm the same clean PDF state there before any external submission handoff.

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
