# Study Design Research Questions Reduction Audit

This document records the accepted reduction for the Study Design mini-section `Research Questions`.

## Process requirements applied

The mini-section was treated as its own section. Each idea was checked against completed sections: Abstract, Introduction, Background, Related Work, and the already-staged System Model. ICNP constraints were checked explicitly: page pressure, formal clarity, blind-submission hygiene, figure/table usefulness, and whether repeated ideas should become cross-references instead of deletions.

## Mini-section role

The Research Questions mini-section should state the questions that organize Study Design and Results. It should not answer the questions, preview all findings again, repeat the abstract, repeat the introduction contribution bullets, or use long subsubsection blocks when a compact paragraph is sufficient.

## Split-level decisions

### Split 1: Section title and label

The title and label are useful Study Design structure and were kept.

Accepted text:

```tex
\subsection{Research Questions}
\label{sec:research_questions}
```

### Split 2: Author comments and validation notes

Internal comments and validation notes were removed. They are not paper content and should not appear in a venue draft.

### Split 3: Opening sentence

The original opening said the study addresses three core questions about stochastic decoherence impact, adversarial robustness, and deployment tradeoffs in algorithm--allocator--capacity selection. This overlapped strongly with the Abstract, Introduction, Background, and System Model. The accepted version turns the idea into a concise cross-reference to the formal interface already defined in System Model.

Accepted reduction:

```tex
Using the matched interface defined in \cref{sec:SystemModel}, we organize the evaluation around three questions:
```

### Split 4: RQ1

RQ1 should ask about stochastic/no-disruption behavior without previewing results.

Accepted reduction:

```tex
\textbf{RQ1:} How do bandit policies differ under stochastic link success and no-disruption or benign-failure regimes?
```

### Split 5: RQ2

The original RQ2 asked how different bandit-based routing strategies perform as disruptions evolve from stochastic noise to structured and adaptive adversarial interference. Dan's accepted feedback reworded this toward how performance changes as disruption evolves. The accepted version keeps that idea while compressing it for inline flow.

Accepted reduction:

```tex
\textbf{RQ2:} How does routing performance change as disruption evolves from stochastic noise to structured and adaptive interference?
```

### Split 6: RQ3

RQ3 should ask about deployment tradeoffs in algorithm--allocator--capacity selection without answering with the capacity paradox.

Accepted reduction:

```tex
\textbf{RQ3:} How do allocator policy and replay/capacity semantics change the best model choice under each threat regime?
```

## Accepted reduced mini-section

```tex
\subsection{Research Questions}
\label{sec:research_questions}

Using the matched interface defined in \cref{sec:SystemModel}, we organize the evaluation around three questions: \textbf{RQ1:} How do bandit policies differ under stochastic link success and no-disruption or benign-failure regimes? \textbf{RQ2:} How does routing performance change as disruption evolves from stochastic noise to structured and adaptive interference? \textbf{RQ3:} How do allocator policy and replay/capacity semantics change the best model choice under each threat regime?
```

## Status

Accepted by audit discussion. The intended staging point is immediately after `\section{Study Design}` in `ICNP_2026_venue_draft.tex`.
