# dashboard/src/grammar/Affordance.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Affordance` is the **display-only** action affordance: it renders one `ActionAvailability` as a
ready/disabled pill carrying the reducer's precomputed reason. It never mutates — slice 06 wires the
POST enforcement.

## Code Commentary

### Logic

A Panda `cva` with a `tone` variant (`ready` cyan / `off` grey). Uses `aria-disabled="true"` (not the
`disabled` attribute) so the `title` tooltip still shows and the node stays announced; the `title` is
`nextSafeAction`/`disabledReason`. No `onClick`.

### Invariants And Boundaries

Read-only by contract (no POST). The enabled/disabled decision + reason come from the server-side
reducer's `ActionAvailability`, never recomputed here.

## Evidence

### Repo-Internal References

- The `ActionAvailability` shape rendered (enabled / disabledReason / nextSafeAction). [1]
