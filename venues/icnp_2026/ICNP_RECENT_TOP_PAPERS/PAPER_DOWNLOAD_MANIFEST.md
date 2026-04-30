# ICNP Recent Paper Download Manifest

This manifest lists the minimum reference-paper set we want in this directory.

Direct download was not possible from the assistant runtime because public web/DNS access failed for the relevant hosts. Use this manifest to download PDFs manually from official ICNP program pages, IEEE Xplore, ACM DL, or author-hosted copies.

## Minimum set: three recent ICNP reference papers

| Slot | Target paper type | Why it matters for our manuscript | PDF filename |
|---|---|---|---|
| 1 | Recent ICNP ML/AI-for-networking paper | Shows how ICNP frames learning as part of a networking/protocol contribution rather than as standalone ML. | `01_recent_icnp_ml_for_networking.pdf` |
| 2 | Recent ICNP routing/path-control/traffic-engineering paper | Shows how ICNP papers present routing/control problems, system model, baselines, and deployment implications. | `02_recent_icnp_routing_or_traffic_engineering.pdf` |
| 3 | Recent ICNP security/robustness/adversarial-networking paper | Shows how ICNP papers justify threat models, robustness evaluation, and attack/defense assumptions. | `03_recent_icnp_security_or_robustness.pdf` |

## Optional fourth paper

| Slot | Target paper type | Why it matters | PDF filename |
|---|---|---|---|
| 4 | ICNP or adjacent quantum-networking paper | Direct topical bridge for quantum networking, if available. | `04_recent_icnp_or_adjacent_quantum_networking.pdf` |

## Manual download process

1. Open the ICNP 2025 and ICNP 2024 program/proceedings pages.
2. Search for accepted papers matching each slot.
3. Prefer papers marked best paper, distinguished paper, award candidate, or papers with strong relevance to routing/learning/robustness.
4. Download PDFs from official proceedings, IEEE Xplore, ACM DL, or author pages.
5. Save PDFs using the filenames above.
6. Fill out a note file per paper using `PAPER_NOTE_TEMPLATE.md`.

## Search queries

```text
site:icnp25.cs.ucr.edu ICNP 2025 machine learning networking PDF
site:ieee-icnp.org ICNP 2024 learning routing PDF
site:ieee-icnp.org ICNP robustness adversarial networking PDF
"ICNP 2025" "routing" "PDF"
"ICNP 2024" "machine learning" "networking" "PDF"
"International Conference on Network Protocols" "adversarial" "routing" PDF
"International Conference on Network Protocols" "quantum networking" PDF
```

## Notes after download

For each paper, record:

- title;
- year;
- venue;
- authors;
- source URL;
- why selected;
- lessons for our ICNP submission;
- figures/tables worth emulating;
- how it handles evaluation and limitations.
