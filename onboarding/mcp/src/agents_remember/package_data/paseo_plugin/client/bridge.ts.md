# mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Authorize dashboard control, navigate the native application, confirm its display and connect native text picks and shown-chat reports.

## Code Commentary

The embed list must pair the dashboard origin with this page's serving origin; incoming messages must also come from the actual parent window. Native opens refresh the agent handle and refuse missing or archived agents. Parent navigation rechecks the live lifetime, visible source and current SDK relation after the agent refresh. Plural DOM selection candidates are intersected with current SDK IDs before publication. [1] [2] [3]

Ready and every pong advertise the plugin's abilities. Trusted `ar.hello` declares which newer replies the dashboard can read. A pending open distinguishes being on the named native screen from its conversation being visibly drawn: exact route segments, the stored focused tab and no contradictory visible selected tab establish the former. A dashboard that advertises the capability receives `on-chat` once when the named native screen is selected. A visible native failure pane settles the request with `load-failed` when negotiated. A drawn conversation settles it with `shown`. Superseded opens, stopped lifetimes and stale Parent relations publish no late answer. While the current open is pending, the bridge checks it on a timer and on DOM changes. [3] [4]

The tray channel starts inside this same trusted lifetime and stays silent until the dashboard advertises `pick`. Trusted `ar.tray` and `ar.tray-space` configure native offers and reserve space; `client/pick.ts` owns their text/provenance and composer observations. A drawn-chat acknowledgement informs that owner that a composer should now be readable.

For a text pick's chat provenance, one visible selected agent names the source. With no visible strip the bridge reads the routed workspace's stored focused pane; with plural visible agents it accepts that focused agent only if it is a member. An unidentifiable source remains unknown. The negotiated `showing` report uses this same identity and reports `null` for no identifiable agent or an agent's not-found/load-error pane. It reports immediately at hello and on changed observations, with DOM batches coalesced into one read per 250 ms window. This report never navigates the application or changes the published compact selected set.

Every agent/workspace open, including invalid `ar.open`, advances the open generation. Ping answers only pong, and teardown uses the separate live guard. Trusted `ar.page` toggles document sidebar isolation; a fresh `arPage=document` URL restores that mode. Teardown releases hierarchy/selection/DOM observation, timers, tray handlers and document isolation. [3]

## Invariants And Boundaries

Browser framing/messages/referrers and the native missing-agent error text are unsupported assumptions. Display confirmation reads the pinned Paseo 0.16.2 web build `index-3d51f4c450eeff5bd838a646e9c611f2.js` route, exact `workspace-layout-state` key and pane focus, `agent_<id>` tab, selected-tab markers and chat display markers. The native address syntax includes `?open=agent:<id>`. `shown` requires a visible conversation. The native `agent-load-error` marker can settle the request through the negotiated `load-failed` reply. Unknown or contradictory display state supplies no confirmation. [4]

Native navigation receives the agent alone; the application resolves its workspace from its own session. Dashboard document scope, native plural selection, requested-agent confirmation and the tray's actually shown-chat identity remain distinct authorities. The shown-chat and pick paths read native presentation but do not write its tab store. The route and marker descriptions characterize the pinned source. Navigation by control message depends on the trusted frame completing its readiness handshake. A release changing those native structures requires revisiting the pinned assumptions; a manifest minimum range does not establish them.


## Evidence

- The embed list pairs both origins. [1]
- Inbound commands require that origin and the actual parent window. [2]
- Native screen identity precedes on-chat; visible conversation or the native failure pane settles the request. [4]
- Selection assertions cover unloaded, unknown, hidden, removed and reconnected SDK/DOM IDs. [5]
- Parent assertions cover deferred lookups, changed visible callers/relations and unavailable parents. [6]
- Pick provenance reads the focused agent consistently across native layouts and plural visible selections. [8]
- Shown-chat reporting is negotiated, nullable, change-only and coalesced across DOM batches. [9]

- Open generations, SDK selection intersection, Parent checks, page mode and teardown share one bridge lifetime. [3]
- Tray control is negotiated within the trusted bridge lifetime. [7]
- The pinned web build documents the exact route, agent intent, store key, focus and tab ID. [10]
