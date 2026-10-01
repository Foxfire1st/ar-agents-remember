# dashboard/src/data/operatorInbox.ts

## Governing Overview

[data overview](overview.md)

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

## Evidence

### Docs References

The observable-lifecycle design names pull-based return channels as the durable fallback when push or
direct re-invocation is not available. This helper is the dashboard client side of that fallback.

- Pull-based return channels resume gate answers when a harness cannot be pushed or directly re-invoked. [1]

### Repo-Internal References

- The helper defines the request/status contract and posts JSON to `/api/operator-inbox`. [2]
- `GateResponder` calls this helper only after lifecycle-to-hosted-session lookup fails. [3]
- The serving endpoint writes the inbox entry with developer/dashboard attribution. [4]
- The helper test pins the POST body and error mapping. [5]
- `AgentPickupIndicator` calls the dismiss helper for stale pending responses. [6]

### Cross-Repo References

No meaningful cross-repo references found.

None.
