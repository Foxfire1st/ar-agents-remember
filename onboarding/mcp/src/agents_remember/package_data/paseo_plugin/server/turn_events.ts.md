# mcp/src/agents_remember/package_data/paseo_plugin/server/turn_events.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Register parent-wake event handlers separately from host-activity publication.

## Code Commentary

One tracker receives turn starts, permission waits/resolutions and archive notifications. Turn-end handling reads the existing role records and passes the host agent identity, the agent's provider, parent identity, the timeline and the ended turn's own id (which scopes the rows the decision reads) to the tracker, so the decision can tell a parent whose provider is known to steer from one that must be told when its turn ends; a permission resolution passes the current role records so a held line re-resolves a departed parent. It prints the decision's once-only missing-agent log line. Turn-end and permission-resolution asynchronous handlers catch/log failures. These handlers own wake wiring, not host-activity snapshot publication, task-stage classification or a new session store.

## Evidence

- Native host handlers and explicit steering sends. [1]
