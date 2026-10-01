# dashboard/src/panels/terminalSession.ts

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The xterm session/stream machinery extracted from `Terminal.tsx` by the
260731-EFA-L8 split. Owns the terminal creation, wheel/application-scroll input
translation, copy shortcut handling, and the terminal stream hook contract
(`TerminalStreamHooks`).

## Code Commentary

### Logic

`createTerminal` builds the xterm instance; `wheelScrollLines` /
`applicationScrollInput` translate wheel deltas into the PTY's scroll sequences;
`hasViewportScrollback` detects DOM-only viewports; the hooks interface keeps the
component thin. The headless-focus fix lives in the component, delegating focus via
rAF to `termRef.focus()`.

### Conventions

PTY bytes flow through the shared data layer; this module owns the xterm adapter.

### Invariants And Boundaries

The terminal keeps its mounted scrollback across view switches; reattach performs at
most one explicit socket reattach per changed serving boot.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The stream hooks contract and input translation. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
