# Active Feedback Resolution Log

This log records feedback-resolution batches applied to the active ICNP venue draft. It complements the per-section audit notes and follows the repository process in `AGENTS.md`: identify the owning file, make the smallest safe change, preserve validated content, and keep reviewer feedback traceable as LaTeX source comments with `SOLVED` explanations.

## Batch: May 22 appendix-reference and Figure 5B bar-alternative pass

- **Owning files changed:** `ICNP_2026_venue_draft.tex`, `ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex`, `ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex`, `figures/icnp-exported-assets/build_G8_G9.py`, `ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md`
- **Generated asset:** `figures/icnp/ICNP-CODE-072_fig5b_threat_escalation_bar_alternative.png`
- **Reason for batching:** The May 22 transcript asked for a surgical follow-up: briefly reference the moved framework figure in the Introduction, describe it in the appendix, ensure appendix figures/tables are connected to text, and add a bar version of Figure 5B for advisor feedback without replacing the main-body heatmap yet.

### Resolved feedback / cleanup

1. **Moved framework figure reference**
   - **Issue:** The former Figure 1 evaluation pipeline was moved to the appendix, but the Introduction still needed a brief description that points readers to the appendix figure.
   - **Change:** Reworded the Introduction sentence to describe the five matched inputs and explicitly identify the pipeline diagram as an appendix figure.

2. **Appendix framework description**
   - **Issue:** The appendix version of the framework figure needed its own description rather than relying only on the caption.
   - **Change:** Added a short paragraph before the framework figure explaining how topology, threat regime, policy family, allocator choice, and replay semantics feed the matched evaluation grid.

3. **Appendix figure/table connector coverage**
   - **Issue:** Appendix figures and tables needed to be explicitly referenced or addressed in nearby prose.
   - **Change:** Kept the setup tables/framework references, added the new Figure 5B alternative connector, and preserved explicit references to the diagnostic appendix figures and full-result appendix tables.

4. **Figure 5B bar alternative**
   - **Issue:** The transcript requested a bar-chart version of Figure 5B for advisor feedback before deciding whether to replace the current heatmap.
   - **Change:** Generated a full-width appendix bar alternative from the same validated threat-escalation values and placed it first in the diagnostic appendix while leaving the main-body heatmap unchanged.

### Validation status

- [x] Pulled latest GitHub paper state before editing (`5bdd987`, `Updates from Overleaf`).
- [x] Python figure generator compiles in the `.quantum` environment.
- [x] Full LaTeX compile completed with no unresolved references.
- [x] Generated PDF remains 18 pages total with Conclusion on page 10 and References starting on page 11.
- [x] Appendix pages visually inspected for the new Figure 5B alternative and diagnostic figure connector order.

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
