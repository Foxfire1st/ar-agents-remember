# mcp/src/agents_remember/tasks/__init__.py

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
`doc_stem`). Since 260831-CCR (commit `99dc249b`) the facade also re-exports the typed
task-intent slot models `AcceptanceObligationQuestion`, `ApprovedRequirementPacketRef`, and
`TaskIntentIdentity` (line 11-15, also in `__all__` line 84-117) so callers reference the typed
intent forms through the package surface. `__all__` lists the full public set.

### Invariants And Boundaries

- Consumers (the `task_doc` application entry point, the observer S7 reader) import from
  `agents_remember.tasks`; keep the facade re-exporting the full set.
- The typed task-intent forms are re-exported, not re-defined here; their home is
  `models/task_intent`.

## Evidence

### Repo-Internal References

- The schema, renderer, and store owned by this package. [1]
- Current facade re-exports of the typed task-intent slot models. [2]

## Series-Contract Notes

The package facade exports `TaskEnclosureRef` so task-document callers can construct `enclosures[]` references without importing the model internals directly.


## 260815-DAG-L12 Title Join Exports

The facade additionally exports the shared execution-graph title join (L12-R1/R4): `SprintGraphTitles`, `build_graph_titles` (in-memory join), and `read_graph_titles` (disk-backed join) from `execution_graph_titles.py` — the one source of truth the mermaid renderer and the dashboard projection both consume. `__all__` lists the new set.

## 260821-CLIVE Final Task-Package Contract

The facade exports the source-snapshot and transactional-publication primitives that keep canonical
task writes independent from projection refresh. The application layer computes the affected sprint
union and publishes bounded projection effects after the accepted task batch; queue state is never a
task write precondition. The facade also exports the discard/audit/registration types and atomic
write/remove primitive described below.

### Reconciled Source Evidence

- The current module exposes the canonical task models, publication primitives, discard/audit types, and rollback-safe store operations. [3]

## 260821-CLIVE Task Audit And Registration Exports

The task package exports discard source/unstarted proof, discarded-subtask audit, and task-execution
registration models plus `write_task_docs_and_remove`. These are canonical task-plane types and the
rollback-safe parent-write/child-removal primitive; they do not give the queue task-history or
deletion authority.

## CCR-R02@v2 Typed Intent Exports

The facade re-exports `AcceptanceObligationQuestion`, `ApprovedRequirementPacketRef`, and
`TaskIntentIdentity` per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, giving
consumers (route review, serving readers, dashboards) one typed import surface for the normative
intent slots and identity.
