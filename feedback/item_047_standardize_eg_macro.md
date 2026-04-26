# Item 047 — Standardize `e.g.,` to `\eg`

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 5:02 pm  
**Feedback:**

> edit  
> Changed: `e.g.,` to `\eg`

## Task

Standardize inline `e.g.,` usage to the existing LaTeX macro `\eg`.

## Content in question

Tracked edit in live prose where `e.g.,` appeared inline.

## Proposed solution

Accept the tracked edit wherever it appears in live prose:

```tex
\eg
```

instead of:

```tex
e.g.,
```

The macro is already defined in the preamble:

```tex
\newcommand{\eg}{\emph{e.g.,}\xspace}
```

## Decision / status

**Accepted / done.** Use `\eg` for style consistency.