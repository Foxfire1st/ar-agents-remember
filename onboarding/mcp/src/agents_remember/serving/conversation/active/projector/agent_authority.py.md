# mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Codex roster items consumed here. | [codex.py](agents-remember/mcp/src/agents_remember/serving/conversation/projectors/codex.py) |
| Adapter registry authority. | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the child identity
  and roster-authority sidecar. Verification metadata remains blank until commit.
