# dashboard/src/panels/review/walkReal.INV-2TQGXFAX.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review of the invariant INV-2TQGXFAX (`GET /api/review/intent`) for leaf `260928-MIK-L33`, as served.

## Code Commentary

### What the body holds

- `state` is `review`; the subject is invariant `09b76b4c-9d5e-50a2-8a4d-de1485e8911c`. The family context is `partial` with 2 families.
- Family "Coherent intent and source review" (state `partial`): 23 of 23 members on the before side and 24 of 24 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 24 member occurrences it describes are 2 `intent`, 4 `implementation`, 1 `membership`, 17 `unchanged`. The roster pages are not complete (`first_page` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
- Family "Comparison-bound unchanged realization context" (state `recorded`): 7 of 7 members on the before side and 7 of 7 on the after side. Its guarantee's change kind is `intent`, and the change kinds of the 7 member occurrences it describes are 7 `unchanged`. Both roster pages are complete and publish no cursor.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`walk.test-utils.tsx` serves it for the shared member (`SHARED`, the last of `CHANGES`), and `walkedTree.test.ts` folds its payload.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (223,559 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
