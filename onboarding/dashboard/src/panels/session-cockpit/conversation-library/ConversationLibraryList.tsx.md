# dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationLibraryList.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The native conversation list (design §4.4): a scrollable column of prior conversations paged by the
server-native cursor, never a locally-accumulated infinite index. Each row shows a boundary-truncated
title with the full value on hover (A5), the safe native id suffix, a humanized last-activity age
(A4), and a granular historical-completeness badge. A row is selectable for *preview only* — selecting
never opens or activates anything.

## Code Commentary

### Logic

- **`completenessLabel`** (L67-L70): reads `row.capabilities.completeness.state` and prints
  `full history` when `supported`, else `partial history` — honest per-row completeness, never a
  fabricated "complete".
- **States** (L91-L111): typed `error` renders a `role="alert"`; an empty-while-loading row prints
  `loading <harness> history…`; a genuinely empty scope prints the A1 empty-state copy
  `No <harness> conversations in this project scope.` (no dash-chain).
- **Rows** (L112-L134): each row is a real `<button>`; `data-selected` marks the previewed row;
  `title` carries the full untruncated title (A5) while `truncateMiddle(title, 60)` renders the
  boundary-truncated visible text; the meta line joins the completeness badge, the mono
  `…safeNativeIdSuffix`, and `humanizeAge(lastActivityAt)`.
- **`Load more`** (L135-L139): rendered only when `nextCursor !== null`; disabled while loading —
  the R5 explicit native paging affordance (never infinite auto-scroll indexing).

### Invariants And Boundaries

- Selecting a row is a preview action only; open/activate is `OpenConversationAction`'s exclusive job.
- Paging is server-native cursor paging (`nextCursor`); the list is never turned into a durable local
  conversation database.
- Truncation always preserves the full value in `title` (A5); the age is always humanized (A4).

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Row/cursor/key wire types this list renders. | L9-L13 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |
| The A4/A5 presentation helpers (`humanizeAge`, `truncateMiddle`, `harnessLabel`). | L7 | [../../../data/conversation/format.ts](../../../data/conversation/format.ts) |
| The surface that owns selection/paging callbacks into the store. | L133-L146 | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the native
  cursor-paged conversation list — preview-only rows, boundary-truncated title with full-value
  affordance (A5), humanized age (A4), per-row completeness badge, and explicit `Load more` native
  paging. Verification is pinned to the leaf base (`0be0099`) because the new source file is
  uncommitted; closeout owns its first source stamp.
