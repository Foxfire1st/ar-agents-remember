# mcp/src/agents_remember/kernel/coordination_context/resolver.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`resolver.py` owns `c-08-ar-coordination-context-resolver` skill coordination context detection and assembly.

## Code Commentary

### Logic

The module resolves the code repository, chooses internal or external memory,
parses settings, loads optional worktree contract facts, computes effective
task/docs/system roots, resolves cross-repo settings, and returns one
`CoordinationContext`. The effective memory root is the contract's
`memory_worktree` when present and otherwise the resolved `memory_root`; it is
not influenced by `memory_mode`.

**The public signature (changed in 260731-EFA-L2):**

```python
resolve_coordination_context(
    code_repository_name=None, workspace_root=None, code_repository_root=None,
    *, hints: CoordinationHints | None = None, selector: EnclosureSelector | None = None,
) -> CoordinationContext
```

The eight former positional/keyword arguments (`requested_topology`, `coordination_root`,
`settings_path`, `onboarding_root`, `contract_path`, `task_name`, `parent_task`, `leaf_id`,
`worktree_name`) now live in the two frozen bundles defined in `models.py`. Both default to
`None` and are replaced by empty instances, so a bare `resolve_coordination_context("repo")` still
works. **`hints.onboarding_root is not None` is still the branch** that selects
`_context_from_onboarding_root` over `_context_from_selection`.

Every private helper was re-signed to match: `_resolve_code_repository` now returns a typed
`CodeRepository` instead of a `dict[str, Path | str]` (so the `Path(repo["root"])` /
`str(repo["name"])` casts at each read are gone); `_context_from_onboarding_root(repo, hints,
onboarding_root, selector)` and `_context_from_selection(repo, hints, selector)` take the bundles;
and `build_coordination_context(repo, *, roots: CoordinationRoots, storage, cross_repo,
selector=None)` takes the resolved roots as one object. `workspace_root` is no longer a separate
parameter of `build_coordination_context` — `repo.workspace` is always the workspace passed to
`resolve_cross_repo_settings`, where the old code fell back to `code_repository_root.parent`;
`_resolve_code_repository` already applies exactly that fallback when constructing the
`CodeRepository`, so the behaviour is preserved.

Contract resolution is unchanged in behaviour: `build_coordination_context` hands the whole
`EnclosureSelector` to `resolve_contract`, which tries the explicit `contract_path`, then
`find_task_contract` (task-based, leaf-enclosure-aware via `parent_task`/`leaf_id`), then
`find_worktree_contract` as a fallback that resolves a contract from `worktree_name` alone
(matched by worktree-group folder name) when no task name is known. Task-based resolution takes
precedence; the `worktree_name` fallback is only consulted when it yields nothing.

### Invariants And Boundaries

- The resolver is facts-only and performs no memory initialization, onboarding
  writes, worktree mutation, or Git branch movement.
- Explicit onboarding roots and contract paths are accepted as overrides only
  for context resolution.
- Callers pass `hints=` / `selector=` keyword-only. Adding a new resolution input means adding a
  defaulted field to `CoordinationHints` or `EnclosureSelector`, not a new resolver parameter.
- Missing memory roots raise `MissingMemoryError` instead of silently creating a
  context.

## Evidence

### Docs References

No external documentation is needed for this package-local resolver flow.

No relevant external documentation is needed.

### Repo-Internal References

- Data models and missing-memory errors are defined separately. [1]
- Settings parsing, contract loading (task-based + worktree-name fallback), and cross-repo resolution are delegated to focused modules. [2]
- Context construction owns resolved task/worktree/memory roots and ledger selection. [3]

### Cross-Repo References

No cross-repository evidence is needed; cross-repo facts are read dynamically from configured adjacent repos.

No static cross-repo references are required.

## Series-Contract Notes

Resolver assembly threads `selector.parent_task` and `selector.leaf_id` into contract and task-root selection, so user-facing calls can keep using task names while the source API resolves nested active roots. Independently, `selector.worktree_name` resolves a contract by its worktree-group folder when no task name is available; the two mechanisms coexist (task-based resolution wins, worktree-name is the fallback). All five live on one `EnclosureSelector`.

## 260731-EFA-L9 Change

The resolver now consumes a "ContractReaderPort" (cit:(["class ContractReaderPort"], mcp/src/agents_remember/kernel/coordination_context/models.py:118-118))
so it never imports `worktrees` directly; the production binding is
`worktrees/modules/contract_reader.py::WorktreeContractReader`, and reader failures degrade to a
reported missing/unreadable contract instead of a crash.
