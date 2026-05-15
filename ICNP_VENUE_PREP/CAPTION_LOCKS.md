# Caption Locks

Use this file as the source of truth for locked figure captions during the ICNP venue draft cleanup.

Process: if a figure has a visible title above the image, do not repeat that title in the caption. The caption should state what the figure shows, what evidence the reader should see, what claim it supports, and how it fits the larger robustness argument.

Locked fig:framework caption: Five matched inputs -- topology, threat, policy, allocator, and replay -- feed a shared evaluation grid to produce Oracle-normalized metrics, robustness comparisons, and deployment guidance. Matching all five simultaneously exposes the policy-allocator-capacity interaction as the controlling robustness factor.

Locked fig:system_model caption: At frame t, the routing controller observes candidate-path context, jointly selects a path and qubit allocation, interacts with the threat-conditioned quantum-network testbed, and updates from reward feedback. The loop supports the paper core modeling claim: routing robustness must be evaluated as a coupled path-selection, allocation, threat, and feedback process, not as path selection alone.

Locked terminology: use routing controller, not agent, in fig:system_model caption.

Patch rule: patch one figure-bearing section at a time. Preserve visible titles, figure bodies, and short table captions unless a separate table-caption change is approved.
