# mcp/src/agents_remember/worktrees/modules/terminal_agents.py

## Governing Overview

[modules overview](overview.md)

## Purpose

The best-effort host-archival boundary for an admitted leaf retirement. It lets the admitted
finalize, cleanup and abandon transactions archive the leaf's recorded agents without letting a host
or receipt failure refuse an already admitted retirement.

## Code Commentary

### Logic

`archive_terminal_agents(contract, *, dry_run)` returns an empty report for a dry run or a non-leaf
contract. It reads the bound `leaf_agent_archive` port from `worktree_services()`; an unbound service
bundle reports `state: not-bound` and a missing port is not an error. Any exception from the port is
caught and reported as `state: failed` with the exception type and message, because host and receipt
failures cannot refuse the admitted retirement — the recurring observer derives the debt from
terminal truth instead.

### Invariants And Boundaries

- A dry run archives nobody.
- A failure returns a report; it never raises into the retirement transaction.
- Only leaf contracts enter the archive boundary.

## Evidence

- The boundary contains host and discovery failures and never refuses retirement. [1]
