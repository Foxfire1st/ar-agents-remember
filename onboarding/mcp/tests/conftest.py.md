# mcp/tests/conftest.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/conftest.py`                    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T23:59+02:00                     |
| lastVerifiedCommitHash | `36d74c5f3fd11b25c96008f06b058105c5c083e2` |
| lastVerifiedCommitDate | 2026-05-30T23:57:28+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

Session-wide pytest setup that keeps the whole test suite hermetic and safe to
run from any environment. It is the single guard that prevents the
temporary-git-repo fixtures from ever committing into a real repository.

## Code Commentary

At conftest import time (before any test is collected or run) the module mutates
`os.environ`:

- It pops git's repo-pointer / object-store variables — `GIT_DIR`,
  `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
  `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`,
  `GIT_PREFIX`. The worktree/closeout/conformance fixtures run `git` with
  `cwd=<temp repo>` but inherit the process environment; any of these variables,
  if present, redirect those `git` subprocesses onto whatever repository they
  point at instead of the temp dir. They are commonly set when the suite runs
  inside a `git` hook (git exports `GIT_DIR` to hooks) or under a parent process
  with `GIT_DIR` set.
- It then `setdefault`s a fallback commit identity
  (`GIT_AUTHOR_*`/`GIT_COMMITTER_*` = "Agents Remember Tests") so the committing
  fixtures never fail with "Author identity unknown" on a machine with no
  configured git user; an already-exported identity is respected.

## Invariants And Boundaries

- This guard must run at import (module level), before any fixture spawns a
  `git` subprocess, so the cleaned environment is inherited by every test.
- Fixture `git` calls deliberately rely on `cwd` for repo selection; this file
  exists so an ambient `GIT_DIR` cannot override that and hijack a real repo.
- The fallback identity only affects throwaway fixture commits in temp dirs,
  never real repository commits.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree fixtures run `git` with `cwd=<temp repo>` and inherit the environment, so they depend on this guard. | [test_worktree_support.py](agents-remember-md/mcp/tests/test_worktree_support.py) |
| Conformance fixtures also shell out to `git` for temp-repo setup. | [test_tool_response_conformance.py](agents-remember-md/mcp/tests/test_tool_response_conformance.py) |
| The pre-push hook runs the suite via the quality wrapper, the original trigger of the ambient-`GIT_DIR` clobber. | [pre-push](agents-remember-md/.githooks/pre-push) |

## Update History

- 2026-05-30T23:59+02:00: Created with `mcp/tests/conftest.py` (commit `36d74c5`). Added after the worktree fixtures clobbered the project repo when the suite ran with an inherited `GIT_DIR` (a git pre-push hook firing, and a concurrent evaluation run). The guard strips git's repo-pointer env and sets a fallback identity so no runner can redirect the fixtures onto a real repo.
