# mcp/requirements.txt

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/requirements.txt` is the simple checkout/install requirements file for
running the MCP package environment outside editable package metadata.

## Code Commentary

### Logic

The file pins the MCP library at `1.27.1` and includes the runtime response
contract dependencies `pydantic>=2,<3` and `tiktoken>=0.12,<1`.

260915-KS-L1 added the knowledge store's SQLite binding, `apsw==3.53.4.0`. It is
**exact-pinned rather than ranged** because the capability the store needs — SQLite's session and changeset
machinery, which the standard library's `sqlite3` module does not expose — is compiled in through SQLite's
`ENABLE_SESSION` build option and therefore belongs to the specific wheel rather than to the APSW version line.
The in-file comment in `mcp/pyproject.toml` above that entry is the durable record of the reason; this file and
`mcp/uv.lock` are the two other places the pin must agree.

### Invariants And Boundaries

- Keep this file aligned with the runtime dependencies in `mcp/pyproject.toml`.
- Do not downgrade the MCP dependency here unless there is a concrete
  compatibility reason and matching source/package metadata update.
- `apsw` is a binary-wheel dependency, not a pure-Python one: changing its version is a capability change, not a
  routine bump, and the pinned release is the artifact whose session support was actually exercised.

## Evidence

### Repo-Internal References

- MCP package metadata declares the same runtime dependencies. [1]
- The exact SQLite-binding pin, with the session build-option reason recorded inline above it. [2]
- The same pin in this manifest, which must agree with the package metadata. [3]
- Pydantic response contracts live under the models package: the base model every knowledge vocabulary model inherits, declared against the pinned range. [4]
- The store that consumes the binding. [5]
