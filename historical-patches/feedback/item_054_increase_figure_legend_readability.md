# Item 054 — Increase figure legend/key readability

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:09 am  
**Feedback:**

> The key is likely going to be hard to see, make it bigger.

## Task

Increase the readability of the figure legend/key.

## Content in question

```tex
legend style={at={(0.5,-0.22)}, anchor=north},
```

## Proposed solution

Increase the legend font and improve legend layout, for example:

```tex
legend style={
    at={(0.5,-0.22)},
    anchor=north,
    font=\scriptsize,
    cells={anchor=west}
},
```

If needed for crowded legends, use two columns:

```tex
legend columns=2,
legend style={
    at={(0.5,-0.24)},
    anchor=north,
    font=\scriptsize,
    cells={anchor=west}
},
```

## Decision / status

**Accepted / done.** Increase the figure legend/key readability.