# mcp/src/agents_remember/application/task_docs/task_sprint_archive_moves.py

## Governing Overview

[mcp/src/agents_remember/application/task_docs/overview.md](overview.md)

## Purpose

Sprint-archive first phase: record write, ordered moves, and rollback.

## Code Commentary

MIK-R82 rule 1: the sprint's own folder moves first, then every moving commanded master's folder in a deterministic recorded order, all under `tasks/<repository>/0_archive/`. A failure before the moves end attempts to restore every moved folder, including the full recorded prefix on a resumed request. Complete restoration removes the record so a repeated request starts clean; incomplete restoration retains it and reports the unresolved folders. After the moves the archive hook runs per archived folder; a hook failure keeps the archive with per-folder deleted and failed lists, and the same request retries only the remaining cleanup.

## Evidence

- Ordered folder moves attempt rollback of the recorded prefix; complete restoration removes the record, while incomplete restoration reports unresolved folders. Per-folder hook cleanup retries its remainder. [1]
