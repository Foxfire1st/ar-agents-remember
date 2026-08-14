# mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/projector/agent_authority.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Codex roster items consumed here. | "def _collab_roster_upserts(" | mcp/src/agents_remember/serving/conversation/projectors/_codex_collab.py:273-273 |
| Adapter registry authority. | `_publish_agent_registry` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:1075-1083 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:59:59+02:00 — Curated 4 citation findings (2 table rows, 2 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

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
