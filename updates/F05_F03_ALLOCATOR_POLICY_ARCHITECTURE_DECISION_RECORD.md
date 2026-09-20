# F-05 / F-03 Allocator--Policy Architecture Decision Record

**Decision date:** 2026-09-20  
**Status:** **APPROVED DESIGN DIRECTION — manuscript implementation deferred to final batch**  
**Scope:** Reviewer-driven allocator--policy semantics (F-05) plus complete decision-loop specification (F-03).  
**Privacy note:** This public record paraphrases the reviewer concern and records the source-grounded reasoning. Exact private reviewer wording remains outside this repository.

## Final approved scientific architecture

The approved hierarchy is:

**shared framework contract -> heterogeneous model algorithms -> controlled allocator--policy coupling -> validated findings**

For the primary matched evaluation, the physical budget is Q=35 qubits. This is a property of the primary matched-evaluation configuration, **not a universal framework limit**.

The allocator and bandit operate at two distinct levels:

1. **Inter-route allocator decision:** the allocator partitions the available physical budget across candidate routes, yielding route-level budgets T_r.
2. **Feasible within-route action construction:** each T_r induces a feasible within-route allocation-action set X_r(T_r) and its associated reward landscape.
3. **Model-specific policy decision:** the selected bandit model applies its own algorithm to select a route and then a **within-route allocation action** from the corresponding feasible set.
4. **Feedback/update:** threat-conditioned reward is observed and the model updates according to its own learning rule.
5. **Conditional adaptive-allocation hook:** when allocator updating is enabled and due, route statistics feed an allocator-update hook; updated T_r values must regenerate the affected X_r(T_r) and reward/context structures before active models continue.

The phrase **within-route allocation action** is the preferred terminology for the bandit's second-level decision so it is not confused with the allocator's inter-route resource-allocation decision.

## Why this became the approved solution

### Step 1 — Initial reviewer problem

The allocator and bandit were presented as independent experimental factors, but the manuscript did not make their operational relationship reconstructable. The missing distinction was not merely execution order; it was the two-level allocation hierarchy.

### Step 2 — Initial framework-layer interpretation was insufficient

The first investigation centered too heavily on runner/environment orchestration. That established how configurations enter an experiment, but it did not answer the core algorithmic question because the actual routing behavior is implemented in the model classes.

Piter correctly redirected the analysis to the **model/algorithm layer**.

### Step 3 — Model-layer trace established the shared two-stage contract

The algorithm classes confirmed a common structural pattern:

- select a route/path;
- select a within-route allocation action from the route-specific feasible set;
- observe reward;
- update according to the concrete model.

The common QuantumModel abstraction provides the shared contract while concrete classes supply heterogeneous path-selection, within-route action-selection, predictive, and update behavior.

This established that the pseudocode can describe a common interface without pretending all policies use the same learning rule.

### Step 4 — Environment trace established what the allocator changes

The primary simulator constructs feasible route-specific actions from the allocator-supplied route budget.

For a route budget T_r, the environment generates feasible qubit splits whose components sum to T_r. It then computes rewards for those actions.

Therefore, in the primary matched evaluation, allocator choice changes **both**:

- the feasible within-route action space X_r(T_r); and
- the reward landscape associated with those feasible actions.

This directly supports the two-level explanation:
**allocator -> T_r -> X_r(T_r) and rewards -> model-specific route/action selection.**

### Step 5 — Concrete model verification

The code directly verifies the following examples:

- **GNeuralUCB:** Simple-UCB path/group selection + NeuralUCB within-route action selection.
- **EXPNeuralUCB:** EXP3 path/group selection + NeuralUCB within-route action selection.
- **EXPUCB:** EXP3 path/group selection + Linear-UCB within-route action selection.
- **CPursuitNeuralUCB:** Pursuit/CMAB path selection + NeuralUCB within-route action selection.
- **iCPursuitNeuralUCB:** iCMAB/Pursuit path selection + NeuralUCB within-route action selection, with ARIMA forecasting and anomaly-aware reward filtering.

The two previously disputed labels are now source-verified:
- GNeuralUCB explicitly documents and implements Simple-UCB group selection.
- iCPursuitNeuralUCB explicitly implements ARIMA-enabled prediction and anomaly-aware reward filtering.

### Step 6 — Portfolio scope was checked against the validated corpus

The four authoritative primary master datasets contain **15 unique non-Oracle policies** across the validated corpus:

- Hybrid: CPursuitNeuralUCB, EXPNeuralUCB, GNeuralUCB, iCPursuitNeuralUCB
- EXP3 corpus adds EXPUCB
- CMAB: CEpsilonGreedy, CEXP4, CPursuit, CEpochGreedy, CThompsonSampling
- iCMAB: iCEpsilonGreedy, iCEXP4, iCPursuit, iCEpochGreedy, iCThompsonSampling

Oracle remains the reference model.

The manuscript currently contains inconsistent policy-count language in several places; the new semantics table must be grounded in the validated corpus rather than inherit those inconsistent counts. Resolving those count references is an implementation/integration item, not a reason to reopen the approved architecture.

### Step 7 — Adaptive allocator hook was separated from an unrelated transition hook

Source inspection confirmed:

- QuantumEnvironment.update_qubit_allocation(timestep, route_stats) exists and is designed to update route budgets, regenerate contexts, and recompute rewards.
- The model classes contain an environment/state transition_trigger / transition_interval mechanism.
- That transition mechanism invokes trigger_state_transition and updates model contexts/rewards; it does **not** call the allocator.
- Therefore the existing default 50-frame transition interval must **not** be presented as the allocator-update cadence.
- A Paper12-specific 500-frame allocator/epoch alignment exists, but it is testbed-specific and must not be generalized to the primary matched evaluation.

The approved common pseudocode will therefore represent allocator adaptation conditionally:

> if allocator update is enabled and due at t

The actual configurable allocator-update contract and cadence must be defined/aligned before the revised pseudocode is finalized as executed-method text.

## Approved revision package

The final F-05/F-03 package will contain all of the following.

### 1. Hierarchical decision-flow diagram

The diagram must show:

**primary matched-evaluation budget Q=35**  
-> **inter-route allocator**  
-> **route budgets T_r**  
-> **feasible within-route action spaces X_r(T_r)**  
-> **model-specific path selection**  
-> **model-specific within-route allocation-action selection**  
-> **threat-conditioned reward**  
-> **model-specific update**

It must also show a feedback arrow from route statistics to the **conditional adaptive allocator-update hook**.

### 2. Algorithm 1 — shared model contract

The common pseudocode must include:

1. primary/global physical-budget input;
2. allocator initialization;
3. route budgets T_r;
4. construction of X_r(T_r);
5. context/reward construction;
6. replay-memory initialization/configuration;
7. model initialization through the shared contract;
8. model-specific route selection;
9. model-specific within-route allocation-action selection;
10. threat-conditioned reward observation;
11. model-specific learning update;
12. replay update;
13. route-statistics update;
14. conditional allocator-update hook;
15. regeneration/propagation of contexts, action sets, and rewards after reallocation.

### 3. Complete policy-semantics table

The table should cover **all 15 validated non-Oracle policies plus the Oracle reference**.

Each row must be verified against the concrete class before manuscript insertion. Recommended columns:

- Policy
- Family
- Path-selection mechanism
- Within-route action mechanism
- Context use
- Predictive machinery
- Feedback/update behavior

Do not infer a row from family resemblance when a concrete class can be checked directly.

### 4. Concise two-level allocation explanation

The prose must explicitly distinguish:

- **inter-route budgeting** by the allocator; from
- **within-route allocation-action selection** by the bandit.

It should explain that allocator choice changes both X_r(T_r) and its reward landscape, while the selected policy determines how route/action choices are explored, selected, and updated from feedback.

## Implementation/alignment work approved as follow-up

These are engineering/completeness tasks, **not conceptual blockers** and not grounds to weaken the validated findings:

1. Define the configurable adaptive-allocator update contract and cadence.
2. Ensure updated T_r values regenerate X_r(T_r), contexts, and rewards.
3. Ensure every active model receives regenerated contexts/rewards rather than stale references.
4. Verify every row of the complete policy-semantics table against its concrete class.
5. Test the completed loop.
6. Preserve the existing validated corpus as the baseline for comparison.
7. Reconcile manuscript policy-count references against the 15-policy validated corpus during final integration.

## Approval history / adjudication

Three independent assessments converged on the architecture-first solution:

- **S:** approved the expanded architecture package and required manuscript notation T_r, primary-only labeling of Q=35, and a conditional allocator-update hook.
- **C:** approved diagram + common pseudocode + policy-semantics table + concise two-level explanation, with direct class verification before insertion.
- **P:** initially withheld approval pending verification of the Simple-UCB and ARIMA/anomaly labels and requested the allocator cadence remain explicit. Both mechanism objections were subsequently resolved by direct source inspection; the cadence issue is retained as the conditional hook/alignment task rather than used to suppress the architecture.

Piter then explicitly **approved the F-05/F-03 design direction**.

## Batch-edit rule

**No manuscript changes are authorized by this approval alone.**

This decision is queued for the final batched manuscript pass. The diagram, pseudocode, complete policy table, and prose must be presented through the approval workflow before insertion. Approved reviewer/manuscript items are not to be reopened during later sentence-by-sentence adjudication unless new source evidence directly contradicts them.

## Canonical status

- **F-05 design direction:** APPROVED.
- **F-03 design direction:** APPROVED jointly with F-05.
- **Scientific architecture:** resolved.
- **Implementation/alignment:** pending as documented above.
- **Manuscript artifacts:** pending presentation/approval.
- **Manuscript edits:** deferred to final batch.
