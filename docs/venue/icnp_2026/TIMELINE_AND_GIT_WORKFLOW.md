# ICNP Timeline and Git Workflow

## Official ICNP 2026 timeline

Verify with the official CFP before final submission:

| Milestone | Date |
|---|---:|
| Title/abstract registration | May 15, 2026, AoE |
| Full-paper submission | May 22, 2026, AoE |
| Notification | July 21, 2026 |
| Camera-ready deadline | August 25, 2026 |

## Suggested internal sprint plan

### Phase 1 — Venue conversion

Goal: make `main.tex` compile as a 10-page ICNP-style conference draft.

Tasks:

- IEEE conference mode.
- Blind-review author block.
- Remove public artifact links from blind build.
- Remove comments/TODOs/highlights.
- Confirm page count.

### Phase 2 — Content compression

Goal: cut non-central material and sharpen the ICNP story.

Tasks:

- Compress Introduction.
- Cut/merge Background.
- Compress Related Work.
- Keep System Model concise.
- Move extended tables to appendix.
- Keep only strongest results in main body.

### Phase 3 — Reviewer-proofing

Goal: make the paper convincing to ICNP reviewers.

Tasks:

- Rationale for threat taxonomy.
- Rationale for allocator selection.
- Clear distinction from Huang et al. / EXPNeuralUCB.
- Clean cross-testbed labels.
- Strong deployment takeaway.

### Phase 4 — Final submission build

Goal: produce a blind, compliant PDF.

Tasks:

- Compile cleanly.
- Check page count.
- Check undefined citations/references.
- Check PDF metadata.
- Check figure readability.
- Register title/abstract.
- Upload final PDF.

## Git workflow

Current pre-ICNP archive branch:

```text
archive/pre-icnp-main-2026-04-27
```

Recommended workflow:

```bash
git checkout main
git pull --ff-only origin main
# edit main.tex or supporting files
git add main.tex docs/venue/icnp_2026/
git commit -m "Prepare ICNP draft section X"
git push origin main
```

For risky large rewrites, use a branch:

```bash
git checkout -b icnp/rewrite-related-work
git push -u origin icnp/rewrite-related-work
```

## Overleaf sync warning

Overleaf Git sync can create timestamped branches when it cannot merge automatically, for example:

```text
overleaf-YYYY-MM-DD-HHMM
```

If this happens:

1. compare the Overleaf branch against `main`;
2. inspect whether it contains new content or only repeated changes;
3. merge content if needed;
4. if content already exists in `main`, record a no-op ancestry merge:

```bash
git fetch origin --prune
git checkout main
git pull --ff-only origin main
git merge -s ours --no-ff origin/overleaf-YYYY-MM-DD-HHMM -m "Record Overleaf updates as merged"
git push origin main
```

## Local files not to accidentally commit

Common local-only files:

- `main.pdf` generated locally;
- draft notes not intended for repo;
- temporary deep-research outputs;
- local trackers.

Before each push:

```bash
git status --short --branch
```

Commit only intended source/docs files.