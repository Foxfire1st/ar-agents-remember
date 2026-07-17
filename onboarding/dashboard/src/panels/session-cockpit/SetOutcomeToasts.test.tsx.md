# dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Visibility, persistence, mark-seen, focus, and collapse cases. | L33-L74 | [SetOutcomeToasts.test.tsx](SetOutcomeToasts.test.tsx) |
| Component under test. | L58-L142 | [SetOutcomeToasts.tsx](SetOutcomeToasts.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 updated the regression contract to the explicit
  `mark seen` wording while preserving focus/view as non-acknowledging. Verification metadata
  remains pinned to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R6 background-outcome regression
  after final reviewer PASS. Base verification metadata is temporary until code commit.
