# mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The web bridge authorizes dashboard control and owns native navigation, current SDK selection intersection and Parent checks.

## Code Commentary

Exact paired origins and parent window bound incoming control. The bridge intersects plural visible DOM candidates with current SDK actor IDs and republishes on either change. Native opens refresh handles and refuse missing/archived actors. Parent additionally rechecks live lifetime, visible source and current relation after await. Teardown stops SDK and DOM resources.

## Invariants And Boundaries

Browser framing/messages/referrers and native not-found text are pinned unsupported assumptions. Shown acknowledgement, canonical AR scope and native selected set are different authorities.

The unsupported display read is bound to Paseo 0.11.1's `index-32cec38dd4de4493a1d5392537c1e464.js`: exact route segments, the `workspace-layout-state` store and its server/workspace key, the focused `agent_<id>` tab and visible chat signs must agree before `shown` is posted. The chat was seen in the dashboard's frame on that release; this is not a recorded assertion of the dashboard's same-receiving-frame acknowledgement, deadline, error or fallback path. A future pin move requires another source read and its own runtime qualification, not an inference from the manifest's minimum range.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The embed list must pair the parent's origin with this page's serving origin. [1]
- Inbound commands require the exact listed parent's origin and window. [2]
- The bridge owns current open generations, selection intersection, display confirmation and teardown. [3]
- The pinned display gate checks route, stored tab identity and visible chat before acknowledging; its dated native observations and qualification limits are separate from that executable predicate. [4]
- Unloaded, unknown and hidden DOM IDs are not published; plural visible IDs are intersected after load and recomputed on SDK removals, reconnect snapshots and teardown. [5]
- Deferred lookup is ignored after tab/relation changes; a still-visible split-pane caller can open its current parent, and missing/archived parents or root transitions do not replace the child. [6]

## MIK-R95 Generation Guard And Page Mode

The bridge keeps one open generation: every agent/workspace open and an invalid `ar.open` advance it, and an awaited read, acknowledgement or error that belongs to a superseded generation is suppressed after the await, so only the latest current open may navigate or emit its result (`ar.ping` only answers pong, and teardown sets the separate `live` guard without changing the generation). It also handles the trusted `ar.page` message: document mode installs the document sidebar isolation, Chats mode removes it, and a fresh page recovers the mode from `arPage=document`. The existing Parent source guard is unchanged.
