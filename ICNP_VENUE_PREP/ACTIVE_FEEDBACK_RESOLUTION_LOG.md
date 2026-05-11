# Active Feedback Resolution Log

This log records feedback-resolution batches applied to the active ICNP venue draft. It complements the per-section audit notes and follows the repository process in `AGENTS.md`: identify the owning file, make the smallest safe change, preserve validated content, and keep reviewer feedback traceable as LaTeX source comments with `SOLVED` explanations.

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
