# dashboard/src/data/intentEntryRevalidation.tsx

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

Decides **when the task entry's Intent review counts are re-validated** (leaf `260921-ICR-L47`, the
Architect's ruling of 2026-09-28T16:27:28+02:00 on L47-R1-F2). The original navigation-and-refresh approach predated scoped memory watching. The provider still owns only a shared generation: showing the detail again and explicit reviewer refresh advance it, while an active live reviewer now also advances it through matching memory notifications on the existing state SSE stream. Initial and reconnect baselines reconcile too. Revalidation requests a read; it does not guarantee that a pending or failed read has produced fresh counts.

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
- **live memory notification** — `useReviewMemoryWatch` calls the same callback alongside review invalidation/refresh for the exact registered repo/master/leaf. Registration requires an active live enclosure and excludes recorded history; matching initial/reconnect baselines also reconcile;
- **task open** needs nothing here: the entry mounts, or its task props change, and reads.

`useIntentEntryGeneration()` reads the number; `useRevalidateIntentEntry()` returns `revalidate`.
Without a provider the generation is 0 and `revalidate` does nothing.

### Conventions

Local React state shared through context. This provider installs no watcher and defines no projection field. Its current live caller consumes scoped memory events from the existing state stream; the earlier ruling describes the original navigation repair.

### Invariants And Boundaries

- `DocChangeSetBar` appends generation to the Intent entry's facts; `IntentReviewEntry` passes those facts to `useIntentReviewSummary`. `ChangeSetButton` also reads generation and includes it in its load effect dependencies. Both behaviors already exist in BASE. The reviewer catalogue does not consume this context directly; it can refresh separately when an observed comparison generation changes.
- Review R2's reported browser measurement is historical. The stored test bodies assert summary counts for navigation, task opening, reviewer return and explicit refresh; they do not establish a universal one-request guarantee for memory events or reconnects. No new execution is reported here.

  Historical prior browser account, not a current per-notification guarantee:

  ```text
  - Each trigger costs exactly one summary read (review R2 measured this in a real browser).
  ```
- Live memory revalidation requires a mounted reviewer with an active live scope. An entry shown without that registration still relies on navigation or explicit refresh; closed and recorded reviews do not register. Unchanged subsequent memory revisions are quiet, while initial/reconnect baselines reconcile.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured for this module.

No relevant domain documentation was found.

### Repo-Internal References

- The provider: the show transition derived during render, and `revalidate`. [2]
- The no-provider default and the two hooks. [3]
### Cross-Repo References

No cross-repository behavior.

No meaningful cross-repo references found.

- The local provider increments generation on a false-to-true shown transition and on revalidate. useReviewMemoryWatch registers only for an active live enclosure and non-recorded history, invokes shared entry revalidation alongside review invalidation/refresh, and filters notifications by exact registered scope. publishReviewMemory reconciles first/initial baselines and changed revisions. connectState carries that scope and dispatches memory events through its existing SSE connection. The original header-only no-signal account is superseded. [1]



- The cockpit shell wraps its body in `IntentEntryRevalidation`, shown true for the Operations view only while neither a takeover nor the in-grid review page is showing.



- DocChangeSetBar appends context generation to leaf facts and passes them to LeafEntries; IntentReviewEntry passes facts to useIntentReviewSummary, whose key/effect includes facts. ChangeSetButton separately consumes the same generation in its load effect dependencies. Generation is not a summary-only input.

Retired at the fifth freeze d59c3493: dashboard/src/panels/detail-panel/changeSetBar.tsx:83-108 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 04729d84383a6787afe84ed33183fdc457a20f6e. Retired means the anchor no longer stands, not that the cited subject was deleted [6]

- The current stored test bodies assert summary-read counts and catalogue isolation for re-show/task switching, opening from another view, reviewer return and explicit refresh. These are static assertions, not new execution or proof of memory-event/reconnect request counts. Both former target ranges are replaced by the current complete scenario extents. [7]

- ReviewRefresh obtains the shared entry revalidation callback, and its actual button onClick calls onRefresh followed by revalidateEntry. The callback declaration alone is not the invocation witness. [5]

- Retired at the fifth freeze d59c3493: dashboard/src/cockpit/Cockpit.tsx:804-841 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit a414bf4725215f2cf236d6d492bc070a973bce08. Retired means the anchor no longer stands, not that the cited subject was deleted.

## Retirements

- Retired at the fifth freeze d59c3493: dashboard/src/panels/detail-panel/changeSetBar.tsx:83-108 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 04729d84383a6787afe84ed33183fdc457a20f6e. Retired means the anchor no longer stands, not that the cited subject was deleted.