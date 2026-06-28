# mcp/src/agents_remember/kernel/coordination_context/resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T18:55+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

`build_coordination_context` threads `parent_task`, `leaf_id`, **and**
`worktree_name` into `resolve_contract`: contract resolution tries the explicit
`contract_path`, then `find_task_contract` (task-based, leaf-enclosure-aware via
`parent_task`/`leaf_id`), then `find_worktree_contract` as a fallback that
resolves a contract from `worktree_name` alone (matched by worktree-group folder
name) when no task name is known. Task-based resolution takes precedence; the
`worktree_name` fallback is only consulted when it yields nothing.

### Invariants And Boundaries

- The resolver is facts-only and performs no memory initialization, onboarding
  writes, worktree mutation, or Git branch movement.
- Explicit onboarding roots and contract paths are accepted as overrides only
  for context resolution.
- Missing memory roots raise `MissingMemoryError` instead of silently creating a
  context.

## Docs References

No external documentation is needed for this package-local resolver flow.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Data models and missing-memory errors are defined separately. | models | [models.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/models.py) |
| Settings parsing, contract loading (task-based + worktree-name fallback), and cross-repo resolution are delegated to focused modules. | package overview | [overview.md](overview.md) |
| Resolver parity and worktree support tests cover the output contract and worktree-aware path behavior. | tests | [test_resolver_parity.py](agents-remember/mcp/tests/test_resolver_parity.py); [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repository evidence is needed; cross-repo facts are read dynamically from configured adjacent repos.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Series-Contract Notes

Resolver assembly threads `parent_task` and `leaf_id` into contract and task-root selection, so user-facing calls can keep using task names while the source API resolves nested active roots. Independently, `worktree_name` resolves a contract by its worktree-group folder when no task name is available; the two mechanisms coexist (task-based resolution wins, worktree-name is the fallback).

## Update History

- 2026-06-28T18:55+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): `build_coordination_context` now also threads `worktree_name`, and `resolve_contract` gained a `find_worktree_contract` fallback (MCP 2.9.3) that resolves a contract from a worktree-group name when no task name is known. Reconciled with the series' `parent_task`/`leaf_id` task-based resolution — both coexist, task-based first.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: context resolution now plumbs `parent_task` and `leaf_id`, derives task roots with the active-task resolver, and can resolve leaf enclosure contracts without requiring users to pass filesystem paths. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — `_effective_memory_root` dropped its unused `memory_mode` parameter and its dead `disabled`-mode branch (both returned `memory_root`); behaviour-preserving, and added a Logic note that the effective memory root is not influenced by `memory_mode` (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting coordination context selection and assembly from the monolithic resolver.
