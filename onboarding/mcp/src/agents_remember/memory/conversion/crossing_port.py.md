# mcp/src/agents_remember/memory/conversion/crossing_port.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The crossing sync's composition-bound adapter (MIK-R24 rule 8).** `GitKnowledgeCrossing` implements the
worktree layer's `KnowledgeCrossingPort`. `application/worktree_services.build_default_worktree_services`
binds it, so `worktrees/` reaches the conversion without importing `memory.conversion`.

## Code Commentary

### Logic

- `plan(request)` reads the three memory commits into a temporary scratch (`inputs.memory_from_git`,
  labelled `base`, `own` and `incoming`). It runs `crossing_sync.cross` with the code repository's
  `CodeObjects`, the own paired commit and the `HistoryOwner`, and returns a `CrossingPlanView` (files,
  `(path, item, reason)` conflicts, conflict versions, report).
- A `CrossingError` becomes `CrossingStepFailed` with the same step-naming message. An `OSError` or
  `ValueError` becomes `crossing sync step 'convert' failed: …`.

### Conventions

- The adapter holds no state; each plan starts from Git objects.

### Invariants And Boundaries

- Nothing is written by the time a step fails: the plan is computed before the managed sync lets Git
  touch the worktree.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The adapter and the port it implements.

- The adapter. [1]
- The port, its request and its view. [2]
- The default composition binds it. [3]

### Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

No cross-repo boundary is crossed by this file.
