# ICNP Reviewer Expectations and Pitfalls

## What ICNP reviewers are likely to care about

ICNP is a network-protocols venue. Reviewers will likely evaluate whether the paper advances understanding of network protocols, network control, routing, robustness, or systems behavior.

For this paper, the strongest reviewer-facing claim is not simply that one bandit algorithm wins. The stronger claim is:

> Quantum entanglement routing robustness is governed by the interaction among learning rule, allocator policy, replay/capacity semantics, and threat process; evaluating these dimensions under matched conditions changes deployment guidance.

## Positive signals to strengthen

### 1. Networking problem first

Start from the routing/control failure mode:

- entanglement is probabilistic;
- path availability changes;
- allocator decisions alter feedback and predictability;
- adaptive adversaries can exploit repeated routing patterns.

Then introduce bandits as the control abstraction.

### 2. Clear system model

The system model should quickly answer:

- What is a path?
- What is a decision round?
- What does the learner observe?
- What does it choose?
- What reward/feedback is available?
- What does the adversary affect?
- What is the role of allocator/capacity semantics?

### 3. Systematic experiment design

ICNP reviewers will not like arbitrary scenario choices. Keep explicit rationales for:

- five threat regimes;
- four allocator strategies;
- replay/capacity scales;
- selected external testbeds;
- selected baselines.

### 4. Strong baselines and ablations

Make sure the paper shows:

- stochastic/contextual baselines;
- adversarial baselines;
- hybrid/neural policies;
- allocator comparisons;
- capacity/replay comparisons;
- cross-testbed validation.

### 5. Deployment takeaway

End results sections with actionable conclusions:

- when contextual structure helps;
- when adversarial methods are insufficient;
- when replay capacity becomes harmful;
- how allocator choice changes robustness.

## Common pitfalls

### Pitfall: Looks like an ML benchmark paper

Fix: Put routing, control, threat model, and deployment guidance in the foreground. Keep algorithm details concise.

### Pitfall: Too much quantum background

Fix: Keep only the quantum facts needed to understand why entanglement routing differs from classical packet routing.

### Pitfall: Too much related work

Fix: Reduce related work to a focused comparison table/paragraphs. Move methodology or broad taxonomy to appendix.

### Pitfall: Double-blind violation

Fix: Remove repo/Drive links, acknowledgments, author names, author macros, and identifying project references.

### Pitfall: Core claims depend on appendices

Fix: Main paper must contain enough evidence to support every major claim.

### Pitfall: Unclear novelty over Huang et al. / EXPNeuralUCB

Fix: State clearly that we use EXPNeuralUCB as one comparator in a broader controlled robustness study, while varying allocator and replay/capacity settings under matched threats.

### Pitfall: ICNP reviewers reject the “quantum” angle as too remote

Fix: Emphasize that ICNP 2026 explicitly lists quantum networking and that the paper studies protocol-level routing/control behavior, not quantum hardware physics.

## Main-paper writing style

Prefer:

- direct claims;
- short contribution bullets;
- concrete system model;
- concise threat taxonomy;
- compact figures/tables;
- deployment language.

Avoid:

- long literature-search narration;
- repeated “in contrast” paragraphs;
- unexplained algorithm acronyms;
- internal paper labels like Paper 2;
- excessive bold text;
- unsupported parameter choices.

## Reviewer-proofing questions

Before submission, make sure the manuscript answers:

1. Why is this a network-protocols paper?
2. Why do matched threat conditions matter?
3. What does the framework reveal that previous quantum-routing papers could not?
4. Which result would change how someone designs a quantum routing protocol?
5. Are the baselines fair and sufficiently strong?
6. Are public artifacts handled correctly under double-blind review?
7. Can the main paper stand alone without appendices?
8. Is the paper clearly within 10 pages excluding references?