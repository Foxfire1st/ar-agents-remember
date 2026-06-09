# mcp/tests/test_worktree_longpath_preflight.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_worktree_longpath_preflight.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T00:40+02:00                     |
| lastVerifiedCommitHash | `9911a8054b6314e051b094456a72eeec668c4c84`|
| lastVerifiedCommitDate | 2026-06-09T22:29:02+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Tests the worktree-start Windows long-path preflight: the pure
`long_path_block_payload` decision, the `longest_tracked_path_length` git
helper, and the `_long_path_preflight` gate over code and external-memory
repos.

## Code Commentary

### Logic

Payload tests cover under-budget (None), over-budget (blocked state with
projected length, budget, longest tracked length, and both remedies including
the computed shorten-by amount), and the exact-budget boundary. The git helper
is tested against a real temporary repository (longest committed path) and an
unborn repository (0). Gate tests drive `_long_path_preflight` with a
`SimpleNamespace` contract while mocking the registry check and the git
helper, so they run identically on Windows and Linux CI.

### Invariants And Boundaries

- The platform/registry dependency stays isolated in
  `_windows_long_paths_enabled`; everything else must remain testable
  cross-platform without mocking `os.name`.
- Existing-contract attach short-circuits before the preflight in
  `start_result`; these tests only cover the preflight itself.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The preflight and pure payload function under test. | [start.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/start.py) |
| The longest-tracked-path git helper. | [git.py](agents-remember-md/mcp/src/agents_remember/worktrees/modules/git.py) |

## Update History

- 2026-06-10T00:40+02:00: Created with the S8 worktree long-path preflight.
