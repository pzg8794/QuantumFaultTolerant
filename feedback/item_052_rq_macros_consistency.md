# Item 052 — Define RQs as reusable LaTeX macros

## Feedback item

**Reviewer:** dan7800  
**Date/time:** 22 April, 6:14 am  
**Feedback:**

> I would make all of the RQs variable names so that if you change them once, they are constantly updated throughout the paper.

## Task

Define RQ labels/text as reusable LaTeX macros so repeated references stay consistent throughout the paper.

## Content in question

Research question labels and repeated references such as:

```tex
RQ1
RQ2
RQ3
```

## Proposed solution

Add macros near the custom command section, for example:

```tex
\newcommand{\RQOne}{\textbf{RQ1}\xspace}
\newcommand{\RQTwo}{\textbf{RQ2}\xspace}
\newcommand{\RQThree}{\textbf{RQ3}\xspace}
```

Then use them in RQ headings and repeated live references:

```tex
\subsubsection*{\emph{\RQOne}}
\subsubsection*{\emph{\RQTwo}}
\subsubsection*{\emph{\RQThree}}
```

## Decision / status

**Accepted / done.** Piter is applying and pushing the manuscript macro changes separately. Use RQ macros for live RQ labels/references; avoid editing old comments or blocked notes unnecessarily.