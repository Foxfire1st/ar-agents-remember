# mcp/src/agents_remember/package_data/paseo_plugin/server/host_activity.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Publish one replaceable host-activity snapshot for the product role-agent population.

## Code Commentary

A publisher has a boot identity and remains incomplete until every host-list page succeeds; unload marks it incomplete again. It retains role-registered agents only and counts ignored unbound events with saturation. Turn, permission and ended facts are distinct: permission wins while requests remain, even after turn end; archive/close clears permission/turn state. A permission-state agent also publishes `permissionPrompts` — the sorted ids of its unanswered native prompts, capped at `PERMISSION_PROMPTS_LIMIT = 32` and omitted when none remain — without carrying a prompt's arguments. More than 32 outstanding native IDs for one agent makes the whole snapshot incomplete; the first 32 serialized IDs do not prove an omitted prompt answered. Reconciliation rejects missing/repeated continuation cursors and preserves events newer than the listing start. A matching same-boot snapshot can retain a known event timestamp; cold idle listing invents no idle timestamp, and active/permission age uses the turn start. The file writer stages then renames one JSON publication, not transition history or a multiwriter transaction. Activity registrations are separate from parent-wake handlers and catch their own publication errors. No polling, task-stage derivation or elapsed-silence inference is owned here.


**L184 — INV-VDWN33, NEW-RUNNING-SUBAGENT-IS-WORK.** The publication is written here, so both the completeness rule and the subagent facts are realized here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Evidence

- Host event transitions and exact registered-agent admission. [1]
- Full paginated reconciliation and event-wins ordering. [2]
- Bound population, published timestamps and snapshot provenance. [3]
- One replacement file and independent activity handlers. [4]


- Per-agent overflow keeps first-32 sorted serialization but denies whole-publication completeness; omission is not native-resolution evidence. [5]
