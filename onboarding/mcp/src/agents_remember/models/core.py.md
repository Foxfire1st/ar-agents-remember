# mcp/src/agents_remember/models/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/core.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`core.py` defines response models for the core `ping` MCP tool and `server_info`
tools.

## Code Commentary

`PingResponse` reports server identity, version, and transport. `ServerInfoResponse`
adds config, coordination, workspace, transcript, allowed repo/provider, public
tool, and reserved-tool metadata.

## Invariants And Boundaries

- Transport is currently the literal `stdio`.
- `server_info` should report configured authority and public surface, not
  perform runtime mutation.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Core payload builders serialize these models. | [tools.py](agents-remember-md/mcp/src/agents_remember/mcp/tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for core MCP response contracts.
