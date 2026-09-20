# F-06 Threat-Taxonomy Physical-Grounding Decision Record

**Decision date:** 2026-09-20  
**Status:** **APPROVED CONCEPTUAL/SCIENTIFIC DIRECTION — exact simulator parameters/process rows provenance-pending; manuscript implementation deferred to final batch**  
**Scope:** Reviewer-driven physical/domain grounding of the five active availability-stress settings.  
**Privacy note:** This public record paraphrases reviewer concerns and preserves the source-grounded reasoning. Exact private reviewer wording remains outside this repository.

## Final approved framing

The five active settings are best described as a **controlled progression in route-availability dependence and reactivity**, layered on top of the inherent probabilistic quantum-success model.

The approved conceptual sequence is:

**no added route unavailability -> independent disruption -> temporally correlated disruption -> routing-history-dependent targeting -> continuously reactive targeting**

The five active settings remain exactly:

- Baseline
- Stochastic
- Markov
- Adaptive
- OnlineAdaptive

Historical references to `Targeted` are not part of the active validated taxonomy and must not be reintroduced unless separate evidence establishes that it belongs to the validated corpus.

## Core mathematical distinction

The live manuscript already defines:

`Y_t(r,x) ~ Bernoulli(q_r(x) A_t(r))`

where `q_r(x)` is the probabilistic quantum-success term and `A_t(r)` is the route-availability gate.

The approved explanatory sentence is:

> The factor `q_r(x)` represents the probabilistic quantum-success process for the selected route and qubit allocation, whereas `A_t(r)` models additional route-level availability disruption.

This distinction is essential:

- Baseline means **no added route-level availability disruption**, not perfect hardware.
- Stochastic availability stress must not be conflated with photon loss, decoherence, or other probabilistic quantum-success mechanisms already represented on the `q_r(x)` side of the model.

## Approved domain interpretations

### Baseline

- **Controlled property:** reference condition with no added availability disruption.
- **Quantum-network interpretation:** normal operation under the probabilistic quantum-success process already represented by `q_r(x)`.
- **Boundary:** not perfect hardware and not zero physical noise.

### Stochastic

- **Controlled property:** independent route-level unavailability.
- **Quantum-network interpretation:** transient independent link, channel, repeater, or station interruption.
- **Boundary:** not a decoherence or photon-loss model.

### Markov

- **Controlled property:** temporal persistence/correlation in route availability.
- **Quantum-network interpretation:** bursty or persistent link/node/channel degradation or outage.
- **Boundary:** does not claim that real quantum-network failures literally follow the simulator's exact Markov process; spatially correlated failures are a separate unmodeled dependence dimension.

### Adaptive

- **Controlled property:** route-history-dependent targeting.
- **Quantum-network interpretation:** controlled route-observing availability stress/adversary abstraction motivated by availability attacks on quantum-network infrastructure.
- **Boundary:** not a literal reproduction of a documented physical attack mechanism.

### OnlineAdaptive

- **Controlled property:** continuously reactive targeting as routing behavior evolves.
- **Quantum-network interpretation:** an online route-observing availability-stress/adversary abstraction.
- **Boundary:** not a hardware-validated adversary or measured attack distribution.

## Literature roles approved

The literature must be used according to what it actually supports:

- **Pant et al.** supports the inherent probabilistic quantum-operation / lossy-link side of the model and therefore belongs primarily to the `q_r(x)` interpretation.
- **Li et al.** supports explicit node/edge/channel failure or interruption as meaningful quantum-network routing robustness conditions and is appropriate for the availability-failure side.
- **Satoh et al.** supports quantum-repeater/network **availability** vulnerabilities and attack motivation, but does not validate the exact Adaptive/OnlineAdaptive targeting rules used in this simulator.
- **Zhang and Zhuang, _Quantum Internet under random breakdowns and intentional attacks_ (arXiv:2012.02241)** is an optional but especially well-matched additional source because it explicitly distinguishes random breakdowns from intentional attacks. It requires a new bibliography entry if adopted.

## Why five settings

The approved justification is methodological, not ontological:

- Baseline isolates routing/allocation behavior without added path unavailability.
- Stochastic introduces independent availability loss.
- Markov introduces temporal dependence/persistence.
- Adaptive introduces dependence on observed routing history.
- OnlineAdaptive introduces continuously reactive routing dependence.

The paper must **not** imply that five is a universal taxonomy of all quantum-network failures or that later settings are monotonically more physically realistic or universally more severe.

## Approved revision package

The final F-06 manuscript package will contain:

1. **Short taxonomy-rationale paragraph** explaining the progression in route-availability dependence and reactivity.
2. **Mapping table** with columns:
   - Setting
   - Availability process
   - Controlled property
   - Quantum-network interpretation/domain analogue
   - Evidence boundary / what it does not claim
3. **Explicit `q_r(x)` versus `A_t(r)` separation sentence** adjacent to the reward model.
4. **Simulator-parameter boundary sentence** stating that rates, windows, transition parameters, and targeting coefficients are controlled experimental settings rather than estimates of universal operational failure distributions.
5. **Excluded-scope statement** covering at least:
   - spatially correlated failures as a dedicated factor;
   - exhaustive device-level fault distributions;
   - hardware-calibrated adversary behavior;
   - hardware/deployment validation.

## Exact-parameter/process provenance gate

The conceptual taxonomy is approved, but **exact parameter/process cells are not yet approved** because the current implementation and manuscript descriptions do not agree.

Direct source inspection of the current `attack_strategy.py` established:

- **MarkovAttack:** binary per-path attacked/not-attacked state with `p_stay=0.7`; this is not the manuscript's current `four-state` description.
- **AdaptiveAttack:** defaults include `attack_rate=0.25`, `adaptation_window=100`, and `adaptation_strength=0.5`; this does not match the manuscript's `w=50` statement unless the validated runs used an explicit override or earlier implementation.
- **OnlineAdaptiveAttack:** current behavior uses `response_delay=5`, `burst_probability=0.3`, burst outages, and recent-path targeting; the current class does not implement the manuscript's stated `gamma=0.97` softmax rule.
- **Factory:** exposes exactly `none`, `stochastic`, `markov`, `adaptive`, and `onlineadaptive`.

Therefore:

- Do **not** copy current class defaults into the paper as though they generated the validated corpus.
- Do **not** assume the existing manuscript parameter values generated the validated corpus.
- Do **not** freeze exact Markov/Adaptive/OnlineAdaptive process descriptions until the validated logs are traced back to their data-producing commit/configuration and overrides.

## Required provenance follow-up

Separately from the approved conceptual revision, trace the validated corpora back to the data-producing implementation/configuration and recover:

1. attack-strategy class/version;
2. constructor/default values active at execution;
3. any notebook/runner/config overrides;
4. scenario-specific attack rates and process parameters;
5. exact Markov transition semantics;
6. exact Adaptive history-window/targeting semantics;
7. exact OnlineAdaptive reactivity/targeting semantics.

This provenance task is an implementation/evidence-alignment task. It is **not** a reason to weaken, invalidate, or delay approval of the conceptual taxonomy.

## Reasoning path that produced the decision

1. Reviewer B and Reviewer C independently identified the same structural gap: the simulator's threat processes were not mapped to meaningful quantum-network failure/availability interpretations.
2. The manuscript's reward model already separates probabilistic quantum success (`q_r(x)`) from route-level availability (`A_t(r)`), providing a clean formal basis for the physical/domain explanation.
3. The five active settings were reinterpreted according to the dependence structure they isolate, rather than presented as a generic escalation of physical severity.
4. Literature roles were bounded carefully so quantum-network papers motivate the analogues without being misrepresented as validation of the exact simulator rules.
5. Independent review converged on the same package: rationale paragraph + mapping table + explicit mathematical separation + simulator-parameter boundary + excluded scope.
6. Direct code verification then revealed mismatches between current attack-strategy defaults/semantics and the manuscript's exact parameter text.
7. The final decision therefore separates **resolved conceptual science** from **pending historical execution provenance**.

## Approval history / adjudication

Three independent assessments converged:

- **S:** approved the F-06 direction with explicit distinctions between `q_r(x)` and `A_t(r)`, careful attribution of adaptive attacks, controlled-parameter caveats, active-five-regime scope, and domain-analogue terminology.
- **C:** approved the same package and recommended the phrase **controlled progression in route-availability dependence and reactivity**, with exact parameter verification before insertion.
- **P:** independently verified the mathematical model, literature roles, and implementation/manuscript discrepancies, and approved the conceptual package subject to the same provenance gate.

Piter subsequently approved the F-06 conceptual/scientific direction through this converged adjudication.

## Batch-edit rule

**No manuscript changes are authorized by this approval alone.**

The rationale, mapping table, separation sentence, parameter-boundary sentence, and excluded-scope statement remain queued for the final batched manuscript pass. Exact parameter/process cells remain provenance-pending until the data-producing attack implementation is recovered.

## Canonical status

- **F-06 conceptual/scientific direction:** APPROVED.
- **Five-regime taxonomy:** APPROVED.
- **Domain mapping:** APPROVED at the abstraction level.
- **`q_r(x)` / `A_t(r)` separation:** APPROVED.
- **Exact simulator parameters/process rows:** PROVENANCE-PENDING.
- **New experiments:** NOT REQUIRED for this reviewer fix.
- **Manuscript edits:** DEFERRED to final batch.
