# System Model Reward Model Reduction Audit

This document records the accepted reduction for the System Model mini-section originally titled `Reward Model and Link-Level Fidelity`.

## Process requirements applied

The mini-section was treated as its own section. Each paragraph was split into internal ideas, checked against the completed Abstract, Introduction, Background, and Related Work, and checked against ICNP constraints: page pressure, formal clarity, notation consistency, blind-submission hygiene, and whether repeated ideas should become cross-references rather than deletions.

The extra rule from the System Model audit was applied: before removing medium/high-overlap text, check whether it should instead become a cross-reference that connects the formal model to earlier audited sections.

## Title decision

### Original title

```tex
\subsection{Reward Model and Link-Level Fidelity}
```

### Accepted title

```tex
\subsection{Reward Model and Link Success}
```

### Rationale

The equations define link success probability, path success probability, and observed Bernoulli success rewards. They do not model full quantum-state fidelity. `Link Success` is therefore more precise than `Link-Level Fidelity`.

## Notation fix

The original text used `h_r` for hop count and also used `h_r(\mathbf{x})` for path success probability. This creates a notation conflict. The accepted version keeps `h_r` for hop count and introduces:

```tex
q_r(\mathbf{x})
```

for path success probability.

The reward equation therefore becomes:

```tex
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
```

## Paragraph 1: Probabilistic entanglement generation

### Original role

Define link-level success probability from per-attempt entanglement probability and allocated qubits/attempts.

### Split-level decisions

- **Link indexing and per-attempt probability:** kept and reduced. This is formal model content. No cross-reference needed.
- **Allocated qubits:** kept. This connects topology allocation to reward.
- **Link-level success equation:** kept and clarified by stating the independent-attempt assumption.

### Accepted recombined paragraph

```tex
\smallTitle{Probabilistic entanglement generation}
For path $P_r$ with $h_r$ links, let $p_e^{(\ell)}\in[10^{-4},2{\times}10^{-4}]$ denote the per-attempt entanglement success probability of link $\ell$, and let $x_\ell$ be the number of allocated qubits/attempts on that link during a frame. Assuming independent attempts within a frame, the link-level success probability is
\[
p_\ell(x_\ell)=1-(1-p_e^{(\ell)})^{x_\ell}.
\]
```

## Paragraph 2: Path-level success

### Original role

Define end-to-end path success as the product of link success probabilities.

### Split-level decisions

- **All links must succeed:** medium/high overlap with Background. Converted into a cross-reference to Background rather than repeated as motivation.
- **Multiplicative path success equation:** kept, with notation changed from `h_r(\mathbf{x})` to `q_r(\mathbf{x})`.
- **Hop-count penalty interpretation:** high overlap with Background. Kept as a short formal interpretation and tied to the routing model rather than repeated as tutorial prose.

### Accepted recombined paragraph

```tex
\smallTitle{Path-level success}
Consistent with the multi-hop constraint summarized in \cref{sec:Background}, path success requires all links on $P_r$ to succeed. We define path success probability as
\[
q_r(\mathbf{x})=\prod_{\ell=1}^{h_r}p_\ell(x_\ell).
\]
Thus, longer paths incur a multiplicative success penalty, while purification effects remain outside this routing model.
```

## Paragraph 3: Bernoulli rewards under adversarial availability

### Original role

Define the observed binary reward and separate stochastic link success from adversarial path availability.

### Split-level decisions

- **Reward distribution:** kept as formal model content and updated to use `q_r(\mathbf{x})`.
- **Reward variable definition:** kept and shortened.
- **Availability indicator:** kept and shortened.
- **Disruption semantics:** medium overlap with threat discussion. Converted into a forward cross-reference to the threat taxonomy subsection.
- **Separation of stochastic decoherence and strategic interference:** high overlap with Background and Related Work. Kept as a cross-reference that explains how the equation formalizes the earlier noise-versus-disruption distinction.

### Accepted recombined paragraph

```tex
\smallTitle{Bernoulli rewards under adversarial availability}
At frame $t$, selecting path $P_r$ with allocation $\mathbf{x}$ yields
\[
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
\]
Here $Y_t(r,\mathbf{x})\in\{0,1\}$ is the observed success indicator, and the availability gate $A_t(r)\in\{0,1\}$ equals 1 when path $P_r$ is available and 0 when it is disrupted. The threat regimes in \cref{subsec:threats} specify how $\mathbf{A}_t=(A_t(1),\ldots,A_t(4))$ evolves over time. This equation formalizes the noise-versus-disruption distinction used throughout \cref{sec:Background,sec:RelatedWork}: stochastic link success enters through $q_r(\mathbf{x})$, while path disruption enters through $A_t(r)$.
```

## Accepted reduced mini-section

```tex
\subsection{Reward Model and Link Success}
\label{subsec:reward}

\smallTitle{Probabilistic entanglement generation}
For path $P_r$ with $h_r$ links, let $p_e^{(\ell)}\in[10^{-4},2{\times}10^{-4}]$ denote the per-attempt entanglement success probability of link $\ell$, and let $x_\ell$ be the number of allocated qubits/attempts on that link during a frame. Assuming independent attempts within a frame, the link-level success probability is
\[
p_\ell(x_\ell)=1-(1-p_e^{(\ell)})^{x_\ell}.
\]

\smallTitle{Path-level success}
Consistent with the multi-hop constraint summarized in \cref{sec:Background}, path success requires all links on $P_r$ to succeed. We define path success probability as
\[
q_r(\mathbf{x})=\prod_{\ell=1}^{h_r}p_\ell(x_\ell).
\]
Thus, longer paths incur a multiplicative success penalty, while purification effects remain outside this routing model.

\smallTitle{Bernoulli rewards under adversarial availability}
At frame $t$, selecting path $P_r$ with allocation $\mathbf{x}$ yields
\[
Y_t(r,\mathbf{x})\sim\mathrm{Bernoulli}\!\big(q_r(\mathbf{x})A_t(r)\big).
\]
Here $Y_t(r,\mathbf{x})\in\{0,1\}$ is the observed success indicator, and the availability gate $A_t(r)\in\{0,1\}$ equals 1 when path $P_r$ is available and 0 when it is disrupted. The threat regimes in \cref{subsec:threats} specify how $\mathbf{A}_t=(A_t(1),\ldots,A_t(4))$ evolves over time. This equation formalizes the noise-versus-disruption distinction used throughout \cref{sec:Background,sec:RelatedWork}: stochastic link success enters through $q_r(\mathbf{x})$, while path disruption enters through $A_t(r)$.
```

## Status

Accepted by audit discussion and staged in the ICNP draft as the next System Model mini-section.
