# dashboard/src/panels/review/triage.shared.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The shared member INV-FFFFFF's review** (`selectorKind=invariant`, 167,361 bytes; test evidence for
`changeTriage.test.ts` and `FamilyTree.triage.test.tsx`: one member in two families).

## Code Commentary

### Logic

- Two families: FAM-F00001 (guarantee `unchanged`, INV-FFFFFF `unchanged`) and FAM-F00002 (guarantee `intent`: its
  guarantee text changed; INV-FFFFFF `membership` where it joined, INV-PPPPPP `intent` with `text_differs`, INV-EEEEEE
  `unchanged`).

### Conventions

Keep the captured bytes and their receipt intact; a recapture rewrites both.

### Invariants And Boundaries

The body is served over the SYNTHETIC store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: a live leaf `260101-TRV-L1` of master `260101_tree_review` over four real Git trees), not current project knowledge; its identities, blobs and scratch paths are that world's.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R33@v1` (adopting `ICR-R32@v1`) and the architect's rulings in `33_review-triage-order-and-change-kind-badges.json` live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Both families' facts: unchanged in one, membership where it joined, the revised guarantee. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
