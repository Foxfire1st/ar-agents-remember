# test_worktree_support.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `skills/U-01-core-skills/tests/test_worktree_support.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-10T01:01                           |
| lastVerifiedCommitHash | `b6a5c21f9309642125a468e63c8aad1a3f3beb88` |
| lastVerifiedCommitDate | 2026-05-10T01:01                           |

## Purpose

This unittest file validates the first worktree-support helper slice.

## Code Commentary

### Logic

The tests cover memory ledger roundtrip/prepend behavior, malformed ledger metadata, invalid ledger top-row detection, branch-mismatched and dirty shared-memory start blocking, compatible shared-memory start reporting, internal memory start reporting, worktree contract roundtrip with wrapper task roots and legacy task-root candidates, internal resolver defaults to `ar-memory` plus `temp`, drift report path placement under `temp_root`, C-09 integration fast-forward/replay/conflict behavior, C-09 cleanup happy path/idempotence/blocking behavior, legacy cross-repo string rejection, v2 code-only inclusion, v2 memory inclusion with matching branch/ledger metadata, and C-10 adoption status/block/adopt behavior.

### Conventions

The test imports helper modules directly from the repo path and uses only Python standard-library `unittest` and temporary directories.

### Invariants And Boundaries

These tests are focused smoke coverage, not exhaustive C-09 lifecycle integration tests. The C-09 integration coverage uses real temporary Git repos and worktrees, checks dirty-memory start blocking, checks fast-forward integration, checks replay integration after parallel non-overlapping source changes, checks conflict blocking before source branches move, and checks cleanup after successful integration. The C-10 coverage uses temporary code and memory repos, writes minimal verified onboarding, captures command output when exercising the CLI-style entry point, checks that adoption drift reports stay out of task folders, and checks that adoption writes `memory.md` plus the bootstrap `.gitkeep`.

### Todos

Add fuller Git fixture tests for compatible shared-memory start. C-10 now has initial command-level coverage, but wrapper UX around its JSON output is not covered here.

### Docs References

No external documentation is needed for this standard-library test.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The test module imports the C-10 helper beside the C-09 helper and creates minimal file-level onboarding fixtures for adoption checks. | L37-L49; L80-L85 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| The shared integration fixture creates real code and memory worktrees, closes a contract with code, memory content, and ledger commits, then reuses that fixture across integration tests. | L104-L165 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Shared-memory start blocks dirty source memory repos before worktree creation. | L238-L270 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Worktree contract tests check wrapper task roots without `-ar`, worktree groups with `-ar`, and current-plus-legacy task-root candidates. | L313-L345 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| C-09 integration and cleanup tests cover ff-only source fast-forwarding, cleanup-pending status, cleanup removal, idempotent cleanup, cleanup blocking before integration, replay after parallel non-overlapping changes with a fresh ledger mapping, and code conflict blocking before main moves. | L347-L449 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Resolver and drift-report path tests check `temp_root`, default report placement under `temp/drift-reports`, relative report resolution, parent-directory escape fallback, and absolute-path containment. | L449-L490 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| C-10 tests cover ready status without a ledger, drift report placement outside task folders, drift blocking without explicit acceptance, and initial ledger creation with docs `.gitkeep`. | L530-L605 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository evidence is needed for the test itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-10T00:56: Updated after adding dirty shared-memory start blocking and blocked integration status assertions.
- 2026-05-10T00:47: Updated after adding wrapper task-root assertions and C-09 cleanup lifecycle tests.
- 2026-05-10T00:36: Refreshed verification metadata after integration tests landed on main and removed a stale task-artifact reference.
- 2026-05-09T23:55: Updated coverage summary after adding C-09 integration fast-forward, replay, and conflict-blocking tests.
- 2026-05-09T23:22: Updated coverage summary after adding temp-root drift report path assertions.
- 2026-05-09T21:59: Created onboarding for the worktree-support smoke tests.
- 2026-05-09T22:10: Updated test coverage summary for malformed metadata, branch-mismatch blocking, compatible shared-memory reporting, internal memory reporting, and cross-repo v2 include states.
- 2026-05-09T22:46: Updated coverage summary for C-10 adoption status, drift blocking, and ledger creation tests.
