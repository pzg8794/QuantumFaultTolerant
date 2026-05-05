# Results RQ3b Audit

This document records the validated audit for RQ3b: Replay Capacity Scaling and Paradox.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- removing `\subsubsection{Hypothesis}`;
- removing `Addresses \Cref{subsubsec:rq3b_question}`;
- replacing repeated design details with a compact RQ3b evidence slice;
- keeping the RQ3b-specific fixed setting because it is necessary to isolate replay-scale behavior;
- preserving the validated master-dataset table values;
- keeping `fig:capacity_all` for second-look rather than treating it as removed.

## Figure handling

`fig:capacity_all` remains on the second-look list. It likely belongs with RQ3b if a visual capacity-paradox artifact is needed, but the validated table is the primary source-backed evidence for this pass. If the figure is included later, its caption should remove `\tiny`, reduce overclaiming, and align with the RQ3b table.

## Validated reduced block

```tex
% ============================================================================
% RQ3b: Replay Capacity Scaling and Paradox
% ============================================================================
\subsection{RQ3b: Replay Capacity Scaling \& Paradox}
\label{subsec:rq3b_answer}

\noindent\textbf{Focus.}
RQ3b tests whether larger replay scale improves robustness or creates a threat-dependent capacity paradox.

\smallTitle{RQ3b evidence slice}
RQ3b fixes the allocator to \texttt{Random}, the horizon to 6K, and the replay anchoring to $T$-type, then varies $s\in\{1,1.5,2\}$ using Hybrid master-dataset means over the 3- and 5-run suites. This isolates replay-scale behavior before allocator co-design is analyzed in RQ3c.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{3pt}
\caption{RQ3b capacity scaling under fixed \texttt{Random} allocation, 6K horizon, and $T$-type replay anchoring. Values are Hybrid master-dataset means over the 3- and 5-run suites.}
\label{tab:rq3b_master_capacity_scaling}
\begin{tabular}{p{0.30\linewidth} c c c c c c c}
\toprule
\textbf{Model} & \textbf{$s$} & \textbf{Bl} & \textbf{Sh} & \textbf{Mk} & \textbf{Ag} & \textbf{OA} & \textbf{Avg.} \\
\midrule
CPursuitNeuralUCB & 1.0 & 94.7 & 93.8 & 89.3 & 88.5 & 81.5 & 89.6 \\
                  & 1.5 & 45.8 & 77.1 & 51.5 & 88.5 & 69.0 & 66.4 \\
                  & 2.0 & 96.3 & 94.9 & 95.9 & 88.5 & 84.5 & 92.0 \\
\midrule
iCPursuitNeuralUCB & 1.0 & 92.1 & 93.6 & 88.7 & 88.5 & 70.8 & 86.7 \\
                   & 1.5 & 56.1 & 73.2 & 42.2 & 88.5 & 83.5 & 68.7 \\
                   & 2.0 & 95.1 & 94.5 & 96.3 & 88.5 & 83.5 & 91.6 \\
\bottomrule
\end{tabular}

{\footnotesize Bl=Baseline, Sh=Stochastic, Mk=Markov, Ag=Adaptive, OA=OnlineAdaptive.}
\end{table}

\Cref{tab:rq3b_master_capacity_scaling} shows that replay scale is not a monotonic ``more is better'' knob. Under fixed \texttt{Random} allocation and $T$-type anchoring, both pursuit-based hybrids degrade sharply at $s=1.5$ and recover at $s=2$, confirming that replay capacity must be tuned jointly with allocator and anchoring type. Extended GA ablations remain supporting evidence, but the master-dataset trend is the validated RQ3b conclusion.

% Keep for second-look before final venue cleanup: capacity--efficiency figure (fig:capacity_all), likely with RQ3b if a visual capacity-paradox artifact is needed.
```

## Status

Validated by project owner.
