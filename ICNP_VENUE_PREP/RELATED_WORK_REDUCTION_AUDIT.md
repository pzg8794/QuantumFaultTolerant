# Related Work Reduction Audit for ICNP Draft

This document records the Related Work reduction process for the ICNP venue draft.

## Venue-aware structure decision

For the ICNP draft, `Background` is placed before `Related Work`. This keeps the minimum conceptual vocabulary before the literature comparison, allowing `Related Work` to focus on prior methods, assumptions, and gaps rather than re-teaching quantum-network or bandit background.

This choice supports the venue constraints tracked in `ICNP_DRAFT_AUDIT_TODO.md`, especially the 10-page main-body target, concise presentation, and the need to keep core claims in the main body.

## Required audit method

For each Related Work paragraph:

1. identify the paragraph's role;
2. split it into conceptual pieces;
3. mark overlap with the reduced Background;
4. preserve ICNP-relevant prior-work comparison and closest-work contrast;
5. reduce each split;
6. recombine accepted reduced content;
7. document removed overlap and why it was removed.

## Opening reduction: former Literature Selection Methodology

### Original structure

The original Related Work opened with:

```tex
\subsection{Literature Selection Methodology}
```

followed by two paragraphs explaining MAB positioning, quantum-routing stress-test motivation, literature strands, review years, and inclusion criteria.

### Decision

Remove the `Literature Selection Methodology` subsection heading and replace the two original paragraphs with one compact opening paragraph.

### Removed overlap and rationale

The original opening reintroduced MABs as uncertainty-aware sequential decision rules and described quantum entanglement routing as a stress test shaped by stochastic noise, structured disruption, and resource constraints. These ideas are already covered in the reduced Background: the MAB paragraph defines bandits as repeated routing decisions under partial feedback, and the allocation/capacity plus Problem Scope paragraphs state that robustness depends jointly on learning model, allocator design, replay-capacity configuration, and threat regime.

The original second paragraph also listed inclusion criteria that duplicate the roadmap and the following subsection structure. Instead of keeping a survey-methodology paragraph, the ICNP draft preserves a shorter review-scope sentence so reviewers can see that the literature review spans quantum routing, entanglement distribution, and bandit-based online decision-making.

### Accepted reduced opening

```tex
\section{Related Work}
\label{sec:RelatedWork}

We organize prior work by the assumptions that shape routing robustness: stochastic and adversarial regret regimes, contextual and neural structure, hybrid robust designs, predictive context, and quantum-routing applications. Our targeted review spans quantum routing, entanglement distribution, and bandit-based online decision-making, emphasizing work that defines robustness assumptions, exploits structured context, adds forecasting, combines mechanisms across regimes, or adapts online decisions to resource-constrained settings. This framing lets us compare routing methods by deployment role, threat model, and resource-control assumptions rather than by algorithm family alone.
```

## Foundational Bandits and Regret Regimes

### Original role

This subsection positioned stochastic and adversarial bandits as canonical baseline families and explained why quantum-routing evaluation should distinguish natural noise from coordinated disruption.

### Split-level reduction

- **Foundational tradeoff:** reduce. Background already introduces the bandit taxonomy, so Related Work does not need a regret tutorial.
- **Stochastic baselines:** keep. UCB and Thompson sampling are important baselines and must be cited for evaluation credibility.
- **Adversarial baselines:** keep. EXP3 supports the paper's threat-regime framing.
- **Natural noise versus coordinated disruption:** merge into the baseline framing. The reduced Background already explains that benign noise and adaptive disruption favor different learning robustness assumptions.
- **Our contrast:** keep. ICNP reviewers need to know that the paper evaluates established families under matched routing conditions rather than claiming new regret theory.

### Removed overlap and rationale

The original paragraph explained the exploration--exploitation tradeoff, regret guarantees, and the distinction between stochastic and adversarial learning regimes. The reduced Background already states that stochastic methods assume stable rewards and adversarial methods handle non-stationary or strategic rewards. Therefore, the Related Work version removes tutorial-style explanation and keeps only the prior-work positioning needed to justify the baseline families.

### Accepted reduced text

```tex
\subsection{Foundational Bandits and Regret Regimes}

Foundational bandit results motivate the stochastic and adversarial baselines used in our evaluation. UCB-style optimism and Thompson-style posterior sampling provide canonical baselines under i.i.d. reward assumptions~\cite{auer2002finite,thompson1933likelihood}, while EXP3 provides an adversarial baseline without stochastic assumptions~\cite{auer2002nonstochastic}. Rather than deriving new regret guarantees, our study evaluates these families under the same quantum-routing threat taxonomy, allocator policies, and replay/capacity settings.
```

## Contextual and Neural Bandits

### Original role

This subsection explained how contextual and neural bandits use observable structure and positioned LinUCB, NeuralUCB, and NeuralTS as structure-aware baselines.

### Split-level reduction

- **Contextual bandit idea:** keep briefly. Background already says contextual/neural methods exploit side information or nonlinear reward structure, so Related Work only needs the routing-relevant form of that idea.
- **Representative methods:** keep. LinUCB, NeuralUCB, and NeuralTS are important comparison families and need citations for baseline credibility.
- **Mechanism abstraction:** remove. The original mechanism sentence about learning a value predictor, maintaining uncertainty, and acting optimistically/probabilistically is tutorial material already implied by Background and not necessary for ICNP Related Work.
- **Our contrast:** keep. The important venue-facing point is that we test when contextual information improves robustness under matched threat, allocator, and replay/capacity conditions.

### Removed overlap and rationale

The original paragraph explained contextual/neural bandit mechanics in detail. The reduced Background already introduces contextual and neural methods as models that exploit predictive side information or nonlinear reward structure. Related Work therefore removes the tutorial mechanism sentence and keeps only the prior-work positioning and the contrast to fixed-assumption routing evaluations.

### Accepted reduced text

```tex
\subsection{Contextual and Neural Bandits}

Contextual bandits use observable state to distinguish arms whose rewards depend on topology, link quality, load, or temporal conditions. LinUCB provides a linear contextual baseline~\cite{li2010contextual}, while NeuralUCB and NeuralTS extend this idea with learned nonlinear representations~\cite{zhou2020neuralucb,zhang2022neuralts}. We use these methods to test when contextual information improves routing robustness under matched threat, allocator, and replay/capacity conditions.
```

## Adversarial and Hybrid Robustness

### Original role

This subsection explained adversarial and hybrid robustness and argued that prior comparisons are confounded by mismatched allocator, replay, and evaluation assumptions.

### Split-level reduction

- **Adversarial bandits:** keep briefly. Background already introduces adversarial methods, but Related Work needs the EXP3-style robustness positioning.
- **Hybrid designs:** keep. This supports the paper's pursuit--neural hybrid story.
- **Quantum-routing adversarial motivation:** keep only the routing-specific part: jamming, targeted disruption, and nonstationary link behavior.
- **Confounding gap:** keep. This is a true Related Work gap and supports the matched-grid evaluation.
- **Our contrast:** keep and compress. The venue-facing point is that all model families are evaluated under the same threat, allocator, and replay/capacity grid.
- **Why this matters:** merge into the final sentence by emphasizing the algorithm--allocator--capacity interaction.

### Removed overlap and rationale

The original text repeated adversarial-bandit motivation and gave extended explanation of allocation/replay as first-class factors. The reduced Background already states that adversarial methods handle non-stationary or strategic rewards and that allocator and replay/capacity semantics shape robustness. The Related Work version therefore removes repeated motivation and keeps the comparison gap: prior adversarial-first and hybrid studies often use mismatched experimental assumptions, making it unclear whether robustness comes from the learning rule or from surrounding allocation/replay choices.

### Accepted reduced text

```tex
\subsection{Adversarial and Hybrid Robustness}

Adversarial bandits use randomized exploration to protect against nonstationary or strategically manipulated rewards, with EXP3-style methods serving as canonical examples~\cite{auer2002nonstochastic}. Hybrid designs combine robust exploration with structured exploitation, such as pursuit-style updates over context-conditioned value estimates or adversarial weighting inside learned reward models~\cite{thathachar2011networks}. In quantum routing, these designs are motivated by jamming, targeted disruption, and nonstationary link behavior, but prior comparisons are often confounded by mismatched allocator policies, replay semantics, and evaluation taxonomies. We evaluate adversarial-first, hybrid pursuit--neural, contextual, and informed variants in the same controlled grid to expose robustness effects attributable to the algorithm--allocator--capacity interaction rather than to isolated learning rules.
```

## Predictive and Informed Bandits

### Original role

This subsection positioned predictive/informed bandits as forecast-using policies and explained why forecast quality matters under threats.

### Split-level reduction

- **Predictive/informed idea:** keep briefly. Background already states that predictive/informed methods incorporate forecasts, so Related Work only needs a compact positioning sentence.
- **Representative methods:** keep. ICMAB and ARIMA are cited to anchor the predictive family and time-series baseline.
- **Routing appeal:** keep. Proactive adaptation to congestion, link degradation, and demand shifts is the networking-relevant motivation.
- **Predictive fragility:** keep. Forecasts can be biased, delayed, or adversarially influenced; this strengthens the threat-aware evaluation motivation.
- **Our contrast:** keep. Predictive variants are evaluated as threat-dependent policies rather than oracle baselines.

### Removed overlap and rationale

The original text explained predictive methods and proactive routing motivation in more detail than needed. The reduced Background already states that predictive/informed methods incorporate forecasts. Related Work therefore keeps the prior-work anchors and the threat-aware limitation, while removing repeated explanation of the decision loop.

### Accepted reduced text

```tex
\subsection{Predictive and Informed Bandits}

Predictive or informed bandits incorporate forecasts, exogenous signals, or learned dynamics into online decisions. ICMAB-style methods bias exploration using side information~\cite{kar2024icmab}, while time-series models such as ARIMA capture temporal reward or load patterns~\cite{box2015time}. In routing, these policies can proactively adapt to congestion, link degradation, or demand shifts, but they can also become fragile when forecasts are biased, delayed, or adversarially influenced. We therefore evaluate predictive variants as threat-dependent policies rather than oracle baselines.
```

## Quantum Network Routing with Bandits

### Original role

This subsection is the venue-facing core of Related Work. It positions the paper against quantum-network routing, online path selection, EXPNeuralUCB, LinkSelFiE, adaptive routing, structural routing, and cost-vector multipath routing.

### Audit type

For this subsection, we used a sentence-construction audit rather than a heavy conceptual split. The content is important for ICNP because it connects the paper to networking and quantum-routing work. The goal was to keep the same comparisons while shortening repeated phrasing.

### Main sentence-level reductions

- Consolidated repeated uses of `shared threat taxonomy`, `matched threat, allocator, replay/capacity settings`, and `algorithm--allocator--capacity triad`.
- Kept the field-facing comparison to Wang et al., Li et al., Liu et al., Wang et al. adaptive routing, Huang et al. EXPNeuralUCB, LinkSelFiE, RL-based routing, QuARC, hierarchical routing, repeater-aware routing, and cost-vector routing.
- Preserved the LinkSelFiE contrast because it directly addresses closest-work positioning: LinkSelFiE is link-level selection/fidelity estimation, while this work targets end-to-end path selection and qubit allocation under multiple threat regimes.
- Removed repeated explanation of the controlled cross-product design where the same idea had already been stated in adjacent paragraphs.

### Accepted reduced text

```tex
\subsection{Quantum Network Routing with Bandits}

Recent quantum-network work applies bandits and related online-learning methods to path selection under stochastic decoherence, online benchmarking signals, and structured disruption~\cite{wehner2018quantum,huang2024quantum,wang2025learning,li2025multipath,liu2024qbgp}. Wang \etal~\cite{wang2025learning} study learning high-quality paths under stochastic dynamics, Li \etal~\cite{li2025multipath} propose multipath inter-domain routing with online path selection, and Liu \etal~\cite{liu2024qbgp} use benchmarking signals to support adaptive routing. Wang \etal~\cite{wang2024adaptive} further formulate user-centric entanglement routing with long-term budget constraints and online per-slot routing and allocation. Our contribution is complementary: we benchmark multiple decision-rule and allocator families under a shared threat taxonomy while treating allocator policy and replay/capacity semantics as explicit experimental factors.

Huang \etal~\cite{huang2024quantum} propose \emph{EXPNeuralUCB}, a group neural bandit that combines EXP3-style adversarial exploration with NeuralUCB-style nonlinear reward modeling for joint path selection and qubit allocation. We use EXPNeuralUCB as one comparator within a broader robustness study that also evaluates pursuit--neural hybrids such as \texttt{CPursuitNeuralUCB} and \texttt{iCPursuitNeuralUCB}. This matched comparison separates changes in the learning rule from changes in allocator strategy and replay capacity, which prior adversarial-first routing studies typically treat as fixed.

\paragraph{Closest-work contrast (LinkSelFiE).}
Liu \etal~\cite{10621263} propose \emph{LinkSelFiE}, which addresses the \emph{link-level} problem of selecting and estimating a high-fidelity entanglement link when link qualities are unknown \emph{a priori}. They cast link selection as best-arm identification and use benchmarking-driven estimation to reduce quantum resource consumption while identifying high-quality links with high confidence. In contrast, we target the \emph{end-to-end routing} problem: joint \emph{path selection and qubit allocation} over time under five threat regimes. LinkSelFiE-style fidelity estimates can be incorporated into our reward model, but our primary focus is routing-layer robustness under structured and adaptive disruption.

Beyond bandit-style path selection, prior work studies learning-based route selection under noisy quantum-network conditions~\cite{chaudhary2023quantum}, RL-based adaptive routing with deep Q-networks~\cite{jallowkhan2025adaptive}, structural decomposition through QuARC adaptive clustering~\cite{clayton2024quarc}, hierarchical routing for scalability~\cite{cicconetti2024scalable}, repeater/efficiency-aware routing~\cite{kumar2024routing}, and cost-vector multipath optimization~\cite{leone2021costvector}. These studies differ materially in allocator assumptions, memory/replay parameterization, and threat models. Our benchmark addresses this comparability gap by evaluating multiple algorithm classes under the same threat, allocator, and replay/capacity grid, enabling direct attribution of robustness to the algorithm--allocator--capacity triad.
```

## Toward a Modular Bandit Evaluation Stack

### Original role

This subsection closed Related Work by framing the paper as a modular evaluation stack and connecting quantum-network benchmarking, best-of-both-worlds bandit theory, allocator configuration, replay semantics, and mixed-regime stress testing.

### Split-level reduction

- **Cross-domain meta-problem:** remove as tutorial repetition. Background already defines MABs as repeated routing decisions under partial feedback.
- **Adapter layer/domain variation:** keep only by reference to Background. The idea is useful, but the detailed context/reward/constraint explanation belongs in System Model or Study Design.
- **Enumerated modular stack:** remove from Related Work. The allocator/decision rule, forecasting layer, and domain adapter list introduces our architecture rather than comparing prior work.
- **Quantum-network benchmarking frameworks:** keep. This supports the ICNP-facing evaluation-methodology framing.
- **Best-of-both-worlds bandit theory:** keep briefly and connect to benchmarking frameworks to justify mixed-regime evaluation.
- **Empirical operationalization:** keep as a bridge from prior-work motivation to our evaluation design.
- **Final contribution summary:** keep and broaden so the ending closes the whole Related Work section, not only the final subsection.

### Removed overlap and rationale

The original subsection repeated the modular stack that should be introduced later in System Model or Study Design. It also restated the general bandit problem already covered by the reduced Background. The accepted version instead references Background directly, keeps the benchmarking/theory citations, and uses the final sentence to synthesize the full Related Work section into the paper's central comparison.

### Accepted reduced text

```tex
\subsection{Toward a Modular Bandit Evaluation Stack}

Building on the Background framing of routing robustness as an interaction among context, reward, allocator, and replay/capacity semantics, we treat these elements as an evaluation interface rather than reintroducing the full modular stack here. Quantum-network benchmarking frameworks motivate separating network behavior from policy behavior~\cite{coopmans2021benchmark,kozlowski2022utility}, while best-of-both-worlds bandit theory motivates evaluation across stochastic and adversarial regimes~\cite{zimmert2019optimal}. Taken together, the reviewed work motivates our central comparison: evaluating classical, contextual/neural, adversarial, hybrid, and informed routing policies under common threat, allocator, and replay/capacity conditions to determine when robustness comes from the decision rule and when it comes from deployment configuration.
```

## Current staged status

- `Background` now appears before `Related Work` in `ICNP_2026_venue_draft.tex`.
- The former Literature Selection Methodology subsection is collapsed into the compact opening above.
- `Foundational Bandits and Regret Regimes` is reduced and staged.
- `Contextual and Neural Bandits` is reduced and staged.
- `Adversarial and Hybrid Robustness` is reduced and staged.
- `Predictive and Informed Bandits` is reduced and staged.
- `Quantum Network Routing with Bandits` is sentence-tightened and staged.
- `Toward a Modular Bandit Evaluation Stack` is reduced and staged.
- Related Work audit is complete for this pass.
