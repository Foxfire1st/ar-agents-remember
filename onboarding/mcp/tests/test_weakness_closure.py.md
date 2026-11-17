# mcp/tests/test_weakness_closure.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Exercises weakness closure authoring through the registered `knowledge_write` tool and closure projections through both registered `knowledge_read` views, using isolated code/memory repositories and real Git histories.

## Code Commentary

### Logic

The fixture creates a writer world and registers the FastMCP tools. `_submit` calls the registered writer with a task-bound handoff; `_read_closures` calls the weakness and record views with `includeClosed`, the selected memory root and code tree. The shared snapshot compares file bytes, HEAD and index bytes in both repositories before and after those reads. `_store` and `_defer` directly construct historical fixture states; they are not public authoring evidence.

The own-task case previews without changing the snapshot, then writes a task/reason closure without guessing a code commit. It preserves the original anchor and seen metadata. Both public views first return the pending closeout note, then return the actual code commit after a paired memory commit, while the stored closure remains unchanged. Explicit and deferred closure forms also parse through the knowledge tree and index and remove the open weakness from maintenance marks/counts.

A newly authored closure for another task without a commit is refused with the observed state unchanged. A real explicit code commit remains exact across later pairs. Separate source cases reject tree, blob, missing, annotated-tag and foreign-repository object values atomically. Later metadata edits, slug/reanchor/revision changes and historical checkout selection preserve the original closing pair. Reopening and reclosing select the new episode; a closure imported from the second parent retains its origin, while independently authored merge closures report unavailable attribution instead of choosing a parent.

A committed closure without a usable trailer pair reports unavailable attribution, distinct from an uncommitted pending closure. The body-only/final-trailer case captures the exact committed message and raw Git command outputs, then compares both public projections: a prose-body mention yields no commit and an unavailable note; a genuine final trailer returns the actual closing commit. Its stored record stays task/reason-only. These are source assertions, not an execution result or a settlement of a live weakness.

### Boundaries

The test worlds are task-local fixtures. The direct historical setup helpers and the registered writer checks establish different kinds of evidence. Explicit stored commits, deferred attribution, pending closeout and unavailable history remain distinct. No live record, branch or closeout authority follows from this card.

## Evidence

### Repo-Internal References

- Registered writer/reader helpers bind the isolated world and compare both repository snapshots around reads. \[1] [1]
- Actual committed-message and Git captures distinguish body-only mentions from a genuine final trailer in both public views. \[2] [2]
- Own-task preview/write and stored explicit/deferred forms preserve observations and remove the closed mark. \[3] [3]
- Other-task authoring requires an explicit actual code commit and rejects the five named invalid object classes without partial writes. \[4] [4]
- Metadata/reanchor/history, recurrent closure and merge cases preserve or distinguish the appropriate closing episode. \[5] [5]
- A committed closure lacking a usable pair reports unavailable rather than pending attribution. \[6] [6]
