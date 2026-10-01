# mcp/src/agents_remember/controlplane/agent_notifier_signals.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Persists agent-notifier cooldown evidence using structural owner identity plus private occupant
correlation. It prevents repeated delivery without making a runtime id the durable address.

## Code Commentary

### Logic

The record and target carry task-document reference, role, and optional current agent/lifecycle
correlation. Cooldown equality compares the full routed target plus finding kind/detail. The store
reads once per sweep, appends under declared ownership, and compacts bounded history.

### Conventions

Task document and role express the owner seat; agent and lifecycle ids are delivery evidence for the
current occupant.

### Invariants And Boundaries

- Replacement changes private correlations without changing the structural owner.
- Cooldown never matches a partial target.
- This log is delivery suppression evidence, not inbox authority.

### Todos

The retained legacy log filename is removed only with its governed durability migration.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Cooldown records carry structural and private correlation fields separately. [1]
- Target equality includes the full routed seat and finding. [2]
- The store bounds and serializes cooldown evidence. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
