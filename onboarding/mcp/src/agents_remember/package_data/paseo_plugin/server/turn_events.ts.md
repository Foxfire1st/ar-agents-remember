# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_events.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Register parent-wake event handlers separately from host-activity publication.

## Code Commentary

One tracker receives turn starts, permission waits/resolutions and archive notifications. Turn-end handling reads the existing role records and passes the host agent identity, parent identity and timeline to the tracker; parent sends explicitly steer an active turn. Turn-end and permission-resolution asynchronous handlers catch/log failures. These handlers own wake wiring, not host-activity snapshot publication, task-stage classification or a new session store.

## Evidence

- Native host handlers and explicit steering sends. [1]
