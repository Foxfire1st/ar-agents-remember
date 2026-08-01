# dashboard/src/grammar/Affordance.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Affordance.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T15:10+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `ActionAvailability` shape rendered (enabled / disabledReason / nextSafeAction). | L36-L49 | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-08-01T15:10+02:00 — 260731-EFA-L4 curator (citation pass): repaired the
  `observer/projection.py` citation. `L26-L33` → `L36-L49`; read there: `class ActionAvailability`
  (L36), `enabled` (L47), `disabledReason` (L48), `nextSafeAction` (L49). The old range was short
  as well as drifted — shifting it alone would have stopped before all three fields the finding
  names, so the end was widened to the class's last field rather than merely moved. No body claim
  changed.

- 2026-06-15T17:00 — Created for slice 5d: `Affordance` migrated to a Panda `cva` (was `.afford--*`).
  Verification metadata pinned until closeout stamps the 5d code commit.
