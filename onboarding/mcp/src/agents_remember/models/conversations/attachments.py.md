# mcp/src/agents_remember/models/conversations/attachments.py

| Field                  | Value                                                           |
| ---------------------- | --------------------------------------------------------------- |
| repository             | agents-remember                                                 |
| path                   | `mcp/src/agents_remember/models/conversations/attachments.py`    |
| doc_type               | `file-level-onboarding`                                         |
| lastUpdated            | 2026-08-08T14:38+02:00                                          |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                      |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                   |

## Governing Overview

[models conversations overview](overview.md)

## Purpose

`models/conversations/attachments.py` (260731-EFA-L9, moved from
`serving/conversation/_models_operations.py`) owns the typed attachment receipt and operation
projection DTOs.

## Code Commentary

### Logic

`AttachmentReceipt` (cit:(["class AttachmentReceipt"], mcp/src/agents_remember/models/conversations/attachments.py:17-17)) is the digest-verified receipt;
`AttachmentOperationProjection` (cit:(["class AttachmentOperationProjection"], mcp/src/agents_remember/models/conversations/attachments.py:34-34)) is the
control operation's projection for the cockpit.

### Invariants And Boundaries

- Attachments ride submit as digest-verified references only; the projection never exposes raw
  asset bytes.

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
| Hostile tests pin attachment products. | `test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` | mcp/tests/test_conversation_contracts.py:196-220 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the attachments module moved from
  `serving/conversation/_models_operations.py`. Verification metadata pinned until closeout
  stamps the L9 code commit.
