# mcp/src/agents_remember/models/conversations/status.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/models/conversations/status.py`      |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                   |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/status.py` (260731-EFA-L9, moved from
`serving/conversation/_models_status.py`) owns the canonical evidence-to-turn-state vocabulary:
waiting and terminal cross-products validate against exact evidence.

## Code Commentary

### Logic

`StatusFreshness` (cit:(["class StatusFreshness"], mcp/src/agents_remember/models/conversations/status.py:55-55)) carries evidence freshness with the L4
defaulted-nullable fields; `ConversationTurnStatus` (cit:(["class ConversationTurnStatus"], mcp/src/agents_remember/models/conversations/status.py:87-87)) validates waiting/terminal
cross-products; `ConversationStatusEvidence` (cit:(["class ConversationStatusEvidence"], mcp/src/agents_remember/models/conversations/status.py:132-132)) and
"class ConversationStatus(WireModel):" (cit:(["class ConversationStatus(WireModel):"], mcp/src/agents_remember/models/conversations/status.py:137-137)) fix the evidence classification —
unknown evidence cannot establish `ready`.

### Invariants And Boundaries

- `ready` cannot be derived from unknown evidence; waiting and terminal states retain matching
  evidence products.
- A model must validate its own emitted body: fields reached by `exclude_none=True` serializers
  must be nullable AND defaulted.

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
| Hostile tests pin status/evidence products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the status module moved from
  `serving/conversation/_models_status.py`; L4 nullable-default knowledge preserved.
  Verification metadata pinned until closeout stamps the L9 code commit.
