# mcp/src/agents_remember/python_runtime.py

## Governing Overview

[MCP overview](../../overview.md)

## Purpose

Provides the stdlib-only policy helpers that locate uv's Python installation directory and verify that a virtual environment or interpreter base uses uv's minor-version symlink without executing `uv`.

## Code Commentary

`read_venv_home(venv)` reads the `home` key from `pyvenv.cfg` without resolving symlinks, returning `None` when the file or key is absent.

`uv_python_directory(environ)` resolves uv's Linux and macOS Python directory in uv's documented order: `UV_PYTHON_INSTALL_DIR` (expanded and made absolute), then `XDG_DATA_HOME/uv/python`, then `$HOME/.local/share/uv/python` (falling back to `Path.home()`).

`is_uv_minor_base(base, minor)` verifies that `base` sits lexically directly under `uv_python_directory()`, is named `cpython-<minor>-<platform>`, is a symbolic link whose target is a sibling directory named `cpython-<minor>.<patch>-<platform>` in the same parent directory, and resolves to an existing directory. An environment bound directly to a patch directory or outside uv's Python directory fails this check so patch upgrades via `uv python upgrade` keep working without rebuilding the venv.

## Relationships

Consumed by `scripts/check-python-runtime.py`, `scripts/bootstrap-mcp-venv.sh` (`current_venv`), `scripts/pnt_sandbox/operations.py`, and `mcp/src/agents_remember/install/checkout_environments.py`. Because `scripts/check-python-runtime.py` and `scripts/bootstrap-mcp-venv.sh` import it from `mcp/src` before project dependencies are installed, this module must stay pure Python standard library.

## Evidence

- `read_venv_home` parses `pyvenv.cfg` `home` without resolving symlinks. [1]
- `uv_python_directory` follows `UV_PYTHON_INSTALL_DIR`, `XDG_DATA_HOME`, and `$HOME/.local/share/uv/python` precedence. [2]
- `is_uv_minor_base` requires a lexical uv minor symlink pointing to a sibling patch directory inside `uv_python_directory()`. [3]
