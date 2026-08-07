# dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `7c56c11d651972515723b4090b8174087eb5236f`|
| lastVerifiedCommitDate |  2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Renders the restrained empty-conversation welcome inside the persistent timeline well without
claiming that a harness link is ready unless process evidence proves it.

## Code Commentary

### Logic

The component derives neutral, connecting, or ready presentation from its harness and optional
process-state inputs. The ready dot/copy is gated by a real connected state; unavailable, exited,
failed, or unknown process state does not inherit confidence from SSE liveness alone.

### Conventions

It is presentation-only and receives state from `ConversationSurface`; it neither opens streams nor
infers server readiness itself.

### Invariants And Boundaries

An open event stream is not proof that the underlying harness is ready. The empty well must stay
honest when the process is disconnected or no current process state exists.

### Todos

None recorded.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component gates its welcome state on optional `processState`, selecting `UNKNOWN_LINK` when it is undefined and otherwise `LINK_STATES[processState]`. | `processState`; `UNKNOWN_LINK`; `LINK_STATES`; "processState === undefined"; "LINK_STATES[processState]" | dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:144-150; dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:152-152; dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:160-160; dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:162-162 |
| The surface supplies harness and current process state only for an empty live timeline. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-341 |
| Focused cases cover each readiness wording. | "never claims the link is ready when the process is %s"; "mirrors the uncertainty when the projection has applied no status frame yet"; "says the link is ready — with the mint live dot — only for a connected process" | dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx:31-41; dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx:43-51; dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx:53-60 |

## Update History

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended the process-state gate through its operative selection and regenerated the final range with the scoped fixer.

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 4 citation finding(s); scoped recheck clean.

- 2026-07-24T13:17:17Z — Curator: created the honest empty-conversation welcome sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
