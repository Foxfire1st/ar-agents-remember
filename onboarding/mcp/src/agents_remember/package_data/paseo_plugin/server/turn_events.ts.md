# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_events.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Register the parent-wake event handlers, read the host facts they need, and sink every decision row to the plugin's own log — separately from host-activity publication.

## Code Commentary

The event feed takes three **optional** injections from its caller: a row writer (`log`, defaulting to this module's own `turn_log.ts` writer, so a caller holding one does not open a second), the host's ACP verdict for a provider id (`acpProvider`, which the feed never asks when it is absent), and a `declaredWait` callback that receives a seat's open declared wait whenever it changes, for the host-activity record.

The handlers are registered through `server.addHook` under Paseo 0.15's hook names (`agent.turn.before`, `agent.turn.after`, `agent.permission.before`, `agent.permission.after`, `agent.archive.after` and `agent.close.after`, a close being treated as an archive). One tracker receives turn starts, permission waits/resolutions and archive notifications. Because the turn-end hook carries an empty timeline from Paseo 0.13, `readTurnTimeline` reads the agent's whole held timeline through `agents.ref(id).timeline.refetch` (tail, `limit: 0`) and puts each entry's turn id back on its row; a read that fails gives `null`, which the decision reads as an unreadable turn, and the hook's own list is never a fallback. Turn-end handling reads the role records, takes the event's own `agent.parentAgentId` field as the agent's parent, and passes the host agent identity, provider, parent identity and that timeline to the tracker, which decides whether the end is silent and what it owes. The host state the decision reads comes from `readHostState`: it walks `agents.list` page by page, marking completion only when a page reports no further pages, and yields the seat's own state and its children — agents whose `paseo.parent-agent-id` label names the seat — only from an exhausted listing; a missing or repeated continuation cursor, or an eight-page cap, returns no authoritative facts, so the decision leaves the seat alone and writes its reason instead of waking on an incomplete view.

The adapter owns the log sink: `createTurnEndLog` from `turn_log.ts` is created from `PASEO_HOME` and every decision row the current generation emits — sent message, marked line, cancelled wait, skipped send, left-alone end — is offered to it. The registration returns its cleanup, which clears the tracker's pending waits and silent-end runs so a stopped plugin has nothing left to fire and a reload starts afresh. A permission resolution passes the current role records so a held line re-resolves a departed parent; the once-only missing-agent log line is printed here; asynchronous handler failures are caught and logged. These handlers own wake wiring, not host-activity snapshot publication, task-stage classification or a new session store.


## Evidence


- Native host handlers and explicit steering sends. [1]
