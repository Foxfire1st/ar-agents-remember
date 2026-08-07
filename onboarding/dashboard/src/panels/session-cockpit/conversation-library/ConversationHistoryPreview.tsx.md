# dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

- **States** cit:([`ConversationHistoryPreview`], dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx:28-84): typed `error` renders a `role="alert"`; `loading` prints `loading preview…`;
  an absent `page` prints the A1 placeholder `Select a conversation to preview it here.`
- **Honest partial note** cit:([`partialReason`], dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx:61-66) (F13): when either `completeness` or `toolCompleteness` is not
  `supported`, the note prints the reason from the capability that is *actually* unsupported —
  `toolCompleteness.reason` is preferred only when tool-completeness is the failing one; otherwise
  `completeness.reason`. It never prints a supported capability's reason text (the round-1 bug).
- **Body** cit:([`ConversationHistoryPreview`], dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx:28-84): the label, the optional partial note, then a `role="list"` scroll region
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared kind-dispatcher that keeps historical and live grammar identical. | `ConversationItemView` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:66-69 |
| The historical page wire type (items + `historicalCapabilities`). | `historicalCapabilities` | dashboard/src/data/conversation-library/types.ts:67-67 |
| The surface that mounts this preview column. | `ConversationLibrarySurface` | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:75-171 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 2 repository-internal references and normalized 2 prose citation references for the shared conversation dispatcher and history-library surface; final scoped result 0 (checker-clean).

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the read-only history
  preview — same block grammar as the live feed via `ConversationItemView`, the `history preview ·
  not active` label, no write affordances, and the F13-fixed partial note that prints the actually
  unsupported capability's reason. Verification is pinned to the leaf base (`0be0099`) because the
  new source file is uncommitted; closeout owns its first source stamp.
