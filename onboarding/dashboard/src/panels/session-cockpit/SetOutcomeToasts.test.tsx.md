# dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Regression contract for background set-outcome persistence, acknowledgment, and collapse.

## Code Commentary

### Logic

Proves that no toast appears without attention or for the focused seat, that focus and `mark seen`
are separate actions, that only mark seen acknowledges the ledger, and that several affected
sessions share one stack.

### Conventions

The real cockpit store supplies attention state while callbacks make focus intent observable.

### Invariants And Boundaries

Changing focus does not silently acknowledge an outcome, and dismissal is an explicit mark-seen
operation.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Visibility, persistence, mark-seen, focus, and collapse cases. | "renders nothing without unacknowledged outcomes" | dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx:34-44 |
| Component under test. | "export function SetOutcomeToasts" | dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx:141-141 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 updated the regression contract to the explicit
  `mark seen` wording while preserving focus/view as non-acknowledging. Verification metadata
  remains pinned to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R6 background-outcome regression
  after final reviewer PASS. Base verification metadata is temporary until code commit.
