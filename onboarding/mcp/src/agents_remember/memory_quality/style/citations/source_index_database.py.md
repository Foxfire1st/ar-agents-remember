# mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

SQLite storage for one immutable citation source-index generation.

## Code Commentary

### Logic

Module-level surface:

- `SourceIndexDatabaseError` (class, lines 36-37) — An index database is incompatible, corrupt, or mismatched.
- `_Digest` (class, lines 40-41)
- `_metadata_integer` (function, lines 44-55)
- `_validate_generation_metadata` (function, lines 58-96)
- `_generation_counters` (function, lines 99-124)
- `IndexedFile` (class, lines 128-132) — All extents one anchor has in one indexed file.
- `Database` (class, lines 136-629) — Typed access to one SQLite source-index generation.
- `_validate_quote_streams` (function, lines 632-651)
- `_record_expected_short` (function, lines 654-658)
- `_validate_direct_postings` (function, lines 661-679)
- `_validate_one_direct_posting` (function, lines 682-689)
- `_validate_short_postings` (function, lines 692-709)
- `_validate_call_literals` (function, lines 712-720)
- `_validate_stored_digest` (function, lines 723-730)
- `_anchor_key` (function, lines 733-738)
- `_application_digest` (function, lines 741-779) — Canonical checksum of every query-bearing row, including FTS term/doc pairs.
- `_digest_value` (function, lines 782-798)
- `_pack_extents` (function, lines 801-804)
- `_pack_posting` (function, lines 807-810)
- `_unpack_postings` (function, lines 813-826)
- `_unpack_stream_ids` (function, lines 829-835)
- `_unpack_extents` (function, lines 838-851)
- `_occurrence_extents` (function, lines 854-861)
- `_pack_text` (function, lines 864-865)
- `_unpack_text` (function, lines 868-872)
- `_pack_marks` (function, lines 875-880)
- `_unpack_marks` (function, lines 883-904)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `SourceIndexDatabaseError` (lines 36-37) — An index database is incompatible, corrupt, or mismatched.. | `SourceIndexDatabaseError` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:36-37 |
| Defines the class `_Digest` (lines 40-41). | `_Digest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:40-41 |
| Defines the function `_metadata_integer` (lines 44-55). | `_metadata_integer` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:44-55 |
| Defines the function `_validate_generation_metadata` (lines 58-96). | `_validate_generation_metadata` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:58-96 |
| Defines the function `_generation_counters` (lines 99-124). | `_generation_counters` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:99-124 |
| Defines the class `IndexedFile` (lines 128-132) — All extents one anchor has in one indexed file.. | `IndexedFile` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:128-132 |
| Defines the class `Database` (lines 136-629) — Typed access to one SQLite source-index generation.. | `Database` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:136-629 |
| Defines the function `_validate_quote_streams` (lines 632-651). | `_validate_quote_streams` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:632-651 |
| Defines the function `_record_expected_short` (lines 654-658). | `_record_expected_short` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:654-658 |
| Defines the function `_validate_direct_postings` (lines 661-679). | `_validate_direct_postings` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:661-679 |
| Defines the function `_validate_one_direct_posting` (lines 682-689). | `_validate_one_direct_posting` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:682-689 |
| Defines the function `_validate_short_postings` (lines 692-709). | `_validate_short_postings` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:692-709 |
| Defines the function `_validate_call_literals` (lines 712-720). | `_validate_call_literals` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:712-720 |
| Defines the function `_validate_stored_digest` (lines 723-730). | `_validate_stored_digest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:723-730 |
| Defines the function `_anchor_key` (lines 733-738). | `_anchor_key` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:733-738 |
| Defines the function `_application_digest` (lines 741-779) — Canonical checksum of every query-bearing row, including FTS term/doc pairs.. | `_application_digest` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:741-779 |
| Defines the function `_digest_value` (lines 782-798). | `_digest_value` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:782-798 |
| Defines the function `_pack_extents` (lines 801-804). | `_pack_extents` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:801-804 |
| Defines the function `_pack_posting` (lines 807-810). | `_pack_posting` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:807-810 |
| Defines the function `_unpack_postings` (lines 813-826). | `_unpack_postings` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:813-826 |
| Defines the function `_unpack_stream_ids` (lines 829-835). | `_unpack_stream_ids` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:829-835 |
| Defines the function `_unpack_extents` (lines 838-851). | `_unpack_extents` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:838-851 |
| Defines the function `_occurrence_extents` (lines 854-861). | `_occurrence_extents` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:854-861 |
| Defines the function `_pack_text` (lines 864-865). | `_pack_text` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:864-865 |
| Defines the function `_unpack_text` (lines 868-872). | `_unpack_text` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:868-872 |
| Defines the function `_pack_marks` (lines 875-880). | `_pack_marks` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:875-880 |
| Defines the function `_unpack_marks` (lines 883-904). | `_unpack_marks` | mcp/src/agents_remember/memory_quality/style/citations/source_index_database.py:883-904 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
