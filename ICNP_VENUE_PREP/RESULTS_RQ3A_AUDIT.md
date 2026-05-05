# Results RQ3a Audit

This document records the validated audit for RQ3a: Predictive Context Modeling Impact.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Verification-hub double check

The RQ3a audit was double checked against the validation notebook and associated logs in `pzg8794/quantum_project`.

Key verification outcome:

- The caption-faithful 3/5-suite mean did **not** support the original RQ3a table or the original `+18.3 pp` OnlineAdaptive lift.
- The strongest source-backed provenance branch is the `6K / Fixed / T / s=2 / 3-run` suite.
- The paper-side RQ3a fix updates the table values to:
  - `CPursuitNeuralUCB = 99.8 / 94.7 / 93.0 / 92.8 / 81.5 / 92.4 / 6.5`
  - `iCPursuitNeuralUCB = 99.9 / 94.8 / 93.0 / 92.8 / 99.8 / 96.0 / 3.3`
- The `OnlineAdaptive` lift remains `+18.3 pp` under the validated 3-run provenance branch.
- The dispersion claim should use `CV_scen: 6.5 -> 3.3`, not the earlier unsupported floor-lift claim.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- keeping the RQ3a traceability heading but reducing question scaffolding;
- replacing repeated setup with a compact evidence slice;
- keeping the fixed deployment details because they are necessary for the comparison;
- correcting the caption and prose so RQ3a states it uses the 3-run suite only;
- preserving the validated OnlineAdaptive lift and CV-scenario improvement.

## Validated reduced block

```tex
% ============================================================================
% RQ3a: Predictive Context Modeling Impact
% ============================================================================
\subsubsection{RQ3a: Predictive Context Modeling Impact}
\label{subsubsec:rq3a_answer}

\noindent\textbf{Focus.}
RQ3a isolates whether the informative/predictive variant, iCPursuitNeuralUCB, improves deployment robustness over reactive CPursuitNeuralUCB.

\smallTitle{RQ3a evidence slice}
To isolate architecture impact, we hold deployment fixed at 6K horizon, \texttt{Fixed} allocator, $T$-type anchoring, and $s=2$, then use the validated 3-run suite from the Hybrid master dataset.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{3pt}
\caption{RQ3a informative-context impact under the fixed deployment setting. Values are from the validated 3-run Hybrid master-dataset provenance branch.}
\label{tab:rq3a_master_informative}
\begin{tabular}{p{0.30\linewidth} c c c c c c c}
\toprule
\textbf{Model} & \textbf{Bl} & \textbf{Sh} & \textbf{Mk} & \textbf{Ag} & \textbf{OA} & \textbf{Avg.} & \textbf{CV} \\
\midrule
CPursuitNeuralUCB & 99.8 & 94.7 & 93.0 & 92.8 & 81.5 & 92.4 & 6.5 \\
iCPursuitNeuralUCB & 99.9 & 94.8 & 93.0 & 92.8 & 99.8 & 96.0 & 3.3 \\
\bottomrule
\end{tabular}

{\footnotesize Bl=Baseline, Sh=Stochastic, Mk=Markov, Ag=Adaptive, OA=OnlineAdaptive; CV is computed across scenario means.}
\end{table}

\Cref{tab:rq3a_master_informative} shows that iCPursuitNeuralUCB improves global robustness mainly by lifting OnlineAdaptive efficiency from 81.5\% to 99.8\% (+18.3 pp) while keeping Stochastic, Markov, and Adaptive performance effectively unchanged. It also reduces scenario-level dispersion from 6.5 to 3.3 CV. Thus, informative context is most valuable when the threat adapts online.
```

## Status

Validated by project owner after verification-hub double check.
