# mcp/src/agents_remember/application/task_docs/task_sprint_archive_moves.py

## Governing Overview

[mcp/src/agents_remember/application/task_docs/overview.md](overview.md)

## Purpose

Sprint-archive first phase: record write, ordered moves, and rollback.

## Code Commentary

MIK-R82 rule 1: the sprint's own folder moves first, then every moving commanded master's folder in a deterministic recorded order, all under `tasks/<repository>/0_archive/`. A failure before the moves end restores every moved folder and removes the record this request wrote, so a repeated request starts clean. After the moves the archive hook runs per archived folder; a hook failure keeps the archive with per-folder deleted and failed lists, and the same request retries only the remaining cleanup.

## Evidence

- Ordered folder moves with full rollback before completion, then per-folder hook cleanup with retry of the remainder. [1]
