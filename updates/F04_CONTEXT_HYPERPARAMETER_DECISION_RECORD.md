# F-04 Context and Hyperparameter Documentation Decision Record

**Decision date:** 2026-09-20  
**Status:** **APPROVED CONCEPTUAL/MECHANISM DIRECTION — exact validated-corpus hyperparameter values provenance-pending; manuscript implementation deferred to final batch**  
**Scope:** Reviewer-driven documentation of context/action representations, NeuralUCB mechanics, Pursuit update semantics, predictive machinery, and hyperparameter provenance.  
**Privacy note:** This public record paraphrases reviewer concerns and preserves the complete source-grounded reasoning path. Exact private reviewer wording remains outside this repository.

## Final approved scientific direction

F-04 extends the already-approved F-03/F-05 architecture package. The manuscript must stop presenting one generic universal context vector and instead document the **scope-specific context/action representation** used by each evaluation setting.

The approved hierarchy is:

**allocator-assigned route budget T_r -> feasible route-specific context/action set X_r(T_r) -> model-specific route selection -> model-specific within-route action scoring/selection -> reward/update/replay**

Mechanisms and current-code defaults may be documented when source-verified. Exact numerical values claimed as having produced the validated corpus must remain explicitly provenance-pending until tied to the data-producing commit/configuration.

## Reviewer problem that drove F-04

The manuscript was too vague for replication in several ways:

- the pursuit/neural composition was not operationally explained;
- the context representation was described generically rather than concretely;
- NeuralUCB network architecture, confidence scoring, training cadence, loss, and optimizer were omitted;
- the Pursuit learning-rate parameter was listed without explaining the probability update it controls;
- predictive/iCMAB descriptions risked presenting one ARIMA order/configuration as universal.

F-05/F-03 resolved the pursuit/neural composition structurally. F-04 resolves the context and learning-mechanism documentation.

## Step-by-step reasoning path

### Step 1 — The live manuscript's generic context sentence was checked

The submission-era and live draft use the same generic statement that contextual/neural policies derive a context vector from path identity, hop count, allocation vector, recent reward history, and threat/availability state.

Direct implementation tracing showed that this is **not an accurate literal description of the primary NeuralUCB input**.

### Step 2 — Primary matched-evaluation context construction was traced

`QuantumEnvironment._generate_contexts()` constructs feasible per-link integer qubit splits from each allocator-assigned route budget.

For route r with h_r links and allocator-assigned budget T_r, the approved primary representation is:

`X_r(T_r) = { x in Z_{>=0}^{h_r} : sum_l x_l = T_r }`.

In the four-route primary topology:

- two-hop routes use 2-dimensional allocation vectors;
- three-hop routes use 3-dimensional allocation vectors.

Therefore the primary context dimension is route-hop dependent rather than globally fixed.

### Step 3 — Information-source roles were separated correctly

For the primary matched evaluation:

- **allocation vector:** explicit instantaneous within-route context/action representation;
- **route identity:** structural, through the selected route-specific learner/action set rather than a concatenated ID feature;
- **hop count:** implicit in h_r and therefore in the dimension of x;
- **threat availability:** affects reward/feedback through the availability process rather than being appended to the primary allocation vector;
- **reward history:** enters learner state, replay, and model updates rather than the instantaneous allocation vector.

This is the approved replacement for the manuscript's current all-purpose context sentence.

### Step 4 — External-testbed context construction was checked

The framework uses a common model interface but does **not** require a universal feature encoding.

Current Paper8 source explicitly builds one 8-dimensional path-level feature vector per path:

1. route budget/capacity;
2. hop count;
3. minimum fidelity;
4. mean fidelity;
5. minimum rate;
6. mean rate;
7. minimum purification-round value;
8. product of swap-success probabilities.

Paper8 currently exposes **one within-path action per path**, unlike the primary simulator's combinatorial within-route allocation sets.

Other external-testbed context rows must be verified against their concrete construction before manuscript insertion; no universal encoding may be inferred from Primary or Paper8.

### Step 5 — NeuralUCB network and scoring mechanics were traced

The verified `NeuralBanditModel` is a one-hidden-layer network:

**d_r -> 128 -> 1**

with ReLU activation between the two linear layers.

The within-route NeuralUCB scorer is represented conceptually as:

`s_t(x) = f_theta(x) + beta * sqrt(g_theta(x)^T Sigma_t^{-1} g_theta(x))`

and selects the feasible action with maximal score.

This turns the manuscript's abstract `q_hat + beta U` expression into an operational explanation: learned reward estimate plus a gradient-based uncertainty bonus.

### Step 6 — NeuralUCB update/training mechanism was traced

Direct source inspection verifies the primary NeuralUCB implementation uses:

- replay memory;
- gradient/covariance update after observed feedback;
- Adam optimization;
- mean-squared-error loss;
- squared parameter-drift regularization toward the initial network parameters;
- training after T > K;
- two optimizer/training iterations per update;
- replay minibatches of size 64.

The code constructor currently exposes defaults including beta=1, lambda=1, hidden_size=128, learning rate 1e-4, and regularization 0.000625.

**Approved wording safeguard:** do not state that every possible NeuralUCB-derived/testbed-specific class uses the exact same cadence. Scope this training description to the verified NeuralUCB within-route implementation used by the relevant primary neural/hybrid models unless broader provenance is established.

### Step 7 — Pursuit probability update was traced

The implementation begins from uniform route-selection probabilities and updates toward the arm with the highest empirical mean reward.

With i* as the current empirical-best arm and alpha as the Pursuit learning rate:

`p_{i*} <- p_{i*} + alpha(1 - p_{i*})`

and for i != i*:

`p_i <- p_i - alpha p_i`.

The next route is sampled from the updated probability vector.

This directly explains what the manuscript's Pursuit learning-rate parameter controls.

### Step 8 — Predictive ARIMA wording was checked

The current implementation uses `auto_arima()` model-order search and anomaly-aware reward filtering. Therefore a fixed `ARIMA(1,0,1)` description must not remain as a universal implementation claim unless data-producing provenance establishes that exact configuration for the reported corpus.

The approved mechanism-level phrase is:

**ARIMA-based predictive reward modeling with anomaly-aware filtering**.

Exact warmup, update interval, order-search configuration, anomaly thresholds, and corpus-specific predictive settings remain provenance-pending.

### Step 9 — NeuralTS scope safeguard was adjudicated

Reviewer discussion mentioned NeuralTS as a possible documentation target. The validated-corpus audit currently identifies 15 non-Oracle evaluated policies and does **not** include NeuralTS.

Therefore NeuralTS must not be added to the evaluated-policy table merely because a class exists in the codebase. If future provenance shows it contributed to a reported corpus, it can then be documented as evaluated.

### Step 10 — Hyperparameter provenance policy was resolved

Independent review converged on a key evidence distinction:

1. **Mechanism:** source-verified and safe to document.
2. **Current-code default:** source-verified as a current implementation value.
3. **Validated-corpus value:** may be stated as a reported-run fact only after tying it to the data-producing commit/configuration.

This distinction resolves the concern that one current default might silently masquerade as the parameter used for every reported corpus.

## Approved manuscript package

F-04 will extend the approved F-03/F-05 package with the following artifacts.

### 1. Primary feasible context/action equation

`X_r(T_r) = { x in Z_{>=0}^{h_r} : sum_l x_l = T_r }`

Use the phrase **route-specific allocation context/action representation** rather than universally calling x 'the context vector.'

### 2. Scope-specific context-representation table

At minimum:

| Evaluation scope | Context/action representation | Dimension | Scope note |
| --- | --- | ---: | --- |
| Primary matched grid | Feasible within-route integer qubit split x in X_r(T_r) | h_r; 2 or 3 in the primary topology | Route-specific action set; threat affects feedback rather than being appended to x |
| Paper8 external | Explicit path-quality feature vector | 8 | One within-path action per path in current implementation |
| Other external testbeds | Testbed-specific | Verify | Do not imply a universal encoding |

Each external-testbed row must be source-verified before insertion.

### 3. NeuralUCB architecture and scoring

Document:

- d_r -> 128 -> 1 network;
- ReLU hidden activation;
- learned reward prediction;
- gradient-based confidence term;
- route-specific feasible-action scoring.

### 4. NeuralUCB training/update description

Document the verified mechanism and scope it to the relevant verified implementation. Corpus-specific numerical values remain provenance-qualified until data-producing configurations are recovered.

### 5. Pursuit update equation

Include the implemented probability-update equations so the meaning of alpha is explicit rather than merely listed in a parameter table.

### 6. Integrated policy-semantics table

Coordinate with F-03/F-05 rather than duplicating model descriptions. The table should show route selector, within-route action selector, predictive machinery, update behavior, and scope/provenance notes.

### 7. Provenance-aware hyperparameter table

Recommended columns:

- Model/family
- Parameter
- Mechanistic role
- Current implementation/default
- Validated-corpus value
- Provenance/source reference

Do not use a simple `Parameter | Value` table that conflates defaults with reported-run settings.

### 8. Replace the current generic context sentence

The current generic context sentence is approved for **replacement**, not expansion, during the final batched manuscript pass.

## Provenance-pending values

Before corpus-specific numerical values are frozen, trace the data-producing commit/configuration for at least:

- NeuralUCB beta and lambda;
- neural learning rate;
- regularization;
- exact optimizer/training cadence and minibatch settings for each reported corpus;
- Pursuit alpha;
- predictive warmup;
- ARIMA update interval/order-search configuration;
- anomaly threshold/filter settings;
- replay settings;
- model-mode overrides;
- testbed-specific context overrides.

These are evidence-alignment tasks, not reasons to weaken or withhold the verified mechanism explanations.

## Approval history / adjudication

Three independent assessments converged on Option C:

- **S:** approved the mechanism/context direction, verified the primary 2/3-dimensional allocation representation, Paper8's 8-dimensional one-action-per-path representation, NeuralUCB mechanics, Pursuit update, and the need to replace fixed ARIMA(1,0,1) language.
- **C:** approved Option C, required the phrase 'route-specific allocation context/action representation,' requested NeuralTS only if actually evaluated, and required scope wording for NeuralUCB training cadence.
- **P:** agreed with the entire conceptual package but initially marked it 'revise before approval' solely to ensure the hyperparameter table explicitly separates mechanisms/current defaults from validated-corpus numerical provenance.

Final adjudication concluded that P's safeguard is an implementation/provenance constraint already compatible with the approved Option C design, not a scientific disagreement requiring conceptual approval to remain open.

Piter then explicitly approved the F-04 direction.

## Batch-edit rule

**No manuscript changes are authorized by this approval alone.**

All F-04 edits remain queued for the final batched manuscript pass. The context equation/table, NeuralUCB/Pursuit explanation, policy-semantics integration, and provenance-aware hyperparameter table must be presented through the approval workflow before final insertion. Approved items are not to be reopened during later sentence-level adjudication unless new source evidence directly contradicts them.

## Canonical status

- **F-04 conceptual/mechanism direction:** APPROVED.
- **Primary context/action representation:** APPROVED.
- **Scope-specific context architecture:** APPROVED.
- **NeuralUCB mechanism:** APPROVED.
- **Pursuit mechanism:** APPROVED.
- **ARIMA/anomaly mechanism description:** APPROVED at mechanism level.
- **Exact validated-corpus hyperparameter values:** PROVENANCE-PENDING.
- **Generic manuscript context sentence:** APPROVED FOR REPLACEMENT in final batch.
- **Manuscript edits:** DEFERRED to final batch.
