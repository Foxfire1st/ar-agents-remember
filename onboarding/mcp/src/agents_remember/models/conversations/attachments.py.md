# mcp/src/agents_remember/models/conversations/attachments.py

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

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
