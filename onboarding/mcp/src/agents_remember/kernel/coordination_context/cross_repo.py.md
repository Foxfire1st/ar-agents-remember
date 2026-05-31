# mcp/src/agents_remember/kernel/coordination_context/cross_repo.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/cross_repo.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`cross_repo.py` resolves branch-gated adjacent repository facts for
`crossRepo.allow` settings.

## Code Commentary

### Logic

The module validates each configured allow entry, checks the adjacent code repo
branch (`git_branch`) and HEAD (`git_head_or_empty`), optionally checks the
matching external memory repo branch, and reads the memory ledger when memory
inclusion is enabled. It returns included, included-code-only, or excluded state
with concrete reasons. `run_git` is no longer defined here; it is imported from
`agents_remember.kernel.git_command` and re-exported via `__all__` alongside the
two git helpers and the two resolvers.

### Invariants And Boundaries

- Cross-repo inclusion is read-only toward adjacent repositories.
- `includeCode=false` is excluded because there is no code repo branch to
  validate.
- Memory inclusion degrades to code-only when the memory repo or ledger cannot
  satisfy the configured branch and ledger checks.

## Docs References

No external documentation is needed for the local cross-repo resolver.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared `run_git` helper is imported from the kernel git command module rather than defined locally. | run_git import | [git_command.py](agents-remember-md/mcp/src/agents_remember/kernel/git_command.py) |
| Cross-repo entries are parsed from settings before this module resolves repository state. | settings values | [setting_values.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/setting_values.py) |
| External memory ledger parsing supplies memory compatibility facts. | ledger helper | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Worktree support tests cover branch-gated cross-repo inclusion and legacy-string exclusion. | cross-repo tests | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No separate repository evidence is needed; the module reports adjacent repo facts at runtime.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Update History

- 2026-05-31T12:50+02:00 — `run_git` is now imported from `agents_remember.kernel.git_command` (local definition removed) and re-exported via a new `__all__`; `git_head` renamed to `git_head_or_empty` (now docstringed) with its `code_repository_info` call site updated; corrected Logic prose to name `git_branch`/`git_head_or_empty` and the shared `run_git`, and added the git_command repo-internal reference (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting branch-gated cross-repo state resolution from the C-08 resolver.
