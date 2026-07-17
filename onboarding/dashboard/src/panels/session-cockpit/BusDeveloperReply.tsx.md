# dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sender-only reverse request construction and message-kind mapping. | L37-L59 | [BusDeveloperReply.tsx](BusDeveloperReply.tsx) |
| Accessible controlled form and the sole operator-inbox POST. | L75-L196 | [BusDeveloperReply.tsx](BusDeveloperReply.tsx) |
| Existing POST client this boundary reuses. | L1-L85 | [../../data/operatorInbox.ts](../../data/operatorInbox.ts) |
| Exact request-body and zero-POST regression coverage. | L146-L196, L297-L338 | [BusPane.test.tsx](BusPane.test.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  authoritative sender-derived reverse reply and the no-consume/no-target-lifecycle boundary.
  Verification metadata remains pinned to the leaf base until closeout.
