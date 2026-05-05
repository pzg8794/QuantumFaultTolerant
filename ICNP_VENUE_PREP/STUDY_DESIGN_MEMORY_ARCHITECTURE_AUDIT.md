# Study Design Memory Architecture and Hyperparameter Table Reduction Audit

This document records the validated reduction for the Study Design block beginning at `Memory Architecture` and ending before `Scenario Specifications`.

## Process requirements applied

The block was audited using the paragraph/table workflow: show the original content, identify short topic/idea subtitles, check each topic against already-audited sections, check venue requirements, reduce each topic, recombine paragraphs, and produce a compile-safe final block. Repeated content is linked back to the already-audited System Model, Research Questions, Network configuration, and `tab:config_summary` rather than restated.

The overlap check was performed against the already-audited Abstract, Introduction, Background, Related Work, System Model, Study Design Research Questions, Experimental Design opening, Network configuration, and Time horizons/configuration summary table.

## Original content being audited

```tex
% ----------------------------------------------------------------------------
% Memory Architecture
% ----------------------------------------------------------------------------
\noindent\textit{Replay configurations (capacity scaling).}
We define the \emph{base} per-run horizon as $F_b \in \{4\text{K}, 6\text{K}, 8\text{K}\}$ frames and execute
$S \in \{3, 5, 8, 10\}$ independent runs per configuration (total of $S\cdot F_b$ frames per setting).
Some configurations apply a frame scaling to yield a \emph{current} horizon $F_c$ (the per-run frame budget for that configuration).
Replay capacity is \emph{always} expressed via a scale factor $s \in \{1, 1.5, 2\}$ (default $s=2$) in two equivalent views:
\[
T_b = s\cdot F_b,
\qquad
T   = s\cdot F_c.
\]
We sweep $s$ to analyze the \textit{Capacity Paradox} (\textbf{RQ3b})---whether larger replay memory can degrade performance under adaptive threats.
In addition to the default $s=2$ setting, we include intermediate ($s=1, 1.5$) sensitivity checks and an extended \emph{doubled-current} stress test ($2T = 2(sF_c)=4F_c$ when $s=2$), mirroring the fixed-capacity convention used in prior implementations without introducing conditional semantics.%
\cite{schaul2015prioritized,mnih2015human}

\noindent\textit{Resource separation.}
Scaling applies to replay memory; the 35-qubit physical network capacity remains invariant. This decoupling isolates learning-system constraints from quantum hardware limits.

% ----------------------------------------------------------------------------
% Threat Taxonomy Intro & Hyperparameter Table
% ----------------------------------------------------------------------------
\noindent\textit{Adversarial threat taxonomy.}
We evaluate five scenarios spanning the efficiency--security spectrum: natural stochastic decoherence, Markovian structure, and three grades of adaptive adversarial attacks (\textbf{RQ2}). This taxonomy enables controlled comparisons under matched interference regimes.%
\cite{huang2024quantum,expneural2024}

\begin{table}[ht!]
\small
\centering
\caption{Hyperparameter settings and literature justifications.}
\label{tab:setup-hyperparameters}
\begin{tabularx}{\linewidth}{l l c l}
\toprule
\textbf{Parameter} & \textbf{Algorithm} & \textbf{Value} & \textbf{Ref.} \\
\midrule
Neural LR & EXPNeuralUCB & 0.01 & \cite{expneural2024} \\
          & GNeuralUCB   & 0.2  & \cite{zhou2020neural} \\
\addlinespace[2pt]
Exp. Weight & EXPNeuralUCB & 0.05  & \cite{expneural2024} \\
            & EXPUCB       & 0.005 & Tuned \\
\addlinespace[2pt]
Pursuit LR & Pursuit family & 0.2 & \cite{thathachar2011networks} \\
\addlinespace[2pt]
UCB Explore & DynamicAlloc & 2.0 & \cite{auer2002finite} \\
\addlinespace[2pt]
ARIMA ($n$) & iCPursuit & 50, 100 & \cite{box2015time} \\
Replay ($T_b,T$) & All & $T_b=sF_b$ & \cite{schaul2015prioritized,mnih2015human} \\
 &  & $T=sF_c$ & \\
\bottomrule
\end{tabularx}
\end{table}
```

## Paragraph 1 topics / ideas

1. Base horizon and run count
2. Current horizon
3. Replay-capacity semantics
4. Capacity-paradox sweep
5. Sensitivity and stress tests

## Paragraph 1 decisions

- Keep the base/current horizon distinction because it defines the replay capacity equations.
- Keep independent run counts for reproducibility.
- Keep the replay equations because they are the core semantics of the mini-section.
- Replace `RQ3b` with `RQ3` to align with the audited Research Questions section.
- Keep the sensitivity/stress-test statement, but compress it and cite replay-buffer practice.

Validated reduction:

```tex
\smallTitle{Replay configurations (capacity scaling)}
We distinguish the base horizon $F_b\in\{4\mathrm{K},6\mathrm{K},8\mathrm{K}\}$ from the current horizon $F_c$ used after frame scaling, and evaluate $S\in\{3,5,8,10\}$ independent runs per configuration. Replay memory is scaled by $s\in\{1,1.5,2\}$, with default $s=2$, under two semantics:
\[
T_b=sF_b,\qquad T=sF_c.
\]
The $s$ sweep, intermediate sensitivity checks, and doubled-current stress test probe the RQ3 capacity-paradox question: when added replay memory helps estimation versus when it increases adversarial predictability~\cite{schaul2015prioritized,mnih2015human}.
```

## Paragraph 2 topics / ideas

1. Replay-memory scaling only
2. Learning-system versus hardware separation

Validated reduction:

```tex
\smallTitle{Resource separation}
Replay scaling changes only classical memory: the physical network budget remains fixed at 35 qubits as defined in \cref{subsec:topology} and summarized in \cref{tab:config_summary}. This separates learning-system memory effects from quantum hardware limits.
```

## Paragraph 3 topics / ideas

1. Five-scenario threat span
2. Matched interference comparison

Validated reduction:

```tex
\smallTitle{Adversarial threat taxonomy}
The five threat settings follow \cref{subsec:threats} and \cref{tab:config_summary}; the scenario-specific parameters below instantiate the matched-interference comparison~\cite{huang2024quantum,expneural2024}.
```

## Table decisions

- Keep the hyperparameter table because it supports reproducibility.
- Change `DynamicAlloc` to `DynamicUCB` for consistency with the audited System Model and configuration summary table.
- Compress replay semantics into one row.
- Replace `tabularx` with standard `tabular` because the venue draft does not load `tabularx`.

Validated table:

```tex
\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Hyperparameter settings and literature justifications.}
\label{tab:setup-hyperparameters}
\begin{tabular}{p{0.22\linewidth} p{0.25\linewidth} p{0.18\linewidth} p{0.20\linewidth}}
\toprule
\textbf{Parameter} & \textbf{Algorithm} & \textbf{Value} & \textbf{Ref.} \\
\midrule
Neural LR & EXPNeuralUCB & 0.01 & \cite{expneural2024} \\
          & GNeuralUCB   & 0.2  & \cite{zhou2020neural} \\
\addlinespace[2pt]
Exp. Weight & EXPNeuralUCB & 0.05  & \cite{expneural2024} \\
            & EXPUCB       & 0.005 & Tuned \\
\addlinespace[2pt]
Pursuit LR & Pursuit family & 0.2 & \cite{thathachar2011networks} \\
\addlinespace[2pt]
UCB Explore & DynamicUCB & 2.0 & \cite{auer2002finite} \\
\addlinespace[2pt]
ARIMA ($n$) & iCPursuit & 50, 100 & \cite{box2015time} \\
\addlinespace[2pt]
Replay semantics & All & $T_b=sF_b$, $T=sF_c$ & \cite{schaul2015prioritized,mnih2015human} \\
\bottomrule
\end{tabular}
\end{table}
```

## Validated reduced block

```tex
% ----------------------------------------------------------------------------
% Memory Architecture
% ----------------------------------------------------------------------------
\smallTitle{Replay configurations (capacity scaling)}
We distinguish the base horizon $F_b\in\{4\mathrm{K},6\mathrm{K},8\mathrm{K}\}$ from the current horizon $F_c$ used after frame scaling, and evaluate $S\in\{3,5,8,10\}$ independent runs per configuration. Replay memory is scaled by $s\in\{1,1.5,2\}$, with default $s=2$, under two semantics:
\[
T_b=sF_b,\qquad T=sF_c.
\]
The $s$ sweep, intermediate sensitivity checks, and doubled-current stress test probe the RQ3 capacity-paradox question: when added replay memory helps estimation versus when it increases adversarial predictability~\cite{schaul2015prioritized,mnih2015human}.

\smallTitle{Resource separation}
Replay scaling changes only classical memory: the physical network budget remains fixed at 35 qubits as defined in \cref{subsec:topology} and summarized in \cref{tab:config_summary}. This separates learning-system memory effects from quantum hardware limits.

% ----------------------------------------------------------------------------
% Threat Taxonomy Intro & Hyperparameter Table
% ----------------------------------------------------------------------------
\smallTitle{Adversarial threat taxonomy}
The five threat settings follow \cref{subsec:threats} and \cref{tab:config_summary}; the scenario-specific parameters below instantiate the matched-interference comparison~\cite{huang2024quantum,expneural2024}.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Hyperparameter settings and literature justifications.}
\label{tab:setup-hyperparameters}
\begin{tabular}{p{0.22\linewidth} p{0.25\linewidth} p{0.18\linewidth} p{0.20\linewidth}}
\toprule
\textbf{Parameter} & \textbf{Algorithm} & \textbf{Value} & \textbf{Ref.} \\
\midrule
Neural LR & EXPNeuralUCB & 0.01 & \cite{expneural2024} \\
          & GNeuralUCB   & 0.2  & \cite{zhou2020neural} \\
\addlinespace[2pt]
Exp. Weight & EXPNeuralUCB & 0.05  & \cite{expneural2024} \\
            & EXPUCB       & 0.005 & Tuned \\
\addlinespace[2pt]
Pursuit LR & Pursuit family & 0.2 & \cite{thathachar2011networks} \\
\addlinespace[2pt]
UCB Explore & DynamicUCB & 2.0 & \cite{auer2002finite} \\
\addlinespace[2pt]
ARIMA ($n$) & iCPursuit & 50, 100 & \cite{box2015time} \\
\addlinespace[2pt]
Replay semantics & All & $T_b=sF_b$, $T=sF_c$ & \cite{schaul2015prioritized,mnih2015human} \\
\bottomrule
\end{tabular}
\end{table}
```

## Status

Validated by project owner and ready for staging and venue-draft rebuild.
