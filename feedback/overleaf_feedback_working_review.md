# Overleaf Feedback Working Review

**Process:** feedback item → task → content in question → proposed solution → decision/status.  
**Rule:** Work one item at a time. If Piter corrects an item, update this log before proceeding.

---

## Item 001 — Blocked

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 8:04 am  
**Feedback:**

> I will review the RL section later on. It will almost surely need to be cut back quite a bit for the actual submission.

### Task

Treat as a section-level compression warning. Do not edit yet because Dan explicitly says he will review later.

### Content in question

```tex
\section{Related Work}
```

### Proposed solution

No manuscript edit yet. Keep this item blocked until Dan completes/clarifies the later section review.

### Decision / status

**Blocked.** Pending later review/clarification.

---

## Item 002 — Blocked

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:25 am  
**Feedback:**

> WIll likely need to remove this entire section

### Task

Evaluate whether the referenced subsection should be removed entirely or absorbed into a shorter Related Work opening. Because this asks for section removal/reduction, defer it until we finish the non-reduction/non-removal items that may affect the same text.

### Content in question

```tex
\subsection{Literature Selection Methodology}
```

### Proposed solution

No manuscript edit yet. Revisit during the later reduction pass. The likely direction is to remove the standalone `Literature Selection Methodology` subsection heading and retain only necessary methodology context as concise Related Work prose.

### Decision / status

**Blocked.** Reduction/removal task deferred until we reach the later cleanup/reduction pass.

---

## Item 003 — Approved

### Feedback item

**Reviewer:** Devroop Kar  
**Date/time:** 22 April, 7:36 am  
**Feedback:**

> I dont think you need to mention the exact source libraries. Just focus on the types of works.

### Task

Revise the literature-review methodology sentence so it avoids naming exact source libraries/databases and instead describes the categories of literature reviewed.

### Content in question

```tex
We conducted a targeted literature search spanning 2002--2025 across arXiv, IEEE Xplore, and the ACM Digital Library, using keyword combinations covering quantum routing, entanglement distribution, and bandit-based online decision-making across stochastic, adversarial, contextual, predictive, and hybrid variants.
```

### Proposed solution

```tex
We conducted a targeted literature review spanning 2002--2025 on quantum routing, entanglement distribution, and bandit-based online decision-making, covering stochastic, adversarial, contextual, predictive, and hybrid variants.
```

### Decision / status

**Approved.** Use Piter's revised wording. Apply during manuscript edit pass.

---

## Item 004 — Approved

### Feedback item

**Reviewer:** Devroop Kar  
**Date/time:** 22 April, 7:37 am  
**Feedback:**

> No need to mention what we are excluding

### Task

Remove detailed exclusion criteria from the literature-review methodology prose while preserving the positive purpose of the comparison.

### Content in question

```tex
We excluded offline optimization and control approaches without online bandit feedback, single-domain demonstrations that do not generalize algorithmically, and tuning-only studies lacking methodological novelty, clearly stated assumptions, or reproducibility artifacts, because our goal is to compare lines of work that differ in learning assumptions, not catalog all quantum-network optimization methods.
```

### Proposed solution

```tex
Our goal is to compare lines of work that differ in learning assumptions.
```

### Decision / status

**Approved.** Use Piter's shortened purpose sentence. Apply during manuscript edit pass.

---

## Item 005 — Approved

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:27 am  
**Feedback:**

> Changed: `I` to `Contrastingly, i`

### Task

Review the tracked wording change at the start of the sentence and decide whether the contrast transition should be accepted, revised, or rejected.

### Content in question

```tex
Contrastingly, in our study we use these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement
```

### Proposed solution

```tex
In contrast, our study uses these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement routing.
```

### Decision / status

**Approved.** Use the cleaner `In contrast` version rather than `Contrastingly`.

---

## Item 006 — Duplicate / covered by Item 005

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:27 am  
**Feedback:**

> Deleted: `,`

### Task

This punctuation deletion belongs to the same tracked edit handled in Item 005.

### Content in question

```tex
Contrastingly, in our study we use these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement
```

### Proposed solution

No separate action. Use the approved Item 005 rewrite:

```tex
In contrast, our study uses these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement routing.
```

### Decision / status

**Duplicate / covered by Item 005.** No independent manuscript edit.

---

## Item 007 — Accepted tracked edit

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:29 am  
**Feedback:**

> Changed: `et al.` to `\etal`

### Task

Verify Dan's tracked macro-standardization. This is a tracked edit he already made, not a separate rewrite request.

### Content in question

```tex
Wang \etal~\cite{wang2025learning} focus on learning high-quality paths under stochastic dynamics, while Li et al.
```

### Proposed solution

Accept Dan's tracked edit from `et al.` to `\etal` wherever that specific tracked change was applied. Do not add additional rewrites under this item.

### Decision / status

**Accepted tracked edit.** No separate manuscript action beyond accepting/keeping Dan's `\etal` change.

---

## Item 008 — Approved

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:30 am  
**Feedback:**

> Changed: `W` to `In contrast, w`

### Task

Verify Dan's tracked transition edit and decide whether to keep it as-is or improve the sentence.

### Content in question

```tex
In contrast, we do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees;
```

### Proposed solution

```tex
In contrast, we provide a controlled robustness characterization that isolates which algorithm--allocator--capacity combinations remain stable when disruption is structured or adaptive.
```

### Decision / status

**Approved.** Use Piter's concise positive-framing version.

---

## Item 009 — Approved

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:30 am  
**Feedback:**

> Make it a bit more clear how our work differs.

### Task

Clarify how this work differs specifically from Huang et al.'s EXPNeuralUCB paper. The contrast should explain that Huang et al. propose a specific group neural bandit, while this paper uses EXPNeuralUCB as one comparator inside a broader controlled robustness study that also varies threat model, allocator choice, and replay/capacity settings.

### Content in question

```tex
In contrast, we provide a controlled robustness characterization that isolates which algorithm--allocator--capacity combinations remain stable when disruption is structured or adaptive. Huang et al.~\cite{huang2024quantum} propose \emph{EXPNeuralUCB}, a group neural bandit that combines EXP3-style adversarial exploration with NeuralUCB-style nonlinear reward modeling for joint path selection and qubit allocation.
```

### Proposed solution

```tex
Huang et al.~\cite{huang2024quantum} propose \emph{EXPNeuralUCB}, a group neural bandit that combines EXP3-style adversarial exploration with NeuralUCB-style nonlinear reward modeling for joint path selection and qubit allocation. Our work uses EXPNeuralUCB as one comparator within a broader controlled robustness study that evaluates multiple bandit families under a shared threat taxonomy. In addition to EXPNeuralUCB, we evaluate pursuit--neural hybrids (e.g., \texttt{CPursuitNeuralUCB}, \texttt{iCPursuitNeuralUCB}) under matched threat, allocator, and replay/capacity settings. This comparison separates the effect of changing the learning rule from the effect of changing the deployment configuration around it. Whereas Huang et al.~\cite{huang2024quantum} treat allocation as a fixed component, our framework explicitly varies allocator strategy and replay capacity, showing that these factors can be as critical to robustness as the learning rule itself.
```

### Decision / status

**Approved.** Use Piter-approved improved paragraph.

---

## Item 010 — Accepted tracked edit

### Feedback item

**Reviewer:** Devroop Kar  
**Date/time:** 22 April, 7:41 am  
**Feedback:**

> Changed: `\` to `~\cite{huang2024quantum}`

### Task

Verify Devroop's tracked citation insertion. This is a tracked edit already made, not a new rewrite request.

### Content in question

```tex
Further, while Huang et al. ~\cite{huang2024quantum} treat allocation as a fixed component,
```

### Proposed solution

Accept Devroop's citation insertion to `~\cite{huang2024quantum}`. No separate manuscript action is needed under this item beyond keeping the citation change.

### Decision / status

**Accepted tracked edit.** No separate manuscript action beyond keeping Devroop's citation insertion.

---

## Item 011 — Blocked

### Feedback item

**Reviewer:** Devroop Kar  
**Date/time:** 22 April, 7:43 am  
**Feedback:**

> Added: `\devroop{Need to reduce the content while keeping the contextual ideas and gap comparisons. This is too long.}`

### Task

Evaluate the referenced section for later compression while preserving the contextual ideas and gap comparisons.

### Content in question

```tex
\subsection{Quantum Network Routing with Bandits}
```

### Proposed solution

No manuscript edit yet. This is a reduce/cut task, so defer it until the later reduction pass after all non-reduction/non-removal items affecting the same section are handled.

During that pass, compress the subsection by keeping only: (1) the closest related works, (2) the gap comparisons, and (3) the specific contrast with our algorithm--allocator--capacity evaluation framework.

### Decision / status

**Blocked.** Reduction/removal task deferred until the later cleanup/reduction pass.

---

## Item 012 — Approved

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 12:00 pm  
**Feedback:**

> Added: `% Piter % Jie % Jie Student % Sheeraja % Travis % Devroop % Dan`

### Task

Verify whether this added author/comment placeholder should remain in the source, be moved into an author-planning note, or be removed from the manuscript source before submission.

### Content in question

```tex
% Piter
% Jie
% Jie Student
% Sheeraja
% Travis
% Devroop
% Dan
```

### Proposed solution

```tex
% TODO(author-list): confirm final author order/names before submission.
```

### Decision / status

**Approved.** Replace informal name-list comments with the TODO author-list reminder.

---

## Item 013 — Accepted tracked edit

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 4:43 pm  
**Feedback:**

> Changed: `often` to `frequently`

### Task

Verify Dan's tracked wording edit.

### Content in question

```tex
Existing routing approaches frequently assume stationary link behavior, decouple selection from allocation, or rely on offline optimization assumptions that can fail when link fidelities drift and disruptions adapt online.
```

### Proposed solution

Accept the tracked wording edit. `Frequently` is slightly more formal than `often` and fits the manuscript tone.

### Decision / status

**Accepted tracked edit.** No separate manuscript action beyond keeping Dan's wording change.

---

## Item 014 — Accepted tracked edit

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 4:43 pm  
**Feedback:**

> Changed: `---` to empty text

### Task

Verify Dan's tracked punctuation cleanup in the same sentence cluster.

### Content in question

```tex
Existing routing approaches frequently assume stationary link behavior, decouple selection from allocation, or rely on offline optimization assumptions that can fail when link fidelities drift and disruptions adapt online.
```

### Proposed solution

Accept the tracked deletion of `---`. The sentence is clearer without an em-dash/placeholder separator.

### Decision / status

**Accepted tracked edit.** No separate manuscript action beyond keeping Dan's punctuation cleanup.

---

## Item 015 — Accepted tracked edit

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 4:44 pm  
**Feedback:**

> Deleted: `those`

### Task

Verify Dan's tracked word deletion in the same sentence cluster.

### Content in question

```tex
Existing routing approaches frequently assume stationary link behavior, decouple selection from allocation, or rely on offline optimization assumptions that can fail when link fidelities drift and disruptions adapt online.
```

### Proposed solution

Accept the tracked deletion of `those`. The current phrase `assumptions that can fail` is concise and grammatical.

### Decision / status

**Accepted tracked edit.** No separate manuscript action beyond keeping Dan's word deletion.

---

## Item 016 — In review

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 4:44 pm  
**Feedback:**

> Changed: `e primary contribution of this paper is` to `is work provides`

### Task

Verify Dan's tracked rewrite from a contribution-framing phrase toward the clearer `This work provides` framing.

### Content in question

```tex
This work provides a systematic threat-aware evaluation framework and uses it to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit--neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.
```

### Proposed solution

Accept the tracked rewrite direction. The `This work provides...` framing is clearer and more direct than `The primary contribution of this paper is...`.

If we want the sentence to align with the earlier approved Item 1 wording, use:

```tex
This work provides a systematic threat-aware framework to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit--neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.
```

### Decision / status

Pending Piter review.
