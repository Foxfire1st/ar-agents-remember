# mcp/src/agents_remember/cli/context_packet.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Both flags and their request fields are removed.

### Superseded inventory

- Pre-repair card claim: Card documents --skip-providers and --provider-detail-limit. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/cli/context_packet.py:20 (def main)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`cli/context_packet.py` is the JSON-only CLI adapter for the context packet
application entry point: it parses arguments, loads trusted MCP settings, calls
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
  registration; the CLI must not grow behavior the application entry point does not own.

### Todos

No file-local todos.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No relevant external documentation found.

### Repo-Internal References

- The application entry point that builds the printed packet and owns request semantics. [1]
- CLI JSON output is covered by the context packet tests. [2]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

</details>
