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

**Meaning:** Threat names and notation must be understandable before the reader reaches Study Design. The solution is two-part: initially add a lightweight threat-regime table in the Introduction, then define technical symbols at first use in the contribution bullet. After page-budget review, the lightweight threat-regime table was commented out, while the contribution bullet was rewritten to avoid naked `OnlineAdaptive` terminology and to define `$T_b$`, `$s$`, and percentage points (`pp`) inline.

**Implementation:** `ICNP_2026_venue_draft.tex` now retains the intro threat table as a commented audit block due to page budget. The Capacity paradox contribution bullet defines base-horizon replay capacity (`$T_b$`), replay-capacity scale (`$s$`), and percentage points (`pp`) at first use, and replaces the naked `OnlineAdaptive` label with plain-language reactive adaptive disruption. The original Devroop comment is preserved as a `%` comment with a `% SOLVED:` note.

**Commits:**

- `0ecb3d2228676f86b7fca5d62d1ec51ae4cfea4d`
- `d0df195a5509f5f482dcba1b5ed554cd5fe5eb78`
- `22ee8570e798d42bdc41a5ca30e0e75645479c03`
- `8e97e03daf443f0351627f8bd434e33e2cedf58d`

### 5. Apply first-use abbreviation rule across active sections

**Ask:** Remove rendered reviewer comments asking “what is ...?” or “define ...?” by defining symbols/abbreviations at first use in the section.

**Meaning:** Technical notation should not be removed or diluted. At first use, the paper should write meaning first, then symbol/abbreviation in parentheses; afterward the abbreviation can be reused normally.

**Implementation:** Updated `ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex` and `ICNP_VENUE_PREP/RESULTS_VALIDATED_STAGING.tex`.

**Resolved items:**

- `\shee{what is S?}`: defined the number of independent runs (`$S$`) at first use.
- `\shee{Define n}`: defined ARIMA warmup window size (`$n$`) at first use.
- `\shee{Define S}`: reused the previously defined repeated-run count (`$S$`) and added a `% SOLVED:` note.
- `\devroop{what is CV?}`: defined coefficient of variation (`CV`) at first use in Results.
- Added first-use wording for replay-capacity scale factor (`$s$`), current-horizon replay capacity (`$T$`), base-horizon replay capacity (`$T_b$`), and percentage points (`pp`) in active Study Design/Results sections.

**Verification:** Searches for `what is CV`, `Define S`, `Define n`, and `what is S` return no active hits.

**Commits:**

- `3e078b10771782087305b06d442b182634895170`
- `7e33c9643ce7e6e14c67b0705469890d35cf600c`

## Remaining high-priority items

### 6. Add the missing graph if page space allows

Status: Pending.

### 7. Address Dan’s remaining draft comments and mark resolved comments complete

Status: Pending.
