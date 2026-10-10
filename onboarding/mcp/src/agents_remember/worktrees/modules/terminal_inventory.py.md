# mcp/src/agents_remember/worktrees/modules/terminal_inventory.py

## Governing Overview

[mcp/src/agents_remember/worktrees/modules/overview.md](overview.md)

## Purpose

No-remains terminal inventory for worktree cleanup and abandon.

## Code Commentary

MIK-R82 rule 5: a leaf enclosure with no locator, no worktree folder and no work branches finishes through `worktree_abandon` (never integrated) or `worktree_cleanup` (integrated) with nothing to archive and nothing to delete. This module owns that probe and its already-absent inventory as one authoritative implementation shared by both routes. The terminal reason is persisted in the surviving contract, not only returned, with a readback that proves the write.

## Evidence

- One shared no-remains probe finishes locator-less, folder-less, branch-less enclosures with a persisted reason. [1]
