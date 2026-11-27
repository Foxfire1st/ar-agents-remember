# docs/reference/mcp-tools.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The reference of the tool server's tools. Each tool has one row, and the sections follow the groups of the tools.

## Code Commentary

The worktree section tells a caller whose client stopped waiting for a sync to look for the `worktree_sync` row in the tool log once the call has ended, and to read the sync's current state with `worktree_status`. The closeout section gives the same direction for a `worktree_closeout_apply` call whose wait ended first: the row and its detail record the outcome.

The knowledge section documents all 11 `knowledge_read` views (`source_context`, `invariant`, `family`, `record`, `records`, `impact`, `search`, `weakness`, `dependent`, `writers`, `consolidation_proposal`), automatic code-tree pairing (`contractPath`/`repo_id`/`memoryRoot`, overridden by `repositoryRoot`/`codeTreeId`), text IDs (`recordId`/`recordIds`), text-bearing `records`/`impact`/`search` responses, and `dependent(compact=true)` closeout triage alongside full moved-link rows, while keeping retrieved claims subordinate to reading source code and running tests.

## Relationships

Both directions link the `Tool log` entry of `docs/concepts.md`, which says how a cancelled request is logged.

## Evidence

- A sync caller who stopped waiting finds the outcome in the tool log and the current state through worktree_status. [1]
- A closeout caller who stopped waiting finds the outcome in the tool log. [2]

- The MCP reference groups tools and their main arguments; the mounted schema supplies the complete argument contract with lossless wire compaction, role-scoped allowlists, and fail-closed bindings. [5]
