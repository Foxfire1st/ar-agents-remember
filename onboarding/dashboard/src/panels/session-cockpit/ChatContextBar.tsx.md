# dashboard/src/panels/session-cockpit/ChatContextBar.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatContextBar.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Carries product duties formerly stranded in the retired Chats route into the canonical cockpit:
launch Chat/Terminal, show task/leaf context, route an existing row locally to a lifecycle, and
authoritatively attach or move a running row to a leaf.

## Code Commentary

New launches inherit the selected lifecycle through the server route. Existing lifecycle attachment
remains explicitly local because no server endpoint exists. Leaf attach/move calls the daemon first,
patches the registry only on success, broadcasts a `leaf` invalidation, and renders same-role conflict
without changing the row.

## Invariants And Boundaries

Do not present local lifecycle routing as durable server authority. Leaf ownership is authoritative:
no optimistic local mutation and no hidden 409 refusal.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The bar composes repository-local task/session helpers and same-origin terminal routes; no cross-repository implementation governs it.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Canonical host. | [SessionsView.tsx](SessionsView.tsx) |
| Session patch/broadcast and server leaf route. | [../../data/sessions.ts](../../data/sessions.ts) · [../../data/terminal.ts](../../data/terminal.ts) |

## Update History

- 2026-07-18T07:22+02:00 — Created for the FEUI-L8 legacy-Chats duty transfer; verification metadata
  remains blank until commit.
