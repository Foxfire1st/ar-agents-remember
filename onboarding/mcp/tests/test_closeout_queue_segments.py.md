# mcp/tests/test_closeout_queue_segments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_segments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force queue scheduling and reporting over leaf-segment sprint graphs (260815-DAG-L11 R3/R6).
Split from `test_closeout_queue.py` under the file-size rail; the queue fixture and refs are
imported from it.

## Code Commentary

### Logic

`SegmentGraphQueueTests` declares leaf candidates on a segmented sprint graph and proves that an
edge into a segment blocks exactly that segment's leafs (completion stays master-granular), and
that an unplaced leaf — a master leaf set that grew after authoring — is reported as a
`leafPlacementFacts` fact with its derived segment placement, never silently scheduled or
auto-written.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; the deployed coordinator is never written.
- The suite asserts behavior through the public `closeout_queue` tool boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Segment-graph queue scheduling and fact reporting forcing. | `SegmentGraphQueueTests` | mcp/tests/test_closeout_queue_segments.py:17-106 |
| The leaf-aware queue projection under test. | `closeout_queue_tool` | mcp/src/agents_remember/worktrees/queue/closeout_queue.py:185-251 |
| The leaf-aware graph helpers under test. | `candidate_predecessors`; `ready_sort_key` | mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:214-227; mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py:247-263 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented test contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved `closeout_queue_tool` and the leaf-aware graph helpers within their modules; re-pointed the two citation rows. Verification metadata unchanged.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created as the segment-graph queue forcing suite
  (split from `test_closeout_queue.py`). Verification remains closeout-owned.
