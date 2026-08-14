# mcp/src/agents_remember/models/conversations/submissions.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/models/conversations/submissions.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-08-08T14:38+02:00                                         |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                     |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/submissions.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns the cockpit queue and submit DTOs:
queue identity, operation queue items/projections, typed submit blocks, and the conversation
submit request.

## Code Commentary

### Logic

`CockpitQueueIdentity` (cit:(["class CockpitQueueIdentity"], mcp/src/agents_remember/models/conversations/submissions.py:16-16)) brands the queue;
`OperationQueueItem` (cit:(["class OperationQueueItem"], mcp/src/agents_remember/models/conversations/submissions.py:23-23)) and `OperationQueueProjection`
(cit:(["class OperationQueueProjection"], mcp/src/agents_remember/models/conversations/submissions.py:44-44)) model the source-aware queue;
`ConversationSubmitRequest` (cit:(["class ConversationSubmitRequest"], mcp/src/agents_remember/models/conversations/submissions.py:71-71)) validates the full
submit semantic product with text/asset composer blocks.

### Invariants And Boundaries

- Only queued cockpit work exposes withdrawal identity; raw drafts exist only in authoritative
  successful withdrawal responses.

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
| Hostile tests pin queue/submission products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the submissions module moved from
  `serving/conversation/_models_operations.py`. Verification metadata pinned until closeout
  stamps the L9 code commit.
