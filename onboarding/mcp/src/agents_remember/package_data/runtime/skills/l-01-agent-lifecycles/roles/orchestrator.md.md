# l-01-agent-lifecycles/roles/orchestrator.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

An optional native Orchestrator coordinates one selected sprint’s tasks and owners at Projects altitude.

## Current Contract

Read only the canonical task/packet/report/predecessor facts needed for the current decision, using exact supplied task arguments. Missing requirement or owner facts are named from their source.

Start distinct Manager, Worker, Reviewer and Curator agents only under the selected sprint; backend coordination remains optional according to scale. Keep actual IDs, reconcile unknown starts by the same request ID and follow assignments through bound messages/results without a separate poller.

Inspect the full candidate and actual checks/reports before requesting required independent review or affected curation. Carry producer Curator handoff data verbatim and co-resolve it rather than paraphrasing.

## Conventions

Canonical skills/l-01-agent-lifecycles/roles/orchestrator.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Paseo turn status is execution metadata, not AR acceptance/landing. Developer decisions remain in the own chat; peer questions return to the actual bound parent when present. No fabricated task, identity, duplicate execution or second semantic ledger.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Selected-sprint truth, optional coordination, same-agent follow-through and producer/evidence preservation. | lines 8-24 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:8-24 |
