# Study Design Network Configuration Reduction Audit

This document records the validated reduction for the Study Design mini-section `Network configuration`.

## Process requirements applied

The section was audited using the project paragraph-level workflow: show the original content, identify short topic/idea subtitles per paragraph, check each topic against already-audited sections, check venue requirements, reduce each topic, recombine the paragraph, and then further reduce the paragraph. Repeated material was handled through cross-references to already-audited content when that helped readers connect the paper's pieces.

The overlap check was performed against the already-audited Abstract, Introduction, Background, Related Work, System Model, Study Design Research Questions, and the staged Experimental Design opening paragraph. The topology figure is kept as part of the validated reduction.

## Original section being audited

```tex
% ----------------------------------------------------------------------------
% Network Configuration
% ----------------------------------------------------------------------------
\paragraph*{Network configuration}
We use a 4-node quantum network with four alternative paths connecting source $S$ to destination $D$ via repeater nodes (\Cref{fig:network_topology}). Paths $P_1$ and $P_4$ have two hops, while $P_2$ and $P_3$ have three hops, matching common small-scale quantum-network architectures and demonstrations~\cite{wehner2018quantum,pompili2021realization} \shee{$P_1$ and $P_2$ have 2 hops while $P_3$ and $P_4$ have 3 hops}. This topology provides sufficient action-space complexity for bandit learning~\cite{huang2024quantum,dai2020quantum} while keeping exhaustive cross-product sweeps tractable (hundreds of algorithm--scenario--allocator configurations; see \Cref{tab:config_summary}).

Total physical network capacity is fixed at 35 qubits across all experiments, representing resource-constrained early-stage deployments~\cite{simon2017towards}. This induces non-trivial exploration--exploitation tradeoffs: algorithms cannot over-provision all paths. Per-path allocations are determined by the allocator (\Cref{tab:setup-allocators}), enabling controlled comparison of static versus adaptive resource management.
```

## Paragraph 1 original

```tex
We use a 4-node quantum network with four alternative paths connecting source $S$ to destination $D$ via repeater nodes (\Cref{fig:network_topology}). Paths $P_1$ and $P_4$ have two hops, while $P_2$ and $P_3$ have three hops, matching common small-scale quantum-network architectures and demonstrations~\cite{wehner2018quantum,pompili2021realization} \shee{$P_1$ and $P_2$ have 2 hops while $P_3$ and $P_4$ have 3 hops}. This topology provides sufficient action-space complexity for bandit learning~\cite{huang2024quantum,dai2020quantum} while keeping exhaustive cross-product sweeps tractable (hundreds of algorithm--scenario--allocator configurations; see \Cref{tab:config_summary}).
```

## Paragraph 1 topics / ideas

1. Topology and hop counts
2. Action-space complexity and tractability

## Topic/Idea 1 -- Topology and hop counts

Original sentences:

```tex
We use a 4-node quantum network with four alternative paths connecting source $S$ to destination $D$ via repeater nodes (\Cref{fig:network_topology}). Paths $P_1$ and $P_4$ have two hops, while $P_2$ and $P_3$ have three hops, matching common small-scale quantum-network architectures and demonstrations~\cite{wehner2018quantum,pompili2021realization} \shee{$P_1$ and $P_2$ have 2 hops while $P_3$ and $P_4$ have 3 hops}.
```

Overlap check:

- Abstract: none.
- Introduction: medium -- topology is part of the evaluation framework, but this specific topology is not described there.
- Background: medium -- discusses multi-hop quantum routing generally, not this testbed.
- Related Work: low.
- System Model: high -- `\cref{subsec:topology}` already defines the four-node diamond topology and path structure.
- Research Questions: low.
- Experimental Design paragraph 1: medium -- it says Study Design defines configuration axes, but not this concrete topology.

Venue check:

Keep and reference. This is a concrete experimental-design setting, and the figure must remain. Correct the hop-count error so $P_1$ and $P_2$ are two-hop paths and $P_3$ and $P_4$ are three-hop paths. Remove the internal `\shee{}` comment.

Decision:

Reduce, correct, and keep the topology figure reference.

Validated reduction:

```tex
We use the four-path diamond topology shown in \cref{fig:network_topology} and defined in \cref{subsec:topology}, with two-hop paths $P_1$ and $P_2$ and three-hop paths $P_3$ and $P_4$.
```

## Topic/Idea 2 -- Action-space complexity and tractability

Original sentence:

```tex
This topology provides sufficient action-space complexity for bandit learning~\cite{huang2024quantum,dai2020quantum} while keeping exhaustive cross-product sweeps tractable (hundreds of algorithm--scenario--allocator configurations; see \Cref{tab:config_summary}).
```

Overlap check:

- Abstract: low.
- Introduction: medium -- introduces matched evaluation but not the tractability reason for the topology.
- Background: medium -- says allocation/action spaces can become combinatorial.
- Related Work: medium -- supports bandit learning context.
- System Model: medium/high -- already says the topology keeps the path set small enough for matched-regime evaluation.
- Research Questions: medium -- tractability makes the RQ grid feasible.
- Experimental Design paragraph 1: medium -- table maps dimensions/options/RQs.

Venue check:

Keep the justification, but reduce. This sentence explains why the topology is not arbitrary. Keep the `\Cref{tab:config_summary}` reference to connect topology choice to the experimental grid.

Decision:

Reduce.

Validated reduction:

```tex
This topology keeps the routing action space nontrivial while preserving tractable cross-product sweeps across \cref{tab:config_summary}.
```

## Paragraph 1 further reduced paragraph

Validated for staging:

```tex
We use the four-path diamond topology shown in \cref{fig:network_topology} and defined in \cref{subsec:topology}, with two-hop paths $P_1$ and $P_2$ and three-hop paths $P_3$ and $P_4$. This topology keeps the routing action space nontrivial while preserving tractable cross-product sweeps across \cref{tab:config_summary}.
```

## Paragraph 2 original

```tex
Total physical network capacity is fixed at 35 qubits across all experiments, representing resource-constrained early-stage deployments~\cite{simon2017towards}. This induces non-trivial exploration--exploitation tradeoffs: algorithms cannot over-provision all paths. Per-path allocations are determined by the allocator (\Cref{tab:setup-allocators}), enabling controlled comparison of static versus adaptive resource management.
```

## Paragraph 2 topics / ideas

1. Fixed capacity and resource pressure
2. Allocator-controlled resource management

## Topic/Idea 1 -- Fixed capacity and resource pressure

Original sentences:

```tex
Total physical network capacity is fixed at 35 qubits across all experiments, representing resource-constrained early-stage deployments~\cite{simon2017towards}. This induces non-trivial exploration--exploitation tradeoffs: algorithms cannot over-provision all paths.
```

Overlap check:

- Abstract: medium -- mentions scarce quantum resources but not the 35-qubit budget.
- Introduction: medium -- says allocator/capacity choices alter routing performance.
- Background: high -- already says routing couples path choice with allocation and scarce resources.
- Related Work: medium -- discusses resource-control assumptions across prior work.
- System Model: high -- `\cref{subsec:topology}` already states the fixed 35-qubit budget.
- Research Questions: high -- RQ3 asks how allocator and replay/capacity semantics change model choice.
- Experimental Design paragraph 1: medium -- this is one of the configuration axes.

Venue check:

Keep both ideas together. The fixed budget alone is not enough; the important reason is that it creates the exploration--exploitation pressure by preventing over-provisioning. Do not separate them in a way that loses the causal relationship.

Decision:

Combine and reduce.

Validated reduction:

```tex
Across all experiments, the total physical budget remains fixed at 35 qubits, matching the resource constraint in \cref{subsec:topology}; this prevents over-provisioning and creates the intended exploration--exploitation pressure.
```

## Topic/Idea 2 -- Allocator-controlled resource management

Original sentence:

```tex
Per-path allocations are determined by the allocator (\Cref{tab:setup-allocators}), enabling controlled comparison of static versus adaptive resource management.
```

Overlap check:

- Abstract: medium -- allocator policy is already named as a first-class factor.
- Introduction: high -- allocator choices are part of the threat-aware framework.
- Background: high -- allocator strategy is framed as central to routing robustness.
- Related Work: high -- prior work is compared partly by allocator assumptions.
- System Model: high -- allocator policies are defined in `\cref{subsec:topology}`.
- Research Questions: high -- RQ3 directly concerns allocator/capacity effects.
- Experimental Design paragraph 1: medium.

Venue check:

Keep and cross-reference. This sentence connects fixed resource pressure to the allocator comparison. Keep `\Cref{tab:setup-allocators}` because it gives readers the concrete allocator options.

Decision:

Reduce lightly.

Validated reduction:

```tex
Per-path budgets are set by allocator policies in \cref{tab:setup-allocators}, enabling controlled comparison of static and adaptive resource management.
```

## Paragraph 2 further reduced paragraph

Validated for staging:

```tex
Across all experiments, the total physical budget remains fixed at 35 qubits, matching the resource constraint in \cref{subsec:topology}; this prevents over-provisioning and creates the intended exploration--exploitation pressure. Per-path budgets are set by allocator policies in \cref{tab:setup-allocators}, enabling controlled comparison of static and adaptive resource management.
```

## Figure decision

The topology figure is kept. Remove the commented-out caption line and revise the caption so it describes what the figure shows while noting that per-path budgets vary by allocator policy.

Validated caption:

```tex
\caption{Four-path quantum-network testbed used for routing evaluation. Paths $P_1$ and $P_2$ have two hops, while $P_3$ and $P_4$ have three hops; per-path qubit budgets are varied by allocator policy.}
\label{fig:network_topology}
```

## Validated reduced section

```tex
\paragraph*{Network configuration}
We use the four-path diamond topology shown in \cref{fig:network_topology} and defined in \cref{subsec:topology}, with two-hop paths $P_1$ and $P_2$ and three-hop paths $P_3$ and $P_4$. This topology keeps the routing action space nontrivial while preserving tractable cross-product sweeps across \cref{tab:config_summary}.

Across all experiments, the total physical budget remains fixed at 35 qubits, matching the resource constraint in \cref{subsec:topology}; this prevents over-provisioning and creates the intended exploration--exploitation pressure. Per-path budgets are set by allocator policies in \cref{tab:setup-allocators}, enabling controlled comparison of static and adaptive resource management.
```

## Status

Validated by project owner and ready for staging in `ICNP_2026_venue_draft.tex`.
