# Item 061 — Add `Bandit` descriptor

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:16 am  
**Feedback:**

> add_circle  
> Added: `Bandit`

## Task

Review Dan's tracked insertion of `Bandit` into a table/header label.

## Content in question

Likely table/header wording such as:

```tex
\textbf{Bandit Family} & \textbf{Algorithm} & \textbf{Avg Eff (\%)} & \textbf{Gap (\%)} & \textbf{Floor (\%)} & \textbf{Exp. Winner} \\
```

## Proposed solution

Accept the addition. `Bandit Family` is clearer than just `Family`, because the table groups routing strategies by bandit model family.

## Decision / status

**Accepted / done.** Use `Bandit Family` where the table groups algorithms by bandit model family.