# Results RQ3/C Intro Audit

This document records the validated audit for the RQ3 introductory block, stopping before RQ3a.

## Process requirements applied

The audit followed the project process: original content, topic/idea split, overlap check, feedback check, venue check, decision, reduced version, and further reduced version where possible. No content was applied before validation.

## Feedback checks applied

Prior reviewer feedback kept active for this audit:

```tex
\shee{Instead of referring to Section V, combine sections V and VI into 1 section. These 2 sections are redundant}
```

Applied locally by:

- removing `\subsubsection{Hypothesis}`;
- removing `Addresses \Cref{subsubsec:rq3d_question}`;
- replacing repeated experimental-design detail with a compact RQ3 evidence slice;
- keeping the RQ3-specific caveat that CV values are computed across scenario means because per-run variance is unavailable in the Hybrid master table;
- preserving the validated RQ3 answer and the key static-configuration numbers.

## Figure handling

These figures are not treated as removed. They are marked for a second-look pass because they may belong in later RQ3 sub-analyses:

- `fig:threat_rules`: keep for second-look, likely with RQ3 allocator/deployment-rule discussion.
- `fig:capacity_all`: keep for second-look, likely with RQ3b capacity-paradox discussion.

If either figure is included later, its caption should be revised to remove `\tiny`, reduce overclaiming, and align with the relevant subsection.

## Validated reduced block

```tex
% ============================================================================
% RQ3: Deployment Optimization
% ============================================================================
\subsection{RQ3: Deployment Optimization}
\label{subsec:rq3}

\noindent\textbf{Takeaway.}
RQ3 evaluates whether algorithm, allocator, and replay-capacity choices should change with the threat regime. Deployment is configuration-sensitive, but the hybrid dataset also reveals a strong static configuration that exceeds the 85\% robustness target across all five scenarios.

\smallTitle{RQ3 evidence slice}
RQ3 uses the validated Hybrid master dataset for CPursuitNeuralUCB, iCPursuitNeuralUCB, GNeuralUCB, and EXPNeuralUCB across all scenarios, allocators, replay anchoring types, scales $s\in\{1,1.5,2\}$, and 4K--8K horizons. Point estimates average the 3- and 5-run suites; RQ3 CV values are computed across scenario means as a deployment-volatility proxy because per-run variance is not available in the master table.

\smallTitle{Validated RQ3 answer}
Deployment is configuration-sensitive, but the Hybrid master dataset also reveals a strong static configuration. At the 6K horizon, \texttt{iCPursuitNeuralUCB + Fixed + ($T$-type, $s=2$)} achieves a 96.0\% global average and a 92.8\% worst-case floor across scenarios, using the validated mean over 3- and 5-run suites. Scenario-specific optima still differ, so later RQ3 analyses disaggregate allocator and replay-capacity effects.

% Keep for second-look before final venue cleanup: threat-adaptive allocator figure (fig:threat_rules) and capacity--efficiency figure (fig:capacity_all). The latter likely belongs with RQ3b.
```

## Status

Validated by project owner.
