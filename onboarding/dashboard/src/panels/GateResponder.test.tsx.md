# dashboard/src/panels/GateResponder.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/GateResponder.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Focused behavior coverage for the shared `GateResponder`. It pins the routing contract: `Yes` and
`No` record targeted durable decisions before notifying the agent, `No` requires a reason, `Dismiss`
records a cancel/delete decision, `Chat` remains message-only, stale targeted gates do not notify the
agent, successful responses close the prompt, hosted/inbox routing still works with active untagged
session attach, and common gate kinds render as readable request previews instead of primary raw JSON.

## Code Commentary

### Logic

The test file mocks `postGateDecision`, `deliverToSession`, and `postOperatorInbox`, while keeping the
real `sessionStore` and `findSessionForLifecycle` helpers. Each test resets the store to empty.

- Yes/hosted route: records `approve` with the current `gateId`, verifies the human-readable preview
  hides raw JSON in the main request area, then delivers the approval notice to the hosted session.
- Yes/external route: records `approve`, queues the approval notice in the operator inbox, and bypasses
  hosted delivery.
- No route: proves the blank reason is ignored, then records `reject` with the typed note and sends the
  rejection reason to the operator inbox.
- Dismiss route: records `cancel` with the current gate id and closes the dialog without sending an
  agent notification.
- Chat route: sends the free-form message through the inbox and asserts no gate decision was recorded.
- Close-on-success route: asserts approved/rejected/chat submissions close the dialog after the server
  accepts the write or delivery.
- Preview fixtures: plan approval, cleanup approval, and agent-question packets render human-readable
  gate kind, request, and context lines while keeping raw JSON in diagnostics.
- Stale route: makes `postGateDecision` return `stale-gate` and asserts no hosted/inbox notification
  follows.
- Attach route: seeds one untagged active terminal session, opens the responder, uses
  `Attach Terminal 1`, asserts `findSessionForLifecycle("LC1")`, then sends `Yes`.

### Invariants And Boundaries

The test distinguishes decision and message paths: `Yes`/`No` must call the `/api/actions` client, while
`Chat` must not. `Dismiss` is separate from approve/reject: it cancels/deletes the interaction and does
not notify the agent.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Component under test. | — | [GateResponder.tsx](GateResponder.tsx) |
| Gate decision client mocked for Yes/No. | — | [data/actions.ts](../data/actions.ts) |
| Session store and delivery seam under test. | — | [data/sessions.ts](../data/sessions.ts) |
| External inbox helper mocked for no-hosted-session routing. | L1-L25 | [data/operatorInbox.ts](../data/operatorInbox.ts) |

## Update History

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
