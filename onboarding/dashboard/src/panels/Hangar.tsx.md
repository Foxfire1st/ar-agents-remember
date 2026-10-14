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

Available enclosure actions render display-only `Affordance` entries. No GateResponder or durable gate-response interaction is mounted. The existing progress text, CSS-ellipsized current command and full-value title retain their actual projection boundary.

### Invariants And Boundaries

Reflects the enclosure node statuses, not a recomputation. The existence filter is **display-only**:
it hides worktree-less enclosures from the list and count but never deletes their on-disk contract
(the durable record stays for memory lineage), and it never infers existence client-side — the flags are
server-stat'ed. All retained enclosure action affordances are display-only/read-only.
There is no GateResponder, gate-response chat injection or enclosure status mutation here.
Long operation commands must remain single-line and bounded. Do not replace the ellipsis/title pair
with a one-time string-length truncation because the available width changes with neighboring
badges and viewport size.

## Evidence

### Repo-Internal References

- The `EnclosureNode` statuses (closeout/integration/cleanup) and existence flags shown/filtered on. [1]
- The shared `hasLiveWorktree` tasks-surface visibility rule. [2]
- The render tests pinning existence-only visibility (reopened hidden, visible again after restart, completed/abandoned gone). [4]
- The running-operation regression proves the durable command is visible and preserved as the full badge title. [5]
