# Caption Locks

Use this file as the source of truth for locked figure captions during the ICNP venue draft cleanup.

Process: if a figure has a visible title above the image, do not repeat that title in the caption. The caption should state what the figure shows, what evidence the reader should see, what claim it supports, and how it fits the larger robustness argument.

Locked fig:framework caption: Five matched inputs -- topology, threat, policy, allocator, and replay -- feed a shared evaluation grid to produce Oracle-normalized metrics, robustness comparisons, and deployment guidance. Matching all five simultaneously exposes the policy-allocator-capacity interaction as the controlling robustness factor.

Locked fig:system_model caption: At frame t, the routing controller observes candidate-path context, jointly selects a path and qubit allocation, interacts with the threat-conditioned quantum-network testbed, and updates from reward feedback. The loop supports the paper core modeling claim: routing robustness must be evaluated as a coupled path-selection, allocation, threat, and feedback process, not as path selection alone.

Locked fig:robustness_floor caption: The figure reports each representative policy lowest Oracle-normalized efficiency across the locked Markov, Adaptive, and OnlineAdaptive scope. Higher floors indicate resistance to catastrophic collapse: iCEpsilonGreedy has the strongest floor, CPursuit has the best average, and EXPNeuralUCB remains fragile despite adversarial-style exploration. Together with fig:threat_penalty_escalation, this supports the RQ2 claim that adaptive threats expose stability gaps not visible from average efficiency alone.

Locked fig:capacity_paradox caption: Panel (a) summarizes how replay scale changes efficiency across threat regimes, and Panel (b) expands this effect across replay semantics and scenarios. Together, the panels support the RQ3b claim that replay capacity acts as a threat-conditioned control variable: robustness depends jointly on replay scale, anchoring rule, allocator behavior, and threat regime.

Locked fig:threat_penalty_escalation panel (a) subcaption: Compared with Baseline, EXPNeuralUCB incurs the largest Stochastic and Adaptive penalties (12.4 and 13.8 percentage points), while CPursuit stays lower under Stochastic and OnlineAdaptive disruption (3.2 and 4.5 percentage points), supporting the RQ2 claim that threat escalation separates fragile adversarial-first designs from more stable contextual/pursuit models.

Locked fig:threat_penalty_escalation panel (b) subcaption: Across Baseline, Stochastic, Markov, Adaptive, and OnlineAdaptive regimes, iCPursuitNeuralUCB preserves high efficiency (92.8 percent under Adaptive and 99.8 percent under OnlineAdaptive), while EXPUCB remains lower across Markov/Adaptive/OnlineAdaptive (73.8--76.4 percent), supporting the RQ2 claim that adaptive threats expose stability gaps across model families.

Locked fig:threat_penalty_escalation main caption: Panels (a) and (b) jointly support the RQ2 escalation claim: contextual and informed models preserve stronger robustness as disruption progresses from stochastic noise to structured and adaptive interference.

Locked fig:cross_testbed_confirmation panel (a) subcaption: Across Paper 2, Paper 7, Paper 12, and Paper 8, iCPursuitNeuralUCB yields the strongest average cross-testbed efficiency, with leading averages ranging from 44.1 percent on Paper 12 to 78.0 percent on Paper 7. The larger Oracle gaps on harder topologies support the claim that pursuit-informed neural routing transfers beyond the primary testbed but becomes harder to separate from the reference as topology complexity increases.

Locked fig:cross_testbed_confirmation panel (b) subcaption: iCPursuitNeuralUCB is the only model that clears the plotted average-efficiency threshold, reaching 90.9 percent; all other families fall below it, supporting the model-family claim that pursuit-neural hybrids form the strongest robustness tier. Across external testbeds, the same top-family pattern persists even as topology complexity compresses efficiency across models.

Locked fig:cross_testbed_confirmation main caption: Panels (a) and (b) jointly support the core cross-testbed claim: pursuit-informed neural designs generalize beyond the primary evaluation network, while increasing topology complexity widens Oracle gaps and compresses separation among models.

Locked terminology: use routing controller, not agent, in fig:system_model caption.

Patch rule: patch one figure-bearing section at a time. Preserve visible titles, figure bodies, and short table captions unless a separate table-caption change is approved.
