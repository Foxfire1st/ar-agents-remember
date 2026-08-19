# mcp/tests/test_closeout_queue_segments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_segments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T08:55+02:00 |
| lastVerifiedCommitHash | `f2e2f4b9c18d89cc0f5c901f43831e014701aae0` |
| lastVerifiedCommitDate | 2026-08-19T11:32:36+02:00|
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
| Segment-graph queue scheduling and fact reporting forcing. | `SegmentGraphQueueTests` | mcp/tests/test_closeout_queue_segments.py:17-110 |
| The leaf-aware queue projection under test. | `closeout_queue_tool` | mcp/src/agents_remember/worktrees/closeout_queue.py:185-251 |
| The leaf-aware graph helpers under test. | `candidate_predecessors`; `ready_sort_key` | mcp/src/agents_remember/worktrees/closeout_queue_graph.py:204-264 |

## Update History

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved `closeout_queue_tool` and the leaf-aware graph helpers within their modules; re-pointed the two citation rows. Verification metadata unchanged.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created as the segment-graph queue forcing suite
  (split from `test_closeout_queue.py`). Verification remains closeout-owned.
