# mcp/src/agents_remember/application/task_docs/task_reopen.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/task_docs/task_reopen.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Owns `task_reopen_tool`, the task-domain application entry point behind the `task_reopen` MCP
tool. Extracted from `application/task_doc_tools.py` in 260815-DAG-L11 so each tool's application
logic stays a focused module (the file-size rail); `task_doc_tools.py` re-exports it unchanged as a
facade, keeping the import surface stable.

## Code Commentary

### Logic

`task_reopen_tool(config, *, contract_path, dry_run=False)` confines the contract path inside the
coordination root, loads the enclosure contract for its lifecycle id, and delegates the reset to
`worktrees.reopen.reopen_task`: the leaf's enclosure contract review/closeout/integration state
returns to virgin and the leaf's task document returns to planning under the exact same leaf id.
After a real (non-dry-run) reopen it ends the completed task's anchored ambient lifecycle so the
next `worktree_start` mints a fresh lifecycle instead of promoting the completed one. The response
keeps the worktree-command shape (contract state fields plus `ok`/`operation`), so it validates
against a `WorktreeCommandResponse` subclass in the tool-response registry.

### Invariants And Boundaries

- A state reset, not a worktree creator: recreating worktrees stays `worktree_start`'s job.
- Contract confinement and reopen refusal rules (masters, in-flight leaves, existing worktrees)
  live in `kernel.authority.require_within_coordination` and `worktrees/reopen.py`; this module
  owns only composition and the ambient-lifecycle handoff.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reopen application entry point and its ambient-lifecycle handoff. | `task_reopen_tool` | mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41 |
| The enclosure-contract reset this delegates to. | `reopen_task` | mcp/src/agents_remember/worktrees/reopen.py:212-289 |
| The facade re-export keeping the old import path working. | `task_reopen_tool` | mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41 |
| The application entry point delegates reopen through its current worktree owner; deleted suites provide no current execution evidence. | `task_reopen_tool` | mcp/src/agents_remember/application/task_docs/task_reopen.py:20-41 |

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/application/task_docs/task_reopen.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 moved the facade re-export within `task_doc_tools.py`; re-pointed the citation to `task_doc_tools.py:83-85`. Verification metadata unchanged.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: created as `task_reopen_tool` moved out of
  `application/task_doc_tools.py` (file-size rail); behavior unchanged, `task_doc_tools.py`
  re-exports the symbol as a facade. Verification remains closeout-owned.