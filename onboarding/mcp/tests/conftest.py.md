# mcp/tests/conftest.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/conftest.py`                    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:03+02:00 |
| lastVerifiedCommitHash | `c881828542f0ca916ce8b1d4fd5ab8a914e24110` |
| lastVerifiedCommitDate | 2026-07-10T13:18:50+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Session-wide pytest setup that keeps the whole test suite hermetic and safe to
run from any environment. It is the single guard that prevents the
temporary-git-repo fixtures from ever committing into a real repository.

## Code Commentary

**260707-HFX2-L15 checkout-source pin.** The test bootstrap removes any previously imported
`agents_remember` modules and places this worktree's `mcp/src` first on `sys.path`. Re-verifiers
therefore test the candidate checkout instead of the official repo's editable-installed package.

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
| Worktree fixtures run `git` with `cwd=<temp repo>` and inherit the environment, so they depend on this guard. | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Conformance fixtures also shell out to `git` for temp-repo setup. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |
| The pre-push hook runs the suite via the quality wrapper, the original trigger of the ambient-`GIT_DIR` clobber. | [pre-push](agents-remember/.githooks/pre-push) |

## Update History

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added the worktree-local source/import pin so pytest
  cannot silently exercise a sibling editable install. Verification metadata remains pinned until
  closeout stamps the eventual L15 code commit.

- 2026-07-03T02:58+02:00 — No content impact: L13 reopen drill second cycle extended the marker comment; the reopened leaf ran under its original id with a fresh lifecycle.
- 2026-07-03T02:40+02:00 — No content impact: L13 reopen drill appended a marker comment at the end of conftest.py (no fixtures, env handling, or behavior touched); the drill exercises task_reopen mechanics, not this file.
- 2026-05-30T23:59+02:00: Created with `mcp/tests/conftest.py` (commit `36d74c5`). Added after the worktree fixtures clobbered the project repo when the suite ran with an inherited `GIT_DIR` (a git pre-push hook firing, and a concurrent evaluation run). The guard strips git's repo-pointer env and sets a fallback identity so no runner can redirect the fixtures onto a real repo.
