# mcp/src/agents_remember/worktrees/task_document_copies.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Publishes rendered, read-only leaf documents with an index inside the enclosure group, outside its Git trees.

## Code Commentary

`prepare_task_document_copies` writes the leaf's rendered Markdown under `task-documents/` preserving its canonical relative path plus an `INDEX.json` carrying the canonical reference, JSON and copy digests and publication time — before the launch's first turn. `_publish_copy_writes` applies all files atomically with full rollback to prior bytes. `refresh_task_document_copies` rewrites only the published leaf in its existing enclosures. Every destination must stay inside the working folder as real files; a root whose resolved path falls inside either the code or the memory Git worktree is refused by the destination guard (task_document_copies.py:98-101), and edits to copies are never read back.

## Evidence

- A leaf role's own rendered document is prepared as a real enclosure file with one index entry. [1]
- Public writes rendering the own leaf refresh copies atomically. [2]
- Copy writes publish through the real destination guard. [3]
