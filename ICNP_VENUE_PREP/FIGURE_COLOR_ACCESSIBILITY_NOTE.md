# Figure Color Accessibility Decision

## Venue check status

The ICNP submission URL was requested for checking whether figures must be grayscale-only. The page could not be reached from this environment due DNS resolution failure, so no definitive venue-specific grayscale prohibition was confirmed here.

## Applied decision

The topology figure was restored to color because no confirmed grayscale-only rule was available. To remain safe for print and accessibility, each route also keeps a distinct line style:

```text
P1: blue + solid
P2: red + dashed
P3: green + dotted
P4: orange + dash-dot
```

This supports:

- easier visual distinction in color;
- fallback readability in grayscale or black-and-white printing;
- accessibility for readers who benefit from redundant visual cues.

## Active file changed

```tex
ICNP_VENUE_PREP/STUDY_DESIGN_VALIDATED_STAGING.tex
```

## Feedback marker handling

The visible Sheeraja comment in the caption was moved to a LaTeX source comment and marked solved:

```tex
% \shee{I think the colors in main.tex were easier to distinguish the paths. } -- SOLVED: Restored color coding while retaining distinct line styles so the topology remains readable in grayscale.
```
