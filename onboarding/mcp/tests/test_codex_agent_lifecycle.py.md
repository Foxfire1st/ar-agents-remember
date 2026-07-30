# mcp/tests/test_codex_agent_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_codex_agent_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash |  `3a8ff703d796dc585b86a458daaf9eb2af6b2b31`|
| lastVerifiedCommitDate |  2026-07-30T13:59:13+02:00|
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

| Finding | Source Path |
| --- | --- |
| Normalizer under test. | [codex_agent_lifecycle.py](agents-remember/mcp/src/agents_remember/serving/codex_agent_lifecycle.py) |

## Cross-Repo References

No meaningful cross-repository references found.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: created onboarding for the
  Codex child lifecycle vocabulary regression. Verification metadata remains blank until commit.
