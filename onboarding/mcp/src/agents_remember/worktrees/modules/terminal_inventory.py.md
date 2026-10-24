# mcp/src/agents_remember/worktrees/modules/terminal_inventory.py

## Governing Overview

[mcp/src/agents_remember/worktrees/modules/overview.md](overview.md)

## Purpose

No-remains terminal inventory for worktree cleanup and abandon.

## Code Commentary

MIK-R82 rule 5: a leaf enclosure with no locator, no worktree folder, no work branches and no recorded outside scratch root still on disk finishes through `worktree_abandon` (never integrated) or `worktree_cleanup` (integrated) with nothing to archive and nothing to delete. This module owns that probe and its already-absent inventory as one authoritative implementation shared by both routes. The terminal reason is persisted in the surviving contract, not only returned, with a readback that proves the write.

## Evidence

- One shared no-remains probe finishes locator-less, folder-less, branch-less enclosures with a persisted reason. [1]

## 260928-MIK-L198 — No remains now means no root on disk either

`terminal_without_remains_reason` now requires `_outside_scratch_absent(contract)` in its conjunction, beside the missing locator, the absent worktree folder and the absent work branches. `_outside_scratch_absent` answers true when `outside_scratch.recorded_root(contract)` is `None`, which is a pre-MIK-R207 enclosure, and otherwise checks that the recorded root no longer exists on disk. The recorded reason sentence is unchanged, and a contract whose root is still there simply gets `None` back and keeps the normal terminal path.
