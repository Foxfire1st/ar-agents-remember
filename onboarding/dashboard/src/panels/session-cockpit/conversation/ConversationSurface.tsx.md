# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T05:30+02:00 |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34` |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The active-conversation **surface** (design §12.1): the page/stream state and scroll shell around the
one `role="feed"` timeline. It reads the reconstructable store (never a fixture authority), renders the
honest reconnect/failure states, drives revision-keyed announcers that stay SILENT during
replay/hydration (§14.2), and exposes the global thinking toggle, the ambient telemetry chips, and the
live/history capability CUES (§10.2, R11). It owns no data/paging/cursor logic — the store/reducer do.

## Code Commentary

### Logic

- **Store reads** (L65-L78): `useActiveConversation` selects the session projection and its typed
  `errorBySession` reason; `items` is the materialized ordered list (`orderedItemIds.map`).
- **Announcer discipline** (L80-L104, §14.2/F21): status announcers key on `(state + revision)` and
  fire ONLY when `projection.lastAppliedDelivery === "live"` — hydration/re-page (delivery `replay` or
  the `undefined` fresh-hydration case) updates the store WITHOUT announcing. `failed` → assertive
  `turn failed`; `ready` → polite `response complete`; process `disconnected` → assertive. Stream-phase
  transitions (L106-L117) politely announce `reconnecting` / `re-syncing history` once per phase.
- **First-connect failure** (L119-L131, F15): with no projection yet, the surface renders
  `ConversationReconnect` carrying the typed `routeError.detail` (honest reason, never a generic
  message).
- **Capability cues (R11, 260718-CHATS-L5P)** (F13): the always-visible italic `history: <reason>` note
  div is GONE. The offending history capability (tool details first, then overall completeness) is
  selected as `historyCapability` and rendered through `CapabilityReason` with `label="history"` INSIDE
  the toolbar; the live-completeness cue likewise carries `label="live"`. Each cue shows only the
  one-word state (`history partial`, `live unavailable`) with the exact server reason behind hover
  (`title`) — the implementation-jargon paragraph never owns above-the-fold chrome (A3). The
  `history-completeness-note` testid now wraps the history cue (not the removed div).
- **Toolbar** (L142-L171): thinking toggle (`thinkingPreferenceStore`), a `terminal diagnostics`
  opener, `AmbientTelemetry` (keyed on `status.revision`), and the live + history capability cues above.
- **Empty vs timeline** (L183-L198): an empty live conversation shows `No messages yet — send one from
  the composer below.` (A1); otherwise it mounts `ConversationTimeline` with `busy` derived from
  `connecting`/`gap`, wiring `onLoadOlder` and the scroll-anchor recorder.

### Invariants And Boundaries

- Only a `live`-delivered transition may voice an announcer; hydration/replay is silent.
- The surface reads the store projection and NEVER a fixture or a second authority.
- The reason shown on a failure is the server's typed reason, not a fabricated calm.
- Data/paging/cursor logic stays in the reducer/store; this file is presentation + announcer only.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Surface shell, announcer discipline, history note, empty state, timeline mount. | L56-L201 | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The reconstructable store + older-paging + scroll-anchor writers this surface reads. | — | [../../../data/conversation/store.ts](../../../data/conversation/store.ts) |
| The `live`-delivery flag the announcers gate on. | — | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts) |
| The shared polite/assertive announcer store. | — | [../../../data/announcer.ts](../../../data/announcer.ts) |
| The one feed timeline, the reconnect banner, the ambient telemetry, and the capability-reason primitive. | — | [ConversationTimeline.tsx](ConversationTimeline.tsx) · [ConversationReconnect.tsx](ConversationReconnect.tsx) · [AmbientTelemetry.tsx](AmbientTelemetry.tsx) · [primitives.tsx](primitives.tsx) |
| The persisted hide-thinking preference. | — | [../../../data/conversation/thinkingPreference.ts](../../../data/conversation/thinkingPreference.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded R11 progressive disclosure — the
  always-visible `history: <reason>` note div was removed; the history and live capabilities now render
  as short `CapabilityReason` CUES (labeled `history`/`live`, state word visible, full reason in the
  hover `title`) inside the toolbar. Announcer discipline, typed first-connect reason, empty state, and
  timeline mount unchanged. Verification pinned to the leaf base (`352d5cd`) until closeout stamps the
  candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the active-conversation
  surface — the page/stream shell with `live`-only announcers (silent on replay/hydration, F21), the
  typed first-connect reason (F15), the failing-capability history note (F13), and the thinking/telemetry
  toolbar. Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
