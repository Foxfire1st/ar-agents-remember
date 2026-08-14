# mcp/tests/test_task_document_application_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `aeca9a2839c965218a61a3040e15cb84367ebeca`                                        |
| lastVerifiedCommitDate | 2026-08-14T13:35:55+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_application_1.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `ApplicationTests1`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_task_document_application_1.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

This application split proves task edits and manager preflight stay canonically document-addressed.
Lineage and review authority are derived from the task hierarchy; runtime and commit identifiers are
not accepted from the caller.

## Update History
- 2026-08-14T06:40+02:00 — L23 final candidate review: application tests preserve strict
  task-addressed mutation and manager-lineage preflight without accepting runtime identifiers.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
