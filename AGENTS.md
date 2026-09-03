# AGENTS.md

This repository contains the working ICNP 2026 venue draft and supporting audit material for the quantum routing / hybrid contextual bandit paper. This file tells future agents how to update the draft without breaking the workflow.

## Highest-level rule

Do not treat this as a normal single-file LaTeX paper. The active venue draft is assembled from staging files, audit notes, exported figures, and appendix fragments. Update the source fragment that owns the content, then verify that `ICNP_2026_venue_draft.tex` includes it.

## Reviewer-revision strategy

The current revision is reviewer-driven. Every active work item must map directly to documented reviewer feedback or an approved advisor/coauthor decision. Do not invent new research problems, blockers, validation projects, or experiments while resolving a manuscript-language task.

### Low-hanging-fruit rule

The first revision wave is manuscript-only work using material that already exists: reviewer feedback, the current manuscript, validated evidence, and existing documentation. Low-hanging work includes rephrasing, adding or removing text, reorganizing material, clarifying contribution framing, calibrating claims, improving transitions, and reducing narrative clutter.

If resolving a task requires inspecting or modifying implementation code, tracing configurations, running notebooks, analyzing datasets, debugging, or running/designing a new experiment, that task is not low-hanging fruit. Defer that portion to a later complexity tier and move to the next manuscript-only task whose dependencies are satisfied.

### Central-contribution framing rule

For the current paper, the primary contribution is the controlled, threat-aware evaluation framework/methodology and the evidence that this matched evaluation reveals. The evaluated bandit families are objects of comparison and sources of findings; they are not the paper's claimed new contribution.

In the Abstract, Introduction, formal contribution list, and Conclusion, do not let a winning bandit family become the rhetorical center if doing so competes with the controlled framework. Where the same validated result can be stated equivalently, prefer language that foregrounds what the framework exposes: performance gaps, discrepancies, tradeoffs, interactions, instability, failure modes, or boundaries. Preserve the numerical evidence and scientific meaning. Do not distort, omit, or reverse evidence merely to avoid naming a winner.

This is a contribution-positioning rule, not a ban on reporting winners. Results and analysis sections may identify the strongest policy when that is scientifically relevant. The high-level framing should make clear that such rankings are findings produced by the framework, not the reason the paper exists.

### Revision-option rule

Do not manufacture an A/B choice. Every proposed solution must independently satisfy the reviewer feedback and remain scientifically defensible. If only one defensible revision exists, present one. For wording changes, show the complete current paragraph first, then isolate only the competing/problematic sentence(s), then propose solutions for one sentence at a time. Do not mix paragraph context, sentence identification, and replacement language.

### Preservation rule

Preserve the strengths already recognized by Reviewer A: the controlled evaluation design, the separation of policy, allocator, and capacity settings, cross-testbed evidence, and the capacity-paradox finding. This is an operating constraint, not a standalone checklist task or evidence-reconciliation project. Use the existing Validation Hub and validated logs when an empirical claim actually needs evidence checking; do not duplicate that infrastructure.

## Key files and what owns what

### Active venue draft

```text
ICNP_2026_venue_draft.tex
```

This is the runnable ICNP draft. It owns the preamble, title/abstract, Introduction/System Model front matter, and the `\input{...}` order for the venue draft.

Do not dump large rewritten sections directly into this file unless that section is actually inline there. Most later sections are owned by staging files.

### Original/reference manuscript

```text
main.tex
```

Use this as the reference manuscript and visual/style source, not as the primary edit target. Do not rewrite `main.tex` unless the user explicitly asks.

### Section staging files

```text
02--related_works.tex
ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex
ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex
ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED.tex
ICNP_VENUE_PREP/DISCUSSION.tex
ICNP_VENUE_PREP/FUTURE_WORK.tex
ICNP_VENUE_PREP/CONCLUSION.tex
```

These are the files to edit for most manuscript content changes.

### Appendix files

```text
ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex
ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES.tex
```

Use these for detailed evidence, full tables, and diagnostic figures that support but would clutter the main paper.

### Figure assets

```text
figures/icnp/
```

These are the exported notebook-validated images currently used in the ICNP draft.

The notebook source for figure generation/validation is:

```text
https://github.com/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb
```

The master validated logs are in:

```text
https://github.com/pzg8794/GA-Work/tree/main/Validated_Logs
```

Do not replace exported figures with simple placeholder plots unless the user explicitly asks for placeholders.

## Current ICNP draft structure

`ICNP_2026_venue_draft.tex` currently includes, in order:

```tex
\input{02--related_works}
\input{ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex}
\input{ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex}
\input{ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED}
\input{ICNP_VENUE_PREP/DISCUSSION}
\input{ICNP_VENUE_PREP/FUTURE_WORK}
\input{ICNP_VENUE_PREP/CONCLUSION}
...
\appendices
\input{ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES}
\input{ICNP_VENUE_PREP/APPENDIX_DIAGNOSTIC_FIGURES}
```

If you add a new appendix or staging fragment, wire it in here and document why.

## Mandatory workflow for updates

1. Identify the owning file before editing.
2. Read the current content from GitHub before modifying it.
3. Apply the smallest safe replacement to the owning file.
4. Preserve validated content, tables, and figures unless the user explicitly approves removal.
5. Document process decisions in `ICNP_VENUE_PREP/*.md` when a change affects workflow, venue requirements, figure selection, appendix organization, or feedback resolution.
6. Commit with a clear message.
7. Sync the active Overleaf branch only after the main branch contains the intended final state.

## Overleaf/GitHub sync rule

The user often works in Overleaf, creating branches like:

```text
overleaf-YYYY-MM-DD-HHMM
```

If Overleaf reports a sync conflict:

1. Compare `main` with the Overleaf branch.
2. Fetch the changed files from the Overleaf branch.
3. Manually merge useful Overleaf edits into `main`.
4. Preserve our newer validated changes on `main`.
5. Only after merging useful edits, move the Overleaf branch to the merged `main` commit if needed to clear the sync.

Do not force-overwrite an Overleaf branch before checking what changed.

## Feedback-marker policy

Reviewer/advisor feedback markers may appear as macros such as:

```tex
\devroop{...}
\shee{...}
\dan{...}
\piter{...}
```

During working passes, do not delete feedback silently. When resolving a marker:

```tex
% \devroop{original feedback text} -- SOLVED: Brief explanation of what changed.
```

Before final submission, rendered comments must be removed or converted to source comments. The TODO tracker records this requirement.

## Figure policy

The ICNP venue does not require grayscale-only figures. It requires figures and plots to print well on black-and-white printers.

Practical rule:

```text
Use color when helpful, but never rely on color alone.
Use redundant cues: line style, marker shape, fill shade, grouping, direct labels, threshold lines, or clear legends.
```

Current figure guidance is documented in:

```text
ICNP_VENUE_PREP/FIGURE_COLOR_ACCESSIBILITY_NOTE.md
ICNP_VENUE_PREP/FIGURE_SELECTION_AUDIT.md
```

### Main-body figure intent

Main paper figures should each support one central claim. Avoid multiple standalone figures making the same point. Group related figures using subfigures when they support the same observation.

Current grouped logic:

- RQ2 groups scenario penalty + threat escalation.
- RQ3b groups compact capacity paradox + detailed replay-configuration sensitivity.
- RQ3d groups deployment guidance + allocator risk.
- Cross-testbed groups external testbed confirmation + model-family summary.

### Appendix figure intent

Appendix figures should preserve detailed diagnostics and audit evidence, but should not duplicate panels already shown in the main body unless there is a clear reason.

## Table policy

Large detailed tables belong in the appendix unless they are essential to a main-body claim.

Current approach:

- Main body keeps concise claim-supporting tables.
- Appendix preserves full cross-testbed/model-family tables.
- Wide appendix tables should use fixed-width columns, concise descriptors, `\scriptsize`, and tighter `\tabcolsep` rather than overflowing.

Relevant file:

```text
ICNP_VENUE_PREP/APPENDIX_CROSS_TESTBED_TABLES.tex
```

## Related Work status

The Related Work consolidation has already been implemented in:

```text
02--related_works.tex
```

It now follows this structure:

1. Quantum routing and online path selection.
2. Bandit policies for routing decisions.
3. Benchmarking and matched robustness evaluation.

Do not redo this task unless new feedback arrives. If an audit trail is needed, create/update a note rather than rewriting the section again.

## Current tracking notes

Use these notes to understand prior decisions:

```text
ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md
ICNP_VENUE_PREP/OFFICIAL_GUIDELINES.md
ICNP_VENUE_PREP/FIGURE_COLOR_ACCESSIBILITY_NOTE.md
ICNP_VENUE_PREP/FIGURE_SELECTION_AUDIT.md
ICNP_VENUE_PREP/RESULTS_TABLE_RELOCATION_PLAN.md
```

Before starting a new cleanup pass, check the relevant note so you do not repeat already-completed work.

## Venue requirements to preserve

The ICNP draft must follow the venue constraints recorded in:

```text
ICNP_VENUE_PREP/OFFICIAL_GUIDELINES.md
```

Important working constraints:

- IEEE conference format.
- US Letter page size.
- Main body within 10 pages excluding references/appendices.
- Abstract under 250 words.
- Double-blind review version must remove identifying names, affiliations, acknowledgments, public links, and metadata.
- Figures must remain readable in black-and-white printing.
- Core claims must stay in the main paper, not only in appendix.

## Safe commit style

Use direct, descriptive commit messages, for example:

```text
Consolidate main Results figures per feedback
Clean appendix full result tables
Document ICNP figure selection audit
Merge Overleaf figure feedback into Results
```

Do not use vague messages such as `update file`.

## Common mistakes to avoid

- Do not paste placeholder figures when notebook-exported figures exist.
- Do not remove tables/figures just because the surrounding paragraph was reduced.
- Do not render reviewer comments in the PDF after solving them.
- Do not rely on color alone in plots.
- Do not make appendix figures a dumping ground; organize them by claim support.
- Do not redo completed tasks like Related Work consolidation unless there is new feedback.
- Do not overwrite Overleaf edits without comparing branches first.
- Do not claim the draft compiles unless you actually compiled it or verified via Overleaf/GitHub status.
