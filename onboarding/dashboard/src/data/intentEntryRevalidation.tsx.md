# dashboard/src/data/intentEntryRevalidation.tsx

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

Decides **when the task entry's Intent review counts are re-validated** (leaf `260921-ICR-L47`, the
Architect's ruling of 2026-09-28T16:27:28+02:00 on L47-R1-F2). No signal the dashboard receives moves when
a leaf's knowledge is generated or published: the candidate and the published dataset live under the
worktree group and the memory root, which the change watcher deliberately excludes, and no projection field
or delta carries a knowledge fact. So the entry re-validates where the developer looks at it again, and a
displayed count is never older than the developer's last navigation to it.

## Code Commentary

### Logic

`IntentEntryRevalidation({ shown, children })` provides one number, the entry's re-validation
generation, through React context:

- **re-show** — when `shown` turns true (a view switch back to Operations, or a takeover such as the
  reviewer closing back to the entry), the generation increments. The transition is derived **during
  render** (adjust-state-in-render), so a task change and a visibility change that arrive together cost
  one read, not one per commit;
- **reviewer refresh** — `revalidate()` increments it; `panels/review/ReviewRefresh.tsx` calls it after
  the reviewer's own refresh;
- **task open** needs nothing here: the entry mounts, or its task props change, and reads.

`useIntentEntryGeneration()` reads the number; `useRevalidateIntentEntry()` returns `revalidate`.
Without a provider the generation is 0 and `revalidate` does nothing.

### Conventions

Local React state shared through context. It is explicitly **not** an event system and not a projection:
the ruling forbade widening the watcher or projector for this repair.

### Invariants And Boundaries

- Only the Intent review summary is keyed on the generation (`panels/detail-panel/changeSetBar.tsx`
  appends it to the summary's facts); the change-set reads and the reviewer's catalogue key are not.
- Each trigger costs exactly one summary read (review R2 measured this in a real browser).
- A live push of a first ingest while the same panel stays open is **not** provided; the ruling records it
  as a possible later enhancement.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- Why no existing signal can carry a knowledge write, and the three re-validation points. [1]
- The provider: the show transition derived during render, and `revalidate`. [2]
- The no-provider default and the two hooks. [3]
- The cockpit wraps its shell with `shown` = Operations view and no takeover. [4]
- The reviewer's refresh calls `revalidate`. [5]
- The summary's facts carry the generation. [6]
- The cases: re-show, open once, leave the reviewer, reviewer refresh. [7]

### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.
