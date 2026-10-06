# dashboard/src/panels/review/walkReal.capture-provenance.json

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The receipt of the 16 real served bodies `walkReal.*.captured.json` that the walked-tree tests (requirement MIK-R39) serve to the mounted reviewer. It records when and how the bodies were captured, over which scratch copy, and one row per body with the route, the parameters, the status, the time taken, the `sha256` and the size.

## Code Commentary

### The capture

- `captured_at` is 2026-10-04T15:58:35+00:00. The producer is the leaf's worker with `capture_real_bodies.py`; the command starts `serve_scratch.py` with the leaf's `mcp/src` on the Python path and then runs the capture script.
- `route`: the application's routes registered by `serve_scratch.py` with `serving_collaborators(config)`, over HTTP on `127.0.0.1:18852`.
- `source_tree`: the `260928-mik-l39` worktree on base `e40d1f21660386f9b091ae5e6fee595a467d4cef`, in which no file under `mcp/` changed.
- `scratch`: `--shared` clones of the real code repository at `e40d1f21` and of the real memory repository at `40ae8395` (converted), with the leaf 260928-MIK-L33 from lane D2's `setup_leaf.py`: four scratch code edits and five scratch-authored curator edits in the leaf's own worktrees, then its curate step (12 entries re-recorded at the candidate blob).
- `attempts`: one capture per body; each body is the first answer.

### The rows

- 14 rows of the first round: the subject catalogue (`entries`); the reviews of the families FAM-R6R095RW and FAM-2HBJREC2; the task-context review (`task`); the unexplained-changes lane (`lane`), the classification of `familyWalkMerge.ts` (`file`) and its source content (`source`); and the reviews of the seven changed members of FAM-R6R095RW: INV-2E8MG43K, INV-ZS9ZS878, INV-555EHWM8, INV-BR5MTSTY, INV-H8EM1VJR, INV-VPX81HXV and INV-2TQGXFAX.
- 2 rows of the partial round, described by the `partial_round` note (2026-10-04T19:56:00+00:00): the same scratch leaf and route asked with the server's own `pageSize=2`, so a real family is partial. `INV-2TQGXFAX-page2` is the shared member's first page, and `FAM-R6R095RW-continued` continues the cursor that page published for FAM-R6R095RW's before side.
- Every row's `sha256` and `bytes` match the file it names.

### Boundaries

These are captures over a scratch copy, not current project knowledge.

## Evidence

- When, by what command, at which source tree and over which scratch leaf the bodies were captured. [1]
- One receipt row per body. [2]
- The note of the partial round. [3]
- The kit that serves these bodies. [4]
