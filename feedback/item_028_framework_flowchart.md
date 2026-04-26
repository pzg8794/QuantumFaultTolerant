# Item 028 — Replace placeholder flowchart with evaluation-framework flowchart

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:42 am  
**Feedback:**

> Would it make sense to include a flowchart in here? WHat I have is obvioulsy wrong, but you get the idea

## Task

Replace the current placeholder flowchart, which appears to describe an unrelated cryptography learning activity, with a paper-specific flowchart that summarizes the threat-aware quantum-routing evaluation pipeline.

## Content in question

```tex
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% Start the flow chart %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\tikzstyle{rrec} = [rectangle, draw, fill=white!20, text width=7.5em, text centered, rounded corners, minimum height=2.7em]
\tikzstyle{arrow} = [thick,->,>=stealth]
\tikzstyle{line} = [draw, -latex']

\begin{figure}[h!]
\footnotesize
\scalebox{.86}{
\begin{tikzpicture}[node distance = 2.5cm, line width=.5mm]

\node [rrec] (Background) {Background};
\node [rrec, right of=Background] (Encrypt) {Create Encrypted Text};
\node [rrec, right of=Encrypt] (Classical) {Observe Classical Breaking};
\node [rrec, right of=Classical] (Quantum) {Observe Quantum Breaking};

% Forward arrows
\draw [arrow] (Background) -- (Encrypt);
\draw [arrow] (Encrypt) -- (Classical);
\draw [arrow] (Classical) -- (Quantum);

% Feedback arrow using only straight segments
\draw [arrow] (Quantum.south) -- ++(0,-.25) --  node[midway, below] {Iterations for each encryption method (\ie Cesar, Vigenère, RSA)} ($(Encrypt.south)+(0,-.25)$) -- (Encrypt.south);

\end{tikzpicture}
}
\caption{Flow of the cryptography learning activity.}
\label{fig:LabProcess-Flowchart}
\end{figure}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% End the flow chart %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

## Proposed solution

Replace the placeholder with a compact flowchart aligned to the paper's evaluation pipeline:

```tex
\begin{figure}[t]
\centering
\footnotesize
\begin{tikzpicture}[
    node distance=1.5cm,
    box/.style={rectangle, draw, rounded corners, align=center, minimum width=2.1cm, minimum height=0.75cm, text width=2.0cm},
    arrow/.style={thick,->,>=stealth}
]
\node[box] (topology) {Quantum network\topology};
\node[box, right=of topology] (threats) {Threat\taxonomy};
\node[box, right=of threats] (policies) {Bandit policy\families};
\node[box, below=of policies] (allocators) {Allocator and\capacity settings};
\node[box, left=of allocators] (metrics) {Oracle-normalized\metrics};
\node[box, left=of metrics] (guidance) {Robustness and\deployment guidance};

\draw[arrow] (topology) -- (threats);
\draw[arrow] (threats) -- (policies);
\draw[arrow] (policies) -- (allocators);
\draw[arrow] (allocators) -- (metrics);
\draw[arrow] (metrics) -- (guidance);
\end{tikzpicture}
\caption{Threat-aware evaluation pipeline for quantum entanglement routing. The framework combines network topology, threat regimes, bandit policy families, allocator and replay-capacity settings, and Oracle-normalized metrics to identify robust deployment choices.}
\label{fig:framework}
\end{figure}
```

## Decision / status

Pending Piter review.
