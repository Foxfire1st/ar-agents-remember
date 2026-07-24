# dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
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

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component gates its welcome state on `processState`. | L1-L206 | [ConversationWelcome.tsx](ConversationWelcome.tsx) |
| The surface supplies harness and current process state only for an empty live timeline. | L202-L226 | [ConversationSurface.tsx](ConversationSurface.tsx) |
| Focused cases cover each readiness wording. | L9-L61 | [ConversationWelcome.test.tsx](ConversationWelcome.test.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-07-24T13:17:17Z — Curator: created the honest empty-conversation welcome sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
