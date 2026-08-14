# dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sender-only reverse request construction and message-kind mapping. | `developerReplyRequest` | dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx:37-59 |
| Accessible controlled form and the sole operator-inbox POST. | "post to operator inbox" | dashboard/src/panels/session-cockpit/BusDeveloperReply.tsx:182-182 |
| Existing POST client this boundary reuses. | `postOperatorInbox` | dashboard/src/data/operatorInbox.ts:18-32 |
| Exact request-body and zero-POST regression coverage. | "posts a developer decision to the original sender through /api/operator-inbox only"; "performs zero POSTs" | dashboard/src/panels/session-cockpit/BusPane.test.tsx:146-184; dashboard/src/panels/session-cockpit/BusPane.test.tsx:186-203 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 4 citation items; scoped citation check now passes.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Documents the
  authoritative sender-derived reverse reply and the no-consume/no-target-lifecycle boundary.
  Verification metadata remains pinned to the leaf base until closeout.
