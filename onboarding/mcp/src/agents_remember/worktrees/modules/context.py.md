# mcp/src/agents_remember/worktrees/modules/context.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/context.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

## Series-Contract Notes

The context wrapper forwards `parent_task` and `leaf_id` from `WorktreeArgs` to the resolver before operation modules build or load contracts.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree context resolution now forwards `parent_task` and `leaf_id` from `WorktreeArgs` into the coordination resolver. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-31T12:50+02:00 — `resolve_context()` now takes a typed `WorktreeArgs` (from `agents_remember.worktrees.modules.args`) instead of `argparse.Namespace`, dropping the `import argparse`; corrected Code Commentary "command namespaces" prose to name the dataclass (1.0.0 review remediation).
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
