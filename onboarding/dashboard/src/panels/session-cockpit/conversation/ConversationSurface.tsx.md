# dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Surface shell, focus model + keys incl. the ArrowDown hijack, announcer discipline, capability cues, agents strip, timeline mount. | `ConversationSurface` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-341 |
| The roster/focus primitives this surface composes (`deriveAgents`, `effectiveAgentFocus`, `cycleAgentFocus`, `filterItemsForFocus`). | `deriveAgents`; `effectiveAgentFocus`; `cycleAgentFocus`; `filterItemsForFocus` | dashboard/src/data/conversation/agents.ts:71-86; dashboard/src/data/conversation/agents.ts:93-103; dashboard/src/data/conversation/agents.ts:106-112; dashboard/src/data/conversation/agents.ts:119-127 |
| The reconstructable store's `agentFocusBySession` focus state and the `setAgentFocus` writer this surface reads/writes. | `setAgentFocus` | dashboard/src/data/conversation/store.ts:69-69 |
| The `live`-delivery flag the announcers gate on. | `lastAppliedDelivery` | dashboard/src/data/conversation/reducer.ts:58-58 |
| The shared polite/assertive announcer store. | `announcePolite` | dashboard/src/data/announcer.ts:33-35 |
| The sub-agents strip (one compact line + listbox menu), the one feed timeline, the reconnect banner, the ambient telemetry, and the capability-reason primitive. | `AgentsArea`; `ConversationTimeline`; `ConversationReconnect`; `AmbientTelemetry`; `CapabilityReason` | dashboard/src/panels/session-cockpit/conversation/AgentsArea.tsx:180-247; dashboard/src/panels/session-cockpit/conversation/AmbientTelemetry.tsx:63-115; dashboard/src/panels/session-cockpit/conversation/ConversationReconnect.tsx:68-102; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/ConversationTimeline.tsx:56-106; dashboard/src/panels/session-cockpit/conversation/primitives.tsx:140-158 |
| The surface-level focus-cycling/filtering/Esc/hijack suite. | "ConversationSurface agent focus" | dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:144-410 |
| The persisted hide-thinking preference. | `thinkingPreferenceStore` | dashboard/src/data/conversation/thinkingPreference.ts:25-36 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

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

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the conversationSurfaceParts/Styles extraction. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:15+02:00 — 260731-EFA-L6 S18-B17 curator: the source had drifted ~2-26 lines past
  every inline cite. Rewrote all nine flagged `(L…)` prose cites as cit forms with re-measured
  frozen-source ranges, did the same for the four drifted but unflagged bullets (focus keys,
  announcer discipline, first-connect failure, capability cues — including the stale `surfaceRef`
  L113/L265 → 125/290), and repaired the eight Repo-Internal rows whose links pointed at `.md`
  cards instead of code: exact anchors and plain path:line-line sources for the shell, the four
  roster/focus primitives, the store focus read/write pair (wording narrowed — the older-paging and
  scroll-anchor writers are outside the cited store span), `lastAppliedDelivery`, the announcer
  store, the five composed components, the focus test suite, and the thinking preference store.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations, both read back
  against the current source. `ownsAgentFocusKeys` L74-L84 → L88-L98 (L74-L84 now sits inside the
  tail of the `agentHistoryError` css recipe plus the head of the focus-keys block comment);
  `applyAgentFocus` L144-L159 → L163-L177 (L144-L159 now covers the
  sub-agent-focus derivation block, not the callback). Both claims are unchanged and still true.
  NOT fixed (beyond this worklist): the rest of the Logic bullets drifted the same way when the
  IM-L2 hydration/error work landed — store reads L107-L133 → L121-L143, sub-agent focus model
  L135-L143 → L145-L161, focus keys L160-L191 → L187-L221 with `surfaceRef` L113/L265 → L127/L292,
  announcer discipline L196-L220 → L223-L247, stream-phase L222-L236 → L249-L261, first-connect
  failure L238-L251 → L263-L275, capability cues L252-L261 → L277-L287 (rendered at L319-L327),
  toolbar L269-L307 → L296-L328, agents strip L308-L310 → L335-L337, empty-vs-timeline L312-L337 →
  L355-L379, and the self row's L86-L338 → L100-L382 (file is 383 lines). The two IM-L2 delta
  citations (L145-L185, L335-L354) are current.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented effective-focus-driven
  one-shot hydration, persisted-versus-stale focus behavior, visible child-local error/retry, and
  unchanged parent stream authority. Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent navigation rework —
  the uniform ArrowDown hijack (feed article AND scroll viewport) moving DOM focus INTO the
  agents line as the primary path (the line owns Enter/menu; ArrowUp from the line returns focus
  to the timeline's tabbable row), ArrowLeft/ArrowRight cycling kept as an additional path, the
  surface-owned focus bar DELETED (the agents line now carries the viewing note + back-to-parent
  affordance), and `surfaceRef` added for the hijack target. Re-anchored every line citation
  against the post-rework source. Verification stays pinned (uncommitted); closeout re-stamps.
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
