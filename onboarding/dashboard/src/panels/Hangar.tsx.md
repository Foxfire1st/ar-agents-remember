# dashboard/src/panels/Hangar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Hangar.tsx`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-23T13:45+02:00                           |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`       |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The hangar (notes 01/06): persistent worktree-backed lifecycles are NEVER auto-reaped — when they
rot, this surfaces the staleness for the developer to step in (the TTL reaper is fleeting-only). It lists
only **LIVE** worktree enclosures: a finalized worktree keeps its enclosure contract on disk (it records
the landed state for memory lineage) even after its directory is reaped, so the raw enclosure set only
ever grows; the hangar hides the archived ones so the count reflects worktrees that physically exist /
still need action.

## Code Commentary

### Logic

First **filters out archived enclosures**, then lists the rest (sorted) with
closeout/integration/cleanup `badge`s + the cross-ref lifecycle's staleness. A module-level
`ARCHIVED_CLEANUP = new Set(["completed", "abandoned"])` and `isArchived(enclosure)` (true when
`enclosure.cleanup` is in that set) drive the filter: `rows = Object.values(enclosures).filter((e) =>
!isArchived(e)).sort(...)`. A completed/abandoned cleanup means there is no worktree left to integrate,
clean up, or rot — so it is dropped (this fixes the bug where finalized enclosure contracts piled up
forever, e.g. 31 shown when only a couple were live). The `Panel` title and the empty state both read off
the filtered `rows`: `Hangar · {rows.length} worktrees`, and "Hangar empty — no live persistent
worktrees." when none remain. `isStale` (cleanup pending / integration completed / inferred lifecycle)
toggles the `row` `cva`'s `stale` boolean variant (amber border). A captured `lifecycleId` guards the
ghost open button. When the bound lifecycle has a worktree-bound gate (`closeout` / `push` / `integration`
/ `cleanup`), the actions row renders compact `GateResponder`; otherwise enclosure actions remain
display-only `Affordance`s.

### Invariants And Boundaries

Reflects the enclosure node statuses, not a recomputation. The archived-cleanup filter is **display-only**:
it hides completed/abandoned enclosures from the list and count but never deletes their on-disk contract
(the durable record stays for memory lineage). Non-gate affordances remain read-only. Gate responses are
instructional chat injections through `GateResponder`, not enclosure status mutation.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `EnclosureNode` statuses (closeout/integration/cleanup) shown. | — | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The shared chat-routed gate responder. | — | [GateResponder.tsx](GateResponder.tsx) |
| The render test pinning that archived (completed/abandoned) enclosures are filtered out so the count reflects live worktrees. | L34-L67 | [Hangar.test.tsx](Hangar.test.tsx) |

## Update History

- 2026-06-30T00:00:00+02:00 — Operations Integration L5: the hangar now **filters out archived enclosures** —
  a module-level `ARCHIVED_CLEANUP = new Set(["completed", "abandoned"])` + `isArchived(e)` (true when
  `e.cleanup` is in that set) gate the rows (`Object.values(enclosures).filter((e) => !isArchived(e))
  .sort(...)`), and the empty text became "Hangar empty — no live persistent worktrees." A finalized
  worktree keeps its enclosure contract on disk, so the raw set only grows; hiding completed/abandoned
  ones makes the count reflect physical worktrees (fixes finalized contracts piling up, e.g. 31 shown
  when only a couple were live). Display-only — the contract is never deleted. Added a `Hangar.test.tsx`
  reference. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-23T13:45+02:00 — Task 11: rows with a bound worktree gate now render compact
  `GateResponder` instead of inert gate-like affordances; non-gate action availability still renders
  through `Affordance`. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda css/cva (local `badge`).
  Verification metadata pinned until closeout stamps the 5d code commit.
