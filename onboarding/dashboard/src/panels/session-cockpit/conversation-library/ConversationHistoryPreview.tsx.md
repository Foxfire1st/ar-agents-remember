# dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

The read-only history preview (design §4.4). It renders a previewed prior conversation with the SAME
block grammar as the live timeline (via `ConversationItemView`) but is clearly labeled
`history preview · not active` and stripped of every write affordance — no composer, interaction
answer, queue, model/effort set, or interrupt. It is a preview, never a live AR session; reading it
never mutates any live conversation.

## Code Commentary

### Logic

- **States** (L37-L57): typed `error` renders a `role="alert"`; `loading` prints `loading preview…`;
  an absent `page` prints the A1 placeholder `Select a conversation to preview it here.`
- **Honest partial note** (L58-L66, F13): when either `completeness` or `toolCompleteness` is not
  `supported`, the note prints the reason from the capability that is *actually* unsupported —
  `toolCompleteness.reason` is preferred only when tool-completeness is the failing one; otherwise
  `completeness.reason`. It never prints a supported capability's reason text (the round-1 bug).
- **Body** (L67-L82): the label, the optional partial note, then a `role="list"` scroll region
  labeled `History preview (read only)` whose items each render through `ConversationItemView` — the
  same dispatcher the live feed uses, so the preview reads identically to the live grammar.

### Invariants And Boundaries

- Read-only by construction: no write affordance is rendered and no store mutation happens on preview.
- The partial-note reason must come from the failing capability (F13), mirroring the live surface's
  completeness note; a supported-state reason must never be shown as the "why partial" copy.
- Reuses `ConversationItemView` so the historical and live grammars can never drift apart.

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
| The shared kind-dispatcher that keeps historical and live grammar identical. | L8 | [../conversation/ConversationItemView.tsx](../conversation/ConversationItemView.tsx) |
| The historical page wire type (items + `historicalCapabilities`). | L7 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |
| The surface that mounts this preview column. | L147-L152 | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the read-only history
  preview — same block grammar as the live feed via `ConversationItemView`, the `history preview ·
  not active` label, no write affordances, and the F13-fixed partial note that prints the actually
  unsupported capability's reason. Verification is pinned to the leaf base (`0be0099`) because the
  new source file is uncommitted; closeout owns its first source stamp.
