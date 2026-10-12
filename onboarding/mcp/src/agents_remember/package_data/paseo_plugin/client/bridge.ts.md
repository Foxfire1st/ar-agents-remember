# mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The web bridge authorizes dashboard control and owns native navigation, current SDK selection intersection and Parent checks.

## Code Commentary

Exact paired origins and the actual parent window bound incoming control. Native opens refresh the agent handle and refuse missing/archived agents; Parent additionally rechecks the live lifetime, visible source and current relation after await. Plural DOM candidates are intersected with current SDK IDs, and teardown releases owned SDK/DOM resources.

Ready and pong advertise plugin abilities; trusted ar.hello states which newer replies the dashboard can consume. Pending display separates being on the selected native screen (exact route, stored focus and no contradicting visible tab) from the visible conversation. For ordinary opens a capable dashboard receives on-chat once before drawing, load-failed when the application's own failure pane is visible, or shown once its conversation is drawn. Load-failed ends observation without inventing dashboard failure text. Superseded generations, teardown and stale Parent relations publish no late answer. A newer dashboard's late open is not discarded merely at its old local deadline.
## Invariants And Boundaries

Browser framing/messages/referrers and native not-found text are pinned unsupported assumptions. Shown acknowledgement, canonical AR scope and native selected set are different authorities.

The unsupported display read is bound to Paseo 0.11.1's `index-32cec38dd4de4493a1d5392537c1e464.js`: exact route segments, the `workspace-layout-state` store and its server/workspace key, the focused `agent_<id>` tab and visible-selection consistency must agree before any selected-screen report. `shown` additionally needs a visible conversation without loading/not-found; capability-gated `load-failed` instead needs the native `agent-load-error` pane, whose marker is pinned on both 0.11.1 and 0.11.0-beta.2. The chat was seen in the dashboard's frame on that release; this is not a recorded assertion of the dashboard's same-receiving-frame acknowledgement, deadline, error or fallback path. A future pin move requires another source read and its own runtime qualification, not an inference from the manifest's minimum range.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The embed list must pair the parent's origin with this page's serving origin. [1]
- Inbound commands require the exact listed parent's origin and window. [2]
- The bridge owns current open generations, selection intersection, display confirmation and teardown. [3]
- Exact selected-screen identity precedes capability-gated on-chat; native failure settles as load-failed, while visible chat settles as shown. [4]
- Unloaded, unknown and hidden DOM IDs are not published; plural visible IDs are intersected after load and recomputed on SDK removals, reconnect snapshots and teardown. [5]
- Deferred lookup is ignored after tab/relation changes; a still-visible split-pane caller can open its current parent, and missing/archived parents or root transitions do not replace the child. [6]

## MIK-R95 Generation Guard And Page Mode

The bridge keeps one open generation: every agent/workspace open and an invalid `ar.open` advance it, and an awaited read, acknowledgement or error that belongs to a superseded generation is suppressed after the await, so only the latest current open may navigate or emit its result (`ar.ping` only answers pong, and teardown sets the separate `live` guard without changing the generation). It also handles the trusted `ar.page` message: document mode installs the document sidebar isolation, Chats mode removes it, and a fresh page recovers the mode from `arPage=document`. The existing Parent source guard is unchanged.
