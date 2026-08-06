# mcp/tests/test_memory_citation_change_detection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_change_detection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f` |
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|
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
- `MemoryProvenanceTests.test_a_memory_relative_source_uses_the_separate_memory_history`
  asserts the report-only arm (260731-EFA-L16): the memory construct changed AND the citation
  still covers it, so the review surface is report-only while the ledger-mapped memory history
  proves the diff.
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
| Defines the class `MemoryProvenanceTests` (lines 296-363). | `MemoryProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:480-551 |
| Defines the class `DependencyProvenanceTests` (lines 366-522). | `DependencyProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:554-710 |
| Defines the class `RegistrationAndLimitsTests` (lines 757-785). | `RegistrationAndLimitsTests` | mcp/tests/test_memory_citation_change_detection.py:757-785 |
| Defines the class `ChangeRoutingTests` (lines 554-873). | `ChangeRoutingTests` | mcp/tests/test_memory_citation_change_detection.py:554-873 |

## Update History

- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the three-way split coverage — the memory-relative source case now asserts the current-citation review surface is report-only (changed construct, covered range, memory-history provenance) — and the two anchor_change arms: current citation surfaces, stale range is enforced. Follow-up waves added the absent-at-stamp rule (construct added after the stamp: surfaced when current, enforced when stale, invalid when ambiguous now), the provenance-debt demotion arms (untouched document demotes, touched stays enforced, git failure fails closed, missing stamp never demotes). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
