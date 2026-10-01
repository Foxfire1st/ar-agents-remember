# dashboard/src/panels/review/MarkerTargetState.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**Where an unknown membership's `Attribution unknown` state is shown (2 cases; ruling Q3).** The payload is the real
review of INV-Z66EMHMH on comparison 3 (`markerUnknown.memberUnknown.captured.json`) and the target is the real
before-side occurrence of its FAM-4V4GSQCS membership (`markerUnknown.file.captured.json`); the one derived body drops
the review's family entries, as a review that composed no family has none.

## Code Commentary

### Logic

- **Case 1.** `MemberTargetNote` marks only the member row of the named family and revision; another row and another
  subject show nothing.
- **Case 2.** When the named family is not in the review's context, `MemberFamilyLabel` shows the state on the
  invariant view (mutation Q3-6).

### Conventions

- `inScope` mounts inside a scope value holding the real target.

### Invariants And Boundaries

- Part of the proof of the candidate invariant recorded on `MarkerTargetState.tsx.md`.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The real payload and target. [1]
- The two cases. [2]
- The components under test. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
