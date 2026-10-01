# dashboard/src/panels/review/triageReal.family.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-R6R095RW's review ("Coherent intent and source review") on the real scratch leaf** (182,908 bytes; test
evidence for `FamilyTree.triageReal.test.tsx`).

## Code Commentary

### Logic

- All 24 members returned (the pages are `complete: false` because the read owner's page also counts realization
  items), guarantee `unchanged`, `members_total` 24: 2 `intent` (INV-2E8MG43K with `text_differs`; INV-ZS9ZS878 with
  `+impl`), 6 `implementation` (INV-BR5MTSTY, H8EM1VJR and VPX81HXV with `+unknown` for entries at an older recorded
  before-side blob; the stale-at-base repairs worded "re-anchored (stale at base)"), 1 `membership` (INV-2TQGXFAX), 15
  `unchanged` (INV-ZY0YMXMQ's carried entry among them).
- The limitations name `review:trees:2`.

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body describes the MIK-L33 worker's scratch copy under `/tmp/mik-l33-real` (memory `0b176f6b` converted with the worktree's `knowledge-convert` and committed as scratch `main` `0c3a0f83` with `Code-Commit` `904e804b`; the leaf's own code change and SCRATCH-AUTHORED knowledge edits), not current project knowledge; its line numbers, blobs and keys are the scratch tree's.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The family context with its change facts. [1]
- The comparison token. [2]
- The receipt row for this body. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
