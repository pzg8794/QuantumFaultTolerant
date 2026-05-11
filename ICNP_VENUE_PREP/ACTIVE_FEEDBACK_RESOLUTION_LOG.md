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

## Remaining feedback-work policy

Simple feedback items can be batched when all of the following are true:

- the owning file is clear;
- the fix is local and mechanical;
- no result value, figure file, or claim interpretation changes;
- the original feedback can be preserved as a source comment with a short `SOLVED` explanation.

Larger feedback items should remain separate when they affect section structure, figure selection, results interpretation, double-blind compliance, or the final submission workflow.
