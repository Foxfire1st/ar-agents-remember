# mcp/tests/test_pnt_sandbox_prepare_python.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Unit tests verifying that PNT sandbox `start` refuses pre-migration product checkouts before environment work and that `Operations.prepare_python` preserves `UV_PYTHON_INSTALL_DIR` while delegating to `scripts/bootstrap-mcp-venv.sh --ensure`.

## Code Commentary

`test_start_refuses_mismatched_runtime_before_environment_work` parametrizes over two legacy checkout markers (`bootstrap` missing `--ensure` and `contract` declaring `AR_PYTHON_SOURCE_URL`), isolates workspace harness markers, patches `commands._start` and `Operations.prepare_python`, and asserts `commands.start` raises `SandboxRefusal` naming the runtime contract mismatch and the per-revision PNT tooling remedy without creating the sandbox root or `mcp/.venv`.

`test_prepare_python_preserves_uv_install_dir_for_checkout_bootstrap` parametrizes over cold vs existing `mcp/.venv/bin/python` and host `XDG_DATA_HOME` vs explicit `UV_PYTHON_INSTALL_DIR`. It patches `pnt_sandbox.operations.subprocess.run` and asserts `Operations.prepare_python` invokes `["bash", "scripts/bootstrap-mcp-venv.sh", "--ensure"]` in the checkout directory with sandbox-redirected `XDG_DATA_HOME` while keeping `UV_PYTHON_INSTALL_DIR` anchored to the caller's uv Python directory.

## Relationships

Registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml` and as a consumer in `mcp/tests/evidence-lifecycle.toml`. Uses `mcp/tests/pnt_sandbox_test_support.py` to exercise `scripts/pnt_sandbox/operations.py`.

## Evidence

- `test_start_refuses_mismatched_runtime_before_environment_work` verifies pre-migration checkouts are refused before `_start` or `prepare_python`. [1]
- `test_prepare_python_preserves_uv_install_dir_for_checkout_bootstrap` verifies `prepare_python` runs `bootstrap-mcp-venv.sh --ensure` with preserved `UV_PYTHON_INSTALL_DIR` across sandbox `XDG_DATA_HOME` redirection. [2]
