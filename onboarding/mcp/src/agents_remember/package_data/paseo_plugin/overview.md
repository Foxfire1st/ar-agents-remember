# Native Paseo plugin

## Governing Overview

[MCP repository overview](../../../../overview.md)

## Purpose

The product-owned plugin bridges provisioned embed data and role-agent lifecycle events into the native host. It neither edits the host's implementation nor asks it at intervals.

## Hot Path Summary

`index.server.ts` retains the embed RPC, contributes the host-activity snapshot RPC and installs two separate event owners. `server/host_activity.ts` publishes recorded agents' activity; `server/turn_events.ts` wires parent wakes through the shared tracker in `server/turn_ended.ts`. `server/role_agents.ts` supplies published role/task/report facts through one replaceable stat-generation cache, not a fresh JSON parse on each event.

## Structure And Boundaries

The client bridge steers the one native frame through exact parent-window/origin admission and an agent-only open. Ready and pong advertise abilities; hello gates newer navigated/on-chat/load-failed replies. Selected-screen identity releases input, drawing completes the dashboard wait, and the application own failed-load pane ends it without invented dashboard failure prose. This does not add another frame, host polling, server lifecycle writer or semantic task acceptance. An older plugin stays message-capable where it supports open and its earlier-answer limitation is disclosed by the dashboard.



The provisioned embed list is read at plugin load, retaining visible malformed-data failure. Role facts have a different lifetime: role start publishes them, and readers stat their path and reuse the parsed value only for the same device/inode/size/mtime/ctime generation. A changed registration replaces that single cached value; absence clears it and returns no records, while malformed content fails visibly. Pure decision tests establish selected event schedules without proving live-host installation or event delivery. Asynchronous turn-end/permission handlers catch and log failures instead of throwing into the host loop. Missing role facts yield no line; they are not reconstructed from source or titles.

Host activity is a separate replaceable publication, bounded by the existing role-agent records. It starts incomplete, becomes usable only after a complete paginated host reconciliation, and returns to incomplete on unload. Events arriving during the whole read win over its older snapshot. Permission waits remain activity, and an idle snapshot invents no event timestamp. The snapshot RPC returns the plugin boot identity after reconciliation; the dashboard input qualifies that boot at its startup and on a newly observed plugin boot, not by periodic status polling. Parent-wake sends separately retain their turn/permission gates: a line goes to a parent that is mid-turn only where the product knows that provider keeps its turn under a steer, and otherwise waits for the turn to end.

A line carries the ended turn's own last line of agent text, shortened to 300 characters, and no document; a turn with no text says so, and a refused return still gives the line. A parent awaiting permission holds the line, and so does one that is in a turn unless the product knows its provider keeps that turn under a steer — the build names no such provider, so in practice a running parent is told when its turn ends, never steered into it and never replaced; the same gate is asked again before each send, so a batch cannot steer into a turn it has just started. Child activity holds the line, while descendant restarts drop the older owed one, including an already claimed deferred one. Each line is sent once, in the order the turns ended, across requeues and a Manager rebind. A leaf agent whose recorded parent is archived or missing gives its line to the current Manager of its master, and an agent outside the product's list is named once in the host log. The tracker is process-local and the source cap is distinct from the settings-reloaded role_message limit.

## Load-Bearing Files

- `index.server.ts`: embed and host-activity RPCs, independent event owners and unload publication.
- `server/host_activity.ts`: bound, boot-qualified host activity and atomic publication.
- `server/role_agents.ts`: typed, stat-generation-cached per-agent fact reader.
- `server/turn_events.ts`: contributed parent-wake handlers and steering sends.
- `server/turn_ended.ts`: stateful pure notification decision.
- `server/turn_ended.test.ts`: host-free schedules and preservation controls.



## Evidence

- The client bridge negotiates display replies while keeping native navigation, selected-screen admission and drawing/failure distinct. [3]
- Keep embed RPC while wiring turn, permission and archive events to product-owned decisions; asynchronous handler failures are logged. [1]
- Read current role/task/report registrations through one replaceable stat-generation cache; absence clears it and malformed content remains visible. [2]
- Host activity is boot-qualified, record-bounded and event-driven; concurrent events win over the whole host read and no idle event time is invented. [4]
- Parent-wake handlers retain the existing gates: any admitted send asks the host for a steer, a free parent takes the line at once, and only a parent that is already in a turn is withheld unless the product knows its provider keeps that turn. [5]
