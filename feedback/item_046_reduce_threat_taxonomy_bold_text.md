# Item 046 — Reduce excessive bold formatting in threat taxonomy

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 19 April, 5:01 pm  
**Feedback:**

> I think that you're overdoing it with all of the bold text

## Task

Reduce excessive bold formatting in the threat taxonomy so the section reads more cleanly.

## Content in question

The threat taxonomy uses bold both for regime labels and explanatory phrases, including:

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

A ready-to-apply patch was added at:

```text
patches/item_046_reduce_threat_taxonomy_bold_text.patch
```

## Decision / status

**Patch prepared.** Apply the patch to `main.tex` once local repository access is available. The GitHub connector repeatedly truncated `main.tex`, so the manuscript itself was not overwritten to avoid corrupting the paper.