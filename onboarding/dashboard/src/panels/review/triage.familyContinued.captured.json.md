# dashboard/src/panels/review/triage.familyContinued.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-F00001's roster continuation** (`pageOf=family_members` with the first page's cursor, 37,639 bytes; test
evidence for `changeTriage.test.ts`: an admitted walk keeps every returned member's facts).

## Code Commentary

### Logic

- The continuation's `change_kinds` describes the member occurrences this response returned (four), still with
  `members_total` 9; `mergeChangeKinds` unions them with the first page's.

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

- The continued family context with its facts. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
