# Related Work Consolidation for Graph Space

This note records the Related Work reduction applied after final graph creation was marked blocked.

## Trigger

The May 6 discussion identified that the Related Work section used more space than needed, especially around bandits and online learning. The team noted that reducing the overlapping Related Work material could free space for final graphs.

## Accepted task

Consolidate overlapping Related Work material while preserving key citations and direct comparison against this paper.

Targeted topics:

```text
online learning
multi-armed bandits
contextual bandits
adversarial bandits
quantum routing comparisons
```

## Applied flow

The active Related Work now uses a tighter three-part flow:

1. Prior quantum-routing work
2. Bandit policies for routing decisions
3. Matched robustness-evaluation gap

This keeps the contrast that matters for the ICNP venue draft: prior work establishes online path selection and bandit-style routing, but does not jointly vary threat regime, allocator policy, and replay/capacity semantics under a matched evaluation grid.

## What was reduced

The edit removes long tutorial explanations of MAB, contextual bandits, adversarial bandits, and predictive bandits. It keeps the taxonomy but expresses it compactly through citation groups.

The edit also merges the previous separate subsections:

```text
Foundational, Contextual, and Hybrid Bandits
Quantum Network Routing with Online Learning
Benchmarking and Robustness Evaluation
```

into compact `\smallTitle{...}` paragraphs. This reduces vertical space compared with separate subsections and leaves more room for Results figures.

## Citation preservation

The consolidated section preserves the core citation groups:

- quantum-network foundations and entanglement routing constraints
- online quantum path selection and quantum routing comparisons
- stochastic, contextual/neural, adversarial, pursuit, and predictive bandit foundations
- EXPNeuralUCB as the closest comparator
- benchmarking/utility evaluation and best-of-both-worlds robustness framing

## Validation checklist

- [x] Related Work length reduced.
- [x] Key citations preserved in compact groups.
- [x] Direct comparison against this work preserved.
- [x] Long tutorial explanations of bandits removed.
- [x] Gap statement now emphasizes matched threat, allocator, and replay/capacity evaluation.
- [x] No final graph form was chosen or generated while the graph-choice task remains blocked.

## Active manuscript path

Applied to:

```tex
02--related_works.tex
```

This file is included by:

```tex
ICNP_2026_venue_draft.tex
```
