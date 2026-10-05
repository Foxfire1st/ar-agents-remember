# mcp/src/agents_remember/package_data/paseo_plugin/shared/rpc.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The shared definition types the canonical ar.embed-list server/client transport.

## Code Commentary

Its empty input returns string dashboardOrigin/frameBaseUrl pairs. The server uses provisioning and the client rechecks its actual framing/serving origin pair.

## Invariants And Boundaries

Schema shape is not origin authorization, independent frame permission or a secret channel.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `arEmbedList` | `mcp/src/agents_remember/package_data/paseo_plugin/shared/rpc.ts:6-12` |
| Current source owner or exact assertion described above. | `ar.embed-list` | `mcp/src/agents_remember/package_data/paseo_plugin/shared/rpc.ts:7-12` |
