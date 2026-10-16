# mcp/src/agents_remember/package_data/paseo_plugin/server/host_activity.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Publish one replaceable host-activity snapshot for the product role-agent population.

## Code Commentary

A publisher has a boot identity and remains incomplete until every host-list page succeeds; unload marks it incomplete again. It retains role-registered agents only and counts ignored unbound events with saturation. Turn, permission and ended facts are distinct: permission wins while requests remain, even after turn end; archive/close clears permission/turn state. Reconciliation rejects missing/repeated continuation cursors and preserves events newer than the listing start. A matching same-boot snapshot can retain a known event timestamp; cold idle listing invents no idle timestamp, and active/permission age uses the turn start. The file writer stages then renames one JSON publication, not transition history or a multiwriter transaction. Activity registrations are separate from parent-wake handlers and catch their own publication errors. No polling, task-stage derivation or elapsed-silence inference is owned here.

## Evidence

- Host event transitions and exact registered-agent admission. [1]
- Full paginated reconciliation and event-wins ordering. [2]
- Bound population, published timestamps and snapshot provenance. [3]
- One replacement file and independent activity handlers. [4]
