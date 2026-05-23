# Active Feedback Resolution Log

This log records feedback-resolution batches applied to the active ICNP venue draft. It complements the per-section audit notes and follows the repository process in `AGENTS.md`: identify the owning file, make the smallest safe change, preserve validated content, and keep reviewer feedback traceable as LaTeX source comments with `SOLVED` explanations.

## Batch: May 23 appendix figure grouping/caption style

- **Owning files changed:** `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`
- **Reason for batching:** The appendix `Context-Capacity Interaction` and `Threat-Conditioned Deployment Rules` figures should follow the same two-panel style as the other double figures, and the grouped synthesis panels needed wider presentation with concise show/evidence/meaning captions.
- **Change:** Converted the two standalone appendix support figures into one two-panel figure, equalized the two panel image heights, widened the four grouped synthesis panel slots, rewrote each subcaption to state what the panel shows/evidences/means, and made the nearby appendix prose reference the correct appendix figure labels.
- **Validation:** Full LaTeX compile passed; PDF remains 16 pages. Appendix pages 13--14 were rendered and inspected to confirm Figures 11--12 fit and captions are visible.

### Follow-up: Appendix support four-panel validation update

- **Reason for follow-up:** The two-panel appendix support view still looked visually similar across panels, and the validation hub needed to reflect the active paper figure set.
- **Change:** Folded the standalone Contextual-vs-EXP3 Oracle-gap diagnostic into the appendix support figure and added the notebook-validated qubit-budget heatmap, producing a four-panel appendix figure without duplicating the Oracle-gap image elsewhere.
- **Validation:** Active figure-reference audit reports no missing figure labels, and the active includegraphics audit reports no exact duplicate image files used in the paper.

### Follow-up: Appendix support capacity-paradox expansion

- **Reason for follow-up:** The appendix support figure needed the missing capacity-paradox evidence chain: replay efficiency by capacity level, regret over capacity steps, and paired replay-scaling deltas.
- **Change:** Replaced the `Threat-Conditioned Deployment Rules` panel with the capacity-paradox trajectory asset (`ICNP-CODE-008`; the current manifest maps `ICNP-CODE-057` to a convergence image), added the regret-trajectory panel (`ICNP-CODE-009`), then replaced the older gray replay-delta panel with the clearer color-coded advanced-synthesis Panel B replay drop/recovery boxplot (`ICNP-CODE-074`). Visible `G13`/`G14` source-generation labels were removed from paper-facing titles.
- **Validation:** Full LaTeX compile passed; PDF remains 16 pages. The validation hub reports 20/20 active images mapped, no exact duplicate active image files, no missing figure labels, and six distinct appendix support panels.

### Follow-up: Appendix caption/reference audit

- **Owning files changed:** `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `ICNP_VENUE_PREP/DISCUSSION.tex`
- **Reason for follow-up:** Figures 10 and 11 needed a final caption-process check, and the appendix diagnostic figures needed to be explicitly connected from the Discussion.
- **Change:** Tightened the Figure 10 and Figure 11 main captions to follow the same pattern as the subcaptions: what the grouped figure shows, which evidence is visible, and what larger claim it supports. Added a Discussion sentence that references both appendix diagnostic figure groups and states how they support the deployment interpretation.
- **Validation:** Full LaTeX compile passed; PDF is 17 pages. The figure-reference audit reports no missing figure labels, and both appendix diagnostic figure groups are now referenced from the Discussion.

### Follow-up: Figure 10(c)--(d) appendix readability

- **Owning files changed:** `figures/icnp_graphs/build_G10_G14.py`, `figures/icnp/ICNP-NOTEBOOK-053_g12_panel_a_efficiency_by_scenario.png`, `figures/icnp/ICNP-NOTEBOOK-054_g12_panel_b_stochastic_vs_adaptive_gap.png`
- **Reason for follow-up:** Figure 10(c) used abbreviated scenario labels, and Figure 10(d) used colored points without direct labels, making the panel less self-explanatory.
- **Change:** Regenerated only the active Figure 10(c)--(d) appendix panels from the G12 source script. Panel (c) now spells out `Baseline`, `Markov`, `Stochastic`, `Adaptive`, and `Online Adaptive`; panel (d) uses larger markers and direct model labels above the points.
- **Validation:** Full LaTeX compile passed; PDF is 16 pages. Appendix page 13 was rendered and inspected to confirm the scenario labels and point labels are visible.

### Follow-up: Figure 10(c)--(d) percentage labels and duplicate-title cleanup

- **Owning files changed:** `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `figures/icnp_graphs/build_G10_G14.py`, `figures/icnp/ICNP-NOTEBOOK-053_g12_panel_a_efficiency_by_scenario.png`, `figures/icnp/ICNP-NOTEBOOK-054_g12_panel_b_stochastic_vs_adaptive_gap.png`
- **Reason for follow-up:** The active appendix Figure 10(c)--(d) panels still carried an internal plot title directly under the LaTeX panel title, and the visible values were not consistently marked as percentages.
- **Change:** Removed the internal Plotly titles from the two active panels, added positive spacing between the LaTeX panel title and the image, added percentage labels to the Figure 10(c) bars, and added percentage coordinates to the Figure 10(d) direct point labels.
- **Validation:** Full LaTeX compile passed; PDF is 16 pages. Appendix page 13 was rendered and inspected to confirm the duplicate titles are gone and the percentage values remain readable.

## Batch: May 23 Figure 11 restyle

- **Owning files changed:** `figures/icnp-exported-assets/build_G8_G9.py`, `figures/icnp/ICNP-CODE-053_fig6_context_capacity.png`, `figures/icnp/icnp_validation_image_manifest.csv`, `ICNP_VENUE_PREP/BUILD_VALIDATION_LOG.md`
- **Reason for batching:** The retained standalone `Context-Capacity Interaction` figure needed to look like the former grouped synthesis Panel D, because that grouped panel had been replaced by Replay-Configuration Sensitivity.
- **Change:** Added a reproducible standalone context-capacity export path to the Matplotlib generator and regenerated the existing Figure 11 image path without changing the underlying data or LaTeX label.
- **Validation:** Full LaTeX compile passed with no unresolved references; PDF remains 16 pages. Page 13 was rendered and inspected, and the page-9 font warning was triaged in `BUILD_VALIDATION_LOG.md`.

## Batch: May 22 appendix duplicate-figure consolidation

- **Owning files changed:** `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`, `ICNP_VENUE_PREP/DISCUSSION.tex`, `figures/icnp-exported-assets/build_G8_G9.py`, `ICNP_VENUE_PREP/FIGURE_SELECTION_AUDIT.md`
- **Regenerated asset:** `figures/icnp/ICNP-CODE-024_g8_advanced_4panel_grouped_full_figure.png`
- **Reason for batching:** The appendix had duplicate capacity/replay diagnostics. The previous grouped synthesis Panel D duplicated the standalone Context-Capacity Interaction figure, so Panel D was repurposed to carry the original Replay-Configuration Sensitivity line view while the standalone context-capacity evidence was retained.
- **Change:** Removed the standalone replay-sensitivity line figure, retained the standalone Context-Capacity Interaction figure as the kept copy, regenerated that retained figure with the same Matplotlib style/data view as the former grouped Panel D, updated grouped synthesis Panel D/caption/context to the replay-sensitivity view, and set the two main-body Figure 6 panels to matching image heights.
- **Validation:** Full LaTeX compile passed with no unresolved references; PDF is 16 pages total. Main-body page 7 and appendix pages 12--14 were rendered and visually inspected.

## Batch: May 22 replay-sensitivity image swap

- **Owning files changed:** `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`, `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md`
- **Reason for batching:** The main-body Replay-Configuration Sensitivity panel should use the bar rendering, while the original line rendering remains available in the appendix for traceability.
- **Change:** Swapped the main-body and appendix image references without changing underlying data or regenerating figures.
- **Validation:** Full LaTeX compile passed with no unresolved references; PDF remains 17 pages, and the affected main-body and appendix pages were visually inspected.

## Batch: May 22 appendix-reference and replay-sensitivity bar-alternative pass

- **Owning files changed:** `ICNP_2026_venue_draft.tex`, `ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex`, `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `figures/icnp-exported-assets/build_G8_G9.py`, `ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md`
- **Generated asset:** `figures/icnp/ICNP-CODE-073_fig6b_replay_configuration_sensitivity_bar_alternative.png`
- **Reason for batching:** The May 22 transcript asked for a surgical follow-up: briefly reference the moved framework figure in the Introduction, describe it in the appendix, ensure appendix figures/tables are connected to text, and add a bar version of the Replay-Configuration Sensitivity panel for advisor feedback without replacing the main-body line plot yet.

### Resolved feedback / cleanup

1. **Moved framework figure reference**
   - **Issue:** The former Figure 1 evaluation pipeline was moved to the appendix, but the Introduction still needed a brief description that points readers to the appendix figure.
   - **Change:** Reworded the Introduction sentence to describe the five matched inputs and explicitly identify the pipeline diagram as an appendix figure.

2. **Appendix framework description**
   - **Issue:** The appendix version of the framework figure needed its own description rather than relying only on the caption.
   - **Change:** Added a short paragraph before the framework figure explaining how topology, threat regime, policy family, allocator choice, and replay semantics feed the matched evaluation grid.

3. **Appendix figure/table connector coverage**
   - **Issue:** Appendix figures and tables needed to be explicitly referenced or addressed in nearby prose.
   - **Change:** Kept the setup tables/framework references, added the new replay-sensitivity alternative connector, and preserved explicit references to the diagnostic appendix figures and full-result appendix tables.

4. **Replay-Configuration Sensitivity bar alternative**
   - **Issue:** The requested bar-chart alternative targeted the Replay-Configuration Sensitivity panel, not the threat-escalation heatmap.
   - **Change:** Replaced the appendix review option with a full-width bar alternative generated from the same validated replay-configuration values and left the main-body line plot unchanged.

### Validation status

- [x] Pulled latest GitHub paper state before editing (`73a6b0f`, `Updates from Overleaf`).
- [x] Python figure generator compiles in the `.quantum` environment.
- [x] Full LaTeX compile completed with no unresolved references.
- [x] Generated PDF remains 17 pages total with Conclusion on page 10 and References starting on page 11.
- [x] Appendix pages visually inspected for the new replay-sensitivity bar alternative and diagnostic figure connector order.

## Batch: May 21 image-first graph cleanup

- **Owning files changed:** `figures/icnp-exported-assets/build_G8_G9.py`, `figures/icnp_figures/icnp_graphs.py`, `figures/icnp_graphs/code_and_plots/script.py`, `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`, `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`
- **Regenerated assets:** `figures/icnp/ICNP-CODE-024_g8_advanced_4panel_grouped_full_figure.png`, `ICNP-CODE-033`, `ICNP-CODE-035`, `ICNP-CODE-036`, `ICNP-CODE-037`, `ICNP-CODE-038`, `ICNP-CODE-039`, `ICNP-CODE-040`, `ICNP-CODE-041`, and `ICNP-CODE-056`
- **Reason for batching:** The May 21 transcript prioritized image-internal fixes before broad formatting. This batch updates generated figures and only touches nearby LaTeX when the image/caption alignment required it. No table values, result claims, or broad page-flow changes were made.
- **Follow-up correction:** A surgical correction restored the Figure 6A drop/recovery shadows, moved the Figure 5 legend inside the plot near the 40--60 x-axis region, moved orange mean labels left, converted Contextual-vs-EXP3 numeric labels to black without repeated `pp`, and removed bar numbers from Figure 13C while adding short A--D panel subtitles.

### Resolved feedback / cleanup

1. **Figure 3: variant grouping and redundant labels**
   - **Issue:** The RQ1 tier plot made variant groupings harder to connect to the caption and carried redundant right-side label clutter.
   - **Change:** Regenerated the panel with visible tier/value labels, no redundant right-side text boxes, and a caption that explicitly names `CPursuit`, `CEpsGreedy`, and `iCEpsGreedy`.

2. **Figure 4: threat-penalty naming**
   - **Issue:** The graph labels needed to match the caption, especially for `EXPNeuralUCB` and `OnlineAdaptive`.
   - **Change:** Regenerated the threat-penalty panel with full `EXPNeuralUCB` and `OnlineAdaptive` labels and visible bar values.

3. **Figure 5: robustness-floor readability**
   - **Issue:** The legend and 85% threshold annotation could overlap plotted labels.
   - **Change:** Moved the legend below the plot and shifted the threshold label so floor/mean/peak values remain readable.

4. **Figures 6A and 6B: capacity-paradox label support**
   - **Issue:** The compact plot used ambiguous shading, and the detailed replay plot was crowded while the caption depended on specific OnlineAdaptive values.
   - **Change:** Replaced shading with explicit drop/recovery callouts in Figure 6A and simplified Figure 6B to emphasize labeled OnlineAdaptive values and replay-configuration spans.

5. **Figures 7B, 8A, 8B, 10, and 13: caption-to-image alignment**
   - **Issue:** Several later figures needed clearer point labels, author/testbed labels, visible threshold labels, or removal of duplicate appendix content.
   - **Change:** Preserved the regenerated allocator-risk labels for the 88.9% vs 73.3% floor claim, replaced `Paper N`/`N` labels with author/testbed labels, strengthened the 85% threshold label, removed overlapping threat-rules text, and replaced the duplicate Figure 13 cross-testbed panel with context-capacity support.

### Validation status

- [x] Figure assets regenerated from source scripts, not manually edited PNGs.
- [x] Captioned values checked visually against regenerated images.
- [x] Python generator scripts compile in the `.quantum` environment.
- [x] Full LaTeX compile completed; generated PDF remains 18 pages total with Conclusion on page 10 and References starting on page 11.

## Batch: May 20 meeting cleanup

- **Owning files changed:** `ICNP_2026_venue_draft.tex`, `ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex`, `ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex`
- **Reason for batching:** The transcript-derived items were local venue-cleanup fixes: move the anonymous artifact link out of its own section, clarify the capacity-paradox contribution bullet, reference the allocator table, and stabilize appendix setup-float ordering. No result values, figure assets, or validated table values were changed.

### Resolved feedback / cleanup

1. **Repository-link placement**
   - **Issue:** The anonymous artifact link rendered as a standalone `Code Metadata` section below the abstract, costing space.
   - **Change:** Moved the same anonymous link to the final sentence of the Introduction, after the contribution bullets, and preserved Dan's original request as a solved source comment.

2. **Capacity-paradox contribution clarity**
   - **Issue:** The contribution bullet described `s=1` to `s=1.5` as "doubling" and did not state why the 15.6 pp allocator-floor shift matters.
   - **Change:** Replaced "doubling" with "increasing" and stated that allocator mismatch lowers worst-case floors, making the consequence explicit without changing the validated numbers.

3. **Allocator-table reference hygiene**
   - **Issue:** The allocator table remained useful in the main body but was not directly referenced.
   - **Change:** Added `\Cref{tab:setup-allocators}` to the allocator-strategy setup sentence.

4. **Appendix setup-float ordering**
   - **Issue:** The moved System Model appendix figure and setup tables could float past later appendix headings.
   - **Change:** Used fixed appendix placement for the setup figure/tables and inserted a page break before the detailed cross-testbed/model-family appendix section.

### Validation status

- [x] Full LaTeX compile completed with existing warning noise only.
- [x] References begin on page 11, preserving the 10-page main-body target.
- [x] Rendered reviewer-marker sweep found no visible feedback text from this batch.
- [x] Appendix setup material appears before the detailed cross-testbed/model-family tables.

## Batch: simple active-draft System Model feedback

- **Commit:** `c435b55f24ed0b05f1a18710ea2b5c834077ae17`
- **Owning file changed:** `ICNP_2026_venue_draft.tex`
- **Reason for batching:** The targeted comments were low-risk, local System Model fixes: missing citation support, threat-regime rationale, and confusing terminology around the no-disruption baseline. No results, figures, claims, or data values were changed.

### Resolved feedback

1. **Devroop: `\devroop{cite}` near path-level success**
   - **Issue:** The path-level success sentence stated that all links on a multi-hop path must succeed, but the supporting citation was missing.
   - **Change:** Added `\cite{briegel1998quantum,zukowski1993event}` to the multi-hop path-success sentence.
   - **Traceability marker:** Kept the original feedback as a LaTeX source comment with a `SOLVED` explanation.

2. **Dan: `Why were these regimes selected? Give a rationale, citations etc...`**
   - **Issue:** The threat taxonomy described a controlled escalation but did not clearly explain why each threat regime was selected.
   - **Change:** Replaced the thin threat-taxonomy introduction with a compact rationale mapping each regime to the routing difficulty it isolates. Added adversarial-bandit citations for adaptive/reactive disruption.
   - **Traceability marker:** Added a solved source comment next to the revised paragraph.

3. **Devroop: avoid confusing/repeated use of `benign`**
   - **Issue:** Using `benign operation` near `Baseline` could make readers wonder whether `benign` is another regime or simply a synonym for the no-disruption condition.
   - **Change:** Used `no-disruption operation` instead.
   - **Traceability marker:** Added a solved source comment next to the revised paragraph.

4. **Threat semantics clarification**
   - **Issue:** The concrete threat-regime sentence did not clearly distinguish Adaptive from OnlineAdaptive.
   - **Change:** Added `Adaptive reacts to recent routing behavior`, while OnlineAdaptive remains tied to current routing behavior.

### Validation status

- [x] Feedback markers are no longer rendered in the paper body.
- [x] Original feedback remains traceable as source comments.
- [x] No validated figures, tables, or data values were changed.
- [x] The changes match the prior threat-taxonomy audit decision.
- [ ] Full LaTeX compile/page-count validation still pending.

## Batch: Discussion and Conclusion rendered-marker cleanup

- **Discussion commit:** `8880cb3e55b5832722c3c51e9aa7d06aedfe69f6`
- **Conclusion commit:** `c341cfdb5bcfa1c9f61ecbb557b3a95c0b81ed60`
- **Owning files changed:** `ICNP_VENUE_PREP/DISCUSSION.tex`, `ICNP_VENUE_PREP/CONCLUSION.tex`
- **Reason for batching:** Both files contained visible audit/feedback placeholders in active manuscript sections. The changes removed rendered draft-review text and tightened prose without changing data values, figure assets, or the validated Results claims.

### Resolved feedback / cleanup

1. **Devroop: `go over this and rewrite as needed` in Discussion**
   - **Issue:** The active Discussion rendered both `Discussion section pending audit.` and a `\devroop{...}` feedback macro.
   - **Change:** Rewrote the Discussion as a concise synthesis of the validated Results claims: contextual policy robustness, conditional capacity paradox, and allocator choice as a deployment lever.
   - **Traceability marker:** Preserved the original feedback as a LaTeX source comment with a `SOLVED` explanation.

2. **Rendered pending-audit marker in Conclusion**
   - **Issue:** The active Conclusion rendered `Conclusion section pending audit.` in red text.
   - **Change:** Removed the rendered audit marker and kept the conclusion focused on the validated claims: threat-aware benchmark, contextual hybrid frontier, capacity paradox, allocator dependence, and future validation.
   - **Traceability marker:** Added a source comment noting the cleanup.

### Validation status

- [x] No reviewer/audit placeholder is rendered in Discussion.
- [x] No red pending-audit marker is rendered in Conclusion.
- [x] No validated result numbers were changed.
- [x] No figure/table assets were changed.
- [ ] Full LaTeX compile/page-count validation still pending.

## Batch: Blind-review acknowledgments cleanup

- **Commit:** `ac5ceb609842cc6220639fb73ce5883ac822b6d4`
- **Owning file changed:** `ICNP_2026_venue_draft.tex`
- **Reason for batching:** The active draft rendered an Acknowledgments section with hidden funding placeholders. For double-blind review, the acknowledgment section should not appear in the submitted PDF.

### Resolved compliance item

1. **Acknowledgments/funding anonymity**
   - **Issue:** The draft rendered an Acknowledgments section even though funding and grants are identifying information in a double-blind review version.
   - **Change:** Removed the rendered section and left a source comment: `Acknowledgments omitted from the double-blind review version. Restore camera-ready acknowledgments only after acceptance.`
   - **Traceability marker:** The camera-ready restoration instruction is preserved as a source comment.

### Validation status

- [x] No rendered Acknowledgments section remains in the active venue draft source.
- [x] No grant/funding placeholders remain rendered in the active venue draft source.
- [ ] PDF metadata/build validation still pending.
- [ ] Full LaTeX compile/page-count validation still pending.

## Remaining feedback-work policy

Simple feedback items can be batched when all of the following are true:

- the owning file is clear;
- the fix is local and mechanical;
- no result value, figure file, or claim interpretation changes;
- the original feedback can be preserved as a source comment with a short `SOLVED` explanation.

Larger feedback items should remain separate when they affect section structure, figure selection, results interpretation, double-blind compliance, or the final submission workflow.
