# mcp/src/agents_remember/package_data/paseo_plugin/server/host_activity.test.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Pin host-activity publication semantics with controlled snapshots, events and filesystem fixtures.

## Code Commentary

A fixed-clock role-record harness distinguishes incomplete boot/unload, cold idle without invented age, individual permission requests through turn end, archive/close/create transitions and event-wins pagination. Definitions cover failed/repeated-cursor reconciliation, pruning removed role records, registration of seven hook names, one replacement file without transition history and active-turn timestamp preservation through permission/reconciliation, and the prompt-id publication: two requests publish two sorted ids, resolving one leaves exactly the other, a repeated request for one id stays one occurrence, archiving the agent drops the ids, an agent with none publishes no `permissionPrompts` key, and more than 32 outstanding prompts publish the first 32 sorted ids while marking the snapshot incomplete. The cap case first publishes z completely, then omits it from the capped list while denying completeness. A native answer restores a complete 32-ID list including z; a later complete reconciliation without z removes it. The registration case checks the registered names, not every SDK callback payload. These are controlled assertion definitions, not a live-host, continuous-idle-process or deployment witness.

## Evidence

- Boot and permission/terminal transitions. [1]
- Pagination, failed listing, population bounds and hook names. [2]
- One file and turn-start age through permission/reconciliation. [3]


- Controlled publisher assertions pin exact sibling IDs before archive and cap-induced incompleteness, followed by complete reconciliation and native removal; this file does not exercise Python retained inputs or a live host population. [4]
