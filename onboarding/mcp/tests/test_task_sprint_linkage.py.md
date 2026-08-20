# mcp/tests/test_task_sprint_linkage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_sprint_linkage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Behavioral test suite for the L14 sprint↔master linkage contract
(`application/task_sprint_linkage.py`): the atomic `attach_master`/`detach_master` operations, the
read-only `linkage_report` surface, and `validate_completed_master_row` for typed rows. Since
260815-DAG-L16 the suite's `task_doc` calls pass `call=TaskDocCall(dry_run=...)` instead of the
bare `dry_run` argument (signature-compat with the L16 `TaskDocCall` refactor); suite purpose is
unchanged.

## Code Commentary

### Logic

`SprintLinkageTests` and `SprintLinkageEdgeTests` drive `task_doc_tool` through the real
application boundary over scratch task roots: attach writes the typed `masterRef` row, the
`orchestrates` slug, and (on a graphed sprint) the lump graph node as one validated atomic batch;
detach removes them, refusing while any edge touches the node and never deleting files;
`linkage_report` surfaces seat-doc rows, slug-only membership, row/membership mismatches, and
uncommanded masters as facts. The helpers `_attach`/`_detach`/`_linkage` build the
`TaskDocTarget`/`TaskDocEdit` objects and dispatch through the `task_doc_tool` application entry
point, passing the `TaskDocCall` call object since the L16 signature-compat change.

### Conventions

Same scratch-task-root harness as the task-document and execution-topology suites; assertions
target typed statuses and document state, not message substrings.

### Invariants And Boundaries

- Tests construct only disposable coordination roots; never a real deployed coordinator.
- Suite purpose is L14 linkage forcing; the L16 delta is the call-shape signature only.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The linkage forcing suite. | `SprintLinkageTests`; `SprintLinkageEdgeTests` | mcp/tests/test_task_sprint_linkage.py:101-706; mcp/tests/test_task_sprint_linkage.py:707-1064 |
| The production module under test. | `SprintLinkageRequest`; `_AttachMasterPayload`; `SprintLinkageCall` | mcp/src/agents_remember/application/task_sprint_linkage.py:86-160 |
| The call-shape the suite now passes (L16). | `TaskDocCall` | mcp/src/agents_remember/application/task_doc_route_review.py:36-48 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created (sidecar was missing since the file's L14
  creation) and recorded the L16 signature-compat update (`call=TaskDocCall(dry_run=...)`);
  suite purpose unchanged. Verified at code commit a9d50e08.
