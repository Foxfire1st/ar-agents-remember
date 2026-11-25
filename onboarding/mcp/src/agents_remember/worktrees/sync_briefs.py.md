# mcp/src/agents_remember/worktrees/sync_briefs.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Refreshes source briefs after a durable memory-content sync.

## Code Commentary

The settled sync record supplies the persistent memory checkout and the matching code result commit. The helper skips an unchanged head, temporary or unconverted memory, and changes limited to the derived ledger. The shared writer refreshes the resulting tree, with any brief advisory returned to the sync caller.

## Evidence

- The refresh requires changed committed memory content and uses the code result recorded by the same sync. [1]
