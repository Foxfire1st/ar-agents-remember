# scripts/bootstrap-mcp-venv.sh

## Governing Overview

[repository overview](../overview.md)

## Purpose

Builds or selects the canonical project-owned CPython, then creates the calling code worktree's
`mcp/.venv` from that exact interpreter and that worktree's frozen uv lock. The editable install
imports the candidate's own source, not the primary checkout's installed source.

## Code Commentary

### Logic

The script loads the canonical runtime contract, delegates source-build installation, and probes
the base interpreter before touching the venv. It selects the interpreter binary from the
contract's minor value (`python$AR_PYTHON_MINOR`, `bootstrap-mcp-venv.sh:34`), so the venv follows
a contract bump. It requires the pinned uv version. An explicit
`--replace` moves the old venv to the user's cache rollback directory; a failed environment
recreation retains the failed candidate for diagnosis and restores the predecessor. Both backup
names include the worktree directory name and UTC second. After uv sync, runtime proof and
dependency checks succeed, the script removes the successful replacement backup. The rollback
root is created only on the existing-environment or failed-candidate branches, not on fresh success.
The new environment is installed with
`--python`, `--no-managed-python`, `--frozen`, and `--all-extras`, then capability-probed and checked
with `uv pip check`.

### Conventions

Interpreter provenance and dependency resolution are separate: python-build owns CPython; uv owns
the venv and locked packages but cannot substitute a managed interpreter.

### Invariants And Boundaries

- Replacement is explicit and rollback-safe; an existing venv is not silently overwritten.
- The selected interpreter must be exact 3.14.8 and expose both native pidfd APIs on Linux.
- uv may install packages but may not select `python-build-standalone` or system Python.
- The runtime, venv, backups, and compiled artifacts remain outside Git.
- Run the repository tool notes' bootstrap command at candidate intake, before the first command
  on the candidate; use explicit `--replace` after a sync changes `mcp/uv.lock`.
- Candidate tests, lint, type checks and agent scripts use the code worktree's own environment.
  The landed AR tools and memory-operation CLI remain product operations, not candidate tests.
- The shared runtime, uv cache and rollback cache are disclosed shared effects. The command must
  not write into the primary checkout or another worktree. Failed candidates remain for diagnosis;
  successful replacement backups do not accumulate.

The Git hook selects a complete checkout-local `mcp/.venv`, or the primary clone’s shared `mcp/.venv`. Before selection it probes the pinned runtime capabilities and imports both quality tools and scope reporting. An incomplete environment stops with the bootstrap repair command; repository-root venvs and system Python are not alternate hook environments.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies; the canonical repository contract and scripts
own this bootstrap.

No external source is required for the repository-owned bootstrap sequence.

### Repo-Internal References

- The source-built interpreter is installed and capability-probed before venv mutation. [1]

- Existing environments require explicit replacement; backup names distinguish worktree directories, and failed recreation restores the predecessor. [2]
- uv consumes the worktree's frozen lock and exact interpreter; successful runtime and dependency proof precede removal of the replaced backup. [3]

- Hook environment selection retains its separate local-then-shared policy and probes runtime and quality imports before selection. [4]

### Cross-Repo References

No meaningful cross-repository implementation source governs this script.

All durable inputs are carried by this repository's runtime contract and uv lock.
