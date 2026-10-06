# dashboard/src/panels/review/walkReal.file.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The per-file classification (`GET /api/review/trees` with `file=`, comparison 1) of `dashboard/src/panels/review/familyWalkMerge.ts` for leaf `260928-MIK-L33`, as served.

## Code Commentary

### What the body holds

- `state` is `trees`. The file's bucket is `attributed`: 1 hunk, 1 linked, 0 unexplained.
- The one hunk (line 121 on both sides) is `linked` to INV-ZS9ZS878 through entry RLZ-95V4M24E, on the before and on the after side, as a member of family FAM-R6R095RW.

### Use

`ReviewSurface.walkFresh.test.tsx` serves it (`serveTreeRoutes`) for the `/trees` request that names the file `dashboard/src/panels/review/familyWalkMerge.ts`.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (5,614 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
