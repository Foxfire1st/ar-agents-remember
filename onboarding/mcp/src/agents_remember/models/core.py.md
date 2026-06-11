# mcp/src/agents_remember/models/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/core.py`   |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-06T12:28+02:00                     |
| lastVerifiedCommitHash | `11f28a2035f06f8bc33f11b0617b41cda1122c1f` |
| lastVerifiedCommitDate | 2026-06-06T13:01:33+02:00|
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
| Core payload builders serialize these models. | [core.py](agents-remember/mcp/src/agents_remember/mcp/tools/core.py) |

## Update History

- 2026-06-06T12:28+02:00: Corrected the core payload-builder reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-05-28T19:52+02:00: Created for core MCP response contracts.
