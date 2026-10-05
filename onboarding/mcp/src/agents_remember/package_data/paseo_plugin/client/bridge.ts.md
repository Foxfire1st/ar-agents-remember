# mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The web bridge authorizes dashboard control and owns native navigation, current SDK selection intersection and Parent checks.

## Code Commentary

Exact paired origins and parent window bound incoming control. The bridge intersects plural visible DOM candidates with current SDK actor IDs and republishes on either change. Native opens refresh handles and refuse missing/archived actors. Parent additionally rechecks live lifetime, visible source and current relation after await. Teardown stops SDK and DOM resources.

## Invariants And Boundaries

Browser framing/messages/referrers and native not-found text are pinned unsupported assumptions. Shown acknowledgement, canonical AR scope and native selected set are different authorities.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `isListedParent` | `mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts:79-88` |
| Current source owner or exact assertion described above. | `isParentMessage` | `mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts:91-97` |
| Current source owner or exact assertion described above. | `installBridge` | `mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts:104-206` |
| Unloaded, unknown and hidden DOM IDs are not published; plural visible IDs are intersected after load and recomputed on SDK removals, reconnect snapshots and teardown. | `validates visible selections against current SDK IDs, recovering after catalog load and clearing removed or reconnected IDs` | `dashboard/src/cockpit/paseoHierarchy.test.ts:244-274` |
| Deferred lookup is ignored after tab/relation changes; a still-visible split-pane caller can open its current parent, and missing/archived parents or root transitions do not replace the child. | `checks current visible caller and parent relation, including deferred navigation, unavailable parents and root transitions` | `dashboard/src/cockpit/paseoHierarchy.test.ts:134-164` |
