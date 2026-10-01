# mcp/src/agents_remember/worktrees/task_resolver.py

## Governing Overview

[mcp/ overview](../../../overview.md)

## Purpose

`task_resolver.py` centralizes task-name and leaf-enclosure path resolution for the series-contract
workflow. It gives application entry points, context resolution, worktree start/load paths, observer snapshots, and
finalization one shared way to find active root tasks, nested task roots, raw leaf
`enclosures/<leaf-id>/` contracts, and completed root-task archive targets. Canonical leaf-ref validation
and normalization live in `worktrees/leaf_refs.py`.

Since 260913-LCA-L5 it is also the **published import site** for the task-layout path vocabulary, not its
owner: the rules themselves (`SERIES_CONTRACT_FILENAME`, `ARCHIVE_DIR`, `ENCLOSURES_DIR`, `slugify`,
`series_contract_path`, `leaf_enclosure_dir`, `leaf_enclosure_path`, `is_archived_path`,
`is_enclosure_contract`, `iter_leaf_enclosure_contracts`) are defined in
`agents_remember.tasks.task_paths` and re-exported here under an explicit `__all__` (`:29-49`), so no
existing caller changes and there is still exactly one definition of each rule.

## Code Commentary

### Logic

The module **re-exports** the filesystem vocabulary for the task layout rather than defining it
(`:16-27`, `__all__` at `:29-49`): `series-contract.md`, `0_archive`, `enclosures/`, `slugify()`, the two
path builders and the two predicates now live in `tasks/task_paths.py`. What this module still defines is
task-*name* resolution: `task_folder_name()` / `legacy_task_folder_name()` and `task_root_candidates()`
keep legacy `-ar` task folders discoverable while the active schema moves to task-name folders.

`iter_active_series_contracts()` (`:79-85`) walks a repository's task tree for root-level
`series-contract.md` files and deliberately excludes archived paths and leaf enclosure contracts.
`resolve_active_task_root()` (`:88-114`) uses that iterator to resolve by `task_name`, optionally
constrained by `parent_task` for nested task folders. It raises `TaskResolutionError` (`:52-53`) when
multiple active task roots share the same name and falls back to the current/legacy deterministic path
only when no active contract exists and fallback is enabled.

`resolve_leaf_enclosure_contract()` (`:117-144`) resolves the parent task root first, then either returns
the requested raw leaf contract path or auto-selects the only leaf contract. Alias-aware legacy lookup
belongs to `leaf_refs.resolve_leaf_enclosure_contract_for_ref()` so this module stays focused on root and
contract path mechanics. Multiple leaves without an explicit `leaf_id` raise `TaskResolutionError`,
forcing callers to disambiguate without asking users for filesystem paths.

`archive_completed_root_task()` (`:147-184`) moves only completed root task folders into
`tasks/<repo>/0_archive/`. It skips nested leaf/task roots, skips roots that still have their own active
`series-contract.md`, blocks if the archive target already exists, and supports dry-run payloads for
finalize previews.

### Conventions

Callers pass human-facing `task_name` and optional `parent_task` / `leaf_id`; this module is the boundary
that turns those names into concrete paths. Archived task folders are excluded from active resolution.
The re-export list is explicit `__all__` rather than implicit star-import, so the published surface is
reviewable and a name cannot silently disappear from it.

### Invariants And Boundaries

- `0_archive` is never searched as active task material.
- Leaf contracts live under `enclosures/<leaf-id>/series-contract.md`; root series contracts live directly
  under their task root.
- **The path vocabulary is defined in `tasks/task_paths.py`, not here.** This module imports and
  re-exports it and redefines none of it: verified with `ast`, each of the ten moved names has exactly
  one definition site in all of `mcp/src` and it is in `tasks/task_paths.py`. The move exists to keep
  `layers.toml`'s `tasks`(9) < `worktrees`(10) order intact while the task package derives its own paths;
  changing a path rule is a change to `task_paths.py`, with this file following.
- Canonical leaf-ref validation, candidate reporting, and legacy alias policy live in `worktrees/leaf_refs.py`.
- User-facing resolution should prefer `task_name` plus optional `parent_task` / `leaf_id`, not raw paths.
- Archiving is root-task-only; leaf cleanup/finalization must not move a parent task folder.

## Evidence

### Docs References

No external documentation is needed for this local task-folder resolver.

No relevant external documentation is needed for the local task resolver.

### Repo-Internal References

Same-repository source and tests define the supported task-folder and series-contract behavior.

- The re-export surface: this module publishes the task-layout vocabulary without defining it. [1]
- The single definition of every path rule, which this module imports and redefines none of. [2]
- Task-name resolution, which this module still owns: current and legacy folder names plus the candidate list. [3]
- The error a resolution failure raises, and the current/legacy root builders. [4]
- Active series discovery excludes archived task folders and leaf enclosure contracts; active task resolution can be constrained by `parent_task` and errors on ambiguous task names. [5]
- Leaf enclosure resolution selects an explicit leaf, auto-selects a single leaf, or errors when several leaves exist. [6]
- `leaf_refs.py` owns qualified/doc-id/legacy-stem leaf-ref validation and alias-aware legacy enclosure lookup. [7]
- `start.py` uses the resolver to load a leaf contract from `task_name` / `leaf_id` and to build starts under the resolved parent task root. [8]
- `finalize.py` calls `archive_completed_root_task` after cleanup so completed root tasks move to `0_archive` while leaf finalization skips that move. [9]
- Worktree support tests pin leaf-start contract placement and branch relationships through `series_contract_path` / `leaf_enclosure_path`. [10]
- The package order that makes `tasks` the correct home for the vocabulary this module re-exports. [11]

### Cross-Repo References

No cross-repo boundary is required to explain this local resolver.

No sibling repository boundary is needed to explain this file.
