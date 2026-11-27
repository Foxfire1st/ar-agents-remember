# docs/reference/mcp-tools.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The reference of the tool server's tools. Each tool has one row, and the sections follow the groups of the tools.

## Code Commentary

The worktree section tells a caller whose client stopped waiting for a sync to look for the `worktree_sync` row in the tool log once the call has ended, and to read the sync's current state with `worktree_status`. The closeout section gives the same direction for a `worktree_closeout_apply` call whose wait ended first: the row and its detail record the outcome.

The `role_message` held-delivery section documents that provider-limited holds with a known reset time publish to the durable reset index and wake through an independent 16-worker reset scheduler delivering within roughly 30 seconds for up to roughly 300 due recipients (and at roughly 11 recipients per second beyond that host-bridge ceiling), separate from the 512-entry / 24-hour held-receipt queue.

## Relationships

Both directions link the `Tool log` entry of `docs/concepts.md`, which says how a cancelled request is logged.

## Evidence

- A sync caller who stopped waiting finds the outcome in the tool log and the current state through worktree_status. [1]
- A closeout caller who stopped waiting finds the outcome in the tool log. [2]

- The MCP reference groups tools and their main arguments; the mounted schema supplies the complete argument contract with lossless wire compaction, role-scoped allowlists, and fail-closed bindings. [5]
