# System Model Reduction Audit for ICNP Draft

This document records the mini-section-by-mini-section reduction process for the System Model section in the ICNP venue draft.

## Venue and process requirements

System Model is treated as a sequence of mini-sections because it is large and critical. Each subsection is audited as if it were its own section.

For every System Model mini-section, the process is:

1. identify the original paragraph role;
2. split that paragraph into internal ideas;
3. check each split against completed sections: Abstract, Introduction, Background, and Related Work;
4. check ICNP constraints: page pressure, formal clarity, figure/caption usefulness, blind-submission hygiene, and whether the text preserves core evaluation claims without repeating earlier sections;
5. choose one of: keep, reduce, reference/connect to earlier section, move later, or remove;
6. recombine the accepted reduced text;
7. apply only after approval.

## Additional rule: reference before removal

When a split has medium or high overlap with an already-audited section, we do not remove it automatically. First, we ask whether the repeated idea can become a useful cross-reference or connective sentence. If referencing an earlier section helps readers see the big picture, we keep a short connective sentence rather than deleting the idea outright.

## System Model opening and figure

### Original role

The opening introduced quantum routing as a sequential decision problem, listed the components formalized by System Model, and positioned the formulation relative to prior work. The figure showed the per-frame routing loop.

### Split-level decisions

- **Joint sequential decision problem:** high overlap with Abstract, Introduction, and Background. Reduced into formal notation rather than motivational prose.
- **What the section formalizes:** low overlap and central to System Model. Kept and tightened.
- **Prior-work positioning:** high overlap with Related Work. Converted into a cross-reference to Background and Related Work so the formal variables instantiate the dimensions already discussed.
- **Figure:** kept. The Introduction figure describes the evaluation framework, while the System Model figure describes the per-frame routing loop.
- **Caption:** tightened to introduce frame notation and reduce repeated explanation.

### Accepted reduced text

```tex
\section{System Model}
\label{sec:SystemModel}

At each decision frame $t$, a routing agent selects a candidate path $P_r$ and qubit-allocation vector $\mathbf{x}$ under uncertain link success and path availability. The model defines the topology, reward and availability process, threat regimes, allocator policies, and bandit interface used in the evaluation. These variables instantiate the routing, allocation, and threat dimensions discussed in \cref{sec:Background,sec:RelatedWork}, turning those dimensions into a concrete evaluation interface.
```

### Accepted reduced caption

```tex
\caption{System-model loop. At frame $t$, the agent observes path context, selects a path and qubit allocation, interacts with the threat-conditioned network, and updates from reward feedback.}
```

## Network Topology and Path Structure

### Original role

This mini-section defines the canonical topology, candidate path set, hop counts, fixed qubit budget, allocator policy set, feasible allocation vector, and context space.

### Paragraph 1: topology and candidate paths

#### Split-level decisions

- **Topology definition:** kept and reduced. Removed personal node names while preserving source, destination, and repeater roles.
- **Candidate path set:** kept. This is core formal setup.
- **Path enumeration:** kept but compressed from bullets into inline form to reduce page pressure.
- **Hop notation:** kept. Needed for reward model.
- **Shorter/longer path tradeoff:** medium/high overlap with Background. Converted into a connective sentence referencing Background rather than deleting the idea.

#### Accepted recombined paragraph

```tex
\smallTitle{4-node diamond topology}
We use a four-node diamond topology with source $S$, destination $D$, and two intermediate repeaters. It yields four candidate paths $\mathcal{P}=\{P_1,P_2,P_3,P_4\}$ with two- and three-hop alternatives: $P_1=S{\to}B{\to}D$, $P_2=S{\to}C{\to}D$, $P_3=S{\to}B{\to}C{\to}D$, and $P_4=S{\to}C{\to}B{\to}D$. Each path $P_r$ has hop count $h_r$, with $h_1=h_2=2$ and $h_3=h_4=3$; each hop denotes one adjacent entanglement link. This topology instantiates the path-length and routing-allocation tradeoffs introduced in \cref{sec:Background}, while keeping the path set small enough for controlled matched-regime evaluation.
```

### Paragraph 2: qubit budget and allocator policies

#### Split-level decisions

- **Fixed budget:** kept. Exact experimental condition.
- **Allocator strategy set:** kept and formalized.
- **Allocator rationale:** reduced. Reviewers need the reason for the policy set, but not extended motivation already covered in earlier sections.
- **Enumerated allocator details:** kept but compressed from a vertical list into a semicolon sentence to reduce page pressure.
- **Allocator connection:** medium overlap with Abstract, Introduction, Background, and Related Work. Added a short cross-reference to Related Work so readers see these policies instantiate the deployment-configuration dimension identified earlier.

#### Accepted recombined paragraph

```tex
\smallTitle{Qubit budget and allocator policies}
The canonical 4-path internal topology uses a fixed baseline budget of 35 qubits distributed across paths. This 35-qubit setting defines the controlled system model in this section, not a global limit of the broader framework, which also supports topology-specific budgets for external testbeds. We evaluate four allocator policies---Fixed, ThompsonSampling, DynamicUCB, and Random---spanning static, uncertainty-aware, optimistic, and uninformed allocation behavior. Fixed uses $(T_1,T_2,T_3,T_4)=(8,10,8,9)$; ThompsonSampling samples path utilities from posterior estimates; DynamicUCB redistributes capacity using upper-confidence estimates; and Random assigns capacity uniformly as a control. These allocator choices instantiate the deployment-configuration dimension identified in \cref{sec:RelatedWork}.
```

### Paragraph 3: feasible allocation and context space

#### Split-level decisions

- **Feasible allocation definition:** kept. This is formal model content.
- **Scaling motivation:** medium overlap with Introduction, Background, and Related Work. Kept briefly because it connects formal context-space growth to the need for structure-aware approximation.

#### Accepted recombined paragraph

```tex
For path $P_r$ with budget $T_r$, a feasible allocation is $\mathbf{x}=(x_1,\ldots,x_{h_r})$ with $\sum_{\ell=1}^{h_r}x_\ell=T_r$, defining context space $\mathcal{X}_r$. For three-hop paths this space grows combinatorially, motivating structure-aware approximation.
```

## Accepted reduced mini-section

```tex
\subsection{Network Topology and Path Structure}
\label{subsec:topology}

\smallTitle{4-node diamond topology}
We use a four-node diamond topology with source $S$, destination $D$, and two intermediate repeaters. It yields four candidate paths $\mathcal{P}=\{P_1,P_2,P_3,P_4\}$ with two- and three-hop alternatives: $P_1=S{\to}B{\to}D$, $P_2=S{\to}C{\to}D$, $P_3=S{\to}B{\to}C{\to}D$, and $P_4=S{\to}C{\to}B{\to}D$. Each path $P_r$ has hop count $h_r$, with $h_1=h_2=2$ and $h_3=h_4=3$; each hop denotes one adjacent entanglement link. This topology instantiates the path-length and routing-allocation tradeoffs introduced in \cref{sec:Background}, while keeping the path set small enough for controlled matched-regime evaluation.

\smallTitle{Qubit budget and allocator policies}
The canonical 4-path internal topology uses a fixed baseline budget of 35 qubits distributed across paths. This 35-qubit setting defines the controlled system model in this section, not a global limit of the broader framework, which also supports topology-specific budgets for external testbeds. We evaluate four allocator policies---Fixed, ThompsonSampling, DynamicUCB, and Random---spanning static, uncertainty-aware, optimistic, and uninformed allocation behavior. Fixed uses $(T_1,T_2,T_3,T_4)=(8,10,8,9)$; ThompsonSampling samples path utilities from posterior estimates; DynamicUCB redistributes capacity using upper-confidence estimates; and Random assigns capacity uniformly as a control. These allocator choices instantiate the deployment-configuration dimension identified in \cref{sec:RelatedWork}.

For path $P_r$ with budget $T_r$, a feasible allocation is $\mathbf{x}=(x_1,\ldots,x_{h_r})$ with $\sum_{\ell=1}^{h_r}x_\ell=T_r$, defining context space $\mathcal{X}_r$. For three-hop paths this space grows combinatorially, motivating structure-aware approximation.
```

## Current staged status

- System Model opening and loop caption accepted.
- `Network Topology and Path Structure` accepted.
- Next pending mini-section: `Reward Model and Link-Level Fidelity`.
