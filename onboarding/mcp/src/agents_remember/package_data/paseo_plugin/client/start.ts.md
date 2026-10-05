# mcp/src/agents_remember/package_data/paseo_plugin/client/start.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper makes the sole parent/trust decision and selects embedded versus standalone behavior.

## Code Commentary

A fresh parent waits for the exact current embed-list pair. Listed pages bootstrap bridge/look; standalone/unlisted pages restore the user look. Same-page verified trust can be reused while the list is rechecked; explicit removal withdraws the bridge. Unknown parent or unreadable first list establishes no new trust. Watching begins only with known running-look attribution.

## Invariants And Boundaries

Fresh-list failure differs from existing verified-page behavior. Stopped async answers do nothing; other web/storage/navigation work stays with its delegated owners.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `startClientPart` | `mcp/src/agents_remember/package_data/paseo_plugin/client/start.ts:26-88` |
| Current source owner or exact assertion described above. | `load.trustedParent` | `mcp/src/agents_remember/package_data/paseo_plugin/client/start.ts:63-88` |
| Current source owner or exact assertion described above. | `live = false` | `mcp/src/agents_remember/package_data/paseo_plugin/client/start.ts:83-88` |
| A fresh page installs no bridge or write watcher before the exact embed-list pair confirms its parent, then installs a bridge only on the settled page. | `listed frame: the AR look and the channel, once the list has confirmed the parent` | `dashboard/src/cockpit/paseoPluginClient.test.ts:775-805` |
