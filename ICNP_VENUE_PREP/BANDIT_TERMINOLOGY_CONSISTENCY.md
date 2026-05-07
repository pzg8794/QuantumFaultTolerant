# Bandit Terminology Consistency

This note records the resolution for pending terminology items:

```text
Item 061 -- Dan added "Bandit"
Item 062 -- Dan: "I think we can say bandit for all"
```

## Accepted rule

Use `bandit policy` or `bandit-based routing strategy` when referring to the evaluated routing decision rules. Do not over-apply `bandit` to components that are not themselves bandit methods.

Accepted terminology:

```text
bandit policy
bandit-based routing strategy
allocator policy
threat regime
```

Rejected terminology:

```text
bandit allocator policy
bandit threat regime
bandit replay capacity
```

## Manuscript updates applied

### Active venue draft

The active draft now uses bandit terminology where the evaluated routing learners are being discussed:

- `algorithm--allocator--capacity interaction` became `bandit-policy--allocator--capacity interaction` in the abstract.
- `Across thirteen algorithms` became `Across thirteen bandit policies` in the abstract.
- RQ1 now asks about `classical and context-aware multi-armed bandit (MAB) policies`.
- RQ3 now asks about `choices in bandit policy, resource allocation strategy, and replay-capacity semantics`.
- The contribution sentence now attributes robustness to interaction among `bandit policy, allocator policy, and replay-capacity semantics`.
- The MAB formulation now says `bandit policies differ` in scoring/update behavior.
- The compact Study Design RQ paragraph now uses `bandit policies`, `bandit-based routing strategies`, and `choices in bandit policy`.

### Study Design staging fragment

The validated Study Design staging fragment now uses:

- `Bandit-policy families` in the design matrix.
- `Bandit-policy portfolio` for the evaluated learning-method table.
- `Bandit policies / reference` as the table header, because Oracle is a reference rather than a bandit learner.
- `Key bandit-policy features` for the CPursuit/iCPursuit feature summary.
- `contextual/adversarial bandit policies` in the experimental-scope paragraph.

## Terms intentionally preserved

The following terms were intentionally left unchanged because they refer to distinct non-bandit components:

- `allocator policy` / `allocator policies`
- `threat regime` / `threat regimes`
- `threat settings`
- `replay-capacity semantics`
- `Oracle` / `Perfect-information reference`

## Feedback-marker handling

The active ICNP venue draft did not contain Dan's inline feedback marker for Items 061--062. If the original marker is reintroduced during a working-review pass, retain it as a LaTeX source comment and add:

```tex
% SOLVED: Standardized terminology so evaluated routing methods are described as bandit policies or bandit-based routing strategies, while allocator policies and threat regimes keep their distinct names.
```

## Validation checklist

- [x] Evaluated learning/routing methods are consistently called bandit policies or bandit-based routing strategies.
- [x] Allocators remain allocator policies.
- [x] Threat models remain threat regimes/settings.
- [x] Oracle remains a reference, not a bandit policy.
- [x] No awkward phrase such as `bandit threat` or `bandit allocator` was introduced.
