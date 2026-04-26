# Item 025 — Add citations to show related-work coverage

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:53 am  
**Feedback:**

> Add citations fo a few here to show that you did your homework.

## Task

Add a few targeted citations to support the claim that existing quantum-routing studies cover online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning. Avoid citation dumping; each citation should correspond to a specific class of prior work.

## Content in question

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, and adversarially robust learning. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}.
```

## Proposed solution

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,coopmans2021benchmark,huang2024quantum}. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}.
```

## Decision / status

**Approved.** Use Piter-approved citation split: first citation group supports the classes of prior work; second citation group supports the comparison/gap claim.
