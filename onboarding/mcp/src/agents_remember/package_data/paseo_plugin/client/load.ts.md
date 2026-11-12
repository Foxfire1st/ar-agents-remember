# mcp/src/agents_remember/package_data/paseo_plugin/client/load.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The load helper owns one-page bootstrap, bounded replacement and running-look write attribution.

## Code Commentary

A page-global record and consumed session reload flag prevent replacement loops. Embed bootstrap stores appearance and repairs only pinned first-visit bounce paths, then runs the one opening migration for an old stored-closed host sidebar (MIK-R75 rule 8). Standalone restoration distinguishes what the page started running from later shared-store writes before attributing app writes.

## Invariants And Boundaries

Failure to persist the reload guard refuses replacement. Separate later page loads get their own decision; re-evaluation preserves the user's later menu choice. Clock/storage/bounce assumptions are pinned unsupported behavior.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `reloadOnce` | `mcp/src/agents_remember/package_data/paseo_plugin/client/load.ts:81-111` |
| Current source owner or exact assertion described above. | `bootstrapEmbed` | `mcp/src/agents_remember/package_data/paseo_plugin/client/load.ts:112-142` |
| Current source owner or exact assertion described above. | `takeOwnLookBack` | `mcp/src/agents_remember/package_data/paseo_plugin/client/load.ts:126-136` |
| The standalone preference is persisted before the application settings can be overwritten with the embedded appearance. | `never overwrites the user's look before it is kept` | `dashboard/src/cockpit/paseoPluginLook.test.ts:86-116` |

## MIK-R95 Write Transform And Document Load

The load-time write watcher accepts an optional transform: the document page passes `preserveSidebarChoice` so a native panel-state write keeps the actually stored `agentListOpen` choice while the rail's in-memory state closes. `bootstrapEmbed` skips its one-time native-sidebar open on a document page and clears a stale page mode, so a standalone tab and the Chats page keep the user's own look and sidebar.
