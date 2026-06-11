# mcp/src/agents_remember/providers/lifecycle/host_ports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/host_ports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`host_ports.py` owns host port availability checks and allocation for provider
containers.

## Code Commentary

### Logic

The module checks whether a host/port can be bound, honors explicit configured
ports, chooses the default port when available for `auto`, and falls back to an
ephemeral host port when the default is busy.

### Invariants And Boundaries

- Invalid or unavailable explicit ports raise `ContextProviderError`.
- Port allocation is provider-agnostic; provider modules supply host/default
  values and consume the selected port.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend uses shared host port allocation before building its Docker command. | [backend.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| GrepAI backend and embedder use the same host port allocation policy. | [backend.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py); [embedder.py](agents-remember/mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py) |

## Update History

- 2026-05-25T21:14+02:00: Created from the host port portion of the former shared lifecycle common module.
