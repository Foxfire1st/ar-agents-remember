# mcp/src/agents_remember/package_data/paseo_plugin/index.server.ts

## Governing Overview

[Plugin overview](overview.md)

## Purpose

The canonical server entry exposes the provisioned embed list and wires native role-agent lifecycle events into product-owned silent-turn notifications.

## Code Commentary

contribute reads the list once at load, logs the entry count and registers ar.embed-list with that value. Provisioning/reload owns refresh, while malformed present data fails visibly.

The same plugin instance owns a shared turn tracker. Turn-start, turn-end, permission-request/resolution and archive events update it; turn-end reads published role/task/report facts fresh and delegates the pure decision to `server/turn_ended.ts`, sending through the supplied host client. Asynchronous turn-end and permission-resolution errors are caught and logged. Embed data remains load-time data; role facts are event-time data. Neither path polls the host.

## Invariants And Boundaries

The server does not infer parent trust, poll another registry or gain dashboard helper gate coverage.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The server entry reads the embed list at load and registers the existing embed RPC. [1]
- Native turn, permission and archive callbacks share one tracker; turn-end reads facts fresh and asynchronous callback errors are caught. [2]
