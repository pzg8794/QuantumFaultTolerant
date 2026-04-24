# Feedback Item 1 Process — Abstract wording: who performs the evaluation

**Source of truth:** `paper_feedback_tracker.md` uploaded in this chat.

## 1. Feedback

> “Does the framework evaluate them, or do we evaluate the various architectures? … could be confusing.”

## 2. Task

Clarify the abstract sentence so the framework is described as the structure/tool used for evaluation, not as an autonomous actor that evaluates algorithms by itself.

## 3. Content in question

Current sentence:

> This work provides a systematic threat-aware framework that evaluates contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

## 4. Proposed solution / new content

Use Piter’s approved minimal edit:

> This work provides a systematic threat-aware framework to evaluate contextual, adversarial, and hybrid bandit algorithms for joint path selection and qubit allocation in quantum networks, together with a family of pursuit–neural hybrid policies that we show outperform both adversarial-first and stochastic-only baselines.

## 5. Evaluation of solution

This is the best solution for Item 1 because it directly resolves Dan’s ambiguity without rewriting the full sentence or changing the contribution claim. The change from “that evaluates” to “to evaluate” makes the framework an instrument for evaluation rather than the grammatical actor doing the evaluation.

## 6. Decision / applied modification

Approved by Piter. Apply the following manuscript patch in `main.tex`:

```diff
- framework that evaluates contextual, adversarial, and hybrid bandit algorithms
+ framework to evaluate contextual, adversarial, and hybrid bandit algorithms
```

## 7. Next item

No next item is present in the uploaded `paper_feedback_tracker.md`. Do not infer Item 2 from older trackers, previous review queues, or unrelated repository files.
