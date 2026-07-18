# dashboard/src/panels/session-cockpit/EvidencePane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EvidencePane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md`                                   |

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

## FEUI-L8 Reviewed Candidate Delta

Updates lifecycle notice fixtures for the new `cleanupFailure` state so evidence tests exercise the complete notice-store shape.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
