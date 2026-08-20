# dashboard/src/panels/session-cockpit/BusPane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusPane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fleet, filter, focus-loss, and draft persistence cases. | "keeps a reply draft keyed to its entry across focused-seat filter unmounts" | dashboard/src/panels/session-cockpit/BusPane.test.tsx:121-144 |
| Exact POST and lifecycle-only zero-write cases. | "posts a developer decision to the original sender through /api/operator-inbox only"; "renders a lifecycle-only source as unavailable and performs zero POSTs" | dashboard/src/panels/session-cockpit/BusPane.test.tsx:146-184; dashboard/src/panels/session-cockpit/BusPane.test.tsx:186-203 |
| Virtualized per-entry async state case. | "keeps each reply's open" | dashboard/src/panels/session-cockpit/BusPane.test.tsx:205-293 |
| Shared coherent and legacy fixture pack. | `L7_PICKUPS` | dashboard/src/test/fixtures/busScenarios.ts:108-112 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## 260815-DAG Master Full-Gate Repair

`afterEach` is now async and flushes the virtualizer's 150 ms scroll-observer debounce (fake-timer clear + real-timer 200 ms settle) before jsdom teardown so orphaned callbacks cannot fire without a `window`.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: async `afterEach` flushes the virtualizer scroll-observer debounce before teardown. Verified at code commit e5cb139f.

- 2026-08-12T00:28+02:00 — No content impact: the developer-reply case now waits for the
  already-required final acknowledgment status, avoiding a race with the legitimate intermediate
  `posting…` state; the POST shape and final-state contract documented above are unchanged.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 4 repository-reference citations (4/4 anchored and sourced; scoped citation check clean).

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
