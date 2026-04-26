# Item 025 — Add citations to show related-work coverage

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:53 am  
**Feedback:**

> Add citations fo a few here to show that you did your homework.

## Task

Add a few targeted citations to support the claim that existing quantum-routing studies cover online path selection, benchmarking-driven routing, adversarially robust learning, and related routing/evaluation mechanisms. Avoid citation dumping; each citation should correspond to a specific class of prior work.

## Content in question

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, and adversarially robust learning. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}.
```

## Proposed solution

Use a slightly broader but still targeted citation set that already exists in `refs.bib`:

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, adaptive route selection, and adversarially robust learning~\cite{wang2025learning,li2025multipath,liu2024qbgp,coopmans2021benchmark,chaudhary2023quantum,huang2024quantum}. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance.
```

## Decision / status

Pending Piter review.
