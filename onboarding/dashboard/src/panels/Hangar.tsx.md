# dashboard/src/panels/Hangar.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Hangar displays pre-bound task worktrees and unbound enclosures from selectWorktrees, admitting only physical code or memory worktree existence. Bound entries use shared task status and exact opaque selection; it does not infer staleness from session state. Retained contracts without directories remain absent; reopened worktrees reappear only when they exist.

## Code Commentary

L23 renders an enclosure's optional lifecycle operation as one compact badge containing its kind,
status, phase, and the durable `currentCommand`. The command is not inferred from a process or
private job id: it is the plane-projected lifecycle-operation field. Badge text is forced onto one
line and clipped with CSS ellipsis inside a shrinkable bounded flex item; the full command remains
available through the badge's `title`. Absent operation state still renders no placeholder.

### Logic

Hangar renders task status and enclosure review, closeout, integration, cleanup and optional lifecycle-operation badges. It renders no served-age span and installs no age ticker.

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


- The running-operation regression proves the durable command is visible and preserved as the full badge title. [5]
