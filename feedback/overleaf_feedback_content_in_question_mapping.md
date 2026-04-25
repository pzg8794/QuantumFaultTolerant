# Overleaf Feedback — Content in Question Mapping

**Source:** Pasted by Piter in ChatGPT on 2026-04-25.  
**Purpose:** Preserve the content-in-question snippets exactly in the order/labels supplied before applying solutions.  
**Important reconciliation note:** The existing queue has 67 feedback items, while this content mapping uses grouped labels, extends to label 75, and includes a duplicate label `22`. Do not destructively merge this into the queue until the mapping is reconciled.

---

## Content 001

```tex
\section{Related Work}
```

## Content 002

```tex
\subsection{Literature Selection Methodology}
```

## Content 003

```tex
We conducted a targeted literature search spanning 2002--2025 across arXiv, IEEE Xplore, and the ACM Digital Library, using keyword combinations covering quantum routing, entanglement distribution, and bandit-based online decision-making across stochastic, adversarial, contextual, predictive, and hybrid variants.
```

## Content 004

```tex
We excluded offline optimization and control approaches without online bandit feedback, single-domain demonstrations that do not generalize algorithmically, and tuning-only studies lacking methodological novelty, clearly stated assumptions, or reproducibility artifacts, because our goal is to compare lines of work that differ in learning assumptions, not catalog all quantum-network optimization methods.
```

## Content 005-006

```tex
Contrastingly, in our study we use these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement 
```

## Content 007

```tex
Wang \etal~\cite{wang2025learning} focus on learning high-quality paths under stochastic dynamics, while Li et al.
```

## Content 008

```tex
In contrast, we do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees;
```

## Content 009

```tex
In contrast, we do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees; 
```

## Content 010

```tex
Further, while Huang et al. ~\cite{huang2024quantum} treat allocation as a fixed component,
```

## Content 011

```tex
\subsection{Quantum Network Routing with Bandits}
```

## Content 012-013

```tex
Contrastingly, in our study we use these canonical stochastic and adversarial bandit algorithms as matched-condition baseline families inside a unified threat taxonomy for entanglement routing:
```

## Content 014

```tex
Wang \etal~\cite{wang2025learning} focus on learning high-quality paths under stochastic dynamics, while Li et al.
```

## Content 015

```tex
In contrast, we do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees; 
```

## Content 016

```tex
In contrast, we do not propose a new quantum-network routing protocol or a new budgeted-control formulation with analytical guarantees; rather, we provide a controlled robustness characterization that isolates which algorithm--allocator--capacity combinations remain stable when disruption is structured or adaptive.
```

## Content 017

```tex
Further, while Huang et al. ~\cite{huang2024quantum} treat allocation as a fixed component,
```

## Content 018

```tex
\subsection{Toward a Modular, Universal Bandit Stack}
```

## Content 019

```tex
% Piter
% Jie
% Jie Student
% Sheeraja
% Travis
% Devroop
% Dan
```

## Content 020-021-022

```tex
Existing routing approaches frequently assume stationary link behavior, decouple selection from allocation, or rely on offline optimization assumptions that can fail when link fidelities drift and disruptions adapt online.
```

## Content 022 duplicate

```tex
This work provides a systematic threat-aware evaluation framework and uses it to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit--neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.
```

## Content 023

```tex
Unlike existing work that fixes allocator policy and replay semantics as background constants, our framework treats them as first-class experimental variables, enabling direct attribution of robustness to the algorithm--allocator--capacity triad.
```

## Content 024

```tex
We found that neural hybrids outperform non-contextual baselines by 18–24 percentage points in scenario-aggregated efficiency across thirteen evaluated algorithms and five threat regimes. They also emerge as the most robust family, sustaining worst-case performance floors above 85\% under stochastic threats and remaining more stable under strategic adaptive attacks than adversarial-first EXP3-style designs.
```

## Content 025

```tex
We found that neural hybrids outperform non-contextual baselines by 18–24 percentage points in scenario-aggregated efficiency across thirteen evaluated algorithms and five threat regimes. They also emerge as the most robust family, sustaining worst-case performance floors above 85\% under stochastic threats and remaining more stable under strategic adaptive attacks than adversarial-first EXP3-style designs. We further identified a \emph{capacity paradox}: increasing replay capacity improves efficiency under structured (Markov) disruption yet induces efficiency collapses of 22–30 percentage points under adaptive adversaries, revealing that resource predictability, not bandwidth, is the dominant robustness constraint.
```

## Content 026-027

```tex
We further validate these robustness trends through cross-testbed evaluation on three external quantum network simulators, showing consistent behavior across diverse topologies and noise models while exposing scale- and physics-dependent performance limitations.
```

## Content 028-029

```tex
All project observations and source code are available on public repository at \url{https://github.com/pzg8794/quantum_project_hub}. 
```

## Content 030

```tex
\section{Introduction}
```

## Content 031

```tex
Quantum routing also differs fundamentally from classical packet switching routing because the underlying resource is \emph{entanglement}, not transferable data~\cite{}.
```

## Content 032

```tex
Quantum states cannot be copied or amplified due to the no-cloning theorem~\cite{wootters1982single}, so classical store-and-forward buffering does not apply. 
```

## Content 033

```tex
Existing quantum routing studies have proposed important mechanisms for online path selection, benchmarking-driven routing, and adversarially robust learning. However, they are often evaluated under incompatible assumptions about threat processes, topology visibility, allocator policy, or replay/memory semantics, making direct comparisons difficult and weakening deployment guidance~\cite{liu2024qbgp,li2025multipath,chaudhary2023quantum}. 
```

## Content 034

```tex
This leaves a \emph{matched-threat evaluation gap}: A lack of a controlled view of when contextual structure is truly necessary, when adversarial robustness dominates, and how allocator policy and replay-capacity semantics alter apparent routing performance. 
```

## Content 035

```tex
\subsection{Our Approach and Evaluation Scope}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Start the flow chart %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\tikzstyle{rrec} = [rectangle, draw, fill=white!20, text width=7.5em, text centered, rounded corners, minimum height=2.7em]
\tikzstyle{arrow} = [thick,->,>=stealth]
\tikzstyle{line} = [draw, -latex']
```

## Content 036

```tex
To close these matched-threat evaluation gaps, we introduce a unified framework that systematically compares adversarial-first (EXP3-family), stochastic/contextual-first (CMAB/iCMAB-family), and hybrid models, including pursuit--neural variants and EXPNeuralUCB~\cite{huang2024quantum}, under a shared threat taxonomy. The evaluation pipeline is illustrated in \cref{fig:framework}. 
```

## Content 037

```tex
Within this framework, context-aware pursuit--neural hybrids achieve the strongest robustness--efficiency tradeoff, while replay capacity exhibits a threat-dependent \emph{capacity paradox}: increasing replay capacity can improve routing efficiency under structured disruption while degrading performance under adaptive attacks. 
```

## Content 038-039-040

```tex
To summarize, this work makes the following contributions:
\begin{itemize}

    \item \descStep{Threat-aware evaluation framework}{We introduce a unified evaluation framework for quantum entanglement routing that systematically compares classical, contextual, adversarial, and hybrid bandit policies for joint path selection and qubit allocation under matched threat conditions.}

    \item \descStep{Coupled design dimensions and capacity paradox}{We show that robustness is governed not only by the learning rule, but by the interaction among \emph{algorithm choice, allocator policy, and replay-capacity semantics}. Within this formulation, we identify a threat-dependent \emph{capacity paradox}, where increased replay capacity improves performance under structured disruption yet degrades efficiency under adaptive adversaries.}

    \item \descStep{Cross-testbed validation and deployment insights}{We validate our findings across multiple external quantum-network testbeds, demonstrating consistent trends and distilling deployment oriented guidance for selecting model  allocator capacity combinations under varying threat regimes.}

    \item \descStep{Joint decision formulation for quantum routing}{We formalize quantum routing as a coupled decision problem over path selection, qubit allocation, and learning under uncertainty, treating learning, allocation, and capacity as interdependent design dimensions rather than independent implementation choices.}
    
    \item \descStep{Open Source Repository}{All source code and datasets are publicly available to enable reproducibility, validation, and further development by the research community~\cite{}.}

%    \item \descStep{XX}{X}
%    \item \descStep{XX}{X}
\end{itemize}
```

## Content 041

```tex
%The \hl{XXX} code repo and data is publicly available on our project repository~\cite{}.
```

## Content 042-043

```tex
%The \hl{XXX} code repo and data is publicly available on our project repository~\cite{}. 
```

## Content 044-045

```tex
\section{Background}
```

## Content 046

```tex
\subsection{Problem Scope}
"Motivated by the joint effects of allocator strategy and capacity semantics on routing performance, stability, and predictability, we study how modeling choices (\eg contextual vs.\ adversarial vs.\ predictive), allocator design, and replay-capacity configuration jointly determine routing robustness under diverse threat regimes."
```

## Content 047-048

```tex
\section{System Model}
\label{sec:SystemModel}

% We model quantum entanglement routing as a sequential decision problem...

We model quantum entanglement routing as a sequential decision problem where an agent must jointly optimize (1) \textbf{Path selection} among candidate routes, and (2) \textbf{Qubit allocation} across path segments, under uncertain link fidelities and adversarial interference. This section formalizes the network topology, reward structure, threat taxonomy, qubit allocation policies, and the underlying MAB formulation.
```

## Content 049

```tex
We model quantum entanglement routing as a sequential decision problem where an agent must jointly optimize (1) \textbf{Path selection} among candidate routes, and (2) \textbf{Qubit allocation} across path segments, under uncertain link fidelities and adversarial interference. This section formalizes the network topology, reward structure, threat taxonomy, qubit allocation policies, and the underlying MAB formulation.
```

## Content 050

```tex
\smallTitle{Qubit budget and allocator policies}
The network operates under a \textbf{fixed total budget of 35 qubits} distributed across paths. We evaluate \textbf{four allocator strategies} that dynamically or statically assign qubits:
\begin{enumerate}
\item \textbf{Fixed} ($T_1{=}8, T_2{=}10, T_3{=}8, T_4{=}9$): static baseline
\item \textbf{ThompsonSampling}: Bayesian posterior sampling over path utilities
\item \textbf{DynamicUCB}: upper-confidence-bound-driven capacity redistribution
\item \textbf{Random}: uniform random assignment (control baseline)
\end{enumerate}
For each path $P_r$ with session budget $T_r$, a \textbf{feasible allocation} $\mathbf{x} = (x_1, \dots, x_{h_r})$ satisfying $\sum_{\ell=1}^{h_r} x_\ell = T_r$ defines the context space $\mathcal{X}_r$. This combinatorial space scales quadratically for 3-hop paths, motivating contextual neural approximation.
```

## Content 051

```tex
\smallTitle{Probabilistic entanglement generation}
Each path $P_r$ contains $h_r$ links indexed by $\ell \in \{1, \ldots, h_r\}$. For each link $\ell$, let $p_e^{(\ell)} \in [10^{-4}, 2{\times}10^{-4}]$ denote its per-attempt entanglement success probability (representative of realistic SNSPD-based quantum memory systems), and let $x_\ell$ denote the number of qubits allocated to that link. Over a decision step (frame), allocating $x_\ell$ qubits yields \textbf{link-level success probability}
\devroop{Define $p_\ell$}
```

## Content 052

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We study routing robustness under \textbf{five escalating threat regimes} spanning benign stochasticity to intelligent reactive attacks. Each scenario modulates the availability vector
$\mathbf{A}_t = (A_t(1), \dots, A_t(4))$ according to distinct disruption semantics.

\textbf{Baseline (No Disruption).}
In the baseline regime, all routes remain available at all times: $A_t(r)=1$ for all $r,t$.
This setting isolates pure stochastic decoherence and serves as the \textbf{benign-condition upper bound} (Oracle-aligned) for comparisons across all disrupted regimes.

\textbf{Stochastic (6.25\% i.i.d. failures).}
Under stochastic disruption, each route is independently available according to $A_t(r)\sim\mathrm{ Bernoulli}(0.9375)$.
This captures benign environmental noise without temporal structure or memory.

\textbf{Markov (25\% structured disruption).}
In the Markov regime, availability is governed by a \textbf{4-state Markov chain} whose states modulate path-failure probabilities.
This setting captures bursty, correlated outages, with an average disruption rate of approximately $25\%$.
```

## Content 053

```tex
\textbf{Stochastic (6.25\% i.i.d. failures).}
Under stochastic disruption, each route is independently available according to $A_t(r)\sim\mathrm{ Bernoulli}(0.9375)$.
This captures benign environmental noise without temporal structure or memory.
```

## Content 054

```tex
This setting mimics intelligent adversaries that \textbf{learn and adapt in real time}, representing the hardest realistic threat model in our taxonomy.
```

## Content 055

```tex
$\rightarrow$ \emph{Capacity semantics} (\eg $T$ vs. $T_b$, replay scale $s$; \S\ref{subsec:capacity})
```

## Content 056

```tex
\subsection{Research Questions}
\label{sec:research_questions}

% All quantitative ranges are computed from the \textbf{validated}
% (\texttt{experimental results}) using the \textbf{3- and 5-run suites}. Core findings \textbf{exclude the Random allocator}
% (which we report separately) to properly compare against other papers. Furthermore, we reference extended observations obtained throughout the development of our experiments that are yet to be validated with current framework.
% \vspace{0.25em}
\devroop{You should just mention your primary research questions. The answers to your questions should a part of your results and observations.}
```

## Content 057

```tex
\noindent Our study addresses three core questions about stochastic decoherence impact, adversarial robustness, and deployment tradeoffs in algorithm--allocator--capacity selection.
% BLOCKED (Needs Dan approval; no action until instructed): \devroop{Wont it make more sense to just relay the questions here and answer them in the results and discussion section?}
```

## Content 058

```tex
\subsubsection*{\emph{\textbf{RQ1}}}
```

## Content 059

```tex
legend style={at={(0.5,-0.22)}, anchor=north},
```

## Content 060

```tex
\subsubsection*{\emph{RQ2}}
\label{subsubsec:rq2_question}
```

## Content 061

```tex
\emph{How do different bandit-based routing strategies perform as network disruptions evolve from stochastic noise to structured and adaptive adversarial interference?}
```

## Content 062-063

```tex
\caption{Worst-case robustness separates the model families: context-aware methods retain higher floors than adversarial-first baselines at the default $2T$--$2T_b$ budget.}
```

## Content 064

```tex
legend style={font=\scriptsize}
```

## Content 065

```tex
legend style={font=\scriptsize},
```

## Content 066

```tex
\item \textbf{Paper 2 Testbed}~\cite{chaudhary2023quantum}: Large-scale stochastic-noise quantum communication testbed for learning-based route selection. 15-node, 51-edge topology with 8 routing paths.
```

## Content 067-068

```tex
\devroop{Dont simply mention Paper [X]. use the exact reference. Same for table XI, XII, XIII}
```

## Content 069-070

```tex
\textbf{Bandit Family} & \textbf{Algorithm} & \textbf{Avg Eff (\%)} & \textbf{Gap (\%)} & \textbf{Floor (\%)} & \textbf{Exp. Winner} \\
```

## Content 071

```tex
Remaining stress sweeps (\eg 10-run) will be reported in a follow-up technical report and integrated into the reproducibility artifacts accompanying this paper.
```

## Content 072-073

```tex
\subsection{Future Work}

\Cref{sec:testbed_comparison}
```

## Content 074

```tex
Across the curated evaluation corpus and accompanying reproducibility artifacts, context-aware pursuit--neural hybrids (\eg \small\texttt{CPursuitNeuralUCB}, \small\texttt{iCPursuitNeuralUCB}) consistently define the efficiency--stability frontier, achieving near-Oracle behavior under stochastic noise while avoiding brittle failure modes observed in adversarial-first EXP3-style designs under reactive threats.
```

## Content 075

```tex
\section{Reproducibility Artifacts}
\label{app:data_artifacts}
All quantitative statements in this paper are anchored to the curated evaluation corpus generated by our framework.
```
