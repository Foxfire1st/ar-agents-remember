# .githooks/_gate.sh

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The shared body of this repository's Git hooks. `pre-commit` runs the `fast` tier over the staged content, `pre-push` runs the `targeted` tier, and the `full` tier refuses host execution because acceptance runs only in the Dagger pipeline. The tiers run deterministic checks and no test.

## Code Commentary

Before any check, the script needs a complete MCP development environment: it takes `mcp/.venv/bin/python` from this checkout or from the primary worktree when that interpreter passes the runtime-contract check and imports Pyright, Ruff and the scope-reporting support, and stops with the bootstrap command otherwise. It puts this checkout's `mcp/src` first on `PYTHONPATH`.

`run_fast_checks` first calls `dashboard_prerequisites`. When `dashboard/package.json` exists, a missing `dashboard/node_modules` stops the tier with the instruction to run `npm ci` in `dashboard/`, and a missing `npm` stops it with its own message, before any long check runs. Without `dashboard/package.json` the look passes and the dashboard checks are skipped later. The tier then reports its wrapper, checks the generated copies, runs Ruff, the Ruff format check, Pyright and the evidence lifecycle catalog over the index-known Python population, and ends with the dashboard's codegen, lint and typecheck. Each step prints its own result line, and the run ends on the tier's pass or fail line, so a prerequisite refusal still ends on `fast-tier FAIL` or `targeted-tier FAIL`.

`run_targeted_checks` repeats `run_fast_checks`. In the fast tier the script parks unstaged and untracked content with `git stash push --keep-index` and restores it on every exit, except during a merge, rebase or cherry-pick, where it checks the working tree as it is.

The fast tier passes every tracked Python file to one GNU `xargs` invocation with a 256 KiB buffer, so Ruff and Pyright run once instead of twice. It derives every tier scope line in one `scope_reporting hook-batch` call and replays each line in its original position. The Python and dashboard rails run concurrently, but their buffered output is printed Python first and dashboard second; a failure in either rail fails the tier. Dashboard ESLint uses a content-addressed `.eslintcache`, and the dashboard's TypeScript projects use incremental build-info files; both are gitignored. `PYRIGHT_PYTHON_IGNORE_WARNINGS=1` is set only for Pyright, and a real type error still fails.

## Relationships

`pre-commit` and `pre-push` call this script; `setup-hooks.sh` enables them per clone. The landing commit check reads the tier's last result line out of a refusal, which is why the prerequisite look runs inside `run_fast_checks` rather than before the tier starts. `mcp/tests/test_git_hook_dashboard_prerequisites.py` runs the real script against a small Git tree.

## Evidence

- The dashboard prerequisite look skips a tree without the dashboard package and stops on a missing dependency folder or npm. [1]
- The targeted tier repeats the fast checks, and the full tier refuses host execution. [3]
- The script selects a complete MCP development environment or stops with the bootstrap command. [5]

- One 256 KiB xargs batch passes the tracked Python population to Ruff and Pyright. [6]
- Every tier scope line is rendered by one scope-batch invocation. [7]
- The Python and dashboard rails overlap while their output keeps fixed order. [8]
- The warm caches are content-addressed and the Pyright wrapper notice is silenced. [9]

- The fast tier runs the prerequisite look first and the dashboard checks last. [2]
- Every tier ends on its own pass or fail line. [4]
