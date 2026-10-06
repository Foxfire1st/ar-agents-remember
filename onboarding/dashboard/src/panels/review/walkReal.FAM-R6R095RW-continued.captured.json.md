# dashboard/src/panels/review/walkReal.FAM-R6R095RW-continued.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review of the family "Coherent intent and source review" (`GET /api/review/intent`) for leaf `260928-MIK-L33`, as served, continued: the request names `pageOf=family_members`, the server's own `pageSize=2` and the cursor that `walkReal.INV-2TQGXFAX-page2.captured.json` published for this family's before side.

## Code Commentary

### What the body holds

- `state` is `review`; the subject is family `b9f95278-5712-5867-aa87-6e225aed4d45`. The family context is `partial` with 1 family.
- Family "Coherent intent and source review" (state `partial`): 2 of 23 members on the before side and 2 of 24 on the after side. Its guarantee's change kind is `unchanged`, and the change kinds of the 4 member occurrences it describes are 1 `membership`, 3 `unchanged`. The roster pages are not complete (`continued` on the before side, `first_page` on the after side) and each publishes a continuation cursor.
- The answer is a page of `family_members` in state `continued`.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`ReviewSurface.walkPartial.test.tsx` serves it for every review request that carries a `continuation` parameter (`CONTINUED`).

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (45,881 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
