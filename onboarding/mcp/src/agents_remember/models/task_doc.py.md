# mcp/src/agents_remember/models/task_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/task_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T00:30+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[models/overview.md](overview.md)

## Purpose

The STRICT response model for the `task_doc` tool: it echoes the document's identity,
progress, dry-run preview, and optional master-row sync outcome after an operation.
L11 adds `TaskReopenResponse` here — the task-domain home for the `task_reopen`
envelope; it subclasses `WorktreeCommandResponse` because the payload legitimately
carries the enclosure contract state.

## Code Commentary

### Logic

`TaskDocResponse` extends `ToolResponse` (so it inherits `ok`/`operation`/token
metadata and `extra="forbid"`) and adds `taskId`, `slug`, `kind`, `status`, optional
`lifecycleId`, `docPath`, `renderedPath`, and `stepsDone`/`stepsTotal`. The R5 **dry-run**
fields — `dryRun`, `rendered`, `diff`, `wouldLose` — are additive optional defaults, set only on a
`dry_run=true` preview (a real op leaves them at their defaults, so its response is unchanged).
`TaskDocMasterSync` is the optional nested leaf-to-master result: status, master doc path,
rendered path, subtask number, and preview-only rendered/diff/wouldLose fields. It is omitted when a
write has no same-root master impact. It is the registered model for the `task_doc` row in
`PUBLIC_TOOL_RESPONSE_MODELS`. The
persisted task document itself (`tasks.TaskDocument`) is deliberately not returned.

### Invariants And Boundaries

- STRICT AR-owned shape (`extra="forbid"`); register STRICT, not flexible.
- `lifecycleId` is optional-null so it survives `exclude_none=True` when absent.
- `masterSync` is optional because light docs, master docs, cross-series refs, and unchanged parent rows
  should not grow response data unnecessarily.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The registry row that maps `task_doc` to this model. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| The strict `ToolResponse` envelope base. | [base.py](agents-remember/mcp/src/agents_remember/models/base.py) |
| The persisted task document this response describes (not returns). | [tasks/document.py](agents-remember/mcp/src/agents_remember/tasks/document.py) |
| The controller builds the optional `masterSync` payload for real and dry-run leaf writes. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |

## Update History

- 2026-07-03T00:30+02:00 — L11 adds `TaskReopenResponse` (task_reopen envelope; WorktreeCommandResponse shape, task-domain home).
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: added `TaskDocMasterSync` and optional
  `TaskDocResponse.masterSync` so leaf writes can report same-root master-row changes and dry-run master
  previews. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): added the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields (set only on a `dry_run=true` preview; real-op responses unchanged). Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `task_doc` STRICT response model. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
