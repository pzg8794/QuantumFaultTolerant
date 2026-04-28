# ICNP Official Guidelines — Working Notes

## Official pages to use as source of truth

- ICNP main series page: https://www.ieee-icnp.org/
- ICNP 2026 Call for Papers: https://icnp26.cs.ucr.edu/cfp.html
- ICNP 2026 submission instructions: https://icnp26.cs.ucr.edu/submission.html
- ICNP 2025 Call for Papers: https://icnp25.cs.ucr.edu/cfp.html
- ICNP 2025 submission instructions: https://icnp25.cs.ucr.edu/submission.html

## 2026 dates listed by the official CFP/submission pages

| Item | Deadline |
|---|---:|
| Title and abstract registration | May 15, 2026, AoE |
| Full paper submission | May 22, 2026, AoE |
| Notification | July 21, 2026 |
| Camera-ready | August 25, 2026 |

## Topic fit from the ICNP CFP

The ICNP CFP covers network protocols broadly. Topics directly relevant to this paper include:

- quantum networking;
- AI/ML for improving networks;
- network protocols for improving AI/ML;
- network security, reliability, and robustness;
- routing, forwarding, measurement, and management;
- protocol design, implementation, and evaluation.

For this manuscript, the strongest framing is:

> Threat-aware evaluation and deployment guidance for quantum entanglement routing protocols under stochastic, structured, and adaptive disruption.

Avoid framing it as:

> A generic comparison of bandit algorithms.

## Format requirements to verify before submission

Current ICNP 2026 pages indicate:

- IEEE conference format.
- US Letter paper.
- 10-point font.
- Two-column format.
- 10-page main paper limit, excluding references.
- Double-blind review.
- Submissions through the official ICNP submission site, likely HotCRP.

Before final submission, verify:

- whether appendices are allowed and how reviewers access them;
- whether supplementary artifacts can be linked during review;
- whether arXiv/preprint policy has changed;
- whether page limit excludes only references or also appendices;
- whether author names must be removed from PDF metadata;
- whether acknowledgments must be removed.

## Double-blind implications

The manuscript should not identify the authors or institution during review. Remove or anonymize:

- author names and affiliations;
- acknowledgments;
- public GitHub repository links;
- public Google Drive links;
- self-identifying project names;
- PDF metadata;
- self-citations written as “our previous work” or similar.

Use neutral phrasing:

```tex
The anonymized artifact package will be released upon acceptance.
```

or:

```tex
An anonymized artifact package is prepared and will be made available according to the conference artifact policy.
```

## Artifact policy working interpretation

Recent ICNP pages encourage accepted papers to release artifacts publicly and provide an artifact badge process for accepted papers. For blind submission, do not include identifying artifact links unless the current CFP explicitly permits anonymized artifact submissions.

Recommended blind-submission wording:

```tex
For double-blind review, artifact links are omitted. The artifact package includes the scripts, configuration files, and run-level summaries required to reproduce the reported tables and figures, and will be released according to the conference artifact policy.
```

## Camera-ready considerations

After acceptance, restore:

- author names;
- affiliations;
- acknowledgments;
- public repository URL;
- shared Drive or artifact DOI if allowed;
- camera-ready artifact badge wording if applicable.

## Submission-system checklist

Before pressing submit:

- Confirm title/abstract registered by May 15, 2026 AoE.
- Confirm full manuscript uploaded by May 22, 2026 AoE.
- Confirm PDF compiles with embedded fonts.
- Confirm PDF is IEEE conference format.
- Confirm no author metadata remains.
- Confirm page count is within the limit.
- Confirm all references compile.
- Confirm no reviewer comments, TODOs, highlights, or internal notes remain.
- Confirm figures and tables are legible in two-column print.