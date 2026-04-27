# Item 064 — Add cross-reference to testbed comparison section

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:18 am  
**Feedback:**

> add_circle  
> Added: `\Cref{sec:testbed_comparison}`

## Task

Review Dan's added cross-reference to the testbed comparison section.

## Content in question

```tex
\Cref{sec:testbed_comparison}
```

## Proposed solution

Accept the reference if the section label exists exactly as:

```tex
\label{sec:testbed_comparison}
```

If the label exists, keep Dan's addition. If the label does not exist or differs in capitalization, update either the label or the reference so they match.

## Decision / status

**Accepted / done.** Keep the `\Cref{sec:testbed_comparison}` reference once the label is verified.