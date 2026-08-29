# mcp/tests/test_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_missing_onboarding.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-29T11:00+02:00                     |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_missing_onboarding.py` verifies the pre-code-commit missing-onboarding
check for current worktree additions.

## Code Commentary

### Logic

The tests build temporary Git repositories and memory onboarding roots, then
exercise the checker against untracked additions, staged additions with existing
sidecars, staged additions removed before the final candidate, path-rule-excluded additions,
renamed targets, and a linked worktree
whose directory name differs from the real repository name. The checks prove
that the script reports only local new worktree responsibility rather than
historical repository gaps.

### Invariants And Boundaries

- Untracked and staged added files are considered new worktree sources.
- A staged added file with a sidecar is clean.
- A staged add deleted before the effective candidate is built does not require a stale-path sidecar.
- Excluded files are ignored by path rules.
- Rename targets require onboarding at the target path.
- CLI resolution must use Git repository identity, not a task-specific linked
  worktree basename.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tested checker lives in `check_missing_onboarding.py`. | `check_missing_onboarding`, `worktree_added_sources` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:46-73; mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:76-85 |
| Storage settings and path rules are resolved by the kernel resolver helpers. | `detect_coordination_selection`, `resolve_coordination_context` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:37-71; mcp/src/agents_remember/kernel/coordination_context/resolver.py:148-164 |

## Update History

- 2026-08-29T11:00+02:00 — Added the cancelled-closeout residue case: a staged add removed before
  the final add-all candidate cannot survive as a false missing-onboarding row.

- 2026-08-03T03:59:59+02:00 — Curated 4 citation findings (2 table rows, 2 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-05-24T18:51+02:00: Added coverage for renamed linked worktrees resolving external memory by Git common-directory repository identity.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new test file has an onboarding pair before closeout.
