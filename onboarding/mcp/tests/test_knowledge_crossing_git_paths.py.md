# mcp/tests/test_knowledge_crossing_git_paths.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Compares the Git index after a structural memory-sync park with the index from Git's own three-way merge.

## Code Commentary

The fixture compares the complete mode, object and stage tuples for the selected fixture paths in both worktrees. It checks the unchanged hidden path, the one-sided edit, the delete/edit and mode/edit conflicts, the symlink, the gitlink and the file-to-directory change. It also checks the symlink and gitlink worktree shapes.

## Relationships

Exercises the structural overlay through `start_side_merge` in `worktrees/sync_transaction_git/_merge.py`.

## Evidence

- The structural merge preserves Git's tuple map and reports surviving conflicts for the selected fixture paths. [1]
