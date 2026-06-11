# mcp/src/agents_remember/worktrees/modules/context.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/context.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Resolves coordination context for worktree lifecycle operations.

## Code Commentary

`resolve_context()` adapts the typed `WorktreeArgs` dataclass (from
`agents_remember.worktrees.modules.args`) to the kernel resolver.
`contract_context()` reconstructs context from a persisted worktree contract
and, for external-memory tasks, reparses settings from the memory worktree when
that task branch changed memory settings.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The kernel resolver owns topology, storage, path rules, and cross-repo resolution. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |
| Closeout planning uses this module before refreshing onboarding metadata. | [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |

## Update History

- 2026-05-31T12:50+02:00 — `resolve_context()` now takes a typed `WorktreeArgs` (from `agents_remember.worktrees.modules.args`) instead of `argparse.Namespace`, dropping the `import argparse`; corrected Code Commentary "command namespaces" prose to name the dataclass (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
