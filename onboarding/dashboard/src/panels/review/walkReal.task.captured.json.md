# dashboard/src/panels/review/walkReal.task.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The task-context review (`GET /api/review/intent` with no subject) of leaf `260928-MIK-L33`, as served.

## Code Commentary

### What the body holds

- `state` is `review` with `selection_state` `task_context`. The family context is `no_subject_selected` with no family.
- The source inventory lists 4 changed files.
- The limitations name `review:trees:1`, so the review is a tree comparison.

### Use

`walk.test-utils.tsx` serves it for every review request that names no subject.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkReal.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (15,110 bytes).
- The body is a served answer over a scratch copy: shared clones of the code repository at `e40d1f21` and of the converted memory repository at `40ae8395`, with the scratch leaf 260928-MIK-L33 that carries four scratch code edits and five scratch-authored curator edits (the receipt's `scratch` field). It is not current project knowledge; its identifiers, blobs and paths are the scratch copy's.

## Evidence

- The served answer, whole. [1]
- Its receipt row: route, parameters, status, hash and size. [2]
