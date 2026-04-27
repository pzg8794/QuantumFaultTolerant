# Item 062 — Use “bandit” consistently for algorithm families

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:16 am  
**Feedback:**

> I think we can say bandit for all

## Task

Decide whether there is any additional wording change beyond the tracked edit where Dan added `Bandit` to the relevant family/table label.

## Content in question

The concrete wording already handled was the table/header label:

```tex
\textbf{Bandit Family}
```

instead of a more generic label such as:

```tex
\textbf{Family}
```

## Proposed solution

No separate global rewrite is needed. This item is covered by using `Bandit Family` in algorithm/model-family tables where the grouping specifically refers to bandit algorithms.

Do not change unrelated labels such as `Allocator Policy`, `Threat Regime`, `Testbed`, or `Model Configuration`, since those are not bandit families.

## Decision / status

**Covered / done.** Treat this as implemented through the `Bandit Family` wording from Item 061. No additional edit needed unless another live `Family` label specifically refers to bandit algorithms.