# mcp/tests/test_memory_citation_source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Snapshot, parity, reuse, and publication tests for the citation source index.

## Code Commentary

### Logic

Module-level surface:

- `_publication_failure` (function, lines 39-70)
- `IndexCase` (class, lines 73-126)
- `SemanticParityTests` (class, lines 129-180)
- `ManagedNamespaceTests` (class, lines 183-517)
- `SnapshotReuseTests` (class, lines 520-772)
- `PublicationAndBoundsTests` (class, lines 775-1247)
- `CrossProcessTests` (class, lines 1250-1349)

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
| Defines the function `_publication_failure` (lines 39-70). | `_publication_failure` | mcp/tests/test_memory_citation_source_index.py:27-59 |
| Defines the class `IndexCase` (lines 73-126). | `IndexCase` | mcp/tests/test_memory_citation_source_index.py:73-126 |
| Defines the class `SemanticParityTests` (lines 129-180). | `SemanticParityTests` | mcp/tests/test_memory_citation_source_index.py:118-169 |
| Defines the class `ManagedNamespaceTests` (lines 183-517). | `ManagedNamespaceTests` | mcp/tests/test_memory_citation_source_index_namespace.py:20-354 |
| Defines the class `SnapshotReuseTests` (lines 520-772). | `SnapshotReuseTests` | mcp/tests/test_memory_citation_source_index_snapshot.py:20-272 |
| Defines the class `PublicationAndBoundsTests1` (IndexCase). | "class PublicationAndBoundsTests1(IndexCase):" | mcp/tests/test_memory_citation_source_index_publication_1.py:17-17 |
| Defines the class `CrossProcessTests` (lines 1250-1349). | `CrossProcessTests` | mcp/tests/test_memory_citation_source_index_cross.py:12-111 |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
