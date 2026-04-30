# PAPER-CHANGES-TRACKER-2 — Comprehensive Analysis
**Project:** QuantumFaultTolerant  
**Scope:** Comprehensive analysis of Dan's comments/tasks in TRACKER-2, gap identification vs current `main.tex` state, and proposed additional changes aligned with Dan's editorial philosophy.  
**Analysis Date:** 2026-03-23  
**Analyst:** Piter Garcia (via Computer)  
**Sources:** `PAPER-CHANGES-TRACKER-2.md`, `PAPER-CHANGES-TRACKER.md`, `main.tex`, `02--related_works.tex`, web/scholar search  

---

## How To Read This Document

- **Section 1** evaluates each existing task in TRACKER-2 (C-001 through C-006 + D-001 through D-010 + P-001 through P-005) against the current `main.tex`/`02--related_works.tex` state.
- **Section 2** identifies new tasks missing from TRACKER-2 that are either (a) directly visible in `main.tex` as unresolved issues, or (b) closely aligned with Dan's documented editorial preferences.
- **Section 3** provides improved/expanded draft text for selected P-### proposals that are still in TRACKER-2 as "Planned" but need strengthening.
- **Section 4** gives a consolidated updated queue ready to merge back into TRACKER-2.

**Status values (used in Section 4):** `Done` | `Planned` | `Needs Update` | `New — Add`

---

## Section 1: Evaluation of Existing TRACKER-2 Tasks

### C-001 — Abstract: Clarify evaluation vs. new contribution
**TRACKER-2 status:** Planned  
**Actual state in `main.tex`:** ⚠️ **Partially resolved, but a critical placeholder remains.**

The abstract contains the line:
```
The primary contribvution of this paper is: XYZ
```
This placeholder is still in the compiled manuscript. The four-paragraph structure that was approved as the "canonical" abstract (from TRACKER-1, C-032) is present in the body, but this dead placeholder line **survives between paragraphs 1 and 2** and will appear in the compiled PDF. Additionally, "contribvution" has a typo.

**What TRACKER-2 says:** "Add explicit novelty framing (benchmark + taxonomy + capacity paradox + deployment rules)"  
**What is actually needed now:** Remove the placeholder `The primary contribvution of this paper is: XYZ` line (it contradicts the novelty framing that already exists in paragraph 2), fix the typo, and confirm the four-paragraph abstract is the single active version with no stale inline comments.

**Recommendation:** Upgrade the fix description. The novelty framing has been addressed; the lingering risk is the visible placeholder in the compiled PDF.

---

### C-002 — Introduction: Cleanup TODOs and improve narrative flow
**TRACKER-2 status:** Planned  
**Actual state in `main.tex`:** ✅ Substantially done (marked Done in TRACKER-1 as C-002, C-022, C-035, C-036, C-044, C-045).

The intro has been extensively revised since TRACKER-2 was created:
- The "Gap in Prior Work" subsection heading was removed (C-035).
- Corpus accounting moved to Study Design (C-036).
- Dan's "uniqueness" paragraph has been inserted (C-002 TRACKER-1).
- The narrative flow is: problem → gap → approach → contributions → uniqueness bridge.
- Commented TODO blocks were cleaned (C-022).

**Remaining gap:** The TRACKER-2 description is too vague ("cleanup TODOs and improve narrative flow") and does not record what was actually done. It should be updated to `Done` in TRACKER-2 with a cross-reference to the C-022/C-035/C-036/C-044/C-045 chain in TRACKER-1. No new action needed.

---

### C-003 — Related Work: Direct paper-to-paper comparisons
**TRACKER-2 status:** Planned  
**Actual state in `02--related_works.tex`:** ✅ Substantially done (all P-001 through P-004 applied in `02--related_works.tex`).

The related works file now contains:
- Explicit Huang et al. EXPNeuralUCB attribution with contrast (P-001) ✓
- LinkSelFiE dedicated contrast paragraph (P-002) ✓
- Adjacent routing families grouped comparison — learning, RL, hierarchical, cost-vector (P-003) ✓
- Wang et al. adaptive user-centric routing comparison (P-004) ✓
- Explicit "In our study/benchmark…" contrast sentences added in all non-quantum subsections (C-056 TRACKER-1) ✓

**Remaining gap (new issue flagged in TRACKER-1 as C-054/C-055):** The Literature Selection Methodology subsection was rewritten from list form to paragraph form (C-054), and micro-subsubsections were collapsed (C-055). TRACKER-2 still shows the original narrowly-scoped fix. Update to Done.

---

### C-004 — Results Section: Organize by RQs / improve continuity
**TRACKER-2 status:** Planned  
**Actual state in `main.tex`:** ⚠️ **Partially done.** 

The duplicated Results intro roadmap paragraph was removed and replaced with a single RQ1/RQ2/RQ3 transition sentence (C-029 TRACKER-1). The RQ-driven structure is in place. However, within the Results narrative, the "RQ claim → evidence → takeaway" scaffolding that C-004 proposes has **not been formally added** — each subsection opens directly with data/figures without a one-sentence claim setup. This is consistent with how Dan's R-04 comment from March 13 asked to "state the primary contribution early."

**Recommendation:** Keep C-004 as active but tighten its scope: the macro RQ scaffold is done; what remains is a per-subsection "one-sentence claim opener" for RQ1, RQ2, and RQ3 answer sections (before diving into numbers). This is a moderate writing task.

---

### C-005 — Limitations/Future Work: Resolve duplication
**TRACKER-2 status:** Planned  
**Actual state in `main.tex`:** ✅ Done (TRACKER-1 C-005/C-028). The duplicated commented Limitations/Future Work block was removed. A single clean section remains (confirmed by reading `main.tex` lines 2300–2400).

Update to Done.

---

### C-006 — Submission Hygiene: Anonymity decision
**TRACKER-2 status:** Planned  
**Actual state:** Deferred/pending Dan's decision (parked in Parking Lot in TRACKER-1). The manuscript has `[Hidden]` placeholders in the Acknowledgments section, indicating a decision was made to keep it masked. No new action needed until Dan specifies the venue.

---

### D-001 — Abstract + Intro: 2–3 sentence process overview
**TRACKER-2 status:** Planned  
**Actual state:** ✅ Substantially done. The abstract's paragraph 2 ("In this paper, we present a systematic threat-aware evaluation…") provides the process overview. The Introduction's "Our Approach and Evaluation Scope" subsection gives the expanded process description. However, the active **abstract placeholder** (see C-001 above) still sits inside the abstract and must be removed before the process description reads correctly.

---

### D-002 — Related Work: Short contrast vs closest MAB routing work(s)
**TRACKER-2 status:** Planned  
**Actual state:** ✅ Done (see C-003 above; P-001/P-002/P-004 provide explicit contrasts against Huang, LinkSelFiE, and Wang et al.).

---

### D-003 — Keep single source of truth manuscript version
**TRACKER-2 status:** Done ✓  
No action needed.

---

### D-004 — Grant advisor access to Overleaf view
**TRACKER-2 status:** Planned  
**Actual state:** Deferred/logistics — parked in TRACKER-1. Not a manuscript issue.

---

### D-005 — Get manuscript into shareable state
**TRACKER-2 status:** Planned  
**Actual state:** Substantially done (TRACKER-1 marks most reviewer items as Done). Still blocked by: abstract placeholder (C-001) and the active R-01 through R-13 queue in TRACKER-1.

---

### D-006 — Add epsilon + NeuralUCB results + extra comparison table
**TRACKER-2 status:** Planned  
**Actual state:** Parked as Technical/Engineering in TRACKER-1 (T-001/T-002). Requires new runs; not a manuscript writing task.

---

### D-007 — Add Paper 7/12 cross-testbed comparison tables once jobs finish
**TRACKER-2 status:** Planned  
**Actual state:** Table is present in `main.tex` at `\label{tab:testbed_comparison}` with complete data for Papers 2, 7, 8, and 12 (added Paper 8 since TRACKER-2 was written). ✅ Done for the current corpus; the "standardized run protocol" follow-up (T-001/T-002) is ongoing.

---

### D-008 — Integrate Professor Travis feedback
**TRACKER-2 status:** Planned  
**Actual state:** Parked in TRACKER-1 (Deferred). No Travis feedback received yet.

---

### D-009 — Add/verify closest-work citation (IEEE 10621263)
**TRACKER-2 status:** Planned  
**Actual state:** ✅ Done (P-002 applied; LinkSelFiE is now cited and contrasted in `02--related_works.tex`). The original `TODO: Be sure to compare against \cite{10621263}` in `main.tex` was removed.

---

### D-010 — Confirm venue strategy + submission sprint plan
**TRACKER-2 status:** Planned  
**Actual state:** External logistics/decision item; not a manuscript task.

---

### P-001 through P-005 — Proposed Edits
| Proposal | Status in TRACKER-2 | Actual State |
|---|---|---|
| P-001 (Huang et al. attribution) | "Applied pending review/commit" | ✅ Applied in `02--related_works.tex` |
| P-002 (LinkSelFiE contrast paragraph) | "Applied pending review/commit" | ✅ Applied in `02--related_works.tex` |
| P-003 (Grouped comparisons — RL/heuristic/scalability) | "Applied pending review/commit" | ✅ Applied in `02--related_works.tex` |
| P-004 (Wang et al. adaptive routing) | "Applied pending review/commit" | ✅ Applied in `02--related_works.tex` |
| P-005 (Citation key fix — paper2/7/12 references) | "Applied pending review/commit" | ✅ Applied in `main.tex` |

All P-### items can be marked as **Done** in TRACKER-2. Their "pending review/commit" note should be updated to reference the resolved state.

---

## Section 2: Missing Tasks — Not in TRACKER-2 but Needed

The following items are present in the current `main.tex` state as active issues, or follow directly from Dan's documented editorial preferences. They are absent from TRACKER-2.

### NEW-01 — Abstract: Remove placeholder line and fix typo
**Source:** Visible in `main.tex` lines ~183–188  
**Dan's concern (root):** C-001 / C-032 — abstract should be clean, no placeholders, no inline comments  
**Issue:** The line `The primary contribvution of this paper is: XYZ` still exists in the abstract between paragraph 1 and paragraph 2 of the approved abstract. Additionally:
- "contribvution" is a typo.
- The line immediately contradicts the approved abstract which already states the contribution in paragraph 2.
- Also present: a joke comment `% This work found I) That Dan is the coolest guy in the world by 20%...` which should be removed before any reviewer sees the compiled PDF.

**Fix:**
```latex
% BEFORE (lines ~183–188):
The primary contribvution of this paper is: XYZ

In this paper, we present...

% AFTER: Delete the placeholder line entirely. Paragraph 2 already starts with "In this paper, we present..."
```
Also remove the `% This work found I) That Dan is the coolest guy...` comment line (~line 188).

**Priority:** Critical / High — this compiles into the PDF and looks unprofessional.

---

### NEW-02 — Devroop: Relay RQ questions, answer in Results (RQ section restructure decision)
**Source:** `main.tex` line 654  
**Visible comment:** `\devroop{Wont it make more sense to just relay the questions here and answer them in the results and discussion section?}`  
**Dan's concern (root):** Dan noted (C-051, C-052, C-053 in TRACKER-1) that RQs should be simplified and standalone-readable; this Devroop comment is a structural echo of the same concern — should the RQ section only pose questions, with answers deferred to Results?  
**Issue:** Currently the RQ section includes both questions and answers (figures + data). Devroop is asking whether this belongs in Results instead.

**Analysis:** This directly intersects TRACKER-1 item C-024 (Blocked: "Move detailed answers to Results; keep questions in RQ section — Needs Dan approval"). The Devroop comment makes the same ask from a different angle.

**Fix options:**
- **Option A (minimal, recommended):** Keep the current structure but add a one-line forward pointer after each RQ statement (e.g., "We answer this question in §VI-A"). Remove the inline figures from the RQ subsection and move them to the corresponding Results subsection. This satisfies both Devroop and Dan without restructuring the paper.
- **Option B (structural, needs Dan approval):** Move the figures/data blocks out of the RQ section entirely. Keep only the question text + 1-sentence hypothesis in §Study Design. This is what C-024 proposes but has been blocked pending Dan's approval.

**Recommendation:** Add to TRACKER-2 as a Blocked item pending Dan's decision (mirrors C-024 in TRACKER-1). Flag it as the same unresolved issue seen by both Devroop and Dan.

---

### NEW-03 — Devroop: Add one more testbed paper to Table VI / cross-testbed
**Source:** `main.tex` line ~2001  
**Visible comment:** `% \devroop{Maybe have one more paper if you can.}` (commented in the caption for `tab:testbed_comparison`)  
**Dan's concern (root):** Cross-testbed validation is a key contribution; more testbeds strengthen generalizability claims  
**Issue:** The current table has 4 testbeds (Papers 2, 7, 8, 12). Devroop wants a 5th.

**Candidate 5th testbed papers** (from `refs.bib` and recent literature):
1. **`akter2025routing`** (Akter et al., 2025, arXiv:2503.03763) — "Routing Dynamics in Distributed Quantum Networks" — simulates 10/20/50/100 node networks. This is a 2025 paper that evaluates routing mechanisms across multiple topologies, directly relevant and already in the literature we searched.
2. **Islam et al. (arXiv:2505.08958, 2025)** — "Adaptive Entanglement Generation" — already noted in `references/pdfs/from_main_tex/`.
3. **Minerva** (OpenReview svsmKvkzFk, 2024) — also in `references/pdfs/from_main_tex/`.

**Fix:** This is a Testing/Validation task (requires new runs on a 5th testbed). Add to TRACKER-2 as:
- **Manuscript task (now):** Note candidate papers. Add a sentence in the cross-testbed section noting "Extension to a 5th testbed is planned in follow-up work" (if runs are not yet ready). Remove or resolve the `% \devroop{...}` comment.
- **Testing task (later):** Run on one additional testbed; integrate results.

---

### NEW-04 — TODO (CRITICAL): Data fix pending for RQ3b at 6K Default
**Source:** `main.tex` line ~1806  
**Visible in compiled PDF:** `\todo{CRITICAL / HIGH PRIORITY (DATA FIX PENDING): For $T$-anchored RQ3b at 6K under Default (=Fixed), the validated master is missing the full $s{=}1.5$ grid...}`  
**Dan's concern (root):** Dan's editorial principle is that all reported numbers must be source-backed. A `\todo{CRITICAL}` marker compiling into the PDF is a major readability/credibility issue.  
**Issue:** The `\todo{}` macro renders as bright cyan text in the compiled PDF. This is currently visible to anyone who reads the PDF. It references a data validation problem with the RQ3b 6K dataset.

**Fix (two parts):**
1. **Immediate (manuscript):** Either (a) comment out or remove the `\todo{}` tag and add a code comment `% DATA FIX PENDING: [explanation]` instead, so the issue is tracked in source but does not appear in the PDF, or (b) resolve the data issue and update the reported values.
2. **Data fix (framework):** Repair the missing $s=1.5$ grid in the 6K master dataset for RQ3b (T-anchored, Default allocator). Until repaired, the manuscript should continue to report RQ3b under $T_b$-anchoring as stated.

**Priority:** High — the `\todo{}` currently compiles into the PDF.

---

### NEW-05 — R-01: Related Work — be more explicit about how existing works differ
**Source:** TRACKER-1 Active Review Queue, R-01 (Dan, March 11, 8:21 am)  
**Location:** Related Work  
**Issue:** Despite the extensive P-001 through P-004 additions, Dan's March 11 comment suggests the "how existing works differ from ours" framing is still not explicit enough in the Related Work section. This goes beyond the TRACKER-2 C-003 fix.

**Analysis of current state:** The current `02--related_works.tex` ends each subsection with a contrast sentence ("In our study…"). However, the quantum routing subsection has multiple contrast blocks spread non-linearly (Wang/Li/Liu block → Wang adaptive → Huang block → LinkSelFiE paragraph → grouped comparisons). A reader scanning the section may not easily find the "how our work differs" synthesis.

**Fix:** Add a short "Positioning Summary" paragraph or a 2-sentence synthesis at the end of the "Quantum Network Routing with Bandits" subsection that explicitly names the 3–4 closest papers and states the key differentiator in one clause each. Example:
```latex
\smallTitle{Positioning summary.}
Relative to the closest related works: Huang et al.~\cite{huang2024quantum} introduce a new adversarial bandit variant; we benchmark decision-rule families.
LinkSelFiE~\cite{10621263} solves link-level selection; we target routing-level path+allocation decisions.
Wang et al.~\cite{wang2024adaptive} propose a new budgeted-control routing algorithm; we evaluate robustness across algorithm--allocator--capacity configurations.
Chaudhary et al.~\cite{chaudhary2023quantum} evaluate learning under stochastic noise only; we extend to five threat regimes including adaptive adversaries.
```

---

### NEW-06 — R-02: Intro — replace awkward `situate` wording
**Source:** TRACKER-1 Active Review Queue, R-02 (Dan, March 13, 10:29 am)  
**Location:** Introduction sentence  
**Issue:** A sentence in Related Work's methodology paragraph uses "situate" (likely "We situate multi-armed bandits..."). Dan flagged this as awkward.

**Current text in `02--related_works.tex`:**
```
We situate multi-armed bandits (MABs) as a family of uncertainty-aware sequential decision rules...
```

**Fix:**
```latex
% BEFORE:
We situate multi-armed bandits (MABs) as a family of uncertainty-aware sequential decision rules...

% AFTER (options):
We frame multi-armed bandits (MABs) as a family of uncertainty-aware sequential decision rules...
% OR:
We treat multi-armed bandits (MABs) as a family of uncertainty-aware sequential decision rules...
```
"Frame" or "treat" are natural, academic-English substitutes that read less awkwardly than "situate."

---

### NEW-07 — R-03: Abstract — add 1–2 sentences on why the problem matters
**Source:** TRACKER-1 Active Review Queue, R-03 (Dan, March 11, 7:30 am)  
**Location:** Abstract  
**Issue:** Dan wants the abstract to open by motivating why quantum entanglement routing under adversarial threats matters — not just describing what the paper does. Currently paragraph 1 describes what existing approaches assume and why they fail, but does not explicitly state the practical consequence (e.g., "this matters because quantum networks are expected to be used for X and must be resilient").

**Fix (add after the first sentence of the abstract):**
```latex
% Current paragraph 1 opens:
Quantum entanglement routing requires dynamic path selection and qubit allocation under noisy and adversarial conditions. Existing routing approaches often assume stationary link behavior...

% Improved paragraph 1:
Quantum entanglement routing is the foundational mechanism enabling quantum key distribution, distributed quantum computing, and quantum sensing across multi-node networks~\cite{wehner2018quantum,kimble2008quantum}. As these applications mature toward deployment, routing must remain reliable under adversarial interference and environment-driven noise—conditions that existing approaches often cannot handle because they assume stationary link behavior, decouple selection from allocation, or rely on offline optimization.
```

---

### NEW-08 — R-04: Early intro — state the primary contribution early
**Source:** TRACKER-1 Active Review Queue, R-04 (Dan, March 13, 9:34 am)  
**Location:** Introduction, first paragraph or opening  
**Issue:** The introduction currently opens with three paragraphs of quantum networking background before reaching the gap/contribution. Dan wants the contribution stated early so readers know why they are reading.

**Fix:** Add a one-sentence "contribution statement" immediately after the first paragraph (quantum networking background), before the gap analysis:
```latex
% After the first intro paragraph (ending "...making multi-armed bandits (MABs) a natural abstraction for online path selection..."):

\noindent\textbf{This paper's primary contribution} is a systematic, threat-aware evaluation framework for joint path selection and qubit allocation in quantum networks, revealing that robust deployment requires co-designing the learning policy, allocator strategy, and replay-capacity semantics rather than optimizing them independently.
```

---

### NEW-09 — R-05: Findings sentence — rewrite pursuit–neural result with concrete backing
**Source:** TRACKER-1 Active Review Queue, R-05 (Dan, March 11, 7:33 am)  
**Location:** Abstract or Key Contributions findings sentence  
**Issue:** The abstract says: "Pursuit–neural hybrids emerge as the most robust family, outperforming non-contextual bandit baselines by 18–24 percentage points." Dan wants this claim backed by a concrete, specific reference (what scenario, what scale, what allocator).

**Fix:** Add a parenthetical anchor:
```latex
% BEFORE:
Pursuit–neural hybrids emerge as the most robust family, outperforming non-contextual bandit baselines by 18--24 percentage points and sustaining higher worst-case performance under strategic attacks than adversarial-first designs.

% AFTER:
Pursuit--neural hybrids emerge as the most robust family, outperforming non-contextual bandit baselines by 18--24 percentage points (scenario-aggregated across all five threat regimes, all four allocators, and capacity scales $s \in \{1,1.5,2\}$) and sustaining higher worst-case efficiency floors under strategic attacks than adversarial-first designs.
```

---

### NEW-10 — R-06: Introduction — cut intro length, move detail elsewhere
**Source:** TRACKER-1 Active Review Queue, R-06 (Dan, March 11, 8:21 am)  
**Location:** Introduction  
**Issue:** Dan's March 11 comment (R-06) requests the intro be shortened and detail moved elsewhere. The current intro has five subsections: (1) background paragraph, (2) quantum-vs-classical paragraph, (3) gap + streams paragraph, (4) Our Approach and Evaluation Scope, (5) The Capacity Paradox, (6) Key Contributions. Dan's earlier feedback (C-045 TRACKER-1) already removed the evaluation-grid bullet list. But "The Capacity Paradox" subsection (4 sentences + a full paragraph) is heavy for an intro.

**Fix:** Compress "The Capacity Paradox" subsection from ~4 sentences to a 1–2 sentence forward pointer:
```latex
% BEFORE (current):
\subsection{The Capacity Paradox}
All efficiency metrics are \emph{Oracle-normalized}---i.e., expressed as a percentage of the performance achieved by an ideal agent with perfect knowledge...
[4 dense sentences]

% AFTER:
\smallTitle{The Capacity Paradox.}
A central finding is that increasing replay capacity can improve performance under Markov regimes while inducing significant collapses under Adaptive attacks, revealing that \emph{predictability}---not bandwidth---is the limiting factor in adversarial settings (see \S\ref{subsec:capacity} and \S\ref{sec:SimulationResults}).
```
This moves the detail to the body sections where it belongs and sharpens the intro's job (motivate + claim, not explain).

---

### NEW-11 — R-07: Introduction gap framing — convert bullet-heavy framing to paragraph form
**Source:** TRACKER-1 Active Review Queue, R-07 (Dan, March 11, 8:20 am)  
**Location:** Introduction — the three "deployment-critical matched-threat evaluation gaps" bullet list  
**Issue:** The three gaps are currently an `enumerate` list with bold headers. Dan prefers paragraph form for the intro (consistent with C-035 which removed the subsection heading). This is the same editorial philosophy applied to the remainder of the gap framing.

**Fix:** Convert the enumerate list to a 2–3 sentence paragraph:
```latex
% BEFORE (current enumerate list):
This divide leaves three deployment-critical matched-threat evaluation gaps insufficiently isolated in prior evaluations:
\begin{enumerate}
\item \textbf{Context dependence is under-characterized.}...
\item \textbf{Matched-threat comparisons are missing.}...
\item \textbf{Deployment interactions are not disentangled.}...
\end{enumerate}

% AFTER (paragraph form):
This divide leaves three deployment-critical matched-threat evaluation gaps insufficiently isolated in prior work. First, context dependence is under-characterized: prior work does not clearly identify which threat and noise regimes require topology/channel features versus when non-contextual policies suffice. Second, matched-threat comparisons are missing: adversarial-first and stochastic/contextual-first methods are rarely evaluated under identical threat conditions. Third, deployment interactions are not disentangled: allocator choice and replay/capacity semantics are typically treated as implementation details rather than first-class experimental factors, obscuring counterintuitive performance shifts.
```

---

### NEW-12 — R-08: Key Contributions — keep only 2–4 concise bullets
**Source:** TRACKER-1 Active Review Queue, R-08 (Dan, March 11, 8:27 am)  
**Location:** Introduction → Key Contributions  
**Issue:** The current Key Contributions section has **5 bullets**, each multi-sentence. Dan's standard editorial ask is "keep it concise, 2–4 bullets." The five-bullet version is dense and repetitive with the intro text.

**Fix:** Consolidate to 4 tight bullets:
```latex
\begin{itemize}[leftmargin=2em]
\item \textbf{Unified apples-to-apples benchmarking:} We evaluate adversarial (EXP3-family), contextual (CMAB/iCMAB), and hybrid pursuit--neural bandit policies under a shared five-regime threat taxonomy, enabling direct comparison of robustness--efficiency tradeoffs~\cite{auer2002nonstochastic,huang2024quantum,chu2011contextual,kar2024icmab}.

\item \textbf{Capacity paradox characterization:} Increasing replay capacity yields gains under Markov regimes but can induce large collapses under Adaptive attacks, revealing that \emph{predictability}---not bandwidth---is a primary vulnerability mechanism in adversarial quantum routing.

\item \textbf{Allocator--algorithm co-design and deployment rules:} Allocator choice produces large performance shifts for identical policies; we distill threat-responsive heuristics for choosing model families, allocators, and capacity scales at deployment time.

\item \textbf{Cross-testbed validation:} We validate algorithms on four external quantum network testbeds~\cite{chaudhary2023quantum,liu2024qbgp,clayton2024quarc}, spanning 15--100 nodes, confirming consistent robustness trends while exposing scale- and physics-dependent limitations.
\end{itemize}
```

---

### NEW-13 — R-09: Intro transition — replace `these considerations` with explicit context
**Source:** TRACKER-1 Active Review Queue, R-09 (Dan, March 12, 10:34 am)  
**Location:** Introduction, closing paragraph before Related Work  
**Issue:** The last paragraph of the Introduction opens: "Motivated by these considerations, we study how modeling choices...". Dan flagged "these considerations" as a weak/vague referent — the reader should not have to look backward to understand what "considerations" means.

**Current text:**
```
Beyond the physics-level differences from classical networking, quantum path determination tightly couples routing to resource allocation and control...
```

**Fix:** Replace the implicit referent with an explicit one:
```latex
% BEFORE:
Beyond the physics-level differences from classical networking, quantum path determination tightly couples routing to resource allocation and control...

% AFTER:
Building on the identified gap—the absence of controlled, matched-threat comparisons that isolate algorithm, allocator, and capacity effects—this paper studies quantum path determination as a joint decision problem...
```

---

### NEW-14 — R-10: Research questions — use `\emph{}` rather than bold
**Source:** TRACKER-1 Active Review Queue, R-10 (Dan, March 13, 8:54 am)  
**Location:** Study Design → Research Questions  
**Issue:** The RQ subsubsection headings and supporting questions use `\textbf{}` or `\textit{}`. Dan's typography preference (consistent with IEEE style) is `\emph{}` for emphasis within text.

**Fix:** Replace `\textbf{RQ1}` / `\textbf{RQ2}` etc. heading labels and inline bold emphasis with `\emph{}` where emphasis is needed within prose. Section headers can remain bold (standard IEEE), but inline "key term" emphasis should use `\emph{}`.

---

### NEW-15 — R-11: Figure captions — shorten and state main takeaway
**Source:** TRACKER-1 Active Review Queue, R-11 (Dan, March 13, 9:39 am)  
**Location:** All remaining figures with long captions  
**Issue:** TRACKER-1 applied C-048 through C-060 to many captions. However, R-11 is a fresh March 13 comment, suggesting **additional** captions remain too wordy or lack a clear takeaway opener. This should trigger a fresh audit of all remaining figure captions.

**Action:** Audit every `\caption{...}` in `main.tex` for:
1. Does it start with the primary takeaway (not "This figure shows...")?
2. Does it use `\tiny` or other manual sizing? (Remove if so.)
3. Is it longer than 3 sentences? (Trim if so.)

---

### NEW-16 — R-12: Hypothesis sentence — review whether to keep or remove
**Source:** TRACKER-1 Active Review Queue, R-12 (Dan, March 13, 9:55 am)  
**Location:** Study Design / RQ section — explicit hypothesis sentence  
**Issue:** There is a hypothesis sentence somewhere in the Study Design section (likely in the RQ preamble or immediately before RQ1). Dan is questioning whether explicitly stating a hypothesis is appropriate for an evaluation paper.

**Analysis:** IEEE conference/journal papers rarely state explicit hypotheses — they state research questions. If the paper is framed as "evaluation" (which is its primary contribution), a formal hypothesis statement may look out of place and suggest over-claiming. 

**Fix options:**
- **Option A (recommended):** Remove the explicit hypothesis sentence; the RQs themselves carry the predictive framing.
- **Option B:** Convert the hypothesis to a "motivation" framing ("We expect that...") placed only in the paragraph introducing the capacity paradox.

---

### NEW-17 — R-13: Table VI caption — shorten and foreground the implication
**Source:** TRACKER-1 Active Review Queue, R-13 (Dan, March 13, 9:56 am)  
**Location:** `main.tex`, `\label{tab:rq2_adversarial}` (RQ2 adversarial results table)  
**Issue:** The caption for Table VI is too long and buries the key implication. Dan wants it to lead with what the table tells the reader.

**Current caption structure (likely):** Configuration description → methodological note → values.  
**Fix:** Rewrite to lead with the takeaway:
```latex
% Proposed structure:
\caption{RQ2 adversarial robustness: Pursuit--neural hybrids dominate win share under Adaptive and OnlineAdaptive threats (Win Dominance: \texttt{iCPursuitNeuralUCB} 43.9\%, \texttt{CPursuitNeuralUCB} 30.5\%). EXP3-based variants earn no wins (0.0\%) under matched-threat evaluation despite their adversarial-first design. All values are Oracle-normalized efficiency (\%) and win dominance (\%) aggregated across [scope].}
```

---

## Section 3: Improved Draft Text for Still-Active TRACKER-2 Proposals

### Strengthened P-002 (LinkSelFiE contrast)
The existing P-002 draft is solid but can be tightened for the IEEE style guide (avoid the `\paragraph{}` heading; embed into the subsection flow):

```latex
% IMPROVED P-002 (replaces standalone paragraph heading with inline citation block):
Liu et al.~\cite{10621263} propose \emph{LinkSelFiE}, which targets the \emph{link-level} problem of selecting a high-fidelity entanglement link and estimating its fidelity when link qualities are unknown \emph{a priori}; they cast this as a best-arm identification task and use a phase-based elimination strategy around a network-benchmarking subroutine to reduce quantum resource consumption while still identifying high-quality links with high confidence. Our study targets the complementary \emph{routing-level} problem: joint path selection and qubit allocation over time under five threat regimes, quantified through a controlled cross-product evaluation across algorithms, allocators, and replay-capacity semantics. The two contributions are architecturally complementary---LinkSelFiE-style estimation outputs can feed the routing reward model as improved link-quality signals---but operate at different abstraction layers.
```

### Strengthened P-003 (Grouped routing comparisons)
The existing P-003 draft is good but does not explicitly state what differentiates our work from the RL line. Add one sentence:

```latex
% IMPROVED concluding sentence for P-003:
...while cost-vector approaches optimize multi-path routing decisions through explicit objective formulations~\cite{leone2021costvector}. In contrast to all of these families, our contribution is an evaluation-first methodology: rather than introducing a new routing algorithm or allocation policy, we systematically isolate how decision-rule families interact with allocation policies, replay semantics, and capacity across a controlled five-regime threat taxonomy, enabling direct attribution of robustness to the \emph{algorithm--allocator--capacity triad}.
```

---

## Section 4: Consolidated Updated Queue for TRACKER-2

This is the recommended update to the TRACKER-2 Current Queue table and proposed additions.

### Updated C-### / D-### Rows

| ID | Updated Status | Action Required | Priority |
|---|---|---|---|
| C-001 | **Needs Update** | Remove abstract placeholder + typo (see NEW-01) | Critical |
| C-002 | **Done** | Cross-reference TRACKER-1 C-022/C-035/C-044/C-045 | None |
| C-003 | **Done** | P-001 through P-004 applied; cross-reference C-054/C-055 | None |
| C-004 | **Partially Done** | Per-subsection claim openers still missing in Results (see NEW-04 for overlap) | Medium |
| C-005 | **Done** | Cross-reference TRACKER-1 C-028 | None |
| C-006 | **Deferred** | Pending Dan's submission decision | None |
| D-001 | **Done** (pending C-001 fix) | Abstract placeholder must be removed | None |
| D-002 | **Done** | P-001/P-004 cover this | None |
| D-003 | **Done** | — | None |
| D-004 | **Deferred** | Logistics | None |
| D-005 | **In Progress** | Blocked by R-01 through R-13 queue | Medium |
| D-006 | **Deferred** | Testing/Validation dependency | None |
| D-007 | **Done** | Table present (4 testbeds); standardized rerun pending | None |
| D-008 | **Deferred** | Pending Travis feedback | None |
| D-009 | **Done** | P-002 applied | None |
| D-010 | **Deferred** | Logistics | None |
| P-001 | **Done** | Applied to `02--related_works.tex` | None |
| P-002 | **Done** | Applied; consider strengthened wording (Section 3) | Optional |
| P-003 | **Done** | Applied; consider strengthened conclusion sentence (Section 3) | Optional |
| P-004 | **Done** | Applied | None |
| P-005 | **Done** | Applied | None |

### New Entries to Add to TRACKER-2

| New ID | Date | Location | Dan's Ask (root) | Planned Fix | Priority |
|---|---|---|---|---|---|
| NEW-01 | 2026-03-23 | Abstract | C-001/C-032 — placeholder still compiles into PDF | Remove `The primary contribvution…: XYZ` line + typo fix + joke comment | **Critical** |
| NEW-02 | 2026-03-23 | RQ Section | Devroop + C-024 — relay questions only; answer in Results | **Blocked — needs Dan decision** | High |
| NEW-03 | 2026-03-23 | Cross-Testbed (Table) | Devroop — add one more testbed | (a) Add "follow-up planned" sentence; (b) resolve `\devroop{}` marker | Medium |
| NEW-04 | 2026-03-23 | Results (RQ3b) | CRITICAL TODO still compiles into PDF | Comment out `\todo{CRITICAL…}` → code comment; fix data or note limitation | **Critical** |
| NEW-05 | 2026-03-23 | Related Work | R-01 — be explicit about how existing works differ | Add positioning summary paragraph at end of Quantum Routing subsection | High |
| NEW-06 | 2026-03-23 | Related Work (opening) | R-02 — replace awkward `situate` | `situate` → `frame` or `treat` | Low |
| NEW-07 | 2026-03-23 | Abstract | R-03 — add why problem matters | Add 1–2 motivation sentences to abstract paragraph 1 | High |
| NEW-08 | 2026-03-23 | Introduction | R-04 — state primary contribution early | Add one-sentence contribution statement after para 1 | High |
| NEW-09 | 2026-03-23 | Abstract / Key Contributions | R-05 — rewrite finding sentence with concrete backing | Add scope parenthetical to pursuit–neural performance claim | Medium |
| NEW-10 | 2026-03-23 | Introduction (Capacity Paradox) | R-06 — cut intro length | Compress Capacity Paradox subsection to 1–2 sentences + forward pointer | High |
| NEW-11 | 2026-03-23 | Introduction (gap list) | R-07 — convert bullet-heavy gap framing to paragraph | Convert 3-item enumerate to prose paragraph | Medium |
| NEW-12 | 2026-03-23 | Key Contributions | R-08 — keep 2–4 concise bullets | Consolidate 5 bullets to 4 (see draft in Section 2) | High |
| NEW-13 | 2026-03-23 | Introduction (closing para) | R-09 — replace `these considerations` | Replace with explicit motivating clause | Low |
| NEW-14 | 2026-03-23 | Study Design / RQs | R-10 — use `\emph{}` not bold | Replace inline bold emphasis in RQ section with `\emph{}` | Low |
| NEW-15 | 2026-03-23 | All figures | R-11 — shorten captions, state main takeaway | Fresh audit of all remaining figure captions | Medium |
| NEW-16 | 2026-03-23 | Study Design | R-12 — review hypothesis sentence | Remove explicit hypothesis or convert to motivation framing | Medium |
| NEW-17 | 2026-03-23 | Table VI (RQ2 adversarial) | R-13 — shorten caption, foreground implication | Rewrite to lead with takeaway (see draft in Section 2) | Medium |

---

## Recommended Work Order (Next Pass)

**Immediate (before any PDF sharing):**
1. NEW-01 — Remove abstract placeholder + typo (5 min fix)
2. NEW-04 — Comment out `\todo{CRITICAL}` in Results

**High priority (Dan's March 11–13 comments):**
3. NEW-07 — Abstract: add why problem matters (R-03)
4. NEW-08 — Intro: state primary contribution early (R-04)
5. NEW-10 — Compress Capacity Paradox in intro (R-06)
6. NEW-12 — Consolidate Key Contributions to 4 bullets (R-08)
7. NEW-05 — Related Work positioning summary (R-01)

**Medium priority:**
8. NEW-11 — Gap framing → paragraph form (R-07)
9. NEW-09 — Concrete backing for finding sentence (R-05)
10. NEW-15 — Figure caption audit (R-11)
11. NEW-16 — Hypothesis sentence decision (R-12)
12. NEW-17 — Table VI caption (R-13)

**Low priority / decision-blocked:**
13. NEW-02 — Devroop/C-024 RQ restructure (needs Dan)
14. NEW-03 — 5th testbed (testing dependency)
15. NEW-06 — "situate" word fix (R-02)
16. NEW-13 — "these considerations" fix (R-09)
17. NEW-14 — `\emph{}` typography (R-10)

---

## Key Observations (Summary for Dan)

1. **TRACKER-2 is out of date** relative to the actual `main.tex` state. Most C-001 through C-006 items and all P-### items have been applied (in TRACKER-1) but TRACKER-2 still shows them as "Planned." The risk is duplicate work or confusion about what is actually done.

2. **Two items compile into the PDF right now** and must be fixed before any review sharing: (a) the abstract placeholder `The primary contribvution of this paper is: XYZ` (NEW-01), and (b) the `\todo{CRITICAL}` in Results (NEW-04).

3. **Dan's March 11–13 comments (R-01 through R-13)** represent the current active backlog and are not yet reflected in TRACKER-2. They are all moderate-scope writing changes — none require new experiments or structural overhaul — and can realistically be addressed in a single 2–3 hour writing session.

4. **The Devroop RQ-restructure comment** (NEW-02) has been deferred correctly as Blocked/pending Dan's decision. The comment touches the same question as the March 11 R-06/R-07 feedback (cut intro, simplify structure), so Dan's ruling on C-024 will likely also address the Devroop comment.

5. **Related Work is strong** but R-01 asks for a positioning summary that makes the "how we differ" message scannable at a glance. The proposed positioning summary paragraph in NEW-05 is the missing piece.
