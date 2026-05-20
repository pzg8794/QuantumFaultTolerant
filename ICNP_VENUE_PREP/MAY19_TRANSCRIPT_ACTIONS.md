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

### 3. Reference figures from RQ claim text

**Ask:** Keep captions descriptive and place figure references where the RQ claims are stated in the body text.

**Meaning:** Readers should connect each RQ claim to the figure evidence from the claim sentence itself, not from caption meta-language.

**Implementation:** Updated `ICNP_2026_venue_draft.tex` so RQ1, RQ2, and RQ3 claim text references the active figure labels.

**Labels used:** `fig:main_performance_summary`, `fig:threat_penalty_escalation`, `fig:robustness_floor`, `fig:capacity_paradox`, and `fig:deployment_guidance`.

**Commit:** `4589b30538fc92ee38898177ccde331c40563383`

### 4. Clarify Introduction threat regimes and capacity-paradox bullet

**Ask:** Address the unresolved Devroop comment that `OnlineAdaptive`, `$s$`, and replay shorthand were not understandable in the Introduction.

**Meaning:** Threat names and notation must be understandable before the reader reaches Study Design. The solution is two-part: add a lightweight threat-regime table in the Introduction and define symbols at first use in the contribution bullet.

**Implementation:** Added `tab:intro_threat_regimes` in `ICNP_2026_venue_draft.tex`, defining Baseline, Stochastic, Markov, Adaptive, and OnlineAdaptive in one line each. Rewrote the Capacity paradox contribution bullet to define base-horizon replay capacity (`$T_b$`), replay-capacity scale (`$s$`), and worst-case efficiency floor at first use. Removed the live `\devroop{...}` comment.

**Commit:** `0ecb3d2228676f86b7fca5d62d1ec51ae4cfea4d`

## Remaining high-priority items

### 5. Apply first-use abbreviation rule across sections

Status: Pending. Search section-by-section for symbols/abbreviations such as `$s$`, `$S$`, `$T_b$`, `$T$`, `CV`, `floor`, and scenario labels, then ensure first use follows meaning-first notation.

### 6. Add the missing graph if page space allows

Status: Pending.

### 7. Address Dan’s remaining draft comments and mark resolved comments complete

Status: Pending.
