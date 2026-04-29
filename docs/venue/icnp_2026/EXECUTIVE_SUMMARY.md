# ICNP Venue Prep — Executive Summary

## Venue fit

ICNP 2026 is a credible venue target for this paper. The 2026 CFP explicitly includes areas that align with our work:

- quantum networking;
- AI/ML to improve networks;
- network protocols for improving AI/ML;
- routing, measurement, management, reliability, security, and protocol design.

The paper should be framed as a **network protocol/control problem under quantum-network uncertainty**, not as a generic machine-learning paper. The learning methods should support the networking contribution.

## Critical deadlines from ICNP 2026

Verify against the official ICNP 2026 pages before submission, but current official pages list:

| Milestone | Date |
|---|---:|
| Title/abstract registration | May 15, 2026, AoE |
| Full paper submission | May 22, 2026, AoE |
| Notification | July 21, 2026 |
| Camera-ready | August 25, 2026 |

Official pages:

- https://icnp26.cs.ucr.edu/cfp.html
- https://icnp26.cs.ucr.edu/submission.html

## High-priority submission requirements

- IEEE conference format.
- US Letter paper.
- 10-point font.
- Two-column format.
- 10-page main paper limit, excluding references.
- Double-blind review.
- Well-marked appendices allowed outside the main paper in recent ICNP 2025/2026 instructions, but core claims should remain in the main 10 pages.
- Public artifacts are encouraged after acceptance, but public repo/Drive links should be removed or anonymized for double-blind review.

## Main manuscript implications

The ICNP version should:

1. switch to IEEE conference mode;
2. anonymize author and affiliation information;
3. remove public GitHub/Drive URLs from the blind manuscript;
4. compress background and related work aggressively;
5. keep the core contribution in the main 10 pages;
6. focus on the network-control/protocol story;
7. emphasize strong results, clean comparisons, and deployment guidance.

## Biggest risks

- Too much broad background before the specific protocol/control problem.
- Looking like a learning-method paper rather than an ICNP networking paper.
- Leaking identity through public repository/Drive links.
- Relying on appendices or artifacts for core claims.
- Leaving the distinction from existing neural/adversarial bandit quantum-network work too implicit.

## Best immediate action

Use `main.tex` as the ICNP working draft and treat this folder as the venue-prep reference pack. Before submitting, run a blind-review audit that checks author metadata, acknowledgments, self-citations, repo links, PDF metadata, page count, and figure/table readability.