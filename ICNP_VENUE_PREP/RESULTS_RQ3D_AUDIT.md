# Results RQ3d Audit

This document records the validated audit for RQ3d: Scenario-Based Deployment Rules and Optimization.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- avoiding another hypothesis/back-reference structure;
- preserving the operational deployment-rule substance;
- converting the dense scenario-specific item list into a compact table;
- clarifying that the switching analysis uses the Hybrid master-dataset 3/5-suite mean, which differs from the RQ3a 3-run provenance branch;
- referencing RQ3b--RQ3c for allocator/capacity mismatch rather than repeating the full explanation;
- keeping `fig:convergence_hybrid` for second-look rather than treating it as removed.

## Figure handling

`fig:convergence_hybrid` remains on the second-look list. It may be useful as a Results learning-curve artifact, but the deployment-rule table is the primary RQ3d artifact for this pass. If included later, its caption should remove `\tiny`, reduce overclaiming, and align with the final Results narrative.

## Validated reduced block

```tex
% ============================================================================
% RQ3d: Scenario-Based Deployment Rules and Optimization
% ============================================================================
\subsection{RQ3d: Scenario-Based Deployment Rules \& Optimization}
\label{subsec:rq3d_answer}

\smallTitle{RQ3d evidence slice}
RQ3d converts the RQ3a--RQ3c findings into 6K deployment rules for iCPursuitNeuralUCB. Under the Hybrid master-dataset 3/5-suite mean used for switching analysis, the strong static default is \texttt{iCPursuitNeuralUCB + Fixed + ($T$-type, $s=2$)}, with 95.5\% average efficiency and an 88.5\% floor across scenarios. Scenario-specific switching provides modest gains, with the largest validated improvement under Adaptive disruption.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{RQ3d scenario-specific deployment rules for iCPursuitNeuralUCB at 6K. Gain is measured relative to the strong static default where applicable.}
\label{tab:rq3d_deployment_rules}
\begin{tabular}{p{0.24\linewidth} p{0.42\linewidth} c c}
\toprule
\textbf{Scenario} & \textbf{Recommended configuration} & \textbf{Eff.} & \textbf{Gain} \\
\midrule
Baseline & DynamicUCB + ($T$, $s=1$) & 99.9 & +0.0 \\
Stochastic & Thompson + ($T$, $s=1$) & 95.4 & +0.6 \\
Markov & DynamicUCB + ($T_b$, $s=1.5$) & 93.2 & +0.3 \\
Adaptive & Thompson + ($T_b$, $s=1.5$) & 95.7 & +2.9 \\
OnlineAdaptive & Fixed + ($T$, $s=2$) & 99.8 & +0.0 \\
\bottomrule
\end{tabular}
\end{table}

\Cref{tab:rq3d_deployment_rules} answers RQ3d affirmatively: clear deployment rules emerge, but the static default remains strong enough to keep all scenarios above the 85\% target at 6K. Threat-adaptive switching is most useful as a safeguard against the allocator/capacity mismatch diagnosed in RQ3b--RQ3c, with the largest validated gain under Adaptive disruption.

% Keep for second-look before final venue cleanup: hybrid convergence figure (fig:convergence_hybrid), if a visual learning-curve artifact is needed in Results.
```

## Status

Validated by project owner.
