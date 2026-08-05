# mcp/tests/test_memory_citation_change_detection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_change_detection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Per-claim change-detection bites over real code, memory, and dependency history.

## Code Commentary

### Logic

Module-level surface:

- `git` (function, lines 29-38)
- `ProvenanceTree` (class, lines 41-107)
- `ChangeDetectionCase` (class, lines 110-121)
- `CodeProvenanceTests` (class, lines 124-293)
- `MemoryProvenanceTests` (class, lines 296-363)
- `DependencyProvenanceTests` (class, lines 366-522)
- `RegistrationAndLimitsTests` (class, lines 525-551)
- `ChangeRoutingTests` (class, lines 554-873)

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
| Defines the function `git` (lines 29-38). | `git` | mcp/tests/test_memory_citation_change_detection.py:29-38 |
| Defines the class `ProvenanceTree` (lines 41-107). | `ProvenanceTree` | mcp/tests/test_memory_citation_change_detection.py:41-107 |
| Defines the class `ChangeDetectionCase` (lines 110-121). | `ChangeDetectionCase` | mcp/tests/test_memory_citation_change_detection.py:110-121 |
| Defines the class `CodeProvenanceTests` (lines 124-293). | `CodeProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:124-293 |
| Defines the class `MemoryProvenanceTests` (lines 296-363). | `MemoryProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:296-363 |
| Defines the class `DependencyProvenanceTests` (lines 366-522). | `DependencyProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:366-522 |
| Defines the class `RegistrationAndLimitsTests` (lines 525-551). | `RegistrationAndLimitsTests` | mcp/tests/test_memory_citation_change_detection.py:525-551 |
| Defines the class `ChangeRoutingTests` (lines 554-873). | `ChangeRoutingTests` | mcp/tests/test_memory_citation_change_detection.py:554-873 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
