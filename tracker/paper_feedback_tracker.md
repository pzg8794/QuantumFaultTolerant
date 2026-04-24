# Paper feedback tracker (QuantumPathOptimization)

## Workflow

For each feedback item, we will review the item in this format before changing the paper:

1. **Feedback**
2. **Task**
3. **Content in question**
4. **Proposed solution / new content**
5. **Decision / status**

Once an item is approved, we will apply the change, update this tracker, commit/push, and then move to the next item.

---

## Item 1 — Abstract wording: who performs the evaluation

**Feedback**  
“Does the framework evaluate them, or do we evaluate the various architectures? … could be confusing.”

**Task**  
Rewrite the abstract sentence so it is explicit that the paper authors use the framework to run the evaluations. The framework does not evaluate algorithms by itself.

**Content in question**  
> This work provides a systematic threat-aware framework that evaluates contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Proposed solution / new content**  
> This work introduces a systematic threat-aware evaluation framework and uses it to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

**Decision / status**  
Approved by Piter as conceptually correct. Needs source verification and application status check before marking fully done.
