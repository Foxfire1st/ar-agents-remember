# mcp/src/agents_remember/install/checkout_environments.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Inspects all registered Git worktrees of the configured product repository and reports those whose existing `mcp/.venv` does not point at the contract uv-managed Python minor link, together with the exact per-checkout bootstrap command, without rebuilding or mutating any environment.

## Code Commentary

`inspect_checkout_environments(repository)` reads `AR_PYTHON_MINOR` from `scripts/python-runtime-contract.env` and enumerates registered worktrees with `run_git_bytes(repository, ["worktree", "list", "--porcelain", "-z"])` so paths containing spaces, quotes, or carriage returns are handled safely.

For each registered checkout, `_is_stale_environment` checks only checkouts where `mcp/.venv` exists: a missing or malformed `pyvenv.cfg` `home`, a `home` not ending in `bin`, or a base failing `is_uv_minor_base(home.parent, minor)` marks the checkout stale. Each stale checkout is returned as `{checkout, bootstrapCommand}` via `_migration_row` using `shlex.quote` (`cd <quoted> && scripts/bootstrap-mcp-venv.sh`). When any stale checkouts are found, `instruction` tells the operator to run each command once its checkout has the uv-managed bootstrap. Read or Git failures populate `error` rather than raising or fabricating an empty clean list.

## Relationships

Called by `mcp/src/agents_remember/application/runtime/install.py::run_runtime_install` to populate `result["checkoutEnvironments"]` for the configured `agents-remember` repository. Delegates Git execution to `kernel/git_command.py::run_git_bytes` and base checks to `python_runtime.py`. Verified by `mcp/tests/test_runtime_checkout_environments.py`.

## Evidence

- `inspect_checkout_environments` reads `AR_PYTHON_MINOR`, enumerates NUL-delimited Git worktrees, and reports stale environments and errors without mutating checkouts. [1]
- `_is_stale_environment` checks only existing `mcp/.venv` directories against `read_venv_home` and `is_uv_minor_base`. [2]
- `_migration_row` formats the shell-quoted per-checkout `scripts/bootstrap-mcp-venv.sh` command. [3]
