# mcp/src/agents_remember/models/conversations/stream_events.py

| Field                  | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| repository             | agents-remember                                                  |
| path                   | `mcp/src/agents_remember/models/conversations/stream_events.py`   |
| doc_type               | `file-level-onboarding`                                          |
| lastUpdated            | 2026-08-29T17:23+02:00                                           |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`                       |
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `overview.md`                                                    |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/stream_events.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the SSE mutation grammar: append, delta, upsert,
replace-page, status, and explicit gap mutations inside `ConversationEventEnvelope`.

## Code Commentary

### Logic

`AppendItemMutation` (cit:(["class AppendItemMutation"], mcp/src/agents_remember/models/conversations/stream_events.py:19-19)) opens the mutation family;
`GapMutation` (cit:(["class GapMutation"], mcp/src/agents_remember/models/conversations/stream_events.py:67-67)) is the explicit established-stream failure
marker; `ConversationEventEnvelope` (cit:(["class ConversationEventEnvelope"], mcp/src/agents_remember/models/conversations/stream_events.py:88-88)) carries the envelope
with the L4 defaulted `previous_cursor`.

### Invariants And Boundaries

- On an established-stream gap, emit the explicit gap mutation, require repage, and close rather
  than silently resetting.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Hostile tests pin event/cursor products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 type-alias syntax migration for `ConversationMutation` and confirmed that the event mutation grammar remains as documented. Verification remains closeout-owned.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the stream-events module moved
  from `serving/conversation/_models_status.py`. Verification metadata pinned until closeout
  stamps the L9 code commit.
