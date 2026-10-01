# mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py

## Governing Overview

[Active projector package overview](overview.md)

## Purpose

Resolves child-thread identity and reconciles historical roster observations with the current
adapter registry.

## Code Commentary

### Logic

`AgentAuthority` classifies a frame as parent or child from its exact thread id, records only
threads observed live, and builds a `ConversationAgentRef` from the adapter snapshot's
`agentRegistry`. Binding attaches the child ref without overwriting evidence-owned identity.
Roster reconciliation can fill a missing path and can replace historical/unknown status with
current registry status, marking that row as harness-live.

### Conventions

Status normalization is an explicit vocabulary. Unrecognized values remain `unknown`.

### Invariants And Boundaries

- The parent thread never becomes its own child agent.
- Identity is never inferred from labels or content.
- Native child item ids are thread-scoped before entering the shared store.
- Historical terminal rows are enriched only from current registry authority.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Codex roster items consumed here. [1]
- Adapter registry authority. [2]

### Cross-Repo References

No meaningful cross-repository references found.
