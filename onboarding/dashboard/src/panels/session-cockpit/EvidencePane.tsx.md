# dashboard/src/panels/session-cockpit/EvidencePane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EvidencePane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Provides the inspector's audit surface for launch, set, submit, pane, lifecycle, and liveness facts,
including post-removal control-stop residuals that must stay visible without a focused seat.

## Code Commentary

### Logic

- Projects launch evidence, SetResult ledger lines, submit receipts and reconciliation, bridge
  errors, pane/raw-interaction facts, and liveness/outcome facts without synthesizing missing proof.
- Set evidence has an explicit `mark seen` action; merely viewing or focusing the pane never
  acknowledges it.
- Reads both terminate `controlStopDetail` and retire `retireControlStopError` from the shared
  `lifecycleNoticeStore`. Residuals stay informational, survive source-row removal, and can be
  dismissed by exact `(sessionId, at)` identity shared with the stage.
- No-focus mode still renders fleet stop residuals while seat-specific sections state their absence.

### Invariants And Boundaries

- A successful stop residual is not a failed stop and must never be styled or worded as one.
- Missing receipts/reconciliation remain visibly absent; the pane does not mint tombstones or proof.
- Viewing is read-only except for the explicit mark-seen and exact residual-dismiss actions.

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
| Pure evidence/detail projection. | L34-L105 | [EvidencePane.tsx](EvidencePane.tsx) |
| Shared terminate/retire residual rendering and exact dismissal. | L107-L167 | [EvidencePane.tsx](EvidencePane.tsx) |
| Full pane rendering and explicit actions. | L169-L374 | [EvidencePane.tsx](EvidencePane.tsx) |
| Lifecycle notice store shared with the stage. | L1-L191 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| Set acknowledgment driver. | L326-L336 | [../../data/setClient.ts](../../data/setClient.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Records the
  full evidence audit surface, explicit mark-seen action, and authoritative post-removal stop
  residual boundary. Verification metadata remains pinned to the leaf base until closeout.
