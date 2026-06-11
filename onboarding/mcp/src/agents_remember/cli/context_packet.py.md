# mcp/src/agents_remember/cli/context_packet.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/cli/context_packet.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T08:39+02:00                     |
| lastVerifiedCommitHash | `f62c732df2acc30ec3766f83c176a24b39c0bc46`                         |
| lastVerifiedCommitDate | 2026-06-10T10:41:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/context_packet.py` is the JSON-only CLI adapter for the context packet
controller: it parses arguments, loads trusted MCP settings, calls
`build_context_packet`, and prints the packet (or an `ok:false` error object)
as JSON.

## Code Commentary

### Logic

`main(argv)` requires `--config` (trusted MCP settings JSON) and `--repo`
(repository id from those settings), with `--skip-providers`,
`--include-drift`, `--include-freshness` (issue #54: requests the branch
freshness section, which fetches remote-tracking refs), `--provider-detail-limit`,
`--drift-detail-limit`, and `--fetch-timeout` shaping the
`ContextPacketRequest`. `ConfigError`/`ContextPacketError`/`ValueError` become
a single-line `{"ok": false, ...}` JSON with exit code 1; success prints the
indented packet and returns 0.

### Conventions

Thin adapter: no behavior beyond argument-to-request mapping and JSON output.
Flag surface mirrors the MCP `context_packet` tool registration.

### Invariants And Boundaries

- Keep the flag set in lockstep with `ContextPacketRequest` and the MCP tool
  registration; the CLI must not grow behavior the controller does not own.

### Todos

No file-local todos.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The controller that builds the printed packet and owns request semantics. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| CLI JSON output is covered by the context packet tests. | [test_context_packet.py](agents-remember/mcp/tests/test_context_packet.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-06-10T08:39+02:00: Created during issue #54 sub-task A when the CLI gained `--include-freshness` and `--fetch-timeout` (first sidecar for this pre-existing adapter).
