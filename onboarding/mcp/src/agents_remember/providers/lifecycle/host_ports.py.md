# mcp/src/agents_remember/providers/lifecycle/host_ports.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/host_ports.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| CGC backend uses shared host port allocation before building its Docker command. | `cgc_backend_host_ports` | mcp/src/agents_remember/providers/cgc/lifecycle/backend.py:333-349 |
| GrepAI backend and embedder use the same host port allocation policy. | `grepai_backend_host_port`; `grepai_embedder_host_port` | mcp/src/agents_remember/providers/grepai/lifecycle/backend.py:399-409; mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py:350-360 |

## Update History

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 2 citation claims
  (Repo-Internal reference rows); scoped result 0 findings.

- 2026-05-25T21:14+02:00: Created from the host port portion of the former shared lifecycle common module.
