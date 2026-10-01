# mcp/src/agents_remember/application/task_docs/task_reopen.py

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

## Evidence

### Repo-Internal References

- The reopen application entry point and its ambient-lifecycle handoff. [1]
- The enclosure-contract reset this delegates to. [2]
- The facade re-export keeping the old import path working. [3]
- The application entry point delegates reopen through its current worktree owner; deleted suites provide no current execution evidence. [4]
