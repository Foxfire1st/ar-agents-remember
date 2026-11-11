# mcp/src/agents_remember/observer/host_activity.py

[governing overview](overview.md)

## Purpose

Define the shared validated host publication and default-unknown retained activity facts.

## Commentary

Strict frozen models admit in-turn/permission/idle/ended and reject naive eventAt; an agent in a permission state also carries `permissionPrompts`, the sorted ids of the native prompts still unanswered — never their arguments, and the key absent when none remains. A seat that ended its turn with a declared wait also carries `declaredWait`, absent when none is open: `waitsFor` (`subagent` and/or `background`, at least one), a timezone-aware `since`, an optional timezone-aware `checkDueAt` (the plugin's next check, while one is armed) and an optional `detail` of at most 300 characters, with every other key refused; the wait never moves `state` or `eventAt`, which stay the host's. `WaitingSeat` is that wait together with the seat's `agentId` and `role`, as the projection serves it. Publication requires bootId, complete, agents and nonnegative ignoredEvents. OSError/validation failure returns None, not a complete empty host. Frozen task facts bind qualified keys; HostActivitySnapshot defaults unknown. These are activity facts, not stage authority.

## Evidence


- Define the shared validated host publication and default-unknown retained activity facts. [1]


**INV-VDWN33.** This reader is where the publication becomes a snapshot, so the completeness rule is realized here.
