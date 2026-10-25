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

The layout constants name `series-contract.md`, `0_archive`, `enclosures` and `notes`.

`slugify` lowercases, strips, collapses every run outside `[a-z0-9._-]` into `-`, trims
leading/trailing `.`, `-` and `_`, and falls back to `"task"` for an input that normalizes to nothing —
which is what makes `leaf_enclosure_dir` derive the directory name from the leaf id, and
`task_resolver.task_folder_name` reuse the same rule for task names.

`series_contract_path` is `task_root / SERIES_CONTRACT_FILENAME`; `leaf_enclosure_path`
is `leaf_enclosure_dir(task_root, leaf_id) / SERIES_CONTRACT_FILENAME`. `is_archived_path`
is membership of `ARCHIVE_DIR` among the path's parts, so it holds at any depth.
`is_enclosure_contract` requires the exact filename, at least three parts, and an
`enclosures` grandparent.

`iter_leaf_enclosure_contracts` returns enclosure-position candidates in sorted order, and since MIK-R83
rules 1 and 2 it takes them from the canonical places only: `iter_task_folders` yields a repository's live
task folders (the direct children of `tasks/<repository>/`, the archive segment excluded) and
`_enclosure_contracts` reads `enclosures/<leaf>/series-contract.md` in each of them. One walk therefore
answers "which folders are tasks", and no lookup walks the tree itself, so a copy under `notes/`,
`requirements/` or a deeper folder is never met; `canonical_contract_place` states the depth rule for a
contract and `scan_stray_task_files` is the one scan that reads such copies, and only to report them.

The iterator does not parse or certify a yielded contract. Consumers use
`is_foreign_enclosure_contract` to reject a task artifact outside the repository tasks folder
derived from the contract's physical position. Both paths are resolved first, so `..` and symlink
escapes cannot borrow membership from a textual prefix or recorded root. Resolution failure is
foreign. Each consumer owns its warning or skipped-list detail; this predicate itself emits none.

### Conventions

Path arithmetic stays in the task domain. Enumeration uses `is_dir`, `os.walk` and `lexists`;
foreign membership uses resolved filesystem paths. There are no imports from `worktrees`, so the
task package can derive its paths without a package cycle.

`worktrees/task_resolver.py` imports the public path vocabulary and re-exports it under an explicit `__all__`;
`worktrees` remains the published import site for its existing callers, while the definition lives here.
Refresh imports its iterator and foreign-membership guard directly. Other consumers may use the
published resolver import site; their guards do not create a second definition of the path rules.

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

- The layout constants and slug rule decide enclosure directory names. [1]
- The two path builders the derived-master-link binding calls. [2]

- The archive/enclosure-position predicates remain, while the iterator excludes notes and archives before descent. [3]



- The explicit re-export list and imports keep the path rules single-defined in the task domain. [4]

- The consumer whose binding need created this module. [5]
- The package order that makes this module the correct home, with no baseline and no exception. [6]
- The armed rail step that measures it. [7]


- The traversal prunes notes and archive descent but preserves a leaf directory named notes. [8]

- Physical, filesystem-resolved task membership rejects foreign artifacts and resolution failures. [9]

### Cross-Repo References

No external-system boundary is owned by this module; it defines repository task-layout paths,
enclosure traversal and positional filesystem membership.

No sibling repository boundary is needed to explain this file.
