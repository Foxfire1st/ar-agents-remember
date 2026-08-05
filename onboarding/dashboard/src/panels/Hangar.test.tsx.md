# dashboard/src/panels/Hangar.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Hangar.test.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-06T02:30+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render tests for `Hangar` (260703-L11): they pin the **worktree-existence** visibility contract —
a row renders ONLY while a worktree physically exists (`hasLiveWorktree` over the projection's stat'ed
`codeWorktreeExists`/`memoryWorktreeExists`), never from a cleanup-state proxy. That covers the L9-reopen
defect (a `cleanup: reopened` contract with no worktrees rendered as live under the old
`ARCHIVED_CLEANUP` proxy) plus the as-before hiding of completed/abandoned enclosures whose worktrees
were reaped. The tests drive the panel through the real `dashboardStore` (the hangar reads `enclosures` /
`lifecycles` from the store), so they cover the filter end-to-end at the render layer.

## Code Commentary

### Logic

A local `enclosure(partial)` factory builds a full `EnclosureNode` from a minimal `{ enclosure }` plus
overrides, defaulting `cleanup: "pending"` **and** `codeWorktreeExists: true` / `memoryWorktreeExists:
true` (a live worktree), so a case only overrides the existence flags (and cleanup label) to mark a row
gone. `afterEach` runs `cleanup()` and `dashboardStore.getState().reset()` so cases don't leak state.
Four cases:

1. **Existence-only filter** — seeds a live enclosure, a memory-only one (`codeWorktreeExists: false`,
   `memoryWorktreeExists: true` — either side admits), and completed + abandoned ones with both flags
   false: exactly two `hangar-row`s survive and the panel title reads `Hangar · 2 worktrees`.
2. **Reopened-no-worktree hidden** — a `cleanup: "reopened"` enclosure with both flags false renders
   zero rows + the empty state: a reopened contract is a reset awaiting restart, not live work.
3. **Reopened-after-restart visible** — the same reopened contract with existence flags true renders
   again: existence, not the cleanup label, re-admits the row.
4. **Empty state** — every enclosure's worktrees physically gone → zero rows and the
   `/no live persistent worktrees/i` text.

### Invariants And Boundaries

Render + store state only; no backend, no gate posting, no WebSocket. The test treats the existence filter
as display-only: it seeds enclosure contracts and asserts they are *hidden*, never that they are deleted.
The existence flags themselves are server-stat'ed truth owned by the observer/projection layer
(`snapshots._enclosure_from_contract`); the tests only assert the client filters on them.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component under test (filters rows through `hasLiveWorktree`). | `Hangar` | dashboard/src/panels/Hangar.tsx:72-138 |
| The shared existence-truth visibility selector. | `hasLiveWorktree` | dashboard/src/data/selectors.ts:24-28 |
| The dashboard store the test seeds `enclosures` / `lifecycles` into and resets between cases. | `dashboardStore` | dashboard/src/data/store.ts:225-347 |
| The `EnclosureNode` shape (incl. `codeWorktreeExists`/`memoryWorktreeExists`) the `enclosure(...)` factory fills. | `EnclosureNode` | dashboard/src/types/projection.ts:133-150 |

## Update History

- 2026-08-03T02:31:31+02:00 — W3-B05 curator: anchored 4 Tier-2 table citations with exact source paths; fixer generated all ranges.

- 2026-07-06T02:30+02:00 — 260703-L11: rewritten from the archived-cleanup proxy contract to the
  worktree-existence contract — the factory defaults the new existence flags true, and the four cases
  pin existence-only filtering (either worktree admits), reopened-no-worktree hidden,
  reopened-after-restart visible again, and the all-gone empty state. Verification metadata pinned until
  closeout stamps the L11 commit.
- 2026-06-30T00:00:00+02:00 — Operations Integration L5: created — render tests pinning that the hangar hides archived
  (cleanup completed/abandoned) enclosures so the row count reflects live worktrees, and fully reduces to
  the "no live persistent worktrees" empty state when every enclosure is archived. Verification metadata
  pinned until closeout stamps the L5 commit.
