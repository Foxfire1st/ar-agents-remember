# dashboard/src/panels/MemoryMirror.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/MemoryMirror.tsx`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-15T17:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The memory mirror (mc2 harvest #2 — "a 1-to-1 mirror of the code"): a coverage/drift segmented bar
per repo + ledger currency + the stalest-sidecar leaderboard, all from the slice-3b analytics nodes
(maps onto `drift_check`).

## Code Commentary

### Logic

`driftSegments` turns a drift snapshot's counts into ordered `{cls,count,pct}` segments. The `segbar`
is a Panda `css()` flex track; each segment's colour comes from a **record** `SEG_BG[cls]` (not a
cva) because drift classifications are forward-compatible (an unanticipated class renders with no
fill). Actionable count toggles an `actionable` (amber) vs `muted` class. Ledger + stalest lists are
plain Panda rows.

### Invariants And Boundaries

Read-only analytics; the segmented bar reads left→right good→actionable (healthy classes first). All
ages are server-computed.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `driftSegments` + the `DRIFT_ORDER`. | L142-L161 | [data/selectors.ts](../data/selectors.ts) |
| The drift/ledger/stalest analytics nodes. | — | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |

## Update History

- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda css (segments by record).
  Verification metadata pinned until closeout stamps the 5d code commit.
