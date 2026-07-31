# mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
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

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py` since the L2
  base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s),
  touching only redundant grouping parentheses. Checked by parsing both revisions and comparing
  the abstract syntax trees (identical) and the comment tokens (identical), so no symbol,
  signature, default, decorator, control-flow branch, docstring, or assertion this card describes
  has moved, and every claim this card makes about its own source still holds.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created the child identity
  and roster-authority sidecar. Verification metadata remains blank until commit.
