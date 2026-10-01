# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## 260731-EFA-L8 Change

The surface render parts moved to `conversationSurfaceParts.tsx` and styles to
`conversationSurfaceStyles.ts`; this file keeps the announcements, paging, and
agents-line wiring. Behavior is unchanged.

## Purpose

The active-conversation **surface** (design §12.1): the page/stream state and scroll shell around the
one `role="feed"` timeline. It reads the reconstructable store (never a fixture authority), renders the
honest reconnect/failure states, drives revision-keyed announcers that stay SILENT during
replay/hydration (§14.2), and exposes the global thinking toggle, the ambient telemetry chips, and the
live/history capability CUES (§10.2, R11). It also owns the **sub-agent focus
  model** (R7, reworked): the roster-derived focus that filters the timeline to one agent's lane
and triggers bounded native-history hydration for only that effective selection,
reached primarily by the uniform ArrowDown hijack INTO the agents line (the Claude Code sub-agent
navigation model), with ArrowLeft/ArrowRight cycling and Escape returning as additional paths. It
owns no data/paging/cursor logic — the store/reducer do.

## Code Commentary

### Logic

- **Store reads** cit:([`orderedItemIds`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:119-141): `useActiveConversation` selects the session projection and its typed
  `errorBySession` reason; `items` is the materialized ordered list (`orderedItemIds.map`).
- **Sub-agent focus model (R7)** cit:(["effectiveAgentFocus", "const storedAgentFocus = useActiveConversation(", "const storedAgentFocus = useActiveConversation(", "const storedAgentFocus = useActiveConversation(", `storedAgentFocus`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:163-167; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:22-22): `storedAgentFocus` reads the
  LRU-surviving `agentFocusBySession` entry; `agents = deriveAgents(items)` derives the roster from
  projection evidence only; `agentFocus = effectiveAgentFocus(stored, agents)` is NEVER the stored
  value applied blindly — a rehydrated projection without that agent honestly falls back to the
  parent conversation; `focusedItems = filterItemsForFocus(items, agentFocus)` yields the lane the
  timeline renders.
- **Focus keys** cit:([`onSurfaceKeyDown`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:294-298) (the Claude Code sub-agent navigation model): the surface root's
  `onKeyDown` handles FOUR keys. ArrowDown ANYWHERE on the surface (feed article AND scroll
  viewport — one uniform hijack, cit:(["surfaceRef.current?.querySelector<HTMLElement>("[data-agents-line]")?.focus();", `, `], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:90-90; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-100)?.focus();`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:90-90; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-100)?.focus();`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:90-90; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-100)?.focus();""], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:90-90; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-100)?.focus();"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:90-90; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:100-100)) moves DOM focus INTO the agents line when
  the roster is non-empty — the primary sub-agent path; the line owns Enter/menu from there and
  ArrowUp from the line returns focus to the timeline's tabbable row. ArrowLeft/ArrowRight cycle
  parent → agent 1 → … → agent N → parent (`cycleAgentFocus`) as an additional path, and Escape
  returns to the parent. `ownsAgentFocusKeys` cit:([`ownsAgentFocusKeys`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:88-98) (including its documenting block
  comment) yields the keys to editable/interactive targets —
  input/textarea/select/contentEditable, or anything inside
  `button, a, pre, [role='group'], .cm-editor` — the same exclusion discipline the feed's own
  navigation uses.
- **`applyAgentFocus`** cit:([`applyAgentFocus`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:182-197): writes the store via `setAgentFocus`, then announces politely
  (`viewing <label>` / `viewing parent conversation`) ONLY when the surface is visible — a hidden
  keep-alive surface never voices an operator action it did not see.
- **Announcer discipline** cit:(["const live = projection?.lastAppliedDelivery === \"live\";"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:231-231) (§14.2/F21): status announcers key on `(state + revision)` and
  fire ONLY when `projection.lastAppliedDelivery === "live"` — hydration/re-page (delivery `replay` or
  the `undefined` fresh-hydration case) updates the store WITHOUT announcing. `failed` → assertive
  `turn failed`; `ready` → polite `response complete`; process `disconnected` → assertive. Stream-phase
  transitions cit:(["re-syncing history"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:265-265) politely announce `reconnecting` / `re-syncing history` once per phase.
- **First-connect failure** cit:(["import { ConversationReconnect } from \"./ConversationReconnect\";"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:38-38; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:16-16) (F15): with no projection yet, the surface renders
  `ConversationReconnect` carrying the typed `routeError.detail` (honest reason, never a generic
  message).
- **Capability cues (R11)** cit:([`historyCapability`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:313-315) (F13): the always-visible italic `history: <reason>` note
  div is GONE. The offending history capability (tool details first, then overall completeness) is
  selected as `historyCapability` and rendered through `CapabilityReason` with `label="history"` INSIDE
  the toolbar; the live-completeness cue likewise carries `label="live"`. Each cue shows only the
  one-word state (`history partial`, `live unavailable`) with the exact server reason behind hover
  (`title`) — the implementation-jargon paragraph never owns above-the-fold chrome (A3). The
  `history-completeness-note` testid now wraps the history cue (not the removed div).
- **Toolbar** cit:([`thinkingPreferenceStore`], dashboard/src/data/conversation/thinkingPreference.ts:25-36): thinking toggle (`thinkingPreferenceStore`), a `terminal diagnostics`
  opener, `AmbientTelemetry` (keyed on `status.revision`), and the live + history capability cues above.
- **Agents strip** cit:(["import { AgentsArea } from \"./AgentsArea\";", "import { AgentsArea } from \"./AgentsArea\";", "import { AgentsArea } from \"./AgentsArea\";", "import { AgentsArea } from \"./AgentsArea\";"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:334-336; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:37-37; dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:16-16): `AgentsArea` mounts above the timeline with the derived roster and
  the effective focus. The area owns the whole compact line — the count chip plus, in an agent
  view, the viewing note and the `← back to parent conversation` affordance; the surface's own
  focus bar is deleted.
- **Empty vs timeline** cit:([`ConversationWelcome`], dashboard/src/panels/session-cockpit/conversation/ConversationWelcome.tsx:154-206): the timeline receives `focusedItems`; `totalItems` is passed
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
- The ArrowDown hijack is UNIFORM (feed article and scroll viewport alike) and focus-only: it
  moves DOM focus into the agents line without switching the view; the feed keeps
  PageUp/PageDown scrolling and `[`/`]` row moves (ArrowDown is no longer a scroll key there).
- The surface reads the store projection and NEVER a fixture or a second authority.
- The reason shown on a failure is the server's typed reason, not a fabricated calm.
- Data/paging/cursor logic stays in the reducer/store; this file is presentation + announcer only.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Surface shell, focus model + keys incl. the ArrowDown hijack, announcer discipline, capability cues, agents strip, timeline mount. [1]
- The roster/focus primitives this surface composes (`deriveAgents`, `effectiveAgentFocus`, `cycleAgentFocus`, `filterItemsForFocus`). [2]
- The reconstructable store's `agentFocusBySession` focus state and the `setAgentFocus` writer this surface reads/writes. [3]
- The `live`-delivery flag the announcers gate on. [4]
- The shared polite/assertive announcer store. [5]
- The sub-agents strip (one compact line + listbox menu), the one feed timeline, the reconnect banner, the ambient telemetry, and the capability-reason primitive. [6]
- The surface-level focus-cycling/filtering/Esc/hijack suite. [7]
- The persisted hide-thinking preference. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Current Structured-Surface Maintenance

The structured surface always retains its timeline well, including an empty live conversation; the
empty state is now `ConversationWelcome` inside that well and receives real process state for its
readiness wording. It tracks scroll memory per session, restores only when layout geometry is active,
and suppresses live-region announcements from hidden keep-alive surfaces while still tracking their
projection state.

## 260727-CHATS-IM-L2 Effective-Focus Hydration Delta

The surface derives history state from the validated effective focus and runs hydration from an
effect keyed by that focus/session/bridge epoch cit:(["hydrateAgentConversation"], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:28-28). A valid persisted focus therefore
hydrates after page load or remount even without a click; a stale focus becomes parent and sends
no request. Runtime singleflight makes the remount path exactly once.

A failed selected-child route renders its typed detail beside a retry action cit:(["conversation-agent-history-retry"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:385-385). Retrying
addresses only that child; the parent projection and reconnect surface remain live. The component
still owns presentation/focus only—the store owns request orchestration and resource bounds.
