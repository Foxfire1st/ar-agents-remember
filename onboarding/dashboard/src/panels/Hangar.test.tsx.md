# dashboard/src/panels/Hangar.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Hangar.test.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-30                                       |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render tests for `Hangar` (Operations Integration L5): they pin the **live-only** contract — the
hangar must hide archived (cleanup `completed` / `abandoned`) enclosures so its count reflects worktrees
that physically exist, not the ever-growing set of finalized enclosure contracts left on disk for memory
lineage. The tests drive the panel through the real `dashboardStore` (the hangar reads `enclosures` /
`lifecycles` from the store), so they cover the filter end-to-end at the render layer.

## Code Commentary

### Logic

A local `enclosure(partial)` factory builds a full `EnclosureNode` from a minimal `{ enclosure }` plus
overrides, defaulting `cleanup: "pending"` (i.e. a live worktree) so a case only sets `cleanup` to mark a
row archived. `afterEach` runs `cleanup()` and `dashboardStore.getState().reset()` so cases don't leak
state. Two cases:

1. **Hides archived, counts only live** — seeds three enclosures (`live` `cleanup: "pending"`, `done`
   `cleanup: "completed"`, `gone` `cleanup: "abandoned"`) with empty `lifecycles`, renders
   `<Hangar onSelect={vi.fn()} />`, and asserts exactly one `hangar-row` survives and the `hangar` panel
   title reads `Hangar · 1 worktrees` — proving the two archived rows are dropped from both the list and
   the count.
2. **Reduces to the empty state when everything is archived** — seeds two `cleanup: "completed"`
   enclosures, asserts zero `hangar-row`s and that the empty text `/no live persistent worktrees/i`
   renders.

### Invariants And Boundaries

Render + store state only; no backend, no gate posting, no WebSocket. The test treats the archived filter
as display-only: it seeds enclosure contracts and asserts they are *hidden*, never that they are deleted.
The cleanup-status semantics themselves (what `completed` / `abandoned` mean) are owned by the
observer/projection layer, not asserted here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test (filters `ARCHIVED_CLEANUP` cleanup states out of the rows). | — | [Hangar.tsx](Hangar.tsx) |
| The dashboard store the test seeds `enclosures` / `lifecycles` into and resets between cases. | — | [data/store.ts](../data/store.ts) |
| The `EnclosureNode` shape (incl. `cleanup`) the `enclosure(...)` factory fills. | — | [types/projection.ts](../types/projection.ts) |

## Update History

- 2026-06-30T00:00:00+02:00 — Operations Integration L5: created — render tests pinning that the hangar hides archived
  (cleanup completed/abandoned) enclosures so the row count reflects live worktrees, and fully reduces to
  the "no live persistent worktrees" empty state when every enclosure is archived. Verification metadata
  pinned until closeout stamps the L5 commit.
