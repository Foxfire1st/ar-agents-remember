# dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T11:50+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `ConversationSurface` sub-agent focus suite (R7, reworked): ArrowDown ANYWHERE on the surface
(feed article AND scroll viewport) moves DOM focus INTO the agents line and Enter opens the agent
menu — the primary path; ArrowUp from the line returns focus to the timeline; ArrowLeft/ArrowRight
cycle parent → agent 1 → … → agent N → parent as an additional path, Escape returns to the parent,
the timeline filters to the focused lane, every switch is announced politely — and a stored focus
naming an agent the roster no longer carries recomputes to the parent, never re-applied blindly.
It also pins selected-child hydration on a valid persisted focus and visible local retry without
parent stream failure.

## Code Commentary

### Logic

- **Setup** (L37-L42, L146-L171): the announcer module and `AmbientTelemetry` (which fetches on
  mount) are mocked; jsdom has no layout, so fixed geometry (`offsetHeight`/`scrollHeight`/`scrollTo`)
  is pinned so the virtualizer renders rows. The REAL `activeConversationStore` is seeded
  and reset per test.
- **Fixtures** cit:([`conversationWire`], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:33-33): a status/identity pair and four items — two parent items, a roster row
  (kind `notice`, role `system`, carrying `agent: { agentId: "t-1", nickname: "scout" }`), and one
  agent-owned message; `seed()` writes them into the store as a live projection. Since 260731-EFA-L4
  they are built with `conversationIdentity` / `conversationStatus` / `conversationItem` /
  `conversationPage` (`test/fixtures/conversationWire.ts`) rather than cast literals. Two details are
  load-bearing here. `item()` passes `turnId: undefined` EXPLICITLY, because the builder's base
  supplies `turnId: "t1"` and these fixtures deliberately carry none. And `initialPage()` — the body
  `connectRuntime`'s fetch stub serves — previously set `capabilities: {} as ConversationCapabilities`,
  an empty tree the server cannot send; it is now the full 23-leaf tree, and the page also carries
  `page.totalItems`.
- **Parent view** cit:(["parent view shows parent items + roster rows"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:172-184): the timeline shows parent items + roster rows, and the agents area
  stays ONE compact line (`1 agent · 1 running`) — the roster lives in the menu (no options, no
  viewing note) until Enter opens it.
- **ArrowDown primary path** cit:(["ArrowDown from the timeline moves focus into the agents line"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:186-211): ArrowDown from a timeline row moves DOM focus INTO the
  agents line WITHOUT switching the view; Enter opens the menu (focus on the listbox, nothing
  announced yet); Enter selects the only agent — the store records the focus, `viewing scout` is
  announced, the menu closes with focus back on the line, and the timeline filters to the agent's
  own items (its roster row included, never the parent's) with the viewing note on the line.
- **Uniform hijack** cit:(["uniform hijack"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:213-220): ArrowDown from the scroll VIEWPORT also moves focus into the
  agents line — the hijack is not article-only.
- **ArrowUp return** cit:(["ArrowUp from the agents line returns focus"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:222-233): ArrowUp from the agents line returns focus to the timeline's
  tabbable row.
- **Scroll-key contract** cit:(["no longer documents ArrowDown as a scroll key"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:235-239): the exported `OPERATOR_SCROLL_KEYS` no longer carries
  ArrowDown (PageDown/`]` remain) — the feed's scroll-key documentation matches the hijack.
- **Cycle + filter + announce** cit:(["ArrowRight focuses the agent"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:241-257): ArrowRight stores the focus, politely announces
  `viewing scout`, and filters the timeline to the agent's own items; Escape stores `undefined`,
  announces `viewing parent conversation`, and restores the parent view.
- **Wrap-around** cit:(["wraps to the parent"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:259-269): ArrowRight from the last agent wraps to the parent; ArrowLeft from
  the parent wraps to agent N.
- **Back-to-parent affordance** cit:(["back-to-parent affordance"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:271-278): the agents line's back-to-parent button returns to
  the parent view.
- **Key ownership** cit:(["ignores the focus keys"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:280-286): keys from an interactive target (the agents line, a button) do
  NOT cycle the focus.
- **Stale stored focus** cit:(["stale stored focus"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:288-295): a stored focus for an agent absent after rehydrate renders the
  parent view with no viewing note — the effective-focus honesty.
- **Hidden keep-alive** cit:(["hidden keep-alive surface"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:393-409): a `visible={false}` surface still STORES the focus switch but
  never voices it (neither polite nor assertive announcer fires).

### Invariants And Boundaries

- The suite exercises the real store and real focus primitives, so the filter/wrap/stale-focus
  assertions are non-vacuous; only the announcer side channel and the telemetry fetch are mocked.
- Timeline membership is asserted via the rendered rows' `data-row-key`, not via store
  internals — the pin is on what the reader sees.
- The ArrowDown hijack is pinned as focus-only at BOTH origins (article and viewport): the view
  must not switch until Enter selects inside the menu.
- **The page fixture never reaches the rendered surface, and the ordering is why.** All three
  `connectRuntime` cases call `connectRuntime(...)`, flush the GET (which does run
  `applyInitialPage`, and that reducer DOES copy `page.capabilities` and `page.page.totalItems` onto
  the projection — `data/conversation/reducer.ts` L182-L195), and only THEN call `seed()`, which
  overwrites `bySession[SESSION_ID]` with a projection spread from `emptyProjection(identity())` and
  carrying no `capabilities` key at all. So the surface always renders with
  `projection.capabilities === undefined`. Keep that order if you add a case: reversing it would put
  a capability tree in front of `ConversationSurface`'s `capabilities?.live.completeness` and
  `capabilities?.history` cues for the first time.

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
| The surface under test; imported at L34. | `statusRevision` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:315-315 |
| The exported scroll-key set the ArrowDown-absence pin imports; imported at L35. | `ArrowDown` | dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:114-114 |
| The real store seeded with projections (`activeConversationStore`, `connectConversation`, `disconnectConversation`); imported at L16-L20. | "export const activeConversationStore =" | dashboard/src/data/conversation/store.ts:84-84 |
| The projection type + `emptyProjection` the fixtures extend; imported at L14-L15. `applyInitialPage` at L182-L195 is what copies a page's `capabilities`/`totalItems` onto the projection. | `applyInitialPage` | dashboard/src/data/conversation/reducer.ts:168-202 |
| The item/identity/status/page wire types the fixtures build (incl. the `agent` ref); imported at L22-L27. | `agent` | dashboard/src/data/conversation/types.ts:172-172 |
| The mocked announcer side channel the visibility gate is asserted against; imported at L13, mocked at L37-L40. | `announcePolite` | dashboard/src/data/announcer.ts:33-35 |
| `conversationIdentity` / `conversationItem` / `conversationStatus` / `conversationPage` — the builders the fixtures now use; imported at L28-L33. | `conversationItem` | dashboard/src/test/fixtures/conversationWire.ts:209-226 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## 260727-CHATS-IM-L2 Persisted-Focus And Retry Delta

The persisted-focus regression proves a valid effective child hydrates exactly once across
mount/remount while a stale stored id sends zero POSTs cit:(["hydrates a valid persisted focus once"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:297-348). The failure/retry regression
renders the server's child-scoped detail, keeps the parent projection `live` with no parent error,
retries explicitly, and clears the local error after success cit:(["child-scoped history failure"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:350-391).

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the superseded `(L…)`
  prose citations with exact test-title anchors, the `n/a` table rows with exact frozen-source
  anchors, and the history `applyInitialPage` range via the scoped fixer; exact non-fixing
  check returns zero findings.

- 2026-08-01T11:50+02:00 — 260731-EFA-L4 curator: recorded the conversation-wire fixture conversion
  and repaired every case range. The two fixture details worth a reader's time are named in the
  Fixtures bullet: `item()` now writes `turnId: undefined` EXPLICITLY, because `conversationItem`'s
  base supplies `turnId: "t1"` and this suite's items deliberately carry none — a silent inheritance
  there would have changed what `resolveWorkingTurnId`-adjacent code sees; and `initialPage()`'s
  `capabilities` went from `{} as ConversationCapabilities` (a tree the server cannot send) to the
  full 23-leaf tree, with `page.totalItems` now set. That second one looked consequential, so I
  traced it instead of trusting the green run: `applyInitialPage` cit:([`applyInitialPage`], dashboard/src/data/conversation/reducer.ts:168-202) really does copy `page.capabilities` and `page.page.totalItems` onto the projection, and
  `ConversationSurface.tsx` — unchanged by this leaf — reads `capabilities?.live.completeness` at
  L319-L321 and `capabilities?.history` at L279. What makes it inert is ORDERING: all three
  `connectRuntime` cases flush the GET and then call `seed()`, which overwrites the session's
  projection with a spread of `emptyProjection(identity())` carrying no `capabilities` key, so the
  surface renders with `capabilities === undefined` both before and after this change. That ordering
  is now written into Invariants, because a future case that reversed it would be the first to put a
  capability tree in front of those two cues. Suite re-run: all cases pass. Citation repairs — every
  Logic range and both IM-L2 ranges were stale and were re-anchored on their `it`/`describe`
  (Setup L25-L31,L119-L142 → L37-L42,L146-L171; Fixtures L34-L115 → L44-L116; the eleven case ranges
  L144-L285 → L172-L296 and L393-L409; IM-L2 L311-L362 → L297-L349 and L364-L405 → L350-L392), and the
  six import-line citations were re-checked against the reshuffled import block (surface L22 → L34,
  timeline L23 → L35, store L16 → L16-L20, types L17-L21 → L22-L27). One row added for the builder
  module.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: recorded exact-once valid persisted-focus
  hydration, stale-focus non-hydration, and child-local visible failure/recovery with parent
  continuity. Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the ArrowDown-primary-path pins —
  the hijack moves DOM focus into the agents line from a timeline row AND from the scroll viewport
  (focus-only; Enter opens the menu, Enter selects and announces), the ArrowUp return to the
  timeline's tabbable row, and the exported `OPERATOR_SCROLL_KEYS` ArrowDown-absence contract; the
  parent-view pin now asserts the one-compact-line area and the stale-focus pin asserts no viewing
  note (the focus bar is gone). Re-anchored the test spans. Verification stays pinned
  (uncommitted); closeout re-stamps.
- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 surface focus
  suite — ArrowLeft/ArrowRight parent↔agents cycling with wrap-around, Escape/back-button return,
  timeline filtering to the focused lane, polite visibility-gated announcements, interactive-target
  key exclusion, and the stale-stored-focus recompute to the parent. Verification is pinned to the
  leaf base (`842b487`) because the new source file is uncommitted; closeout owns its first source
  stamp.
