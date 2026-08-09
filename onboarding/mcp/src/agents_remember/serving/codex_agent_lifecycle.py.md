# mcp/src/agents_remember/serving/codex_agent_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_agent_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `fb0296562ceb29929a3675a1b0195700d23bc56a`|
| lastVerifiedCommitDate |  2026-08-09T20:35:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Serving overview](overview.md)

## Purpose

Centralizes authority ordering for status changes in the Codex adapter's bounded child registry.

## Code Commentary

### Logic

`merge_agent_status` prevents history or generic thread state from reopening a terminal child;
only an explicit later `turn/started` can prove a new lifecycle. `completed_turn_status` maps
Codex terminal spellings into the public completed/failed/interrupted roster vocabulary.

### Conventions

Authority ordering is shared by live notifications and history reconstruction rather than
duplicated in adapter branches.

### Invariants And Boundaries

- Terminal status is monotonic absent an explicit new turn.
- Cancelled and interrupted normalize to `interrupted`.
- Failed and errored normalize to `failed`.
- Unknown terminal spellings settle as `completed` only at the already-terminal turn boundary.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Adapter registry applies the shared ordering. | "thread/status/changed params" | mcp/src/agents_remember/serving/codex_app_server_adapter.py:658-658 |
| Lifecycle vocabulary regression. | `test_completed_turn_status_uses_roster_vocabulary` | mcp/tests/test_codex_agent_lifecycle.py:7-21 |

## Cross-Repo References

The status spellings originate in Codex app-server evidence, but no external Domain Documentation
source was configured for this pass.

## Update History

- 2026-08-02T21:14:56+02:00 — 260731-EFA-L6 curator W2-B10: repaired 4 citation findings (2 reference rows); scoped recheck clean.

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  shared child lifecycle authority ordering. Verification metadata remains blank until commit.
