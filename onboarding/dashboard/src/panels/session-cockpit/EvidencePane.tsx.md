# dashboard/src/panels/session-cockpit/EvidencePane.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Provides the inspector's audit surface for launch, set, submit, pane, lifecycle, and liveness facts,
including post-removal control-stop residuals that must stay visible without a focused seat.

## Code Commentary

### Logic

- Projects launch evidence, SetResult ledger lines, submit receipts and reconciliation, bridge
  errors, pane/raw-interaction facts, the selected seat's task-document identity, and
  liveness/outcome facts without synthesizing missing proof.
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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Pure evidence/detail projection. [1]
- Shared terminate/retire residual rendering and exact dismissal. [2]
- Full pane rendering and explicit actions. [3]
- Lifecycle notice store shared with the stage. [4]
- Set acknowledgment driver. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
