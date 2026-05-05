# Study Design Scenario, Algorithm, Allocator, and Scope Reduction Audit

This document records the validated reduction for the remaining Study Design material beginning at `Scenario Specifications` and ending immediately before the next master section, `Simulation Results` / `Results`.

## Process requirements applied

The block was audited as four items:

1. Scenario specifications
2. Algorithm portfolio and key algorithm features
3. Qubit allocation strategies and allocator mechanisms
4. Experimental scope and statistical protocol

For each item, the audit used the project process: preserve the original meaning, split into short topic/idea subtitles, check overlap against already-audited sections, check venue requirements, reduce repeated content through references, keep tables when needed for reproducibility, and produce compile-safe venue LaTeX. The final block was validated by the project owner.

## Overlap and venue decisions

- Scenario taxonomy is not re-explained. It now references `\cref{subsec:threats}` and keeps only scenario-specific parameters.
- Algorithm families are not re-explained. The table keeps the actual portfolio because the configuration summary only lists families.
- Allocator mechanisms are not repeated in prose because System Model already defines them. The allocator table is kept because it resolves `\cref{tab:setup-allocators}` and provides the setup values.
- The four-phase list is not repeated as a full itemized list because `\cref{tab:config_summary}` already summarizes the phases. It is reduced to one scope sentence.
- Citation keys were made compile-safe for the venue draft: `NeuralTS` uses `\cite{zhang2022neuralts}`, and references to the EXPNeuralUCB paper use the available `\cite{huang2024quantum}` key.

## Validated reduced block

```tex
\smallTitle{Scenario specifications}
\Cref{tab:scenario_specs} instantiates the five threat settings defined in \cref{subsec:threats} for the matched evaluation grid.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Scenario specifications used for matched threat evaluation.}
\label{tab:scenario_specs}
\begin{tabular}{p{0.22\linewidth} p{0.62\linewidth} p{0.08\linewidth}}
\toprule
\textbf{Scenario} & \textbf{Specification} & \textbf{RQ(s)} \\
\midrule
Baseline & 0\% disruption; benign-operation reference & RQ1 \\
Stochastic & 6.25\% i.i.d. disruption~\cite{huang2024quantum} & RQ1, RQ2 \\
Markov & 25\% four-state structured disruption~\cite{huang2024quantum} & RQ2 \\
Adaptive & 25\% high-usage targeting over $w=50$ frames~\cite{huang2024quantum} & RQ2 \\
OnlineAdaptive & 25\% adaptive targeting with $\gamma=0.97$ and softmax selection~\cite{huang2024quantum} & RQ2 \\
\bottomrule
\end{tabular}
\end{table}

\smallTitle{Algorithm portfolio}
The evaluated portfolio spans classical, adversarial, contextual/neural, pursuit-based, predictive, and Oracle policies, enabling matched comparisons across architectural paradigms.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Algorithm portfolio by evaluation phase.}
\label{tab:setup-algorithm-portfolio}
\begin{tabular}{p{0.18\linewidth} p{0.24\linewidth} p{0.48\linewidth}}
\toprule
\textbf{Phase} & \textbf{Category} & \textbf{Algorithms} \\
\midrule
Phase 1 & Classical MAB & LinUCB~\cite{li2010contextual}, LinTS~\cite{agrawal2013thompson}, UCB1~\cite{auer2002finite}, Thompson Sampling~\cite{thompson1933likelihood} \\
Phase 1--2 & Adversarial & EXP3~\cite{auer2002nonstochastic}, EXPUCB~\cite{huang2024quantum}, EXPNeuralUCB~\cite{huang2024quantum} \\
Phase 2 & Contextual/Neural & GNeuralUCB, NeuralUCB~\cite{zhou2020neuralucb}, NeuralTS~\cite{zhang2022neuralts}, CEpsilonGreedy, CThompsonSampling \\
Phase 2--3 & Pursuit-based & CPursuitNeuralUCB \\
Phase 3 & Predictive & iCPursuitNeuralUCB \\
Baseline & Oracle & Perfect-information reference \\
\bottomrule
\end{tabular}
\end{table}

\smallTitle{Key algorithm features}
CPursuitNeuralUCB adds topology/channel-quality context to pursuit learning, while iCPursuitNeuralUCB adds ARIMA$(1,0,1)$ forecasts with $n\in\{50,100\}$ warmup~\cite{box2015time}. The Oracle normalizes efficiency to a perfect-information reference.

\smallTitle{Qubit allocation strategies}
Phase 3 varies the allocator policies defined in \cref{subsec:topology} and summarized in \cref{tab:config_summary} while keeping the physical budget fixed at 35 qubits.

\begin{table}[ht!]
\footnotesize
\centering
\setlength{\tabcolsep}{4pt}
\caption{Qubit allocation strategies and average efficiency across scenarios.}
\label{tab:setup-allocators}
\begin{tabular}{p{0.20\linewidth} p{0.42\linewidth} p{0.14\linewidth} p{0.14\linewidth}}
\toprule
\textbf{Allocator} & \textbf{Mechanism} & \textbf{Avg Eff.} & \textbf{Overhead} \\
\midrule
Fixed & Static distribution $(8,10,8,9)$ & 87.7\% & 1.0$\times$ \\
Thompson & Bayesian posterior sampling~\cite{thompson1933likelihood,agrawal2013thompson} & \textbf{88.2\%} & 0.3$\times$ \\
DynamicUCB & Adaptive UCB, $\lambda=2.0$~\cite{auer2002finite} & 85.3\% & 1.0$\times$ \\
Random & Uniform sampling, $\epsilon=1.0$ & 77.3\% & 1.0$\times$ \\
\bottomrule
\end{tabular}
\end{table}

\smallTitle{Experimental scope and statistical protocol}
The four phases in \cref{tab:config_summary} progress from MAB baselines to contextual/adversarial models, allocator interactions, and replay-capacity ablations. Overall, the design covers 552 unique configurations with up to 10 runs each, targeting roughly 5{,}520 episodes and about 380 A100 GPU-hours. Runs use fixed seeds with $S\in\{3,5,8,10\}$; primary results report 3- and 5-run averages.

We report Oracle-normalized efficiency,
\[
\mathrm{Eff}(\%)=\frac{\sum_{t=1}^{T} r_t}{T\theta^*}\times100,
\]
and coefficient of variation,
\[
\mathrm{CV}(\%)=\frac{\sigma(\mathrm{Eff})}{\mu(\mathrm{Eff})}\times100.
\]
Significance uses 10{,}000-sample nonparametric bootstrap confidence intervals~\cite{efron1994introduction}; differences above 5 pp with non-overlapping intervals are practically significant, and head-to-head wins require more than a 2 pp efficiency lead.
```

## Status

Validated by project owner and staged for venue-draft rebuild.
