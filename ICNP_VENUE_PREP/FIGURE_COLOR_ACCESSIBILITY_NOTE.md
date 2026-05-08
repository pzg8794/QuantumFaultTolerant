# Figure Color Accessibility Decision

## Confirmed venue requirement

The ICNP 2026 submission page does not prohibit color figures. It requires papers to display and print correctly with standard tools and printers, and it specifically says to make sure papers print well on black-and-white printers, especially plots and graphs.

Practical interpretation:

```text
Color is allowed, but color must not be the only visual cue.
Figures should remain distinguishable in grayscale / black-and-white printing.
```

## Applied decision

Figures should use color for readability and accessibility, while also using redundant cues such as line style, fill shade, direct labels, legends, threshold lines, and grouping.

For the network-topology figure, the active encoding is:

```text
P1: blue + solid
P2: red + dashed
P3: green + dotted
P4: orange + dash-dot
```

For generated result plots, the active encoding uses named palette colors already present in the draft:

```text
networkblue
envgreen
algorange
allocpurple
findingRed / findingOrange / findingGreen / findingBlue
```

This supports:

- easier visual distinction in color;
- fallback readability in grayscale or black-and-white printing;
- accessibility for readers who benefit from redundant visual cues.

## Active files changed

```tex
ICNP_2026_venue_draft.tex
ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex
ICNP_VENUE_PREP/generated_figures/*.tex
```

## Feedback marker handling

The visible Sheeraja comment in the caption was moved to a LaTeX source comment and marked solved:

```tex
% \shee{I think the colors in main.tex were easier to distinguish the paths. } -- SOLVED: Restored color coding while retaining distinct line styles so the topology remains readable in grayscale.
```
