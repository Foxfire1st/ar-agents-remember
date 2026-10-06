# dashboard/src/panels/review/walkReal.lane.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The unexplained-changes lane (`GET /api/review/trees` with `lane=files`, comparison 1) of leaf `260928-MIK-L33`, as served.

## Code Commentary

### What the body holds

- `state` is `trees`. The lane is `measured`: 4 changed files, 4 attributed, 0 unexplained and 0 of unknown attribution.
- The four files are `FamilyReviewCenter.tsx`, `FamilyTree.tsx`, `ReviewSurface.tsx` and `familyWalkMerge.ts` under `dashboard/src/panels/review/`.

### Use

`ReviewSurface.walkFresh.test.tsx` serves it (`serveTreeRoutes`) for a `/trees` request that names a lane.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (3,239 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
