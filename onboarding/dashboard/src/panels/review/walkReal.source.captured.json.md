# dashboard/src/panels/review/walkReal.source.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The content of one changed file (`GET /api/review/intent/source-content`) for leaf `260928-MIK-L33`, as served: `dashboard/src/panels/review/familyWalkMerge.ts` at the bound pair of code trees.

## Code Commentary

### What the body holds

- `state` is `content`. The expansion is of `dashboard/src/panels/review/familyWalkMerge.ts` (status `modified`, language `typescript`), between the code trees `e40d1f21` and `d3e51778`, with currentness `current`.

### Use

`ReviewSurface.walkFresh.test.tsx` serves it (`serveTreeRoutes`) for every `/source-content` request.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (15,582 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
