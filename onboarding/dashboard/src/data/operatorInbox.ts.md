# dashboard/src/data/operatorInbox.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/operatorInbox.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-04T12:31+02:00                           |
| lastVerifiedCommitHash |                                                  `e358c4ac520d94ae2e597ae3cbe186e07a4d1063`|
| lastVerifiedCommitDate |                                                  2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Same-origin client helper for the dashboard's durable operator/agent inbox post
path and pending-entry dismissal.

## Code Commentary

### Logic

`OperatorInboxPostRequest` mirrors the serving endpoint's camelCase body: optional `lifecycleId`,
optional `agentId`, optional `recipientRole`, optional `gateId`, sender/message metadata,
optional `artifactPath`, optional `deliverToHosted`, plus the preserved `ask` and developer `response`.
`postOperatorInbox(request, base = "")` sends that JSON to `POST /api/operator-inbox` and returns the
small UI status union `"posted"` or `"error"`. A non-2xx response and a network throw both map to
`"error"` so the responder can show a retryable status instead of claiming delivery.

`dismissOperatorInboxEntry(entryId, base = "")` sends `POST /api/operator-inbox/{entryId}/dismiss` for
the task-row check-chat warning. It returns `"dismissed"`, `"not-found"`, or `"error"`. This is
developer dismissal of a warning, not agent consumption.

### Conventions

The helper follows the existing dashboard data-client pattern: same-origin `fetch`, JSON request
body, tiny status union, and no optimistic store mutation.

### Invariants And Boundaries

- This is a transport helper, not gate enforcement. The inbox entry is a durable message for an
  external or hosted agent; it does not decide or release a gate by itself.
- Same-origin by default. The FastAPI dashboard server owns the trusted developer/dashboard
  attribution for this write.
- The helper reports small status unions only; callers own route selection, copy, and retry affordance.

### Todos

None.

## Docs References

The observable-lifecycle design names pull-based return channels as the durable fallback when push or
direct re-invocation is not available. This helper is the dashboard client side of that fallback.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pull-based return channels resume gate answers when a harness cannot be pushed or directly re-invoked. | L251-L266 | [observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The helper defines the request/status contract and posts JSON to `/api/operator-inbox`. | L1-L25 | [operatorInbox.ts](agents-remember/dashboard/src/data/operatorInbox.ts) |
| `GateResponder` calls this helper only after lifecycle-to-hosted-session lookup fails. | L195-L214 | [GateResponder.tsx](agents-remember/dashboard/src/panels/GateResponder.tsx) |
| The serving endpoint writes the inbox entry with developer/dashboard attribution. | L358-L376 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The helper test pins the POST body and error mapping. | L5-L45 | [operatorInbox.test.ts](agents-remember/dashboard/src/data/operatorInbox.test.ts) |
| `AgentPickupIndicator` calls the dismiss helper for stale pending responses. | — | [AgentPickupIndicator.tsx](../panels/AgentPickupIndicator.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-04T12:31+02:00 - L3: mirrored the expanded `/api/operator-inbox`
  request body with recipient role, sender/message metadata, artifact path, and
  hosted-delivery opt-in. Verification metadata pinned until closeout stamps the
  L3 commit.
- 2026-06-25T13:10+02:00 — Task 23/24: added `dismissOperatorInboxEntry` for the task-row check-chat warning.
- 2026-06-23T15:05+02:00 — Created for task 10 dashboard fallback: `postOperatorInbox` sends missing-hosted-session gate responses to `POST /api/operator-inbox` and reports posted/error for the responder UI. Verification metadata pinned until closeout stamps the task-10 code commit.
