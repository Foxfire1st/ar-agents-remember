# scripts/bootstrap-mcp-venv.sh

## Governing Overview

[repository overview](../overview.md)

## Purpose

Builds or selects the canonical project-owned CPython, then recreates `mcp/.venv` from that exact
interpreter with the locked uv dependency graph.

## Code Commentary

### Logic

The script loads the canonical runtime contract, delegates source-build installation, and probes
the base interpreter before touching the venv. It selects the interpreter binary from the
contract's minor value (`python$AR_PYTHON_MINOR`, `bootstrap-mcp-venv.sh:34`), so the venv follows
a contract bump. It requires the pinned uv version. An explicit
`--replace` moves the old venv to a bounded rollback directory; any failed sync retains the failed
candidate for diagnosis and restores the predecessor. The new environment is installed with
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
- Existing environments require explicit replacement and are restored after a failed recreation. [2]
- uv is pinned to the exact interpreter and lock, followed by runtime and dependency proof. [3]

| Hook environment selection probes runtime and quality imports before using local or shared MCP venv. | "dev_python_ready() {"; "local_py="; "shared_py=" | .githooks/_gate.sh:53-80 |

### Cross-Repo References

No meaningful cross-repository implementation source governs this script.

All durable inputs are carried by this repository's runtime contract and uv lock.
