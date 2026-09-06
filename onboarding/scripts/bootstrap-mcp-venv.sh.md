# scripts/bootstrap-mcp-venv.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `scripts/bootstrap-mcp-venv.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-07T00:00+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[repository overview](../overview.md)

## Purpose

Builds or selects the canonical project-owned CPython, then recreates `mcp/.venv` from that exact
interpreter with the locked uv dependency graph.

## Code Commentary

### Logic

The script loads the canonical runtime contract, delegates source-build installation, and probes
the base interpreter before touching the venv. It requires the pinned uv version. An explicit
`--replace` moves the old venv to a bounded rollback directory; any failed sync retains the failed
candidate for diagnosis and restores the predecessor. The new environment is installed with
`--python`, `--no-managed-python`, `--frozen`, and `--all-extras`, then capability-probed and checked
with `uv pip check`.

### Conventions

Interpreter provenance and dependency resolution are separate: python-build owns CPython; uv owns
the venv and locked packages but cannot substitute a managed interpreter.

### Invariants And Boundaries

- Replacement is explicit and rollback-safe; an existing venv is not silently overwritten.
- The selected interpreter must be exact 3.13.15 and expose both native pidfd APIs on Linux.
- uv may install packages but may not select `python-build-standalone` or system Python.
- The runtime, venv, backups, and compiled artifacts remain outside Git.

The Git hook selects a complete checkout-local `mcp/.venv`, or the primary clone’s shared `mcp/.venv`. Before selection it probes the pinned runtime capabilities and imports both quality tools and scope reporting. An incomplete environment stops with the bootstrap repair command; repository-root venvs and system Python are not alternate hook environments.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the canonical repository contract and scripts
own this bootstrap.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for the repository-owned bootstrap sequence. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The source-built interpreter is installed and capability-probed before venv mutation. | "install-python-runtime.sh" | scripts/bootstrap-mcp-venv.sh:33-41 |
| Existing environments require explicit replacement and are restored after a failed recreation. | "restore_previous() {" | scripts/bootstrap-mcp-venv.sh:53-81 |
| uv is pinned to the exact interpreter and lock, followed by runtime and dependency proof. | "--no-managed-python"; "uv pip check" | scripts/bootstrap-mcp-venv.sh:83-103 |

| Hook environment selection probes runtime and quality imports before using local or shared MCP venv. | "dev_python_ready() {"; "local_py="; "shared_py=" | .githooks/_gate.sh:53-80 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this script.

| Finding | Anchor | Source |
| --- | --- | --- |
| All durable inputs are carried by this repository's runtime contract and uv lock. | — | — |

## Update History

- 2026-09-07T00:00+02:00 — Preserved the current hook caller contract while retiring obsolete scope-reporting test documentation; verification pins unchanged.

- 2026-08-29T16:10+02:00 — Created for deterministic project-owned Python 3.13.15 bootstrap,
  rollback, and locked-venv adoption. Verification remains closeout-owned.
