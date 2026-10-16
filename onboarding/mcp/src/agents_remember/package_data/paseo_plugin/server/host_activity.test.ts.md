# mcp/src/agents_remember/package_data/paseo_plugin/server/host_activity.test.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Pin host-activity publication semantics with controlled snapshots, events and filesystem fixtures.

## Code Commentary

A fixed-clock role-record harness distinguishes incomplete boot/unload, cold idle without invented age, individual permission requests through turn end, archive/close/create transitions and event-wins pagination. Definitions cover failed/repeated-cursor reconciliation, pruning removed role records, registration of seven hook names, one replacement file without transition history and active-turn timestamp preservation through permission/reconciliation. The registration case checks the registered names, not every SDK callback payload. These are controlled assertion definitions, not a live-host, continuous-idle-process or deployment witness.

## Evidence

- Boot and permission/terminal transitions. [1]
- Pagination, failed listing, population bounds and hook names. [2]
- One file and turn-start age through permission/reconciliation. [3]
