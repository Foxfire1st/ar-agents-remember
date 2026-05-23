# scripts Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| doc_type               | `route-local-overview`                     |
| sourceRoute            | `scripts`                                  |
| lastUpdated            | 2026-05-23T05:35+02:00                     |
| lastVerifiedCommitHash | `7ab4b520b9178a31c4a5f5f8a5393b9b6ba82e0e` |
| lastVerifiedCommitDate | 2026-05-23T00:34:51+02:00                  |

## Purpose

`scripts/` contains source-checkout operational helpers that are intentionally
not installed into coordinator runtimes. The current route holds manual/debug
provider lifecycle code, provider setup/CGC seed mechanics, and the benchmark
runner.

## Current Model

Coordinator runtime installation copies only `runtime/scripts/install-skills.sh`
into `ar-coordination/scripts/`. Python provider and benchmark scripts stay in
the source checkout or package-owned MCP code so mutable coordinator files do
not become host-executed provider authority.

MCP runtime install and provider status use package-local modules under
`mcp/src/agents_remember/`. These source-level scripts remain useful for local
debugging and benchmark preparation, but normal agent-facing install/status
flows should go through MCP tools.

