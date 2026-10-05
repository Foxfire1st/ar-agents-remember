# mcp/src/agents_remember/package_data/paseo_plugin/client/selection.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The pinned web DOM adapter emits the plural candidate set of visible selected native actor tabs.

## Code Commentary

workspace-tab-agent_<id> plus aria-selected, positive bounds and checkVisibility determine candidates. IDs are sorted/deduplicated, DOM/resize updates publish only changed sets and teardown releases observation. The bridge intersects them with current SDK IDs before public use.

## Invariants And Boundaries

This is one explicitly unsupported pinned DOM dependency; hidden caches, focus, color and URL cannot establish native selection.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `watchSelectedChats` | `mcp/src/agents_remember/package_data/paseo_plugin/client/selection.ts:12-41` |
| Current source owner or exact assertion described above. | `checkVisibility` | `mcp/src/agents_remember/package_data/paseo_plugin/client/selection.ts:18-41` |
| Unloaded, unknown and hidden DOM IDs are not published; plural visible IDs are intersected after load and recomputed on SDK removals, reconnect snapshots and teardown. | `validates visible selections against current SDK IDs, recovering after catalog load and clearing removed or reconnected IDs` | `dashboard/src/cockpit/paseoHierarchy.test.ts:244-274` |
