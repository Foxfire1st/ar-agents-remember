# mcp/src/agents_remember/memory/knowledge_census/inventory.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The mechanical census inventory at a pinned baseline (MIK-R20 rule 1).** `take_inventory(census_id,
code=, memory=, scope=)` resolves the code and memory revisions to exact commits, lists both trees through
Git objects only (no checkout), and returns the census's `CensusBaseline` and `CensusInventory`. It reads
no file content: the inventory is mechanical, and claims are agent work (D11).

## Code Commentary

### Logic

- `resolve_commit` runs `git rev-parse --verify --quiet <rev>^{commit}`; a revision that names no commit
  raises `CensusBaselineError` ("unreadable baseline").
- `_paths_at` lists a commit with the validator's `code_tree_from_git`; a tree Git cannot list is also
  `CensusBaselineError`.
- `onboarding_routes` are the directories under `onboarding/` holding an `overview.md`, with `.` for
  `onboarding/overview.md`. `governing_route` walks up from a location to the nearest route (MIK-R21
  rule 1), falling back to `.`; a path no route governs has no `route`.
- `build_inventory` (the Git-free part, used by the tests): one source row per code path in scope, routed
  by its onboarding location `onboarding/<path>.md`, and one artifact row per memory path under
  `onboarding/` that `is_knowledge_path` accepts (the `*.index.json` cache and hidden directories are
  excluded), routed by its own location. Rows are sorted.
- `in_scope`: an empty scope means every file; otherwise a path equal to or under a scope directory.

### Conventions

- `baseline.scope` is stored sorted, so the output is deterministic for a pair of commits and a scope.
- Symlinks and submodules are excluded, as in the validator's tree reader.

### Invariants And Boundaries

- An inventory taken at an unreadable baseline is refused; nothing is returned and so nothing is written.
- Measured on the real repositories by the worker (read only): 3,560 source rows, 2,574 artifact rows and 86 routes, in about 1.5 s.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

Commit resolution, the route walk and the two builders.

- A revision that names no commit is an unreadable baseline. [1]
- A tree Git cannot list is an unreadable baseline. [2]
- Routes are the directories holding `overview.md`; the nearest governs. [3]
- The mechanical inventory from two path sets. [4]
- Pin the baseline and inventory it. [5]
- Inventory rows carry their governing onboarding route. [6]
- Exact commits are pinned and an unreadable baseline refused. [7]

### Cross-Repo References

The inventory reads two repositories, the code repository and its memory repository, each addressed explicitly by the caller as a path and a revision; it only reads their Git objects.

No cross-repo boundary is crossed by this file.
