# dashboard/src/panels/review/triage.familyPage.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-F00001's first bounded roster page** (`pageSize=2`, 34,067 bytes; test evidence for `changeTriage.test.ts` and
`FamilyTree.triage.test.tsx`: the partial family and its continuation stop).

## Code Commentary

### Logic

- Both sides' pages are incomplete; `change_kinds` describes only the two returned member occurrences, with
  `members_total` 9, so the breakdown reads "… of 2 returned (9 total)" and the family sorts no lower than `unknown`.

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

- The bounded family context with facts for the returned members only. [1]
- The receipt row for this body. [2]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
