# mcp/src/agents_remember/memory/conversion/crossing_port.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/crossing_port.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The adapter and the port it implements.

| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter. | `GitKnowledgeCrossing`; `plan` | mcp/src/agents_remember/memory/conversion/crossing_port.py:24-52 |
| The port, its request and its view. | `KnowledgeCrossingPort`; `CrossingRequest`; `CrossingPlanView` | mcp/src/agents_remember/worktrees/services.py:183-186; mcp/src/agents_remember/worktrees/services.py:170-180; mcp/src/agents_remember/worktrees/services.py:151-163 |
| The default composition binds it. | `build_default_worktree_services` | mcp/src/agents_remember/application/worktree_services.py:208-218 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
