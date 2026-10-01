# dashboard/src/panels/session-cockpit/stageLayers.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The stage layer components. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
