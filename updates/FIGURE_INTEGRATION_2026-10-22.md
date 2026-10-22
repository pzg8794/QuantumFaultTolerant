# Accepted medium figures integrated — October 22, 2026

## Authority and scope

Piter requested completion of the previously authorized figure integration. The independent Viber/latest-model and Perplexity comparison supported the new action-exposure design and appendix placement of block-resolved route exposure, with explicit safeguards for OnlineAdaptive. Those presentation corrections are implemented; no new scientific analysis, simulator execution, manuscript-wide revision, or historical-result reinterpretation is included.

Source package manifest: `3835ec30494d82cb24d17688649e1868d40f6c8953f602e43333049cfce6ef28`. All 49 source artifacts match their frozen hashes. The original analysis packages and earlier figure-review candidates are preserved.

## Placement

| View | Manuscript figure | Page | Placement |
|---|---|---|---|
| Efficiency trajectory | 9 | 12 | Medium Results |
| Action coverage and top-five concentration | 10 | 13 | Medium Results |
| Structural-zero trajectory | 14 | 23 | Accepted Medium-Campaign Diagnostics appendix |
| Oracle continuous-payoff gap | 15 | 24 | Same appendix |
| OnlineAdaptive availability/normalization | 16 | 25 | Same appendix |
| Block-local route exposure | 17 | 26 | Same appendix |

The main body explicitly references the appendix diagnostics. The appendix is flushed before the algorithm specification so unrelated algorithm text does not separate its figures. The trajectories retain all original values, windows, line styles, and ranges; their layout is changed from five very small panels in one row to a readable two-row grid at manuscript width.

## Reviewer safeguards implemented

- OnlineAdaptive retains exact zeros with axis margin, not a positive offset. The symlog threshold is 0.01%. Captions distinguish 60,000 route-frames from 6,000 decisions per block, overlapping zero categories, equal-block ratios, the two denominator histories, Oracle privilege, and all-routes-down fallback choices.
- Action coverage uses 550 route/action pairs; top-five concentration uses 6,000 selections and a separately selected frequency-based top five per policy/threat/block. Open block markers and min–max ranges are not confidence intervals or significance evidence.
- Route exposure retains original block-local identities and one common ±1.1 percentage-point scale around 10%, with the absolute range printed. White is observed equal share, not missingness. The caption excludes fairness/optimality, temporal-uniformity, random-selection, and mechanism claims.
- Oracle-gap trajectory is an absolute difference in continuous payoff per frame, not a percentage-point efficiency gap. Its caption matches the accepted `oracle_gap_mean` definition.

## Validation

- Full campaign identities retained: 75 cells, 6,000 frames each, five models and five threats, three blocks.
- 720 trajectory rows match accepted plot data within `rtol=1e-12, atol=1e-14`; 210 plotted block values match accepted summaries to a maximum absolute difference of `7.105427357601002e-15`; all 600 block-local route shares are preserved and each cell sums to 100%.
- Full `latexmk -pdf -interaction=nonstopmode -halt-on-error` build succeeds: 29 pages, with figure/table/equation references resolved and no new overfull horizontal boxes or missing citations.
- Existing warnings remain: page 8 contains only floats, a 0.95433pt vertical overflow, three Times small-cap italic font fallbacks, and underfull boxes. These were present before this figure integration.
- Final-size PDF pages for all six views were rendered and visually inspected; zero markers, legends, axes, captions, and cross-references checked. Manuscript vector PDFs are used, not raster screenshots.
- The pre-integration 24-page review PDF remains preserved separately from the earlier 18-page baseline. Neither original checkout nor Overleaf was overwritten.

## Remaining gates and source boundaries

This is a review candidate, not submission clearance: 29 pages exceed the documented initial journal limit, and previously recorded manuscript-wide wording/provenance/human review gates remain open. No cause of the historical 100-node result is asserted. Prototype website deployment is not part of this figure integration.

The isolated branch `codex/reviewer-closure-20261018` owns this candidate. The existing restricted campaign manuscript mirror is `https://drive.google.com/drive/folders/10U3LJBsKAV1Elxz6TWdHA4BvrS6PSzZO`; final upload and Git receipts are recorded with the private presentation artifacts. No private traces, derived CSV tables, reviewer transcripts, or credentials are published in this repository. Original local-main/GitHub/Overleaf divergence is preserved, not silently resolved.
