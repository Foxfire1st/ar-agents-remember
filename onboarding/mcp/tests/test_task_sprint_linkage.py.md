# mcp/tests/test_task_sprint_linkage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_sprint_linkage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00 |
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
| The production module under test. | `SprintLinkageRequest`; `_AttachMasterPayload`; `SprintLinkageCall` | mcp/src/agents_remember/application/task_sprint_linkage.py:102-111; mcp/src/agents_remember/application/task_sprint_linkage.py:130-154; mcp/src/agents_remember/application/task_sprint_linkage.py:164-173 |
| The call-shape the suite now passes (L16). | `TaskDocCall` | mcp/src/agents_remember/application/task_doc_route_review.py:36-48 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG-L15 F8 Fact Vocabulary And Serving-Build Preflight

`test_report_does_not_flag_a_sprint_as_uncommanded_master` proves an orchestrates-bearing sprint
doc is excluded from `uncommanded-master`, while a genuinely commanded-but-rowless master still
surfaces as `membership-without-row`. `test_report_seat_row_edge_shapes` moved to the F8 vocabulary:
rows whose seat doc is absent or carries no master reference now report `seat-doc-row-unresolved`
(expected kinds ["seat-doc-row-unresolved", "seat-doc-row", "seat-doc-row-unresolved"]) instead of a
master-less `seat-doc-row`. `test_attach_wraps_a_serving_build_preflight_refusal` proves attach wraps
the `TopologyServingBuildError` as a `TaskDocError` (`serving-build-unsupported`) refusal.

## Update History

- 2026-08-20T21:30+02:00 — 260815-DAG-L15: added test_report_does_not_flag_a_sprint_as_uncommanded_master and test_attach_wraps_a_serving_build_preflight_refusal; updated test_report_seat_row_edge_shapes to the F8 fact vocabulary (seat-doc-row-unresolved). Verified at code commit de3a0fd9.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created (sidecar was missing since the file's L14
  creation) and recorded the L16 signature-compat update (`call=TaskDocCall(dry_run=...)`);
  suite purpose unchanged. Verified at code commit a9d50e08.
