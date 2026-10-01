# dashboard/src/panels/review/markerNavigation.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The workspace's moves for an intent marker (4 cases).** Recording stand-ins for the workspace state's setters and the
navigation's `onSelect` show exactly what a follow selects and what a return restores, in order. Added because the
real review's default selection coincided with the target and let mutation M8 escape.

## Code Commentary

### Logic

- **Following (2).** The invariant's own review at its member row of the named family (`onSelect` with
  `{ kind: 'invariant', id }` and `{ familyId, memberRevisionId }`, after `setOpenPath null`); the invariant alone when
  no family records it.
- **The return (2).** The subject and family, then the lane, the opened file, the layout and the full-file choice, with
  the tree's focus request cleared; without navigation the family selection is restored directly.

### Conventions

- `workspace()` and `navigation()` record each call as a line.

### Invariants And Boundaries

- Pins ICR-R34 rules 2 and 3's workspace moves (mutation M8).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Following a marker. [1]
- The return. [2]
- The moves under test. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
