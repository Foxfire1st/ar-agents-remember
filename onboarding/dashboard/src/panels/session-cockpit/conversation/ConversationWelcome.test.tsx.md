# dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Conversation renderer overview](overview.md)

## Purpose

Pins process-evidenced welcome language for an empty structured conversation.

## Code Commentary

### Logic

Cases render the welcome through its public props and assert that only the connected process form
uses ready copy/dot; starting, disconnected, exited, failed, and absent state remain neutral or
honestly unavailable.

### Conventions

This is a focused renderer test: it does not simulate stream opening because stream liveness is
deliberately not the readiness authority for this component.

### Invariants And Boundaries

Tests must reject a future regression that paints a fresh-online token merely because a conversation
projection happens to be live.

### Todos

None recorded.

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Focused cases cover all process readiness variants. | "never claims the link is ready when the process is %s" | dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.test.tsx:31-41 |
| Component under test. | `ConversationWelcome` | dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:154-206 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History
- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 2 repository-reference citations (2/2 anchored and sourced; scoped citation check clean).

- 2026-07-24T13:17:17Z — Curator: created welcome-readiness regression coverage onboarding. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
