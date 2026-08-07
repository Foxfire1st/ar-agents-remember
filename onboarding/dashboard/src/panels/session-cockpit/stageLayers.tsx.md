# dashboard/src/panels/session-cockpit/stageLayers.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/stageLayers.tsx`      |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
`EmptyChatStage`/`LibraryAndDiagnostics` cover the empty and library states.

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

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the stage
  layers module extracted from `ChatsStageBody.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
