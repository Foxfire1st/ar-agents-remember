# dashboard/src/panels/review/walkReal.entries.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The subject catalogue (`GET /api/review/intent/entries`) of leaf `260928-MIK-L33`, as served.

## Code Commentary

### What the body holds

- `state` is `entries`: 129 subjects, of which 18 families and 111 invariants.

### Use

`walk.test-utils.tsx` serves it as the subject catalogue of the real-data world, which `ReviewSurface.walk.test.tsx`, `ReviewSurface.walkFresh.test.tsx`, `ReviewSurface.walkPartial.test.tsx` and the key case of `ReviewSurface.navigation.test.tsx` use.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (19,949 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
