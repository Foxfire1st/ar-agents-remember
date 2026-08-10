# dashboard/src/panels/session-cockpit/EvidencePane.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EvidencePane.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Focused-seat case covers launch, receipt/reconciliation, bridge, pane, retire-stop residual, and liveness evidence. | "reveals launch" | dashboard/src/panels/session-cockpit/EvidencePane.test.tsx:32-113 |
| Missing-receipt honesty case. | "keeps missing receipt evidence explicitly absent in the pure detail projection" | dashboard/src/panels/session-cockpit/EvidencePane.test.tsx:115-127 |
| Terminate and retire residuals remain inspectable without focus and share dismissal across surfaces. | "keeps terminate and retire residuals inspectable without focus and shares exact dismissal" | dashboard/src/panels/session-cockpit/EvidencePane.test.tsx:129-177 |
| A successful terminate residual remains visible after the terminated seat is removed. | "reveals a successful terminate residual after the terminated seat is removed" | dashboard/src/panels/session-cockpit/EvidencePane.test.tsx:179-201 |
| Component under test. | "export function EvidencePane({" | dashboard/src/panels/session-cockpit/EvidencePane.tsx:407-407 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Updates lifecycle notice fixtures for the new `cleanupFailure` state so evidence tests exercise the complete notice-store shape.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-04T11:39:21+02:00 — 260731-EFA-L6 S18-B09 curator: reconciled the frozen-source ledger and repaired scoped citations; unsupported source claims were narrowed or removed, and the landing provenance mismatch remains an explicit Tier-3 item.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
