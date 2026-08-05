# mcp/requirements.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/requirements.txt`                     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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
| MCP package metadata declares the same runtime dependencies. | "pydantic>=2,<3" | mcp/pyproject.toml:25-25 |
| Pydantic response contracts live under the models package. | `# mcp/src/agents_remember/models/ - Response Contract Models Overview` | onboarding/mcp/src/agents_remember/models/overview.md:1-506 |

## Update History

- 2026-08-02T21:08+02:00 — 260731-EFA-L6 W2-B09 curator: repaired 2 citation entries (4 findings); no Tier-3 findings.

- 2026-05-28T19:52+02:00: Created after requirements added Pydantic/tiktoken and restored the MCP dependency to `1.27.1`.
