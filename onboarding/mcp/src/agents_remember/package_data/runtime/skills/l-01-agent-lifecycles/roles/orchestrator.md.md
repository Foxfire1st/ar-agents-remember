# l-01-agent-lifecycles/roles/orchestrator.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

A native Orchestrator coordinates one selected sprint’s tasks and owners at Projects altitude when two or more masters are worked on at the same time, or when the developer explicitly asks for one above a single master.

## Current Contract

Read only the canonical task/packet/report/predecessor facts needed for the current decision, using exact supplied task arguments. Missing requirement or owner facts are named from their source.

Start distinct Manager, Worker, Reviewer and Curator agents only under the selected sprint; reuse each existing Manager named by the Architect and start one Manager per other master. Keep actual IDs, reconcile unknown starts by the same request ID and follow assignments through bound messages/results without a separate poller.

Verify each Manager's delivery and aggregate evidence; it may inspect the supplied actual diffs for acceptance without taking over the leaf-diff or repair loop, which the Manager owns. Request independent review and affected curation when the brief or risk requires it. Carry producer Curator handoff data verbatim and co-resolve it rather than paraphrasing.

## Conventions

Canonical skills/l-01-agent-lifecycles/roles/orchestrator.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

Paseo turn status is execution metadata, not AR acceptance/landing. Developer decisions remain in the own chat; a parent-bound coordinating role sends only the four developer-needed categories plus the once-only final report to its actual parent, while ordinary requirement readings and operational rulings stay with the role. No fabricated task, identity, duplicate execution or second semantic ledger.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Selected-sprint truth, one Manager per master, same-agent follow-through and producer/evidence preservation. | lines 8-24 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md:8-24 |
