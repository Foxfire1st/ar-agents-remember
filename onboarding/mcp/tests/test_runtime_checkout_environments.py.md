# mcp/tests/test_runtime_checkout_environments.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Integration tests verifying that `runtime_install` reports stale registered product checkouts in `checkoutEnvironments` (both in compact payloads and full overflow logs) without mutating or rebuilding any checkout environment.

## Code Commentary

`test_runtime_install_lists_registered_stale_checkouts_without_rebuilding` creates a temporary Git repository with `scripts/python-runtime-contract.env` (`AR_PYTHON_MINOR=3.14`), a scratch `UV_PYTHON_INSTALL_DIR` containing a valid `cpython-3.14-linux-x86_64-gnu` minor symlink, and multiple linked worktrees covering legacy-home, patch-pinned, carriage-return-path, incomplete-venv, current-minor-link, no-venv, and decoy-repository cases. It invokes `run_runtime_install(..., dry_run=True)` and asserts that exactly the four stale checkouts appear with shell-quoted `cd <path> && scripts/bootstrap-mcp-venv.sh` commands, `compact_runtime_install_payload` retains `checkoutEnvironments`, and all `pyvenv.cfg` bytes and mtimes remain untouched.

`test_runtime_install_overflow_retains_every_stale_checkout` creates 24 stale linked worktrees, invokes `runtime_install_payload` inside `tool_call_context`, and asserts that the overflowing answer logs all 24 stale checkouts in the whole-result log file.

## Relationships

Registered in the `integration` lane of `mcp/tests/test-evidence-lanes.toml` and as a consumer in `mcp/tests/evidence-lifecycle.toml`. Exercises `mcp/src/agents_remember/application/runtime/install.py`, `mcp/src/agents_remember/install/checkout_environments.py`, and `mcp/src/agents_remember/mcp/tools/core.py`.

## Evidence

- `test_runtime_install_lists_registered_stale_checkouts_without_rebuilding` verifies read-only stale-checkout inventory, NUL-safe path handling, and compact payload retention. [1]
- `test_runtime_install_overflow_retains_every_stale_checkout` verifies that overflowing `runtime_install` answers preserve every stale checkout in the recorded log. [2]
