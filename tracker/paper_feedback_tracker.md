# Paper feedback tracker (QuantumPathOptimization)

## Workflow

For each feedback item, we will review the item in this format before changing the paper:

1. **Feedback**
2. **Task**
3. **Content in question**
4. **Proposed solution / new content**
5. **Evaluation of solution**
6. **Decision / applied modification**

Once an item is approved, we apply the change where possible, update this tracker, commit/push, and move directly to the next item.

---

## Item 1 — Abstract wording: who performs the evaluation

**Feedback**  
“Does the framework evaluate them, or do we evaluate the various architectures? … could be confusing.”

**Task**  
Clarify the abstract sentence so the framework is described as the tool or structure used for evaluation, not as an autonomous actor that evaluates algorithms by itself.

**Content in question**  
> This work provides a systematic threat-aware framework that evaluates contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Approved solution / new content**  
> This work provides a systematic threat-aware framework to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Evaluation of solution**  
Approved. This is the correct minimal edit because it directly resolves the ambiguity raised by the feedback while preserving the original sentence structure, contribution framing, and technical meaning.

**Decision / applied modification**  
Approved by Piter. Tracker updated. Manuscript target is `main.tex`, Abstract paragraph 2, changing `framework that evaluates` to `framework to evaluate`.

---

## Item 2 — Related Work wording: replace awkward “situate” phrasing

**Feedback**  
“Replace awkward `situate` wording.”

**Task**  
Review the Related Work sentence that previously used `situate` and decide whether the replacement better expresses the intended scholarly positioning.

**Content in question**  
The tracked issue refers to the Related Work sentence that placed multi-armed bandits in relation to uncertainty-aware sequential decision rules.

**Current source text**  
> We place multi-armed bandits (MABs) within the family of uncertainty-aware sequential decision rules and use quantum entanglement routing as a stress test in which stochastic noise, structured disruption, and resource constraints jointly shape performance.

**Proposed solution / new content**  
Keep the current wording:

> We place multi-armed bandits (MABs) within the family of uncertainty-aware sequential decision rules and use quantum entanglement routing as a stress test in which stochastic noise, structured disruption, and resource constraints jointly shape performance.

**Evaluation of solution**  
Recommended. The current wording is already better than `We situate ... as ...` because `place ... within the family of ...` is clearer, less awkward, and academically precise. It states the conceptual relationship without overclaiming that MABs are equivalent to the broader family of uncertainty-aware decision rules.

**Decision / applied modification**  
Pending approval. If approved, no manuscript change is needed because the source already contains the improved wording in `sections/02--related_works.tex`; we only mark Item 2 as accepted and proceed to Item 3.
