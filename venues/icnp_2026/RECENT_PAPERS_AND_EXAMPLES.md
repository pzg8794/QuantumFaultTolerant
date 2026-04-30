# Recent ICNP Papers and Example Targets

This file records ICNP-style example papers to inspect while reshaping the manuscript. The point is not to copy structure mechanically, but to learn what recent ICNP papers tend to foreground: protocol problem, deployment motivation, system model, evaluation discipline, and clear networking relevance.

## Official proceedings links

- ICNP 2025 accepted papers: https://icnp25.cs.ucr.edu/program.html
- ICNP 2024 program/proceedings: https://ieee-icnp.org/2024/
- ICNP series page: https://www.ieee-icnp.org/
- IEEE Xplore ICNP proceedings search: https://ieeexplore.ieee.org/xpl/conhome/1000142/all-proceedings

## Example categories to collect

### 1. Routing / path selection / path control

Look for ICNP papers with:

- routing under failure or uncertainty;
- traffic engineering;
- adaptive path selection;
- congestion-aware or reliability-aware forwarding;
- path diversity and multipath control.

Use these to guide how we explain quantum routing as a network-control problem rather than as a pure ML benchmark.

### 2. ML for networking / learning-assisted protocols

Look for papers where ML is a component inside a protocol or control system. Extract how they present:

- the networking problem before the ML method;
- baselines and ablations;
- robustness/generalization across scenarios;
- deployment constraints and failure modes.

Our paper should follow this pattern: the bandit methods are instruments for robust quantum routing, not the entire contribution.

### 3. Security / adversarial networking / robustness

Look for papers on:

- adversarial traffic or attacks;
- protocol robustness;
- reactive defenses;
- measurement under adversarial or changing conditions.

Use these to frame the threat taxonomy as a networking contribution.

### 4. Quantum networking

ICNP 2026 explicitly lists quantum networking as an area. Search recent ICNP and adjacent IEEE/ACM networking venues for:

- quantum network routing;
- entanglement distribution protocols;
- quantum repeater control;
- QKD network protocols;
- quantum network simulation and benchmarking.

Even if ICNP has few prior quantum papers, this CFP topic creates room for our work if the story is framed around protocols and evaluation.

## Recent ICNP award/example anchors

The ICNP site lists award and program pages that can be used as style references. Collect PDFs from recent years and summarize:

- problem statement style;
- paper organization;
- evaluation depth;
- main contribution count;
- how figures/tables are used;
- how limitations are handled.

Example paper categories to inspect manually:

| Category | What to learn |
|---|---|
| Best paper / distinguished paper | What ICNP reviewers reward as clear contribution framing |
| ML-for-networking paper | How to justify ML without becoming ML-only |
| Security/robustness paper | How to define threat models and experimental stress tests |
| Routing/control paper | How to present system model and protocol-level evaluation |
| Measurement/benchmarking paper | How to justify datasets, reproducibility, and experimental scope |

## What to extract from each example

For each example paper, create a note with:

```text
Title:
Year:
Authors:
Link:
Problem framing:
Main contribution:
System model / protocol model:
Evaluation setup:
Baselines:
Figures/tables worth emulating:
How it handles limitations:
Lessons for our ICNP draft:
```

## Relevance to our manuscript

Our paper should emulate the strongest ICNP-style structure:

1. Start with a concrete network protocol/control failure mode.
2. Explain why current routing evaluations do not give deployment guidance.
3. Present the threat-aware evaluation framework as the contribution.
4. Keep the bandit taxonomy concise.
5. Focus results on actionable deployment guidance.
6. Move broad background, exhaustive tables, and less-central experiments to appendix or later journal version.

## Example-paper search queries

Use these queries in IEEE Xplore, ACM DL, Google Scholar, and the ICNP program pages:

```text
site:ieee-icnp.org ICNP learning network protocols routing
site:ieee-icnp.org ICNP machine learning networking protocol
site:ieee-icnp.org ICNP adversarial network protocol
site:ieee-icnp.org ICNP routing robustness
site:ieee-icnp.org ICNP quantum networking
"International Conference on Network Protocols" "machine learning" routing
"International Conference on Network Protocols" adversarial network
"International Conference on Network Protocols" quantum networking
```

## Paper-specific example needs

Prioritize examples that help answer these manuscript questions:

- How much background is acceptable before the first contribution?
- How do ICNP papers phrase protocol/control novelty?
- How detailed should threat models be in the main paper?
- How many baselines/experiments are enough for a 10-page paper?
- How do papers handle appendix-only extended results?
- How are artifacts described under double-blind review?