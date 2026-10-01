# mcp/src/agents_remember/providers/lifecycle/host_ports.py

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

## Evidence

### Repo-Internal References

- CGC backend uses shared host port allocation before building its Docker command. [1]
- GrepAI backend and embedder use the same host port allocation policy. [2]
