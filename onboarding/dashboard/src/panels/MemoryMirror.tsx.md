# dashboard/src/panels/MemoryMirror.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The memory mirror (mc2 harvest #2 — "a 1-to-1 mirror of the code"): a coverage/drift segmented bar per repo and ledger currency, read from `analytics.driftSnapshots` and `analytics.ledgers`. It presents drift reporting, not an exposed `drift_check` tool; the retired stalest-sidecar leaderboard is neither selected nor rendered.

## Code Commentary

### Logic

Since L15 the panel's served ages advance LOCALLY: the wire carries stable forms without the volatile *Seconds fields, so the panel derives display ages from per-object arrival anchors (data/servedAges.ts) refreshed by a 10-second useNowMs ticker — the deliberate, disclosed deviation from the no-re-render ideal that replaced the per-second whole-payload churn.

`driftSegments` turns a drift snapshot's counts into ordered `{cls,count,pct}` segments. The `segbar`
is a Panda `css()` flex track; each segment's colour comes from a **record** `SEG_BG[cls]` (not a
cva) because drift classifications are forward-compatible (an unanticipated class renders with no
fill). Converted repositories report `stale` anchors and validator `violation`s; they read like their
legacy counterparts (amber and alarm). Actionable count toggles an `actionable` (amber) vs `muted`
class. Ledger currency uses plain Panda rows.

### Invariants And Boundaries

Read-only analytics; the segmented bar reads left→right good→actionable (healthy classes first). Ages are server/arrival-anchored and advance locally through `servedAgeSeconds` and `useNowMs`; this display progression grants no mutation authority.

## Evidence

### Repo-Internal References

- `driftSegments` + the `DRIFT_ORDER`. [1]

- The panel reads only driftSnapshots and ledgers from Analytics; the retired stalest-sidecar list is not rendered. [2]



- Converted stale and violation segments read like their legacy counterparts. [3]

- The Memory mirror renders the retained `driftSnapshots` classification-count bars and the ledger-currency list only. Its two-collection empty check shows “No memory analytics yet.” only when both are empty. Segment ordering and forward-compatible color lookup survive, including converted `stale`/`violation`; displayed drift ages stay server/arrival-anchored and advance locally. No panel call recreates the retired stamp-age leaderboard or confers mutation authority. [4]
