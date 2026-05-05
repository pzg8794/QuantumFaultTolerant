# Results RQ2/B Audit

This document records the validated audit for Results subsection B / RQ2.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- removing `\subsubsection{Hypothesis}`;
- removing `Addresses \Cref{subsubsec:rq2_question}`;
- replacing repeated experimental-design details with a compact RQ2 evidence slice;
- preserving the substance of the RQ2 setup while reducing redundancy;
- keeping the direct RQ2 answer but folding it into the interpretation paragraph.

Table-specific feedback/checks applied:

- The old `Win Rate` / `Win Share` wording was corrected to `Win Dominance`.
- `Win Dominance` is defined in the caption as each displayed model's share of aggregated scenario wins among the four representatives under the locked Markov/Adaptive/OnlineAdaptive scope.
- Corrected Win Dominance values are: CPursuit 25.6, iCEpsilonGreedy 43.9, EXPNeuralUCB 30.5, and EXP3/UCB 0.0.

## Second-look items explicitly not decided as final removals

The project owner requested that these not be treated as permanently omitted yet:

- Original paragraph 1 / opening RQ2 setup: revised and preserved in substance, not discarded.
- Figure 2 / robustness frontier (`fig:floor`): not inserted into the reduced venue block yet, but flagged for second-look because it may still be useful as visual support for the floor/mean/peak robustness claim.
- Original supporting question answers (`RQ2a/RQ2b/RQ2c`): not inserted into the reduced venue block yet, but flagged for second-look because they may still be useful if explicit sub-question traceability is needed.

## Validated reduced block

```tex
% ============================================================================
% RQ2: Robustness Under Adaptive Threats
% ============================================================================
\subsection{RQ2: Robustness Under Adaptive Threats}
\label{subsec:rq2_answer}

\noindent\textbf{Takeaway.}
Under Markov, Adaptive, and OnlineAdaptive threats, contextual and informed policies maintain stronger robustness floors than EXP-family adversarial-first baselines. This extends RQ1 from stochastic viability to adaptive disruption.

\smallTitle{RQ2 evidence slice}
RQ2 uses the Markov, Adaptive, and OnlineAdaptive threat slice from \cref{tab:scenario_specs}, restricted to the default allocator and aggregated across 4K--8K horizons, $s\in\{1,1.5,2\}$, both $T$/$T_b$ replay semantics, and the 3- and 5-run suites. The table reports the strongest CMAB and iCMAB representatives together with two EXP-family adversarial baselines.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{RQ2 adversarial-scope results. Win Dominance is each displayed model's share of aggregated scenario wins among the four representatives under the locked Markov/Adaptive/OnlineAdaptive scope.}
\label{tab:rq2_adversarial}
\begin{tabular}{p{0.30\linewidth} c c c c}
\toprule
\textbf{Algorithm} & \textbf{Avg.} & \textbf{CV} & \textbf{Floor} & \textbf{Win Dom.} \\
\midrule
CPursuit & \textbf{88.1} & 5.3 & 77.4 & 25.6 \\
iCEpsilonGreedy & 86.9 & \textbf{3.6} & \textbf{81.0} & \textbf{43.9} \\
EXPNeuralUCB & 82.4 & 16.5 & 18.0 & 30.5 \\
EXP3/UCB & 76.3 & 6.0 & 68.8 & 0.0 \\
\bottomrule
\end{tabular}
\end{table}

\Cref{tab:rq2_adversarial} refutes the adversarial-first hypothesis: CPursuit leads average efficiency, iCEpsilonGreedy provides the strongest stability floor, and EXPNeuralUCB remains fragile despite adversarial exploration. Thus, RQ2 is answered affirmatively: structured and adaptive threats expose stability gaps not visible in RQ1, and adversarial-first EXP-family baselines do not dominate the locked adversarial scope.

% Second-look candidates before final venue cleanup: robustness frontier figure (fig:floor) and explicit RQ2a/RQ2b/RQ2c supporting-answer bullets.
```

## Status

Validated by project owner with second-look caveats.
