# Item 029 — Add context for threat regimes

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:43 am  
**Feedback:**

> Add some context to what these threats are. (a few reaffirming words is fine)

## Task

Add a short setup sentence before the threat taxonomy so readers understand what the five threat regimes represent and why they are ordered from benign to adaptive/adversarial.

## Content in question

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We study routing robustness under \textbf{five escalating threat regimes} spanning benign stochasticity to intelligent reactive attacks. Each scenario modulates the availability vector
$\mathbf{A}_t = (A_t(1), \dots, A_t(4))$ according to distinct disruption semantics.
```

## Proposed solution

```tex
\subsection{Adversarial Threat Taxonomy}
\label{subsec:threats}

We study routing robustness under \textbf{five escalating threat regimes} spanning benign stochasticity, temporally correlated disruption, targeted failures, and adaptive adversarial interference. These regimes are intended to separate routine quantum-network uncertainty from increasingly structured and strategic forms of path unavailability. Each scenario modulates the availability vector
$\mathbf{A}_t = (A_t(1), \dots, A_t(4))$ according to distinct disruption semantics.
```

## Decision / status

**Approved / done.** Use the proposed short context sentence.