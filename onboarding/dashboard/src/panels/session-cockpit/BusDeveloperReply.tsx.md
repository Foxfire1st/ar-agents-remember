# dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Owns the Bus pane's one write boundary: compose and post a new developer reply or decision to the
projected original sender through the existing operator-inbox route without consuming,
acknowledging, or otherwise mutating the source pickup.

## Code Commentary

### Logic

- `developerReplyRequest` accepts only a projected `senderAgentId` and/or `senderRole` as the
  reverse address. It maps those to `agentId`/`recipientRole`, preserves gate/artifact metadata,
  and never copies the original recipient's `lifecycleId` into the request.
- A decision item becomes `decision-ruling`; an escalation becomes a plain `message`. A row with
  only target lifecycle/recipient facts returns `null`, so it cannot issue a POST.
- The controlled form posts through `postOperatorInbox`, disables during the request, clears a
  successful draft, and retains a failed draft with an assertive error. Sending and posted states
  use a polite live region.

### Invariants And Boundaries

- This component creates a new inbox entry only. Source-row consume/acknowledge and session submit
  are outside this boundary.
- Reverse routing must remain sender-derived; target lifecycle identity is not a reply address.
- The textarea keeps its label, name, disabled/busy semantics, and retained-draft failure message.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Sender-only reverse request construction and message-kind mapping. [1]
- Accessible controlled form and the sole operator-inbox POST. [2]
- Existing POST client this boundary reuses. [3]
- Exact request-body and zero-POST regression coverage. [4]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
