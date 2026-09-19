# mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Owns deterministic anchor-to-range projection bindings (CCR-R10). A claim's exact anchors must each resolve to one extent in the frozen source-index snapshot through the shared repair oracle. The projection records snapshot ID, prior source-cell digest, anchors, resolved extents, replacement text and repair-tool version. Its final document digest is supplied by `documents.transaction` only after the complete accepted batch has been rendered and validated. Generated no-content-impact history is included when the document already has a canonical Update History section.

Ambiguity, absent anchors, renames, deletion and malformed claims remain actionable refusals. There is no similarity search or old-range fallback, and no parallel persistent citation sidecar.

## Code Commentary

### Logic

`plan_projection` binds the repair oracle's resolved locations and leaves `new_document_digest` unset for the document owner. `verify_unchanged` checks line/span bounds before comparing the selected source cell. `conflicting_write_decline` reports that the entire document batch failed its document, cell or leased-snapshot precondition, including normalization edits whose anchor is absent.

`history_section_line` locates an existing section; `history_bullet` uses one injected UTC clock and a no-content-impact marker. `history_edit` preserves LF or CRLF and now chooses its insertion line by the section's own INSTANTS, not simply the top of the block: the generated bullet is stamped in UTC while the document's entries may carry any offset, so "directly under the heading" and "newest first" are different claims and inserting above a newer offset-bearing entry manufactured `update_history_not_newest_first` on a document nobody edited wrongly (D-27, measured `05:29:42+00:00` = 07:29:42 local sitting below `06:05+02:00`). The bullets go below every offset-bearing entry newer than the newest generated bullet, and directly under the heading when none is — the same comparison the checker makes, delegated to `history_order` (`BULLET_PATTERN`, `parse_timestamp`, `has_offset`, `datetime_value`, `update_history_sections`, `parse_entries`). Entries whose instant is not comparable (a naive stamp, a malformed bullet) end the scan rather than being ordered against, because the checker does not compare across frames either; `_newest_first` orders the generated bullets among themselves and `_bullet_instant` reads one bullet's instant or `None`. Every element keeps its own bytes. The former `document_digest` helper is removed: `DocumentTransaction.render`, `preview`, `publish` and `projections` own final bytes and their digest.

### Conventions

The fixer admits or declines each projection before adding an edit to `Staging.documents`. The document transaction owns publication and final-byte accounting. This module uses the exact-name repair/source-index oracle and does not introduce a second resolver.

### Invariants And Boundaries

- Declined projections never become accepted edits or generated history.
- No Update History section is invented when none exists.
- The generated bullet's insertion point is decided by the PARSED INSTANT, never by the block's top. The UTC stamp stays (it is an unambiguous real frame the checker normalises), and an entry whose instant is not comparable ends the scan instead of being ordered against, because the checker does not compare across frames either.
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

- 2026-09-18T19:21+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): corrected the `history_edit` claim this change falsified and recorded the frame rule behind it. The card said the edit "preserves LF or CRLF when inserting grouped bullets", which no longer describes the mechanism: `history_edit` now chooses its insertion LINE by the section's parsed instants, below every offset-bearing entry newer than the newest generated bullet and directly under the heading when none is, because the generated bullet's UTC stamp and the document's own offset are different frames — top-of-block and newest-first are therefore different claims (item 22; the recorded "inserted in string order" diagnosis was wrong, the engine has inserted at the top since `709dd076`, and the surviving defect is the frame). Incomparable instants (a naive stamp, a malformed bullet) end the scan instead of being ordered against, matching the checker. Added the invariant and the named `history_order` members the edit delegates to. Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.
- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Moved final-byte publication ownership to the document transaction, documented bounded source-cell checks and CRLF history preservation, and removed the deleted digest helper from the live inventory. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: created this file-level
  onboarding card for the new deterministic anchor-to-range projection module (CCR-R10) delivered
  in code commit 709dd076; anchors and ranges derived from the current worktree source and pinned
  to that commit.
