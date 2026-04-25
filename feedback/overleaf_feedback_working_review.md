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

## Item 002 — In review

### Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:25 am  
**Feedback:**

> WIll likely need to remove this entire section

### Task

Evaluate whether the referenced subsection should be removed entirely or absorbed into a shorter Related Work opening.

### Content in question

```tex
\subsection{Literature Selection Methodology}
```

### Proposed solution

Remove the standalone `Literature Selection Methodology` subsection heading and fold only the necessary methodological context into the opening Related Work prose. This preserves the useful framing while avoiding a separate methods-style subsection that may be too long or unnecessary for the final submission.

Candidate action:

```diff
- \subsection{Literature Selection Methodology}
+ % Removed standalone literature-selection subsection; retained only concise related-work framing in prose.
```

### Decision / status

Pending Piter review.
