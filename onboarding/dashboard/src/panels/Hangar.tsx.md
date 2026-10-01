# dashboard/src/panels/Hangar.tsx

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

L23 renders an enclosure's optional lifecycle operation as one compact badge containing its kind,
status, phase, and the durable `currentCommand`. The command is not inferred from a process or
private job id: it is the plane-projected lifecycle-operation field. Badge text is forced onto one
line and clipped with CSS ellipsis inside a shrinkable bounded flex item; the full command remains
available through the badge's `title`. Absent operation state still renders no placeholder.

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
Long operation commands must remain single-line and bounded. Do not replace the ellipsis/title pair
with a one-time string-length truncation because the available width changes with neighboring
badges and viewport size.

## Evidence

### Repo-Internal References

- The `EnclosureNode` statuses (closeout/integration/cleanup) and existence flags shown/filtered on. [1]
- The shared `hasLiveWorktree` tasks-surface visibility rule. [2]
- The shared chat-routed gate responder. [3]
- The render tests pinning existence-only visibility (reopened hidden, visible again after restart, completed/abandoned gone). [4]
- The running-operation regression proves the durable command is visible and preserved as the full badge title. [5]
