# Consolidated Feedback Provenance

This file consolidates the reviewer/Overleaf feedback provenance that had previously been scattered across many one-item files under `feedback/`.

The detailed one-item markdown files were useful during live processing, but the cleaner long-term convention is:

- keep this single consolidated file for provenance;
- keep future feedback decisions in this file or another single dated consolidated file;
- avoid adding many separate `feedback/item_*.md` files;
- keep historical patch/provenance material under top-level `historical-patches/`, not under `archive/`.

## Feedback item inventory

| Item/file | Topic / status summary |
|---|---|
| `item_020_reproducibility_artifacts.md` | Reproducibility artifacts / repo and artifact availability. |
| `item_021_public_repo_link.md` | Public repository link. |
| `item_022_intro_reduction.md` | Introduction reduction / blocked or reduction-related handling. |
| `item_023_add_citation_entanglement_resource.md` | Add citation for entanglement resource statement. |
| `item_024_optional_remove_citation_for_space.md` | Optional citation removal for space. |
| `item_025_add_related_work_citations.md` | Add related-work citations. |
| `item_026_inline_quantum_routing_paragraph_cleanup.md` | Inline quantum-routing paragraph cleanup. |
| `item_027_add_problem_impact_sentence.md` | Add problem-impact sentence. |
| `item_028_framework_flowchart.md` | Framework flowchart. |
| `item_029_threat_taxonomy_context.md` | Threat taxonomy context. |
| `item_030_cref_reference_cleanup.md` | `\cref` reference cleanup. |
| `item_031_rewrite_check_covered_by_repo_artifacts.md` | Rewrite/check covered by repo artifacts. |
| `item_032_delete_stray_percent.md` | Delete stray percent marker. |
| `item_033_open_source_repository_bullet_duplicate.md` | Open-source repository bullet duplicate. |
| `item_034_added_percent_duplicate.md` | Added percent duplicate. |
| `item_035_anonymized_repo_duplicate.md` | Anonymized repository duplicate. |
| `item_036_background_reduction_blocked.md` | Background reduction blocked. |
| `item_037_background_related_work_refactor_blocked.md` | Background/related-work refactor blocked. |
| `item_038_problem_scope_quote_cleanup.md` | Problem-scope quote cleanup. |
| `item_039_design_rationale_citations.md` | Design rationale/citations. |
| `item_040_allocator_strategy_rationale.md` | Allocator-strategy rationale. |
| `item_044_threat_regime_rationale.md` | Threat-regime rationale. |
| `item_045_replace_benign_stochastic_wording.md` | Replace repeated benign wording. |
| `item_046_reduce_threat_taxonomy_bold_text.md` | Reduce excessive bold formatting in threat taxonomy. |
| `item_047_standardize_eg_macro.md` | Standardize `e.g.,` to `\eg`. |
| `item_048_rq_answers_vs_questions_blocked.md` | RQ answers versus question-only conflict; blocked. |
| `item_050_rq1_bold_formatting.md` | RQ label bold formatting. |
| `item_051_delete_outdated_rq_count.md` | Delete outdated RQ count. |
| `item_052_rq_macros_consistency.md` | RQ macro consistency. |
| `item_053_rq2_reword_done.md` | RQ2 rewording already done. |
| `item_054_increase_figure_legend_readability.md` | Increase figure legend readability. |
| `item_055_added_es_tracked_edit.md` | Accept tracked insertion of `es`. |
| `item_056_tiny_to_scriptsize_first.md` | Change `\tiny` to `\scriptsize`. |
| `item_059_delete_percent_near_testbed_section.md` | Delete percent marker near testbed section. |
| `item_061_add_bandit_descriptor.md` | Add `Bandit` descriptor. |
| `item_062_bandit_terminology_covered.md` | Use bandit terminology consistently where relevant. |
| `item_063_standardize_eg_macro_second.md` | Second `e.g.,` to `\eg` cleanup. |
| `item_064_add_testbed_comparison_cref.md` | Add `\Cref{sec:testbed_comparison}`. |

## Overleaf mapping / working queue files

| File | Purpose |
|---|---|
| `overleaf_feedback_working_review.md` | Working review queue. |
| `overleaf_feedback_content_mapping_correction.md` | Mapping correction notes. |
| `overleaf_feedback_content_in_question_mapping.md` | Content-in-question mapping notes. |
| `overleaf_feedback_queue_pending_content.md` | Pending-content queue. |

## Cleanup decision

- Top-level `historical-patches/` is now the canonical place for feedback/patch provenance.
- `archive/` should remain limited to manuscript checkpoints and legacy material.
- `archive/legacy-drafts/` is legacy/Dan-owned material and should not be touched during cleanup.
- Local helper `scripts/` and `tools/` are removed from the remote branch and ignored going forward.

## Notes

The original individual feedback files remain recoverable through git history. If a full physical cleanup is desired later, delete the scattered `feedback/item_*.md` files after confirming this consolidated record is sufficient.
