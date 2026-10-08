# mcp/src/agents_remember/application/legacy_dataset_copies.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

The content probe and the one cleanup run for leftover copies of the retired knowledge database.

## Code Commentary

MIK-R26 rule 6: a copy is any SQLite file holding the knowledge tables, identified by content rather than name; the cleanup deletes the copies in provider-runtime directories, dead worktrees and archived-task notes, protects tracked and symbolic-link companions, and binds its apply to the reviewed dry-run digest.

## Evidence

No separate reference list: the file's sidecar carries the realization entries this leaf re-anchored.
