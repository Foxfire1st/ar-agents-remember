# mcp/src/agents_remember/kernel/coordination_context/cross_repo.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/cross_repo.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`cross_repo.py` resolves branch-gated adjacent repository facts for
`crossRepo.allow` settings.

## Code Commentary

### Logic

The module validates each configured allow entry, checks the adjacent code repo
branch and HEAD, optionally checks the matching external memory repo branch,
and reads the memory ledger when memory inclusion is enabled. It returns
included, included-code-only, or excluded state with concrete reasons.

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
| Cross-repo entries are parsed from settings before this module resolves repository state. | settings values | [setting_values.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/setting_values.py) |
| External memory ledger parsing supplies memory compatibility facts. | ledger helper | [memory_ledger.py](agents-remember-md/mcp/src/agents_remember/kernel/memory_ledger.py) |
| Worktree support tests cover branch-gated cross-repo inclusion and legacy-string exclusion. | cross-repo tests | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No separate repository evidence is needed; the module reports adjacent repo facts at runtime.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No static cross-repo references are required. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting branch-gated cross-repo state resolution from the C-08 resolver.
