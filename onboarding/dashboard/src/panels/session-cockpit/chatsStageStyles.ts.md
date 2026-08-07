# dashboard/src/panels/session-cockpit/chatsStageStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/chatsStageStyles.ts`  |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The stage body recipes. | `body`; `hiddenBehind`; `keptHidden` | dashboard/src/panels/session-cockpit/chatsStageStyles.ts:3-41 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `ChatsStageBody.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
