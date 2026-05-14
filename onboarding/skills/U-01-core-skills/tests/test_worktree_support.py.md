# test_worktree_support.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember-md                                       |
| path                   | `skills/U-01-core-skills/tests/test_worktree_support.py` |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-05-12T10:59                                         |
| lastVerifiedCommitHash | `f314b0d369e7f68125670caa99986cde1328e08a`               |
| lastVerifiedCommitDate | 2026-05-14T20:13:45+02:00|

## Purpose

This unittest file validates the first worktree-support helper slice.

## Code Commentary

### Logic

The tests cover memory ledger roundtrip/prepend behavior, branchless canonical ledger output, legacy branch-metadata ledger parsing without branch-metadata blocking, malformed ledger metadata, invalid ledger top-row detection, dirty external-memory start blocking, compatible external-memory start reporting, internal memory start reporting, worktree contract roundtrip with wrapper task roots and legacy task-root candidates, direct contract-path status loading, closeout commit-preview, approval-note, onboarding metadata refresh, missing-onboarding blocking behavior, direct checkout closeout dry-run/success/missing-onboarding behavior with `code_repository_name`/`code_repository_root` resolver args, internal resolver defaults to `ar-memory` plus `temp`, drift report path placement under `temp_root` including redirection away from durable memory repos, C-09 integration fast-forward/replay/conflict behavior, C-09 cleanup happy path/idempotence/blocking behavior, legacy cross-repo string rejection, v2 code-only inclusion, v2 memory inclusion with matching checkout branches and ledger commit metadata, C-10 adoption status/block/adopt behavior, and C-11 memory carryover plan/apply behavior.

### Conventions

The test imports helper modules directly from the repo path and uses only Python standard-library `unittest` and temporary directories.

### Invariants And Boundaries

These tests are focused smoke coverage, not exhaustive C-09 lifecycle integration tests. The C-09 coverage uses real temporary Git repos and worktrees, checks dirty-memory start blocking, checks closeout preview before approval, checks approval-note enforcement and recording, checks closeout metadata refresh to the new code commit before memory commit, checks missing onboarding blocking before code commit, checks direct checkout closeout preview without mutation, checks direct closeout metadata refresh plus ledger update, checks direct closeout missing-onboarding failure before code commit, checks fast-forward integration, checks replay integration after parallel non-overlapping source changes, checks conflict blocking before source branches move, and checks cleanup after successful integration. The C-10 coverage uses temporary code and memory repos, writes minimal verified onboarding, captures command output when exercising the CLI-style entry point, checks that adoption drift reports stay out of task folders, and checks that adoption writes `memory.md` plus the bootstrap `.gitkeep`. The C-11 coverage uses temporary code and memory repos to prove landed source branch code carries new onboarding into official memory, same-path but different official changes remain review-required, and unlanded source branch memory is rejected.

### Todos

Add fuller Git fixture tests for compatible external-memory start. Direct closeout currently has external-memory smoke coverage only; internal-memory semantics are intentionally not covered because the command is external-ledger focused.

### Docs References

No external documentation is needed for this standard-library test.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                                                                                                                                                                                                           | Citations            | Source Path                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| The test module imports the C-10 and C-11 helpers beside the C-09 helper and creates minimal file-level onboarding fixtures for adoption and carryover checks.                                                                                                                                                                    | L41-L61; L88-L106    | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| The common integration fixture creates real code and memory worktrees, closes a contract with code, memory content, and ledger commits, then reuses that fixture across integration tests.                                                                                                                                        | L203-L233            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| External-memory start blocks dirty source memory repos before worktree creation.                                                                                                                                                                                                                                                    | L320-L349            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Worktree contract tests check wrapper task roots without `-ar`, worktree groups with `-ar`, current-plus-legacy task-root candidates, and direct contract-path status loading.                                                                                                                                                    | L395-L430            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Closeout tests cover dry-run preview without approval, metadata refresh plan output, real closeout blocking without an approval note, approval-note persistence, onboarding metadata refresh to the new code commit, missing onboarding blocking, and dirty closed contracts reporting `commit-approval-pending`.                 | L433-L643            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Direct closeout tests create real current-branch code and memory repos, pass `code_repository_name` and `code_repository_root` through CLI-style namespaces, check dry-run preview without mutation, check code-first onboarding metadata refresh and ledger update, and verify missing onboarding blocks before the code commit. | L182-L201; L546-L633 | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| C-09 integration and cleanup tests cover ff-only source fast-forwarding, cleanup-pending status, cleanup removal, idempotent cleanup, cleanup blocking before integration, replay after parallel non-overlapping changes with a fresh ledger mapping, and code conflict blocking before main moves.                               | L645-L745            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| Resolver and drift-report path tests check `code_repository_name`, `temp_root`, default report placement under `temp/drift-reports`, relative report resolution, parent-directory escape fallback, absolute-path containment, and explicit memory-root report redirection back to temp.                                           | L747-L793            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| C-10 tests cover ready status without a ledger, `code_repository_name`/`code_repository_root` resolver args, drift report placement outside task folders, drift blocking without explicit acceptance, and initial ledger creation with docs `.gitkeep`.                                                                           | L834-L905            | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |
| C-11 tests pass `code_repository_name` and `code_repository_root`, then cover auto-carry for landed source branch code with new onboarding, refreshed official verification metadata, official ledger prepending, review-required same-path ambiguity, and rejected unlanded source branch memory.                                | L907-L1023           | [test_worktree_support.py](agents-remember-md/skills/U-01-core-skills/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository evidence is needed for the test itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-05-12T10:59: Updated coverage summary after branch fields were removed from canonical ledgers and legacy branch metadata became non-blocking.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale/placeholder test citation ranges after source verification.
- 2026-05-11T18:34: Updated after resolver-facing and C-11 test namespaces switched from ambiguous repo args to `code_repository_name` and `code_repository_root`.
- 2026-05-10T03:11: Updated after drift report path coverage began asserting explicit memory-root paths are redirected to coordination temp.
- 2026-05-11T03:00: Updated after adding C-11 memory carryover fixtures for landed, ambiguous, and unlanded source branch memory.
- 2026-05-10T03:01: Updated after adding C-09 direct checkout closeout fixture and dry-run/success/missing-onboarding tests.
- 2026-05-10T01:55: Updated after adding closeout metadata refresh and missing-onboarding regression coverage.
- 2026-05-10T01:19: Updated after adding closeout commit-approval preview and approval-note tests.
- 2026-05-10T01:04: Updated after adding direct contract-path status coverage.
- 2026-05-10T00:56: Updated after adding dirty external-memory start blocking and blocked integration status assertions.
- 2026-05-10T00:47: Updated after adding wrapper task-root assertions and C-09 cleanup lifecycle tests.
- 2026-05-10T00:36: Refreshed verification metadata after integration tests landed on main and removed a stale task-artifact reference.
- 2026-05-09T23:55: Updated coverage summary after adding C-09 integration fast-forward, replay, and conflict-blocking tests.
- 2026-05-09T23:22: Updated coverage summary after adding temp-root drift report path assertions.
- 2026-05-09T21:59: Created onboarding for the worktree-support smoke tests.
- 2026-05-09T22:10: Updated test coverage summary for malformed metadata, branch-mismatch blocking, compatible external-memory reporting, internal memory reporting, and cross-repo v2 include states.
- 2026-05-09T22:46: Updated coverage summary for C-10 adoption status, drift blocking, and ledger creation tests.
