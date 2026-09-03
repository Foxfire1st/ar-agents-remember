# mcp/tests/test_task_document_application_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_application_2.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `ApplicationTests2`, including the master-altitude closeout regression that proves a series
  contract with no leaf id bypasses leaf-only route-review resolution.

Since 260831-CCR (commit `99dc249b`) the route-review forcing calls now pass the exact resolved
leaf document: the helper `_review_candidate(contract, document)` (line 46-51) builds a
`ResolvedTaskDocument` from `document_ref(contract, json_path_for(contract.task_root, document))`,
and the `build_route_review` and `_record_route_review` seams receive it (e.g. lines 400-413,
457-490). The JSON-primary success regression was renamed
`test_json_primary_success_records_current_route_review` (line 1069-1106): it writes real verdict
and route-evidence files, drops the hand-authored candidate tree and reviewedAt, and asserts the
recorded review carries a current `TaskIntentIdentity` (`schema_ == "task-intent/v1"`).

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_task_document_application_2.py`.
- Route-review forcing passes the exact resolved leaf document so the stamped review binds the
  canonical task-intent identity; legacy hand-authored review rows are no longer valid fixtures.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
| The resolved-candidate helper used by review forcing. | `_review_candidate` | mcp/tests/test_task_document_application_2.py:46-51 |
| The JSON-primary success regression binding current task intent. | `test_json_primary_success_records_current_route_review` | mcp/tests/test_task_document_application_2.py:1069-1106 |

## L23 Final Candidate Disposition

This application split covers completed-leaf reopen planning before removed descendant refs,
candidate-bound route-review evidence, and fail-closed code/external-memory lineage at task
admission. The tests preserve one task-domain path rather than a worktree fallback.

## R39 Non-Leaf Review Boundary

A new application regression proves series/master closeout returns
not-required-master-altitude without probing candidate change or terminal leaf task-document
identity. Leaf candidate-bound review behavior remains unchanged.

## 260815-DAG Master Full-Gate Repair

Imports and mock targets re-point to the `application/task_docs/` package
(`task_doc_route_review`, `task_doc_tools`). `ApplicationTests2` gained two helper-branch
regressions: `test_route_review_contract_initializes_a_fresh_coordination_tree` (git-init path
on a fresh coordination tree) and `test_organizational_leaf_contract_reuses_an_existing_super_branch`
(a second helper call on the same coord reuses the existing `super` source branch).

## CCR-R02@v2 Intent-Bound Route Review Forcing

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, a recorded route review binds
the current canonical task intent of the exact leaf document; the forcing suite now passes the
resolved candidate and asserts the resulting `TaskIntentIdentity`. Part of the landed L25
candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  route-review forcing now passes the exact `ResolvedTaskDocument` and the JSON-primary success
  regression asserts a current `TaskIntentIdentity` on the recorded review (`_review_candidate`,
  `test_json_primary_success_records_current_route_review`). Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: re-pointed task_doc imports and
  mock targets to the application/task_docs package and added the fresh-coordination-tree
  git-init and existing-super-branch helper regressions. Verified at code commit e5cb139f.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-16T04:06+02:00 — 260815-DAG-L4 Dagger repair: lifecycle-id and route-review application tests now use real configured Git worktrees plus an organizational master and sprint-super topology, allowing the public task-document boundary to exercise exact contract authority instead of impossible placeholder repositories.
- 2026-08-16T02:51+02:00 — No content impact: the route-review helper now reuses the real Git
  repository already created by the shared configured-authority fixture instead of initializing it
  a second time; master-altitude route-review behavior is unchanged.

- 2026-08-14T11:27+02:00 — R39 curator: recorded the explicit master route-review bypass.
  Verification remains closeout-owned.
- 2026-08-14T09:08+02:00 — Reopened L23 repair: added the dirty master-series regression proving
  route-review admission returns the explicit master-altitude exemption before leaf resolution.
  Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: application forcing covers completed-leaf
  task-reopen planning before removed descendant refs, route-review evidence, and fail-closed
  transitive lineage. Verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
