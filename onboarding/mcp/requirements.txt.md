# mcp/requirements.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/requirements.txt`                     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`mcp/requirements.txt` is the simple checkout/install requirements file for
running the MCP package environment outside editable package metadata.

## Code Commentary

The file pins the MCP library at `1.27.1` and includes runtime response
contract dependencies `pydantic>=2,<3` and `tiktoken>=0.12,<1`.

## Invariants And Boundaries

- Keep this file aligned with the runtime dependencies in `mcp/pyproject.toml`.
- Do not downgrade the MCP dependency here unless there is a concrete
  compatibility reason and matching source/package metadata update.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| MCP package metadata declares the same runtime dependencies. | [pyproject.toml](agents-remember-md/mcp/pyproject.toml) |
| Pydantic response contracts live under the models package. | [models overview](agents-remember-md/mcp/src/agents_remember/models/overview.md) |

## Update History

- 2026-05-28T19:52+02:00: Created after requirements added Pydantic/tiktoken and restored the MCP dependency to `1.27.1`.
