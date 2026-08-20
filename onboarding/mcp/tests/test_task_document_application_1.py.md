# mcp/tests/test_task_document_application_1.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_application_1.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-20T09:35+02:00 |
| lastVerifiedCommitHash | `a9d50e08b830c4a34c14e495706c19fe697f47ab` |
| lastVerifiedCommitDate | 2026-08-20T09:26:15+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_application_1.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `ApplicationTests1`
- The legacy master mutation regression now proves that adding `orchestrates` to a plain master
  refuses only on inexact declared facts — an undeclared super branch or a commanded alias that
  resolves to no master — because a graph-less sprint is the legal atomic-sequential default
  (260815-DAG-L13), and that sprint-only `integrationBranch` cannot be placed on the unchanged
  legacy master.

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

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the legacy-master orchestration regression became
  `test_set_field_orchestration_fields_require_exact_commanded_masters` — a graph-less sprint is
  the legal atomic-sequential default, so refusal now requires inexact declared facts (undeclared
  super branch or unresolvable commanded alias); the sprint-only `integrationBranch` refusal is
  unchanged. Verification remains closeout-owned.
- 2026-08-15T03:33:21+02:00 — 260815-DAG-L1 second targeted-Dagger repair: the exact artifact
  showed the adjacent legacy `integrationBranch` success expectation also contradicted the closed
  sprint schema. The regression now proves both partial orchestration edits refuse and leave the
  master unchanged.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: replaced the obsolete
  implicit-orchestration success expectation with the explicit topology-migration refusal required
  by the new contract, while retaining the adjacent integration-branch assertions.
- 2026-08-14T06:40+02:00 — L23 final candidate review: application tests preserve strict
  task-addressed mutation and manager-lineage preflight without accepting runtime identifiers.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
