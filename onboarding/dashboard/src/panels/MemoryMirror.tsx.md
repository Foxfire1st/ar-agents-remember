# dashboard/src/panels/MemoryMirror.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/MemoryMirror.tsx`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T10:50+02:00                           |
| lastVerifiedCommitHash | `2597ff98306ba7c7963005092ac597c4972e63ce`       |
| lastVerifiedCommitDate | 2026-08-18T15:45:32+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `driftSegments` + the `DRIFT_ORDER`. | `driftSegments` | dashboard/src/data/selectors.ts:178-186 |
| The drift/ledger/stalest analytics nodes. | `Analytics` | mcp/src/agents_remember/observer/projection.py:1097-1153 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 2 citation items; scoped citation check now passes.

- 2026-07-07T10:50+02:00 — L15: served ages advance locally (servedAges anchors + 10s ticker); volatile fields no longer arrive on the wire. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:32+02:00 — 260703-L15 S1: both age readouts now advance locally —
  `servedAgeSeconds(snapshot, snapshot.snapshotStaleSeconds, nowMs)` for drift rows and
  `servedAgeSeconds(sidecar, sidecar.ageSeconds, nowMs)` for the stalest-sidecar leaderboard,
  with a panel-level `useNowMs()` (10 s tick); the header comment's "server-computed" ages became
  "server-anchored, client-advanced".
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-06-15T17:00 — Created for slice 5d: migrated onto `Panel` + Panda css (segments by record).
  Verification metadata pinned until closeout stamps the 5d code commit.
