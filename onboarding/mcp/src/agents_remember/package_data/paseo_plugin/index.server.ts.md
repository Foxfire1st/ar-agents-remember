# mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts

## Governing Overview

[Plugin overview](overview.md)

## Purpose

The canonical server entry exposes the provisioned embed list, composes host-activity publication and registers parent-wake notifications as distinct event-driven owners.

## Code Commentary

contribute reads the list once at load, logs the entry count and registers ar.embed-list with that value. Provisioning/reload owns refresh, while malformed present data fails visibly.

A host-activity publisher is created from PASEO_HOME, registers its own event handlers, and supplies the explicit ar.host-activity-snapshot RPC: a full reconciliation returns the publisher boot identity. Initialization and unload-publication failures are logged; an unavailable publisher makes the RPC fail visibly. Unload marks publication incomplete. registerParentWakeEvents separately owns its tracker, host-state reads, log sink and steer sends, and returns the cleanup that stops every pending seat wait when the plugin unloads, preserving turn/permission gates without conflating wake behavior with task-state publication. Embed data remains load-time data; neither owner starts a poll.


**L184 — INV-VDWN33.** This is the plugin's one handler for both calls, so the number crosses the boundary here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Invariants And Boundaries

The server does not infer parent trust, poll another registry or gain dashboard helper gate coverage.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The server entry reads the embed list at load and registers the existing embed RPC. [1]

- The entry composes independent activity publication/RPC and parent-wake registration, with explicit initialization and unload failure handling. [2]
