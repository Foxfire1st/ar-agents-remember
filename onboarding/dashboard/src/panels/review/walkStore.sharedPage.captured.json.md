# dashboard/src/panels/review/walkStore.sharedPage.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review of the invariant INV-FFFFFF (`GET /api/review/intent`) for leaf `260101-TRV-L1`, as served, asked with the server's own `pageSize=2`.

## Code Commentary

### What the body holds

- `state` is `review`; the subject is invariant `e701c262-50a6-553b-bab6-691caed0fb04`. The family context is `partial` with 2 families.
- Family "FAM-F00001" (state `partial`): 2 of 8 members on the before side and 2 of 9 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 2 member occurrences it describes are 1 `implementation`, 1 `unknown`. The roster pages are not complete (`first_page` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
- Family "FAM-F00002" (state `partial`): 2 of 2 members on the before side and 2 of 3 on the after side. Its guarantee's change kind is `intent`, and the change kinds of the 2 member occurrences it describes are 1 `intent`, 1 `unchanged`. The roster pages are not complete (`first_page` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`ReviewSurface.walkStore.test.tsx` serves it for the shared member when a case sets `useFirstPage` (`SHARED_PAGE`), and `walkedTree.test.ts` folds its payload.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkStore.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (49,980 bytes).
- The body is a served answer over the store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: the live leaf `260101-TRV-L1` of master `260101_tree_review` over four Git trees; the receipt's `comparison` field). It is not current project knowledge; its identifiers and blobs are that world's.

## Evidence

- The served answer, whole. [3]
- Its receipt row: route, parameters, status, hash and size. [4]
