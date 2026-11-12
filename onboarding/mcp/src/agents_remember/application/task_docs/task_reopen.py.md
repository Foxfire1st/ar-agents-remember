# mcp/src/agents_remember/application/task_docs/task_reopen.py

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Owns `task_reopen_tool`, the confined task-domain application entry point behind the `task_reopen` MCP tool. The current `application/task_docs/task_doc_tools.py` facade re-exports it unchanged, keeping application composition separate from the worktree reset owner.

## Code Commentary

### Logic

`task_reopen_tool(config, *, contract_path, dry_run=False)` confines the contract path inside the
coordination root and delegates the reset to
`worktrees.reopen.reopen_task`: the leaf's enclosure contract review/closeout/integration state
returns to virgin and the leaf's task document returns to planning under the exact same leaf id.
No ambient lifecycle is read or ended. The worktree owner retains the same-leaf reset and successor-workspace authority. The response
keeps the worktree-command shape (contract state fields plus `ok`/`operation`), so it validates
against a `WorktreeCommandResponse` subclass in the tool-response registry.

### Invariants And Boundaries

- A state reset, not a worktree creator: recreating worktrees stays `worktree_start`'s job.
- Contract confinement lives in `kernel.authority.require_within_coordination`; `worktrees/reopen.py` dispatches series to their own owner and applies the leaf preflight/refusal and reset rules. This module owns confined application composition, not a blanket master refusal or a session-lifecycle handoff.

## Evidence

### Repo-Internal References

- The confined application entry delegates reopen without ambient lifecycle access. [1]


- The worktree owner dispatches series separately and performs admitted leaf reset, leaving worktree recreation to start. [2]



- The current task-doc facade re-exports the same application entry. [3]


- The application entry confines the contract and delegates; this is source evidence, not a test execution. [4]
