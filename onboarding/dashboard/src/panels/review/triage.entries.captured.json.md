# dashboard/src/panels/review/triage.entries.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The store-authored comparison's subject catalogue** (`GET /api/review/intent/entries`, 2,922 bytes; test evidence
for `ReviewSurface.triage.test.tsx`, the catalogue the mounted surface lists).

## Code Commentary

### Logic

- `state` `entries`: 18 subjects (3 families, 15 invariants) of leaf `260101-TRV-L1`.

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

- The catalogue's entries and totals. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
