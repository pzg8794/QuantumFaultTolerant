# ICNP Author Kit and Formatting Notes

## Official template source

Use the official IEEE conference template source linked by ICNP:

- IEEE conference templates: https://www.ieee.org/conferences/publishing/templates
- ICNP 2026 submission instructions: https://icnp26.cs.ucr.edu/submission.html

## Required manuscript format

The official ICNP 2026 submission page states that papers must be:

- written in English;
- no more than 10 pages in double-column format;
- standard margins;
- 10-point font;
- US Letter, 8.5 x 11 inch;
- IEEE formatting requirements;
- PDF compatible with standard Acrobat tools;
- printable in black and white;
- author names and affiliations removed for double-blind review.

## LaTeX class setting

Use IEEEtran conference mode. The safest starting point is:

```tex
\documentclass[10pt,conference]{IEEEtran}
```

or, if the IEEE/ICNP checker expects explicit letterpaper:

```tex
\documentclass[10pt,conference,letterpaper]{IEEEtran}
```

Do not modify margins, line spacing, or column widths to fit content. ICNP warns that template violations may be rejected without review.

## Abstract limit

ICNP 2026 submission instructions state that the abstract must be fewer than 250 words.

Action:

```bash
# quick rough abstract word count after extracting abstract text manually
wc -w abstract.txt
```

## Page limit interpretation

ICNP 2026 states:

- maximum 10 pages for the submitted paper body;
- figures and tables count within the 10 pages;
- unlimited pages for references and appendices;
- longer submissions will not be reviewed.

Working rule for us:

- Main story, all key claims, and all reviewer-needed evidence must fit in the first 10 pages.
- Appendices can hold extra tables, extra runs, implementation details, and artifact details.
- Do not rely on appendix-only material to justify the main claim.

## PDF checker risk areas

Before submission, check:

- PDF is US Letter, not A4.
- Fonts are embedded.
- No Type 3 fonts.
- Figures are readable in black and white.
- No overfull boxes crossing margins.
- No links that identify authors in the blind version.
- No source filenames embedded in the PDF that reveal identity.

## Recommended ICNP LaTeX cleanup

Before the submission build:

- Remove `\todo`, `\dan`, `\devroop`, `\piter`, and reviewer comment macros from rendered text.
- Remove `\hl{}` question marks or unresolved highlights.
- Remove acknowledgments from the blind version.
- Remove author names and affiliations.
- Remove public artifact URLs from the blind version.
- Keep `\cref`/`\Cref` references consistent.
- Make legends at least `\scriptsize` when possible.
- Ensure all figures are readable in grayscale.

## Recommended build variants

Use one source file if possible, but consider a simple blind-review toggle:

```tex
\newif\ificnpblind
\icnpblindtrue

\ificnpblind
\author{Anonymous Authors}
\else
\author{First Author, Second Author, and Third Author}
\fi
```

For artifact links:

```tex
\ificnpblind
For double-blind review, artifact links are omitted. The artifact package will be released according to the conference artifact policy.
\else
All source code, datasets, and experiment scripts are available at \url{...}.
\fi
```

This prevents us from manually deleting/restoring links multiple times.