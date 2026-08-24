# mcp/tests/test_observer_projection_taskdocs.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_observer_projection_taskdocs.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_observer_projection_taskdocs.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `TaskDocumentsReaderTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_observer_projection_taskdocs.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## L23 Final Candidate Disposition

Projection tests bind the latest validated lifecycle operation to canonical task documents and
expose bounded phase/report evidence. Private worker, lease, recovery, and resume coordinates never
enter the observer packet.

## 260821-CLIVE-L2 Addressable Task-Document Projection Fixtures

Task-document projection tests now write addressable contracts through one helper that publishes
the locator and immutable manifest. Planning/task truth remains task-document-owned, while optional
lifecycle attachment is discovered through the enclosure-root address chain.

| Finding | Source |
| --- | --- |
| The helper publishes the normal lifecycle location after contract publication. | mcp/tests/test_observer_projection_taskdocs.py:48-58 |
| Lifecycle-attached task-document cases all use the addressable helper. | mcp/tests/test_observer_projection_taskdocs.py:294-364 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces task-document observer projection for hierarchy, graph, route reviews, closeout projection problems, execution registrations, and discarded-subtask history.

### Current Invariants

- Observer output is a read-only projection of canonical task and projection facts.
- Discard audit/proof remains visible after the live child files are removed.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-20T05:14+02:00 — 260815-DAG-L14: the suite gains
  `test_projects_sprint_master_ref_rows_and_seats` and
  `test_body_revision_covers_sprint_structure` (projected `masterRef`/`seats` with defaults filled,
  non-sprint docs staying empty, and bodyRevision movement across seats-only and masterRef-row
  edits). Verified at code commit 9c3180c1.

- 2026-08-14T06:38+02:00 — L23 final candidate review: projection tests attach the latest validated
  task-addressed operation and canonical task hierarchy while excluding private worker/recovery
  identity. Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
