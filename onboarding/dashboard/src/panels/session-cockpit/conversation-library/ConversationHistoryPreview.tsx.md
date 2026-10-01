# dashboard/src/panels/session-cockpit/conversation-library/ConversationHistoryPreview.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The shared kind-dispatcher that keeps historical and live grammar identical. [1]
- The historical page wire type (items + `historicalCapabilities`). [2]
- The surface that mounts this preview column. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
