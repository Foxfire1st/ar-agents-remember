# dashboard/src/panels/session-cockpit/chatsStageStyles.ts

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The Chats-stage body styles extracted from `ChatsStageBody.tsx` by the
260731-EFA-L8 split. Owns the stage body layout, the hidden-behind/kept-hidden
states for the PTY keep-alive handoff, and the conversation pool.

## Code Commentary

### Logic

`body` is the stage container; `hiddenBehind`/`keptHidden` implement the transient
hidden state while the PTY layer stays mounted through smart-focus handoff (the
keep-alive fix); `pool` styles the conversation pool surface.

### Conventions

Tokens only; no animation.

### Invariants And Boundaries

The hidden styles must never unmount content — visibility only.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The stage body recipes. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
