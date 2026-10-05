# dashboard/src/cockpit/paseoPluginClient.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The helper suite protects web page lifetime, exact framing trust, checked navigation and appearance/write provenance.

## Code Commentary

Cases bound reloads, retain first-visit deep links and perform one startup native-sidebar collapse that yields to early menu clicks. Fresh trust waits for exact pair confirmation; window/origin lookalikes fail. Same-page verified trust is rechecked for explicit revocation, and stopped async completion does nothing. Shared-storage cases distinguish running-look writers.

## Invariants And Boundaries

The old initial-open sidebar claim is superseded. Plain-page/SDK fixtures do not establish live native framing or actor operations.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `one reload per page load` | `dashboard/src/cockpit/paseoPluginClient.test.ts:63-93` |
| Current source owner or exact assertion described above. | `who frames the page` | `dashboard/src/cockpit/paseoPluginClient.test.ts:227-257` |
| Current source owner or exact assertion described above. | `starting the client part` | `dashboard/src/cockpit/paseoPluginClient.test.ts:735-765` |
| Saves standalone look/sidebar values before storing the AR appearance, and keeps earlier saved values when the last recorded writer was a frame. | `applyEmbedLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:158-182` |
| Waits for an exact embed-list match before trusting a new parent and drops a previously trusted bridge when the refreshed list excludes it. | `startClientPart` | `mcp/src/agents_remember/package_data/paseo_plugin/client/start.ts:26-88` |
