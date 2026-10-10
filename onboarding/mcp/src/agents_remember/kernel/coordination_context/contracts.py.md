# mcp/src/agents_remember/kernel/coordination_context/contracts.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Finds and loads the worktree contract of a resolution request. The kernel sits below the `worktrees`
package, so every contract operation goes through the injected `ContractReaderPort`; this module only
decides which candidate path to try and what to return when it cannot be loaded.

## Code Commentary

`resolve_contract(selector, coordination_root, code_repository_name, reader)` returns `(contract, path)`.

1. An explicit `selector.contract_path` is resolved with `observed_resolve` and is the candidate.
2. Without one, `selector.task_name` asks `reader.find_task_contract`, with `parent_task` and `leaf_id`
   passed on.
3. Without a candidate so far, `selector.worktree_name` asks `reader.find_worktree_contract`.
4. No candidate gives `(None, None)`. A candidate that does not exist (`observed_exists`) gives
   `(None, candidate)`. A candidate whose load raises any exception gives `(None, candidate)` too, so the
   caller can report the path it tried. Otherwise the loaded contract is returned with its path.

The two path operations go through the kernel's read recorder. Inside a recording block the resolution of an
explicit contract path is recorded as a `resolve:` row keyed by the absolute, unresolved path, and a missing
candidate is recorded as `absent`. A symbolic link that is retargeted between two resolutions of one computation therefore
shows as a conflict, and a kept result is not reused after the link moved. Outside a recording block the
function records nothing and behaves as `Path.resolve()` and `Path.exists()` do. The contract's bytes are
recorded by the loader behind the port.

The module creates and changes no contract.

### Logic

`resolve_contract(selector, coordination_root, code_repository_name)` — since 260731-EFA-L2 the
five naming arguments arrive as one frozen `EnclosureSelector` (from `models.py`) rather than as
`contract_path, task_name, parent_task, leaf_id, worktree_name`. It resolves a worktree contract in
priority order: an explicit `selector.contract_path` first, then a task-based lookup via
`find_task_contract` when `selector.task_name` is supplied (leaf-enclosure-aware through
`selector.parent_task` / `selector.leaf_id`), then a `find_worktree_contract` fallback keyed on
`selector.worktree_name` alone. Missing or unparsable contracts produce `(None, candidate_path)` so
the resolver can still report the attempted path without mutating contract state.

`find_task_contract` selects the root `series-contract.md` or a specific leaf
enclosure contract through `worktrees.task_resolver.resolve_active_task_root` and
`worktrees.leaf_refs.resolve_leaf_enclosure_contract_for_ref`, with `parent_task` used for
disambiguation. `find_worktree_contract` exists because a `worktree_name` cannot
be reversed to a `task_name` (`slugify` keeps both `-` and `_`, so the prefix
boundary is lossy); it derives the worktree-group folder name via
`worktree_group_for` and matches it against each contract's recorded
`coordination.worktree_group`, scanning `tasks/<repo>` **recursively** for the
canonical `series-contract.md` (the enclosure layout nests contracts under
master + leaf folders, so main's original flat `*/contract.md` glob no longer
suffices). Archived (`0_archive/`) contracts are skipped during the scan
(`is_archived_path`), so a retired task cannot shadow an active one that shares a
worktree-group name.

### Invariants And Boundaries

- This module reads contract facts only; `c-09-git-worktree-manager` skill owns contract creation and
  mutation.
- Contract parser failures should not fabricate worktree facts.

## Evidence

- The candidate order, the recorded resolution and existence probe, and the three empty answers. [4]
- The recorded resolution keeps the absolute, unresolved path as its key. [5]
- A contract link retargeted during a computation is recorded as a conflict and the result is not kept. [6]

### Docs References

No external documentation is needed for this package-local worktree contract adapter.

No relevant external documentation is needed.

- Worktree contract parsing and task-root candidate logic live in the worktrees package. [7]
- Alias-aware leaf enclosure lookup for explicit leaf ids lives in the dedicated leaf-ref resolver. [8]
- Resolver assembly consumes the optional contract payload. [9]

### Cross-Repo References

No cross-repository evidence is needed for local contract fact loading.

No meaningful cross-repo references found.

## Series-Contract Notes

Contract lookup delegates task-name selection to `worktrees.task_resolver` and explicit leaf-id selection to `worktrees.leaf_refs`, first resolving active task roots outside `0_archive/` and then choosing a root series contract or alias-aware leaf enclosure contract as requested. Independently, the `worktree_name` fallback resolves a contract by its derived worktree-group folder when no task name is available; the two paths coexist (task-based selection wins, worktree-name is the fallback), and both honor the canonical `series-contract.md` filename and skip `0_archive/`.
