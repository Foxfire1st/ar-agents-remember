# mcp/src/agents_remember/worktrees/modules/git.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/worktrees/modules/git.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T00:40+02:00                     |
| lastVerifiedCommitHash | `9911a8054b6314e051b094456a72eeec668c4c84` |
| lastVerifiedCommitDate | 2026-06-09T22:29:02+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Owns the Git subprocess adapter and small repository state helpers used by the
`c-09-git-worktree-manager` skill worktree lifecycle.

## Code Commentary

All Git commands run with `stdin=subprocess.DEVNULL` and an explicit
`safe.directory` override. The module exposes branch, commit, cleanliness,
worktree creation, commit-if-dirty, and changed-path helpers without owning
workflow policy.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Memory baseline code reuses these facade-exported Git helpers. | [baseline.py](agents-remember-md/mcp/src/agents_remember/memory/baseline.py) |
| Worktree tests cover changed-path behavior for long filesystem paths. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |

## Update History

- 2026-06-10T00:40+02:00 — Added `longest_tracked_path_length()` (`git ls-tree -r --name-only <ref>` with HEAD fallback, 0 for unborn repos) for the worktree-start Windows long-path preflight.

- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
