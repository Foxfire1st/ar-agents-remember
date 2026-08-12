# mcp/tests/test_memory_citation_change_detection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_change_detection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-07T14:30+02:00 |
| lastVerifiedCommitHash | `65cb81f7de4db13c0627264fec1eb46f444e0ee3` |
| lastVerifiedCommitDate | 2026-08-12T04:57:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Per-claim change-detection bites over real code, memory, and dependency history. Registration,
cache limits, and history-routing cases now live in `test_memory_citation_change_routing.py` while
the shared real-Git fixtures remain single-owned here.

## Code Commentary

### Logic

Module-level surface:

- `git` (function, lines 29-38)
- `ProvenanceTree` (class, lines 42-110)
- `ChangeDetectionCase` (class, lines 111-124)
- `CodeProvenanceTests` (class, lines 125-587) — round 9 adds the whole-new-file arms:
  `test_a_new_source_surfaces_report_only_when_current`, `test_a_new_source_is_enforced_when_stale`,
  `test_a_new_source_is_invalid_when_ambiguous`, and
  `test_a_new_source_is_invalid_when_absent_from_the_working_tree` pin the absent-at-stamp rule
  extended to whole source files added after the stamp (unique working-tree anchor inside a cited
  range surfaces report-only; stale, ambiguous, or absent evidence stays hard).
  ARG-L1 adds the closeout fallback boundary: a dirty unstamped card can be compared against the
  supplied leaf base, while committed unstamped debt still returns `citation_provenance_missing`.
- `MemoryProvenanceTests.test_a_memory_relative_source_uses_the_separate_memory_history`
  asserts the report-only arm (260731-EFA-L16): the memory construct changed AND the citation
  still covers it, so the review surface is report-only while the ledger-mapped memory history
  proves the diff.
- `MemoryProvenanceTests` (class, lines 588-661)
- `DependencyProvenanceTests` (class, lines 662-820)
- `RegistrationAndLimitsTests` moved to `test_memory_citation_change_routing.py`.
- `ChangeRoutingTests` moved to `test_memory_citation_change_routing.py`; its round 9 update
  `test_untracked_and_ignored_local_paths_are_never_proven_unchanged` so an untracked/ignored
  new source whose anchor resolves exactly once inside a cited range is the report-only surface
  rather than invalid provenance.

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
| Defines the function `git` (lines 29-38). | `git` | mcp/tests/test_memory_citation_change_detection.py:24-33 |
| Defines the class `ProvenanceTree` (lines 42-110). | `ProvenanceTree` | mcp/tests/test_memory_citation_change_detection.py:36-106 |
| Defines the class `ChangeDetectionCase` (lines 111-124). | `ChangeDetectionCase` | mcp/tests/test_memory_citation_change_detection.py:109-121 |
| Defines the class `CodeProvenanceTests` (lines 125-587). | `CodeProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:123-612 |
| Defines the class `MemoryProvenanceTests` (lines 588-661). | `MemoryProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:614-686 |
| Defines the class `DependencyProvenanceTests` (current history-suite range). | `DependencyProvenanceTests` | mcp/tests/test_memory_citation_change_detection.py:688-844 |
| Defines the class `RegistrationAndLimitsTests` (lines 821-849). | `RegistrationAndLimitsTests` | mcp/tests/test_memory_citation_change_routing.py:20-47 |
| Defines the class `ChangeRoutingTests` (lines 850-1180). | `ChangeRoutingTests` | mcp/tests/test_memory_citation_change_routing.py:49-380 |

## Update History

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: split registration/routing from provenance
  history, retained one shared real-Git fixture owner, and refreshed all moved ranges.

- 2026-08-10T08:20+02:00 — 260805-ARG-L1: added real-Git proofs that temporary leaf-base
  provenance applies only to dirty unstamped cards and never forgives committed unstamped debt.
  Verification metadata remains pinned until closeout stamps ARG-L1.
- 2026-08-07T14:30+02:00 — 260731-EFA-L8 curator (bounded delta): recorded the round-9
  whole-new-file rule — the absent-at-stamp tests now cover whole source files added after the
  stamp (surfaces report-only when current and unique in range; enforced when stale or absent;
  invalid when ambiguous), and `ChangeRoutingTests`' untracked/ignored local-path arm asserts the
  report-only surface for an exactly-once in-range anchor. Refreshed the class ranges. Verification
  metadata stays pinned until closeout stamps the code commit.
- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the three-way split coverage — the memory-relative source case now asserts the current-citation review surface is report-only (changed construct, covered range, memory-history provenance) — and the two anchor_change arms: current citation surfaces, stale range is enforced. Follow-up waves added the absent-at-stamp rule (construct added after the stamp: surfaced when current, enforced when stale, invalid when ambiguous now), the provenance-debt demotion arms (untouched document demotes, touched stays enforced, git failure fails closed, missing stamp never demotes). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
