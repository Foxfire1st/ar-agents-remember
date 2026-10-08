# mcp/src/agents_remember/worktrees/reopen_reset.py

## Governing Overview

[mcp/src/agents_remember/worktrees/overview.md](overview.md)

## Purpose

Reset support for a reopened worktree.

## Code Commentary

The owner restores a reopened leaf's candidate state from its recorded base so a reopened attempt starts from a known tree.

## Evidence

- The file realizes its current contract at the corrected candidate. [1]
