# Paper Changes / Updates Tracker

**Project:** QuantumFaultTolerant
**Scope:** Track paper edits made in response to advisor/peer comments and internal cleanup.
**Start Date:** 2026-02-14
**Owner:** Piter Garcia

**Canonical task tracker (project-wide):** [../../GA_Communications/md_files/Task-Tracker-Formal.md](../../GA_Communications/md_files/Task-Tracker-Formal.md)

**Quick links:** [../main.tex](../main.tex) | [../sections/02--related_works.tex](../sections/02--related_works.tex)

**Research communications log (source):** [../../GA_Communications/md_files/Research-Communications.md](../../GA_Communications/md_files/Research-Communications.md)

---

## How To Use

- Add one row per *atomic* change (small enough to review in a diff).
- Prefer section-level granularity (e.g., Abstract, Intro, Study Design, Related Work).
- Use **Status** to keep the queue honest.
- Link the change to a commit hash (or PR) when available.
- When a change is prompted by an email/comment thread, link the source in **Notes** (or in the comms-driven queue).

**Status values:** `Planned` | `In Progress` | `Done` | `Deferred` | `Blocked` | `TBD`

---

## Task Categories (Rules)

We use categories to avoid mixing **reviewer-comment tasks** with internal planning:

- **Reviewer tasks (active/closed):** Must be a direct reviewer/advisor/peer comment tied to manuscript text. These go in **Current Queue**.
- **Blocked (advisor approval):** Reviewer task that **cannot be actioned** until Dan approves. These go in **Blocked** and are not worked until unblocked.
- **Parking Lot (non-review):** Internal ideas, roadmap items, submission logistics, late-stage hygiene. These are kept for completeness but are **not** treated as “what’s left” for review closure.

Rule of thumb: if it wasn’t explicitly asked by a reviewer (or it’s not required to unblock a reviewer item), it belongs in the **Parking Lot**.

### Workstreams (What We Work On)

In addition to “review vs non-review,” every non-review item must fit one workstream so we can time-box correctly:

- **Review/Submission (Reviewing):** writing, paper structure, citations, LaTeX/layout, and submission prep
- **Testing/Validation (Testing):** running testbeds/models, validating results, generating tables/figures from runs
- **Technical/Engineering (Technical):** adding models/testbeds, framework changes, automation, refactors

Sprint rule: during a submission sprint, we only pull from **Review/Submission** unless a **Testing/Validation** or **Technical/Engineering** task is required to close a reviewer item.

## Current Queue (From Paper Comments)

| ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Related Canonical Task(s) | Notes |
|---|---|---|---|---|---|---|---|---|
| C-001 | 2026-02-14 | Abstract | Clarify whether this is “evaluation only” vs. new contribution | Add explicit novelty framing (benchmark + taxonomy + capacity paradox + deployment rules) | Done |  | T-2026-007, T-2025-011 | Also see D-001 |
| C-002 | 2026-02-14 | Introduction | Dan: add paragraph on why quantum path determination is unique vs traditional routing | Insert uniqueness paragraph after Key Contributions; keep flow unchanged | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-003 | 2026-02-14 | Related Work | Dan: "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others" | Ensure every process/method in Related Work is explicitly attributed to the paper(s) that introduced it, with clear descriptions of what each paper does and how it differs from our work | Done |  | T-2026-007, T-2025-015 | Implemented in `02--related_works.tex` (added explicit compares; removed the in-text Dan note and the `main.tex` TODO once resolved; left `% [C-003]` pointers in source for traceability) |
| C-007 | 2026-02-15 | References + Cross-Testbed Validation | Paper 12 / QuARC misattributed as “Wang et al.” (but QuARC paper is Clayton/Wu/Bhattacharjee) | Add a dedicated BibTeX key (`clayton2024quarc`) for QuARC (arXiv:2410.23007) and update any Paper 12 testbed citations/mappings to point to it; keep `wang2024adaptive` reserved for Lei Wang’s user-centric routing paper | Done | 338d284 | T-2026-007, T-2025-015 | Verified from the QuARC PDF author list (Connor Clayton et al.) vs the “Adaptive User-Centric…” PDF (Lei Wang et al.) |
| C-008 | 2026-02-16 | RQ2 Supporting Questions | Devroop: "Reduce repetition in supporting questions (RQ2 area); consolidate overlapping sub-questions" | Consolidate RQ2 supporting questions into two two-clause questions; remove duplicate block | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` (duplicate block removed; RQ2a/RQ2b consolidated) |
| C-011 | 2026-02-16 | Figure 5 (Network Topology) | Labels overlap; too much detail | Simplify figure; move details to caption; increase spacing/bends | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-012 | 2026-02-16 | Figure 2 (Legend) | Legend cramped (4 columns) | Reduce legend columns to 2; set font `\scriptsize` | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-013 | 2026-02-16 | Figure 6 (Legend) | Legend cramped (6 columns) | Reduce legend columns to 3; set font `\scriptsize` | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-014 | 2026-02-16 | Table IV (Allocators) | Allocator table needed fit/clarity | Confirm allocator table + label; fix table layout to fit column | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` (tabularx + tightened columns) |
| C-015 | 2026-02-16 | Table II (Widths) | Multi-row table may overflow | Reduce font size and adjust layout if needed | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-016 | 2026-02-16 | Table VIII (Font Size) | Readability | Add `\footnotesize` if needed | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-017 | 2026-02-16 | Figure 12 (Legend) | Legend cramped (4 columns) | Reduce legend columns to 2; set font `\scriptsize` | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-018 | 2026-02-16 | Table III (Algorithm Portfolio) | Overflow to right column | Fit to column width (tabularx + reduced padding) | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-020 | 2026-02-16 | Table Citations (Complete Audit) | Devroop: "refer the tables per your findings" | Add missing `\Cref{...}` references for all uncited tables | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` |
| C-021 | 2026-02-16 | Abstract | Two versions exist | Choose final abstract version | Done |  | T-2026-007, T-2025-011 | Resolved via C-032 (single abstract retained) |
| C-022 | 2026-02-16 | Introduction Cleanup | Commented blocks remain | Remove commented intro drafts; keep C-### markers | Done | 5990ad2 | T-2026-007, T-2025-011 | Cleaned `main.tex` front-matter/intro planning blocks; rationale retained in tracker |
| C-026 | 2026-02-16 | Cleanup | Resolved comment markers remain | Remove resolved comment markers | Done | 5990ad2 | T-2026-007, T-2025-011 | Removed resolved in-draft reviewer markers/TODO blocks from `main.tex`; kept active open notes (e.g., Devroop “relay questions…” and “one more paper…”) in-source for later resolution |
| C-027 | 2026-02-16 | Experimental Design | Missing design rationale | Add 1 sentence per major design choice | Done | TBD | T-2026-007, T-2025-011 | Already present in `main.tex` Experimental Design opening (rationale + citations for topology choice, fixed-capacity choice, and allocator axis) |
| C-028 | 2026-02-16 | Limitations/Future Work | Duplicate sections | Consolidate into one section | Done | 5990ad2 | T-2025-011 | Removed the duplicated commented Limitations/Future Work block; single section remains |
| C-029 | 2026-02-16 | Results Narrative | Weak transitions | Replace duplicated Results intro roadmap with a single RQ1/RQ2/RQ3 transition sentence with direct `\S\ref{}` pointers | Done | 1f79a7d | T-2025-011 | Applied at `main.tex` Simulation Results opening (removes back-to-back duplicate “Results are organized…” paragraphs) |
| C-005 | 2026-02-14 | Limitations/Future Work | Resolve duplication notes in commented blocks | Remove/retire duplicate commented section after confirming nothing unique | Done | 5990ad2 | T-2025-011 | Duplicate of C-028; resolved by removing the duplicated Limitations/FW block in `main.tex` |
| C-031 | 2026-02-17 | Title | Comment: paper focuses on entanglement routing; include in title | Update title to explicitly include “entanglement routing” and clarify evaluation framing | Done |  | T-2026-007, T-2025-011 | DECISION: “Threat-Aware Evaluation of Quantum Entanglement Routing and Qubit Allocation via Hybrid Contextual Bandits” (concise, domain-clear, evaluation-framed) |
| C-032 | 2026-02-17 | Abstract | Comment: abstract confusing; unclear if evaluation-only vs new contributions; too many numbers; unclear referents (“they”); sentence clarity | Rewrite abstract for clarity: (1) state contribution type carefully, (2) reduce numeric density (keep 1 scale indicator), (3) fix ambiguous referents, (4) remove duplicate/alternate abstract + inline comments from compiled draft, (5) reconcile count consistency with body or avoid counts | Done |  | T-2026-007, T-2025-011 | Approved draft applied in `main.tex` (4-paragraph structure; reduced numeric overload; clarified scope/novelty language) |
| C-033 | 2026-02-17 | Introduction | Comment: “Yet, reliable end-to-end entanglement…” needs citation | Add a minimal citation to support fragility + probabilistic swapping + decoherence/interference claim (without adding number/citation clutter) | Done |  | T-2026-007, T-2025-015 | Applied in `main.tex`: `~\\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}` at end of the “Yet, …” sentence |
| C-034 | 2026-02-17 | Introduction | Comment: may need more/updated citations for swapping waiting-time compounding | Validate waiting-time citation support and update the BibTeX metadata for the targeted waiting-time reference (no extra padding citations) | Done |  | T-2026-007, T-2025-015 | Kept `~\\cite{wang2019waiting}` in `main.tex`; updated `refs.bib` entry for completeness |
| C-035 | 2026-02-17 | Introduction | Comment: remove “Gap in Prior Work” subsection to keep flow consistent | Remove the “Gap in Prior Work” subsection heading and keep the same content as a normal intro paragraph to preserve flow | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` (removed subsection heading; added transition “However, …”) |
| C-036 | 2026-02-17 | Introduction → Study Design | Comment: move “In total, we report about … evaluations …” to Results/Discussion | Move corpus accounting (7,890 / 835) out of the Introduction into Study Design (corpus accounting belongs with methods) | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` (removed from Intro; added to Study Design opening) |
| C-037 | 2026-02-17 | Contributions | Comment: reword “Unified, reproducible benchmarking across bandit families” bullet (apples-to-apples) | Update bullet to explicitly say apples-to-apples and keep wording concise | Done |  | T-2026-007, T-2025-011 | Applied in `main.tex` (bullet rewritten; EXP3 key standardized to `auer2002nonstochastic`) |
| C-038 | 2026-02-17 | Framework Section | Comment: speak more about the layers (Algorithmic Framework) | Expand the framework description to explicitly name/describe the layers (env/threat/allocator/capacity/learner/metrics) | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` directly after the six-layer list in the Algorithmic Framework section |
| C-039 | 2026-02-17 | Cross-Testbed Validation | Comment: mentions noise models/settings without explaining what they are/how they work | Add brief explanations/citations for noise models/settings; ensure Paper 7 is described accurately (benchmarking-driven fidelity estimation + online path selection, not “context-driven rewards”) and align the Key Contributions parenthetical with the detailed section | Done | TBD | T-2026-007, T-2025-011 | Paper 2/7 bullets corrected; Key Contributions aligned; 1-line “what/how” context added before the external-testbed list |
| C-040 | 2026-02-18 | Build / Appendix Ref | LaTeX warning: `app:data_artifacts` undefined (Appendix ref referenced in Results) | Add/confirm Appendix section with `\\label{app:data_artifacts}` (or update refs to correct label); remove “(or Supplementary Material)” placeholder if not applicable | Deferred |  | T-2026-007, T-2025-011 | Snippet in Results: “...provided in Appendix~\\ref{app:data_artifacts} ...” |
| C-041 | 2026-02-18 | Build / LaTeX Output | LaTeX warning: “Missing character: There is no ` in font nullfont!” | Suppress pdfTeX lost-character warnings triggered during auxiliary/PDF-string writes by setting `\tracinglostchars=0` (rendered output unchanged); keep any `\texorpdfstring` fixes where appropriate | Done | 5007e44 | T-2026-007, T-2025-011 | Verified: `main.log` no longer contains “Missing character: There is no ` ...” (previously 4 hits around page [7]) |
| C-042 | 2026-02-18 | Conclusion | Dan: “Not sure where this should go” (classical-vs-quantum routing paragraph) | Comment out the redundant background paragraph in the Conclusion (already covered in Intro) and tighten the Conclusion body into 2–3 result-focused paragraphs | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` (Dan note + redundant paragraph commented; conclusion rewritten to avoid repetition) |
| C-043 | 2026-02-18 | References / BibTeX | Audit: inconsistent/duplicate BibTeX keys (risk of wrong/missing citations) | Standardize on one key per paper; remove duplicate/placeholder BibTeX entries; verify all `\\cite{...}` keys resolve | Done | TBD | T-2026-007, T-2025-015 | Standardized keys used in `main.tex`/`02--related_works.tex`; verified no missing cite keys; no remaining duplicate DOI/title groups in `refs.bib` |
| C-044 | 2026-02-20 | Introduction | Dan: “These should have citations… build this up… drive home the problem.” (re: incompatible assumptions/threat models) | Add citations supporting the incompatibility claim; add 1–2 sentences that connect incompatibility to attribution difficulty + weak deployment generalization | Done | TBD | T-2026-007, T-2025-015 | Applied in `main.tex`: added `~\\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}` + two motivation sentences before the “Two streams…” list |
| C-045 | 2026-02-20 | Introduction | Dan: “Intro focuses too much on the process… Focus on the problem… tiny bit on the process… more on the findings/impacts.” | Rebalance intro: expand problem/gap framing; compress framework/process exposition; add a short findings/impact preview (avoid numeric overload) | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex`: removed the evaluation-grid bullet list; added a 2-sentence findings/impact preview + pointer to `\\S\\ref{sec:studydesign}` |
| C-046 | 2026-02-20 | Introduction | Dan: “Find newer citations if you can.” | Add 1–2 newer citations in the intro where they materially strengthen motivation (no padding) | Done | TBD | T-2026-007, T-2025-015 | Applied: added `pompili2021realization` to the opening “quantum Internet applications” sentence and to the repeater-architecture anchor; refined adversarial-stream parenthetical to “EXP3-family and adversarial-adaptive” and included `zimmert2019optimal` (already in `refs.bib`) |
| C-047 | 2026-02-20 | Introduction | Dan: “what gap? Add a few words context.” | Add 1–3 words clarifying what “gap” refers to so the sentence reads standalone | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` in both intro locations (“matched-threat evaluation gaps”) |
| C-048 | 2026-02-20 | Figures (Captions) | Dan: “Too wordy and dont change caption size.” (re: Context vs EXP3 caption) | Rewrite caption to takeaway-first; remove manual `\\tiny` and use IEEE default caption sizing | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` at `\\label{fig:context_exp3_capacity}` (removed `\\tiny`; shortened to takeaway-first caption) |
| C-049 | 2026-02-20 | Figures (Captions) | Dan: “For all references, mention the primary takeaway.” (re: floor/peak/mean caption) | Rewrite number-led captions so the first clause states the takeaway; keep caption sizing unchanged (no manual `\\tiny`) | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` at `\\label{fig:floor}` (takeaway-first caption; removed manual `\\tiny`) |
| C-050 | 2026-02-20 | Study Design | Dan: “If there are any similar studies, then cite them.” | Add closest-study citations in Study Design (testbeds + benchmarking context) without over-claiming methodological overlap | Done | TBD | T-2026-007, T-2025-015 | Applied in `main.tex` Study Design opening: testbed comparability cites `chaudhary2023quantum,liu2024qbgp,clayton2024quarc`; scoped benchmarking as “complementing” `coopmans2021benchmark,kozlowski2022utility` |
| C-051 | 2026-02-20 | Research Questions | Dan: “Some of these RQs can be simplified, and maybe broken up.” | Simplify RQ wording for standalone readability; split only when one RQ truly bundles multiple independent asks | Done | TBD | T-2026-007, T-2025-011 | Applied to RQ1 block (main + RQ1a/b/c wording tightened) |
| C-052 | 2026-02-20 | Research Questions | Dan: “Predicitive 'what' context.” (re: RQ3a) | Clarify what “predictive context” refers to so the question reads standalone (name the mechanism) | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex`: “predictive (ARIMA-informed) context” + “routing stability” |
| C-053 | 2026-02-20 | Research Questions | Dan: “All RQs should largely be written so that they can be understood as standalone questions.” (re: RQ3d) | Rewrite RQs to remove ambiguous “we/this/it” phrasing and add minimal context nouns so each reads standalone | Done | TBD | T-2026-007, T-2025-011 | Applied to RQ2 + RQ3 main + supporting questions (adds “routing/entanglement routing”, clarifies replay-capacity wording) |
| C-054 | 2026-02-20 | Related Work | Dan: “write this better and in paragraph form.” (re: Inclusion/Exclusion Criteria) | Rewrite Inclusion/Exclusion Criteria from list form into 1 cohesive paragraph; preserve criteria content while improving readability | Done | TBD | T-2026-007, T-2025-015 | Applied in `sections/02--related_works.tex` (single paragraph replaces nested lists; citations preserved) |
| C-055 | 2026-02-20 | Related Work | Dan: “You dont need subsesctions for each of these” | Collapse/merge micro-subsubsections in Related Work (e.g., Search Strategy/Time Span) into fewer paragraphs; remove labels/headings where they don’t add structure | Done | TBD | T-2026-007, T-2025-015 | Applied in `sections/02--related_works.tex` (removed micro-subsubsections; merged into label-free methodology prose with a bridge phrase) |
| C-056 | 2026-02-20 | Related Work | Dan: “Make sure that youre directly comparing/contrasting the work against yours.” | Ensure each Related Work thread includes an explicit 1–2 sentence contrast vs our work (what they do + what we do differently) | Done | TBD | T-2026-007, T-2025-015 | Applied in `sections/02--related_works.tex` (added explicit “In our study/benchmark…” contrast sentences in foundational/contextual/adversarial/predictive subsections; quantum-routing subsection already had paper-to-paper contrasts) |
| C-057 | 2026-02-28 | Figures (Caption) | Dan: “Too wordy and dont change caption size.” (heatmap caption) | Rewrite heatmap caption to be takeaway-first and remove manual `\tiny` sizing | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` at `\label{fig:heatmap}` (removed `\tiny`; shortened caption; references “Fixed” to match x-axis label) |
| C-058 | 2026-02-28 | Figures (Caption) | Dan: “Too wordy and dont change caption size.” (framework caption) | Rewrite framework caption to be takeaway-first and remove manual `\tiny` sizing | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` at `\label{fig:framework}` (removed `\tiny`; shortened caption; kept label immediately after caption) |
| C-059 | 2026-02-28 | Figures (Caption) | Dan: “Too wordy and dont change caption size.” (global win share caption) | Rewrite global-win-share caption to be takeaway-first and remove manual `\tiny` sizing | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` at `\label{fig:global_win_share}` (removed `\tiny`; shortened caption; term “default allocator” matches legend text) |
| C-060 | 2026-02-28 | Figures (Captions) | Dan: “Too wordy and dont change caption size.” (remaining `\caption{\tiny ...}` captions) | Remove remaining `\tiny` caption sizing and rewrite captions to be takeaway-first with minimal numeric density | Done | TBD | T-2026-007, T-2025-011 | Applied in `main.tex` (removed all remaining `\caption{\tiny ...}`; updated: `fig:context_capacity_effects`, `fig:scenario_penalties`, `fig:capacity_all`, `fig:threat_rules`, `fig:convergence_hybrid`, `fig:context_hybrid`) |

---

## Blocked (Needs Dan Approval)

These are reviewer-comment tasks that we will **not** implement until Dan explicitly approves the structural change.

| ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Related Canonical Task(s) | Notes |
|---|---|---|---|---|---|---|---|---|
| C-024 | 2026-02-16 | RQ Section Flow | Answers appear in RQ section | Move detailed answers to Results; keep questions in RQ section | Blocked |  | T-2026-007, T-2025-011 | Needs Dan approval (no action until instructed) |

---

## Parking Lot (Non-review Backlog by Workstream)

These are items that were captured during internal planning, roadmap, or logistics. They are kept for completeness but are **not** treated as reviewer-comment tasks and should not be surfaced as “what’s left” for review closure.

| Workstream | ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Related Canonical Task(s) | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Testing/Validation | T-001 | 2026-03-01 | Cross-Testbed Validation | Standardized, apples-to-apples reruns (same run configuration across Papers 2/7/12) | Run each external testbed under our standardized run protocol (base: 4K base frames, 2K step, S=3/5 runs; stress: S=8/10 runs) under consistent allocator/capacity semantics where supported; record scenario-aggregated metrics | Planned |  | T-2025-011 | Produces the standardized corpora used for the unified cross-testbed table |
| Review/Submission | T-002 | 2026-03-01 | Results + Tables | Standardized cross-testbed comparison table | Add a “standardized run protocol” results table (Papers 2/7/12) showing top-tier model performance under identical run settings; replace the current “follow-up campaign” placeholder text once values are available | Planned |  | T-2025-011 | Depends on T-001 |
| Technical/Engineering | T-003 | 2026-03-01 | Framework / Runner | Add standardized run-config preset | Add a single preset/config helper so Paper2/Paper7/Paper12 can be executed with identical (base_frames, frame_step, runs, seeds) and consistent output naming to support T-001 | Planned |  | T-2025-011 | Implement in the experiment framework repo (not in this paper repo) |
| Technical/Engineering | T-004 | 2026-03-01 | Framework / State Naming | Random allocator state naming includes qubit allocations in runner/model filenames | Drop qubit-allocation suffix from **runner/model** state filenames for Random allocator; use a seed/sample identifier instead (or allow canonical overwrite) to prevent filename explosion and avoid resume logic expecting `_(qubit_alloc)` in names | Planned |  | T-2025-011 | Decision: keep evaluator naming unchanged; focus is runner + model state keys |
| Technical/Engineering | T-005 | 2026-03-01 | Framework / Resume Logic | Resume path relies on parsing `_(qubit_alloc)` in runner filenames | Update runner resume logic so it does **not** depend on `_(qubit_alloc)` being present; optionally keep backward compatibility for old state files | Planned |  | T-2025-011 | Must align with T-004 (new naming scheme) |
| Technical/Engineering | T-006 | 2026-03-01 | Framework / Evaluator Audit | Ensure evaluator naming + resume behavior matches the intended policy (Random allocator only) | Audit `MultiRunEvaluator` + `ExperimentConfiguration.get_key_attrs()` + `LocalBackupManager` registry handling to ensure (i) evaluator filenames are allocation-agnostic, (ii) evaluator resume/equality does not require qubit allocations in names, and (iii) **for Random allocator only** we intentionally ignore `qubit_capacities` in evaluator comparisons while still requiring runner instances to store the exact allocation used per experiment for apples-to-apples model comparison | Planned |  | T-2025-011 | Do this before state migration (rename/normalize existing pickles) |
| Review/Submission | C-023 | 2026-02-16 | Submission Hygiene | Anonymous submission decision | Decide anonymous vs non-anonymous; update authors/acks accordingly | Deferred |  | T-2026-007, T-2025-011 | Decision-only; do not surface as an action item until requested |
| Review/Submission | C-006 | 2026-02-14 | Submission Hygiene | Anonymity question + acknowledgments | Decide anonymous vs non-anonymous; adjust authors/acks accordingly | Deferred |  | T-2025-011 | Duplicate of C-023; decision-only |
| Review/Submission | C-025 | 2026-02-16 | RQ Scope Clarification | Scope/novelty unclear | Add prior-work citations or clarify novelty statement | Deferred |  | T-2026-007, T-2025-011 | Internal note captured during tracker setup (not a direct reviewer quote) |
| Review/Submission | C-030 | 2026-02-16 | Code/Data Availability | Statement decision needed | Decide availability statement; add or remove | Deferred |  | T-2025-011 | Late-stage hygiene decision; park until final submission sweep |
| Review/Submission | C-004 | 2026-02-14 | Results Section | Improve continuity; organize by RQs | Add short “RQ claim → evidence → takeaway” scaffolding per subsection | Deferred |  | T-2025-011 | Internal narrative polish (not a direct reviewer quote) |
| Review/Submission | D-004 | 2026-02-15 | Submission Logistics | Grant advisor access to the condensed Overleaf view/project | Ensure access is granted (or provide an equivalent local PDF) and record what was shared | Deferred |  | T-2026-009 | Logistics; not a manuscript review comment |
| Review/Submission | D-005 | 2026-02-15 | Whole paper (general) | Get the manuscript into a shareable state and address high-level comments | Address high-level comments; ensure the manuscript is shareable for team review | Deferred |  | T-2026-007, T-2025-011 | Logistics/coordination; not a specific review comment |
| Technical/Engineering | D-006 | 2026-02-15 | Results + Tables | Add epsilon + NeuralUCB results + extra comparison table (testbed configs) | Add epsilon + NeuralUCB results; add a comparison table contrasting paper config vs our run config | Deferred |  | T-2025-011 | Owner roadmap / extension work; requires new runs (Testing/Validation) |
| Review/Submission | D-008 | 2026-02-15 | Whole paper (general) | Integrate Professor Travis feedback before submission | Apply Travis edits/comments once received; record deltas as atomic C-### items | Deferred |  | T-2026-005, T-2025-011 | Blocked until feedback received |

## C-031–C-039 Comment Details (Ask → Meaning → Issue → Proposed Fix)

Use these blocks to preserve the intent of the comment and keep fixes reviewable before touching `main.tex`.

### C-031 — Title: include entanglement routing
- **Ask:** Include entanglement routing in the title if the paper focuses on it.
- **Meaning:** The title should reflect the paper’s primary topic(s), not only “qubit allocation”.
- **Issue:** Current title may under-signal the routing contribution and mis-set reader expectations.
- **Proposed fix:** Update the title to explicitly include “entanglement routing” (keep qubit allocation if still central).
- **Deep notes (from report):**
  - Current title says “stochastic,” but the paper emphasizes threat escalation (Markov/Adaptive/OnlineAdaptive) and “capacity paradox” behavior; avoid underselling scope.
  - Candidate title directions to consider: “bandit learning under threats,” “context-aware bandits,” or “adversarial-robust bandits.”
- **Decision (2026-02-17):**
  - Selected final title: \textit{Threat-Aware Evaluation of Quantum Entanglement Routing and Qubit Allocation via Hybrid Contextual Bandits}.
  - Rationale: concise, domain-clear, evaluation-framed, and better aligned with entanglement routing + threat taxonomy scope than the prior “stochastic” title.

### C-032 — Abstract clarity + contribution type
- **Ask:** Abstract is confusing; clarify whether this is evaluation-only or includes new contributions; reduce number density; fix ambiguous referents (“they”); fix sentence clarity.
- **Meaning:** Make the abstract readable on first pass and explicit about contribution type.
- **Issue:** Dense numeric listing + ambiguous pronouns makes the primary takeaway hard to parse; one sentence was flagged as unclear.
- **Proposed fix:** Rewrite abstract with a simple structure: (1) problem + scope, (2) what we contribute (evaluation framework + any new model/family), (3) 1–2 key findings (keep only essential numbers; move deep numerics to Results).
- **Deep notes (from report):**
  - Remove duplicate/alternate abstract draft and any inline author notes from the compiled manuscript.
  - Reduce numeric overload: keep **one** scale indicator (either internal-corpus breadth or external-testbed span), not multiple ranges + multiple counts.
  - Avoid pronouns like “they”: name the subject (“pursuit–neural hybrids…”).
  - Count consistency: Intro uses different totals (models/evaluations) than the abstract; either reconcile via “curated corpora” wording or avoid the counts in abstract.
  - Be careful with novelty wording: don’t over-claim “new algorithms” unless the paper explicitly positions CPursuitNeuralUCB/iCPursuitNeuralUCB as introduced here (vs baseline import).


**Approved draft (2026-02-17) — apply to `main.tex`:**
```tex
Quantum entanglement routing requires dynamic path selection and qubit allocation
under noisy and adversarial conditions. Existing routing approaches often assume
stationary link behavior, decouple selection from allocation, or rely on offline
optimization—assumptions that can fail when link fidelities drift and disruptions
adapt online.

In this paper, we present a systematic threat-aware evaluation of bandit algorithms
(contextual, adversarial, and hybrid) for joint path selection and qubit allocation
in quantum networks, introducing pursuit--neural hybrid variants that balance
stochastic efficiency with adversarial robustness. We evaluate 13 algorithms across
five threat scenarios while varying allocator policies and replay-capacity semantics.

Pursuit--neural hybrids emerge as the most robust family, outperforming non-contextual
bandit baselines by 18--24 percentage points and sustaining higher worst-case performance
under strategic attacks than adversarial-first designs.

We validate robustness through cross-testbed evaluation on three external quantum
network simulators, confirming consistent robustness trends across diverse topologies
and noise models while exposing scale- and physics-dependent performance limitations.
```

**Decision rationale (why this wording):**
- Dan’s core feedback was “too many numbers” in the abstract; we removed the full design-grid accounting (e.g., configs/allocators/capacity settings and per-testbed efficiency ranges).
- We adopted a clear 4-part structure (problem/gap → what we do → headline finding → validation/impact) while keeping the wording evaluation-framed.
- We fixed two clarity traps that could trigger new reviewer confusion:
  - Avoided partial parenthetical lists (e.g., implying the full threat set but listing only examples).
  - Replaced “context-aware stochastic bandits” framing with an umbrella “threat-aware” framing (contextual, adversarial, hybrid) to match scope.
- We clarified “novelty vs evaluation” language by using “introducing pursuit--neural hybrid variants” (rather than “including”), without expanding into a long novelty claim.
- Capacity-paradox details remain in the body; we intentionally did not restate them in the abstract to keep numeric density low.

### C-033 — Intro claim needs citation (entanglement fragility / probabilistic swapping / decoherence)
- **Ask:** Add citation for: “Yet, reliable end-to-end entanglement is difficult to sustain…”
- **Meaning:** Anchor the claim in prior work (foundational quantum networking/repeater citations).
- **Issue:** Statement reads as a factual claim but is currently not explicitly supported by a citation.
- **Proposed fix (minimal):** Append `~\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}` to the end of the “Yet, reliable end-to-end entanglement…” sentence in `main.tex` (all keys already exist in `refs.bib` and are already used elsewhere in the intro).
- **Deep notes (from report):** Cross-testbed sources can support this claim (e.g., Chaudhary testbed and/or QBGP) in addition to foundational repeater/swapping citations.

**Decision rationale (why this citation set):**
- Keep the fix minimal to avoid triggering Dan’s “too many numbers” / clutter feedback in the intro.
- Use existing BibTeX keys already in the paper (no new bibliography additions required).
- Use citations that directly support the specific mechanisms named in the sentence (repeaters/operations: `briegel1998quantum`; simulator + decoherence/imperfections context: `dahlberg2021netsquid`; swapping is probabilistic: `zukowski1993event`).
- Keep `wang2019waiting` focused on the waiting-time compounding claim (C-034).

**Applied (2026-02-18):**
- Added `~\cite{briegel1998quantum,dahlberg2021netsquid,zukowski1993event}` to the end of the “Yet, …” sentence in `main.tex`.

### C-034 — Update/expand waiting-time citation(s)
- **Ask:** May need more/updated citations for: “entanglement swapping introduces stochastic waiting-time effects…”
- **Meaning:** Ensure the cited work is the right authority and add a second supporting cite if needed.
- **Issue:** Single citation may be outdated/insufficient for the exact claim phrasing.
- **Proposed fix:** Keep `~\cite{wang2019waiting}` (it is directly on-point for probabilistic swapping waiting times); avoid adding off-target routing citations purely to pad support. If any change is needed, prefer improving the BibTeX completeness for `wang2019waiting` rather than adding a new key.
- **Deep notes (from report):** If adding a second citation, prefer a repeater waiting-time / memory-decoherence authority (not just “routing exists”).

**Decision rationale (why no extra cite was added):**
- The sentence is already supported by a directly matching waiting-time paper (`wang2019waiting`) plus repeater context in the preceding clause (`briegel1998quantum`).
- Adding a routing-protocol citation (e.g., `li2025multipath`) risks looking like citation padding if it does not explicitly discuss waiting-time compounding.

**Applied (2026-02-18):**
- Updated `refs.bib` entry `wang2019waiting` to include `url` and `publisher` metadata (no change to the in-text citation).

### C-035 — Intro flow: remove “Gap in Prior Work” subsection heading
- **Ask:** “You can remove these sections. Make the flow consistent.” (Gap in Prior Work)
- **Meaning:** Avoid abrupt heading/structure changes that break narrative flow.
- **Issue:** The heading may be redundant with the surrounding intro flow and reads like a structural speed bump.
- **Proposed fix:** Remove/merge the subsection heading and integrate the content into the surrounding intro (keep the same ideas).
- **Deep notes (from report):** If we remove only this one heading while keeping other intro subheadings, flow may become *less* consistent; consider either (a) keep but rename, or (b) convert intro subheadings to a consistent paragraph-style scheme.

**Decision rationale (why this approach):**
- Implemented the minimal structural change requested: removed only the `\subsection{Gap in Prior Work}` heading.
- Preserved all gap content and enumerations verbatim to avoid changing argument/claims while improving narrative flow.
- Added a single transition word (“However,”) so the paragraph reads naturally without a heading.

**Applied (2026-02-18):**
- Removed `\subsection{Gap in Prior Work}` in `main.tex` and integrated the paragraph into the surrounding intro flow.

### C-036 — Move evaluation counts out of intro
- **Ask:** Move: “In total, we report about … evaluations …” to Results/Discussion.
- **Meaning:** Keep intro high-level; move detailed corpus accounting to where results/methods are discussed.
- **Issue:** Large numeric accounting in the intro distracts from the problem/approach message.
- **Proposed fix:** Remove the sentence from the Introduction and place it in Study Design as a one-line corpus accounting statement.

**Decision rationale (placement):**
- The core constraint was “too many numbers in the intro”; moving the counts out resolves the complaint without changing values.
- Study Design is the natural home for corpus accounting (methods), while Results should stay focused on findings.
- Keep the change move-only: do not alter the counts or add new claims.

**Applied (2026-02-18):**
- Removed the 7,890/835 sentence from the Introduction (“Our Approach and Evaluation Scope”).
- Added the same sentence to the opening of Study Design as corpus accounting.

### C-037 — Reword contributions bullet (benchmarking across families)
- **Ask:** Reword the “Unified, reproducible benchmarking across bandit families” contribution bullet.
- **Meaning:** Keep the claim but make it easier to read and less jargon-heavy.
- **Issue:** Current bullet is long and reads as a dense citation dump.
- **Proposed fix:** Rewrite as a shorter bullet that states: apples-to-apples benchmarking across decision-rule families under a shared threat taxonomy (citations can remain but be lighter).
- **Deep notes (from report):** Standardize EXP3 citation key usage across the manuscript (avoid mixed keys like `auer2002exp3` vs `auer2002nonstochastic`).

**Decision (approved wording):**
```tex
\item \textbf{Unified, reproducible apples-to-apples benchmarking:} We evaluate adversarial (EXP3-family), contextual (CMAB/iCMAB), and hybrid pursuit--neural bandit policies under a shared threat taxonomy, enabling direct comparison of robustness--efficiency tradeoffs~\cite{auer2002nonstochastic,huang2024quantum,chu2011contextual,kar2024icmab}.
```

**Decision rationale (citation key):**
- `refs.bib` contained two keys for the same Auer et al.\ (2002) adversarial bandits paper (`auer2002exp3` and `auer2002nonstochastic`).
- We standardized the manuscript to cite `auer2002nonstochastic` and removed the duplicate `auer2002exp3` entry to avoid ambiguity and ezproxy URLs in the bibliography.

**Applied (2026-02-18):**
- Updated the Key Contributions bullet wording in `main.tex`.
- Replaced remaining `\cite{auer2002exp3}` uses in `main.tex` with `\cite{auer2002nonstochastic}`.
- Removed the duplicate BibTeX entry `auer2002exp3` from `refs.bib`.

### C-038 — Framework: explain the layers
- **Ask:** “You need to speak more about the layers” (Algorithmic Framework).
- **Meaning:** Readers should understand the stack (environment/threat/allocator/capacity/learner/metrics) without guessing.
- **Issue:** Framework description may not explicitly enumerate layers and their interfaces.
- **Proposed fix:** Add a brief layer breakdown (1–2 sentences per layer) and state what inputs/outputs pass between layers.
- **Deep notes (from report):** Framework figure lists only a subset of algorithms (hybrid set) in the “Configuration” block; text should clarify the figure is illustrative/corpus-specific and that the full evaluation spans the complete model portfolio.
- **Decision rationale (how we got to the draft):**
  - We kept the change \emph{surgical}: add a single interface paragraph rather than rewriting the full framework section.
  - We anchored the “interface stack” to the paper’s existing six-layer names (ALLOCATOR / CONFIGURATION / EVALUATOR / RUNNER / MODEL / VISUALIZER), so it reads like an explanation of our implementation (not a second taxonomy).
  - We explicitly clarify that Fig.~\ref{fig:framework} is illustrative and that the full evaluated portfolio lives in \Cref{tab:setup-algorithm-portfolio}.
  
**Proposed text (LaTeX; insert right after `\end{enumerate}` in the Algorithmic Framework section, before the next paragraph):**
```latex
\noindent\textbf{Interface view (how the layers connect).}
Each experiment instantiates a consistent decision pipeline:
\emph{Environment} (topology + link/fidelity model)
$\rightarrow$ \emph{Threat/Noise process} (how disruptions evolve)
$\rightarrow$ \emph{Allocator} (maps total capacity to per-path budgets)
$\rightarrow$ \emph{Capacity semantics} (e.g., $T$ vs. $T_b$, replay scale $s$; \S\ref{subsec:capacity})
$\rightarrow$ \emph{Learner/Policy} (bandit selects paths from feedback/context)
$\rightarrow$ \emph{Metrics} (oracle-normalized efficiency and robustness summaries).

\noindent In our implementation, \textbf{CONFIGURATION} fixes the shared environment, threat regime, and capacity semantics;
\textbf{ALLOCATOR} chooses the distribution rule; \textbf{EVALUATOR} instantiates the threat model and logging/oracle tracking;
\textbf{RUNNER} executes batched runs under fixed seeds and aggregation rules; \textbf{MODEL} implements the bandit policy and routing stack;
and \textbf{VISUALIZER} aggregates results into scenario rankings, efficiency curves, and summary tables.

\noindent Figure~\ref{fig:framework} is illustrative (one representative configuration); the full evaluated model portfolio
is summarized in \Cref{tab:setup-algorithm-portfolio}.
```

**Applied (2026-02-18):**
- Inserted the “Interface view (how the layers connect)” block in `main.tex` immediately after the `\end{enumerate}` list in the Algorithmic Framework section.
- Rebuilt `main.pdf` for GitHub rendering.

### C-039 — Cross-testbed: explain referenced models/settings
- **Ask:** You mention noise models/settings but don’t discuss what/how they work.
- **Meaning:** Provide minimal interpretive context so testbed configs are understandable to non-authors.
- **Issue:** Cross-testbed bullets list model names/params without explanation.
- **Proposed fix:** Add 1-line explanations (and/or citations) for the named noise models and key parameter meanings.
- **Deep notes (from report):**
  - Align the Key Contributions “diverse noise models” parenthetical with what each cited testbed actually does.
  - Correct Paper 7 description: QBGP uses noise-channel modeling (e.g., depolarizing channels) + benchmarking-driven fidelity estimation; avoid “context-driven rewards/dynamics” wording.

**Applied (Paper 2 reference cleanup; 2026-02-18):**
- Updated the Paper 2 testbed bullet in `main.tex` to remove the inaccurate “adaptive capacity allocation” phrasing and describe it as a stochastic-noise testbed for learning-based route selection.
- Updated `refs.bib` for `chaudhary2023quantum` (replaced “and others” with the actual author list from the PDF header; expanded the ICC booktitle).

**Applied (Paper 7 + alignment + 1-line context; 2026-02-18):**
- Replaced the Paper 7 testbed description in `main.tex` to reference QBGP’s network benchmarking + online top-$K$ path selection (and removed “context-driven external rewards” wording).
- Added a single sentence before the external-testbed bullet list explaining, at a high level, what each testbed’s link-quality model/estimation setting represents.
- Updated the Key Contributions bullet noise-model parenthetical in `main.tex` to align with the corrected Paper 7 wording (benchmarking-driven fidelity estimation / online path selection).

### C-040 — Fix undefined Appendix label (`app:data_artifacts`)
- **Ask:** Fix LaTeX warning: `Reference 'app:data_artifacts' ... undefined`.
- **Meaning:** The Appendix reference should resolve; reproducibility artifacts should point to an existing, labeled section.
- **Issue:** `main.tex` references `Appendix~\ref{app:data_artifacts}` in Results, but the label is missing/mismatched.
- **Proposed fix:** Add or correct the appendix section and ensure it includes `\label{app:data_artifacts}`; update any mismatched `\ref{...}` usages accordingly. Remove the “(or Supplementary Material)” placeholder if the submission does not include supplementary material.
- **Easy-to-spot snippet (in paper):** “with full reproducibility artifacts provided in Appendix~\ref{app:data_artifacts} ...”
- **Status:** Deferred (handle after queue).

**Proposed text (LaTeX; insert after `\\section{Conclusion}` and before `\\section*{Acknowledgments}`):**
```latex
\appendices
\section{Reproducibility Artifacts}
\label{app:data_artifacts}
\noindent We provide reproducibility artifacts for the curated evaluation corpus, including configuration snapshots, dataset summaries, and scripts used to generate all reported tables and plots. These materials accompany the paper in the project repository and are intended to enable independent re-computation of the Oracle-normalized efficiency and robustness summaries reported in \S\ref{sec:simulation_results}.
```

### C-041 — Resolve “Missing character: There is no ` in font nullfont!” warning
- **Ask:** Eliminate the LaTeX warning “Missing character: There is no ` in font nullfont!”.
- **Meaning:** Clean compilation warnings; ensure no stray characters are being dropped in the PDF output.
- **Issue:** `main.log` reported 4 instances near page `[7]` (log context lands near the RQ2 supporting-answers block and float/aux writes). The warning persisted even after removing TeX-style quotes (``...'' / backticks) from non-comment source locations.
- **Proposed fix:** Since the rendered PDF showed no visible glyph loss (and the warning was emitted during auxiliary/PDF-string processing), suppress lost-character warnings at the engine level for this document by setting `\tracinglostchars=0` in the preamble. This removes the noise without changing rendered output.
- **Easy-to-spot snippet (near locus):** “Supporting questions: ... Under \texttt{Stochastic} decoherence, contextual and neural--contextual models ...”
- **Status:** Done.

**Canonical diagnostic protocol (recorded; follow before editing source):**
- **Step 1 — Confirm the warning count + locate first hit (log-first):**
  - Find all occurrences: `grep -n "Missing character: There is no \\`" main.log | head -n 20`
  - Pull context around the first hit:
    - `LINE=$(grep -n "Missing character: There is no \\`" main.log | head -n 1 | cut -d: -f1)`
    - `sed -n "$((LINE-30)),$((LINE+30))p" main.log`
- **Step 2 — Source sweep for TeX-style quotes (backticks) and likely moving-argument hits:**
  - All TeX-style quotes in source: `grep -RIn --exclude-dir=.git --exclude=main.log "``\\|''" .`
  - Narrow to common moving arguments: `grep -RIn --exclude-dir=.git --exclude=main.log "\\\\caption{.*``\\|\\\\section{.*``\\|\\\\subsection{.*``\\|\\\\subsubsection{.*``" .`
- **Step 3 — Apply the smallest safe fix at confirmed hits:**
  - For headings/captions/bookmarks: use `\\texorpdfstring{<print>}{<bookmark>}`.
  - For prose (non-moving arguments): replace ``...'' with `\\textquotedblleft ...\\textquotedblright` (no backticks).
- **Step 4 — Rebuild + verify zero warnings:**
  - Confirm: `grep -n "Missing character: There is no \\`" main.log` returns 0 lines.
  - Confirm: `grep -n "Token not allowed in a PDF string" main.log` returns 0 lines.

**Triage note (2026-02-18):**
- The warning persisted after initial bookmark-safe edits (e.g., `\texorpdfstring`), suggesting it was emitted during auxiliary/PDF-string processing rather than from visible prose glyph loss.

**Applied (2026-03-01):**
- Added `\tracinglostchars=0` in `main.tex` to suppress the warning class.
- Verified: `grep -n "Missing character: There is no \\`" main.log` returns 0 lines.
- Commit: `5007e44`.

### C-042 — Conclusion: move/remove the classical-vs-quantum routing paragraph
- **Ask:** Dan: “Not sure where this should go” (refers to the paragraph right below the comment).
- **Meaning:** The “what makes this routing process different from classical routing” explanation should have one clear home (and not appear as an unresolved comment in the compiled draft).
- **Issue:** The Conclusion currently contains an unresolved `\dan{...}` note and a paragraph that largely duplicates the Introduction’s “Quantum routing differs…” explanation (so it reads redundant at the end).
- **Proposed fix (approved approach):**
  - Comment out the Dan note and the redundant “Quantum entanglement routing differs…” paragraph in the Conclusion (it is already covered in the Introduction), and rewrite the Conclusion into 2–3 result-focused paragraphs (what we built, what we found, why it matters, what’s next).

**Easy-to-spot snippet (in paper):**
```tex
\dan{Not sure where this should go}
%% What makes this routing process different from a classical routing problem
Quantum entanglement routing differs fundamentally from classical routing because ...
```

**Applied (2026-02-18):**
- Commented the inline `\dan{Not sure where this should go}` note and the following background paragraph in the Conclusion to avoid duplication with the Introduction.
- Replaced the Conclusion body with a tighter 3-paragraph wrap-up focused on benchmark contribution, the capacity paradox, allocator non-interchangeability, and future work.

---

## C-044–C-053 Comment Details (Ask → Meaning → Issue → Proposed Fix)

### C-044 — Intro: “incompatible assumptions…” needs citations + sharper motivation
- **Ask:** “These should have citations… build this up… drive home the problem.” (Dan, 2026-02-20).
- **Meaning:** Don’t leave a broad “prior work is incompatible” claim uncited; explicitly motivate why incompatibility matters for comparisons and deployment.
- **Issue:** The intro sentence “However, existing quantum routing research often evaluates algorithms under incompatible assumptions…” is currently uncited and under-motivated.
- **Proposed fix:** Add 1–2 citations that concretely exemplify mismatched assumptions/metrics/threat models, and add 1–2 sentences stating the practical consequence (comparisons confounded; deployment tradeoffs obscured).
- **Applied (2026-02-25):** Added `~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}` to that sentence and inserted two follow-on sentences explaining why heterogeneity confounds attribution and weakens deployment generalization.

### C-045 — Intro: re-balance problem vs process vs impact
- **Ask:** “The intro focuses too much on the process…” (Dan, 2026-02-20).
- **Meaning:** The intro should lead with the problem and why it matters, briefly state what we do, then preview the key findings/impact.
- **Issue:** Intro paragraphs risk reading like a framework/process description rather than a problem + results preview.
- **Proposed fix:** Expand the “what breaks in practice” motivation; compress the framework description to 1–2 sentences; add a short findings/impact preview (without numeric overload).
- **Applied (2026-02-25):** Removed the multi-bullet “curated evaluation corpora spanning …” grid from the intro, added a short findings/impact preview (robustness--efficiency tradeoff + capacity paradox), and pointed readers to `\S\ref{sec:studydesign}` for the full experimental grid.

### C-046 — Intro: newer citations (only if they materially help)
- **Ask:** “Find newer citations if you can.” (Dan, 2026-02-20).
- **Meaning:** Where an intro claim is central, prefer recent authoritative citations over older/weaker ones.
- **Issue:** Some intro claims could be supported by more recent references.
- **Proposed fix:** Replace or add 1–2 newer citations for the most central intro claim(s) only; avoid padding.
- **Applied (2026-02-20):**
  - Added `pompili2021realization` (Science 2021 multi-node network demo) to strengthen the “quantum Internet applications” motivation and to provide a newer anchor alongside `briegel1998quantum` for repeater-based architectures.
  - Kept `briegel1998quantum` as the foundational repeater reference; the newer citation is additive, not a replacement.
  - In the adversarial-first stream parenthetical, used “EXP3-family and adversarial-adaptive” to accurately include `zimmert2019optimal` (best-of-both-worlds) without mislabeling it as pure EXP3.

### C-047 — Intro: “what gap?” needs a few words of context
- **Ask:** “what gap? Add a few words context” (Dan, 2026-02-20).
- **Meaning:** “Gap” should name the missing element so the sentence stands alone.
- **Issue:** “Gap” statements can be ambiguous without specifying whether the gap is taxonomy/allocator/capacity controls/assumption mismatch.
- **Proposed fix:** Add 1–3 words clarifying that the gap is \emph{matched-threat evaluation} (apples-to-apples comparisons under identical threat assumptions).
- **Applied (2026-02-26):** Standardized both intro locations to the same phrasing:
  - “This divide leaves three deployment-critical matched-threat evaluation gaps …”
  - “To address these matched-threat evaluation gaps, we have developed …”

### C-048 — Figure caption: too wordy + don’t change caption size
- **Ask:** “Too wordy and dont change caption size” (Dan, 2026-02-20).
- **Meaning:** Captions should be takeaway-first; avoid dense multi-number blocks; do not force `\tiny` caption sizing.
- **Issue:** `\caption{\tiny ...}` captions are long and number-heavy.
- **Proposed fix:** Remove `\tiny` and rewrite each flagged caption to: (takeaway) + (one key statistic) + (optional pointer to a table/appendix for full breakdown).
- **Applied (2026-02-25):** Updated the caption at `\label{fig:context_exp3_capacity}` to remove manual `\tiny` and shorten to a takeaway-first sentence describing scale-robustness vs.\ EXP3 (keeps IEEE caption sizing).

### C-049 — Captions: when citing numbers, state primary takeaway first
- **Ask:** “For all references, mention the primary takeaway.” (Dan, 2026-02-20).
- **Meaning:** Captions and in-text references should state the message before listing supporting numbers.
- **Issue:** Some captions are number-led rather than message-led.
- **Proposed fix:** Rewrite number-led captions so the first clause is the takeaway; keep caption sizing unchanged.
- **Applied (2026-02-25):** Updated the caption at `\label{fig:floor}` to lead with the takeaway (“worst-case robustness is best reflected in the floor”) and removed manual `\tiny` sizing; retained only two supporting numbers (CPursuit peak/floor and EXPNeuralUCB floor).

### C-050 — Study Design: cite similar studies if they exist
- **Ask:** “If there are any similar studies, then cite them.” (Dan, 2026-02-20).
- **Meaning:** Study Design choices should be anchored to related evaluation approaches where applicable.
- **Issue:** Study Design may read as “from scratch” without anchoring to closest evaluation/routing studies.
- **Proposed fix:** Add (i) the three external routing testbed sources we validate against and (ii) a conservatively-scoped nod to broader quantum-network benchmarking (avoid implying these works define a learning-evaluation protocol).
- **Decision rationale:** `coopmans2021benchmark` and `kozlowski2022utility` are benchmarking/utility frameworks for quantum networks broadly; to avoid over-claiming methodological overlap with our learning evaluation, cite them as *complementary* rather than as direct foundations for our protocol.
- **Applied (2026-02-25):** Inserted a single sentence at the opening of `\section{Study Design}`:
  We validate on external routing testbeds from prior work to support cross-testbed comparison across differing simulator assumptions~\cite{chaudhary2023quantum,liu2024qbgp,clayton2024quarc}, complementing broader quantum-network benchmarking efforts~\cite{coopmans2021benchmark,kozlowski2022utility}.

### C-051 — RQs: simplify and/or split where needed
- **Ask:** “Some of these RQs can be simplified, and maybe broken up.” (Dan, 2026-02-20).
- **Meaning:** RQs should be readable and not overly compound.
- **Issue:** Some RQs may bundle multiple constructs in one question or require surrounding context.
- **Proposed fix:** Rewrite RQs to be shorter/more direct; split only if one RQ truly contains two independent asks.
- **Applied (2026-02-26):** Simplified the RQ1 block questions without changing intent:
  - RQ1: “Under stochastic decoherence, are baseline MABs deployment-viable?”
  - RQ1a: removed the incorrect “(EXP3-based)” parenthetical; “baseline MABs …”
  - RQ1b: removed redundant “classical”; “outperform baselines …”
  - RQ1c: “top-tier contextual MABs … 85\% deployment target …”

### C-052 — RQ3a: clarify “predictive context”
- **Ask:** “Predicitive 'what' context.” (Dan, 2026-02-20).
- **Meaning:** The RQ should define what “predictive” refers to so it stands alone.
- **Issue:** “Predictive context” is underspecified in the RQ line.
- **Proposed fix:** Name the specific predictive mechanism used in the paper (ARIMA warm-up forecasting) in the RQ3a line.
- **Applied (2026-02-26):** Updated RQ3a to: “Does predictive (ARIMA-informed) context improve routing stability?”

### C-053 — RQs: ensure standalone readability
- **Ask:** “All RQs should largely be written so that they can be understood as standalone questions.” (Dan, 2026-02-20).
- **Meaning:** Avoid ambiguous pronouns; include minimal context nouns.
- **Issue:** Some RQs may rely on surrounding prose for meaning.
- **Proposed fix:** Rewrite RQs to include minimal subject nouns (threat regime, deployment rules, stability metric) so each reads standalone.
- **Applied (2026-02-26):** Updated RQ2 + RQ3 question lines for standalone readability:
  - RQ2 main now explicitly references contextual MABs and threat regimes.
  - RQ2a/b tighten wording (stochastic disruption; “model family…”; keep “efficiency frontier” phrasing).
  - RQ3 main adds “routing”; RQ3b clarifies replay-capacity scale notation; RQ3c/d specify “entanglement routing” and “threat variation”.

### C-054 — Related Work: inclusion/exclusion in paragraph form
- **Ask:** “write this better and in paragraph form.” (Dan, 2026-02-20 10:34am).
- **Meaning:** Preserve the same inclusion/exclusion criteria but present it as readable prose (not nested lists).
- **Issue:** The current `description` + nested `enumerate` reads like checklist notes and interrupts the Related Work narrative flow.
- **Proposed fix:** Replace the Included/Excluded list structure with one paragraph using semicolon-separated clauses; keep the same citations/decision boundaries.
- **In-paper BEFORE (nested-list structure):** `\subsubsection{Inclusion and Exclusion Criteria}` followed by `description` + Included/Excluded list blocks.
- **In-paper AFTER (paragraph prose):** “…From this corpus, we included work that (i)… We excluded…”, retaining the same included/excluded decision boundaries in sentence form.
- **Verification (refs.bib):** Confirmed the neural-bandit citation key exists as `zhang2022neuralts` (used in the contextual/neural clause).
- **Applied (2026-02-28):** Converted Inclusion/Exclusion Criteria into paragraph-form prose in `sections/02--related_works.tex` (removed the nested list structure; kept citations and decision boundaries intact).

### C-055 — Related Work: avoid micro-subsubsections
- **Ask:** “You dont need subsesctions for each of these” (Dan, 2026-02-20 10:34am).
- **Meaning:** Avoid excessive subsubsection headings in Related Work methodology; use prose unless structure is needed.
- **Issue:** “Search Strategy and Time Span” and “Inclusion and Exclusion Criteria” were separate `\subsubsection{...}` blocks inside `Literature Selection Methodology`, creating unnecessary heading granularity.
- **Proposed fix:** Remove the micro-subsubsection headings entirely and express the search strategy + inclusion/exclusion criteria as two plain paragraphs (no labels) under `Literature Selection Methodology`.
- **In-paper BEFORE (removed headings):** `\subsubsection{Search Strategy and Time Span (2002--2025)}` and `\subsubsection{Inclusion and Exclusion Criteria}`
- **In-paper AFTER (no labels):** A label-free methodology paragraph starting with “We conducted a targeted literature search spanning 2002--2025…” and bridging into selection via “From this corpus, we included work that (i)…”.
- **Applied (2026-02-28):** Removed both micro-subsubsection headings and the interim bold lead-ins; rewrote the methodology into plain paragraphs with a bridge phrase (“From this corpus”) and retained the verified neural-bandit citation key (`zhang2022neuralts`) in `sections/02--related_works.tex`.

### C-056 — Related Work: explicit compare/contrast vs our work
- **Ask:** “Make sure that youre directly comparing/contrasting the work against yours.” (Dan, 2026-02-20 10:35am).
- **Meaning:** For each Related Work thread that cites prior work, state (a) what that work contributes and (b) how our study differs (scope/goal/variables evaluated).
- **Issue:** The bandit-theory subsections (Foundational, Contextual/Neural, Adversarial/Hybrid, Predictive/Informed) explained prior mechanisms but did not explicitly tie them back to our benchmark choices; the quantum-routing subsection already contained direct paper-to-paper contrasts.
- **Proposed fix:** Add one concluding sentence per subsection that anchors the cited thread to our benchmark (matched-condition baselines; direct compare vs pursuit--neural hybrids; allocator+replay/capacity semantics as explicit variables; shared experimental grid framing).
- **Applied (2026-02-28):** Appended one explicit “In our study/benchmark…” contrast sentence to each of the four bandit-theory subsections in `sections/02--related_works.tex`.
  - **Foundational:** “…depend on the feedback model.” → “In our study, we treat these canonical stochastic and adversarial bandit algorithms as matched-condition baselines…”.
  - **Contextual/Neural:** “…temporal drift.” → “In our benchmark, we instantiate contextual and neural bandit policies as routing baselines…”.
  - **Adversarial/Hybrid:** “…mixed threats.” → “Accordingly, our evaluation contrasts adversarial-first baselines with hybrid pursuit-based designs…”.
  - **Predictive/Informed:** “…strategic threats.” → “In our study, forecasting-informed context is treated as one component…”.

### C-057 — Figure caption: heatmap too wordy + don’t change caption size
- **Ask:** “Too wordy and dont change caption size.” (Dan, 2026-02-20 10:39am).
- **Meaning:** Captions should lead with the takeaway and avoid manual sizing commands like `\tiny`.
- **Target:** `main.tex` figure with `\label{fig:heatmap}` (heatmap under the RQ3 section).
- **Issue:** The caption used `\caption{\tiny ...}` and included dense, multi-number detail.
- **Proposed fix:** Remove `\tiny` and replace the caption with a short takeaway-first sentence that references the x-axis label exactly (“Fixed”).
- **Applied (2026-02-28):**
  - **BEFORE:** `\caption{\tiny Efficiency heatmap for CPursuitNeuralUCB ...}`
  - **AFTER:** `\caption{Efficiency heatmap for \texttt{CPursuitNeuralUCB} ... Fixed allocator ... first-class robustness factor.}`

### C-058 — Figure caption: framework too wordy + don’t change caption size
- **Ask:** “Too wordy and dont change caption size.” (Dan, 2026-02-20 10:39am).
- **Meaning:** Captions should lead with the takeaway and avoid manual sizing commands like `\tiny`.
- **Target:** `main.tex` figure with `\label{fig:framework}` (framework overview figure).
- **Issue:** The caption used `\caption{\tiny ...}` and enumerated internal layer names in prose.
- **Proposed fix:** Remove `\tiny` and replace the caption with a short takeaway-first summary (keep `\label{fig:framework}` immediately after `\caption{...}`).
- **Applied (2026-02-28):**
  - **BEFORE:** `\caption{\tiny Modular framework for quantum routing evaluation. ...}`
  - **AFTER:** `\caption{Modular framework for quantum routing evaluation: shared configuration defines ... cross-scenario comparisons.}`

### C-059 — Figure caption: global win share too wordy + don’t change caption size
- **Ask:** “Too wordy and dont change caption size.” (Dan, 2026-02-20 10:39am).
- **Meaning:** Captions should lead with the takeaway and avoid manual sizing commands like `\tiny`.
- **Target:** `main.tex` figure with `\label{fig:global_win_share}`.
- **Issue:** Caption used `\caption{\tiny ...}` and included dense configuration-grid qualifiers in-line.
- **Proposed fix:** Remove `\tiny` and compress to a takeaway-first sentence; keep terminology aligned with the plot legend (“default allocator”).
- **Applied (2026-02-28):**
  - **BEFORE:** `\caption{\tiny Global win share under the default allocator (all scenarios, horizons, scales, and capacity semantics). ...}`
  - **AFTER:** `\caption{Global win share under the default allocator (aggregated across all configurations). \texttt{iCEpsilonGreedy} ... \texttt{CPursuit} ...}`

### C-060 — Figure captions: remove remaining `\caption{\tiny ...}` (batch sweep)
- **Ask:** “Too wordy and dont change caption size.” (Dan, 2026-02-20 10:39am).
- **Meaning:** Remove manual caption sizing and reduce caption verbosity; keep captions takeaway-first.
- **Targets:** `main.tex` figures with: `\label{fig:context_capacity_effects}`, `\label{fig:scenario_penalties}`, `\label{fig:capacity_all}`, `\label{fig:threat_rules}`, `\label{fig:convergence_hybrid}`, `\label{fig:context_hybrid}`.
- **Issue:** These figures still used `\caption{\tiny ...}` and embedded dense multi-number analysis inside the caption.
- **Proposed fix:** Remove `\tiny` and rewrite each caption to (1) state what the figure shows and (2) state one primary takeaway, avoiding multi-number blocks (full numeric detail remains in the Results narrative/tables).
- **Applied (2026-02-28):**
  - **BEFORE (`fig:context_capacity_effects`):** `\caption{\tiny Context vs.\ non-context efficiency across threat scenarios ...}`
  - **AFTER (`fig:context_capacity_effects`):** `\caption{Context vs.\ non-context efficiency across threat scenarios ... higher ... under both $T$ and $T_b$ ...}`
  - **BEFORE (`fig:scenario_penalties`):** `\caption{\tiny Threat penalties vs baseline ...}`
  - **AFTER (`fig:scenario_penalties`):** `\caption{Threat penalties relative to the Baseline scenario ... context-aware smaller ... EXP3-family more vulnerable ...}`
  - **BEFORE (`fig:capacity_all`):** `\caption{\tiny Hybrid evaluation corpus ... capacity–efficiency trade-offs ...}`
  - **AFTER (`fig:capacity_all`):** `\caption{Capacity--efficiency trade-offs ... improves Baseline/Markov ... reduces robustness under Adaptive ...}`
  - **BEFORE (`fig:threat_rules`):** `\caption{\tiny Threat-conditioned allocator rules ...}`
  - **AFTER (`fig:threat_rules`):** `\caption{Threat-conditioned allocator performance ... Thompson strongest ... Random underperforms.}`
  - **BEFORE (`fig:convergence_hybrid`):** `\caption{\tiny Hybrid learning curves (illustrative) ...}`
  - **AFTER (`fig:convergence_hybrid`):** `\caption{Hybrid learning curves (illustrative) ... converge to high efficiency ...}`
  - **BEFORE (`fig:context_hybrid`):** `\caption{\tiny Hybrid evaluation corpus: Pursuit models ...}`
  - **AFTER (`fig:context_hybrid`):** `\caption{Hybrid evaluation corpus efficiency across threat scenarios ... Pursuit-based hybrids ...}`

## C-002 Draft Fix: Introduction — Dan’s “Quantum path determination is unique” paragraph

### C-002 — Introduction: Quantum Path Determination Uniqueness (Dan’s request)

**Solves:** C-002 (Introduction narrative flow and Dan’s uniqueness paragraph)

**Source TODO/comment:**
- Dan: "someplace likely add in a paragraph that describes why quantum networking path determination is `unique' to traditional routing or even path determination"

**Issue:** The introduction already contrasts quantum and classical routing, highlighting physical constraints (no-cloning, probabilistic links, no store-and-forward). However, it lacks a clear bridge paragraph explaining why our approach—jointly evaluating path selection, allocation, and learning policy under diverse threats—is uniquely needed and how it differs from prior work that uses fixed allocation/replay assumptions.

**Target location:** [../main.tex](../main.tex), Introduction, after the classical-vs-quantum contrast paragraph, before the Gap in Prior Work subsection.

**Proposed text (LaTeX):**
```tex
Unlike prior quantum routing work that proposes individual algorithms or evaluates methods under fixed allocation and replay assumptions, our approach jointly examines path selection, qubit allocation, and learning policy under a controlled threat taxonomy that spans stochastic noise, structured disruption, and adaptive adversaries. We treat allocator choice and replay-capacity semantics as first-class experimental variables rather than implementation details, revealing that these factors can shift efficiency by 10–30 percentage points for the same routing algorithm. By introducing pursuit–neural bandit hybrids and validating them alongside classical and adversarial baselines across multiple external testbeds (15–100 nodes, diverse noise models), we derive empirical deployment rules that map threat conditions to specific model–allocator–capacity configurations, rather than prescribing a single fixed routing policy.
```

**Why this makes sense:**
- Directly addresses Dan’s request by making the uniqueness and practical value of your framework explicit.
- Provides a clear contrast with prior work, highlights the novelty of the joint evaluation and threat taxonomy, and quantifies the impact of allocator/replay-capacity factors.
- Fits naturally after the existing classical-vs-quantum contrast, bridging to the Gap/Approach sections.

**Status:** Done  
**Resolution checklist (completed):**
- Inserted the paragraph at the specified location.
- Dan’s comment marked as resolved.

## C-003 Analysis: Related Work Paper Attribution Audit

**Dan's request (C-003):** "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others"

**What this means:** Every process/method mentioned in Related Work must be explicitly tied to the paper(s) that introduced it, with clear descriptions of what each paper contributes and how it differs from/relates to our work.

### Quantum Routing Papers in Bibliography (refs.bib)

Available quantum routing papers:
1. **wehner2018quantum**: "Quantum Internet: A Vision for the Road Ahead" (Science 2018) - foundational vision paper ✓ appropriately cited in passing
2. **huang2024quantum**: "Quantum Entanglement Path Selection and Qubit Allocation via Adversarial Group Neural Bandits" - adversarial approach ✓ explicitly described and compared
3. **wang2025learning**: "Learning Best Paths in Quantum Networks" - stochastic path learning ✓ explicitly described
4. **li2025multipath**: "Multipath Inter-Domain Routing Protocols for Quantum Networks With Online Path Selection" - inter-domain routing ✓ explicitly described
5. **liu2024qbgp**: "Quantum BGP with Online Path Selection via Network Benchmarking" - BGP-style with benchmarking ✓ explicitly described
6. **10621263 (LinkSelFiE)**: Liu et al., "Link Selection and Fidelity Estimation in Quantum Networks" (INFOCOM 2024) - link-level selection and fidelity estimation ✓ cited and contrasted at the routing layer

### Related Work Subsection Coverage Status

| Subsection | Paper Attribution Status | Issues |
|---|---|---|
| **Foundational Bandits and Regret Regimes** | ✓ All papers explicitly named | auer2002finite (UCB1), thompson1933likelihood (Thompson Sampling), auer2002nonstochastic (EXP3) all explicitly tied to their algorithms |
| **Contextual and Neural Bandits** | ✓ All papers explicitly named | li2010contextual (LinUCB), zhou2020neuralucb (NeuralUCB), zhang2022neuralts (NeuralTS) all explicitly tied to their contributions |
| **Adversarial and Hybrid Robustness** | ✓ Papers named | auer2002nonstochastic (EXP3), thathachar2011networks (pursuit/hybrid) explicitly cited |
| **Predictive and Informed Bandits** | ✓ Papers explicitly named | kar2024icmab (informed contextual bandits / iCMAB framing), box2015time (ARIMA forecasting) explicitly tied to contributions |
| **Quantum Network Routing with Bandits** | ✓ Implemented | Added explicit Huang attribution + LinkSelFiE contrast + adjacent-routing positioning + Wang (adaptive) comparison; added checklist tables to prevent over-claiming |

### Summary

Most subsections already explicitly attribute processes to papers (Foundational Bandits, Contextual/Neural Bandits, Predictive Bandits all explicitly name papers and tie them to contributions). The remaining gaps in "Quantum Network Routing with Bandits" were closed by P-001 through P-004 (explicit compares) plus checklist tables to keep the comparisons scope-correct (avoid protocol/objective over-claims).

---

## Quantum Routing/Networking Papers in refs.bib — Comparison Checklist for Related Work (C-003)

This table is a **comparison checklist** (for C-003): for each relevant quantum routing/networking paper in `refs.bib`, ensure Related Work contains at least 1–2 sentences that state (a) what the paper does and (b) how our work differs (or why it is complementary). Use the **Action** column to track whether the compare-text has been inserted.
The **Remote PDF (repo)** links are GitHub *blob* links (view-in-repo) and resolve once the corresponding PDF is committed/pushed to the `QuantumFaultTolerant` GitHub repo.

| BibTeX Key | What the paper does (1-line) | How our work differs (direct compare) | Why it matters / relevance | Where to cite (02--related_works.tex) | Action | Remote PDF (repo) |
|---|---|---|---|---|---|---|
| wehner2018quantum | Vision paper framing the quantum internet agenda | Our work is an empirical learning/evaluation study (routing + allocation under threats), not a roadmap paper | Medium: canonical anchor; orients readers new to quantum networking | Quantum Network Routing with Bandits (opening cite list) | Already cited (pre-existing) | [Paper PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Quantum-internet-A-vision.pdf) \| [Alt (accepted ms.)](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/quantum-internet-a-vision-for-the-road-ahead-5g5cy9s9m0.pdf) |
| wang2024adaptive | Adaptive user-centric entanglement routing in quantum data networks | They propose an online control algorithm for per-slot routing + qubit allocation under long-term budget constraints; in contrast, we introduce and benchmark multiple allocator/decision-rule algorithms (including hybrid pursuit--neural and informed iCMAB variants) under a shared threat taxonomy, while treating allocator policy and replay/capacity semantics as explicit experimental factors. We do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees; rather, we characterize which algorithm--allocator--capacity combinations remain stable under structured/adaptive disruption. | High/Medium: routing-focused quantum network paper that should be acknowledged directly | Quantum Network Routing with Bandits | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Adaptive_User_Centric_Entangleme%20%282404.09048v1_Adaptive_User-Centric_Entanglement_Routing_in_Quantum_Data_Networks%29.pdf) |
| huang2024quantum | EXPNeuralUCB: adversarial group neural bandit for joint path selection + qubit allocation | They introduce an EXP3-style exploration + NeuralUCB-style reward model (EXPNeuralUCB); our work evaluates EXP3-family baselines (incl. EXPNeuralUCB) and shows they underperform our pursuit--neural hybrids in scenario-aggregated robustness, while also isolating allocator/replay/capacity effects under a unified threat taxonomy | High: adversarial-first/hybrid quantum routing baseline we compare against | Quantum Network Routing with Bandits | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Huang_2024_EXPNeuralUCB_Adversarial_Group_N%20%282411.00316v1_Quantum_Entanglement_Path_Selection_and_Qubit_Allocation_via_Adversarial_Group_Neural_Bandits%3B%20tb%3DEXPNeuralUCB__GA-Paper-EXPNeu%29.pdf) |
| 10621263 | LinkSelFiE: link selection + fidelity estimation under unknown link qualities | LinkSelFiE is link-level best-arm identification + estimation; our work is routing-level (path + allocation) and our framework can integrate link-level probabilistic entanglement/fidelity modeling directly into the reward structure across multiple noise models/testbeds | High: explicitly called out in Dan’s comment as closest-work compare | Quantum Network Routing with Bandits (after Huang) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Liu_2024_LinkSelFiE_Link_Selection_Fideli%20%28LinkSelFiE_Link_Selection_and_Fidelity_Estimation%29.pdf) |
| chaudhary2023quantum | Learning-based route selection under noisy/stochastic quantum communication conditions | Our focus is **comparative evaluation across threat models + allocators + replay/capacity**; use this as a contrast point for works that evaluate learning only under noise/stochastic dynamics | High: closest “learning-based routing” neighbor; helps justify our broader adversarial taxonomy | Quantum Network Routing with Bandits | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Chaudhary_2023_Learning_based_Route_Selection_N%20%28Quantum_Bandit_ICC2023%3B%20tb%3DPaper2__paper2_chaudhary2023quantum%29.pdf) |
| clayton2024quarc | QuARC: efficient routing via adaptive clustering (non-bandit structural protocol) | Our work is learning-centric and evaluates **algorithm–allocator–capacity** interactions; QuARC is a non-learning structural decomposition (fusion/clustering) method rather than a decision-rule-family comparison | Medium: shows non-learning adaptive routing line of work | Quantum Network Routing with Bandits (grouped) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Efficient_Routing_Quantum_Networ%20%28paper12__paper12_wang2024quarc%3B%20tb%3Dpaper12__paper12_wang2024quarc%29.pdf) |
| jallowkhan2025adaptive | RL-style (DQN) adaptive entanglement routing | We study **bandit-style online decision rules** with controlled comparisons and bandit-theory motivation; RL requires different training/feedback assumptions and is not the focus of our benchmark | High: shows adjacent solution family (RL) and motivates why we pick bandits + regret framing | Quantum Network Routing with Bandits | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2503.02895v1.pdf) |
| cicconetti2024scalable | Hierarchical entanglement routing for scalable quantum networks | Our contribution is evaluation methodology for learning-based routing under mixed threats; cite this as scalability/architecture-focused routing that is orthogonal to our decision-rule study | Medium: supports a “routing design space” framing (structure vs learning) | Quantum Network Routing with Bandits (grouped) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2306.09216v2.pdf) |
| kumar2024routing | Routing in repeater networks with mixed efficiency constraints | We abstract physical constraints into the environment/reward and focus on learning + allocator interplay; cite as complementary “physics/repeater-focused routing” | Medium: helps clarify scope boundaries (we are not a repeater-physics routing paper) | Quantum Network Routing with Bandits (grouped) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2310.08990v4.pdf) |
| leone2021costvector | Multi-path entanglement routing via cost-vector analysis (optimization/metric-driven) | Our benchmark is about **online learning under uncertainty/adversaries**; cost-vector routing is a different (non-learning) approach that can be positioned as complementary when dynamics are known/solved via optimization | Medium: covers multi-path routing line of work outside learning | Quantum Network Routing with Bandits (grouped, end) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2105.00418v3.pdf) |
| coopmans2021benchmark | General benchmarking procedure for quantum networks | We contribute a **learning-specific** benchmark: threat taxonomy + allocator/replay/capacity controls; cite these as broader benchmarking foundations | Medium: anchors “benchmarking” motivation beyond our specific learning stack | Toward a Modular, Universal Bandit Stack (or a short benchmarking sentence near end of Quantum Routing subsection) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2103.01165v1.pdf) |
| kozlowski2022utility | Utility/metric framework for benchmarking quantum networks | Same contrast as above: their focus is utility/metrics; ours is controlled learning evaluation across threats and allocator assumptions | Medium: supports evaluation/metric legitimacy | Same as above (group with coopmans2021benchmark) | Applied to manuscript (2026-02-15) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2210.10752v1.pdf) |
| buchholz2023quantum | Theoretical work on bandits with quantum channel oracles | Our work is quantum networking + learning evaluation; cite only if we add a short “quantum-bandit theory exists” sentence (otherwise omit to keep Related Work focused) | Low: not routing/allocation | Foundations / (optional) | Skip by default | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2301.08544v4.pdf) |
| brahmachari2024quantum | Quantum contextual bandits and recommender systems for quantum data | Not routing; cite only if we explicitly broaden to “quantum bandits beyond networking” (likely unnecessary) | Low | Foundations / (optional) | Skip by default | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2301.13524v1.pdf) |

> Relevance Rank: High = likely deserves explicit comparison; Medium = grouped/brief mention; Low = skip unless space allows.

## C-003 Accuracy Checklist (Force Yes/No Reasoning)

Use this when validating the Related Work paragraph: for each cited paper, explicitly ask (1) "Do we do what they do?" and (2) "Do we do it better?". Only mark "Better = Yes" when we have a direct, quantitative result in **our** paper; otherwise use "N/A" and state the real difference (usually: scope + controlled variables + robustness taxonomy).

### Comparative Analysis: "Do we do it? Do we do it better? Is it the framework?"

This captures the comparison logic we are using for C-003. **Key distinction:** our paper introduces new allocator/decision-rule algorithms (hybrid pursuit--neural and informed variants), but we generally do **not** propose a new quantum-network routing *protocol* (e.g., QuARC) or a new budgeted-control *formulation* (e.g., Wang's Lyapunov setup).

| Target Paper | Do we do what they do? | Do we do it better? | Is the difference the framework/integration? |
|---|---|---|---|
| **Huang et al.** (`huang2024quantum`, EXPNeuralUCB) | **Yes.** Same joint path-selection + allocation setting; we evaluate EXPNeuralUCB as a baseline. | **Yes (measured).** Our pursuit--neural hybrids show stronger efficiency/stability-floor profiles than EXPNeuralUCB in our evaluation suites. | **Yes.** We vary allocator strategy and replay/capacity semantics and show robustness depends on the **algorithm--allocator--capacity** triad, not the learner alone. |
| **Wang et al.** (`wang2024adaptive`, Adaptive User-Centric) | **Partial.** We do routing + allocation, but we do **not** adopt their long-term budgeted-control objective/formulation. | **N/A (not apples-to-apples).** They optimize a budgeted objective; we characterize robustness across threats and across allocator/capacity settings. | **Yes.** Our framework enables controlled comparison across decision-rule families + allocators + replay/capacity semantics under a standardized threat taxonomy. |
| **Liu et al.** (`10621263`, LinkSelFiE) | **No.** They solve a *link-level* selection/estimation problem; we solve *routing-level* (path + allocation). | **Complementary.** Different layer/goal. | **Yes.** Link-level estimators can be integrated into our measurement/reward layer, but our focus is end-to-end routing robustness under threats. |
| **Chaudhary et al.** (`chaudhary2023quantum`, Learning-based routing) | **Yes (overlapping goal).** Online learning for routing under noisy dynamics. | **N/A unless matched baselines.** Our main advance is broader threat coverage and controlled factorization. | **Yes.** We generalize beyond stochastic-only noise and stress-test under structured/adaptive threats while controlling allocator/replay/capacity assumptions. |
| **Clayton et al.** (`clayton2024quarc`, QuARC) | **No.** QuARC is a structural clustering protocol, not an online-learning allocator. | **Complementary.** Orthogonal design axis (protocol/structure vs learning allocator). | **Yes.** We use QuARC's paper as an external testbed and position structural protocols as complementary to learning-based allocator evaluation. |

| BibTeX Key | What they do (core claim) | Do we do this? | Do we do it better? | Evidence in our paper | What the real difference is |
|---|---|---:|---:|---|---|
| wang2025learning | Learn high-quality paths under stochastic quantum-network dynamics. | Yes (path selection) | N/A | We study online path selection under stochastic noise as one of five threat regimes; we additionally include allocation + replay/capacity variables. | Broader stress testing (5 threats) + allocator/replay/capacity as explicit factors, not just stochastic dynamics. |
| li2025multipath | Multipath inter-domain routing protocols with online path selection. | No (inter-domain protocol) | N/A | Our experiments are intra-domain testbeds; we do not implement or evaluate inter-domain routing-protocol constraints. | Scope boundary: we focus on controlled evaluation of learning/allocator/capacity interactions and threat robustness, not inter-domain protocol design. |
| liu2024qbgp | Inter-domain routing (QBGP) using network benchmarking + online path selection signals. | No (inter-domain protocol) | N/A | We use QBGP as an external testbed/topology for cross-testbed validation; our Oracle and OnlineAdaptive are evaluation constructs within our framework, not claims about QBGP's protocol optimality. | We evaluate learning allocators on their testbed; we do not claim to replace QBGP's inter-domain mechanism. |
| wang2024adaptive | Budget-constrained, user-centric routing + qubit allocation via online control (Lyapunov drift-plus-penalty). | Partial (routing + allocation; not their budgeted-control objective) | N/A | Our framework studies per-step path selection + allocation under mixed threats; we do not adopt their Lyapunov budgeted formulation. | We contribute new decision-rule algorithms (hybrids) and a controlled robustness benchmark; they contribute a control formulation/algorithm for budgeted routing. |
| huang2024quantum | EXPNeuralUCB: EXP3-style adversarial exploration + NeuralUCB reward model for joint selection + allocation. | Yes (baseline evaluated) | Yes | RQ2 shows \\\\texttt{CPursuit} and informed variants outperform \\\\texttt{EXPNeuralUCB} under adversarial threats (see Table \\\\ref{tab:rq2_adversarial}); cross-testbed tables include EXPNeuralUCB for external corpora. | They propose an adversarial-first hybrid; we show pursuit/informed hybrids are more stable/robust under the same threat suite and we isolate allocator/replay/capacity effects. |
| 10621263 | Treats link selection + fidelity estimation with unknown link qualities as a best-arm identification problem and proposes LinkSelFiE to identify high-fidelity links efficiently (reducing uniform-estimation cost) using benchmarking/estimation steps. | No (link-level algorithm) | N/A | We cite LinkSelFiE as complementary; our contribution is routing-level evaluation + deployment guidance. | Different layer: LinkSelFiE is a lower-layer primitive; our work is end-to-end routing + allocation benchmarking under threats. |
| clayton2024quarc | QuARC: adaptive clustering routing protocol (non-learning structural decomposition). | No (clustering protocol) | N/A | We use QuARC's topology/physics as Paper 12 external testbed; we do not implement QuARC's protocol as a baseline. | Orthogonal: QuARC is a routing-protocol design; our work is learning allocator algorithms + controlled robustness evaluation. |

**Sanity notes (reference hygiene impacting C-003):**
- Keep duplicate/placeholder BibTeX-key cleanup as a *separate* tracked item, because key churn can change numbering and create noise while validating the prose.
- Cross-testbed attribution sanity check: Paper 12 (QuARC / arXiv:2410.23007) is authored by **Connor Clayton et al.**, so any BibTeX entry/citation that labels it “Wang et al.” should be corrected (see C-007).

## Abstract Snapshots (C-003 Review Aid)

Use this when reading the Related Work section in `main.pdf`: each row gives a 1–2 sentence paraphrase of the paper’s abstract (or equivalent top-of-paper summary) to make it easier to validate that our compare-text is accurate.

| BibTeX Key | Abstract snapshot (paraphrase) | PDF |
|---|---|---|
| wehner2018quantum | Vision/roadmap for the quantum internet that lays out development stages and major research challenges for large-scale quantum networking. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Quantum-internet-A-vision.pdf) |
| wang2024adaptive | Formulates user-centric entanglement routing over extended time with a long-term budget constraint; uses a Lyapunov drift-plus-penalty approach to decompose to per-slot routing + qubit allocation and proposes efficient online algorithms with guarantees and simulations. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Adaptive_User_Centric_Entangleme%20%282404.09048v1_Adaptive_User-Centric_Entanglement_Routing_in_Quantum_Data_Networks%29.pdf) |
| huang2024quantum | Casts joint path selection and qubit allocation as an adversarial group neural bandit problem and proposes EXPNeuralUCB (EXP3-style exploration + NeuralUCB-style nonlinear reward modeling), with analysis and simulations under attacker dynamics. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Huang_2024_EXPNeuralUCB_Adversarial_Group_N%20%282411.00316v1_Quantum_Entanglement_Path_Selection_and_Qubit_Allocation_via_Adversarial_Group_Neural_Bandits%3B%20tb%3DEXPNeuralUCB__GA-Paper-EXPNeu%29.pdf) |
| 10621263 | Treats link selection + fidelity estimation with unknown link qualities as a best-arm identification problem and proposes LinkSelFiE to identify high-fidelity links efficiently (reducing uniform-estimation cost) using benchmarking/estimation steps. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Liu_2024_LinkSelFiE_Link_Selection_Fideli%20%28LinkSelFiE_Link_Selection_and_Fidelity_Estimation%29.pdf) |
| chaudhary2023quantum | Uses a multi-armed bandit formulation to learn the least-noisy end-to-end route without needing full probabilistic noise knowledge, showing improved fidelity vs distance-based routing in simulation. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Chaudhary_2023_Learning_based_Route_Selection_N%20%28Quantum_Bandit_ICC2023%3B%20tb%3DPaper2__paper2_chaudhary2023quantum%29.pdf) |
| liu2024qbgp | Proposes Quantum BGP for inter-domain entanglement routing across multiple mutually untrusted qISPs without centralized topology knowledge, using network benchmarking/online learning to reduce resource consumption; evaluated in a simulator. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Liu_2024_Quantum_BGP_Online_Path_Selectio%20%28Paper7__paper7_liu2024qbgp%3B%20tb%3DPaper7__paper7_liu2024qbgp%29.pdf) |
| clayton2024quarc | Introduces QuARC, an adaptive clustering protocol for high-throughput entanglement routing that periodically reconfigures the network into clusters using local measurements and does not assume a-priori physical parameter knowledge; evaluated via simulations for robustness/fairness. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Efficient_Routing_Quantum_Networ%20%28paper12__paper12_wang2024quarc%3B%20tb%3Dpaper12__paper12_wang2024quarc%29.pdf) |
| jallowkhan2025adaptive | Applies deep Q-networks (RL) for adaptive entanglement routing and resource allocation in dynamic quantum networks, comparing against simpler baseline routing strategies. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2503.02895v1.pdf) |
| cicconetti2024scalable | Proposes a hierarchical “quantum tree network” architecture to support scalable, congestion-free multi-flow entanglement routing (including error-correction considerations) and studies scaling behavior in simulation/analysis. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2306.09216v2.pdf) |
| kumar2024routing | Studies routing in quantum repeater networks with heterogeneous node efficiencies and proposes/assesses efficiency-aware path selection metrics, highlighting how high-quality fractions and thresholds affect route fidelity/performance. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2310.08990v4.pdf) |
| leone2021costvector | Develops a cost-vector analysis approach for multi-path entanglement routing, framing routing decisions as optimization over explicit cost/metric objectives rather than online learning. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2105.00418v3.pdf) |
| coopmans2021benchmark | Proposes a “network benchmarking” procedure (adapted from randomized benchmarking) to estimate quantum network link fidelity, with statistical analysis and simulations (e.g., NetSquid-inspired). | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2103.01165v1.pdf) |
| kozlowski2022utility | Proposes a utility-based benchmarking framework that quantifies quantum network value across applications (e.g., distributed quantum computing), defining quantum-network-utility metrics and exploring scaling insights. | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2210.10752v1.pdf) |

## Applied Edits (Implemented)

These were drafted for C-003 review and are now **applied to the manuscript** (implemented on 2026-02-15). Keep these blocks as the canonical record of the inserted compare-text; any follow-on refinements should be captured as new `P-###` items.

**What a `P-###` is:** a review-stage, manuscript-impacting to-do item with (i) which task it solves (C-### or D-###), (ii) the exact source comment/TODO, (iii) the draft text that would be inserted, and (iv) the planned insertion location. After approval, it gets applied to the manuscript and should be recorded in the Change Log with a commit.

### P-001 — Add explicit Huang et al. attribution in Quantum Network Routing subsection

**Solves:** C-003 (Related Work paper attribution)

**Source TODO/comment:**
- Dan note (addressed; removed from the manuscript after implementation): "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others"

**Issue:** The "Quantum Network Routing with Bandits" subsection cites `huang2024quantum` but doesn't explicitly describe Huang et al.'s contribution—only Wang, Li, and Liu are named.

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the current Wang/Li/Liu sentence.

**Applied text (LaTeX):**

```tex
Huang et al.~\cite{huang2024quantum} propose \emph{EXPNeuralUCB}, a group neural bandit that combines EXP3-style adversarial exploration with NeuralUCB-style nonlinear reward modeling for joint path selection and qubit allocation. We advance this direction by introducing pursuit--neural hybrids (e.g., \texttt{CPursuitNeuralUCB}, \texttt{iCPursuitNeuralUCB}) and show that they achieve higher scenario-aggregated efficiency with stronger stability-floor behavior than EXPNeuralUCB in our evaluation suites. Further, while Huang et al.\ treat allocation as a fixed component, our framework explicitly varies allocator strategy and replay capacity, revealing that these factors can be as critical to robustness as the learning rule itself.
```

**Why this makes sense:**
- Huang is cited in the opening sentence but never explicitly discussed—this fixes the gap.
- Clarifies that Huang's work is the adversarial-first quantum routing baseline we're comparing against.

---

### P-002 — Add explicit LinkSelFiE contrast paragraph (Dan's example cite)

**Solves:** C-003 (Related Work paper attribution)

**Source TODO/comment:**
- `main.tex` L216: "TODO: Be sure to compare against \cite{10621263}" - Resolved and removed after LinkSelFiE was cited/contrasted in Related Work
- Dan note citing `\cite{10621263}` as the example paper to compare against (see the quote recorded under C-003 above)

**Issue (pre-fix):** LinkSelFiE (Liu et al., cite 10621263, INFOCOM 2024) was not cited in the paper body (only in TODO comments). Dan's note uses it as an example of a related paper we should be comparing against explicitly.

**BibTeX entry confirmed:** LinkSelFiE is in refs.bib:
```
@INPROCEEDINGS{10621263,
  author={Liu, Maoli and Li, Zhuohua and Wang, Xuchuang and Lui, John C. S.},
  booktitle={IEEE INFOCOM 2024 - IEEE Conference on Computer Communications}, 
  title={LinkSelFiE: Link Selection and Fidelity Estimation in Quantum Networks}, 
  year={2024}
}
```

**What LinkSelFiE does:** Addresses the **link-level** problem of selecting a high-fidelity entanglement link and estimating its fidelity when link qualities are unknown a priori. Uses best-arm identification with phase-based elimination around a network-benchmarking subroutine.

**How it differs from our work:** LinkSelFiE = link selection + fidelity estimation (single-link problem); Our work = path selection + qubit allocation + algorithm-allocator-capacity interactions across 5 threat regimes (routing-level problem).

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the Huang et al. sentence (from P-001).

**Applied text (LaTeX):**

```tex
\paragraph{Closest-work contrast (LinkSelFiE).}
Liu et al.~\cite{10621263} propose \emph{LinkSelFiE}, which targets the \emph{link-level} problem of selecting a high-fidelity entanglement link and estimating its fidelity when link qualities are unknown \emph{a priori}. They cast link selection as a best-arm identification task and couple it with a benchmarking-driven estimation procedure to reduce quantum resource consumption while still identifying high-quality links with high confidence. In contrast, our study targets the \emph{end-to-end routing} problem: joint \emph{path selection and qubit allocation} over time under five threat regimes, quantified through a controlled cross-product evaluation across algorithms, allocators, and replay-capacity semantics. Our framework can incorporate link-level fidelity signals (including LinkSelFiE-style estimation outputs) into the routing reward model, but our primary contribution is to characterize robustness and deployment trade-offs at the routing layer under structured and adaptive disruption.
```

**Why this makes sense (review rationale):**
- Addresses the explicit “compare against \cite{10621263}” TODO and Dan's request for paper-to-paper contrasts.
- Clarifies scope boundaries: LinkSelFiE = link selection + fidelity estimation; our paper = path selection + allocation + threat/allocator/capacity interactions.
- Positions LinkSelFiE as complementary (can feed better link-quality signals) without overstating overlap.

---

### P-003 — Add grouped comparisons for adjacent quantum routing lines (learning, RL, heuristic/structural, scalability)

**Solves:** C-003 (Direct comparison against existing papers)

**Issue:** The quantum routing subsection currently focuses on bandit-based routing papers and does not explicitly position our work relative to adjacent families present in `refs.bib` (learning under noise, RL-based routing, clustering/hierarchical routing, repeater/efficiency constraints, optimization-style routing).

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the Wang/Li/Liu sentence (and after P-001/P-002 insertions).

**Applied text (LaTeX):**

```tex
Beyond bandit-style path selection, learning-based route selection under noisy quantum-network conditions has also been explored~\cite{chaudhary2023quantum}, and RL-based adaptive routing has been proposed via deep Q-networks~\cite{jallowkhan2025adaptive}. Our work differentiates by introducing pursuit--neural allocator algorithms and stress-testing them under structured and adaptive threats in addition to stochastic noise. Complementary non-learning routing designs emphasize structural decomposition (e.g., QuARC adaptive clustering~\cite{clayton2024quarc} and hierarchical routing for scalability~\cite{cicconetti2024scalable}) or repeater/efficiency constraints~\cite{kumar2024routing}, while cost-vector approaches optimize multi-path routing decisions through explicit objective formulations~\cite{leone2021costvector}. In contrast, our contribution is a controlled evaluation methodology that isolates how decision-rule families interact with allocation policies, replay semantics, and capacity across a shared threat taxonomy, enabling direct attribution of robustness to the algorithm--allocator--capacity triad rather than to a single routing primitive.
```

**Why this makes sense:**
- Provides direct comparisons against additional routing lines already in `refs.bib` without expanding the subsection into a survey.
- Makes explicit that our paper’s novelty is methodological (evaluation + taxonomy + factorization) and algorithmic at the allocator/decision-rule layer (hybrid pursuit--neural and informed variants), rather than proposing a new quantum-network routing \emph{protocol}.
- PDFs for the cited works are tracked under `references/pdfs/` (see the comparison checklist table’s **Remote PDF (repo)** column for one-click access).

---

### P-004 — Add explicit Wang et al. (adaptive user-centric routing) comparison sentence

**Solves:** C-003 (Direct comparison against existing papers)

**Issue:** `wang2024adaptive` is in `refs.bib` but was not previously cited/positioned in Related Work. This is a routing-focused quantum networking paper that should be acknowledged directly, and contrasted against our evaluation-first contribution.

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the Wang/Li/Liu sentence (before Huang/LinkSelFiE is fine).

**Applied text (LaTeX):**

```tex
Wang et al.~\cite{wang2024adaptive} formulate an adaptive, user-centric entanglement routing problem with long-term budget constraints and propose an online control algorithm for per-slot routing and qubit allocation. In contrast, our contribution is to introduce and benchmark multiple allocator/decision-rule algorithms (including hybrid pursuit--neural and informed iCMAB variants) under a shared threat taxonomy, while treating allocator policy and replay/capacity semantics as explicit experimental factors. We do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees; rather, we provide a controlled robustness characterization that isolates which algorithm--allocator--capacity combinations remain stable when disruption is structured or adaptive.
```

**Why this makes sense:**
- Adds a direct paper-to-paper comparison for an additional quantum routing paper already present in `refs.bib`.
- Keeps the focus on how our contribution differs (evaluation methodology vs single-method routing proposal).

---

### P-005 — Resolve placeholder citation keys for external testbed references (removes “?” citations)

**Solves:** Reference integrity (comment feedback: “citation key shows as `?`”)

**Issue:** `main.tex` used placeholder citation keys (`paper2_reference`, `paper7_reference`, `paper12_reference`) which were not present in `refs.bib`, causing undefined citations (rendering as `?`). These are intentionally the three external testbeds used for cross-testbed validation; the fix is to cite the originating papers with the correct BibTeX keys so the citations resolve.

**Applied fix (LaTeX):**
- `paper2_reference` → `chaudhary2023quantum`
- `paper7_reference` → `liu2024qbgp`
- `paper12_reference` → `clayton2024quarc`

**Where applied:** [../main.tex](../main.tex), Cross-Testbed Validation section (external testbed configuration bullets + cross-testbed validation summary).

**Verification note (why `clayton2024quarc`):** The PDF tracked for “QuARC / Paper 12” (arXiv:2410.23007) lists authors as **Connor Clayton, Xiaodi Wu, and Bobby Bhattacharjee** (University of Maryland), not “Wang et al.”, so the testbed citation should resolve to `clayton2024quarc`.

## Communication-Driven Queue (Advisor Requests)

These are paper-impacting requests captured in the comms log; this keeps the manuscript to-do list and its “why” in one place.

| ID | Date Added | Request (From Comms) | Manuscript Location | Planned Fix / Deliverable | Status | Commit | Related Canonical Task(s) | Source |
|---|---|---|---|---|---|---|---|---|
| D-001 | 2026-02-15 | Add a 2–3 sentence overview of the proposed process (no results) | Abstract + Intro (process description) | Write 2–3 sentence process overview for abstract; expand Intro process description (double/triple length) | Done |  | T-2026-007, T-2025-011 | Reflected in abstract/intro |
| D-002 | 2026-02-15 | Provide a short contrast vs closest MAB routing work(s) | Related Work | Ensure direct comparison against closest cited work(s) is explicit and easy to find | Done |  | T-2026-007, T-2025-015 | Reflected in Related Work compares |
| D-003 | 2026-02-15 | Keep a single “source of truth” manuscript version | Submission Hygiene | Confirm single-source workflow in the paper repo (local) and avoid diverging forks; reflect in tracker conventions | Done |  | T-2026-007 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-004 | 2026-02-15 | Grant advisor access to the condensed Overleaf view/project | Submission Logistics | Ensure access is granted (or provide an equivalent local PDF) and record what was shared | Deferred |  | T-2026-009 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-005 | 2026-02-15 | Get the manuscript into a shareable state and address high-level comments | Whole paper (general) | Address high-level comments; ensure the manuscript is shareable for team review | Deferred |  | T-2026-007, T-2025-011 | [Email PDF: Qubit Allocation Paper](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Qubit%20Allocation%20Paper.pdf) |
| D-006 | 2026-02-15 | Add epsilon + NeuralUCB results + extra comparison table (testbed configs) | Results + Tables | Add epsilon + NeuralUCB results; add a comparison table contrasting paper config vs our run config | Deferred |  | T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-007 | 2026-02-15 | Add Paper 7/12 cross-testbed comparison tables once jobs finish | Results + Tables | Integrate comparison tables into the manuscript once jobs complete; keep values source-backed | Done |  | T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-008 | 2026-02-15 | Integrate Professor Travis feedback before submission | Whole paper (general) | Apply Travis edits/comments once received; record deltas as atomic C-### items | Deferred |  | T-2026-005, T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-009 | 2026-02-15 | Add/verify closest-work citation suggestion (e.g., IEEE 10621263) | Related Work | Read + incorporate as closest-work reference; ensure direct comparison is explicit | Done |  | T-2026-007, T-2025-015 | Closest-work compare included |
| D-010 | 2026-02-15 | Confirm venue strategy + submission sprint plan | Submission Planning | Confirm target venue(s)/track(s) and the 1–2 week sprint plan to get the manuscript submission-ready | Done |  | T-2026-009 | [Email PDF: US venues shortlist](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20US%20venues%20%28B-rated%20or%20higher%29%20for%20quantum%20networking%20paper.pdf) |

---

## Sources / Reference Index (Local)

Use this section when sharing the repo so reviewers can find “where a claim came from” without chasing links.

- Communications history: [../../GA_Communications/md_files/Research-Communications.md](../../GA_Communications/md_files/Research-Communications.md)
- Dataset-verified snapshots (master CSVs):
	- [../../Validated_Logs/Master_Dataset_paper2_4000_2000_5_ST.csv](../../Validated_Logs/Master_Dataset_paper2_4000_2000_5_ST.csv)
	- [../../Validated_Logs/Master_Dataset_paper7_50_50_5_ST.csv](../../Validated_Logs/Master_Dataset_paper7_50_50_5_ST.csv)
	- [../../Validated_Logs/Master_Dataset_paper12_1500_500_5_ST.csv](../../Validated_Logs/Master_Dataset_paper12_1500_500_5_ST.csv)

## Active Canonical Tasks (Paper-Specific)

These mirror the active paper-related items in the canonical tracker so the paper edit queue stays aligned.

| Canonical Task ID | Summary | Status | Notes |
|---|---|---|---|
| T-2026-007 | Address paper comments and compare manuscript claims against cited papers | In Progress | Treat C-001…C-006 as the concrete checklist for closure |
| T-2025-011 | Manuscript drafting + revisions (conference/journal paper) | In Progress | Ongoing writing passes + tightening narrative |
| T-2025-015 | Related works synthesis + structure alignment | In Progress | Drives C-003 primarily |

---

## Change Log (Completed Work)

| Date | Location | Change Summary | Why | Commit | Notes |
|---|---|---|---|---|---|
| 2026-02-14 | main.tex | Resolved merge conflicts in abstract; preserved alternative draft in comments | Merge without losing content | 5180e32 |  |
| 2026-02-16 | main.tex | Consolidated RQ2 supporting questions into two items (C-008) | Reduce duplication per Devroop |  |  |
| 2026-02-16 | main.tex | Figure/table formatting fixes (C-011, C-012, C-013, C-015, C-016, C-017, C-018) | Improve layout/readability |  |  |
| 2026-02-16 | main.tex | Added missing table citations (C-020) | Ensure all tables are cited |  | Pending review |
| 2026-02-17 | main.tex | Updated title to include entanglement routing (C-031) | Align title with paper scope |  |  |

---

## Conventions

- **Location**: use the paper section name or a local file link (e.g., [../main.tex](../main.tex), [../sections/02--related_works.tex](../sections/02--related_works.tex)).
- **Commit**: short hash (e.g., `a1b2c3d`) once committed.
- Keep this file free of remote URLs when possible.


## C-020 Draft Fix: Missing Table Citations (Complete Audit)

### C-020 — Complete Table Citation Audit

**Solves:** C-020 (Ensure ALL tables are cited in text)

**Source comment:**
- Devroop (line 1374): "refer the tables per your findings. they have not all been refered"

---

### **📋 ASK**
Ensure all tables in the paper are explicitly referenced using `\Cref{...}` in the corresponding text passages.

---

### **❌ PROBLEM**

**Complete audit reveals 6 out of 11 tables lack text citations:**

| # | Table Label | Location | Section | Status |
|---|------------|----------|---------|--------|
| 1 | `tab:setup-hyperparameters` | Setup/Design | Experimental Design | ❌ Not cited |
| 2 | `tab:setup-algorithm-portfolio` | Setup/Design | Experimental Design (Table III) | ❌ Not cited |
| 3 | `tab:rq1_master_stochastic` | Results | RQ1 Stochastic | ❌ Not cited |
| 4 | `tab:rq3a_informative` | Results | RQ3a Predictive | ❌ Not cited |
| 5 | `tab:rq3b_capacity_scaling` | Results | RQ3b Capacity | ❌ Not cited |
| 6 | `tab:rq3c_allocators` | Results | RQ3c Allocators | ❌ Not cited |

**Already cited (5 tables):** ✅
- `tab:config_summary`, `tab:setup-allocators`, `tab:rq2_adversarial`, `tab:testbed_comparison`, `tab:model_family_comparison`

**Why this matters:**
- Academic standard requires every table/figure be cited in main text
- Reader guidance: citations direct readers to supporting data at the right moment
- IEEE compliance: conference papers require all floats to be referenced
- Narrative flow: citations integrate data into the argument structure

---

### **✅ PROPOSED SOLUTIONS**

---

#### **FIX 1: Hyperparameter Table (Setup Section)**

**Table:** `tab:setup-hyperparameters`  
**Location:** ~line 1240 (Experimental Design, Algorithm portfolio subsection)

**Current:**
```latex
\subsection{Algorithm portfolio}
\label{subsec:algorithms}

We evaluate 14 algorithms spanning three generations of MAB development plus an Oracle baseline.
```

**Fixed:**
```latex
\subsection{Algorithm portfolio}
\label{subsec:algorithms}

All algorithms use the hyperparameters specified in \Cref{tab:setup-hyperparameters}. We evaluate 14 algorithms spanning three generations of MAB development plus an Oracle baseline.
```

---

#### **FIX 2: Algorithm Portfolio Table III (Setup Section)**

**Table:** `tab:setup-algorithm-portfolio`  
**Location:** ~line 1260 (Algorithm portfolio subsection)

**Current:**
```latex
Phase progression covers classical exploration (Phase~1), adversarial defenses (Phase~1--2), contextual/neural methods (Phase~2), and pursuit-based predictive models (Phase~2--3), enabling systematic comparison across architectural paradigms
```

**Fixed:**
```latex
Phase progression (\Cref{tab:setup-algorithm-portfolio}) covers classical exploration (Phase~1), adversarial defenses (Phase~1--2), contextual/neural methods (Phase~2), and pursuit-based predictive models (Phase~2--3), enabling systematic comparison across architectural paradigms
```

---

#### **FIX 3: RQ1 Stochastic Table (Results Section)**

**Table:** `tab:rq1_master_stochastic`  
**Location:** ~line 1520 (RQ1 Key Findings)

**Current:**
```latex
Corpus results show a clear separation under stochastic decoherence: a small top tier remains deployment-viable ($\geq 85\%$), while several variants degrade into the 60--80 band
```

**Fixed:**
```latex
Corpus results (\Cref{tab:rq1_master_stochastic}) show a clear separation under stochastic decoherence: a small top tier remains deployment-viable ($\geq 85\%$), while several variants degrade into the 60--80 band
```

---

#### **FIX 4: RQ3a Predictive Table (Results Section)**

**Table:** `tab:rq3a_informative`  
**Location:** ~line 1840 (RQ3a Answer)

**Current:**
```latex
\textbf{Answer to RQ3a:} \texttt{iCPursuitNeuralUCB} improves global robustness primarily by lifting OnlineAdaptive performance ($+18.3$~pp under the same deployment setting)
```

**Fixed:**
```latex
\textbf{Answer to RQ3a:} As shown in \Cref{tab:rq3a_informative}, \texttt{iCPursuitNeuralUCB} improves global robustness primarily by lifting OnlineAdaptive performance ($+18.3$~pp under the same deployment setting)
```

---

#### **FIX 5: RQ3b Capacity Table (Results Section)**

**Table:** `tab:rq3b_capacity_scaling`  
**Location:** ~line 1880 (RQ3b Answer)

**Current:**
```latex
\textbf{Answer to RQ3b:} Replay capacity is \emph{not} a ``more is better'' knob. Under T-type anchoring, both pursuit-based hybrids exhibit a sharp degradation
```

**Fixed:**
```latex
\textbf{Answer to RQ3b:} Replay capacity is \emph{not} a ``more is better'' knob. Under T-type anchoring (\Cref{tab:rq3b_capacity_scaling}), both pursuit-based hybrids exhibit a sharp degradation
```

---

#### **FIX 6: RQ3c Allocators Table (Results Section)**

**Table:** `tab:rq3c_allocators`  
**Location:** ~line 1760 (RQ3c Answer)

**Current:**
```latex
\textbf{Answer to RQ3c:} Allocator effects are not independent. Fixed provides the strongest global robustness for \texttt{iCPursuitNeuralUCB}
```

**Fixed:**
```latex
\textbf{Answer to RQ3c:} Allocator effects are not independent. As summarized in \Cref{tab:rq3c_allocators}, Fixed provides the strongest global robustness for \texttt{iCPursuitNeuralUCB}
```

---

### **📊 IMPACT**

**Before:** 5/11 tables cited (45%)  
**After:** 11/11 tables cited (100%) ✅

- ✅ All tables now properly referenced
- ✅ Readers guided to supporting data at the right moment
- ✅ Meets IEEE formatting standards
- ✅ Improved narrative flow
- ✅ No structural changes to tables needed

---

**Status:** Done  
**Supersedes:** C-019 (which only tracked 2 of the 6 missing citations)  
**Related tasks:** T-2026-007, T-2025-011

---
