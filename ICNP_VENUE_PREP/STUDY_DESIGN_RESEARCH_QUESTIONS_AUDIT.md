# Study Design Research Questions Reduction Audit

This document records the accepted reduction for the Study Design mini-section `Research Questions`.

## Process requirements applied

The mini-section was treated as its own section. Each idea was checked against completed sections: Abstract, Introduction, Background, Related Work, and the already-staged System Model. ICNP constraints were checked explicitly: page pressure, formal clarity, blind-submission hygiene, figure/table usefulness, and whether repeated ideas should become cross-references instead of deletions.

## Mini-section role

The Research Questions mini-section should state the questions that organize Study Design and Results. It should not answer each question in place, preview all findings again, repeat the abstract, repeat the introduction contribution bullets, or use long subsubsection blocks when a compact paragraph is sufficient.

## Split-level decisions

### Split 1: Section title and label

The title and label are useful Study Design structure and were kept.

Accepted text:

```tex
\subsection{Research Questions}
\label{sec:research_questions}
```

### Split 2: Opening role sentence

The older version introduced the RQs as a list and then split RQ2/RQ3 into subproblems. That made the section read like a checklist and created pressure to answer each RQ locally. The accepted version makes the section flow as a compact paragraph.

Accepted reduction:

```tex
We organize the evaluation around three research questions that connect routing performance, threat progression, and deployment configuration.
```

### Split 3: RQ statement paragraph

The RQ statement keeps the section question-focused while avoiding answer bullets under each RQ. It also avoids the nested bold/italic style addressed in `FORMATTING_BOLD_TEXT_REDUCTION.md`.

Accepted reduction:

```tex
\textit{RQ1 asks how classical and context-aware multi-armed bandit routing approaches perform under stochastic quantum-network conditions. RQ2 asks how bandit-based routing strategies change as network disruptions evolve from stochastic noise to structured, adaptive adversarial interference. RQ3 asks how algorithm choice, resource allocation strategy, and replay-capacity semantics interact to affect routing efficiency and stability in quantum entanglement routing.}
```

### Split 4: Collective roadmap sentence

Devroop's feedback pushed against answering each RQ in the Research Questions section. The accepted compromise adds one synthesis/roadmap sentence, not separate answers.

Accepted reduction:

```tex
Together, the findings support a threat-aware view of entanglement routing: robustness depends not only on the learning rule, but also on how allocator policy and replay-capacity semantics interact with the disruption regime.
```

## Accepted reduced mini-section

```tex
\subsection{Research Questions}
\label{sec:research_questions}

We organize the evaluation around three research questions that connect routing performance, threat progression, and deployment configuration. \textit{RQ1 asks how classical and context-aware multi-armed bandit routing approaches perform under stochastic quantum-network conditions. RQ2 asks how bandit-based routing strategies change as network disruptions evolve from stochastic noise to structured, adaptive adversarial interference. RQ3 asks how algorithm choice, resource allocation strategy, and replay-capacity semantics interact to affect routing efficiency and stability in quantum entanglement routing.} Together, the findings support a threat-aware view of entanglement routing: robustness depends not only on the learning rule, but also on how allocator policy and replay-capacity semantics interact with the disruption regime.
% \devroop{Research questions should not be answered here.} -- SOLVED: Converted the RQ section into a compact paragraph that states the primary questions and gives one collective findings-oriented roadmap sentence, while leaving detailed answers for Results and Discussion.
```

## Feedback-marker handling

If Devroop's original marker appears in the source, retain it as a LaTeX source comment and add:

```tex
% SOLVED: Converted the RQ section into a compact paragraph that states the primary questions and gives one collective findings-oriented roadmap sentence, while leaving detailed answers for Results and Discussion.
```

## Status

Accepted by audit discussion and applied to `ICNP_2026_venue_draft.tex` immediately after `\section{Study Design}`.
