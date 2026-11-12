# mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts

## Governing Overview

[Plugin overview](overview.md)

## Purpose

The canonical server entry exposes the provisioned embed list, composes host-activity publication and registers parent-wake notifications as distinct event-driven owners.

## Code Commentary

The boot writes **one** row file and shares it: `createTurnEndLog(home)` is built once, so the turn-end rows and the provider-verdict row land in the same sink rather than two. The ACP verdict is read at this point too — `createAcpProviderSet` over the installation the plugin runs against — and held for the turn-end decision, which uses it only to choose an ACP seat's wake sentence; `PASEO_HOME` is resolved here, so a boot without it is answered at the entry rather than at the first write.

contribute reads the list once at load, logs the entry count and registers ar.embed-list with that value. Provisioning/reload owns refresh, while malformed present data fails visibly.

A host-activity publisher is created from PASEO_HOME, registers its own event handlers, and supplies the explicit ar.host-activity-snapshot RPC: a full reconciliation returns the publisher boot identity. Initialization and unload-publication failures are logged; an unavailable publisher makes the RPC fail visibly. Unload marks publication incomplete. registerParentWakeEvents separately owns its tracker, host-state reads, log sink and steer sends, and returns the cleanup that stops every pending seat wait when the plugin unloads, preserving turn/permission gates without conflating wake behavior with task-state publication. The parent-wake registration is also handed a `declaredWait` callback that passes each seat's open declared wait to the publisher's `noteDeclaredWait`, catching its own failure, so the host-activity record shows a waiting seat while the host reports it idle. The subagent subscription is taken at the first of the host-activity hooks (`ATTACH_HOOKS` is derived from `HOST_ACTIVITY_HOOKS`), each registered through `server.addHook`. Embed data remains load-time data; neither owner starts a poll.


## Invariants And Boundaries

The server does not infer parent trust, poll another registry or gain dashboard helper gate coverage.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The server entry reads the embed list at load and registers the existing embed RPC. [1]

- The entry composes independent activity publication/RPC and parent-wake registration, with explicit initialization and unload failure handling.
