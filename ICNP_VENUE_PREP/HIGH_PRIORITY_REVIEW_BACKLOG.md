# High-Priority Review Backlog

For the concise advisor-facing status and schedule, see
[`../updates/README.md`](../updates/README.md). This file retains the detailed
implementation and evidence view.

This tracker consolidates high-priority work from three sources:

1. the active ICNP venue draft and included staging files;
2. advisor/reviewer feedback that is available in GitHub or has been surfaced in the working session;
3. transcript-derived planning items that affect the paper workflow.

It intentionally does **not** replace `ICNP_DRAFT_AUDIT_TODO.md`; that file remains the broader venue/compliance checklist. This file is the shorter high-priority working board.

## Current source status

- **Active paper path:** `ICNP_2026_venue_draft.tex`.
- **Editing rule:** update the owning staging file, then verify `ICNP_2026_venue_draft.tex` includes it.
- **Latest GitHub paper state pulled:** `d3b6442` (`Updates from Overleaf`) before the replay-sensitivity image swap.
- **Latest Overleaf branch checked:** `overleaf-2026-05-11-0445`.
- **Overleaf/GitHub state:** latest Overleaf branch is identical to `main` at the time of this tracker.
- **Review-panel limitation:** live Overleaf review-panel comments are not available through GitHub unless they are pushed/exported into the repository or pasted/uploaded into the working session.

## Status legend

- **Open:** ready to work now.
- **Blocked:** cannot proceed until an external input arrives.
- **Final-gate:** intentionally deferred until the end of active commenting/review.
- **Done in active source:** reflected in the current active `.tex` path.
- **Non-paper:** relevant to transcript planning, but not an ICNP manuscript task.

## High-priority paper tasks

| ID | Priority | Task | Status | Evidence / latest-source check | Next action |
|---|---:|---|---|---|---|
| H1 | H | Import new Overleaf review-panel comments into this backlog. | **Blocked** | Latest GitHub Overleaf branch checked (`overleaf-2026-05-11-0445`) is identical to `main`; no review-panel comments are available in GitHub. Transcript says advisor comments are being left through the Overleaf review panel. | User must paste/upload comments, export them, or push source markers from Overleaf. Then convert each into a tracked backlog item. |
| H2 | H | Resolve newly imported review-panel comments. | **Blocked by H1** | Cannot resolve comments that are not visible in GitHub/session context. | Start immediately once H1 is unblocked. |
| H3 | H | Continue paper cleanup so it is ready to share with outside reviewers/collaborators. | **Open / ongoing** | Transcript prioritizes the paper over the thesis/write-up and asks that comments and cleanup be handled before wider review. Current source already reflects many cleanup passes: active ICNP draft, anonymous author block, omitted acknowledgments, polished Results wording, Discussion/Conclusion cleanup, and appendix prose cleanup. | Continue with targeted prose/formatting checks only; do not reopen already-completed Related Work unless new feedback explicitly asks for it. |
| H4 | H | Review and fix figure-internal labels/titles created by earlier figure-generation workflows. | **Done in active source / monitor** | May 21 transcript-derived image pass regenerated the affected main-body and appendix PNGs from source scripts, preserving filenames and avoiding broad page-flow/caption rewrites. Covered Figures 3, 4, 5, 6A, 6B, 7B, 8A, 8B, 10, and 13: values are now directly labeled where captions depend on them, `EXPNeuralUCB`/`OnlineAdaptive` naming is visible, author/testbed labels replace `Paper N` labels, duplicate appendix cross-testbed content was replaced, and the threat-rules plot no longer carries overlapping white labels. | Monitor only. Reopen if a reviewer flags a specific remaining image/caption mismatch. |
| H5 | H | Validate Overleaf warning panel for unresolved refs/cites and missing figures. | **Open** | Source-level cite/ref preflight found no active-path fix needed, but Overleaf warnings are the authority for generated-output issues. | In Overleaf, check warning panel after sync/recompile. Record only actual warnings/regressions in `BUILD_VALIDATION_LOG.md`. |
| H6 | H | Review generated PDF figure/table placement and page flow. | **Open** | Current audit checklist still requires figure/table readability and layout review after compile/PDF inspection. | Inspect PDF visually: figures near claims, captions consistent, no awkward float ordering, no table/figure overflow. |
| H7 | H | Review appendix layout and float order. | **Open** | Appendix tables/diagnostics were reorganized, but compiled appendix page breaks and float order still need PDF review. | Inspect appendix in generated PDF; fix only if order, overflow, or page breaks hurt readability. |
| H8 | H | Keep double-blind state clean in the active review draft. | **Partly done / final-gate remains** | Active draft uses `Anonymous Authors`; acknowledgments are omitted as a source-only note. Public artifact links and PDF metadata still require final-gate validation. | Do not add identifying links/text. Perform final PDF metadata/public-link check before submission. |
| H9 | H | Final rendered-marker/source sweep. | **Final-gate / blocked** | Feedback markers may still be useful while advisors are commenting. User explicitly said source sweep should wait until everyone is done commenting. | Do only after advisors/reviewers confirm commenting is done. Convert or remove rendered markers before final submission. |
| H10 | H | Cross-testbed/new testbed integration in the paper. | **Done in active source, pending reviewer acceptance** | Active draft includes `ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED`; abstract also states cross-testbed evaluation on three external quantum-network simulators. | Do not reopen unless review-panel comments or advisor feedback ask for changes. |
| H11 | H | Maintain GitHub/Overleaf sync discipline. | **Done currently / monitor** | Latest Overleaf branch checked is identical to `main`; AGENTS.md says to compare Overleaf branches before overwriting. | Continue comparing before force-syncing or overwriting Overleaf changes. |
| H12 | H | May 22 transcript: reference the moved framework figure and add a Replay-Configuration Sensitivity bar alternative. | **Done in active source** | Transcript requested a brief Introduction reference to the moved framework figure, a separate appendix description, proper appendix figure/table references, and a bar version of the Replay-Configuration Sensitivity panel for feedback. The bar rendering is now promoted to main-body Figure 6B, the original replay line rendering is retained inside grouped appendix Panel D, and the standalone Context-Capacity Interaction figure is kept as the non-duplicate context-capacity copy. | Monitor only unless advisors request the line rendering back in the main body. |
| H13 | H | Approve surgical space-recovery cuts. | **Open / approval queue ready** | Quick sweep documented approval-ready remove/replace candidates in `ICNP_VENUE_PREP/SPACE_RECOVERY_CANDIDATE_SWEEP.md`; no manuscript prose was changed in this sweep. | Review the candidate list and approve cuts in order: low-risk source/caption cuts first, then medium-risk compression, then page-end compression if still needed. |

## May 22 transcript-derived next items

- **Done in this lane:** brief Introduction reference to the moved framework schematic; separate appendix description for the schematic; appendix figure/table connector references; Replay-Configuration Sensitivity bar chart promoted to the main body; original replay line rendering retained inside grouped synthesis Panel D; standalone replay duplicate removed; standalone Context-Capacity Interaction retained.
- **Next space-recovery item:** review `ICNP_VENUE_PREP/SPACE_RECOVERY_CANDIDATE_SWEEP.md` and approve which exact remove/replace proposals should be implemented.
- **Next validation item:** inspect Overleaf warning panel after the GitHub sync/recompile and record only real warnings or regressions in `BUILD_VALIDATION_LOG.md`.
- **Next visual item:** inspect appendix float order after the image swap; fix only if ordering or readability is harmed.
- **Final-gate items:** page-limit/font checker, rendered-marker sweep, public-link/double-blind metadata check, and source-comment cleanup after commenting is finished.

## Done in active source from recent paper work

These items should not be reopened unless new feedback specifically targets them:

- Active venue draft established as `ICNP_2026_venue_draft.tex`.
- Related Work consolidation completed and should not be redone without new feedback.
- System Model path/reward/threat feedback resolved in source comments with `SOLVED` markers.
- Research Questions prose converted away from answer-by-question scaffolding.
- Results section internal scaffolding (`Focus.`, `evidence slice`, `Validated RQ3 answer`) removed from the active Results staging file.
- Discussion and Conclusion pending-audit markers removed from active rendered prose.
- Blind-review acknowledgments omitted from the active review draft.
- Subfigure caption formatting normalized in the LaTeX preamble.
- Appendix diagnostic prose cleaned to remove process/audit wording from rendered captions.

## Transcript-derived non-paper priorities

These are high priority for the broader plan but are not ICNP manuscript edit tasks:

| ID | Priority | Item | Status | Notes |
|---|---:|---|---|---|
| NP1 | H | Graduation/defense requirements. | **Done per transcript discussion** | User stated the graduation plan had already been reviewed with the relevant advisor/program contacts. |
| NP2 | H | GRE preparation for PhD applications. | **Open / non-paper** | Transcript guidance emphasizes GRE and publications as the main PhD-application priorities and deprioritizes LinkedIn cleanup. |
| NP3 | H | Publications over LinkedIn/profile polishing. | **Ongoing / non-paper** | Continue prioritizing paper submission and publication progress over LinkedIn cleanup. |
| NP4 | L | Dissertation/thesis write-up polishing. | **Deferred** | Transcript guidance says the paper is the priority and the thesis/write-up can be derived from the paper later. |

## Not treated as standalone tasks

The following are tracked metrics or final-gate checks, not separate active tasks by themselves:

- Page count: tracked as a page-budget metric/regression check, not a task.
- Compile: Overleaf already compiles when synced; the useful task is warning/PDF inspection.
- Source sweep: final-gate only, blocked until commenting is complete.
