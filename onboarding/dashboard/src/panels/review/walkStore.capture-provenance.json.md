# dashboard/src/panels/review/walkStore.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The receipt of the 7 served bodies `walkStore.*.captured.json` of the store-authored comparison that the walked-tree tests (requirement MIK-R39) use. It records when and how the bodies were captured, over which world, and one row per body with the route, the parameters, the status, the time taken, the `sha256` and the size.

## Code Commentary

### The capture

- `captured_at` is 2026-10-04T15:56:14+00:00. The producer is the leaf's worker with `capture_store_bodies.py`, run with `mcp/tests` and `mcp/src` on the Python path.
- `route`: `create_app(config, collaborators=serving_collaborators(config))` over a FastAPI `TestClient`.
- `source_tree`: the `260928-mik-l39` worktree on base `e40d1f21660386f9b091ae5e6fee595a467d4cef`, in which no file under `mcp/` changed.
- `comparison`: a store-authored fixture, `build_world` of `mcp/tests/test_review_change_kinds.py`: a live leaf over four Git trees, every memory side read through its derived index.
- `attempts`: one capture per body; each body is the first answer.
- `not_kept`: the same run also captured `walkStore.INV-AAAAAA.captured.json` and `walkStore.INV-HHHHHH.captured.json`. No test loads them, so the two files are not in the tree and the receipt lists no row for them.

### The rows

All seven rows are of leaf `260101-TRV-L1` of master `260101_tree_review`:

- the subject catalogue (`entries`);
- the shared member's review (`shared`) and the same review asked with `pageSize=2` (`sharedPage`);
- the reviews of the families FAM-F00001 and FAM-F00002;
- the review of the invariant INV-PPPPPP;
- `FAM-F00001Continued`: the review of FAM-F00001 asked with `pageSize=2`, `pageOf=family_members` and the cursor that `sharedPage` published for that family's before side.

Every row's `sha256` and `bytes` match the file it names.

### Boundaries

These are captures over a synthetic store-authored world, not current project knowledge.

## Evidence

- When, by what command, at which source tree and over which world the bodies were captured, and which two captures are not kept. [4]
- One receipt row per body. [5]
- The test file that serves these bodies. [6]
