# Journal Submission Readiness Checklist

Use this checklist after the ICNP version is stabilized. It is written for a fuller journal submission, likely IEEE/ACM Transactions on Networking (ToN), but it can be adapted to another networking journal.

## 1. Target and positioning

- [ ] Confirm primary journal target and backup journal target.
- [ ] Download and review the target journal author instructions.
- [ ] Confirm page limits, formatting, open-access options, artifact policies, and supplemental-material rules.
- [ ] Decide whether the journal manuscript extends the ICNP version or is prepared independently.
- [ ] Write a one-paragraph journal positioning statement.
- [ ] Decide how to describe the relationship to the ICNP submission if both are active.

## 2. Core story and contribution scope

- [ ] State the central journal contribution in one paragraph.
- [ ] Separate conference-sized contributions from journal-expanded contributions.
- [ ] Make the novelty over Huang et al. / EXPNeuralUCB explicit.
- [ ] Make the novelty over Wang et al., Li et al., Liu et al., and Chaudhary et al. explicit.
- [ ] Explain why allocator and replay/capacity semantics are first-class routing variables.
- [ ] Present the capacity paradox as a major empirical insight, not a side observation.
- [ ] Convert deployment guidance into a stronger journal-level takeaway.

## 3. Related work expansion

- [ ] Expand quantum routing literature beyond the compressed ICNP version.
- [ ] Add a structured comparison table of quantum-routing papers.
- [ ] Add a structured comparison table of bandit/online-learning assumptions.
- [ ] Explain which works are stochastic, contextual, adversarial, predictive, or hybrid.
- [ ] Distinguish routing protocols from evaluation frameworks.
- [ ] Distinguish online learning under feedback from offline optimization.
- [ ] Include UF-related work comparison in a dedicated paragraph or subsection.

## 4. System model and problem formulation

- [ ] Ensure notation is introduced before use.
- [ ] Verify all variables are consistent across sections.
- [ ] Formalize path selection, qubit allocation, and threat availability in one coherent model.
- [ ] Clearly define the reward/efficiency metric.
- [ ] Define allocator policies and capacity/replay semantics rigorously.
- [ ] Include the system-model diagram if it remains useful.
- [ ] Include a concise statement of assumptions and limitations.

## 5. Algorithm and framework description

- [ ] Explain all baseline bandit families at the right level of detail.
- [ ] Describe pursuit-neural hybrid policies clearly.
- [ ] Explain how EXPNeuralUCB is used as a comparator.
- [ ] Include pseudocode only if it clarifies the framework.
- [ ] Move implementation-only details to appendix if they interrupt the main argument.
- [ ] Confirm algorithm names are consistent across tables, figures, and text.

## 6. Experimental suite

- [ ] Include the full 3-run, 5-run, and 10-run suite status.
- [ ] Decide what belongs in the main paper versus appendix/supplement.
- [ ] Document all topologies, testbeds, and dataset sources.
- [ ] Document all threat regimes and rationale.
- [ ] Document all allocator policies and rationale.
- [ ] Document all capacity scales and rationale.
- [ ] Include random seed and reproducibility details.
- [ ] Ensure tables can be regenerated deterministically from scripts.

## 7. Results and ablations

- [ ] Keep the main result table concise and readable.
- [ ] Include scenario-aggregated efficiency comparisons.
- [ ] Include worst-case robustness floors.
- [ ] Include allocator/capacity ablations.
- [ ] Include threat-regime breakdowns.
- [ ] Include cross-testbed validation.
- [ ] Include scale/topology sensitivity.
- [ ] Include statistical uncertainty where available.
- [ ] Explain any counterintuitive results, especially the capacity paradox.
- [ ] Include negative or limitation results rather than hiding them.

## 8. Reproducibility and artifacts

- [ ] Decide whether artifact links are public at submission time.
- [ ] Ensure repository is clean, documented, and runnable.
- [ ] Provide a README for reproducing key tables/figures.
- [ ] Provide scripts to regenerate manuscript-facing metrics.
- [ ] Provide dataset manifests and checksums if possible.
- [ ] Document software dependencies and environment.
- [ ] Confirm shared Drive materials are organized or replaced by stable artifact hosting.
- [ ] Consider Zenodo/DOI for journal archival version.

## 9. Writing and presentation polish

- [ ] Remove all reviewer comments and TODOs.
- [ ] Remove dead/commented alternate versions.
- [ ] Replace internal labels such as Paper 2 with reader-facing references.
- [ ] Use consistent macros for RQs and paper/testbed references.
- [ ] Ensure figures are readable in grayscale.
- [ ] Ensure legends and labels are not too small.
- [ ] Shorten captions and make them takeaway-first.
- [ ] Ensure every figure/table is referenced in text.
- [ ] Ensure every section has a clear purpose.

## 10. Journal-specific final checks

- [ ] Confirm author information is final.
- [ ] Confirm acknowledgments and funding text.
- [ ] Confirm conflicts of interest or data-availability statements if required.
- [ ] Confirm ORCID requirements if applicable.
- [ ] Confirm bibliography style.
- [ ] Confirm figure resolution requirements.
- [ ] Confirm supplementary-material upload requirements.
- [ ] Run final spell/grammar pass.
- [ ] Compile clean PDF.
- [ ] Save final source snapshot before submission.

## 11. Decision log

Use this section to track major journal decisions.

| Date | Decision | Owner | Notes |
|---|---|---|---|
| 2026-04-28 | Prepare ICNP version first, then expand into journal version | Team | Journal version can include broader suite, ablations, and UF comparison. |
