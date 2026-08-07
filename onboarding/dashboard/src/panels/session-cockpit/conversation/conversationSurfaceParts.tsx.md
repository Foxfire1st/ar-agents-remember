# dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The conversation-surface render parts, extracted from `ConversationSurface.tsx` by
the 260731-EFA-L8 split. Owns the projection-failed surface, toolbar, agent-history
error banner, timeline section, and the history-capability resolver.

## Code Commentary

### Logic

`SurfaceToolbar` renders the surface controls; `TimelineSection` hosts the timeline
with its slots; `resolveHistoryCapability` decides whether agent-history rendering
applies; the error banner surfaces honest history failures.

### Conventions

Presentational parts; announcements/paging stay in the surface controller.

### Invariants And Boundaries

The timeline section must keep the feed mounted per the keep-alive rules.

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
| The surface parts. | `SurfaceToolbar`; `TimelineSection`; `resolveHistoryCapability` | dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx:48-130; dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx:131-186; dashboard/src/panels/session-cockpit/conversation/conversationSurfaceParts.tsx:187-196 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the surface
  parts module extracted from `ConversationSurface.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
