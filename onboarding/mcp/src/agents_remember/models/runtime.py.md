# mcp/src/agents_remember/models/runtime.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`runtime.py` defines response contracts for runtime installation and resolved
coordination context tools.

## Code Commentary

`RuntimeInstallResponse` remains flexible because install reports include
summary and message blocks from installer services; since 2.5.1 it also
declares an optional `reportPath` — the full install detail (watcher rebind
runs, compose renders, transcripts) is filed under `temp/tool-reports/` while
the inline payload keeps counts and a compact rebind digest.
`ResolveContextResponse` uses a strict tool envelope and carries the resolved
context dictionary.

## Invariants And Boundaries

- Runtime install response shape is modeled, but installer-specific summary
  details remain flexible for now.
- Resolver output remains authoritative context data from the resolver service;
  path authority still comes from MCP settings.

## Evidence

### Repo-Internal References

- Runtime install application entry point produces the installer response payload. [1]
- Coordination application entry point exposes resolver output through MCP. [2]
