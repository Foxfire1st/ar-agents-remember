# mcp/tests/test_atomic_write.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Atomic file publication, interruption cleanup and directory durability tests.

## Code Commentary

### Logic

Readers see the old complete destination until replacement; successful writes publish exact bytes without temp leftovers. Failed replacement and KeyboardInterrupt remove private temporary files. The helper fsyncs both file and directory, and cross-directory replacement flushes destination and source directories.

Two cases added by the `KS-R23` repair pin the failure vocabulary `atomic_replace` now carries, in `AtomicReplaceTests`: a post-rename directory-flush failure must raise `AtomicReplaceError` with `leg == "directory-fsync"` and `destination_state == "source-absent"`, and the case **reads the destination and the source path** to assert that state rather than trusting the label (the new bytes are published, the source is consumed); the other leg asserts a failed rename reports `leg == "replace"` with `destination_state == "previous-bytes"` and leaves the destination on its old bytes with the source still present. Both legs also assert the failure is still an `OSError` and now an `AgentsRememberError`.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Cancellation includes BaseException paths. Cross-directory durability matters for asset-spool promotion; a successful rename alone is not the asserted durability guarantee.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- It publishes the exact bytes and leaves no temp behind. [1]
- A reader never sees a partial file because the temp is private. [2]
- A failed replace removes the temp and leaves the destination alone. [3]
- Cancellation between write and replace also removes the temp. [4]
- The directory entry is flushed so a completed rename survives. [5]
- A cross directory rename flushes both. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
