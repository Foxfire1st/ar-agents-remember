# dashboard/src/data/intentEntryRevalidation.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/intentEntryRevalidation.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:15:39+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` |
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

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

## Docs References

No Domain Documentation source is configured for this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Why no existing signal can carry a knowledge write, and the three re-validation points. | "change watcher deliberately excludes" | dashboard/src/data/intentEntryRevalidation.tsx:1-20 |
| The provider: the show transition derived during render, and `revalidate`. | `IntentEntryRevalidation`; `state.shown !== shown`; `revalidate` | dashboard/src/data/intentEntryRevalidation.tsx:29-54 |
| The no-provider default and the two hooks. | `NO_REVALIDATION`; `useIntentEntryGeneration`; `useRevalidateIntentEntry` | dashboard/src/data/intentEntryRevalidation.tsx:26-26; dashboard/src/data/intentEntryRevalidation.tsx:57-58; dashboard/src/data/intentEntryRevalidation.tsx:61-62 |
| The cockpit wraps its shell with `shown` = Operations view and no takeover. | `IntentEntryRevalidation` | dashboard/src/cockpit/Cockpit.tsx:912-912 |
| The reviewer's refresh calls `revalidate`. | `useRevalidateIntentEntry`; `revalidateEntry()` | dashboard/src/panels/review/ReviewRefresh.tsx:58-58 |
| The summary's facts carry the generation. | `useIntentEntryGeneration` | dashboard/src/panels/detail-panel/changeSetBar.tsx:315-365 |
| The cases: re-show, open once, leave the reviewer, reviewer refresh. | "(a) re-validates when the task detail is shown again, once per showing, with no catalogue read"; "(c) re-validates when the reviewer's own refresh runs" | dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:213-232; dashboard/src/cockpit/Cockpit.intentEntry.test.tsx:266-280 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `dashboard/src/cockpit/Cockpit.tsx` (two imports, the `knowledge` destination, the reader-hash initial view and the `ViewBody` case), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.

- 2026-09-28T17:06:50+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the entry re-validation context added in L47-A3 under the 16:27:28 ruling on L47-R1-F2. The verification pair names the code base; closeout owns the real stamp.
