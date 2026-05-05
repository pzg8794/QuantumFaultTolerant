# Results RQ3c Audit

This document records the validated audit for RQ3c: Algorithm-Allocator Co-Design.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- removing `\subsubsection{Hypothesis}`;
- removing `Addresses \Cref{subsubsec:rq3c_question}`;
- replacing repeated design detail with a compact RQ3c evidence slice;
- preserving the allocator-independence hypothesis as a focus statement;
- keeping the validated table values because this table is the primary RQ3c evidence artifact;
- table-referencing the conclusion rather than repeating all row values in prose.

## Validated reduced block

```tex
% ============================================================================
% RQ3c: Algorithm-Allocator Co-Design
% ============================================================================
\subsection{RQ3c: Algorithm-Allocator Co-Design}
\label{subsec:rq3c_answer}

\noindent\textbf{Focus.}
RQ3c tests whether allocator choice is independent of algorithm architecture or instead acts as a first-class deployment decision.

\smallTitle{RQ3c evidence slice}
RQ3c fixes the model to iCPursuitNeuralUCB, the horizon to 6K, and capacity to $T$-type with $s=2$, then varies allocator policy. This isolates allocator effects after RQ3b isolates replay-scale behavior.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{3pt}
\caption{RQ3c allocator interaction for iCPursuitNeuralUCB under the fixed 6K, $T$-type, $s=2$ deployment. Values are Hybrid master-dataset means over the 3- and 5-run suites.}
\label{tab:rq3c_master_allocators}
\begin{tabular}{lccccccc}
\toprule
\textbf{Allocator} & \textbf{Bl} & \textbf{Sh} & \textbf{Mk} & \textbf{Ag} & \textbf{OA} & \textbf{Avg.} & \textbf{Floor} \\
\midrule
Fixed      & 99.9 & 94.6 & 94.7 & 88.5 & 99.8 & 95.5 & 88.5 \\
DynamicUCB & 85.0 & 89.5 & 88.9 & 88.5 & 97.1 & 89.8 & 85.0 \\
Random     & 95.1 & 94.5 & 96.3 & 88.5 & 83.5 & 91.6 & 83.5 \\
Thompson   & 58.4 & 65.4 & 87.8 & 91.7 & 65.2 & 73.7 & 58.4 \\
\bottomrule
\end{tabular}

{\footnotesize Bl=Baseline, Sh=Stochastic, Mk=Markov, Ag=Adaptive, OA=OnlineAdaptive.}
\end{table}

\Cref{tab:rq3c_master_allocators} shows that allocator effects are deployment-critical: Fixed gives iCPursuitNeuralUCB the best average and floor, while Thompson is strong under Adaptive but fragile under Baseline/Stochastic mismatch. Thus, allocator selection is a first-class deployment decision.
```

## Status

Validated by project owner.
