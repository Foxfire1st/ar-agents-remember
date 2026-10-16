# mcp/src/agents_remember/observer/host_activity.py

[governing overview](overview.md)

## Purpose

Define the shared validated host publication and default-unknown retained activity facts.

## Commentary

Strict frozen models admit in-turn/permission/idle/ended and reject naive eventAt. Publication requires bootId, complete, agents and nonnegative ignoredEvents. OSError/validation failure returns None, not a complete empty host. Frozen task facts bind qualified keys; HostActivitySnapshot defaults unknown. These are activity facts, not stage authority.

## Evidence

- Define the shared validated host publication and default-unknown retained activity facts. [1]
