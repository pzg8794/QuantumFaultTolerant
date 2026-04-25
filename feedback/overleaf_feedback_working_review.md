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

## Item 006 — In review

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:27 am  
**Feedback:**

> Deleted: `,`

### Task

Review the punctuation deletion associated with the same contrast sentence.

### Content in question

```tex
Contrastingly, in our study we use these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement
```

### Proposed solution

The punctuation issue is resolved by the approved Item 005 rewrite. Use:

```tex
In contrast, our study uses these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement routing.
```

This keeps the comma after `In contrast`, which is grammatically correct and clearer than the tracked deletion applied to `Contrastingly`.

### Decision / status

Pending Piter review.
