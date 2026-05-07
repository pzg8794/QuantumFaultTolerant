# Formatting Bold Text Reduction

This note records the resolution for pending Item 046:

```text
Dan: I think that you're overdoing it with all of the bold text
```

## Scope

This is a formatting cleanup, not a content rewrite. The accepted rule is:

```text
Keep bold for short structural labels only. Remove bold from explanatory prose, long phrases, and repeated emphasis inside paragraphs.
```

## Applied change

The active ICNP venue draft had nested bold-inside-emphasis formatting for supporting research questions in `\subsection{Research Questions}`:

```tex
\emph{\textbf{RQ2a}: Do context-aware routing policies outperform baseline policies under stochastic disruption, and do they maintain this advantage under structured and adaptive threat regimes?}
```

This was converted to lighter italic-only formatting:

```tex
\noindent\textit{RQ2a. Do context-aware routing policies outperform baseline policies under stochastic disruption, and do they maintain this advantage under structured and adaptive threat regimes?}
```

The same pattern was applied to:

- RQ2a
- RQ2b
- RQ3a
- RQ3b
- RQ3c
- RQ3d

## Intentionally left bold

Bold was intentionally retained for short structural labels where it improves scanning or is standard table formatting:

- Main RQ labels in the Introduction: `\textbf{RQ1.}`, `\textbf{RQ2.}`, `\textbf{RQ3.}`
- Short references such as `\textbf{RQ2}` and `\textbf{RQ3}` in prose
- Table headers such as `\textbf{Scenario}` or `\textbf{Configuration Dimension}`
- Existing macros such as `\RQOne`, `\RQTwo`, and `\RQThree`, which are short structural labels

## Feedback-marker handling

The active ICNP venue draft did not contain Dan's feedback marker inline. The feedback exists in the historical feedback queue. If the original marker is reintroduced during a review pass, keep it as a LaTeX source comment and add:

```tex
% SOLVED: Reduced bold emphasis to short structural labels only; converted long bold/emphasized RQ text to lighter italic formatting.
```

## Validation checklist

- [x] Long nested bold/italic RQ question lines were simplified.
- [x] Content wording was not changed.
- [x] Short structural bold labels were retained.
- [x] Table/header bold formatting was retained.
- [x] The formatting rule is documented for future passes.
