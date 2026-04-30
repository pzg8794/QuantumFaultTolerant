# Item 040 — Add rationale for four allocator strategies

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 8:17 am  
**Feedback:**

> How/why did you choose these 4?

## Task

Add a short rationale for the four allocator strategies so the selection does not look arbitrary.

## Content in question

```tex
\smallTitle{Qubit budget and allocator policies}
The network operates under a \textbf{fixed total budget of 35 qubits} distributed across paths. We evaluate \textbf{four allocator strategies} that dynamically or statically assign qubits:
\begin{enumerate}
\item \textbf{Fixed} ($T_1{=}8, T_2{=}10, T_3{=}8, T_4{=}9$): static baseline
\item \textbf{ThompsonSampling}: Bayesian posterior sampling over path utilities
\item \textbf{DynamicUCB}: upper-confidence-bound-driven capacity redistribution
\item \textbf{Random}: uniform random assignment (control baseline)
\end{enumerate}
```

## Proposed solution

Add one concise rationale sentence right before the list:

```tex
\smallTitle{Qubit budget and allocator policies}
The network operates under a \textbf{fixed total budget of 35 qubits} distributed across paths. We evaluate \textbf{four allocator strategies} chosen to span complementary allocation behaviors: a static baseline (\textbf{Fixed}), two principled adaptive heuristics based on posterior sampling and optimistic exploration (\textbf{ThompsonSampling} and \textbf{DynamicUCB}), and a non-informative control baseline (\textbf{Random}). This set allows us to compare whether routing robustness is best supported by fixed, uncertainty-aware, or uninformed allocation under the same total resource budget.
\begin{enumerate}
\item \textbf{Fixed} ($T_1{=}8, T_2{=}10, T_3{=}8, T_4{=}9$): static baseline
\item \textbf{ThompsonSampling}: Bayesian posterior sampling over path utilities
\item \textbf{DynamicUCB}: upper-confidence-bound-driven capacity redistribution
\item \textbf{Random}: uniform random assignment (control baseline)
\end{enumerate}
```

## Decision / status

**Accepted / done.** Add the rationale sentence.