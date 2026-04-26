# Item 030 — Use `\cref` for section references

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 17 April, 7:33 am  
**Feedback:**

> Not a big deal, but you can reference easier using cref.

## Task

Replace manual section-style references like `\S\ref{...}` with `\cref{...}` where appropriate.

## Content in question

```tex
$\rightarrow$ \emph{Capacity semantics} (\eg $T$ vs. $T_b$, replay scale $s$; \S\ref{subsec:capacity})
```

## Proposed solution

```tex
$\rightarrow$ \emph{Capacity semantics} (\eg $T$ vs. $T_b$, replay scale $s$; \cref{subsec:capacity})
```

## Decision / status

**Accepted / done.** Use `\cref{subsec:capacity}` instead of manual `\S\ref{subsec:capacity}`.
