# operations/planning.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Turn the developer outcome and current relevant knowledge into approved, bounded requirements and an owner graph.

## Current Contract

Give independently falsifiable obligations stable IDs/versions and canonical packets, cold-read new packets, and obtain developer approval before projecting task topology. Each executable leaf has one primary requirement; adjacent obligations are dependencies or preservation constraints. Preserve existing approvals.

Choose the smallest graph with independent evidence. Architect may directly coordinate distinct Worker, Reviewer and Curator agents; larger coordination may add Orchestrator or Manager. Name deliverables, paired/report roots, dependencies, evidence class, requested review, curation and publication authority.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/planning.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Tasks project approved scope and do not replace requirements. New scope, requirement contradiction or high-impact unresolved decisions return to the developer through the owner; unaffected versions stay valid. No fake task or agent identity is created for a taskless Projects role.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Canonical approved requirements, optional flat graph and ruled scope changes. | lines 3-7 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/planning.md:3-7 |
