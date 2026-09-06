# mcp/tests/test_memory_citation_source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:23:26+00:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Snapshot, parity, reuse, and publication tests for the citation source index.

## Code Commentary

### Logic

This module owns the shared `IndexCase` fixture, `_publication_failure` injection helper and
`SemanticParityTests`. Namespace, snapshot, publication/bounds and cross-process cases live in
their respective companion modules. The snapshot companion additionally exercises real Git
candidate selection; that coverage is described in its own file card.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- This card describes `mcp/tests/test_memory_citation_source_index.py`; companion rows identify their separate source files.

### Todos

None.

## Repo-Internal References

The first three rows identify this module; the remaining rows point to companion suites.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_publication_failure` (lines 27-59). | `_publication_failure` | mcp/tests/test_memory_citation_source_index.py:27-59 |
| Defines the class `IndexCase` (lines 62-115). | `IndexCase` | mcp/tests/test_memory_citation_source_index.py:62-115 |
| Defines the class `SemanticParityTests` (lines 118-169). | `SemanticParityTests` | mcp/tests/test_memory_citation_source_index.py:118-169 |
| Companion namespace suite. | `ManagedNamespaceTests` | mcp/tests/test_memory_citation_source_index_namespace.py:20-354 |
| Companion snapshot-reuse suite. | `SnapshotReuseTests` | mcp/tests/test_memory_citation_source_index_snapshot.py:26-279 |
| Companion publication and bounds suite. | "class PublicationAndBoundsTests1(IndexCase):" | mcp/tests/test_memory_citation_source_index_publication_1.py:21-21 |
| Companion cross-process suite. | `CrossProcessTests` | mcp/tests/test_memory_citation_source_index_cross.py:12-111 |

## Update History

- 2026-09-06T00:23:26+00:00 — L30 recovery: Corrected shared-fixture versus companion-suite ownership and candidate-index incoming ranges; source is unchanged and keeps its genuine verification stamp.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
