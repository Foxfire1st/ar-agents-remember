# mcp/src/agents_remember/kernel/coordination_context/contracts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/contracts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-22T22:00+02:00                     |
| lastVerifiedCommitHash | `6a87054534caec754faae00447f737d71b094cb9` |
| lastVerifiedCommitDate | 2026-06-22T21:58:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`contracts.py` loads optional `c-09-git-worktree-manager` skill worktree contract facts for the `c-08-ar-coordination-context-resolver` skill
coordination context.

## Code Commentary

### Logic

`resolve_contract()` honors an explicit contract path first, then falls back to
task-root candidates for a `contract.md` when a task name is supplied, and finally
to `find_worktree_contract()` when only a `worktree_name` is known. Precedence is
`contract_path` > `task_name` > `worktree_name`: each later branch runs only when
the earlier inputs are absent. Missing or unparsable contracts produce
`(None, candidate_path)` so the resolver can still report the attempted path
without mutating contract state.

`find_worktree_contract()` exists because `worktree_name` cannot be reversed to a
`task_name` (`slugify` keeps both `-` and `_`, so the hyphen/underscore prefix
boundary is lossy) and `contract.md` is stored at
`tasks/<repo>/<task_name>/contract.md`, not inside the worktree directory. It
enumerates `tasks/<repo>/*/contract.md`, loads each contract, and matches the
derived `worktree_group_for(...).name` against the contract's recorded
`coordination.worktree_group` name, skipping unreadable or unparsable contracts
(`ContractError`/`OSError`). The first match wins; no match returns `None`.

### Invariants And Boundaries

- This module reads contract facts only; `c-09-git-worktree-manager` skill owns contract creation and
  mutation.
- Contract parser failures should not fabricate worktree facts.
- An unmatched `worktree_name` returns `None` without raising; the enumeration
  skips contracts it cannot read rather than aborting the search.

## Docs References

No external documentation is needed for this package-local worktree contract adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Worktree contract parsing, task-root candidates, and the `worktree_group_for` folder-name derivation live in the worktrees package. | contract + worktree-group helpers | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| Resolver assembly consumes the optional contract payload. | context assembly | [resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |

## Cross-Repo References

No cross-repository evidence is needed for local contract fact loading.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-22T22:00+02:00: Added a `worktree_name` fallback to `resolve_contract()` plus the `find_worktree_contract()` helper so `resolve_context`/`resolve_coordination_context` resolve a worktree contract from `worktree_name` alone (precedence `contract_path` > `task_name` > `worktree_name`; graceful-empty preserved). Imports `worktree_group_for` for the lossless worktree-group-name join. Fixes #90.
- 2026-05-25T20:57+02:00: Created by extracting worktree contract fact loading from the `c-08-ar-coordination-context-resolver` skill resolver.
