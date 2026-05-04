# Study Design Experimental Design Reduction Audit

This document records the accepted reduction for Paragraph 1 of the Study Design mini-section `Experimental Design`.

## Process requirements applied

The paragraph was audited using the paragraph-level process requested for the ICNP venue draft: show the original paragraph, identify short topic/idea subtitles per sentence, check each sentence against already-audited sections, check venue requirements, reduce each sentence, recombine the paragraph, and run a final paragraph-level reduction. No text is staged unless validated by the project owner.

The overlap check was performed against the already-audited Abstract, Introduction, Background, Related Work, System Model, and Study Design Research Questions. Repeated content was handled by cross-referencing previously audited sections when useful, rather than repeating motivation.

## Staging target

The accepted paragraph belongs immediately after:

```tex
\section{Study Design}
\label{sec:studydesign}
```

and before the already-staged Research Questions mini-section.

## Paragraph 1 original

```tex
This section specifies the experimental design used to evaluate adaptive quantum entanglement routing under stochastic and adversarial interference, and ties each configuration axis to the research questions. \Cref{tab:config_summary} consolidates design dimensions, tested options, and the corresponding RQ coverage.
```

## Paragraph 1 topics / ideas

1. Experimental-design purpose and RQ mapping
2. Configuration-summary table

## Topic/Idea 1 -- Experimental-design purpose and RQ mapping

Original sentence:

```tex
This section specifies the experimental design used to evaluate adaptive quantum entanglement routing under stochastic and adversarial interference, and ties each configuration axis to the research questions.
```

Overlap check:

- Abstract: medium -- already frames evaluation under noisy/adversarial conditions.
- Introduction: high -- already introduces the threat-aware framework and matched configuration axes.
- Background: medium -- already motivates routing under uncertainty.
- Related Work: medium -- already motivates matched evaluation across threat/allocator/replay assumptions.
- System Model: high -- already defines routing interface, threat regimes, allocators, and reward setup.
- Research Questions: high -- already states the questions the axes answer.

Venue check:

Reduce and reference. Keep the purpose, but connect it to already-audited `System Model` and `Research Questions` instead of repeating stochastic/adversarial motivation.

Decision:

Reduce.

Accepted reduction:

```tex
This section uses the interface in \cref{sec:SystemModel} to define the configuration axes used to answer \cref{sec:research_questions}.
```

## Topic/Idea 2 -- Configuration-summary table

Original sentence:

```tex
\Cref{tab:config_summary} consolidates design dimensions, tested options, and the corresponding RQ coverage.
```

Overlap check:

- Abstract: none.
- Introduction: low -- the framework figure is conceptual, but not a configuration table.
- Background: none.
- Related Work: none.
- System Model: medium -- table likely summarizes variables defined there.
- Research Questions: high -- table directly maps dimensions to RQ coverage.

Venue check:

Keep, lightly reduce. This table reference helps readers connect the design grid to the RQs without extra prose.

Decision:

Lightly reduce.

Accepted reduction:

```tex
\Cref{tab:config_summary} summarizes the design dimensions, tested options, and RQ coverage.
```

## Paragraph 1 recombined reduced paragraph

```tex
This section uses the interface in \cref{sec:SystemModel} to define the configuration axes used to answer \cref{sec:research_questions}. \Cref{tab:config_summary} summarizes the design dimensions, tested options, and RQ coverage.
```

## Paragraph 1 further reduced paragraph

Accepted for staging:

```tex
\subsection{Experimental Design}
\label{sec:expDesign}

Using the interface in \cref{sec:SystemModel}, this section defines the configuration axes used to answer \cref{sec:research_questions}. \Cref{tab:config_summary} summarizes the design dimensions, tested options, and RQ coverage.
```

## Status

Validated by project owner and ready for staging in `ICNP_2026_venue_draft.tex`.
