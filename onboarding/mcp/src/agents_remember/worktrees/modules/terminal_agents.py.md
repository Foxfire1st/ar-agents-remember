# mcp/src/agents_remember/worktrees/modules/terminal_agents.py

## Governing Overview

[modules overview](overview.md)

## Purpose

The seat-archival and blocker boundary for an admitted terminal worktree retirement (leaf or series). It invokes the bound archive service on both dry-run and apply, captures unbound, host, and receipt failures as structured reports, and translates unresolved or failed seat outcomes into terminal blockers that prevent folder removal.

## Code Commentary

### Logic

`archive_terminal_agents(contract, *, dry_run, check_census=None)` reads `worktree_services().leaf_agent_archive` for both leaf and series contracts and forwards `dry_run` (and optional `check_census`) to `port.archive(...)`. When no port is bound, it returns `state: "not-bound"` with a reason if `receipt_holder(contract.task_root)` exists, or `{}` when no launch receipt directory exists. `(OSError, ValueError, RuntimeError)` from the port is caught as `state: "failed"` with the exception type and message. `terminal_agent_blockers(archive)` turns `not-bound`, `failed`, and every row in `owed` or `leftAlone` into named terminal blockers.

### Invariants And Boundaries

- A dry run invokes the port with `dry_run=True` to inspect recorded seats and unowned stores without mutating host or receipt state.
- Expected port failures (`OSError`, `ValueError`, `RuntimeError`) and missing bindings (when receipts exist) return structured reports that `terminal_agent_blockers` converts into terminal blockers.
- Both leaf and modern series contracts enter the archive boundary (only legacy series skip it in `terminal_group.py`).

## Evidence


- The boundary captures expected port and binding failures into structured reports and converts `not-bound`, `failed`, `owed`, and `leftAlone` outcomes into terminal blockers. [1]
