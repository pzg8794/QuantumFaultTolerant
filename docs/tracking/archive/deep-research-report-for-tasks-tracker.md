# Actionable Response to Dan’s Paper Comments and Tracker Tasks Across QuantumFaultTolerant and quantum_project

## Executive summary

Dan’s core request (“directly compare your work against existing papers, not only existing processes… e.g., \cite{10621263}”) is already substantially implemented in the **Related Work** narrative: the current `sections/02--related_works.tex` explicitly contrasts **Huang et al. (EXPNeuralUCB)** and adds an explicit **LinkSelFiE** “closest-work contrast” paragraph, plus grouped comparisons to adjacent routing families. fileciteturn36file0turn38file0

The main blockers to producing a “shareable / submission-ready” manuscript are **not** Dan’s attribution request anymore; they are (i) an **unfinished Abstract** (“The primary contribvution…XYZ”), (ii) **Introduction length and draft artifacts** (inline reviewer macros, drafting comments), (iii) several **scope/count inconsistencies** (e.g., “13 algorithms” vs “14 algorithms” vs “16 models”), and (iv) **submission hygiene** (anonymous vs non-anonymous toggles, acknowledgments handling). fileciteturn38file0turn45file0

For cross-testbed configuration comparison work (D-006/D-007), the manuscript already contains a substantial **Cross-Testbed Validation** section with multi-testbed tables, but the *tracker’s* status fields have not been updated to reflect that, and the requested “paper config vs our run config” comparison table should be made explicit and sourced from the testbed documentation (which lives in `pzg8794/quantum_project/docs/...`). fileciteturn45file0turn49file0turn55file0turn53file0turn54file0

## Scope, repositories consulted, and evidence trail

### Repositories and primary files used

The work is grounded in two repositories only (per your constraint):

- `pzg8794/QuantumFaultTolerant`
  - Tracker: `docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md` fileciteturn38file0
  - Manuscript: `main.tex` fileciteturn45file0
  - Related work: `sections/02--related_works.tex` fileciteturn36file0turn38file2

- `pzg8794/quantum_project`
  - Testbeds overview (canonical documentation hub): `docs/TESTBEDS_OVERVIEW.md` fileciteturn49file0
  - Testbed quick refs: `docs/testbeds/Paper2_Quick_Reference.md`, `Paper7_Quick_Reference.md`, `Paper12_Quick_Reference.md` fileciteturn55file0turn53file0turn54file0
  - Paper-validation provenance and “source of truth” contract: `docs/guides/MASTER_DATASET_VALIDATION_HUB_PLAN.md` fileciteturn56file0

### Important clarification about “main.tex in quantum_project”

Your instructions ask me to map tracker items to `main.tex` in `pzg8794/quantum_project`, but the **quantum_project documentation explicitly identifies** the paper source-of-truth as **`GA Papers/QuantumFaultTolerant/main.tex`** (i.e., the manuscript is in `QuantumFaultTolerant`, not in `quantum_project`). fileciteturn56file0

Accordingly, this report maps tracker items to edits in **`pzg8794/QuantumFaultTolerant/main.tex`** and **`pzg8794/QuantumFaultTolerant/sections/...`**, while using `quantum_project` to source cross-testbed configuration facts and validation provenance.

### Permalink targets (commit-pinned) to use when you paste into messages/issues

Use these commit-stable GitHub links as your “exact references” starting points (line anchors omitted where not reliably derivable from connector output):

```text
QuantumFaultTolerant tracker (PAPER-CHANGES-TRACKER-2.md):
https://github.com/pzg8794/QuantumFaultTolerant/blob/44e272d191d419952884f944912fa68b076371de/docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md

QuantumFaultTolerant manuscript (main.tex):
https://github.com/pzg8794/QuantumFaultTolerant/blob/44e272d191d419952884f944912fa68b076371de/main.tex

QuantumFaultTolerant related works (02--related_works.tex):
https://github.com/pzg8794/QuantumFaultTolerant/blob/44e272d191d419952884f944912fa68b076371de/sections/02--related_works.tex

quantum_project testbeds overview:
https://github.com/pzg8794/quantum_project/blob/a17772651938219492d83fc1e4a2d4d68a057acf/docs/TESTBEDS_OVERVIEW.md
```

## Itemized mapping and response for each tracker comment/task

### Summary table across all C-* and D-* items

The table below compresses the (1) tracker quote, (2) manuscript mapping, (3) status, (4) proposed fix, (5) effort/priority. Detailed per-item edit snippets follow.

| ID | Tracker comment (quoted) | Manuscript mapping (actual edit surface) | Implemented now? | Proposed change (what to edit) | Effort | Priority |
|---|---|---|---|---|---|---|
| C-001 | “Clarify whether this is ‘evaluation only’ vs. new contribution” fileciteturn38file0 | `main.tex` Abstract + early Intro framing fileciteturn45file0 | **Partially** (method described; novelty not crisp; placeholder remains) fileciteturn45file0 | Rewrite abstract novelty sentence(s); remove “XYZ”; tighten contribution claims | Medium | High |
| C-002 | “Cleanup TODOs and improve narrative flow” fileciteturn38file0 | `main.tex` Introduction (plus draft macros) fileciteturn45file0 | **Partially** (draft artifacts remain) fileciteturn45file0 | Create “draft toggle”; remove inline reviewer macros; shorten intro; reduce bullet density | Medium–High | High |
| C-003 | Dan: “directly comparing your work against existing papers… \cite{10621263}…” fileciteturn38file0 | `sections/02--related_works.tex` “Quantum Network Routing with Bandits” subsection fileciteturn36file0 | **Yes (substantively)** fileciteturn36file0 | Update tracker status to Done; remove any leftover “compare against…” TODOs in `main.tex` if present | Low | High |
| C-004 | “Improve continuity; organize by RQs” fileciteturn38file0 | `main.tex` Results section (RQ1–RQ3 structure) fileciteturn45file0 | **Mostly yes** (already RQ-driven) fileciteturn45file0 | Add 1–2 sentence “RQ claim → evidence → takeaway” at top of each RQ, shorten supporting-question lists | Medium | Medium |
| C-005 | “Resolve duplication notes in commented blocks” fileciteturn38file0 | `main.tex` Limitations/Future Work contains a full commented-out duplicate block fileciteturn45file0 | **No** (duplicate remains commented) fileciteturn45file0 | Delete commented duplicate section; keep one clean canonical version | Low | High |
| C-006 | “Anonymity question + acknowledgments” fileciteturn38file0 | `main.tex` author block + acknowledgments section fileciteturn45file0 | **No** (placeholders remain) fileciteturn45file0 | Add `\ifanonymous` toggle; produce anonymous and non-anonymous builds deterministically | Low | High |
| D-001 | “Add a 2–3 sentence overview of the proposed process (no results)” fileciteturn38file0 | Abstract + “Our Approach and Evaluation Scope” in Intro fileciteturn45file0 | **Partially** (overview exists but abstract contains results and placeholder) fileciteturn45file0 | Insert explicit process paragraph in abstract *before* results; ensure it’s “no results” | Low–Medium | High |
| D-002 | “Provide a short contrast vs closest MAB routing work(s)” fileciteturn38file0 | Related Work + optionally 1 sentence in Intro signposting closest-work contrast fileciteturn36file0turn45file0 | **Yes in Related Work** fileciteturn36file0 | Add a single early-intro sentence pointing to LinkSelFiE/Huang contrast; keep details in Related Work | Low | Medium |
| D-003 | “Keep a single ‘source of truth’ manuscript version” (Status Done) fileciteturn38file0 | Repo/process policy; referenced in quantum_project validation hierarchy fileciteturn56file0 | **Yes (documented)** fileciteturn56file0 | Add a short note in `docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md` under Conventions: “QuantumFaultTolerant is canonical; Overleaf is downstream” | Low | Medium |
| D-004 | “Grant advisor access to condensed Overleaf view/project” fileciteturn38file0 | Not LaTeX; submission logistics | Unknown | Add tracker resolution note: link to Overleaf (or commit hash of shared PDF artifact) | Low | Medium |
| D-005 | “Get the manuscript into a shareable state…” fileciteturn38file0 | Whole manuscript | **No (blocked by C-001/C-002/C-005/C-006)** fileciteturn45file0 | Bundle: abstract rewrite, remove TODO macros, anonymize toggle, delete dup blocks | Medium | High |
| D-006 | “Add epsilon + NeuralUCB results + extra comparison table (testbed configs)” fileciteturn38file0 | RQ tables + Cross-testbed section + new “config table” sourced from `quantum_project/docs/testbeds/*` fileciteturn45file0turn55file0turn53file0turn54file0 | **Partially** (epsilon present; NeuralUCB discussed but not consistently reported; configs described in prose) fileciteturn45file0 | Add explicit Testbed-Config comparison table; add NeuralUCB row(s) or state explicitly if excluded from validated corpora | Medium | High |
| D-007 | “Add Paper 7/12 cross-testbed comparison tables once jobs finish” fileciteturn38file0 | `tab:testbed_comparison`, `tab:model_family_comparison` already include Papers 7 and 12 fileciteturn45file0 | **Yes (in manuscript)** fileciteturn45file0 | Update tracker status to Done and add provenance note pointing to validation hub plan | Low | Medium |
| D-008 | “Integrate Professor Travis feedback before submission” fileciteturn38file0 | Whole paper | Unknown | Convert into atomic C-* tasks once feedback is in repo; add placeholders in tracker for each section impacted | Medium | Medium |
| D-009 | “Add/verify closest-work citation suggestion (e.g., IEEE 10621263)” fileciteturn38file0 | Related Work LinkSelFiE paragraph + bib entry usage fileciteturn36file0turn43file1 | **Yes** fileciteturn36file0turn43file1 | Update tracker status to Done; ensure no residual TODO-only cite remains | Low | High |
| D-010 | “Confirm venue strategy + submission sprint plan” fileciteturn38file0 | Not in LaTeX | Unknown | Add a short submission-plan stanza to tracker (dates, freeze rules, checklist) | Low | Medium |

### C-001 – Abstract novelty framing

**Tracker quote + location.** In `docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md` row **C-001**: “Clarify whether this is ‘evaluation only’ vs. new contribution” with planned fix “Add explicit novelty framing (benchmark + taxonomy + capacity paradox + deployment rules).” fileciteturn38file0

**Manuscript mapping.** `main.tex` → `\begin{abstract} ... \end{abstract}` and the opening of `\section{Introduction}` / “Key Contributions.” fileciteturn45file0

**Current status assessment.**
- The abstract currently includes a draft placeholder line (“The primary contribvution of this paper is: XYZ”) that breaks novelty clarity and will read as unfinished. fileciteturn45file0
- Method elements (threat taxonomy, evaluation grid, allocators, replay capacity semantics) are present, but a *reader-facing* novelty sentence distinguishing “evaluation-only” vs “new evaluative contribution” needs to be explicit. fileciteturn45file0

**Precise edit proposal (diff-style).** Replace the placeholder and insert a 2–3 sentence “process overview (no results)” that also resolves D-001:

```diff
--- a/main.tex
+++ b/main.tex
@@
 \begin{abstract}
 Quantum entanglement routing requires dynamic path selection and qubit allocation under noisy and adversarial conditions. Existing routing approaches often assume stationary link behavior, decouple selection from allocation, or rely on offline optimization---assumptions that can fail when link fidelities drift and disruptions adapt online.
 
-The primary contribvution of this paper is: XYZ
+We contribute a threat-aware, reproducible evaluation methodology for joint path selection and qubit allocation that (i) introduces a unified threat taxonomy spanning stochastic, structured, and adaptive disruption, (ii) factorizes deployment-critical design choices (allocator policy and replay-capacity semantics) as first-class experimental variables, and (iii) distills regime-conditioned deployment rules from the resulting corpus.
 
 In this paper, we present a systematic threat-aware evaluation of bandit algorithms (contextual, adversarial, and hybrid) for joint path selection and qubit allocation in quantum networks, introducing pursuit--neural hybrid variants that balance stochastic efficiency with adversarial robustness. We evaluate 13 algorithms across five threat scenarios while varying allocator policies and replay-capacity semantics.
@@
 \end{abstract}
```

**Why this addresses Dan’s concern / open questions.**
- This makes the “what is new?” answer explicit: **not** claiming a new quantum routing protocol, but claiming a **new evaluation/taxonomy/factorization** contribution that yields deployment rules (exactly what C-001 asks for). fileciteturn38file0turn45file0
- Open question: you must harmonize the algorithm/model counts (“13 algorithms”, “14 algorithms”, “16 models”) to match what is actually in your validated corpora and tables. The validation plan in `quantum_project` is a good “single source of truth” reference for what artifacts are actually backed by master datasets. fileciteturn56file0turn45file0

**Effort and priority.** Effort **Medium** (writing + consistency pass). Priority **High** (blocks shareable manuscript; directly answers reviewer skepticism).

### C-002 – Introduction cleanup and narrative flow

**Tracker quote + location.** Row **C-002**: “Cleanup TODOs and improve narrative flow” with planned fix “Rewrite intro flow: problem → gap → approach → contributions.” fileciteturn38file0

**Manuscript mapping.** `main.tex` → `\section{Introduction}` (and draft macros `\todo`, `\dan`, `\piter`, `\devroop`). fileciteturn45file0

**Current status assessment.**
- The intro already approximates the desired flow (problem → gap bullets → approach → capacity paradox → contributions), but it is **too long and still visibly “in-draft”** due to reviewer-comment macros and at least one inline comment callout. fileciteturn45file0
- Dan’s likely “reader experience” issue: a reviewer should not see internal `\devroop{...}` or a long bullet-heavy gap taxonomy without narrative smoothing. fileciteturn45file0

**Precise edit proposal.** Add a single `draft` toggle and disable comment macros in non-draft builds:

```diff
--- a/main.tex
+++ b/main.tex
@@
-% Author comments (remove for camera-ready)
-\newcommand{\todo}[1]{\textcolor{cyan}{\textbf{[TODO: #1]}}}
-\newcommand{\dan}[1]{\textcolor{blue}{\textit{[Dan: #1]}}}
-\newcommand{\piter}[1]{\textcolor{green}{\textit{[Piter: #1]}}}
-\newcommand{\devroop}[1]{\textcolor{magenta}{\textit{[Devroop: #1]}}}
+% Draft toggle (set to \draftfalse for shareable/camera-ready builds)
+\newif\ifdraft
+\drafttrue
+
+\ifdraft
+  \newcommand{\todo}[1]{\textcolor{cyan}{\textbf{[TODO: #1]}}}
+  \newcommand{\dan}[1]{\textcolor{blue}{\textit{[Dan: #1]}}}
+  \newcommand{\piter}[1]{\textcolor{green}{\textit{[Piter: #1]}}}
+  \newcommand{\devroop}[1]{\textcolor{magenta}{\textit{[Devroop: #1]}}}
+\else
+  \newcommand{\todo}[1]{}
+  \newcommand{\dan}[1]{}
+  \newcommand{\piter}[1]{}
+  \newcommand{\devroop}[1]{}
+\fi
```

Then, in the intro itself, convert the three enumerated “gaps” into paragraph form (to satisfy a likely Dan readability ask) while keeping the taxonomy intact.

**Why this addresses Dan’s concern / open questions.**
- This makes “shareable state” deterministic: one switch (`\draftfalse`) removes internal chatter from the PDF, which directly supports D-005 (shareable) and avoids accidental submission artifacts. fileciteturn45file0turn38file0
- Open question: if Dan’s actual comment set includes “shorten the Introduction,” you should *move some tactical details* (e.g., explicit allocator lists, parameter values) into Study Design and keep the high-level message in the intro.

**Effort and priority.** Effort **Medium–High** (writing + refactoring). Priority **High** (shareable manuscript blocker).

### C-003 – Dan’s “direct paper-to-paper comparisons” request

**Tracker quote + location.** Row **C-003**: Dan: “make sure that you are directly comparing your work against existing papers… \cite{10621263} and others.” Planned fix: “Ensure every process/method… is explicitly attributed to the paper(s)… with clear descriptions… and how it differs.” fileciteturn38file0

**Manuscript mapping.** `sections/02--related_works.tex` → “Quantum Network Routing with Bandits” subsection + explicit LinkSelFiE contrast paragraph. fileciteturn36file0

**Current status assessment (rigorous).**
- **Implemented**: the current related work explicitly attributes **Huang et al.** (EXPNeuralUCB) and explicitly contrasts **LinkSelFiE** at the link level vs your routing-level evaluation. fileciteturn36file0
- The tracker file still says “Planned” for C-003, but the manuscript text already reflects the intended P-001/P-002/P-003 style insertions. This is now a tracker hygiene problem, not a manuscript gap. fileciteturn38file0turn36file0

**Precise edit proposal (tracker-only).**
- Update `docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md`:
  - C-003 Status → **Done**
  - Commit → the commit where the text landed (if you don’t know, use the merge commit that introduced it once you identify it)
  - Notes → “LinkSelFiE contrast paragraph present; Huang explicit attribution present.”

**Why this addresses Dan’s concern / open questions.**
- It demonstrates that the “closest-work compare” is not buried in TODOs; it is explicit and titled.
- Open question: ensure the same closest-work contrast is *easy to find* for skimmers (optional: one short intro sentence pointing to it, see D-002).

**Effort and priority.** Effort **Low** (tracker hygiene). Priority **High** (it is Dan’s explicit ask; should be marked closed).

### C-004 – Results continuity and RQ scaffolding

**Tracker quote + location.** Row **C-004**: “Improve continuity; organize by RQs” → planned fix “Add short ‘RQ claim → evidence → takeaway’ scaffolding per subsection.” fileciteturn38file0

**Manuscript mapping.** `main.tex` → `\section{Simulation Results}` which is already organized by RQ1–RQ3, with hypothesis/experimental design/findings/answer blocks. fileciteturn45file0

**Current status assessment.**
- The RQ structure exists and is visible, so the core “organize by RQs” request is already satisfied. fileciteturn45file0
- However, the continuity can be improved by:
  - shortening “supporting questions” lists,
  - ensuring each RQ opens with a single clear declarative take-away sentence,
  - and making table/figure captions less essay-like (Dan commonly flags caption length; your repo also contains a “caption shortening” ask elsewhere). fileciteturn45file0

**Precise edit proposal.**
- At the top of each RQ subsection, add a one-liner:

```tex
\noindent\textbf{Takeaway:} Context-aware pursuit policies remain above the deployment threshold under stochastic decoherence, whereas several baseline variants collapse even without adversarial targeting.
```

- Replace large itemized supporting questions with a 2–3 sentence narrative and optionally keep the list in draft mode only (`\ifdraft`).

**Effort and priority.** Effort **Medium**. Priority **Medium** (improves readability but not the biggest blocker unless Dan explicitly requested shortening).

### C-005 – Limitations/Future Work duplication cleanup

**Tracker quote + location.** Row **C-005**: “Resolve duplication notes in commented blocks” → planned fix “Remove/retire duplicate commented section after confirming nothing unique.” fileciteturn38file0

**Manuscript mapping.** `main.tex` → `\section{Limitations and Future Work}`, which currently includes a fully commented-out alternate version after the active text. fileciteturn45file0

**Current status assessment.**
- Not done: the commented duplicate is still present and will confuse collaborators and reviewers if a draft PDF includes it accidentally or if someone edits the “wrong” block. fileciteturn45file0

**Precise edit proposal (diff-style).**
- Delete the entire commented duplicate block starting at the commented `\section{Limitations and Future Work}` through its commented subsections (keep only the active one). This is purely hygiene.

**Why this addresses Dan’s concern / open questions.**
- This directly supports D-005 (“shareable state”) by removing internal clutter and eliminating ambiguity about which limitations text is canonical.

**Effort and priority.** Effort **Low**. Priority **High**.

### C-006 – Submission hygiene: anonymity and acknowledgments

**Tracker quote + location.** Row **C-006**: “Anonymity question + acknowledgments” → planned fix “Decide anonymous vs non-anonymous; adjust authors/acks accordingly.” fileciteturn38file0

**Manuscript mapping.** `main.tex` → `\author{...}` block and `\section*{Acknowledgments}`. fileciteturn45file0

**Current status assessment.**
- Not done: author names and `\thanks{...}` are placeholders, acknowledgments are `[Hidden]`. fileciteturn45file0

**Precise edit proposal: deterministic anonymity toggle.**

```diff
--- a/main.tex
+++ b/main.tex
@@
+\newif\ifanonymous
+\anonymoustrue  % set false for non-anonymous builds
@@
-\author{First Author,~Second Author,~and~Third Author%
-\thanks{Affiliations and funding info here.}}
+\ifanonymous
+  \author{Anonymous Authors}
+\else
+  \author{First Author,~Second Author,~and~Third Author%
+  \thanks{Affiliations and funding info here.}}
+\fi
@@
-\section*{Acknowledgments}
-
-This material is based upon work supported by [Hidden] under grants [Hidden].%\#XXXX.
+\section*{Acknowledgments}
+\ifanonymous
+  \textit{Acknowledgments omitted for anonymous review.}
+\else
+  This material is based upon work supported by [Funder] under grants [Grant IDs].
+\fi
```

**Why this addresses Dan’s concern / open questions.**
- It cleanly resolves the “anonymity question” without manual edits right before submission.
- Open question: confirm the target venue’s anonymity policy (D-010) so you set `\anonymoustrue/\false` correctly.

**Effort and priority.** Effort **Low**. Priority **High**.

### D-001 – 2–3 sentence process overview (no results)

**Tracker quote + location.** Row **D-001** requests “Add a 2–3 sentence overview of the proposed process (no results)” in Abstract + Intro. fileciteturn38file0

**Manuscript mapping.** Abstract and “Our Approach and Evaluation Scope.” fileciteturn45file0

**Current status assessment.**
- Partially present (you describe the evaluation and the grid), but it is mixed in with result statements and still includes the placeholder “XYZ,” so it does not read as a clean “process overview.” fileciteturn45file0

**Precise edit proposal.**
- Implemented via the C-001 abstract rewrite above (insert “We contribute … methodology … factorizes allocator and replay semantics …” before any result statements).

**Effort/priority.** **Low–Medium**, **High**.

### D-002 – Short contrast vs closest MAB routing works

**Tracker quote + location.** Row **D-002** requests “Provide a short contrast vs closest MAB routing work(s)” in Related Work. fileciteturn38file0

**Manuscript mapping + status.**
- **Already satisfied** in `sections/02--related_works.tex` via explicit Huang contrast and titled LinkSelFiE paragraph. fileciteturn36file0

**Suggested improvement (optional but helpful).**
- Add one sentence in the Introduction near the “gap framing” to direct readers:

```tex
For the closest quantum-routing neighbors, we provide explicit paper-to-paper contrasts—e.g., Huang et al.’s adversarial group neural bandit formulation and Liu et al.’s LinkSelFiE link-level selection/estimation—highlighting how our contribution is routing-level, threat-taxonomy-driven evaluation (\S\ref{sec:RelatedWork}).
```

**Effort/priority.** **Low**, **Medium**.

### D-003 – Single source of truth (already Done)

**Tracker quote + location.** Row **D-003** is marked Done. fileciteturn38file0

**Cross-repo evidence.**
- `quantum_project`’s validation plan explicitly names the “paper source of truth” as `GA Papers/QuantumFaultTolerant/main.tex` and defines a canonical hierarchy for validation against master datasets. fileciteturn56file0

**Action.**
- Add one sentence to `docs/tracking/archive/PAPER-CHANGES-TRACKER-2.md` “Conventions” clarifying that Overleaf is downstream and this repo is canonical (to resolve future confusion).

**Effort/priority.** **Low**, **Medium**.

### D-004 – Advisor access to Overleaf

**Tracker quote + location.** Row **D-004** asks to grant advisor access to Overleaf or provide equivalent local PDF and record what was shared. fileciteturn38file0

**Mapping.**
- Not a LaTeX edit; this is a logistics deliverable. Your best “artifact” is an exported PDF whose provenance is pinned to a commit hash.

**Suggested tracker resolution comment.**
- Add to tracker Notes: “Shared Overleaf read-only link on YYYY-MM-DD; also exported PDF `paper_exports/<date>_dan_review.pdf` built from commit <hash>.”

**Effort/priority.** **Low**, **Medium**.

### D-005 – Shareable state (bundle task)

**Tracker quote + location.** Row **D-005** is a general “make it shareable” request. fileciteturn38file0

**What truly blocks shareable state right now (from manuscript evidence).**
- Abstract placeholder “XYZ” fileciteturn45file0
- Visible comment macros / TODOs in the compiled PDF unless suppressed fileciteturn45file0
- Duplicate commented limitations block fileciteturn45file0
- Author/ack placeholders and anonymity uncertainty fileciteturn45file0

**Action.** Treat D-005 as “done” only when C-001/C-002/C-005/C-006 are done.

**Effort/priority.** **Medium**, **High**.

### D-006 – Add epsilon + NeuralUCB results and a testbed-config comparison table

**Tracker quote + location.** Row **D-006** requests adding epsilon + NeuralUCB results and “a comparison table contrasting paper config vs our run config.” fileciteturn38file0

**Manuscript mapping.**
- Epsilon-greedy results already appear in RQ1 table (`CEpsilonGreedy`, `iCEpsilonGreedy`). fileciteturn45file0
- NeuralUCB is described in the algorithm portfolio and in uncertainty-handling bullets, but it is **not consistently surfaced in the RQ result tables** (risk: reviewers ask “where are those results?”). fileciteturn45file0
- Cross-testbed configs are currently described in prose bullets in Cross-Testbed Validation; you should add an explicit table. fileciteturn45file0

**Cross-reference to quantum_project for config facts.**
- `docs/TESTBEDS_OVERVIEW.md` gives the integrated testbeds list and high-level parameters. fileciteturn49file0
- `Paper2_Quick_Reference.md`, `Paper7_Quick_Reference.md`, `Paper12_Quick_Reference.md` provide key parameter blocks suitable for a comparison table. fileciteturn55file0turn53file0turn54file0

**Precise edit proposal: add a “Testbed configuration comparison” table** right under `\subsection{External Testbed Configurations}` in `main.tex`.

Skeleton (fill numeric values from your manuscript bullets + quick refs):

```tex
\begin{table*}[ht!]
\centering
\caption{External testbed configuration comparison (paper-native vs. our evaluation-corpus runs). Values are sourced from the integrated testbed documentation and the experiment corpus metadata.}
\label{tab:testbed_config_compare}
\small
\begin{tabular}{lcccccc}
\toprule
\textbf{Testbed} & \textbf{Nodes} & \textbf{Edges} & \textbf{Paths} & \textbf{Runs} & \textbf{Horizon/Step} & \textbf{Key noise/constraints} \\
\midrule
Paper 2 (Chaudhary 2023)  & 15 (or paper std.) & 51 & 8  & 5 & 4K / 2K & $E_p{=}0.7$, $q{=}0.9$ (+ gate/depol params) \\
Paper 7 (Liu 2024 QBGP)   & 50--400 (std. 100) & 141 (example) & 15 & 5 & 50 / 50 & fidelity $\ge0.85$, QoS thresh $0.80$ \\
Paper 12 (Wang 2024 QuARC)& 100 & 426 & 4 & 5 & 1500 / 500 & fusion $0.9$, entanglement $0.6$ (54\%) \\
Paper 8 (RL testbed)      & 20 & 19 & 8 & 1 & 1K / 1K & RL reward modes (paper-config slice) \\
\bottomrule
\end{tabular}
\end{table*}
```

**NeuralUCB integration decision (must be explicit).** Choose one of two defensible states:

- If NeuralUCB is in your validated corpora: add NeuralUCB rows to the relevant RQ table(s) and ensure it appears in the narrative.
- If it is **not** in validated corpora yet: add an explicit sentence in Study Design clarifying what is actually in the curated corpus and what is “planned but not reported.”

Your own validation-hub plan emphasizes: if an artifact is backed by master datasets, compute/verify it there before trusting manuscript values. fileciteturn56file0

**Effort/priority.** **Medium**, **High** (because it prevents “missing results” review feedback and makes D-006 demonstrably complete).

### D-007 – Add Paper 7/12 cross-testbed comparison tables once jobs finish

**Tracker quote + location.** Row **D-007** requests integrating cross-testbed comparison tables once jobs complete. fileciteturn38file0

**Manuscript mapping + current status.**
- The manuscript already contains `tab:testbed_comparison` and `tab:model_family_comparison`, and both include Paper 7 and Paper 12 results. fileciteturn45file0

**Action.**
- Update D-007 status → Done, and in Notes add provenance pointer to the validation hub plan (which lists `tab:testbed_comparison` and source dataset names). fileciteturn56file0turn45file0

**Effort/priority.** **Low**, **Medium**.

### D-008 – Integrate Travis feedback

**Status.** Not possible to verify without the feedback artifact, but you can pre-stage the tracker structure:

- Add placeholder: “Awaiting Travis feedback artifact; will convert into C-### atomic tasks per section” and keep this item Planned until the feedback is present in-repo. fileciteturn38file0

**Effort/priority.** **Medium**, **Medium**.

### D-009 – Closest-work citation (10621263)

**Tracker quote + location.** Row **D-009** requests adding/validating the closest-work citation suggestion (IEEE 10621263). fileciteturn38file0

**Manuscript mapping + status.**
- Implemented: `sections/02--related_works.tex` includes a titled “Closest-work contrast (LinkSelFiE)” paragraph with citation `\cite{10621263}`. fileciteturn36file0
- Bibliography contains the `@INPROCEEDINGS{10621263,...}` entry. fileciteturn43file1

**Action.** Update tracker status to Done; confirm no leftover TODO-only use remains.

**Effort/priority.** **Low**, **High**.

### D-010 – Venue strategy + submission sprint plan

**Status.** Not a LaTeX change; add it as a tracker governance item:

- target venue list
- anonymous policy
- frozen date
- “no new figures” date
- final PDF export procedure tied to commit hash

**Effort/priority.** **Low**, **Medium**.

## Consolidated ordered action list and a practical sprint workflow

### Ordered actions

High-priority, manuscript-facing (shareability blockers):
1) **C-001 + D-001:** Rewrite Abstract: remove “XYZ,” add explicit process overview (no results), and state novelty as evaluation/taxonomy/factorization/deployment rules. fileciteturn45file0turn38file0  
2) **C-006:** Add deterministic anonymity + acknowledgments toggles. fileciteturn45file0turn38file0  
3) **C-005:** Delete the commented-out duplicate limitations block. fileciteturn45file0turn38file0  
4) **C-002:** Add a draft toggle to suppress internal comments and shorten/deflate bullet-heavy intro text for reader flow. fileciteturn45file0turn38file0  

High-priority, Dan-comment closure (tracker hygiene):
5) **C-003 + D-009:** Mark as Done in tracker; ensure LinkSelFiE/Huang contrasts remain present and not TODO-only. fileciteturn36file0turn38file0  

High-priority, “missing-results” risk:
6) **D-006:** Add explicit testbed-config comparison table sourced from `quantum_project/docs/testbeds/*`; decide and document NeuralUCB reporting status. fileciteturn49file0turn55file0turn53file0turn54file0turn45file0  

Medium priority:
7) **C-004:** Tighten RQ continuity and shorten captions and supporting-question lists (especially if Dan’s March feedback includes caption shortening). fileciteturn45file0  
8) **D-007:** Update tracker to Done (tables appear in manuscript; add validation provenance note). fileciteturn45file0turn56file0  

Process/logistics:
9) **D-004:** Log Overleaf access or PDF export tied to commit hash. fileciteturn38file0  
10) **D-010:** Add sprint plan & venue policy confirmation to tracker. fileciteturn38file0  

### Mermaid workflow for a two-pass submission sprint

```mermaid
flowchart TD
  A[Pass 1: Shareable Manuscript\n(C-001,C-002,C-005,C-006)] --> B[Compile + PDF export\n(commit-pinned)]
  B --> C[Dan review delta pass\n(C-003 confirm + caption/intro tightening)]
  C --> D[Pass 2: Results completeness\n(D-006 configs + NeuralUCB status)]
  D --> E[Final hygiene\n(D-004 Overleaf/PDF, D-010 venue policy,\nupdate tracker statuses + commits)]
```

## Proposed updated PAPER-CHANGES-TRACKER-2.md

Below is a proposed update (drop-in replacement style) focusing on **status truthfulness**, adding **resolution notes**, and aligning “done” items with what is already present in the manuscript.

```md
# Paper Changes / Updates Tracker

Project: QuantumFaultTolerant
Owner: Piter Garcia

Quick links:
- main.tex (canonical manuscript): ../main.tex
- Related Work: ../sections/02--related_works.tex

## Current Queue (From Paper Comments)

| ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Notes |
|---|---|---|---|---|---|---|---|
| C-001 | 2026-02-14 | Abstract | Clarify whether this is “evaluation only” vs. new contribution | Rewrite abstract novelty sentence(s): threat taxonomy + allocator/replay factorization + capacity paradox + deployment rules; remove placeholder “XYZ” | In Progress |  | Blocker for shareable PDF |
| C-002 | 2026-02-14 | Introduction | Cleanup TODOs and improve narrative flow | Add draft toggle; remove inline reviewer macros from shareable build; shorten intro + convert bullet-heavy gap framing to narrative | Planned |  | Blocker for D-005 |
| C-003 | 2026-02-14 | Related Work | Dan: “directly compare against existing papers… e.g., \cite{10621263}” | Ensure explicit paper-to-paper contrasts (Huang et al.; LinkSelFiE; grouped neighbors) | Done |  | Implemented in 02--related_works.tex (Huang attribution + LinkSelFiE paragraph) |
| C-004 | 2026-02-14 | Results Section | Improve continuity; organize by RQs | Add 1-sentence takeaway per RQ; shorten captions + supporting-question lists | Planned |  | Already RQ-driven; polish pass remaining |
| C-005 | 2026-02-14 | Limitations/Future Work | Resolve duplication notes in commented blocks | Delete commented duplicate limitations section; keep one canonical version | Planned |  | Shareability blocker |
| C-006 | 2026-02-14 | Submission Hygiene | Anonymity question + acknowledgments | Add \ifanonymous toggle: author/acks; ensure both anonymous + non-anonymous builds compile | Planned |  | Shareability blocker |

## Communication-Driven Queue (Advisor Requests)

| ID | Date Added | Request | Manuscript Location | Planned Fix / Deliverable | Status | Commit | Notes |
|---|---|---|---|---|---|---|---|
| D-001 | 2026-02-15 | Add 2–3 sentence overview of proposed process (no results) | Abstract + Intro | Insert explicit process overview before result sentences in Abstract; expand intro process description only if needed | In Progress |  | Should be done as part of C-001 rewrite |
| D-002 | 2026-02-15 | Short contrast vs closest MAB routing work(s) | Related Work (+ optional intro signpost) | Keep explicit LinkSelFiE/Huang contrasts; add 1 intro sentence signposting the closest-work paragraph | Done |  | Related Work already contains explicit contrasts |
| D-003 | 2026-02-15 | Single “source of truth” manuscript version | Process | Declare QuantumFaultTolerant/main.tex canonical; Overleaf downstream | Done |  | Documented in validation hierarchy; add quick sentence under Conventions |
| D-004 | 2026-02-15 | Advisor access to condensed Overleaf | Logistics | Record what was shared (Overleaf link or commit-pinned PDF) | Planned |  | Non-LaTeX deliverable |
| D-005 | 2026-02-15 | Get manuscript shareable | Whole paper | Bundle closure of C-001/C-002/C-005/C-006 then export PDF | Planned |  | Depends on those items |
| D-006 | 2026-02-15 | Add epsilon + NeuralUCB results + testbed-config comparison table | Results + Cross-Testbed | Add explicit testbed config table (paper-native vs corpus); resolve NeuralUCB reporting consistency | In Progress |  | Source config facts from quantum_project/docs/testbeds/* |
| D-007 | 2026-02-15 | Add Paper 7/12 cross-testbed comparison tables | Cross-Testbed Validation | Ensure tables are integrated and provenance-backed | Done |  | Tables present; add provenance note to validation hub |
| D-008 | 2026-02-15 | Integrate Prof. Travis feedback | Whole paper | Convert Travis feedback into atomic C-* tasks once received | Planned |  | Awaiting feedback artifact |
| D-009 | 2026-02-15 | Add/verify closest-work citation (10621263) | Related Work | Ensure LinkSelFiE is cited in body with direct compare | Done |  | Present as titled LinkSelFiE paragraph |
| D-010 | 2026-02-15 | Confirm venue strategy + sprint plan | Planning | Add sprint checklist: anonymization policy, freeze date, PDF export steps | Planned |  | Non-LaTeX deliverable |
```

## Cross-repo “where to pull facts from” for D-006/D-007 tables

To keep the new testbed-config table defensible (and aligned with your validation posture), the cleanest source paths are:

- Integrated testbed list + status: `quantum_project/docs/TESTBEDS_OVERVIEW.md` fileciteturn49file0  
- Parameter blocks suitable for table rows:
  - Paper 2: `quantum_project/docs/testbeds/Paper2_Quick_Reference.md` fileciteturn55file0  
  - Paper 7: `quantum_project/docs/testbeds/Paper7_Quick_Reference.md` fileciteturn53file0  
  - Paper 12: `quantum_project/docs/testbeds/Paper12_Quick_Reference.md` fileciteturn54file0  
- Provenance contract for what’s “dataset-backed” vs “TBD”: `quantum_project/docs/guides/MASTER_DATASET_VALIDATION_HUB_PLAN.md` fileciteturn56file0  

This also gives you a clean way to answer Dan-style “how do you know these numbers?” questions: you can point to the verification hub plan and (when present) the validation notebook it describes. fileciteturn56file0