# Results Intro and RQ1 Audit

This document records the validated audit for the Results introductory paragraph and subsection A / RQ1.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback check added

Reviewer feedback found in the original RQ1 block:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally in this block by:

- removing `\subsubsection{Hypothesis}`;
- removing `Addresses \Cref{subsubsec:rq1_question}`;
- replacing repeated design material with a compact RQ1 evidence slice;
- removing repeated model-family lists already covered by `\cref{tab:setup-algorithm-portfolio}` and the RQ1 table;
- omitting all-dataset/all-scenario figures from RQ1 so they can be audited later with RQ2/RQ3 if needed;
- removing `RQ1a/RQ1b/RQ1c` scaffolding because the venue draft uses RQ1/RQ2/RQ3.

The broader section-level feedback about fully merging Section V and VI remains on the unresolved feedback checklist for a later structural pass unless explicitly validated for immediate application.

## Validated reduced block

```tex
\section{Results}
\label{sec:SimulationResults}

Using the matched grid defined in \cref{sec:studydesign}, we report validated master-dataset results by \cref{sec:research_questions}: RQ1 tests stochastic viability, RQ2 tests threat escalation, and RQ3 tests allocator/capacity deployment effects. GA-report observations are used only as supporting context.

% ============================================================================
% RQ1: Stochastic Routing Viability
% ============================================================================
\subsection{RQ1: Stochastic Routing Viability}
\label{subsec:rq1_answer}

\noindent\textbf{Takeaway.}
Under the Stochastic scenario in \cref{tab:scenario_specs}, contextual pursuit and epsilon-greedy baselines remain viable, while several context-free or poorly matched variants collapse. This establishes baseline viability before the structured and adaptive threats analyzed in RQ2.

\smallTitle{RQ1 evidence slice}
RQ1 uses the EXP-family, CMAB, and iCMAB master datasets, filtered to Stochastic runs under the default allocator. Results aggregate across 4K--8K horizons, $s\in\{1,1.5,2\}$, both $T$/$T_b$ replay semantics, and the 3- and 5-run suites.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{RQ1 stochastic results from the validated master datasets. Values are mean Oracle-normalized efficiency.}
\label{tab:rq1_master_stochastic}
\begin{tabular}{p{0.42\linewidth} c c c}
\toprule
\textbf{Model} & \textbf{3 runs} & \textbf{5 runs} & \textbf{Avg.} \\
\midrule
\multicolumn{4}{l}{\textit{Top tier: viable under stochastic disruption}} \\
CPursuit & 89.3 & 90.6 & \textbf{89.9} \\
CEpsilonGreedy & 87.3 & 88.4 & 87.8 \\
iCEpsilonGreedy & 87.3 & 88.4 & 87.8 \\
GNeuralUCB & 83.7 & 87.4 & 85.5 \\
\midrule
\multicolumn{4}{l}{\textit{Mid tier: degraded}} \\
EXPNeuralUCB & 81.6 & 79.6 & 80.6 \\
EXPUCB & 75.1 & 73.9 & 74.5 \\
CThompsonSampling & 65.5 & 67.9 & 66.7 \\
iCPursuit & 66.7 & 68.0 & 67.4 \\
iCThompsonSampling & 60.4 & 61.7 & 61.1 \\
\midrule
\multicolumn{4}{l}{\textit{Collapsed: structural failure}} \\
CEXP4 & 38.2 & 41.0 & 39.6 \\
CEpochGreedy & 35.6 & 38.3 & 37.0 \\
iCEpochGreedy & 35.6 & 38.3 & 37.0 \\
iCEXP4 & 35.6 & 38.3 & 37.0 \\
\bottomrule
\end{tabular}
\end{table}

\Cref{tab:rq1_master_stochastic} shows a sharp stochastic-regime split: CPursuit and epsilon-greedy contextual variants remain at or above the 85\% viability target, while CEXP4 and epoch-greedy variants collapse to roughly 37--40\%. Thus, RQ1 is answered affirmatively: stochastic decoherence alone separates viable contextual baselines from structural failures. RQ3 later disaggregates the capacity effects hidden inside this aggregate.
```

## Status

Validated by project owner.
