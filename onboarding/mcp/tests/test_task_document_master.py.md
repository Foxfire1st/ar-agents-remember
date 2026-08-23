# mcp/tests/test_task_document_master.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_master.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_master.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `MasterApplicationTests`, including the master-altitude lifecycle-id regression that calls the
  real document builder with a series contract and proves leaf lifecycle identity is not inherited,
  and the sprint-get regression proving `task_doc.get` on a sprint carries declared `linkageFacts`
  in the identity payload.
- `TerminalLeafResolutionTests`
- `RegistrationTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_task_document_master.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved the task-doc imports under
`application/task_docs/` (`task_doc_tools`, `task_doc_tools_module`) and added
`test_get_on_a_sprint_carries_declared_linkage_facts` to `MasterApplicationTests`: the new
regression proves `task_doc.get` on a sprint appends `linkageFacts` to the identity payload and
that the `extra=forbid` `TaskDocResponse` envelope declares it (a `ValidationError` before the
repair).

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints the public tool response registry to its moved `models.tools` package. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: task-doc imports moved under
  `application/task_docs/`; `MasterApplicationTests` gained the sprint-get regression proving
  `task_doc.get` on a sprint carries declared `linkageFacts` in the identity payload. Verified at
  code commit e5cb139f.
- 2026-08-20T09:35+02:00 — 260815-DAG-L16: signature-compat update (task_doc_tool takes
  `call: TaskDocCall`); suite purpose unchanged. Verified at code commit a9d50e08.


- 2026-08-16T04:24+02:00 — No content impact: removed the now-unused `write_contract` import after the lifecycle-id fixture moved to the real document builder; assertions and production route are unchanged.
- 2026-08-16T04:06+02:00 — Dagger fixture repair: lifecycle-id altitude is tested through the document builder with a master contract, avoiding an impossible persisted leaf topology while preserving the non-leaf assertion.
- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: partial leaf-artifact removal remains
  idempotent, deleting and reporting only the JSON or Markdown sibling that still exists.
- 2026-08-15T12:53+02:00 — No content impact: corrected one synthetic leaf row's repository id to
  the canonical `agents-remember` fixture scope required by queue-aware topology publication; the
  master application assertion is unchanged.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
