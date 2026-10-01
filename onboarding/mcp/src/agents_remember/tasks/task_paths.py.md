# mcp/src/agents_remember/tasks/task_paths.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

The on-disk paths a task root owns, and the predicates over them — as task-domain rules rather than
worktree rules. A series contract, an enclosure directory, a leaf's enclosure contract and the archive
segment are decided by the task root alone, so the single definition belongs in `tasks/`.

The module exists because of a measured layering defect: `tasks/leaf_doc.py` needed
`series_contract_path` and `leaf_enclosure_path` to bind a leaf document's derived master link, and the
only definition of those rules lived in `worktrees/task_resolver.py`. Importing them from there inverts
`layers.toml`'s declared order (`tasks` rank 9 below `worktrees` rank 10, no baseline, no exception) and
produced a `tasks <-> worktrees` package cycle the armed `layering` rail reports. Moving the rules down
here resolves it without a second definition and without touching `layers.toml`.

## Code Commentary

### Logic

Three module-level constants name the layout: `SERIES_CONTRACT_FILENAME` (`"series-contract.md"`, `:20`),
`ARCHIVE_DIR` (`"0_archive"`, `:21`) and `ENCLOSURES_DIR` (`"enclosures"`, `:22`).

`slugify` (`:25-28`) lowercases, strips, collapses every run outside `[a-z0-9._-]` into `-`, trims
leading/trailing `.`, `-` and `_`, and falls back to `"task"` for an input that normalizes to nothing —
which is what makes `leaf_enclosure_dir` (`:37-40`) derive the directory name from the leaf id, and
`task_resolver.task_folder_name` reuse the same rule for task names.

`series_contract_path` (`:31-34`) is `task_root / SERIES_CONTRACT_FILENAME`; `leaf_enclosure_path`
(`:43-46`) is `leaf_enclosure_dir(task_root, leaf_id) / SERIES_CONTRACT_FILENAME`. `is_archived_path`
(`:49-50`) is membership of `ARCHIVE_DIR` among the path's parts, so it holds at any depth.
`is_enclosure_contract` (`:53-58`) requires the exact filename, at least three parts, and an
`enclosures` grandparent. `iter_leaf_enclosure_contracts` (`:61-66`) walks
`enclosures/*/series-contract.md` under a tasks root in sorted order and skips archived paths, which is
the catalogue's source of leaf contracts.

### Conventions

Pure path arithmetic over `pathlib`, no filesystem reads except the two `is_dir`/`rglob` probes the
iterator needs. No imports from `worktrees`, and therefore no cycle: this module is what lets the task
package derive its own paths.

`worktrees/task_resolver.py` imports all ten names and re-exports them under an explicit `__all__`;
`worktrees` remains the published import site for its existing callers, while the definition lives here.
No caller other than `worktrees/task_resolver.py` and `tasks/leaf_doc.py` imports this module directly
today, and `tasks/__init__.py` does not re-export it.

### Invariants And Boundaries

- **Exactly one definition per rule.** Verified structurally with `ast` over all of `mcp/src`: each of
  `SERIES_CONTRACT_FILENAME`, `ARCHIVE_DIR`, `ENCLOSURES_DIR`, `slugify`, `series_contract_path`,
  `leaf_enclosure_dir`, `leaf_enclosure_path`, `is_archived_path`, `is_enclosure_contract` and
  `iter_leaf_enclosure_contracts` has exactly one definition site, and it is in this file.
  `worktrees/task_resolver.py` redefines none of them, so its re-export binds the same objects by
  construction rather than by convention.
- The rules are declared by the task root, not by a worktree: changing one here changes it for every
  caller, so a task-layout change is a change to this module and the re-export surface together.
- `0_archive` is never active task material — `is_archived_path` and
  `iter_leaf_enclosure_contracts` enforce that at the vocabulary level, and the resolver above them
  relies on it.
- This module makes no claim about which callers exist; the import census above is source inspection,
  not a runtime guarantee.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source and its `layers.toml` contract.

No external source is required for this repository-owned path vocabulary.

### Repo-Internal References

- The two constants and the slug rule that decide the enclosure directory name. [1]
- The two path builders the derived-master-link binding calls. [2]
- The predicates and the leaf-contract enumerator the resolution and catalogue paths rely on. [3]
- The re-export surface that keeps every existing caller working while the definition sits here. [4]
- The consumer whose binding need created this module. [5]
- The package order that makes this module the correct home, with no baseline and no exception. [6]
- The armed rail step that measures it. [7]

### Cross-Repo References

No cross-repository boundary is owned by this module; it is pure path arithmetic over one task root.

No sibling repository boundary is needed to explain this file.
