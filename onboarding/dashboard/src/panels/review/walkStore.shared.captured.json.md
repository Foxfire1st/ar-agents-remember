# dashboard/src/panels/review/walkStore.shared.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review of the invariant INV-FFFFFF (`GET /api/review/intent`) for leaf `260101-TRV-L1`, as served.

## Code Commentary

### What the body holds

- `state` is `review`; the subject is invariant `e701c262-50a6-553b-bab6-691caed0fb04`. The family context is `recorded` with 2 families.
- Family "FAM-F00001" (state `recorded`): 8 of 8 members on the before side and 9 of 9 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 9 member occurrences it describes are 2 `intent`, 3 `implementation`, 1 `unknown`, 3 `unchanged`. Both roster pages are complete and publish no cursor.
- Family "FAM-F00002" (state `recorded`): 2 of 2 members on the before side and 3 of 3 on the after side. Its guarantee's change kind is `intent`, and the change kinds of the 3 member occurrences it describes are 1 `intent`, 1 `membership`, 1 `unchanged`. Both roster pages are complete and publish no cursor.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`ReviewSurface.walkStore.test.tsx` serves it for the shared member (`SHARED`) unless a case asks for the first page.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkStore.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (167,364 bytes).
- The body is a served answer over the store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: the live leaf `260101-TRV-L1` of master `260101_tree_review` over four Git trees; the receipt's `comparison` field). It is not current project knowledge; its identifiers and blobs are that world's.

## Evidence

- The served answer, whole. [3]
- Its receipt row: route, parameters, status, hash and size. [4]
