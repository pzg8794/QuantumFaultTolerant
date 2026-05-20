# May 19 Transcript Action Tracker

Source: 2026-05-19 team meeting on draft clarification, variable definitions, and caption revisions.

## Completed

### 1. Add compact notation/metrics table in Study Design

**Ask:** Define recurring notation and metrics so readers do not have to scroll back and forth when terms such as `CV`, `floor`, `s`, `S`, `T_b`, and `T` appear.

**Meaning:** The reviewers were not asking for a broad glossary. They wanted the confusing symbols and metrics defined before the paper uses them heavily.

**Implementation:** Added `tab:notation_metrics` near the start of `ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex`.

**Final scope:** Kept only high-value entries: `Oracle gap`, `Floor`, `CV`, `s`, `S`, `F_b`, `F_c`, `T_b`, and `T`. Removed lower-value rows for `Efficiency`, `Percentage points`, and `Run suite` to protect space.

**Commit:** `3522217db533ceef52e4193ed9ac4238cd95d6ef`

### 2. Clean up figure-caption claim language in active Results fragments

**Ask:** Remove caption wording such as “supports the RQ claim” while preserving the evidence and insight visible in the figure.

**Meaning:** Captions should state what the figure shows. The corresponding body claim should carry the `\cref{...}` evidence link, so the reader connects the claim to the figure from the text rather than from meta-commentary inside the caption.

**Implementation:** Updated active main-body Results figure captions in:

- `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`
- `ICNP_VENUE_PREP/RESULTS_VALIDATED_CROSS_TESTBED.tex`

**Labels verified and used/preserved:** `fig:main_performance_summary`, `fig:threat_penalty_escalation`, `fig:robustness_floor`, `fig:capacity_paradox`, `fig:deployment_guidance`, `fig:cross_testbed_confirmation`, plus their subfigure labels.

**Commits:**

- `d84943975fe8c5c567ae552cf57becfb2e236fca`
- `04c31ee43ada30ad5068dd353ae5bf3b0c1b9ba3`

**Note:** The top-level draft file `ICNP_2026_venue_draft.tex` still contains early RQ/contribution comments and should be patched separately. It is large enough that the current GitHub update tool risks a full-file overwrite if applied without a safe patch mechanism.

## Remaining high-priority items

### 3. Rewrite early RQ/contribution wording to avoid undefined shorthand

Status: Pending. The notation table reduces the definition problem, but the early contribution bullet still has reviewer comments about `OnlineAdaptive`, `$s$`, and replay shorthand.

### 4. Add the missing graph if page space allows

Status: Pending.

### 5. Address Dan’s remaining draft comments and mark resolved comments complete

Status: Pending.
