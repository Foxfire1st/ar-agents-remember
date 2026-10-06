# dashboard/src/panels/review/walkStore.entries.captured.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The subject catalogue (`GET /api/review/intent/entries`) of leaf `260101-TRV-L1`, as served.

## Code Commentary

### What the body holds

- `state` is `entries`: 18 subjects, of which 3 families and 15 invariants.

### Use

`ReviewSurface.walkStore.test.tsx` serves it as the subject catalogue.

### Boundaries

- The body is one captured answer of the route. Its receipt is `walkStore.capture-provenance.json`, which records the route, the parameters, the status, the hash and the size of the capture; the receipt's `sha256` and `bytes` for this file match the file (2,922 bytes).
- The body is a served answer over the store-authored world of `mcp/tests/test_review_change_kinds.py` (`build_world`: the live leaf `260101-TRV-L1` of master `260101_tree_review` over four Git trees; the receipt's `comparison` field). It is not current project knowledge; its identifiers and blobs are that world's.

## Evidence

- The served answer, whole. [3]
- Its receipt row: route, parameters, status, hash and size. [4]
