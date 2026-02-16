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

**Status values:** `Planned` | `In Progress` | `Done` | `Deferred` | `TBD`

---

## Current Queue (From Paper Comments)

| ID | Date Added | Location | Comment / Issue | Planned Fix | Status | Commit | Related Canonical Task(s) | Notes |
|---|---|---|---|---|---|---|---|---|
| C-001 | 2026-02-14 | Abstract | Clarify whether this is “evaluation only” vs. new contribution | Add explicit novelty framing (benchmark + taxonomy + capacity paradox + deployment rules) | Planned |  | T-2026-007, T-2025-011 | Also see D-001 |
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
| C-021 | 2026-02-16 | Abstract | Two versions exist | Choose final abstract version | TBD |  | T-2026-007, T-2025-011 | Needs advisor decision |
| C-022 | 2026-02-16 | Introduction Cleanup | Commented blocks remain | Remove commented intro drafts; keep C-### markers | TBD |  | T-2026-007, T-2025-011 |  |
| C-023 | 2026-02-16 | Submission Hygiene | Anonymous submission decision | Decide anonymous vs non-anonymous; update authors/acks accordingly | TBD |  | T-2026-007, T-2025-011 | Needs advisor approval |
| C-024 | 2026-02-16 | RQ Section Flow | Answers appear in RQ section | Move detailed answers to Results; keep questions in RQ section | TBD |  | T-2026-007, T-2025-011 |  |
| C-025 | 2026-02-16 | RQ Scope Clarification | Scope/novelty unclear | Add prior-work citations or clarify novelty statement | TBD |  | T-2026-007, T-2025-011 | Needs advisor input |
| C-026 | 2026-02-16 | Cleanup | Resolved comment markers remain | Remove resolved comment markers | TBD |  | T-2026-007, T-2025-011 |  |
| C-027 | 2026-02-16 | Experimental Design | Missing design rationale | Add 1 sentence per major design choice | TBD |  | T-2026-007, T-2025-011 |  |
| C-028 | 2026-02-16 | Limitations/Future Work | Duplicate sections | Consolidate into one section | TBD |  | T-2025-011 |  |
| C-029 | 2026-02-16 | Results Narrative | Weak transitions | Add question → finding → evidence transitions | TBD |  | T-2025-011 |  |
| C-030 | 2026-02-16 | Code/Data Availability | Statement decision needed | Decide availability statement; add or remove | TBD |  | T-2025-011 | Needs advisor input |
| C-004 | 2026-02-14 | Results Section | Improve continuity; organize by RQs | Add short “RQ claim → evidence → takeaway” scaffolding per subsection | Done |  | T-2025-011 | Visible in `main.tex` (Hypothesis → Experimental Design → Key Findings → Answer per RQ) |
| C-005 | 2026-02-14 | Limitations/Future Work | Resolve duplication notes in commented blocks | Remove/retire duplicate commented section after confirming nothing unique | Planned |  | T-2025-011 |  |
| C-006 | 2026-02-14 | Submission Hygiene | Anonymity question + acknowledgments | Decide anonymous vs non-anonymous; adjust authors/acks accordingly | Planned |  | T-2025-011 |  |

---

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

**Resolution checklist (apply only after approval):**
- Insert the paragraph at the specified location in `main.tex` (do not move other content).
- Keep Dan’s comment as an audit trail but mark it resolved by commenting it out (prefix with `%`) and appending: `RESOLVED by paragraph inserted below (commit: TBD)`.

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
| **Foundational Bandits and Regret Regimes** | ✓ All papers explicitly named | auer2002ucb1 (UCB), thompson1933likelihood (Thompson Sampling), auer2002nonstochastic (EXP3) all explicitly tied to their algorithms |
| **Contextual and Neural Bandits** | ✓ All papers explicitly named | li2010contextual (LinUCB), zhou2020neuralucb (NeuralUCB), zhang2020neural (NeuralTS) all explicitly tied to their contributions |
| **Adversarial and Hybrid Robustness** | ✓ Papers named | auer2002nonstochastic (EXP3), thathachar2011networks (pursuit/hybrid) explicitly cited |
| **Predictive and Informed Bandits** | ✓ Papers explicitly named | zhang2021icmab (iCMAB), box2015time (ARIMA forecasting) explicitly tied to contributions |
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
| 2026-02-16 | main.tex | Consolidated RQ2 supporting questions into two items (C-008) | Reduce duplication per Devroop |  |  |
| 2026-02-16 | main.tex | Figure/table formatting fixes (C-011, C-012, C-013, C-015, C-016, C-017, C-018) | Improve layout/readability |  |  |
| 2026-02-16 | main.tex | Added missing table citations (C-020) | Ensure all tables are cited |  | Pending review |

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

**Status:** In Progress (applied in `main.tex`; pending final review)  
**Supersedes:** C-019 (which only tracked 2 of the 6 missing citations)  
**Related tasks:** T-2026-007, T-2025-011

---
