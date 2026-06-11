# mcp/tests/test_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_missing_onboarding.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:51+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`test_missing_onboarding.py` verifies the pre-code-commit missing-onboarding
check for current worktree additions.

## Code Commentary

### Logic

The tests build temporary Git repositories and memory onboarding roots, then
exercise the checker against untracked additions, staged additions with existing
sidecars, path-rule-excluded additions, renamed targets, and a linked worktree
whose directory name differs from the real repository name. The checks prove
that the script reports only local new worktree responsibility rather than
historical repository gaps.

### Invariants And Boundaries

- Untracked and staged added files are considered new worktree sources.
- A staged added file with a sidecar is clean.
- Excluded files are ignored by path rules.
- Rename targets require onboarding at the target path.
- CLI resolution must use Git repository identity, not a task-specific linked
  worktree basename.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The tested checker lives in `check_missing_onboarding.py`. | [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py) |
| Storage settings and path rules are resolved by the kernel resolver helpers. | [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py) |

## Update History

- 2026-05-24T18:51+02:00: Added coverage for renamed linked worktrees resolving external memory by Git common-directory repository identity.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new test file has an onboarding pair before closeout.
