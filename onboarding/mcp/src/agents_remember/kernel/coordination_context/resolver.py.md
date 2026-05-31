# mcp/src/agents_remember/kernel/coordination_context/resolver.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/resolver.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`resolver.py` owns C-08 coordination context detection and assembly.

## Code Commentary

### Logic

The module resolves the code repository, chooses internal or external memory,
parses settings, loads optional worktree contract facts, computes effective
task/docs/system roots, resolves cross-repo settings, and returns one
`CoordinationContext`. The effective memory root is the contract's
`memory_worktree` when present and otherwise the resolved `memory_root`; it is
not influenced by `memory_mode`.

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
| Data models and missing-memory errors are defined separately. | models | [models.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/models.py) |
| Settings parsing, contract loading, and cross-repo resolution are delegated to focused modules. | package overview | [overview.md](overview.md) |
| Resolver parity and worktree support tests cover the output contract and worktree-aware path behavior. | tests | [test_resolver_parity.py](agents-remember-md/mcp/tests/test_resolver_parity.py); [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No cross-repository evidence is needed; cross-repo facts are read dynamically from configured adjacent repos.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Update History

- 2026-05-31T12:50+02:00 — `_effective_memory_root` dropped its unused `memory_mode` parameter and its dead `disabled`-mode branch (both returned `memory_root`); behaviour-preserving, and added a Logic note that the effective memory root is not influenced by `memory_mode` (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting coordination context selection and assembly from the monolithic resolver.
