# Item 027 — Add impact sentence for the matched-threat evaluation gap

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:53 am  
**Feedback:**

> Add a few words/sentence about the impact of this problem. You allude to it above.

## Task

Add one concise sentence explaining why incompatible evaluation assumptions and the matched-threat evaluation gap matter in practice.

## Content in question

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. In some cases, strong results may reflect the surrounding evaluation setup (\eg allocator policy, replay-capacity choices) as much as the learning rule itself.
```

## Proposed solution

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. In some cases, strong results may reflect the surrounding evaluation setup (\eg allocator policy, replay-capacity choices) as much as the learning rule itself. This leaves a \emph{matched-threat evaluation gap}: the lack of a controlled view of when contextual structure is truly necessary, when adversarial robustness dominates, and how allocator policy and replay-capacity semantics alter apparent routing performance. This matters because a routing policy that appears robust may fail when deployed under a different operating regime.
```

## Decision / status

**Approved.** Use Piter-approved wording; remove the duplicated setup sentence and add the concise impact sentence after the matched-threat gap.
