# dashboard/src/panels/session-cockpit/BusPane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusPane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the Bus pane's fleet/filter honesty, supervisor facts, authoritative reverse-address request,
and reply-state persistence across filtering and more-than-100-row virtualization.

## Code Commentary

### Logic

- Covers the fleet-global default, sender-to-owner and redelivery facts, exact focused-seat
  filtering, non-health empty copy, and reset when focus disappears.
- Proves the exact operator-inbox request body for coherent sender pairs plus sender-agent-only and
  sender-role-only rows. Lifecycle-only targets perform zero POSTs and target lifecycle never leaks.
- A 120-row case drives virtual unmount/remount and async success/failure settlement, proving that
  each `entryId` retains its own open, draft, posted, or error state.

### Invariants And Boundaries

- Tests must assert both positive request shape and prohibited addressing fields.
- Large-list coverage protects interaction continuity, not merely row-count performance.

### Todos

None recorded; browser-level long-list/off-tab smoke remains a leaf integration residual.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Fleet, filter, focus-loss, and draft persistence cases. | L50-L145 | [BusPane.test.tsx](BusPane.test.tsx) |
| Exact POST and lifecycle-only zero-write cases. | L146-L204, L297-L338 | [BusPane.test.tsx](BusPane.test.tsx) |
| Virtualized per-entry async state case. | L205-L296 | [BusPane.test.tsx](BusPane.test.tsx) |
| Shared coherent and legacy fixture pack. | L1-L117 | [../../test/fixtures/busScenarios.ts](../../test/fixtures/busScenarios.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
