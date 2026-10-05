# composition-manifest.json

## Governing Overview

[MCP package overview](../../../../../../overview.md)

## Purpose

Routing metadata for the canonical lifecycle corpus; it declares source selection rather than duplicating instruction prose.

## Current Contract

`routing_conditions` names explicit supplied native role binding and manual taskless Projects selection. Missing, unsupported, inapplicable or conflicting selection fails closed; no role, task, repository, parent or operation default is inferred.

`composition_order` is `role`, then `operation`. The retained core map is inert metadata for the compiler and supplies no shared instructions to a role capsule. Task facts and workspace bindings are a separate handover channel.

The registry/compiler vocabulary retains ten roles and nine operations, while the native launcher exposes seven roles. Native role-start authority is granted only to Architect, Orchestrator and Manager within their documented scope; the seven launched roles receive role messaging.

## Conventions

Canonical skills/l-01-agent-lifecycles/composition-manifest.json owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

A retained registry entry does not establish native launch support. Select an operation only when the manifest admits it for the role. Generated copies never define separate routing policy.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| The two explicit routing conditions and their scope/refusal fields. | lines 18-36 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:18-36 |
| Role/operation order, inert core metadata, separate facts and seven-launcher distinction. | lines 593-602 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:593-602 |
