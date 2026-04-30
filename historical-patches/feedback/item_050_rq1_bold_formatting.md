# Item 050 — Bold RQ label formatting

## Feedback item

**Reviewer:** Devroop Kar  
**Date/time:** 22 April, 7:54 am  
**Feedback:**

> edit  
> Changed: `RQ1` to `\textbf{RQ1}`

## Task

Review whether the RQ label formatting should use bold text.

## Content in question

```tex
\subsubsection*{\emph{\textbf{RQ1}}}
```

## Proposed solution

Accept the change and keep formatting consistent across all RQs:

```tex
\subsubsection*{\emph{\textbf{RQ1}}}
\subsubsection*{\emph{\textbf{RQ2}}}
\subsubsection*{\emph{\textbf{RQ3}}}
```

## Decision / status

**Accepted / done.** Use bold RQ labels consistently.