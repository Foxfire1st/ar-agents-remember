# dashboard/src/panels/review/walkStore.FAM-F00001Continued.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review of the family "FAM-F00001" (`GET /api/review/intent`) for leaf `260101-TRV-L1`, as served, continued: the request names `pageOf=family_members`, the server's own `pageSize=2` and the cursor that `walkStore.sharedPage.captured.json` published for this family's before side.

## Code Commentary

### What the body holds

- `state` is `review`; the subject is family `338785bb-9701-50e9-a383-ff33746d5bc0`. The family context is `partial` with 1 family.
- Family "FAM-F00001" (state `partial`): 2 of 8 members on the before side and 2 of 9 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 4 member occurrences it describes are 2 `implementation`, 1 `unknown`, 1 `unchanged`. The roster pages are not complete (`continued` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
- The answer is a page of `family_members` in state `continued`.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`ReviewSurface.walkStore.test.tsx` serves it for every review request that carries a `continuation` parameter (`CONTINUED`), and `walkedTree.test.ts` folds its payload.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkStore.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (37,642 bytes).
- The body is a served answer over the store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: the live leaf `260101-TRV-L1` of master `260101_tree_review` over four Git trees; the receipt's `comparison` field). It is not current project knowledge; its identifiers and blobs are that world's.

## Evidence

- The served answer, whole. [3]
- Its receipt row: route, parameters, status, hash and size. [4]
