# dashboard/src/panels/session-cockpit/stageLayers.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/stageLayers.tsx`      |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The Chats-stage layer components, extracted from `ChatsStageBody.tsx` by the
260731-EFA-L8 split. Owns the empty stage, conversation pool, the persistent PTY
layer (keep-alive), and the library/diagnostics slot.

## Code Commentary

### Logic

`PtyLayer` keeps the PTY surface mounted through smart-focus handoffs (the B1
keep-alive rule); `ConversationPool` renders the pool when no session is live;
`EmptyChatStage`/`LibraryAndDiagnostics` cover the empty and library states. The library layer
forwards the focused seat's `taskDocumentRef` and role as resume launch context; it does not
reconstruct a leaf address.

### Conventions

Layer composition only; the stage decides which layer is visible.

### Invariants And Boundaries

The PTY layer must never unmount on transient focus changes.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stage layer components. | `EmptyChatStage`; `ConversationPool`; `PtyLayer` | dashboard/src/panels/session-cockpit/stageLayers.tsx:13-109 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Recorded task-document-plus-role launch context at the library-stage
  composition seam.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the stage
  layers module extracted from `ChatsStageBody.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
