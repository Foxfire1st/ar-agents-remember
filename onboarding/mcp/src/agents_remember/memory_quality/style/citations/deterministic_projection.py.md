# mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Owns deterministic anchor-to-range projection bindings (CCR-R10). A claim's exact anchors must each resolve to one extent in the frozen source-index snapshot through the shared repair oracle. The projection records snapshot ID, prior source-cell digest, anchors, resolved extents, replacement text and repair-tool version. Its final document digest is supplied by `documents.transaction` only after the complete accepted batch has been rendered and validated. Generated no-content-impact history is included when the document already has a canonical Update History section.

Ambiguity, absent anchors, renames, deletion and malformed claims remain actionable refusals. There is no similarity search or old-range fallback, and no parallel persistent citation sidecar.

## Code Commentary

### Logic

`plan_projection` binds the repair oracle's resolved locations and leaves `new_document_digest` unset for the document owner. `verify_unchanged` checks line/span bounds before comparing the selected source cell. `conflicting_write_decline` reports that the entire document batch failed its document, cell or leased-snapshot precondition, including normalization edits whose anchor is absent.

`history_section_line` locates an existing section; `history_bullet` uses one injected UTC clock and a no-content-impact marker. `history_edit` preserves LF or CRLF when inserting grouped bullets. The former `document_digest` helper is removed: `DocumentTransaction.render`, `preview`, `publish` and `projections` own final bytes and their digest.

### Conventions

The fixer admits or declines each projection before adding an edit to `Staging.documents`. The document transaction owns publication and final-byte accounting. This module uses the exact-name repair/source-index oracle and does not introduce a second resolver.

### Invariants And Boundaries

- Declined projections never become accepted edits or generated history.
- No Update History section is invented when none exists.
- Source-cell validation is a bounded precondition, not a memory-file mutex or operating-system compare-and-swap.
- The document owner checks complete bytes and the held lease as well as these projection bindings.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

The binding owner delegates publication to the document transaction.

| Finding | Anchor | Source |
| --- | --- | --- |
| A projection carries original cell, oracle extents and deferred document digest. | `Projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:64-104 |
| Each anchor must have exactly one resolved extent from the repair outcome. | `plan_projection` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:167-218 |
| Removed lines and unsafe source spans refuse before slicing. | `verify_unchanged` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:221-232 |
| A document-batch conflict has an explicit refusal, including an optional anchor. | `conflicting_write_decline` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:235-243 |
| History insertion preserves the heading line-ending convention. | `history_edit` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:246-256 |
| The transaction renders, validates and publishes the complete accepted batch. | `DocumentTransaction` | mcp/src/agents_remember/memory_quality/style/citations/documents/transaction.py:30-99 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Moved final-byte publication ownership to the document transaction, documented bounded source-cell checks and CRLF history preservation, and removed the deleted digest helper from the live inventory. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: created this file-level
  onboarding card for the new deterministic anchor-to-range projection module (CCR-R10) delivered
  in code commit 709dd076; anchors and ranges derived from the current worktree source and pinned
  to that commit.
