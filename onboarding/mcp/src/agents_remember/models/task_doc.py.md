# mcp/src/agents_remember/models/task_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/task_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
write has no same-root master impact. The **`remove_subtask` outcome** fields — `removedSubtask`
(the dropped row number), `deletedFiles` (the real op: the leaf json+md paths unlinked, or `[]` under
`keep_file`), and `wouldDeleteFiles` (the dry-run preview) — are additive optional defaults declared
so the destructive success VALIDATES against `extra="forbid"` (260703-L18 finding 1, closing friction
F-N): the application entry point emits them, and without the declaration the envelope rejected the payload,
surfacing a tool error after the removal already happened (a caller could retry an already-done op).
Every non-`remove_subtask` operation leaves them `None` (excluded by `exclude_none`). It is the
registered model for the `task_doc` row in `PUBLIC_TOOL_RESPONSE_MODELS`. The
persisted task document itself (`tasks.TaskDocument`) is deliberately not returned.

### Invariants And Boundaries

- STRICT AR-owned shape (`extra="forbid"`); register STRICT, not flexible.
- `lifecycleId` is optional-null so it survives `exclude_none=True` when absent.
- `masterSync` is optional because light docs, master docs, cross-series refs, and unchanged parent rows
  should not grow response data unnecessarily.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry row that maps `task_doc` to this model. | `task_reopen` | mcp/src/agents_remember/models/tool_registry.py:153-153 |
| The strict `ToolResponse` envelope base. | `ToolResponse` | mcp/src/agents_remember/models/base.py:63-66 |
| The persisted task document this response describes (not returns). | `TaskDocument` | mcp/src/agents_remember/tasks/document.py:109-173 |
| The application entry point builds the optional `masterSync` payload for real and dry-run leaf writes. | `task_doc_tool` | mcp/src/agents_remember/application/task_doc_tools.py:122-164 |

## Update History
- 2026-08-03T02:58:43+02:00 — W3-B05 curator: resolved 3 Tier-2 table findings with exact source paths; fixer generated all final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 1 / friction F-N): declared the
  `remove_subtask` outcome fields `removedSubtask` / `deletedFiles` / `wouldDeleteFiles` on
  `TaskDocResponse` so the destructive success validates against `extra="forbid"` — no more false
  tool error after a real removal. Regression test validates the response on both the delete-with-files
  and `keep_file` paths (and the dry-run preview). Verification metadata pinned until closeout stamps
  the L18 commit.
- 2026-07-03T00:30+02:00 — L11 adds `TaskReopenResponse` (task_reopen envelope; WorktreeCommandResponse shape, task-domain home).
- 2026-06-26T20:18+02:00 — Task 21 task-doc master sync: added `TaskDocMasterSync` and optional
  `TaskDocResponse.masterSync` so leaf writes can report same-root master-row changes and dry-run master
  previews. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): added the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields (set only on a `dry_run=true` preview; real-op responses unchanged). Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `task_doc` STRICT response model. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
