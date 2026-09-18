# mcp/requirements.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/requirements.txt`                     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-15T22:40+02:00                     |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00 |
| governingOverview      | `overview.md`                              |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP package metadata declares the same runtime dependencies. | "pydantic>=2,<3" | mcp/pyproject.toml:28-28 |
| The exact SQLite-binding pin, with the session build-option reason recorded inline above it. | "apsw==3.53.4.0" | mcp/pyproject.toml:21-26 |
| The same pin in this manifest, which must agree with the package metadata. | "apsw==3.53.4.0" | mcp/requirements.txt:2-2 |
| Pydantic response contracts live under the models package: the base model every knowledge vocabulary model inherits, declared against the pinned range. | `KnowledgeModel` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The store that consumes the binding. | `open_database`; `apply_connection_contract` | mcp/src/agents_remember/memory/knowledge/connection.py:26-32 |

## Update History

- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): recorded the new `apsw==3.53.4.0` entry, why the pin is exact (session support is a build-time SQLite option carried by the wheel, not by the version line) and that the three places it appears must agree. Corrected the `pydantic>=2` citation, which the insertion shifted from `mcp/pyproject.toml:22` to `:28`, and added the matching rows for the pin itself and for the store that consumes the binding. Verification metadata remains closeout-owned.

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-05-28T19:52+02:00: Created after requirements added Pydantic/tiktoken and restored the MCP dependency to `1.27.1`.
