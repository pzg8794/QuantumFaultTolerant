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

**Status values:** `Planned` | `In Progress` | `Done` | `Deferred`

---

## Current Queue (From Paper Comments)

| ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Related Canonical Task(s) | Notes |
|---|---|---|---|---|---|---|---|---|
| C-001 | 2026-02-14 | Abstract | Clarify whether this is “evaluation only” vs. new contribution | Add explicit novelty framing (benchmark + taxonomy + capacity paradox + deployment rules) | Planned |  | T-2026-007, T-2025-011 | Also see D-001 |
| C-002 | 2026-02-14 | Introduction | Cleanup TODOs and improve narrative flow | Rewrite intro flow: problem → gap → approach → contributions | Planned |  | T-2026-007, T-2025-011 |  |
| C-003 | 2026-02-14 | Related Work | Dan: "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others" | Ensure every process/method in Related Work is explicitly attributed to the paper(s) that introduced it, with clear descriptions of what each paper does and how it differs from our work | Planned |  | T-2026-007, T-2025-015 | Address via P-001/P-002 + compare-audit table below |
| C-004 | 2026-02-14 | Results Section | Improve continuity; organize by RQs | Add short “RQ claim → evidence → takeaway” scaffolding per subsection | Planned |  | T-2025-011 |  |
| C-005 | 2026-02-14 | Limitations/Future Work | Resolve duplication notes in commented blocks | Remove/retire duplicate commented section after confirming nothing unique | Planned |  | T-2025-011 |  |
| C-006 | 2026-02-14 | Submission Hygiene | Anonymity question + acknowledgments | Decide anonymous vs non-anonymous; adjust authors/acks accordingly | Planned |  | T-2025-011 |  |

---

## C-003 Analysis: Related Work Paper Attribution Audit

**Dan's request (C-003):** "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others"

**What this means:** Every process/method mentioned in Related Work must be explicitly tied to the paper(s) that introduced it, with clear descriptions of what each paper contributes and how it differs from/relates to our work.

### Quantum Routing Papers in Bibliography (refs.bib)

Available quantum routing papers:
1. **wehner2018quantum**: "Quantum Internet: A Vision for the Road Ahead" (Science 2018) - foundational vision paper ✓ appropriately cited in passing
2. **huang2024quantum**: "Quantum Entanglement Path Selection and Qubit Allocation via Adversarial Group Neural Bandits" - adversarial approach ✗ cited but NOT described
3. **wang2025learning**: "Learning Best Paths in Quantum Networks" - stochastic path learning ✓ explicitly described
4. **li2025multipath**: "Multipath Inter-Domain Routing Protocols for Quantum Networks With Online Path Selection" - inter-domain routing ✓ explicitly described
5. **liu2024qbgp**: "Quantum BGP with Online Path Selection via Network Benchmarking" - BGP-style with benchmarking ✓ explicitly described
6. **10621263 (LinkSelFiE)**: Liu et al., "Link Selection and Fidelity Estimation in Quantum Networks" (INFOCOM 2024) - link-level selection and fidelity estimation ✗ NOT cited in body (only in TODOs)

### Related Work Subsection Coverage Status

| Subsection | Paper Attribution Status | Issues |
|---|---|---|
| **Foundational Bandits and Regret Regimes** | ✓ All papers explicitly named | auer2002ucb1 (UCB), thompson1933likelihood (Thompson Sampling), auer2002nonstochastic (EXP3) all explicitly tied to their algorithms |
| **Contextual and Neural Bandits** | ✓ All papers explicitly named | li2010contextual (LinUCB), zhou2020neuralucb (NeuralUCB), zhang2020neural (NeuralTS) all explicitly tied to their contributions |
| **Adversarial and Hybrid Robustness** | ✓ Papers named | auer2002nonstochastic (EXP3), thathachar2011networks (pursuit/hybrid) explicitly cited |
| **Predictive and Informed Bandits** | ✓ Papers explicitly named | zhang2021icmab (iCMAB), box2015time (ARIMA forecasting) explicitly tied to contributions |
| **Quantum Network Routing with Bandits** | ✅ Addressed (pending review/commit) | Added explicit Huang attribution + LinkSelFiE contrast + grouped comparisons (learning/RL/heuristic routing + benchmarking frameworks) via P-001/P-002/P-003 |

### Summary

Most subsections already explicitly attribute processes to papers (Foundational Bandits, Contextual/Neural Bandits, Predictive Bandits all explicitly name papers and tie them to contributions). The **only subsection with gaps** is "Quantum Network Routing with Bandits":

- **Gap 1:** Huang et al. is cited but never explicitly described → **P-001**
- **Gap 2:** LinkSelFiE (10621263) is not cited in the body at all → **P-002**
- **Gap 3:** Adjacent quantum routing lines (learning/RL/heuristic routing + benchmarking frameworks) not explicitly positioned → **P-003**
- **Gap 4:** Wang et al. (adaptive user-centric routing) not cited/positioned → **P-004**
- **Already complete:** Wang, Li, Liu (qbgp) are explicitly discussed; wehner2018quantum is appropriately cited as foundational/vision paper

---

## Quantum Routing/Networking Papers in refs.bib — Comparison Checklist for Related Work (C-003)

This table is a **comparison checklist** (for C-003): for each relevant quantum routing/networking paper in `refs.bib`, ensure Related Work contains at least 1–2 sentences that state (a) what the paper does and (b) how our work differs (or why it is complementary). Use the **Action** column to track whether the compare-text has been inserted.
The **Remote PDF (repo)** links are GitHub *blob* links (view-in-repo) and resolve once the corresponding PDF is committed/pushed to the `QuantumFaultTolerant` GitHub repo.

| BibTeX Key | What the paper does (1-line) | How our work differs (direct compare) | Why it matters / relevance | Where to cite (02--related_works.tex) | Action | Remote PDF (repo) |
|---|---|---|---|---|---|---|
| wehner2018quantum | Vision paper framing the quantum internet agenda | Our work is an empirical learning/evaluation study (routing + allocation under threats), not a roadmap paper | Medium: canonical anchor; orients readers new to quantum networking | Quantum Network Routing with Bandits (opening cite list) | Already cited (pre-existing) | [Paper PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Quantum-internet-A-vision.pdf) \| [Alt (accepted ms.)](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/quantum-internet-a-vision-for-the-road-ahead-5g5cy9s9m0.pdf) |
| wang2024adaptive | Adaptive user-centric entanglement routing in quantum data networks | Our work contributes a controlled evaluation methodology (threat taxonomy + allocator/replay/capacity factorization) rather than proposing a single routing algorithm | High/Medium: routing-focused quantum network paper that should be acknowledged directly | Quantum Network Routing with Bandits | Applied (02--related_works.tex; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Adaptive_User_Centric_Entangleme%20%282404.09048v1_Adaptive_User-Centric_Entanglement_Routing_in_Quantum_Data_Networks%29.pdf) |
| huang2024quantum | Adversarially robust path selection + qubit allocation via group neural bandit formulations | We do not introduce a new adversarial bandit variant; we benchmark decision-rule families and isolate allocator/replay/capacity effects under a shared threat taxonomy | High: closest adversarial-first quantum routing baseline we compare against | Quantum Network Routing with Bandits | Applied (P-001; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Huang_2024_EXPNeuralUCB_Adversarial_Group_N%20%282411.00316v1_Quantum_Entanglement_Path_Selection_and_Qubit_Allocation_via_Adversarial_Group_Neural_Bandits%3B%20tb%3DEXPNeuralUCB__GA-Paper-EXPNeu%29.pdf) |
| 10621263 | LinkSelFiE: link selection + fidelity estimation under unknown link qualities | LinkSelFiE is link-level best-arm identification + estimation; our work is routing-level (path + allocation) and methodology-first (threat taxonomy + allocator/replay/capacity factorization) | High: explicitly called out in Dan’s comment as closest-work compare | Quantum Network Routing with Bandits (after Huang) | Applied (P-002; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Liu_2024_LinkSelFiE_Link_Selection_Fideli%20%28LinkSelFiE_Link_Selection_and_Fidelity_Estimation%29.pdf) |
| chaudhary2023quantum | Learning-based route selection under noisy/stochastic quantum communication conditions | Our focus is **comparative evaluation across threat models + allocators + replay/capacity**; use this as a contrast point for works that evaluate learning only under noise/stochastic dynamics | High: closest “learning-based routing” neighbor; helps justify our broader adversarial taxonomy | Quantum Network Routing with Bandits | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Chaudhary_2023_Learning_based_Route_Selection_N%20%28Quantum_Bandit_ICC2023%3B%20tb%3DPaper2__paper2_chaudhary2023quantum%29.pdf) |
| wang2024quarc | Routing using adaptive clustering (non-bandit heuristic/structure method) | Our work is learning-centric and evaluates **algorithm–allocator–capacity** interactions; clustering can be framed as a complementary baseline/structure prior rather than a decision-rule comparison | Medium: shows non-learning adaptive routing line of work | Quantum Network Routing with Bandits (grouped) | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/Wang_2024_Efficient_Routing_Quantum_Networ%20%28paper12__paper12_wang2024quarc%3B%20tb%3Dpaper12__paper12_wang2024quarc%29.pdf) |
| jallowkhan2025adaptive | RL-style (DQN) adaptive entanglement routing | We study **bandit-style online decision rules** with controlled comparisons and bandit-theory motivation; RL requires different training/feedback assumptions and is not the focus of our benchmark | High: shows adjacent solution family (RL) and motivates why we pick bandits + regret framing | Quantum Network Routing with Bandits | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2503.02895v1.pdf) |
| cicconetti2024scalable | Hierarchical entanglement routing for scalable quantum networks | Our contribution is evaluation methodology for learning-based routing under mixed threats; cite this as scalability/architecture-focused routing that is orthogonal to our decision-rule study | Medium: supports a “routing design space” framing (structure vs learning) | Quantum Network Routing with Bandits (grouped) | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2306.09216v2.pdf) |
| kumar2024routing | Routing in repeater networks with mixed efficiency constraints | We abstract physical constraints into the environment/reward and focus on learning + allocator interplay; cite as complementary “physics/repeater-focused routing” | Medium: helps clarify scope boundaries (we are not a repeater-physics routing paper) | Quantum Network Routing with Bandits (grouped) | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2310.08990v4.pdf) |
| leone2021costvector | Multi-path entanglement routing via cost-vector analysis (optimization/metric-driven) | Our benchmark is about **online learning under uncertainty/adversaries**; cost-vector routing is a different (non-learning) approach that can be positioned as complementary when dynamics are known/solved via optimization | Medium: covers multi-path routing line of work outside learning | Quantum Network Routing with Bandits (grouped, end) | Applied (P-003; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2105.00418v3.pdf) |
| coopmans2021benchmark | General benchmarking procedure for quantum networks | We contribute a **learning-specific** benchmark: threat taxonomy + allocator/replay/capacity controls; cite these as broader benchmarking foundations | Medium: anchors “benchmarking” motivation beyond our specific learning stack | Toward a Modular, Universal Bandit Stack (or a short benchmarking sentence near end of Quantum Routing subsection) | Applied (02--related_works.tex; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2103.01165v1.pdf) |
| kozlowski2022utility | Utility/metric framework for benchmarking quantum networks | Same contrast as above: their focus is utility/metrics; ours is controlled learning evaluation across threats and allocator assumptions | Medium: supports evaluation/metric legitimacy | Same as above (group with coopmans2021benchmark) | Applied (02--related_works.tex; pending review/commit) | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2210.10752v1.pdf) |
| buchholz2023quantum | Theoretical work on bandits with quantum channel oracles | Our work is quantum networking + learning evaluation; cite only if we add a short “quantum-bandit theory exists” sentence (otherwise omit to keep Related Work focused) | Low: not routing/allocation | Foundations / (optional) | Skip by default | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2301.08544v4.pdf) |
| brahmachari2024quantum | Quantum contextual bandits and recommender systems for quantum data | Not routing; cite only if we explicitly broaden to “quantum bandits beyond networking” (likely unnecessary) | Low | Foundations / (optional) | Skip by default | [PDF](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/references/pdfs/2301.13524v1.pdf) |

> Relevance Rank: High = likely deserves explicit comparison; Medium = grouped/brief mention; Low = skip unless space allows.

**Sanity notes (bib hygiene impacting C-003):**
- `refs.bib`: duplicates now commented out to avoid duplicate numbered references: `lee2022utility` → `kozlowski2022utility` (arXiv:2210.10752), `smith2024costvector` → `leone2021costvector` (arXiv:2105.00418), and `brahmachari2023quantum` → `brahmachari2024quantum` (arXiv:2301.13524). Corresponding duplicate rows are removed/avoided in this table.

## Proposed Edits (Review Before Applying)

These are **draft insertions** prepared for review. **Current state:** P-001/P-002/P-003/P-004 are applied in the working tree (uncommitted) to `02--related_works.tex`, and P-005 is applied in the working tree (uncommitted) to `main.tex`; both should be reviewed before finalizing/committing.

**What a `P-###` is:** a review-stage, manuscript-impacting to-do item with (i) which task it solves (C-### or D-###), (ii) the exact source comment/TODO, (iii) the draft text that would be inserted, and (iv) the planned insertion location. After approval, it gets applied to the manuscript and should be recorded in the Change Log with a commit.

### P-001 — Add explicit Huang et al. attribution in Quantum Network Routing subsection

**Solves:** C-003 (Related Work paper attribution)

**Source TODO/comment:**
- `related_works.tex` L79: Dan note: "make sure that you are directly comparing your work against existing papers, not only existing processes: \eg ~\cite{10621263} and others" ([../sections/02--related_works.tex](../sections/02--related_works.tex#L79))

**Issue:** The "Quantum Network Routing with Bandits" subsection cites `huang2024quantum` but doesn't explicitly describe Huang et al.'s contribution—only Wang, Li, and Liu are named.

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the current Wang/Li/Liu sentence.

**Proposed text (LaTeX):**

```tex
Huang et al.~\cite{huang2024quantum} study adversarially robust path selection and qubit allocation via group neural bandit formulations; in contrast to introducing a new adversarial learner, our contribution is to benchmark multiple decision-rule families under a shared threat taxonomy with allocator/replay/capacity treated as explicit experimental variables.
```

**Why this makes sense:**
- Huang is cited in the opening sentence but never explicitly discussed—this fixes the gap.
- Clarifies that Huang's work is the adversarial-first quantum routing baseline we're comparing against.

---

### P-002 — Add explicit LinkSelFiE contrast paragraph (Dan's example cite)

**Solves:** C-003 (Related Work paper attribution)

**Source TODO/comment:**
- `main.tex` L216: "TODO: Be sure to compare against \cite{10621263}" ([../main.tex](../main.tex#L216)) - **This TODO will be removed once LinkSelFiE is properly cited in Related Work**
- `related_works.tex` L79: Dan note citing `\cite{10621263}` as example ([../sections/02--related_works.tex](../sections/02--related_works.tex#L79))

**Issue:** LinkSelFiE (Liu et al., cite 10621263, INFOCOM 2024) is NOT currently cited anywhere in the paper body—only in TODO comments. Dan's note uses it as an example of a related paper we should be comparing against explicitly.

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

**Proposed text (LaTeX):**

```tex
\paragraph{Closest-work contrast (LinkSelFiE).}
Liu et al.~\cite{10621263} propose \emph{LinkSelFiE}, which targets the \emph{link-level} problem of selecting a high-fidelity entanglement link and accurately estimating its fidelity when link qualities are unknown \emph{a priori}. They formulate this as a best-arm identification task and use a phase-based elimination strategy around a network-benchmarking subroutine to reduce quantum resource consumption while still identifying the best link with high confidence. In contrast, our study targets \emph{routing-level} decisions: joint \emph{path selection and qubit allocation} over time under five threat regimes, and we quantify robustness through a controlled cross-product evaluation across algorithms, allocators, and replay-capacity semantics. LinkSelFiE is therefore best viewed as a complementary lower-layer primitive (improving link-quality estimation/benchmarking), whereas our contribution is an end-to-end evaluation and deployment characterization that isolates allocator--capacity interactions and failure modes under adaptive disruption.
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

**Proposed text (LaTeX):**

```tex
Beyond bandit-style path selection, learning-based route selection under noisy quantum-network conditions has also been explored~\cite{chaudhary2023quantum}, and RL-based adaptive routing has been proposed via deep Q-networks~\cite{jallowkhan2025adaptive}. Complementary non-learning routing designs emphasize structural decomposition (e.g., adaptive clustering~\cite{wang2024quarc} and hierarchical routing for scalability~\cite{cicconetti2024scalable}) or repeater/efficiency constraints~\cite{kumar2024routing}, while cost-vector approaches optimize multi-path routing decisions through explicit objective formulations~\cite{leone2021costvector}. In contrast, our contribution is a controlled evaluation methodology that isolates how decision-rule families interact with allocation policies, replay semantics, and capacity across a shared threat taxonomy, enabling direct attribution of robustness to the algorithm--allocator--capacity triad rather than to a single routing primitive.
```

**Why this makes sense:**
- Provides direct comparisons against additional routing lines already in `refs.bib` without expanding the subsection into a survey.
- Makes explicit that our paper’s novelty is methodological (evaluation + taxonomy + factorization), not “yet another routing algorithm”.
- PDFs for the cited works are tracked under `references/pdfs/` (see the comparison checklist table’s **Remote PDF (repo)** column for one-click access).

---

### P-004 — Add explicit Wang et al. (adaptive user-centric routing) comparison sentence

**Solves:** C-003 (Direct comparison against existing papers)

**Issue:** `wang2024adaptive` is in `refs.bib` but was not previously cited/positioned in Related Work. This is a routing-focused quantum networking paper that should be acknowledged directly, and contrasted against our evaluation-first contribution.

**Target location:** [../sections/02--related_works.tex](../sections/02--related_works.tex), "Quantum Network Routing with Bandits" subsection, after the Wang/Li/Liu sentence (before Huang/LinkSelFiE is fine).

**Proposed text (LaTeX):**

```tex
Wang et al.~\cite{wang2024adaptive} further study adaptive, user-centric entanglement routing in quantum data networks; in contrast, we do not propose a new routing algorithm but rather provide a controlled evaluation methodology that isolates algorithm--allocator--capacity effects across threat regimes.
```

**Why this makes sense:**
- Adds a direct paper-to-paper comparison for an additional quantum routing paper already present in `refs.bib`.
- Keeps the focus on how our contribution differs (evaluation methodology vs single-method routing proposal).

---

### P-005 — Fix undefined citation keys for external testbed references (removes “?” citations)

**Solves:** Reference integrity (comment feedback: “citation key shows as `?`”)

**Issue:** `main.tex` used placeholder citation keys (`paper2_reference`, `paper7_reference`, `paper12_reference`) which were not present in `refs.bib`, causing undefined citations.

**Applied fix (LaTeX):**
- `paper2_reference` → `chaudhary2023quantum`
- `paper7_reference` → `liu2024qbgp`
- `paper12_reference` → `wang2024quarc`

**Where applied:** [../main.tex](../main.tex), Cross-Testbed Validation section (external testbed configuration bullets + cross-testbed validation summary).

## Communication-Driven Queue (Advisor Requests)

These are paper-impacting requests captured in the comms log; this keeps the manuscript to-do list and its “why” in one place.

| ID | Date Added | Request (From Comms) | Manuscript Location | Planned Fix / Deliverable | Status | Commit | Related Canonical Task(s) | Source |
|---|---|---|---|---|---|---|---|---|
| D-001 | 2026-02-15 | Add a 2–3 sentence overview of the proposed process (no results) | Abstract + Intro (process description) | Write 2–3 sentence process overview for abstract; expand Intro process description (double/triple length) | Planned |  | T-2026-007, T-2025-011 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-002 | 2026-02-15 | Provide a short contrast vs closest MAB routing work(s) | Related Work | Ensure direct comparison against closest cited work(s) is explicit and easy to find | Planned |  | T-2026-007, T-2025-015 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-003 | 2026-02-15 | Keep a single “source of truth” manuscript version | Submission Hygiene | Confirm single-source workflow in the paper repo (local) and avoid diverging forks; reflect in tracker conventions | Done |  | T-2026-007 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-004 | 2026-02-15 | Grant advisor access to the condensed Overleaf view/project | Submission Logistics | Ensure access is granted (or provide an equivalent local PDF) and record what was shared | Planned |  | T-2026-009 | [Research comms log](../../GA_Communications/md_files/Research-Communications.md) |
| D-005 | 2026-02-15 | Get the manuscript into a shareable state and address high-level comments | Whole paper (general) | Address high-level comments; ensure the manuscript is shareable for team review | Planned |  | T-2026-007, T-2025-011 | [Email PDF: Qubit Allocation Paper](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Qubit%20Allocation%20Paper.pdf) |
| D-006 | 2026-02-15 | Add epsilon + NeuralUCB results + extra comparison table (testbed configs) | Results + Tables | Add epsilon + NeuralUCB results; add a comparison table contrasting paper config vs our run config | Planned |  | T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-007 | 2026-02-15 | Add Paper 7/12 cross-testbed comparison tables once jobs finish | Results + Tables | Integrate comparison tables into the manuscript once jobs complete; keep values source-backed | Planned |  | T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-008 | 2026-02-15 | Integrate Professor Travis feedback before submission | Whole paper (general) | Apply Travis edits/comments once received; record deltas as atomic C-### items | Planned |  | T-2026-005, T-2025-011 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-009 | 2026-02-15 | Add/verify closest-work citation suggestion (e.g., IEEE 10621263) | Related Work | Read + incorporate as closest-work reference; ensure direct comparison is explicit | Planned |  | T-2026-007, T-2025-015 | [Email PDF: Sheeraja feedback update](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Update_%20Sheeraja%27s%20Feedback%20Items%20-%20All%20Core%20Tasks%20Completed.pdf) |
| D-010 | 2026-02-15 | Confirm venue strategy + submission sprint plan | Submission Planning | Confirm target venue(s)/track(s) and the 1–2 week sprint plan to get the manuscript submission-ready | Planned |  | T-2026-009 | [Email PDF: US venues shortlist](../../GA_Communications/emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20US%20venues%20%28B-rated%20or%20higher%29%20for%20quantum%20networking%20paper.pdf) |

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

---

## Conventions

- **Location**: use the paper section name or a local file link (e.g., [../main.tex](../main.tex), [../sections/02--related_works.tex](../sections/02--related_works.tex)).
- **Commit**: short hash (e.g., `a1b2c3d`) once committed.
- Keep this file free of remote URLs when possible.
