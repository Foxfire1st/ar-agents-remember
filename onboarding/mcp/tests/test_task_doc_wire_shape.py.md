# mcp/tests/test_task_doc_wire_shape.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_doc_wire_shape.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Wire-shape lock for the `task_doc` special operations (260815-DAG master full-gate repair envelope
fix): every special op — `attach_master`, `detach_master`, `linkage_report`,
`author_execution_graph`, and get-on-a-sprint — must satisfy the strict `TaskDocResponse` envelope
(`extra="forbid"`). This is the same bug class as 260703-L18 finding 1 (`remove_subtask`): before
the fix the special ops returned raw operation payloads lacking the standard task-doc identity
(`taskId`/`slug`/`kind`/`status`/`docPath`/`renderedPath`/...) and carrying undeclared extras, so
the envelope rejected them after their writes.

## Code Commentary

### Logic

`TaskDocSpecialOpWireShapeTests` drives the production `task_doc_tool` path for each special op
(real and dry-run) against a temp task tree, then validates the returned payload through
`TaskDocResponse.model_validate` — proving both the declared wire fields (the `_sprint_doc_identity`
merge + the `TaskDocResponse` special-op field declarations) and the absence of undeclared extras.
It reuses the shared fixtures from `test_task_execution_topology` (`MASTER_A`/`MASTER_B`/`MASTER_C`,
`REPOSITORY`, `_config`, `_master`) and `test_task_sprint_linkage._register_section`, plus the
`test_worktree_support` git helpers.

### Invariants And Boundaries

- The suite validates the RESPONSE envelope, not the underlying operation semantics (those live in
  the linkage/topology suites) — it locks the wire shape end to end through `task_doc_tool`.
- A payload failing `TaskDocResponse` validation here is the exact regression the fix prevents:
  a special op whose write succeeded but whose response the strict envelope rejects.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The special-op wire-shape forcing suite. | `TaskDocSpecialOpWireShapeTests` | mcp/tests/test_task_doc_wire_shape.py:38-240 |
| The strict response envelope under test. | `TaskDocResponse` | mcp/src/agents_remember/models/task_doc.py:115-188 |
| The special-op identity merge. | `_sprint_doc_identity`; `_special_task_doc_operation` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:396-418; mcp/src/agents_remember/application/task_docs/task_doc_tools.py:421-477 |

## Cross-Repo References

No cross-repo boundary applies to this forcing suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-21T00:45+02:00 — Created for 260815-DAG master full-gate repair: the special-op
  wire-shape lock proving every `task_doc` special op validates through the strict
  `TaskDocResponse` envelope. Verified at code commit e5cb139f.
