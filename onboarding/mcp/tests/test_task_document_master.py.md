# mcp/tests/test_task_document_master.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_task_document_master.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-15T14:05+02:00                                            |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2`                                        |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_task_document_master.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `MasterApplicationTests`
- `TerminalLeafResolutionTests`
- `RegistrationTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_task_document_master.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-15T14:05+02:00 — L3 final targeted-gate repair: partial leaf-artifact removal remains
  idempotent, deleting and reporting only the JSON or Markdown sibling that still exists.
- 2026-08-15T12:53+02:00 — No content impact: corrected one synthetic leaf row's repository id to
  the canonical `agents-remember` fixture scope required by queue-aware topology publication; the
  master application assertion is unchanged.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
