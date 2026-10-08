# l-01-agent-lifecycles/SKILL.md

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

The packaged thin router selects the native AR role capsule; canonical `skills/l-01-agent-lifecycles/SKILL.md` owns this contract and `scripts/sync-skills.py` produces the copies.

## Current Contract

A capsule contains the explicitly selected `roles/<role>.md` followed by one applicable operation. Canonical task and workspace bindings travel separately in the handover. Shared `core/` blocks are not injected.

The native launcher supports Architect, Investigator, Orchestrator, Manager, Worker, Reviewer and Curator. System Specialist is the earlier read spelling of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created.

Paseo runs the agents. AR tools come from the launching build’s `agents-remember-task` server; agent starts and peer messages use `role_start` and `role_message` with actual returned identities. With a parent named in host.parent, every question requiring the developer's decision goes to that actual parent through bound role_message. Continue independent work; if none remains, record the state and await the parent's message. Busy or permission-prompt delivery stays pending and is retried before ending; it does not permit own-chat escalation. Only a parentless agent, or an agent whose parent cannot be reached at all with the exact refusal recorded, asks the developer in its own chat. Dashboard starts need no parent. An Architect first delegates coordination to one Manager for one master, or one Orchestrator for concurrently worked masters; direct coordination is the developer’s choice. Prior approvals survive reconnects and compaction.

## Conventions

Canonical skills/l-01-agent-lifecycles/SKILL.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Restore the same role, operation, task, agent IDs and report from the durable handover. Reconcile an uncertain start with the same request ID. A finished turn, review, curation, semantic acceptance and paired Git publication require their separate owning evidence.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Explicit role/operation composition and taskless Projects scope. | lines 8-16 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:8-16 |
| Bound server, actual role identities, one coordinating agent under the Architect and recovery/acceptance distinction. | lines 20-35 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md:20-35 |


## Current Investigator contract impact

The native launcher’s seven roles use canonical Investigator in place of the earlier role name. Projects is execution location rather than repository identity, and manual parentless concern intake invents no task. The selected canonical role/operation owns duties; generated copies author no second role or routing authority.

- This source owns the stated current Investigator scope or canonical vocabulary. [1]


## Current intake and developer-question evidence

- Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. \[2] [2]
