# scripts/agent_evals/adapters/stdio_probe.py

## Governing Overview

[governing overview](../overview.md)

## Purpose

Initializes the exact supplied stdio definition, collects its paginated tool inventory and reads `server_info` in that session.

## Code Commentary

`_parse_server_info` prefers `result.structured_content` when present as a mapping and otherwise parses the JSON object from `TextContent` blocks in `result.content`, so probing succeeds against tool servers that emit compact single-line JSON text without duplicate `structuredContent`.

### Invariants And Boundaries

Repeated cursors or tool names refuse. Each awaited boundary has its own timeout (`PROBE_STEP_TIMEOUT_SECONDS`).

## Evidence

- The module initializes the stdio session with per-step timeouts, rejects duplicate cursors or tool names, and parses `server_info` from `structured_content` or JSON text blocks via `_parse_server_info`. [1]
