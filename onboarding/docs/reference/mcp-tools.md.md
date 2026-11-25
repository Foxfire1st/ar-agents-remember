# docs/reference/mcp-tools.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The reference of the tool server's tools. Each tool has one row, and the sections follow the groups of the tools.

## Code Commentary

The worktree section tells a caller whose client stopped waiting for a sync to look for the `worktree_sync` row in the tool log once the call has ended, and to read the sync's current state with `worktree_status`. The closeout section gives the same direction for a `worktree_closeout_apply` call whose wait ended first: the row and its detail record the outcome.

## Relationships

Both directions link the `Tool log` entry of `docs/concepts.md`, which says how a cancelled request is logged.

## Evidence

- A sync caller who stopped waiting finds the outcome in the tool log and the current state through worktree_status. [1]
- A closeout caller who stopped waiting finds the outcome in the tool log. [2]
