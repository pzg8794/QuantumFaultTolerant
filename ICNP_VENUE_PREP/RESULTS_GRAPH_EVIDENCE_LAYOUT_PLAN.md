# Results Graph/Evidence Layout Plan

This note records the Results evidence-layout pass for the ICNP venue draft.

## Current status

Final graph creation and final graph replacement remain blocked while Piter decides which graph forms to use. This pass does not choose final graph designs, generate figures, or remove validated evidence. It prepares the Results section so final graphs can drop in cleanly.

Blocked graph task:

```text
H / Blocked -- Create or replace final result graphs
Reason: Piter is deciding which graph forms to use first.
```

## Layout rule

Each Results subsection should carry only the evidence needed for the main claim:

```text
one clear claim
one intended figure slot or evidence slot
one short interpretation paragraph
no giant detail block interrupting the main story
no claim without a nearby graph/evidence reference
```

Oversized detailed breakdowns, exhaustive run/configuration details, and secondary evidence should move to appendix/supporting material or remain in audit notes once the final graph set is chosen.

## Results claim-to-evidence map

| Results location | Main claim to preserve | Intended figure/evidence slot | Text that must stay nearby | Layout decision |
|---|---|---|---|---|
| Results opening | Results follow the matched grid: RQ1 stochastic viability, RQ2 threat escalation, RQ3 allocator/capacity effects. | No figure required; short roadmap sentence only. | One sentence tying Results to `\cref{sec:studydesign}` and `\cref{sec:research_questions}`. | Keep concise. Do not add extra narrative here. |
| RQ1: Stochastic Routing Viability | Stochastic decoherence separates viable contextual baselines from structural failures. | Current evidence: `\Cref{tab:rq1_master_stochastic}`. Optional final graph: main performance summary if chosen. | Keep the claim sentence, evidence-slice sentence, and one interpretation paragraph citing the table/graph. | Table is acceptable now; if a main-performance graph is added later, consider moving lower-tier row detail to support material. |
| RQ2: Robustness Under Adaptive Threats | Contextual/informed policies maintain stronger robustness floors than adversarial-first EXP-family baselines under structured/adaptive threats. | Intended placeholder/final graph: `fig:robustness_floor_placeholder` or final robustness-floor graph. Current evidence: `\Cref{tab:rq2_adversarial}`. | Keep the locked adversarial-scope setup and one paragraph interpreting average, floor, and win dominance. | Add robustness-floor placeholder next if graph placement continues. Avoid extra RQ2a/RQ2b/RQ2c bullets unless needed for Discussion. |
| RQ3: Deployment Optimization | Deployment is configuration-sensitive, but one strong static configuration exceeds the 85% robustness target. | Evidence slot: short RQ3 answer paragraph; possible deployment-summary graph if final graph set includes it. | Keep the 6K `iCPursuitNeuralUCB + Fixed + (T-type, s=2)` claim and its global average/floor. | Keep concise. Avoid repeating RQ3a--RQ3d details in the parent subsection. |
| RQ3a: Predictive Context Modeling Impact | Informative context mainly improves OnlineAdaptive robustness and lowers scenario dispersion. | Current evidence: `\Cref{tab:rq3a_master_informative}`. Optional final graph: small paired comparison or integrated main performance graph. | Keep fixed deployment setting, table/graph reference, OnlineAdaptive lift, and CV reduction. | Current table is small and claim-supporting; keep unless replaced by a graph. |
| RQ3b: Replay Capacity Scaling & Paradox | Replay capacity is not monotonic; the effect is threat-dependent and allocator/anchoring-sensitive. | Inserted placeholder: `\Cref{fig:capacity_paradox_placeholder}`. Current evidence: `\Cref{tab:rq3b_master_capacity_scaling}`. | Keep the evidence-slice setup, the capacity-paradox figure, and the short interpretation paragraph. | This is the highest-priority graph slot. Once final graph exists, decide whether the detailed capacity table stays in body or moves to supporting material. |
| RQ3c: Algorithm-Allocator Co-Design | Allocator effects are deployment-critical; Fixed has best global profile while Thompson is threat-sensitive. | Current evidence: `\Cref{tab:rq3c_master_allocators}`. Optional final graph: deployment-guidance graph if chosen. | Keep fixed setting, allocator comparison table/graph, and one interpretation paragraph. | Keep table for now. If deployment guidance graph is inserted, consider moving full allocator table to support material. |
| RQ3d: Scenario-Based Deployment Rules | Clear deployment rules emerge, but the static default remains strong. | Current evidence: `\Cref{tab:rq3d_deployment_rules}`. Intended final graph candidate: deployment guidance. | Keep static-default sentence, scenario-switching table/graph, and one interpretation paragraph that references RQ3b--RQ3c. | This is the natural home for a final deployment guidance graphic. Avoid adding extra prose beyond the table/graph interpretation. |
| Cross-Testbed Validation | Pursuit--neural hybrids generalize across external testbeds, but scale/topology affects efficiency and winner structure. | Optional final graph candidate: cross-testbed confirmation. Current evidence: `\Cref{tab:testbed_comparison}` and `\Cref{tab:model_family_comparison}`. | Keep one compact cross-testbed claim and one sentence explaining topology-complexity effects. | This is currently the largest detail block. Strong candidate for compression: keep one summary table or graph in body; move exhaustive per-testbed/per-family breakdown to appendix/supporting material. |

## Main-body evidence policy

Keep in the main paper:

- RQ1 viability split or its graph/table summary.
- RQ2 robustness floor evidence.
- RQ3 static-default statement.
- RQ3a OnlineAdaptive lift if the informative-context claim remains in Results.
- RQ3b capacity paradox figure/table.
- RQ3c allocator interaction evidence.
- RQ3d deployment rules.
- One cross-testbed confirmation artifact if space allows.

Move out of the main flow after graph choices are finalized:

- exhaustive per-run/per-configuration details;
- large secondary cross-testbed tables if a compact graph can carry the claim;
- duplicate winner-count explanations already captured in captions or notes;
- extended GA-report observations not needed for the main Results story.

## Discussion synchronization checklist

The Discussion audit must stay synchronized with the Results evidence slots:

- Discussion Finding 1 should cite or reference RQ1/RQ2 evidence only after the final main-performance/robustness-floor evidence is settled.
- Discussion Finding 2 should align with RQ3b and the final capacity-paradox graph/table. Do not state capacity-paradox magnitudes that are not in the retained main-body evidence.
- Discussion Finding 3 should align with RQ3c/RQ3d and the final allocator/deployment guidance evidence.
- Cross-testbed claims in Discussion should match whatever cross-testbed artifact remains in the main body.
- If a detailed table moves to supporting material, Discussion should cite the retained summary artifact and mention supporting detail only if necessary.

## Immediate next unblocked actions

1. Insert `fig:robustness_floor_placeholder` if we continue placeholder placement before choosing final graph forms.
2. Decide whether RQ1's full stochastic table should remain or be replaced by a main-performance summary graph later.
3. Compress Cross-Testbed Validation after deciding whether the optional cross-testbed confirmation graph is included.
4. Audit Discussion only after the final Results evidence layout is stable enough to avoid mismatched claims.

## Validation checklist

- [x] Every Results subsection has one clear claim.
- [x] Every Results subsection has an identified figure/evidence slot.
- [x] Every Results subsection identifies nearby text that must remain.
- [x] Oversized detail candidates are flagged but not moved yet.
- [x] No final graph form was selected while graph creation remains blocked.
- [x] Discussion synchronization requirements are documented.
