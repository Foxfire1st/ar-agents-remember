# mcp/src/agents_remember/worktrees/sync_transaction_git/_ignore_merge.py

## Governing Overview

[Sync transaction Git overview](overview.md)

## Purpose

Resolve a converted memory worktree's generated briefs rule when Git stops on a root ignore-file merge conflict.

## Code Commentary

The resolver checks the converted layout marker, the unmerged regular-file stages and their pinned parent blobs. It proceeds only while the working file still matches Git's `AUTO_MERGE` bytes. It strips the exact generated stanza, gives each nonempty authored stage a terminal newline, and uses Git's three-way merge on the remaining authored text. Add/add uses an empty base. A clean authored merge receives one generated stanza before staging. A genuine authored conflict or an intervening working-file edit retains Git's unresolved state.

## Evidence

- The resolver checks the memory layout, pins both parent blobs and compares the conflict bytes again before staging. [1]
- The authored merge removes the generated stanza, normalizes terminal newlines in nonempty stages and restores the stanza only after a clean merge. [2]
