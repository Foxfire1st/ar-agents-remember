# mcp/src/agents_remember/models/task_document.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/models/task_document.py`               |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                     |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[models overview](overview.md)

## Purpose

`models/task_document.py` (260731-EFA-L9) is the task-document wire vocabulary shared with the
response models: `StepStatus`/`DocStatus` and the terminal-readiness blocker moved here from the
`tasks` package so response models can import them without reaching up (layering cleanup).

## Code Commentary

### Logic

`CompletionBlocker` (cit:(["class CompletionBlocker"], mcp/src/agents_remember/models/task_document.py:23-23)) models the terminal-readiness blocker a task
document carries; the module exports the status literals the wire layer re-exports.

### Invariants And Boundaries

- Models owns the vocabulary; `tasks` must not import `models` for these names (layering rail
  enforced).

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Response and task modules import the vocabulary from this module. | "from agents_remember.models.task_document import CompletionBlocker" | mcp/src/agents_remember/models/lifecycle_finalize.py:10-10; mcp/src/agents_remember/tasks/document.py:23-23 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the task-document wire vocabulary
  moved into models. Verification metadata pinned until closeout stamps the L9 code commit.
