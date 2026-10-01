# dashboard/src/panels/GateResponder.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Focused behavior coverage for the shared `GateResponder`. It pins the routing contract: `Yes` and
`No` record targeted durable decisions, `No` requires a reason, and ordinary approval/rejection
notices use the durable operator inbox even when a hosted session is attached. `Dismiss` records a
cancel decision without an agent notice; stale targeted gates do not notify; adapter-interaction
gates use the durable gate response without a second inbox or terminal message. Approval and dismiss
tests assert dialog closure, while the rejection test focuses on the required reason and inbox route.
Common gate kinds render readable request previews instead of primary raw JSON. L8 removes the obsolete
message-only `Chat` path from this gate UI.

## Code Commentary

### Logic

The test file mocks `postGateDecision`, `deliverToSession`, and `postOperatorInbox`, while keeping the
real `sessionStore` and `findSessionForLifecycle` helpers. Each test resets the store to empty.

- Yes/hosted route: records `approve` with the current `gateId`, verifies the human-readable preview
  hides raw JSON in the main request area, queues the approval notice in the operator inbox, and
  asserts that `deliverToSession` is not called.
- Yes/external route: records `approve`, queues the approval notice in the operator inbox, and closes
  the dialog after the durable route succeeds.
- No route: proves the blank reason is ignored, then records `reject` with the typed note and sends the
  rejection reason to the operator inbox; this test does not claim a separate close assertion.
- Dismiss route: records `cancel` with the current gate id and closes the dialog without sending an
  agent notification.
- Obsolete-chat route: opens the prompt and asserts `gate-respond-chat` is absent, with no decision or
  inbox write triggered just by opening the dialog.
- Close coverage: approval closes after the decision and inbox notice succeed; dismiss closes after its
  recorded cancel. Rejection is covered for decision/reason/inbox routing without a separate close
  assertion.
- Preview fixtures: plan approval, cleanup approval, and agent-question packets render human-readable
  gate kind, request, and context lines while keeping raw JSON in diagnostics.
- Stale route: makes `postGateDecision` return `stale-gate` and asserts no hosted/inbox notification
  follows.
- Attach route: seeds one untagged active terminal session, opens the responder, uses
  `Attach Terminal 1`, asserts `findSessionForLifecycle("LC1")`, then sends `Yes`.

### Invariants And Boundaries

The test distinguishes durable decisions from the removed message-only path: ordinary `Yes`/`No` call
the `/api/actions` client and route their notices through the operator inbox, `Dismiss` cancels the
interaction without notification, and an adapter-interaction gate ends at the durable response source
without a duplicate notice. The old `Chat` control must stay absent.

## Evidence

### Repo-Internal References

- Component under test and its response branches. [1]
- Gate decision client mocked for Yes/No/Dismiss. [2]
- Session store and attach lookup. [3]
- Direct delivery seam asserted unused on the durable inbox route. [4]
- Operator inbox helper used for ordinary approval/rejection routing. [5]

#### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Current L5I Maintenance

The tests seed reopened gates with both delivery certainties. They pin the prior-answer/reason
display for a proven unsent response, the no-fabricated-answer form for unknown delivery, and the
absence of a warning on an ordinary open gate.
