# mcp/src/agents_remember/memory_quality/style/citations/editing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/editing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T04:32:25+00:00 |
| lastVerifiedCommitHash | `b34f4a59562b76a3e2413027468e0f699117b36f` |
| lastVerifiedCommitDate | 2026-09-06T06:31:12+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Byte-preserving edits shared by citation migration and steady-state repair.

## Code Commentary

### Logic

`Documents.lines` reads raw bytes, decodes UTF-8 and splits only on LF. Rejoining therefore preserves CRLF carriage returns and a trailing newline. `Site` identifies one source-list span; `spliced` retains its surrounding padding; `rewritten` applies edits right-to-left so multiple cells on one line keep their original offsets.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- UTF-8 decoding does not perform universal-newline conversion.
- Untouched text and source-cell padding survive a rewrite; right-to-left composition preserves offsets.
- This cache is the original document read. Publication freshness belongs to `documents.transaction`, which rereads the full document before replacement.

### Todos

None.

## Docs References

No external Domain Documentation source is configured. This card describes the repository's own implementation and forcing contracts without an external documentation claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source. | N/A | N/A |

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Site` (lines 9-15) — The exact span of one claim's source list, in one line of one document.. | `Site` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:9-15 |
| Defines the class `Documents` (lines 18-27) — The memory documents one run reads, split so that rejoining is lossless.. | `Documents` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:18-27 |
| Defines the function `spliced` (lines 30-34) — ``line`` with the source list replaced and the cell's own padding untouched.. | `spliced` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:30-34 |
| Defines the function `rewritten` (lines 37-42) — ``lines`` with each site's source list replaced, right to left so offsets hold.. | `rewritten` | mcp/src/agents_remember/memory_quality/style/citations/editing.py:37-42 |

## Cross-Repo References

This file introduces no separate cross-repository protocol. Local temporary code/memory roots and their application write-scope contract remain distinct from a cross-repository authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No new cross-repository protocol. | N/A | N/A |

## Update History

- 2026-09-06T04:32:25+00:00 — L32 private-candidate curation at `b34f4a59562b76a3e2413027468e0f699117b36f`: Documented raw-byte UTF-8 reads and lossless CRLF composition; kept freshness and publication authority with the document transaction. Verification is source review of the prepared commit; Gate 5 and delivery remain pending.

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
