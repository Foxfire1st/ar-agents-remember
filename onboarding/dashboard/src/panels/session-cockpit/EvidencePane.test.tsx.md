# dashboard/src/panels/session-cockpit/EvidencePane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EvidencePane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Pins the Evidence pane's proof completeness, missing-evidence honesty, both lifecycle stop-residual
classes, and exact dismissal behavior before and after a seat leaves the catalog.

## Code Commentary

### Logic

- Covers launch, set receipt, submit receipt/reconciliation, bridge error, pane, liveness, and
  explicit mark-seen rendering.
- Proves absent receipt fields remain absent rather than being inferred.
- Covers terminate and retire residuals, exact `(sessionId, at)` dismissal, no-focus visibility,
  and a successful terminate residual revealed after the terminated seat disappears.

### Invariants And Boundaries

- Both stop classes are informational and share the same authoritative notice store.
- Catalog removal must not erase the latest confirmed control-stop detail.

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
| Complete focused-seat evidence case. | L27-L109 | [EvidencePane.test.tsx](EvidencePane.test.tsx) |
| Missing-receipt honesty case. | L110-L123 | [EvidencePane.test.tsx](EvidencePane.test.tsx) |
| Both residual classes, exact dismissal, and post-removal case. | L124-L197 | [EvidencePane.test.tsx](EvidencePane.test.tsx) |
| Component under test. | L34-L374 | [EvidencePane.tsx](EvidencePane.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
