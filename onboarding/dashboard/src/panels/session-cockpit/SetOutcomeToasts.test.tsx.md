# dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/SetOutcomeToasts.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Regression contract for background set-outcome persistence, acknowledgment, and collapse.

## Code Commentary

### Logic

Proves that no toast appears without attention or for the focused seat, that focus and dismiss are
separate actions, that dismiss acknowledges the ledger, and that several affected sessions share
one stack.

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
| Visibility, persistence, dismissal, focus, and collapse cases. | L33-L74 | [SetOutcomeToasts.test.tsx](SetOutcomeToasts.test.tsx) |
| Component under test. | L58-L142 | [SetOutcomeToasts.tsx](SetOutcomeToasts.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R6 background-outcome regression
  after final reviewer PASS. Base verification metadata is temporary until code commit.
