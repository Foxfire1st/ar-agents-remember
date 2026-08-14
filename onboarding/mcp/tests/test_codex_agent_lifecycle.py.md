# mcp/tests/test_codex_agent_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_agent_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Pins Codex terminal turn statuses to the public child-roster vocabulary.

## Code Commentary

### Logic

A parameterized table verifies that cancelled/interrupted become `interrupted`,
failed/errored become `failed`, and successful or otherwise terminal completion becomes
`completed`.

### Conventions

This is the unit-level vocabulary pin for the adapter and history reader.

### Invariants And Boundaries

- All exposed terminal states are valid `ConversationAgentStatus` values.
- Equivalent Codex terminal spellings converge.

### Todos

None known.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Normalizer under test. | `completed_turn_status` | mcp/src/agents_remember/serving/codex_agent_lifecycle.py:26-33 |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  Codex child lifecycle vocabulary regression. Verification metadata remains blank until commit.
