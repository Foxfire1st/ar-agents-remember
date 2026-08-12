# dashboard/src/panels/Hangar.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Hangar.tsx`                |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T10:50+02:00                           |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`       |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The hangar (notes 01/06): persistent worktree-backed lifecycles are NEVER auto-reaped — when they
rot, this surfaces the staleness for the developer to step in (the TTL reaper is fleeting-only). It lists
only **LIVE** worktree enclosures: a finalized worktree keeps its enclosure contract on disk (it records
the landed state for memory lineage) even after its directory is reaped, so the raw enclosure set only
ever grows. Since 260703-L11 "live" means the projection's stat'ed worktree-existence truth
(`hasLiveWorktree`: `codeWorktreeExists || memoryWorktreeExists`), never a cleanup-state proxy — the
count reflects worktrees that physically exist / still need action, and a reopened contract
(`cleanup: reopened`, worktrees gone) stays hidden until `worktree_start` recreates them.

## Code Commentary

L23 renders an enclosure's optional lifecycle operation as one compact badge containing its kind, status, and phase. Absent operation state still renders no placeholder.

### Logic

Since L15 the panel's served ages advance LOCALLY: the wire carries stable forms without the volatile *Seconds fields, so the panel derives display ages from per-object arrival anchors (data/servedAges.ts) refreshed by a 10-second useNowMs ticker — the deliberate, disclosed deviation from the no-re-render ideal that replaced the per-second whole-payload churn.

First **filters to enclosures whose worktrees physically exist**, then lists the rest (sorted) with
closeout/integration/cleanup `badge`s + the cross-ref lifecycle's staleness. The filter is the shared
`hasLiveWorktree` selector (`data/selectors.ts`): `rows =
Object.values(enclosures).filter(hasLiveWorktree).sort(...)` — true when `codeWorktreeExists ||
memoryWorktreeExists`, the flags the snapshots I/O layer stats onto `EnclosureNode` (260703-L11). This
replaced the earlier `ARCHIVED_CLEANUP = {completed, abandoned}` cleanup-state proxy, which
`task_reopen`'s `cleanup: reopened` outflanked (a reopened contract has no worktrees on disk yet rendered
as live): completed/abandoned enclosures still drop out (their worktrees were reaped), and a reopened
contract stays hidden until `worktree_start` recreates its worktrees. The `Panel` title and the empty
state both read off the filtered `rows`: `Hangar · {rows.length} worktrees`, and "Hangar empty — no live
persistent worktrees." when none remain. `isStale` (cleanup pending / integration completed / inferred
lifecycle) toggles the `row` `cva`'s `stale` boolean variant (amber border). A captured `lifecycleId`
guards the ghost open button. When the bound lifecycle has a worktree-bound gate (`closeout` / `push` /
`integration` / `cleanup`), the actions row renders compact `GateResponder`; otherwise enclosure actions
remain display-only `Affordance`s.

### Invariants And Boundaries

Reflects the enclosure node statuses, not a recomputation. The existence filter is **display-only**:
it hides worktree-less enclosures from the list and count but never deletes their on-disk contract
(the durable record stays for memory lineage), and it never infers existence client-side — the flags are
server-stat'ed. Non-gate affordances remain read-only. Gate responses are
instructional chat injections through `GateResponder`, not enclosure status mutation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `EnclosureNode` statuses (closeout/integration/cleanup) and existence flags shown/filtered on. | `EnclosureNode` | mcp/src/agents_remember/observer/projection.py:141-172 |
| The shared `hasLiveWorktree` tasks-surface visibility rule. | `hasLiveWorktree` | dashboard/src/data/selectors.ts:24-28 |
| The shared chat-routed gate responder. | `GateResponder` | dashboard/src/panels/GateResponder.tsx:720-780 |
| The render tests pinning existence-only visibility (reopened hidden, visible again after restart, completed/abandoned gone). | "renders a row ONLY while a worktree physically exists — never from a cleanup-state proxy"; "hides a reopened contract with no worktrees on disk (reset-awaiting-restart"; "shows a reopened leaf again once worktree_start recreates its worktrees"; "fully reduces to the empty state once every worktree is physically gone" | dashboard/src/panels/Hangar.test.tsx:37-71; dashboard/src/panels/Hangar.test.tsx:73-93; dashboard/src/panels/Hangar.test.tsx:95-113; dashboard/src/panels/Hangar.test.tsx:115-138 |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-04T17:54+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 2 citation rows with exact anchors (GateResponder definition, quoted Hangar render-test names) and ledger-verified ranges; widened the EnclosureNode citation to its complete class extent (statuses + existence flags). Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-07T10:50+02:00 — L15: served ages advance locally (servedAges anchors + 10s ticker); volatile fields no longer arrive on the wire. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:28+02:00 — 260703-L15 S1: the row staleness readout now advances locally —
  `fmtWait(servedAgeSeconds(lifecycle, lifecycle?.staleSeconds, nowMs))` with a panel-level
  `useNowMs()` (10 s tick). The change gate stopped re-serving nodes whose only movement is
  their age, so the served value is an anchor, not a live feed.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T02:25+02:00 — 260703-L11: visibility flipped from the `ARCHIVED_CLEANUP` cleanup-state
  proxy to worktree-existence truth — rows filter through the shared `hasLiveWorktree` selector over the
  new `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags, so a reopened contract
  (`cleanup: reopened`, no worktrees) stays hidden until `worktree_start` recreates its worktrees while
  completed/abandoned stay hidden as before. Verification metadata pinned until closeout stamps the L11
  commit.
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
