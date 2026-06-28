# mcp/src/agents_remember/mcp/tools/task_doc.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/mcp/tools/task_doc.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-19T07:23                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tools/overview.md](overview.md)

## Purpose

Transport-thin payload builder for the `task_doc` authoring tool.

## Code Commentary

### Logic

`task_doc_payload(config, *, repo_id, operation, task_name, contract_path, slug,
fields, step, decision, subtask, section)` forwards its arguments to
`controllers.task_doc_tools.task_doc_tool` and wraps the result through
`base._tool_payload("task_doc", ...)`, so the response is validated against
`TaskDocResponse` and (like every tool) attributed to the active lifecycle at the
`_tool_payload` choke point. The `subtask`/`section` payloads carry the master
`set_subtask`/`set_section` edits; `dry_run` threads the R5 preview flag (the controller
renders + diffs the would-be doc and returns it **without** writing).

### Invariants And Boundaries

- Stays transport-thin: all behavior (resolution, mutation, render) lives in the
  controller and the `tasks/` package.
- Must route through `base._tool_payload`, like every other builder.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The controller this builder forwards to. | [task_doc_tools.py](agents-remember/mcp/src/agents_remember/controllers/task_doc_tools.py) |
| The shared validation/emission choke point. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The response model the payload validates against. | [models/task_doc.py](agents-remember/mcp/src/agents_remember/models/task_doc.py) |

## Update History

- 2026-06-19T07:23 — Slice 3c reopened (R5, dry-run/preview): threads the new `dry_run` flag into `task_doc_tool`. Verification metadata pinned until closeout stamps the R5 code commit.
- 2026-06-14T00:16 — Slice 3c commit 3: forwards the new `subtask`/`section` payloads for the master `set_subtask`/`set_section` ops. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T22:34 — Created for slice 3c commit 1: the `task_doc` payload builder. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
