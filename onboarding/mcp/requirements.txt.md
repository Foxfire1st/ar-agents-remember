# mcp/requirements.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/requirements.txt`                     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a` |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| MCP package metadata declares the same runtime dependencies. | "pydantic>=2" | mcp/pyproject.toml:22-22 |
| Pydantic response contracts live under the models package. | `# mcp/src/agents_remember/models/ - Response Contract Models Overview` | onboarding/mcp/src/agents_remember/models/overview.md:1-506 |

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-05-28T19:52+02:00: Created after requirements added Pydantic/tiktoken and restored the MCP dependency to `1.27.1`.
