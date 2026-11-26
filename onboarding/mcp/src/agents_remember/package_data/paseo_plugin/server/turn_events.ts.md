# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_events.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Register the parent-wake event handlers, read the host facts they need, and sink every decision row to the plugin's own log — separately from host-activity publication.

## Code Commentary

The event feed takes three **optional** injections from its caller: a row writer (`log`, defaulting to this module's own `turn_log.ts` writer, so a caller holding one does not open a second), the host's ACP verdict for a provider id (`acpProvider`, which the feed never asks when it is absent), and a `declaredWait` callback that receives a seat's open declared wait whenever it changes, for the host-activity record. The tracker's `readProviderLimits` signal is the same generation-cached document reader, used by the pending-only early-clear check; that check starts and stops with pending resume or flush work, not with an event.

The handlers are registered through `server.addHook` with the pinned Paseo 0.16.2 hook names (`agent.turn.before`, `agent.turn.after`, `agent.permission.before`, `agent.permission.after`, `agent.archive.after` and `agent.close.after`). One tracker receives turn starts, permission waits and resolutions, and separate archive and close notifications. The pinned SDK's turn-end event type contains no timeline. The host's compatibility wire payload includes an empty timeline. `readTurnTimeline` reads the agent's whole held timeline through `agents.ref(id).timeline.refetch` (tail, `limit: 0`) and puts each entry's turn id back on its row; a read that fails gives `null`, which the decision reads as an unreadable turn. Turn-end handling reads the role records, takes the event's own `agent.parentAgentId` field as the agent's parent, and passes the host agent identity, provider, parent identity and that timeline to the tracker, which decides whether the end is silent and what it owes. `readHostState` includes archived and background agents on each listing page. It treats a page as terminal when `pageInfo?.hasMore !== true`, including when the pagination metadata is absent. While `hasMore` is true, a missing or repeated continuation cursor leaves the read incomplete. Reaching a bound before a terminal page or failing to read also leaves the host facts unavailable. A complete read supplies the seat's state and identifies its children through `paseo.parent-agent-id`. An incomplete read leaves the seat alone and records the reason.

The adapter owns the log sink: `createTurnEndLog` from `turn_log.ts` is created from `PASEO_HOME` and every decision row the current generation emits — sent message, marked line, cancelled wait, skipped send, left-alone end — is offered to it. The registration returns its cleanup, which clears the tracker's pending waits and silent-end runs so a stopped plugin has nothing left to fire and a reload starts afresh. A permission resolution passes the current role records so a held line re-resolves a departed parent; the once-only missing-agent log line is printed here; asynchronous handler failures are caught and logged. These handlers own wake wiring, not host-activity snapshot publication, task-stage classification or a new session store.


## Evidence



- Native host handlers register through addHook, read the ended turn through refetch and request explicit steering on sends admitted by the decision. [1]


- In the 0.16.2 distribution, `plugins/runtime.js` applies `wireEvent` at 375 and adds the empty compatibility timeline at 1152–1155. `plugins/plugin-process.js:535` passes the input to the hook. [2]
- The 0.16.2 SDK declares the turn-end event at `dist/server/lifecycle.d.ts:107–117` without timeline history. [3]


- The host state walk accepts a terminal page when hasMore is absent or false and requires an unused cursor while hasMore is true. Only a complete read supplies state facts. [4]
