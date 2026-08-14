# mcp/tests/test_task_document_application_2.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_2.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-14T09:08+02:00                                            |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca`                                        |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_application_2.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `ApplicationTests2`, including the master-altitude closeout regression that proves a series
  contract with no leaf id bypasses leaf-only route-review resolution.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_task_document_application_2.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

This application split covers completed-leaf reopen planning before removed descendant refs,
candidate-bound route-review evidence, and fail-closed code/external-memory lineage at task
admission. The tests preserve one task-domain path rather than a worktree fallback.

## R39 Non-Leaf Review Boundary

A new application regression proves series/master closeout returns
not-required-master-altitude without probing candidate change or terminal leaf task-document
identity. Leaf candidate-bound review behavior remains unchanged.

## Update History

- 2026-08-14T11:27+02:00 — R39 curator: recorded the explicit master route-review bypass.
  Verification remains closeout-owned.
- 2026-08-14T09:08+02:00 — Reopened L23 repair: added the dirty master-series regression proving
  route-review admission returns the explicit master-altitude exemption before leaf resolution.
  Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: application forcing covers completed-leaf
  task-reopen planning before removed descendant refs, route-review evidence, and fail-closed
  transitive lineage. Verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
