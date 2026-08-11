# dashboard/src/panels/GateResponder.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponder.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Component under test and its response branches. | `GateResponder` | dashboard/src/panels/GateResponder.tsx:720-780 |
| Gate decision client mocked for Yes/No/Dismiss. | `postGateDecision` | dashboard/src/data/actions.ts:14-38 |
| Session store and attach lookup. | `sessionStore`, `findSessionForLifecycle` | dashboard/src/data/sessions.ts:508-522; dashboard/src/data/sessions.ts:527-531 |
| Direct delivery seam asserted unused on the durable inbox route. | `deliverToSession` | dashboard/src/data/sessions.ts:736-759 |
| Operator inbox helper used for ordinary approval/rejection routing. | `postOperatorInbox` | dashboard/src/data/operatorInbox.ts:18-32 |

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Current L5I Maintenance

The tests seed reopened gates with both delivery certainties. They pin the prior-answer/reason
display for a proven unsent response, the no-fabricated-answer form for unknown delivery, and the
absence of a warning on an ordinary open gate.

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-07-24T13:17:17Z — Curator: recorded coverage for evidence-bounded adapter-decision-failure
  rendering; verification fields remain pre-commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.

- 2026-07-02T16:18+02:00 — L8: replaced the message-only Chat route assertion with a regression that
  `gate-respond-chat` is absent while durable Yes/No/Dismiss behavior remains covered. Verification
  metadata pinned until closeout stamps the L8 commit.
- 2026-06-27T03:04+02:00 — No content impact: updated the store reset shape after Task 22 removed the
  hidden-label reservation state; GateResponder behavior and assertions are unchanged.
- 2026-06-27T01:03+02:00 — Task 22 label allocator follow-up: no behavior change to GateResponder
  coverage; store resets now include reserved labels so hidden-session label state cannot leak between
  cases.
- 2026-06-25T13:20+02:00 — Task 23/24: added tests for Dismiss/cancel and close-on-success behavior for approve/reject/chat/dismiss paths.
- 2026-06-25T07:26+02:00 — Task 19 follow-up: added readable-preview fixtures for plan approval, cleanup approval, and agent-question gates so the request preview test covers more than the closeout-like changed-path packet.
- 2026-06-25T07:17+02:00 — Task 19: rewrote GateResponder coverage for targeted Yes approval, required-reason No rejection, message-only Chat, stale-gate no-notify behavior, human-readable request preview, and retained hosted/inbox routing. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: updated coverage so missing hosted sessions queue through `postOperatorInbox`, inbox failures show retryable copy, and direct hosted delivery still bypasses the inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:45+02:00 — Created for Task 11 Gate Respond coverage.
