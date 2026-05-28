# mcp/src/agents_remember/mcp/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/mcp/__init__.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T15:43+02:00                     |
| lastVerifiedCommitHash | `9680d150ac9d2e6c1ae04dbab42eac0088dceef8` |
| lastVerifiedCommitDate | 2026-05-28T15:55:29+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

Defines package-level MCP server identity constants used by public payload
builders.

## Code Commentary

The module currently exposes `SERVER_NAME` and `SERVER_VERSION`. Payload
builders in `mcp.tools` use those constants for `ping` and `server_info`, so
release version bumps must keep `SERVER_VERSION` aligned with
`mcp/pyproject.toml`.

## Docs References

No external Domain Documentation source is configured for this memory repo.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `ping_payload()` and `server_info_payload()` report `SERVER_VERSION`. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |
| Tool tests assert the public version reported by `ping_payload()`. | [test_tools.py](agents-remember-md/mcp/tests/test_tools.py) |

## Update History

- 2026-05-28T15:43+02:00: Created while preparing MCP package release `0.2.0`. Verification metadata remains pinned until closeout commits the source change.
