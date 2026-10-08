# operations/orientation.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Recover the selected native role assignment and canonical inputs without deriving scope from the execution workspace.

## Current Contract

The native launcher supports Architect, Investigator, Orchestrator, Manager, Worker, Reviewer and Curator. System Specialist is the earlier read spelling of the same Investigator role. Missing, unsupported, inapplicable or conflicting role/operation/task bindings are reported rather than inferred. Projects is an execution location, not a repository identity. A manually selected taskless Architect asks only for missing outcome or registered repository details. An Investigator accepts a scoped concern of any kind from its actual parent's first message and asks that parent for missing concern/report scope; without a parent it uses the developer's request and own chat. Investigator may be selected at Projects, on a sprint, or on a sprint and master, never on a leaf. No synthetic repository, sprint, master, task or parent is created. Existing work recovers durable requirements, rulings, approvals, agent IDs and reports; reconnects do not invalidate supplied approval.

Task-bound reads use unchanged `taskDocReadArgs` with extensionless slug, then the returned canonical `docPath`. Read only the selected packet/task scope and verify role, requirement revision, altitude, paired roots, contract and report agree.

Use the launching build’s `agents-remember-task` server through its actual harness tool surface and schemas. The tool-server binding supplies identity; the handover supplies a parent when one exists. With a parent named in host.parent, every question requiring the developer's decision goes to that actual parent through bound role_message. Continue independent work; if none remains, record the state and await the parent's message. Busy or permission-prompt delivery stays pending and is retried before ending; it does not permit own-chat escalation. Only a parentless agent, or an agent whose parent cannot be reached at all with the exact refusal recorded, asks the developer in its own chat. Peer communication retains its bound role-message route.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/orientation.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Worker/Reviewer use memory read-only; Curator owns admitted memory writes. A dashboard role needs no parent. After compaction/reconnect restore the same assignment and inspect current AR truth before retrying an action.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Taskless/approved-scope intake, exact task reads, paired write surfaces, bound server and same-task recovery. | lines 3-13 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/orientation.md:3-13 |


## Current Investigator contract impact

Parentless Projects Investigator intake asks only for the missing concern/report scope from the developer request. Selected sprint/master intake uses the supplied actual references and concern channel. No repository, task or parent is synthesized; reconnecting preserves durable approvals and evidence.

- This source owns the stated current Investigator scope or canonical vocabulary. [1]


## Current intake and developer-question evidence

- Investigator takes any scoped concern from the actual parent, uses the developer request only without a parent, and never synthesizes task identity; developer decisions follow the parent channel with the stated parentless and unreachable exceptions. \[2] [2]
