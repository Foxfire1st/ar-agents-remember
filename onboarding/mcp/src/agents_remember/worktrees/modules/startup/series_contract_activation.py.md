# mcp/src/agents_remember/worktrees/modules/startup/series_contract_activation.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Activate a canonical master series after task-stage preflight and shared structural bootstrap.

## Code Commentary

Manager dispatch and first-leaf start use one activation owner. Preflight requires the commanded atomic master and validates its start-stage binding before mutation; dry-run uses a read-only preflight path. Best-effort upstream fetch occurs before integration authority. Bootstrap recovery/existence checks, branch setup and contract publication share the per-master native lock; that store transaction finishes before per-contract reconciliation to avoid nesting store locks. The selected series is reconciled under its existing authority. A returned contract then publishes its task-stage facts; a binding failure becomes a typed refusal, not rollback of already-created structural work. Contract existence is durable-work evidence, not scheduling or session authority.

## Evidence

- Shared bootstrap, lock ordering and reconciliation. [1]
- Read-only dry-run and task-stage preflight. [2]
- Post-activation stage publication and typed failure. [3]
