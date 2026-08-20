# mcp/src/agents_remember/tasks/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/tasks/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-20T10:45+02:00                     |
| lastVerifiedCommitHash | `b7f2c8e2c7020642780e2c9b997ffb035a782e62` |
| lastVerifiedCommitDate | 2026-08-20T10:42:29+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Public import surface for the JSON-primary task-document package: the schema, the
renderer, and the single/batch store helpers.

## Code Commentary

### Logic

Re-exports `document` (`TaskDocument` + the node models incl. `SubTaskRef`/`Section`/`HeaderNote`,
the `DocKind`/`DocStatus`/`StepStatus` Literals, `TASK_DOCUMENT_SCHEMA`, and the
`step_total`/`step_done`/`current_step` + R1 `series_total`/`series_done` helpers), the
260815-DAG-L11 graph surface (`SprintExecutionNode`/`SprintExecutionEndpoint`/`SprintExecutionEdge`/
`SprintExecutionGraph`, `LeafPlacement`, `resolve_graph_endpoint`, `derived_leaf_placement`,
`leaf_placement_facts`, `numbering_drift_hints`), the 260815-DAG-L14 `SprintSeat`/`SprintSeatState` first-class seat surface, `render`
(`render_markdown`), and
`store` (`read_task_doc`/`write_task_doc`/`write_task_docs`/`json_path_for`/`markdown_path_for`/
`doc_stem`). `__all__` lists the full public set.

### Invariants And Boundaries

- Consumers (the `task_doc` application entry point, the observer S7 reader) import from
  `agents_remember.tasks`; keep the facade re-exporting the full set.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The schema, renderer, and store owned by this package. | "class TaskDocument(_Doc):"; "def render_markdown(doc: TaskDocument, *, graph_titles:"; "def write_task_docs(" | mcp/src/agents_remember/tasks/document.py:679-679; mcp/src/agents_remember/tasks/render.py:39-39; mcp/src/agents_remember/tasks/store.py:41-41 |

## Series-Contract Notes

The package facade exports `TaskEnclosureRef` so task-document callers can construct `enclosures[]` references without importing the model internals directly.


## 260815-DAG-L12 Title Join Exports

The facade additionally exports the shared execution-graph title join (L12-R1/R4): `SprintGraphTitles`, `build_graph_titles` (in-memory join), and `read_graph_titles` (disk-backed join) from `execution_graph_titles.py` — the one source of truth the mermaid renderer and the dashboard projection both consume. `__all__` lists the new set.

## Update History
- 2026-08-20T10:45+02:00 — 260815-DAG-L12: the facade additionally exports `SprintGraphTitles`, `build_graph_titles`, and `read_graph_titles` (the shared execution-graph title join); claim re-read and citation ranges regenerated for the new `render_markdown(doc, *, graph_titles=...)` and multi-line `write_task_docs` signatures. Verified at code commit b7f2c8e2.


- 2026-08-20T04:18+02:00 — 260815-DAG-L14: the facade additionally exports `SprintSeat` and
  `SprintSeatState` (the first-class sprint seat surface). Verified at code commit 2f494982.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: the facade additionally exports the segment-graph
  surface (`SprintExecutionNode`, `SprintExecutionEndpoint`, `LeafPlacement`,
  `resolve_graph_endpoint`, `derived_leaf_placement`, `leaf_placement_facts`,
  `numbering_drift_hints`). Verification remains closeout-owned.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: the task package facade exports execution nature,
  sprint graph/edge models, and the cross-root atomic document batch writer.
- 2026-08-14T06:34+02:00 — L23 final candidate review: task exports expose the canonical document
  and reopen-planning helpers used by lineage/start admission; no second task identity is added.

- 2026-08-04T18:31+02:00 — 260731-EFA-L6 S18-B14 curator: re-derived 2 stale citation ranges (`class TaskDocument` document.py:141, `def render_markdown` render.py:28); scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-08-02T17:00+02:00 — 260731-EFA-L6 curator W1-B03: repaired 1 citation row with exact anchors and current source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: facade now exports `write_task_docs` so the
  controller can persist coupled leaf/master task-document updates through the package surface. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: the task package now exports `TaskEnclosureRef`, the JSON task-doc reference that binds leaf documents to enclosure `series-contract.md` paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03 — Slice 3c reopened (R4): facade now also re-exports `HeaderNote` (the extra-header-line model). Verification metadata pinned until closeout stamps the R4 code commit.
- 2026-06-19T03:17 — Slice 3c reopened (R1): facade now also re-exports `series_total`/`series_done` (the master series-progress helpers). Verification metadata pinned until closeout stamps the R1 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: facade now also re-exports `SubTaskRef` and `Section` (the master series-index + section models). Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1 as the task-document package facade. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
