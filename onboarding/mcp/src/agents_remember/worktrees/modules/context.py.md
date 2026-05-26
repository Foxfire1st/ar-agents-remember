# mcp/src/agents_remember/worktrees/modules/context.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/context.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:41+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Resolves coordination context for worktree lifecycle operations.

## Code Commentary

`resolve_context()` adapts command namespaces to the kernel resolver.
`contract_context()` reconstructs context from a persisted worktree contract
and, for external-memory tasks, reparses settings from the memory worktree when
that task branch changed memory settings.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The kernel resolver owns topology, storage, path rules, and cross-repo resolution. | [coordination_context_resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Closeout planning uses this module before refreshing onboarding metadata. | [closeout.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/closeout.py) |

## Update History

- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
