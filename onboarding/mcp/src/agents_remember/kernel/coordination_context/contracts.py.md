# mcp/src/agents_remember/kernel/coordination_context/contracts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/contracts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`contracts.py` loads optional `c-09-git-worktree-manager` skill worktree contract facts for the `c-08-ar-coordination-context-resolver` skill
coordination context.

## Code Commentary

### Logic

`resolve_contract()` honors an explicit contract path first, otherwise searches
task-root candidates for a `contract.md` when a task name is supplied. Missing
or unparsable contracts produce `(None, candidate_path)` so the resolver can
still report the attempted path without mutating contract state.

### Invariants And Boundaries

- This module reads contract facts only; `c-09-git-worktree-manager` skill owns contract creation and
  mutation.
- Contract parser failures should not fabricate worktree facts.

## Docs References

No external documentation is needed for this package-local worktree contract adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Worktree contract parsing and task-root candidate logic live in the worktrees package. | contract helper | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Resolver assembly consumes the optional contract payload. | context assembly | [resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |

## Cross-Repo References

No cross-repository evidence is needed for local contract fact loading.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting worktree contract fact loading from the `c-08-ar-coordination-context-resolver` skill resolver.
