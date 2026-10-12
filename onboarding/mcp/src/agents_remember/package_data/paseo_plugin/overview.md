# Native Paseo plugin

## Governing Overview

[MCP repository overview](../../../../overview.md)

## Purpose

The product-owned plugin bridges provisioned embed data and role-agent lifecycle events into the native host. It neither edits the host's implementation nor asks it at intervals.

## Hot Path Summary

`index.server.ts` exposes the embed RPC and wires host turn/permission/archive events into a shared tracker. `server/role_agents.ts` reads published role/task/report facts on each turn end; `server/turn_ended.ts` decides suppression, holding, claim invalidation and sending through the supplied host client.

## Structure And Boundaries

The client bridge steers the one native frame through exact parent-window/origin admission and an agent-only open. Ready and pong advertise abilities; hello gates newer navigated/on-chat/load-failed replies. Selected-screen identity releases input, drawing completes the dashboard wait, and the application own failed-load pane ends it without invented dashboard failure prose. This does not add another frame, host polling, server lifecycle writer or semantic task acceptance. An older plugin stays message-capable where it supports open and its earlier-answer limitation is disclosed by the dashboard.



The provisioned embed list is read at plugin load, retaining visible malformed-data failure. Role facts have a different lifetime: role start publishes them and the turn-end handler reads them fresh. Pure decision tests establish selected event schedules without proving live-host installation or event delivery. Asynchronous turn-end/permission handlers catch and log failures instead of throwing into the host loop. Missing role facts yield no line; they are not reconstructed from source or titles.

A line carries no agent final text. Parent permission waits and running turns defer notification; child activity holds it, while descendant restarts drop the older owed line, including an already claimed deferred one. The tracker is process-local and the source cap is distinct from the settings-reloaded role_message limit.

## Load-Bearing Files

- `index.server.ts`: existing embed RPC and lifecycle event wiring.
- `server/role_agents.ts`: typed per-agent fact reader.
- `server/turn_ended.ts`: stateful pure notification decision.
- `server/turn_ended.test.ts`: host-free schedules and preservation controls.



## Evidence

- The client bridge negotiates display replies while keeping native navigation, selected-screen admission and drawing/failure distinct. [3]
- Keep embed RPC while wiring turn, permission and archive events to product-owned decisions; asynchronous handler failures are logged. [1]
- Read fresh role/task/report facts for notifications without polling or source inference. [2]
