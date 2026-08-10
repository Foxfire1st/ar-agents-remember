# mcp/tests/test_memory_document_shape.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_document_shape.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `201b0599e5d79049252033c7b737df631135b11d` |
| lastVerifiedCommitDate | 2026-08-10T13:54:43+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Precision and recall for the memory-document style surface, including the entity-catalog alignment check that closeout runs during its fail-fast preflight.

## Code Commentary

### Logic

Module-level surface:

- `write` (function, lines 67-71)
- `document` (function, lines 74-75)
- `history_document` (function, lines 78-79)
- `table_document` (function, lines 82-83)
- `PrecisionFixtures` (class, lines 86-170) — Known-good constructs, copied from live memory documents, that must not be flagged.
- `InlineScanTests` (class, lines 173-195) — The ordering rule itself: code spans located before escapes are applied.
- `DiffMarkerTests` (class, lines 198-223)
- `TableTests` (class, lines 226-277)
- `RemediationTests` (class, lines 280-345) — The remediation must be complete, because it is followed.
- `UpdateHistoryTimezoneTests` (class, lines 348-432) — The offset rule, and the closeout diff that scopes it.
- `ClosingDiffScopeTests` (class, lines 435-556) — The rule applies to what this closeout wrote, and to nothing else.
- `StyleSurfaceTests` (class, lines 559-594)
- `DefensiveBranchTests` (class, lines 597-710) — The guards that keep a sweep from crashing on a tree that is not what it expects.

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
| Defines the function `write` (lines 67-71). | `write` | mcp/tests/test_memory_document_shape.py:67-71 |
| Defines the function `document` (lines 74-75). | `document` | mcp/tests/test_memory_document_shape.py:74-75 |
| Defines the function `history_document` (lines 78-79). | `history_document` | mcp/tests/test_memory_document_shape.py:78-79 |
| Defines the function `table_document` (lines 82-83). | `table_document` | mcp/tests/test_memory_document_shape.py:82-83 |
| Defines the class `PrecisionFixtures` (lines 86-170) — Known-good constructs, copied from live memory documents, that must not be flagged.. | `PrecisionFixtures` | mcp/tests/test_memory_document_shape.py:86-170 |
| Defines the class `InlineScanTests` (lines 173-195) — The ordering rule itself: code spans located before escapes are applied.. | `InlineScanTests` | mcp/tests/test_memory_document_shape.py:173-195 |
| Defines the class `DiffMarkerTests` (lines 198-223). | `DiffMarkerTests` | mcp/tests/test_memory_document_shape.py:198-223 |
| Defines the class `TableTests` (lines 226-277). | `TableTests` | mcp/tests/test_memory_document_shape.py:226-277 |
| Defines the class `RemediationTests` (lines 280-345) — The remediation must be complete, because it is followed.. | `RemediationTests` | mcp/tests/test_memory_document_shape.py:280-345 |
| Defines the class `UpdateHistoryTimezoneTests` (lines 348-432) — The offset rule, and the closeout diff that scopes it.. | `UpdateHistoryTimezoneTests` | mcp/tests/test_memory_document_shape.py:348-432 |
| Defines the class `ClosingDiffScopeTests` (lines 435-556) — The rule applies to what this closeout wrote, and to nothing else.. | `ClosingDiffScopeTests` | mcp/tests/test_memory_document_shape.py:435-556 |
| Defines the class `StyleSurfaceTests` (lines 559-594). | `StyleSurfaceTests` | mcp/tests/test_memory_document_shape.py:559-594 |
| Defines the class `DefensiveBranchTests` (lines 597-710) — The guards that keep a sweep from crashing on a tree that is not what it expects.. | `DefensiveBranchTests` | mcp/tests/test_memory_document_shape.py:597-710 |

## Update History

- 2026-08-10T00:00+02:00 — 260731-EFA-L9 follow-up: the default-style surface assertion now includes entity-catalog alignment so the full suite proves registration of the new fail-fast preflight check. Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
