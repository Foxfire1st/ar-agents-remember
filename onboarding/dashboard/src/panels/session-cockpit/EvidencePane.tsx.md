# dashboard/src/panels/session-cockpit/EvidencePane.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/EvidencePane.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure evidence/detail projection. | `submitEvidenceLines` | dashboard/src/panels/session-cockpit/EvidencePane.tsx:102-112 |
| Shared terminate/retire residual rendering and exact dismissal. | `RetainedStopResiduals` | dashboard/src/panels/session-cockpit/EvidencePane.tsx:356-405 |
| Full pane rendering and explicit actions. | `EvidencePane` | dashboard/src/panels/session-cockpit/EvidencePane.tsx:407-463 |
| Lifecycle notice store shared with the stage. | `useLifecycleNotices` | dashboard/src/data/sessionLifecycle.ts:123-125 |
| Set acknowledgment driver. | `acknowledgeSetAttention` | dashboard/src/data/setClient.ts:386-391 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Records the
  full evidence audit surface, explicit mark-seen action, and authoritative post-removal stop
  residual boundary. Verification metadata remains pinned to the leaf base until closeout.
