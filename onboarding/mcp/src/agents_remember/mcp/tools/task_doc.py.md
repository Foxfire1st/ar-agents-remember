# mcp/src/agents_remember/mcp/tools/task_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/mcp/tools/task_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tools/overview.md](overview.md)

## Purpose

Transport-thin payload builders for the task-domain tools: `task_doc` authoring and,
since L11, `task_reopen` (reopen a completed leaf task under its exact leaf id).

## Code Commentary

### Logic

`task_doc_payload(config, target: TaskDocTarget, *, operation, edit: TaskDocEdit = NO_EDIT,
dry_run=False)` calls `task_doc_tool(config, target, operation=..., edit=..., dry_run=...)` and
wraps the result through `base._tool_payload("task_doc", ...)`, so the response is validated against
`TaskDocResponse` and (like every tool) attributed to the active lifecycle at the `_tool_payload`
choke point.

Since 260731-EFA-L2 the arguments arrive in two objects that answer two different questions:
`TaskDocTarget(repo_id, task_name, contract_path, slug)` — which document — and
`TaskDocEdit(fields, step, decision, subtask, section)` — what the edit is. `NO_EDIT` is the
shared empty edit a read (`operation='get'`) passes. The `subtask`/`section` slots still carry the
master `set_subtask`/`set_section`/`remove_subtask` edits; `dry_run` still threads the R5 preview
flag (the application entry point renders + diffs the would-be doc and returns it **without** writing).

The published MCP signature is still the flat argument list; `mcp/registration/tasks.py` builds the
two objects, because a model-typed tool parameter would republish `task_doc` as a nested object.

### Invariants And Boundaries

- Stays transport-thin: all behavior (resolution, mutation, render) lives in the
  application entry point and the `tasks/` package.
- Must route through `base._tool_payload`, like every other builder.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point this builder forwards to. | `task_doc_tool` | mcp/src/agents_remember/application/task_doc_tools.py:122-164 |
| The shared validation/emission choke point. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| The response model the payload validates against. | `TaskDocResponse` | mcp/src/agents_remember/models/task_doc.py:33-59 |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 anchored 3 Repo-Internal citation rows with 3 exact identifiers and generated source ranges; verification metadata was preserved.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `task_doc_payload`'s ten keyword arguments became
  `target: TaskDocTarget` plus `edit: TaskDocEdit` (default `NO_EDIT`), with `operation` and
  `dry_run` still separate. `task_reopen_payload` is unchanged. Verification metadata pinned until
  closeout stamps the L2 code commit.
- 2026-07-03T00:30+02:00 — L11 adds `task_reopen_payload` beside the task_doc builder — the payload lives in the task domain.
- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): threads the new `dry_run` flag into `task_doc_tool`. Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: forwards the new `subtask`/`section` payloads for the master `set_subtask`/`set_section` ops. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `task_doc` payload builder. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
