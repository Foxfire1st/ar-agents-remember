# mcp/src/agents_remember/worktrees/task_resolver.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/worktrees/task_resolver.py`     |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-07T20:50+02:00                                  |
| lastVerifiedCommitHash |                                                         `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`|
| lastVerifiedCommitDate |                                                         2026-06-28T18:49:06+02:00|
| governingOverview      | `../../../overview.md`                                  |

## Governing Overview

[mcp/ overview](../../../overview.md)

## Purpose

`task_resolver.py` centralizes task-name and leaf-enclosure path resolution for the series-contract
workflow. It gives controllers, context resolution, worktree start/load paths, observer snapshots, and
finalization one shared way to find active root tasks, nested task roots, raw leaf
`enclosures/<leaf-id>/` contracts, and completed root-task archive targets. Canonical leaf-ref validation
and normalization live in `worktrees/leaf_refs.py`.

## Code Commentary

### Logic

The module owns the filesystem vocabulary for the new task layout: `series-contract.md`, `0_archive`,
and `enclosures/`. `slugify()` normalizes user-facing `task_name` / `leaf_id` values into stable folder
names; `task_root_candidates()` keeps legacy `-ar` task folders discoverable while the active schema moves
to task-name folders.

`iter_active_series_contracts()` walks a repository's task tree for root-level `series-contract.md` files
and deliberately excludes archived paths and leaf enclosure contracts. `resolve_active_task_root()` uses
that iterator to resolve by `task_name`, optionally constrained by `parent_task` for nested task folders. It
raises `TaskResolutionError` when multiple active task roots share the same name and falls back to the
current/legacy deterministic path only when no active contract exists and fallback is enabled.

`resolve_leaf_enclosure_contract()` resolves the parent task root first, then either returns the requested
raw leaf contract path or auto-selects the only leaf contract. Alias-aware legacy lookup belongs to
`leaf_refs.resolve_leaf_enclosure_contract_for_ref()` so this module stays focused on root and contract path
mechanics. Multiple leaves without an explicit `leaf_id` raise `TaskResolutionError`, forcing callers to
disambiguate without asking users for filesystem paths.

`archive_completed_root_task()` moves only completed root task folders into `tasks/<repo>/0_archive/`. It
skips nested leaf/task roots, skips roots that still have their own active `series-contract.md`, blocks if
the archive target already exists, and supports dry-run payloads for finalize previews.

### Conventions

Callers pass human-facing `task_name` and optional `parent_task` / `leaf_id`; this module is the boundary
that turns those names into concrete paths. Archived task folders are excluded from active resolution.

### Invariants And Boundaries

- `0_archive` is never searched as active task material.
- Leaf contracts live under `enclosures/<leaf-id>/series-contract.md`; root series contracts live directly
  under their task root.
- Canonical leaf-ref validation, candidate reporting, and legacy alias policy live in `worktrees/leaf_refs.py`.
- User-facing resolution should prefer `task_name` plus optional `parent_task` / `leaf_id`, not raw paths.
- Archiving is root-task-only; leaf cleanup/finalization must not move a parent task folder.

## Docs References

No external documentation is needed for this local task-folder resolver.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for the local task resolver. | n/a | n/a |

## Repo-Internal References

Same-repository source and tests define the supported task-folder and series-contract behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The resolver defines series-contract filenames, archive/enclosure directory names, slug helpers, current/legacy task-root candidates, and leaf enclosure paths. | L9-L68 | [task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| Active series discovery excludes archived task folders and leaf enclosure contracts; active task resolution can be constrained by `parent_task` and errors on ambiguous task names. | L71-L114 | [task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| Leaf enclosure resolution selects an explicit leaf, auto-selects a single leaf, or errors when several leaves exist; completed root tasks archive under `0_archive` with dry-run support and safety blockers. | L117-L184 | [task_resolver.py](agents-remember/mcp/src/agents_remember/worktrees/task_resolver.py) |
| `leaf_refs.py` owns qualified/doc-id/legacy-stem leaf-ref validation and alias-aware legacy enclosure lookup. | n/a | [leaf_refs.py](agents-remember/mcp/src/agents_remember/worktrees/leaf_refs.py) |
| `start.py` uses the resolver to load a leaf contract from `task_name` / `leaf_id` and to build starts under the resolved parent task root. | L38-L43; L71-L86 | [modules/start.py](agents-remember/mcp/src/agents_remember/worktrees/modules/start.py) |
| `finalize.py` calls `archive_completed_root_task` after cleanup so completed root tasks move to `0_archive` while leaf finalization skips that move. | L14-L15; L60-L74 | [modules/finalize.py](agents-remember/mcp/src/agents_remember/worktrees/modules/finalize.py) |
| Resolver parity tests pin parent-task disambiguation and archive exclusion from active task discovery. | L155-L251 | [test_resolver_parity.py](agents-remember/mcp/tests/test_resolver_parity.py) |
| Worktree support tests pin leaf-start contract placement and branch relationships through `series_contract_path` / `leaf_enclosure_path`. | L60-L64; L493-L528 | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repo boundary is required to explain this local resolver.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No sibling repository boundary is needed to explain this file. | n/a | n/a |

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. The two parity
  tests the row names now read at `test_resolver_parity.py` L155-L251 —
  `test_parent_task_disambiguates_nested_task_roots` (L155-L210) and
  `test_active_series_discovery_excludes_archive` (L212-L251, which asserts
  `iter_active_series_contracts` skips the archived folder and that `resolve_active_task_root` raises
  `TaskResolutionError`). Was L146-L234.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: kept this module focused on active task root, raw leaf
  enclosure path, and root-task archive resolution after the qualified leaf-ref resolver moved to
  `worktrees/leaf_refs.py`. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-06-24T06:26+02:00 — Created for the series-contract task resolver: documents active task-name
  resolution, nested parent disambiguation, leaf enclosure contract lookup, archive exclusion, and completed
  root-task archival. Verification metadata will be stamped during closeout after the new source file is
  committed.
