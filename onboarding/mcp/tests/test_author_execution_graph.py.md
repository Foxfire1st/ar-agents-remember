# mcp/tests/test_author_execution_graph.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_author_execution_graph.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Force the incremental `author_execution_graph` operation (260815-DAG-L11 R5/R6/R8): typed
structural mutation batches over a sprint's executionGraph with judgment provenance,
partition refusals, dry-run preview, and atomic publication — since 260815-DAG-L13 including the
graph-less bootstrap seam (the first `add_node` batch creates the graph, reported as
`bootstrapped: true`). Split from
`test_task_execution_topology.py` under the file-size rail; fixtures and shared helpers are
imported from it.

## Code Commentary

### Logic

`ExecutionGraphAuthoringTests` builds a migrated segmented sprint, then forces: the
non-orchestration refusal; the graph-less bootstrap (first `add_node` batch creates the graph,
final validation requires exact `orchestrates` membership and an explicit nature for every
commanded master, with `set_nature` in the same batch covering a nature-less document); judgment provenance (missing `judgmentId` on a
judgment-bearing mutation, a missing Judgment Register section as a typed refusal naming the
section, unknown register rows, non-strategist/orchestrator authors, malformed registers, and
lump-only batches needing no register); dry-run previews that write nothing followed by apply
publication; batch atomicity leaving every document untouched on failure; unknown/incomplete
partition refusals; segment-on-atomic and uncommanded `set_nature` refusals; `set_nature` master
rewrite; remove-node in-use/ambiguity/unknown-leaf handling; edge endpoint resolution errors
(blank reason, self, duplicate, unknown) plus the remove-edge happy path; `move_leaf` moving,
placing an unplaced leaf, and refusing emptied or unknown-target segments; numbering hints
reported and never refusing; and registration/documentation of the operation.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; unpublished candidate code never writes the
  deployed coordinator.
- The suite asserts behavior through the public `task_doc` application entry point instead of
  duplicating the authoring algorithm.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The authoring forcing suite. | `ExecutionGraphAuthoringTests` | mcp/tests/test_author_execution_graph.py:56-983 |
| The production operation under test. | `author_execution_graph` | mcp/src/agents_remember/application/task_execution_topology.py:182-247 |
| Fixtures and shared helpers are imported from the topology suite. | `_config`; `_master`; `_graph` | mcp/tests/test_task_execution_topology.py:51-99 |

## 260815-DAG-L15 Gate-Repair Judgment Provenance

The gate-repair round updated `test_judgment_provenance_is_enforced`: a judgmentless `add_edge`
now asserts the typed `task-execution-graph-judgment-required` refusal (the F5 behavior —
judgmentId optional at parse, statically-required typed refusal) instead of the old raw pydantic
wrap "invalid execution-graph authoring". The judgment-unknown and judgment-author-refused
assertions are unchanged.

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: judgment-provenance forcing now asserts the typed task-execution-graph-judgment-required refusal for a judgmentless add_edge (F5) instead of the old raw pydantic wrap. Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the unmigrated-sprint refusal became the graph-less
  bootstrap forcing (first `add_node` batch creates the graph with `bootstrapped: true`; final
  validation requires exact membership and explicit natures). Verification remains closeout-owned.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created for the incremental graph-authoring forcing
  suite (split from `test_task_execution_topology.py`). Verification remains closeout-owned.
