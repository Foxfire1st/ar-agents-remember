# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The active-conversation **surface** (design §12.1): the page/stream state and scroll shell around the
one `role="feed"` timeline. It reads the reconstructable store (never a fixture authority), renders the
honest reconnect/failure states, drives revision-keyed announcers that stay SILENT during
replay/hydration (§14.2), and exposes the global thinking toggle, the ambient telemetry chips, and the
live/history capability CUES (§10.2, R11). It also owns the **sub-agent focus
model** (R7): the roster-derived focus that filters the timeline to one agent's lane, cycled from the
keyboard with the Claude Code agents-view precedent. It owns no data/paging/cursor logic — the
store/reducer do.

## Code Commentary

### Logic

- **Store reads** (L111-L132): `useActiveConversation` selects the session projection and its typed
  `errorBySession` reason; `items` is the materialized ordered list (`orderedItemIds.map`).
- **Sub-agent focus model (R7)** (L134-L145): `storedAgentFocus` reads the
  LRU-surviving `agentFocusBySession` entry; `agents = deriveAgents(items)` derives the roster from
  projection evidence only; `agentFocus = effectiveAgentFocus(stored, agents)` is NEVER the stored
  value applied blindly — a rehydrated projection without that agent honestly falls back to the
  parent conversation; `focusedItems = filterItemsForFocus(items, agentFocus)` yields the lane the
  timeline renders.
- **Focus keys** (L163-L185, the Claude Code agents-view precedent): the surface root's `onKeyDown`
  cycles ArrowLeft/ArrowRight through parent → agent 1 → … → agent N → parent (`cycleAgentFocus`),
  and Escape returns to the parent. `ownsAgentFocusKeys` (L78-L88) yields the keys to
  editable/interactive targets — input/textarea/select/contentEditable, or anything inside
  `button, a, pre, [role='group'], .cm-editor` — the same exclusion discipline the feed's own
  navigation uses.
- **`applyAgentFocus`** (L147-L161): writes the store via `setAgentFocus`, then announces politely
  (`viewing <label>` / `viewing parent conversation`) ONLY when the surface is visible — a hidden
  keep-alive surface never voices an operator action it did not see.
- **Announcer discipline** (L188-L211, §14.2/F21): status announcers key on `(state + revision)` and
  fire ONLY when `projection.lastAppliedDelivery === "live"` — hydration/re-page (delivery `replay` or
  the `undefined` fresh-hydration case) updates the store WITHOUT announcing. `failed` → assertive
  `turn failed`; `ready` → polite `response complete`; process `disconnected` → assertive. Stream-phase
  transitions (L214-L225) politely announce `reconnecting` / `re-syncing history` once per phase.
- **First-connect failure** (L227-L239, F15): with no projection yet, the surface renders
  `ConversationReconnect` carrying the typed `routeError.detail` (honest reason, never a generic
  message).
- **Capability cues (R11)** (F13): the always-visible italic `history: <reason>` note
  div is GONE. The offending history capability (tool details first, then overall completeness) is
  selected as `historyCapability` and rendered through `CapabilityReason` with `label="history"` INSIDE
  the toolbar; the live-completeness cue likewise carries `label="live"`. Each cue shows only the
  one-word state (`history partial`, `live unavailable`) with the exact server reason behind hover
  (`title`) — the implementation-jargon paragraph never owns above-the-fold chrome (A3). The
  `history-completeness-note` testid now wraps the history cue (not the removed div).
- **Toolbar** (L255-L287): thinking toggle (`thinkingPreferenceStore`), a `terminal diagnostics`
  opener, `AmbientTelemetry` (keyed on `status.revision`), and the live + history capability cues above.
- **Agents strip + focus bar** (L294-L309): `AgentsArea` mounts above the timeline with the derived
  roster and the effective focus; while focused, a `conversation-agent-focus-bar` carries the
  `← back to parent conversation` button and a `viewing <label>` note.
- **Empty vs timeline** (L310-L334): the timeline receives `focusedItems`; `totalItems` is passed
  only when unfocused (a focused lane's count is not the server's total, so the honest-total
  contract stays intact). An empty live conversation shows the `ConversationWelcome` when unfocused
  (A1); a focused lane with no evidence shows `no evidence from <label> yet` instead — never the
  parent welcome. `busy` is derived from `connecting`/`gap`, wiring `onLoadOlder` and the
  scroll-anchor recorder.

### Invariants And Boundaries

- Only a `live`-delivered transition may voice an announcer; hydration/replay is silent — and a
  focus switch is voiced only from a visible surface.
- The stored agent focus is never applied blindly; the effective focus is recomputed against the
  live roster, so stale focus honestly degrades to the parent view.
- The focus keys never fire from editable/interactive targets (composer, buttons, overflow regions,
  code blocks).
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
| Surface shell, focus model + keys, announcer discipline, capability cues, agents strip, focus bar, timeline mount. | L90-L337 | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The roster/focus primitives this surface composes (`deriveAgents`, `effectiveAgentFocus`, `cycleAgentFocus`, `filterItemsForFocus`). | L11-L16 | [../../../data/conversation/agents.ts](../../../data/conversation/agents.ts) |
| The reconstructable store + older-paging + scroll-anchor writers + `agentFocusBySession`/`setAgentFocus` this surface reads/writes. | L17-L24 | [../../../data/conversation/store.ts](../../../data/conversation/store.ts) |
| The `live`-delivery flag the announcers gate on. | — | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts) |
| The shared polite/assertive announcer store. | — | [../../../data/announcer.ts](../../../data/announcer.ts) |
| The sub-agents strip, the one feed timeline, the reconnect banner, the ambient telemetry, and the capability-reason primitive. | — | [AgentsArea.tsx](AgentsArea.tsx) · [ConversationTimeline.tsx](ConversationTimeline.tsx) · [ConversationReconnect.tsx](ConversationReconnect.tsx) · [AmbientTelemetry.tsx](AmbientTelemetry.tsx) · [primitives.tsx](primitives.tsx) |
| The surface-level focus-cycling/filtering/Esc suite. | — | [ConversationAgentFocus.test.tsx](ConversationAgentFocus.test.tsx) |
| The persisted hide-thinking preference. | — | [../../../data/conversation/thinkingPreference.ts](../../../data/conversation/thinkingPreference.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Current Structured-Surface Maintenance

The structured surface always retains its timeline well, including an empty live conversation; the
empty state is now `ConversationWelcome` inside that well and receives real process state for its
readiness wording. It tracks scroll memory per session, restores only when layout geometry is active,
and suppresses live-region announcements from hidden keep-alive surfaces while still tracking their
projection state.

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the R7 sub-agent focus model —
  `storedAgentFocus` → `deriveAgents` → `effectiveAgentFocus` (never applied blindly; stale focus
  falls back to the parent), `filterItemsForFocus` driving the timeline, the ArrowLeft/ArrowRight/Escape
  focus keys with the interactive-target exclusion list, the polite visibility-gated `viewing <label>`
  announcements, the `AgentsArea` mount, the focus bar with `← back to parent conversation`, and the
  focused-lane empty note replacing the welcome. All pre-L7 line citations re-verified against the
  current source. The L7 source is uncommitted; lastVerified* stays at the leaf base and closeout
  re-stamps verification.
- 2026-07-24T13:17:17Z — Curator: corrected empty-well, process-readiness, scroll-memory, and
  hidden-announcement invariants; verification fields remain pre-commit.

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
