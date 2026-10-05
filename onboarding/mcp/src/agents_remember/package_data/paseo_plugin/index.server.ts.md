# mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The canonical server entry exposes the provisioned embed list through one typed native plugin RPC.

## Code Commentary

contribute reads the list once at load, logs the entry count and registers ar.embed-list with that value. Provisioning/reload owns refresh, while malformed present data fails visibly.

## Invariants And Boundaries

The server does not infer parent trust, poll another registry or gain dashboard helper gate coverage.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `contribute` | `mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts:9-14` |
| Current source owner or exact assertion described above. | `server.handle` | `mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts:12-14` |
