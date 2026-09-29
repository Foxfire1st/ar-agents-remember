# mcp/src/agents_remember/memory/knowledge_census/inventory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_census/inventory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

Commit resolution, the route walk and the two builders.

| Finding | Anchor | Source |
| --- | --- | --- |
| A revision that names no commit is an unreadable baseline. | `resolve_commit` | mcp/src/agents_remember/memory/knowledge_census/inventory.py:56-69 |
| A tree Git cannot list is an unreadable baseline. | `_paths_at` | mcp/src/agents_remember/memory/knowledge_census/inventory.py:72-78 |
| Routes are the directories holding `overview.md`; the nearest governs. | `onboarding_routes`; `governing_route` | mcp/src/agents_remember/memory/knowledge_census/inventory.py:81-93; mcp/src/agents_remember/memory/knowledge_census/inventory.py:96-107 |
| The mechanical inventory from two path sets. | `build_inventory` | mcp/src/agents_remember/memory/knowledge_census/inventory.py:116-144 |
| Pin the baseline and inventory it. | `take_inventory` | mcp/src/agents_remember/memory/knowledge_census/inventory.py:155-180 |
| Inventory rows carry their governing onboarding route. | `test_inventory_rows_carry_their_governing_onboarding_route` | mcp/tests/test_knowledge_census_files.py:164-192 |
| Exact commits are pinned and an unreadable baseline refused. | `test_take_inventory_pins_exact_commits_and_refuses_an_unreadable_baseline` | mcp/tests/test_knowledge_census_files.py:210-229 |

## Cross-Repo References

The inventory reads two repositories, the code repository and its memory repository, each addressed explicitly by the caller as a path and a revision; it only reads their Git objects.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
