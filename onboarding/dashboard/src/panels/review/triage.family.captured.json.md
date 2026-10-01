# dashboard/src/panels/review/triage.family.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**FAM-F00001's review on the store-authored comparison** (`selectorKind=family`, 147,276 bytes; test evidence for
`changeTriage.test.ts`, `FamilyTree.triage.test.tsx` and `ReviewSurface.triage.test.tsx`).

## Code Commentary

### Logic

- One family, FAM-F00001, with all nine members returned and `change_kinds`: guarantee `unchanged`, `members_total`
  9, and one occurrence per member: INV-AAAAAA `intent` `+impl +unknown`, INV-BBBBBB and INV-CCCCCC `implementation`,
  INV-DDDDDD `implementation` `+test +unknown`, INV-GGGGGG `unknown` (its reasons name RLZ-G00001's blobs),
  INV-HHHHHH `intent` `+membership`, and INV-EEEEEE, INV-FFFFFF and INV-KKKKKK `unchanged`; each with
  `authored_position`, `evidence`, `unknown_reasons` and `membership_reasons`.
- The limitations name `review:trees:1`.

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

- The family context with its change facts. [1]
- The comparison token. [2]
- The receipt row for this body. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
