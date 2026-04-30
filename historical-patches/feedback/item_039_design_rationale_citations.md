# Item 039 — Add rationale/citations for systematic modeling choices

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:44 am  
**Feedback:**

> Do any other works also do this? Is there a rationale for doing it like this? Even a few word rationale/citations would be good. Make your decisions be systemtatic. I left comments in the section where other statements regarding decisions should have some reasoning behind them.

## Task

Add concise rationale and citations for modeling/design choices so the paper does not appear to select structure or parameters arbitrarily.

## Content in question

```tex
We model quantum entanglement routing as a sequential decision problem where an agent must jointly optimize (1) \textbf{Path selection} among candidate routes, and (2) \textbf{Qubit allocation} across path segments, under uncertain link fidelities and adversarial interference.
```

## Proposed solution

Add a short rationale sentence after the opening system-model paragraph:

```tex
This joint formulation follows prior quantum-routing work that couples path choice with fidelity estimation, online path selection, or qubit allocation, while making those design dimensions explicit so they can be varied systematically in our evaluation~\cite{wang2025learning,li2025multipath,huang2024quantum}.
```

## Decision / status

**Accepted / done.** Add the rationale sentence with targeted citations.