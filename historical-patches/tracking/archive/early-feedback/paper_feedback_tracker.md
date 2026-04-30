# Paper feedback tracker (QuantumPathOptimization)

## Workflow

For each feedback item, review and record:

1. **Feedback**
2. **Task**
3. **Content in question**
4. **Proposed solution / new content**
5. **Evaluation of solution**
6. **Decision / applied modification**

Once an item is approved, apply the change where possible, update this tracker, push the documentation update, and move only to the next item explicitly present in the user-provided Dan feedback list.

---

## Item 1 — Abstract wording: who performs the evaluation

**Feedback**  
“Does the framework evaluate them, or do we evaluate the various architectures? … could be confusing.”

**Task**  
Clarify the abstract sentence so the framework is described as the structure/tool used for evaluation, not as an autonomous actor that evaluates algorithms by itself.

**Content in question**  
> This work provides a systematic threat-aware framework that evaluates contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Approved solution / new content**  
> This work provides a systematic threat-aware framework to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Evaluation of solution**  
Approved. This minimal edit directly resolves the ambiguity while preserving the original sentence structure, contribution framing, and technical meaning.

**Decision / applied modification**  
Approved by Piter. Apply in `main.tex` by replacing `framework that evaluates` with `framework to evaluate` in the abstract sentence.

---

## Next item

No next item is present in the uploaded `paper_feedback_tracker.md`. Do not infer Item 2 from older trackers, previous review queues, or unrelated repository files.
