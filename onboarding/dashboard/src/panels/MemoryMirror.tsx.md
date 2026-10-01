# dashboard/src/panels/MemoryMirror.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The memory mirror (mc2 harvest #2 — "a 1-to-1 mirror of the code"): a coverage/drift segmented bar
per repo + ledger currency + the stalest-sidecar leaderboard, all from the slice-3b analytics nodes
(maps onto `drift_check`).

## Code Commentary

### Logic

Since L15 the panel's served ages advance LOCALLY: the wire carries stable forms without the volatile *Seconds fields, so the panel derives display ages from per-object arrival anchors (data/servedAges.ts) refreshed by a 10-second useNowMs ticker — the deliberate, disclosed deviation from the no-re-render ideal that replaced the per-second whole-payload churn.

`driftSegments` turns a drift snapshot's counts into ordered `{cls,count,pct}` segments. The `segbar`
is a Panda `css()` flex track; each segment's colour comes from a **record** `SEG_BG[cls]` (not a
cva) because drift classifications are forward-compatible (an unanticipated class renders with no
fill). Actionable count toggles an `actionable` (amber) vs `muted` class. Ledger + stalest lists are
plain Panda rows.

### Invariants And Boundaries

Read-only analytics; the segmented bar reads left→right good→actionable (healthy classes first). All
ages are server-computed.

## Evidence

### Repo-Internal References

- `driftSegments` + the `DRIFT_ORDER`. [1]
- The drift/ledger/stalest analytics nodes. [2]
