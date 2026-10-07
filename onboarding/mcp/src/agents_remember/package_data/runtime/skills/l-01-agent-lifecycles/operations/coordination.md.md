# operations/coordination.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Start and reach native role agents for exact canonical AR assignments while keeping delivery with Paseo and semantic truth with AR.

## Current Contract

The Architect delegates coordination first to one Manager for one master or one Orchestrator for concurrent masters; direct coordination is only the developer’s choice. A bound start supplies the role, required canonical references and request ID, resolves the AR paired enclosure, writes the handover and returns the actual agent/report/artifact identities.

Architect may start every role except Architect; Orchestrator may start Manager, Worker, Reviewer and Curator under its sprint; Manager may start Worker, Reviewer and Curator under its master. Other roles start none. An unknown start is reconciled by the same request ID. A rejected candidate returns finding-specific repair to the same Worker.

`role_message` names one recipient by actual agent ID or unambiguous role/task selection, attributes the sender and never cancels a running turn. Busy, permission, unfinished-start, missing, archived and ambiguous outcomes remain explicit. A wait reports the consumed turn or a pending/timeout/uncertain outcome; it is not semantic completion. Dashboard-started agents need no parent.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/coordination.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Use only `role_start`/`role_message` on `agents-remember-task`. Preserve canonical task and paired paths; do not create an independent Paseo Git worktree, background scheduler, duplicate owner or acceptance ledger. Avoid mutually waiting agents.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| One coordinating agent under the Architect, bound start/messaging, same-request recovery and execution metadata boundary. | lines 3-15 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/coordination.md:3-15 |
