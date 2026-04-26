# Item 023 — Add citation for entanglement-routing distinction

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:27 am  
**Feedback:**

> Add citation

## Task

Add an appropriate citation to support the claim that quantum routing differs from classical packet switching because the routed resource is entanglement rather than transferable classical data.

## Content in question

```tex
Quantum routing also differs fundamentally from classical packet switching routing because the underlying resource is \emph{entanglement}, not transferable data~\cite{}.
```

## Proposed solution

Use existing bibliography keys that already appear in `refs.bib`. The best local fit is to cite general quantum Internet/networking references here, while leaving the no-cloning theorem citation in the following sentence.

```tex
Quantum routing also differs fundamentally from classical packet-switching routing because the underlying resource is \emph{entanglement}, not transferable data~\cite{kimble2008quantum,wehner2018quantum}.
```

## Decision / status

Pending Piter review.
