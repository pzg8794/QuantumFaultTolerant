# Item 046 — Reduce excessive bold formatting in threat taxonomy

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 5:01 pm  
**Feedback:**

> I think that you're overdoing it with all of the bold text

## Task

Reduce excessive bold formatting in the threat taxonomy so the section reads more cleanly.

## Content in question

The threat taxonomy used bold both for regime labels and explanatory phrases, including:

```tex
\textbf{five escalating threat regimes}
\textbf{benign-condition upper bound}
\textbf{4-state Markov chain}
\textbf{most-used path}
\textbf{exponentially weighted path usage}
\textbf{softmax targeting}
\textbf{learn and adapt in real time}
```

## Proposed solution

Keep bold only for the regime labels and remove bold from explanatory phrases in the body text.

## Applied manuscript change

Removed bold formatting from the threat-taxonomy body text while keeping the regime headings bold. The public `main` branch includes the manuscript update in commit `9762d51`.

## Decision / status

**Applied / done.** Excessive bold formatting was removed from the threat taxonomy body text.