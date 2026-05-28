# mcp/src/agents_remember/models/runtime.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/models/runtime.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T19:52+02:00                     |
| lastVerifiedCommitHash | `bf3a3c4e310fb11032da885083d026a74a31ee9c` |
| lastVerifiedCommitDate | 2026-05-28T20:06:49+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`runtime.py` defines response contracts for runtime installation and resolved
coordination context tools.

## Code Commentary

`RuntimeInstallResponse` remains flexible because install reports include
summary and message blocks from installer services. `ResolveContextResponse`
uses a strict tool envelope and carries the resolved context dictionary.

## Invariants And Boundaries

- Runtime install response shape is modeled, but installer-specific summary
  details remain flexible for now.
- Resolver output remains authoritative context data from the resolver service;
  path authority still comes from MCP settings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime install controller produces the installer response payload. | [runtime_install.py](agents-remember-md/mcp/src/agents_remember/controllers/runtime_install.py) |
| Coordination controller exposes resolver output through MCP. | [coordination_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/coordination_tools.py) |

## Update History

- 2026-05-28T19:52+02:00: Created for runtime and resolver response contracts.
