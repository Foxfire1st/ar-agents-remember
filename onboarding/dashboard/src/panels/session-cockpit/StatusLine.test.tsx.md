# dashboard/src/panels/session-cockpit/StatusLine.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/StatusLine.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the footer's segment order, launch/state evidence, bounded elapsed/freshness copy, and literal
honest absence of UA-5 context/cost telemetry.

## Code Commentary

### Logic

- The primary case freezes time and checks DOM order across harness, pair badge, state/elapsed,
  leaf/seat, pending/queue, UA-5, freshness, actions, and hint.
- The absent-seat case keeps placeholders visible without inventing evidence.

### Invariants And Boundaries

- Order assertions are deliberate: new segments require an explicit contract change.
- The reserved slot must remain `ctx — / cost — (UA-5 slot)` until real telemetry lands.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Contractual order and freshness case. | L13-L111 | [StatusLine.test.tsx](StatusLine.test.tsx) |
| Honest absent-seat case. | L112-L129 | [StatusLine.test.tsx](StatusLine.test.tsx) |
| Component under test. | L76-L184 | [StatusLine.tsx](StatusLine.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
