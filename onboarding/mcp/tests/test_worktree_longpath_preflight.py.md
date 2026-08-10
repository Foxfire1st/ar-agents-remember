# mcp/tests/test_worktree_longpath_preflight.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_longpath_preflight.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T00:40+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`|
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The preflight and pure payload function under test. | `long_path_block_payload`; `_long_path_preflight` | mcp/src/agents_remember/worktrees/modules/start.py:247-275; mcp/src/agents_remember/worktrees/modules/start.py:278-305 |
| The longest-tracked-path git helper. | `longest_tracked_path_length` | mcp/src/agents_remember/worktrees/modules/git.py:93-102 |

## Update History

- 2026-08-04T18:52+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the two malformed rows —
  `long_path_block_payload` + `_long_path_preflight` (start.py:248-308) and
  `longest_tracked_path_length` (git.py:93-103). Spurious `agents-remember/` prefixes dropped;
  claim wording unchanged.
- 2026-06-10T00:40+02:00: Created with the S8 worktree long-path preflight.
