# Item 044 — Add rationale for selected threat regimes

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 5:00 pm  
**Feedback:**

> Why were these regimes selected? Give a rationale, citations etc...

## Task

Explain why the five threat regimes were selected and support the design with citations.

## Content in question

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We study routing robustness under \textbf{five escalating threat regimes} spanning benign stochasticity, temporally correlated disruption, targeted failures, and adaptive adversarial interference. These regimes are intended to separate routine quantum-network uncertainty from increasingly structured and strategic forms of path unavailability. Each scenario modulates the availability vector
$\mathbf{A}_t = (A_t(1), \dots, A_t(4))$ according to distinct disruption semantics.
```

## Proposed solution

Revise the opening sentence to avoid repeated use of "benign" and add a rationale paragraph immediately after the opening paragraph:

```tex
We study routing robustness under \textbf{five escalating threat regimes} spanning no-disruption operation, independent stochastic failures, temporally correlated disruption, targeted failures, and adaptive adversarial interference. These regimes are intended to separate routine quantum-network uncertainty from increasingly structured and strategic forms of path unavailability. Each scenario modulates the availability vector
$\mathbf{A}_t = (A_t(1), \dots, A_t(4))$ according to distinct disruption semantics.

The regimes are selected to form a controlled escalation from normal operating conditions to increasingly structured and strategic disruptions. The baseline regime isolates routing and allocation behavior without path unavailability, while the stochastic and Markov regimes capture two common non-adversarial uncertainty models: independent random failures and temporally correlated outages. The adaptive and OnlineAdaptive regimes then stress-test whether policies remain robust when path unavailability is coupled to the learner's own routing behavior, which is consistent with adversarial-bandit settings where rewards or losses may be strategically selected rather than drawn from a fixed distribution~\cite{auer2002finite,auer2002nonstochastic,bubeck2012regret,lattimore2020bandit}. This design also reflects quantum-network routing concerns in which entanglement generation is probabilistic, path quality varies over time, and routing policies may need to remain stable under interference or attacker-driven disruption~\cite{wang2025learning,li2025multipath,huang2024quantum}.
```

## Decision / status

**Approved / done.** Add the rationale paragraph and revise the opening sentence.