# dashboard/src/panels/lifecycle-list/signals.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The Operations row/page coherence suite pins one served task status word and host-event age across native deltas, with no status borrowed from attention severity. Retired independent lifecycle/gate/inbox signal assertions are not current coverage.

## Code Commentary

### Logic

Native row/page deltas require shared stage/activity words, unchanged attention severity and distinct paused/aborted marks. Fake host timestamps retain age through later mounts and deltas. Hidden/inactive/nested owners stop aging; visible dependents share one clock and clean it up. Parameterized dependency pages and 30/150-task rails are real source ranges, not named symbols.

### Invariants And Boundaries

Task status is shared across row, page and dependencies; attention remains a separate severity lane. These mounted/fake-time assertions cover timer ownership and cleanup, not native host-state acquisition, real elapsed-time performance or backend activity derivation.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The Operations-signals suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
