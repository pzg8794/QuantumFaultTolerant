# `main.tex` to ICNP Submission Checklist

Use this checklist while converting the active `main.tex` into the ICNP submission draft.

## 0. Preserve source state

Already done:

```text
archive/pre-icnp-main-2026-04-27
```

Before major rewrites, use small commits with clear messages.

## 1. Switch to ICNP/IEEE conference format

Target:

```tex
\documentclass[10pt,conference]{IEEEtran}
```

Check after compiling:

- 10-point font.
- Two columns.
- US Letter page size.
- No margin hacks.
- No illegal spacing reductions.

## 2. Blind review conversion

Remove or anonymize:

- author names;
- affiliations;
- acknowledgments;
- public repo URL;
- public Drive URL;
- self-identifying artifact language;
- PDF metadata;
- internal comments.

Suggested blind artifact wording:

```tex
For double-blind review, artifact links are omitted. The artifact package includes the scripts, configuration files, and run-level summaries needed to reproduce the reported tables and figures, and will be released according to the conference artifact policy.
```

## 3. Page-budget strategy

Main paper limit: 10 pages excluding references.

Recommended allocation:

| Section | Target |
|---|---:|
| Introduction | 1.0-1.25 pages |
| Related Work | 0.75-1.0 page |
| System Model / Problem | 1.0-1.25 pages |
| Framework / Algorithms | 1.0-1.25 pages |
| Experimental Setup | 1.0 page |
| Results | 2.5-3.0 pages |
| Discussion / Deployment Guidance | 0.75-1.0 page |
| Conclusion | 0.25 page |

Move to appendix:

- broad quantum-network background;
- exhaustive algorithm taxonomy;
- extra tables;
- extended 10-run sweeps;
- full reproducibility details;
- non-central related-work comparisons.

## 4. Core ICNP story

The core story should be:

1. Quantum entanglement routing is a network-control problem under uncertainty.
2. Existing studies are hard to compare because threat, allocator, and replay assumptions differ.
3. We provide a matched-threat evaluation framework.
4. Robustness depends on the algorithm--allocator--capacity triad.
5. Neural/pursuit hybrids define the best robustness-efficiency frontier.
6. Replay capacity can backfire under adaptive adversaries, creating a capacity paradox.
7. The result is deployment guidance for quantum routing protocols.

## 5. Mandatory cleanup before submission

Search and remove/fix:

```text
TODO
\todo
\dan
\devroop
\piter
\shee
\hl{
??
XXX
Paper 2
Paper 7
Paper 8
Paper 12
\S\ref
```

Also verify:

- no broken references;
- no undefined citations;
- no duplicate figure/table labels;
- no overfull boxes in visible parts;
- all figures readable in two-column layout;
- no author-identifying URLs.

## 6. Public repository handling

Current non-blind text mentions:

- https://github.com/pzg8794/quantum_project_hub
- https://drive.google.com/drive/folders/0AK0VchnNyM-xUk9PVA

For ICNP blind submission, replace with anonymized wording. After acceptance, restore public links in camera-ready.

## 7. Related work compression

Keep only the comparisons needed to establish:

- what prior quantum-routing papers do;
- what prior bandit/learning-based routing papers do;
- why threat/allocator/replay assumptions are not directly comparable;
- what is new in our matched evaluation.

Cut or move:

- long literature selection details;
- broad bandit background;
- repeated contrasts;
- detailed excluded-work discussion.

## 8. Results prioritization

Main paper should emphasize:

- one main robustness/efficiency table;
- one figure showing threat escalation behavior;
- one figure/table for allocator-capacity interaction;
- one concise cross-testbed validation result;
- one deployment-guidance summary.

Move all other detailed tables to appendix.

## 9. Final submission checks

Before upload:

- Abstract under 250 words.
- Main content within 10 pages, excluding references.
- PDF generated from clean source.
- No hidden metadata identifying authors.
- All links safe for blind review.
- Title/abstract registered by May 15, 2026 AoE.
- Full paper uploaded by May 22, 2026 AoE.