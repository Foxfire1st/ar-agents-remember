# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_events.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Register the parent-wake event handlers, read the host facts they need, and sink every decision row to the plugin's own log — separately from host-activity publication.

## Code Commentary

One tracker receives turn starts, permission waits/resolutions and archive notifications. Turn-end handling reads the role records, takes the event's own `agent.parentAgentId` field as the agent's parent, and passes the host agent identity, provider, parent identity and the event's timeline to the tracker, which decides whether the end is silent and what it owes. The host state the decision reads comes from `readHostState`: it walks `agents.list` page by page, marking completion only when a page reports no further pages, and yields the seat's own state and its children — agents whose `paseo.parent-agent-id` label names the seat — only from an exhausted listing; a missing or repeated continuation cursor, or an eight-page cap, returns no authoritative facts, so the decision leaves the seat alone and writes its reason instead of waking on an incomplete view.

The adapter owns the log sink: `createTurnEndLog` from `turn_log.ts` is created from `PASEO_HOME` and every decision row the current generation emits — sent message, marked line, cancelled wait, skipped send, left-alone end — is offered to it. The registration returns its cleanup, which clears the tracker's pending waits and silent-end runs so a stopped plugin has nothing left to fire and a reload starts afresh. A permission resolution passes the current role records so a held line re-resolves a departed parent; the once-only missing-agent log line is printed here; asynchronous handler failures are caught and logged. These handlers own wake wiring, not host-activity snapshot publication, task-stage classification or a new session store.


**L184 — INV-1ZKP4R.** Event handling is where the cost bound is kept, so the skip belongs here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence


- Native host handlers and explicit steering sends. [1]
