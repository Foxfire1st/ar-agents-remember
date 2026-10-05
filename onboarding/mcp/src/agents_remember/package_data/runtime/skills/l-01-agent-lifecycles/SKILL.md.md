# l-01-agent-lifecycles/SKILL.md

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

The packaged thin router selects the native AR role capsule; canonical `skills/l-01-agent-lifecycles/SKILL.md` owns this contract and `scripts/sync-skills.py` produces the copies.

## Current Contract

A capsule contains the explicitly selected `roles/<role>.md` followed by one applicable operation. Canonical task and workspace bindings travel separately in the handover. Shared `core/` blocks are not injected.

The launcher supports Architect, System Specialist, Orchestrator, Manager, Worker, Reviewer and Curator. Missing or unsupported role/operation or conflicting bindings are reported, not inferred. Projects is an execution location, not a repository identity. Manual taskless Architect and System Specialist launches ask only for missing outcome/repository or concern/report scope.

Paseo runs the agents. AR tools come from the launching build’s `agents-remember-task` server; agent starts and peer messages use `role_start` and `role_message` with actual returned identities. Developer decisions stay in the agent’s own chat. Dashboard starts need no parent. Flat distinct-role ownership is valid; prior approvals survive reconnects and compaction.

## Conventions

Canonical skills/l-01-agent-lifecycles/SKILL.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Restore the same role, operation, task, agent IDs and report from the durable handover. Reconcile an uncertain start with the same request ID. A finished turn, review, curation, semantic acceptance and paired Git publication require their separate owning evidence.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Explicit role/operation composition and taskless Projects scope. | lines 8-16 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:8-16 |
| Bound server, actual role identities, flat ownership and recovery/acceptance distinction. | lines 20-35 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:20-35 |
