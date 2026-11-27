# scripts/bootstrap-mcp-venv.sh

## Governing Overview

[repository overview](../overview.md)

## Purpose

Ensures and selects uv-managed CPython for `AR_PYTHON_MINOR`, then creates or migrates the calling code worktree's `mcp/.venv` from that uv minor symlink and that worktree's frozen uv lock. The editable install imports the candidate's own source, not the primary checkout's installed source.

## Code Commentary

### Logic

The script loads `scripts/python-runtime-contract.env`, resolves the PATH `uv` before any runtime or venv mutation, and accepts `AR_UV_VERSION` or newer by decimal-part comparison (`version_at_least`, `resolve_uv`). Missing, older, unreadable, or failed version output is refused with the minimum and available version/path; the first reported version token is retained on refusal. It installs no `uv`. The gate prints the accepted version and path; a failed frozen sync repeats that identity and minimum.

It then ensures uv-managed CPython with `uv python install --no-bin "$AR_PYTHON_MINOR"`, locates its minor symlink with `uv python find --system --managed-python --no-python-downloads "$AR_PYTHON_MINOR"`, and probes the base interpreter with `scripts/check-python-runtime.py --base-interpreter --require-linux-pidfd --uv-version "$observed_uv"`.

Before inspecting or mutating `mcp/.venv`, the script acquires an exclusive `fcntl.flock` on `$repo_root/mcp` (file descriptor 9). It supports optional `[--replace | --ensure]`: if `mcp/.venv` already points to `$runtime_base/bin` (`current_venv` via `agents_remember.python_runtime.read_venv_home`), `--ensure` returns 0 when `mcp/.venv/bin/python` is executable, ordinary mode refuses without `--replace`, and `--replace` moves the existing venv aside; if an existing `mcp/.venv` points at a stale base, it is moved aside and recreated automatically even without `--replace`. Each backup path uses a private `mktemp -d` reservation under `${XDG_CACHE_HOME:-$HOME/.cache}/agents-remember/venv-backups` carrying the worktree directory name and UTC second, so directory and symlink predecessors restore cleanly on failure while retaining the failed candidate for diagnosis. After `uv sync --project "$repo_root/mcp" --python "$AR_PYTHON_MINOR" --managed-python --no-python-downloads --frozen --all-extras`, `scripts/check-python-runtime.py`, and `uv pip check` succeed, the replaced backup is removed. After that venv transaction finishes, the script pre-warms the external grammar cache for this repository's languages by running `agents-remember languages warm --repo "$repo_root"` (writing only to the external language cache, never into `mcp/.venv`).

### Conventions

uv owns both the managed CPython minor-link runtime (`--managed-python --no-python-downloads`) and locked package installation; system or PATH Python is refused.

### Invariants And Boundaries

- An existing current-base venv is never overwritten without `--replace` (and is reused under `--ensure`); a stale-base venv is replaced under exclusive `mcp/` flock with rollback restoration on failure.
- The selected interpreter must match `AR_PYTHON_MINOR` (`3.14`) through uv's minor symlink and expose both native pidfd APIs on Linux.
- System and PATH Python are refused; the bootstrap uses only uv-managed CPython (`--managed-python --no-python-downloads`).
- The runtime, venv, backups, and compiled artifacts remain outside Git.
- Run the repository tool notes' bootstrap command at candidate intake, before the first command on the candidate; use explicit `--replace` after a sync changes `mcp/uv.lock`.
- Candidate tests, lint, type checks and agent scripts use the code worktree's own environment. The landed AR tools and memory-operation CLI remain product operations, not candidate tests.
- The uv Python directory, uv cache and rollback cache are disclosed shared effects. The command must not write into the primary checkout or another worktree. Failed candidates remain for diagnosis; successful replacement backups do not accumulate.

The Git hook selects a complete checkout-local `mcp/.venv`, or the primary clone's shared `mcp/.venv`. Before selection it probes the minor-line runtime capabilities and imports both quality tools and scope reporting. An incomplete environment stops with the bootstrap repair command; repository-root venvs and system Python are not alternate hook environments.

After selecting its interpreter, the Git hook prepends the current checkout's `mcp/src` to `PYTHONPATH`, including when it uses the complete environment from the primary clone.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; the canonical repository contract and scripts own this bootstrap.

No external source is required for the repository-owned bootstrap sequence.

### Repo-Internal References



- The uv-managed interpreter is installed, located through uv's minor link, and capability-probed before venv mutation. [1]




- Replacement acquires an exclusive lock on `mcp/`, reuses a current venv under `--ensure`, requires `--replace` for a current venv, replaces a stale-base venv automatically, and rolls back on failure while retaining the failed candidate. [2]




- `uv sync` runs with `--managed-python --no-python-downloads --frozen --all-extras`; post-sync runtime proof and `uv pip check` precede removal of the replaced backup. [3]





- Hook environment selection retains its separate local-then-shared policy and probes minor-line runtime and quality imports before selection. [4]




- A qualifying PATH uv is selected without installation before runtime/venv mutation, with minimum and observed identity in diagnostics. [5]



### Cross-Repo References

This card uses repository-owned code and test references and invokes no sibling-repository contract.

The runtime minor line and uv floor are declared in `scripts/python-runtime-contract.env`; bootstrap freezes dependency resolution with `uv sync --frozen` against the MCP project.

- The hook prepends the checkout's code to any inherited Python search path. [6]
