# dashboard/src/panels/terminalSession.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/terminalSession.ts`                   |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stream hooks contract and input translation. | `TerminalStreamHooks`; `createTerminal`; `wheelScrollLines` | dashboard/src/panels/terminalSession.ts:17-50; dashboard/src/panels/terminalSession.ts:84-130; dashboard/src/panels/terminalSession.ts:31-50 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  terminal-session module extracted from `Terminal.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
