# mcp/tests/test_atomic_write.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_write.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489` |
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Atomic file publication, interruption cleanup and directory durability tests.

## Code Commentary

### Logic

Readers see the old complete destination until replacement; successful writes publish exact bytes without temp leftovers. Failed replacement and KeyboardInterrupt remove private temporary files. The helper fsyncs both file and directory, and cross-directory replacement flushes destination and source directories.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Cancellation includes BaseException paths. Cross-directory durability matters for asset-spool promotion; a successful rename alone is not the asserted durability guarantee.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| It publishes the exact bytes and leaves no temp behind. | `test_it_publishes_the_exact_bytes_and_leaves_no_temp_behind` | mcp/tests/test_atomic_write.py:32-38 |
| A reader never sees a partial file because the temp is private. | `test_a_reader_never_sees_a_partial_file_because_the_temp_is_private` | mcp/tests/test_atomic_write.py:40-57 |
| A failed replace removes the temp and leaves the destination alone. | `test_a_failed_replace_removes_the_temp_and_leaves_the_destination_alone` | mcp/tests/test_atomic_write.py:61-73 |
| Cancellation between write and replace also removes the temp. | `test_cancellation_between_write_and_replace_also_removes_the_temp` | mcp/tests/test_atomic_write.py:75-87 |
| The directory entry is flushed so a completed rename survives. | `test_the_directory_entry_is_flushed_so_a_completed_rename_survives` | mcp/tests/test_atomic_write.py:91-97 |
| A cross directory rename flushes both. | `test_a_cross_directory_rename_flushes_both` | mcp/tests/test_atomic_write.py:101-112 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
