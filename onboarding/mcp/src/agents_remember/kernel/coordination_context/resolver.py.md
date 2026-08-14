# mcp/src/agents_remember/kernel/coordination_context/resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external documentation is needed for this package-local resolver flow.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Data models and missing-memory errors are defined separately. | `CoordinationHints` | mcp/src/agents_remember/kernel/coordination_context/models.py:93-106 |
| Settings parsing, contract loading (task-based + worktree-name fallback), and cross-repo resolution are delegated to focused modules. | `# mcp/src/agents_remember/kernel/coordination_context/ — Coordination Context Modules` | onboarding/mcp/src/agents_remember/kernel/coordination_context/overview.md:1-131 |
| Resolver parity and worktree support tests cover the output contract and worktree-aware path behavior. | `test_parent_task_disambiguates_nested_task_roots`, `test_resolver_prefers_task_name_over_worktree_name` | mcp/tests/test_resolver_parity.py:155-210; mcp/tests/test_worktree_support_tests_1.py:485-512 |

## Cross-Repo References

No cross-repository evidence is needed; cross-repo facts are read dynamically from configured adjacent repos.

| Finding | Anchor | Source |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Series-Contract Notes

Resolver assembly threads `selector.parent_task` and `selector.leaf_id` into contract and task-root selection, so user-facing calls can keep using task names while the source API resolves nested active roots. Independently, `selector.worktree_name` resolves a contract by its worktree-group folder when no task name is available; the two mechanisms coexist (task-based resolution wins, worktree-name is the fallback). All five live on one `EnclosureSelector`.

## 260731-EFA-L9 Change

The resolver now consumes a "ContractReaderPort" (cit:(["class ContractReaderPort"], mcp/src/agents_remember/kernel/coordination_context/models.py:108-108))
so it never imports `worktrees` directly; the production binding is
`worktrees/modules/contract_reader.py::WorktreeContractReader`, and reader failures degrade to a
reported missing/unreadable contract instead of a crash.

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: recorded the contract-reader port seam and
  degradation behavior; the L9 change section above documents it. Verification metadata pinned
  until closeout stamps the L9 code commit.
- 2026-08-02T21:03:24+02:00 — 260731-EFA-L6 curator W2-B10: repaired 7 citation findings (3 reference rows); scoped recheck clean.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  **public API change.** `resolve_coordination_context` now takes keyword-only
  `hints: CoordinationHints` + `selector: EnclosureSelector` in place of nine individual
  arguments; `build_coordination_context` takes `(repo: CodeRepository, *, roots:
  CoordinationRoots, storage, cross_repo, selector=None)`; `_resolve_code_repository` returns a
  typed `CodeRepository` rather than an untyped dict; `_context_from_onboarding_root` /
  `_context_from_selection` take the bundles. `build_coordination_context` lost its separate
  `workspace_root` parameter — `repo.workspace` already carries the same value including the
  `code_repository_root.parent` fallback. Resolution order, the onboarding-root branch, contract
  lookup precedence and the returned `CoordinationContext` are all unchanged. Verification
  metadata pinned until closeout stamps the L2 commit.
- 2026-06-28T18:55+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): `build_coordination_context` now also threads `worktree_name`, and `resolve_contract` gained a `find_worktree_contract` fallback (MCP 2.9.3) that resolves a contract from a worktree-group name when no task name is known. Reconciled with the series' `parent_task`/`leaf_id` task-based resolution — both coexist, task-based first.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: context resolution now plumbs `parent_task` and `leaf_id`, derives task roots with the active-task resolver, and can resolve leaf enclosure contracts without requiring users to pass filesystem paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — `_effective_memory_root` dropped its unused `memory_mode` parameter and its dead `disabled`-mode branch (both returned `memory_root`); behaviour-preserving, and added a Logic note that the effective memory root is not influenced by `memory_mode` (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting coordination context selection and assembly from the monolithic resolver.
