# mcp/src/agents_remember/application/task_sprint_linkage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_sprint_linkage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T04:10+02:00 |
| lastVerifiedCommitHash | `8071a64497ed88f8f423e853dc9440532fd573af` |
| lastVerifiedCommitDate | 2026-08-20T02:19:58+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Own the sprint↔master linkage contract (260815-DAG-L14): one atomic `attach_master` /
symmetric `detach_master` operation pair and the read-only `linkage_report` drift surface.
`attach_master` supersedes the three-write manual flow (`set_subtask` + `set_field
orchestrates` + `author_execution_graph add_node`) that produced the M16/rc7 drift, and
`task_doc.get` on a sprint carries the same linkage facts as `linkage_report` (L14-R5).
Registered as a reviewed task-document writer in `mcp/registration/tasks.py` and gated as a
task-document-writer authority in `code_quality/single_owner.py`.

## Code Commentary

### Logic

The public surface is `SPRINT_LINKAGE_OPERATIONS = ("attach_master", "detach_master",
"linkage_report")`; `sprint_linkage_operation` dispatches a `SprintLinkageCall` (tool-layer
context) to one of the three operations, and `task_doc_tools._special_task_doc_operation`
routes those operations here while wrapping `SprintLinkageError` in `TaskDocError`.

`attach_master` parses a strict `_AttachMasterPayload` (`extra="forbid"`), resolves the sprint
document through `_sprint_context` (must be a `master` with non-empty `orchestrates`), then runs
the whole refusal ladder before any write: cross-repo/self-attach target checks
(`_resolve_attach_target`), already-attached detection across typed rows, `orchestrates` aliases,
and graph placement (`_require_not_attached`), row-number collisions, execution-nature assertion
(`_assert_execution_nature` — a nature-less master requires `executionNature` plus a
`judgmentId` verified against the sprint's canonical Judgment Register through the shared
`verify_sprint_judgment_ids`; a mismatched existing nature refuses), and the Completed-row
terminal check (`_require_completed_master`). `_attach_candidate` builds the one candidate
document: the typed row (number/name/status/masterRef), the `orchestrates` membership slug, and —
only when the sprint has an `executionGraph` — one unique lump `SprintExecutionNode`; a graph-less
sprint reports `graphNode: "deferred-no-graph-default"` and keeps the L13 atomic-sequential
default. `_validate_candidate` then runs full topology validation on a graphed sprint or the
typed-linkage cross-check (`validate_sprint_linkage`) on a graph-less one, and `_publish` writes
the sprint (± nature-asserted master) through the sprint queue's `publish_sprint_update`
publication lane under `integration_authority_lock`, exactly like graph authoring.

`detach_master` is symmetric: it refuses a cross-repo target, tolerates a deleted master document
(`_resolve_tolerantly`), removes the typed row plus every `orchestrates` alias for the master, and
drops its graph node — refusing while any edge still touches the node (`_require_no_touching_edges`)
and refusing to empty the graph. It never deletes files; seat documents stay on disk as historical
records (L14-R3).

`linkage_report` / `linkage_facts_for_get` compute `collect_linkage_facts` — read-only and never
raising. Facts are exception-guarded (`sprint-scan-failed` fallback) and classify legacy and
inconsistent shapes without hard errors (L14-R7): `orchestrates-entry-unresolved`,
`seat-doc-row` (legacy rows correlated through the seat doc's references via `_correlate_seat_row`),
`row-without-membership`, `membership-without-row`, `slug-only-membership`, and
`uncommanded-master` (a master named in the sprint's decisions but never commanded — the
260812_mcp-rc7-release and 260815_ias-memory-ledger-reconciliation witnesses).

`validate_completed_master_row` is the moved terminal check for a master row newly marked
`Completed`: a typed `masterRef` row completes against the linked master document's own status and
completion blockers, while any other row resolves the terminal leaf doc exactly as before.

### Conventions

- Errors are `SprintLinkageError(AgentsRememberError)` with `task-sprint-linkage-*` statuses and
  are translated to `TaskDocError` at the tool boundary.
- All validation precedes the single `write_task_doc_batch` (rollback-safe); dry-run previews the
  rendered diff + `wouldLose` for every affected pair.
- Judgment provenance is shared with graph authoring: `verify_sprint_judgment_ids` (canonical home
  in `task_execution_topology.py`) is the single verifier.

### Invariants And Boundaries

- Sprint↔master membership is same-repository only; a sprint cannot attach itself, and a master
  that itself orchestrates cannot be commanded.
- A nature-less master requires `executionNature` + `judgmentId`; disagreeing with an existing
  nature refuses (reclassify via `author_execution_graph` instead).
- Attach refuses over existing `orchestrates` membership (detach-first is the conversion path);
  detach refuses on touching edges and on emptying the graph.
- This module never deletes files and never hard-fails on legacy shapes — those are facts, not
  errors (L14-R7 backward tolerance).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The typed row model (`masterRef`) and first-class `SprintSeat` schema this module writes. | `SubTaskRef`; `SprintSeat`; `TaskDocument` | mcp/src/agents_remember/tasks/document.py:537-573; mcp/src/agents_remember/tasks/document.py:602-716 |
| The typed-linkage cross-check and altitude role sets this module relies on. | `validate_sprint_linkage` | mcp/src/agents_remember/tasks/document_refs.py:288-341 |
| The tool-layer registration and operation routing. | `_register_task_document_tools`; `_special_task_doc_operation` | mcp/src/agents_remember/mcp/registration/tasks.py:102-199; mcp/src/agents_remember/application/task_doc_tools.py:377-404 |
| The shared judgment verifier and completion gate. | `verify_sprint_judgment_ids`; `require_commanded_masters_completed` | mcp/src/agents_remember/application/task_execution_topology.py:369-398; mcp/src/agents_remember/application/task_execution_topology.py:655-675 |
| The rollback-safe atomic batch writer and the queue publication lane. | `write_task_doc_batch`; `publish_sprint_update` | mcp/src/agents_remember/tasks/store.py:50-90; mcp/src/agents_remember/controlplane/closeout_queue_store.py:190-258 |
| The single-owner authority gate admitting this module as a task-document writer. | `TASK_DOCUMENT_WRITER_AUTHORITIES` | mcp/src/agents_remember/code_quality/single_owner.py:38-50 |

## 260815-DAG-L14 Linkage Boundary

The module is the one authority for typed sprint↔master linkage: attach and detach are atomic
batches, `linkage_report`/`linkageFacts` are the read-only drift surface, and
`validate_completed_master_row` completes typed rows against the linked master document. The
consistency cross-check (`validate_sprint_linkage` in `tasks/document_refs.py`) hard-fails only
new-shape drift; legacy shapes surface as facts (L14-R5/R7).

## Update History

- 2026-08-20T04:10+02:00 — 260815-DAG-L14: created — one atomic `attach_master`/`detach_master`
  operation pair (typed row + `orchestrates` slug + graph lump node + nature assertion as one
  validated batch), the read-only `linkage_report`/`linkageFacts` drift surface, and the moved
  `validate_completed_master_row` for typed rows. Verified at code commit 8071a644 (L14 HEAD);
  the 23-test suite passed under the Dagger-targeted gate.
