# mcp/src/agents_remember/package_data/paseo_plugin/server/embed.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper reads the sole provisioned dashboard/frame pair list from the selected Paseo home.

## Code Commentary

PASEO_HOME is required and selects agents-remember/embed.json. A missing file is an unprovisioned empty list; other reads and malformed existing pair arrays fail. Provisioning/reload owns refresh, and the client owns exact-origin trust.

## Invariants And Boundaries

Malformed present data cannot claim successful empty trust. This pair list carries URLs/origins, not secrets or another runtime registry.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `embedListPath` | `mcp/src/agents_remember/package_data/paseo_plugin/server/embed.ts:13-43` |
| Current source owner or exact assertion described above. | `readEmbedList` | `mcp/src/agents_remember/package_data/paseo_plugin/server/embed.ts:33-49` |
| Current source owner or exact assertion described above. | `ENOENT` | `mcp/src/agents_remember/package_data/paseo_plugin/server/embed.ts:39-49` |
