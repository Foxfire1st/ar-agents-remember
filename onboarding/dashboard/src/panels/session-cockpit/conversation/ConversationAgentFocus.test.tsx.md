# dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The surface under test; imported at L34. [1]
- The exported scroll-key set the ArrowDown-absence pin imports; imported at L35. [2]
- The real store seeded with projections (`activeConversationStore`, `connectConversation`, `disconnectConversation`); imported at L16-L20. [3]
- The projection type + `emptyProjection` the fixtures extend; imported at L14-L15. `applyInitialPage` at L182-L195 is what copies a page's `capabilities`/`totalItems` onto the projection. [4]
- The item/identity/status/page wire types the fixtures build (incl. the `agent` ref); imported at L22-L27. [5]
- The mocked announcer side channel the visibility gate is asserted against; imported at L13, mocked at L37-L40. [6]
- `conversationIdentity` / `conversationItem` / `conversationStatus` / `conversationPage` — the builders the fixtures now use; imported at L28-L33. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## 260727-CHATS-IM-L2 Persisted-Focus And Retry Delta

The persisted-focus regression proves a valid effective child hydrates exactly once across
mount/remount while a stale stored id sends zero POSTs cit:(["hydrates a valid persisted focus once"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:297-348). The failure/retry regression
renders the server's child-scoped detail, keeps the parent projection `live` with no parent error,
retries explicitly, and clears the local error after success cit:(["child-scoped history failure"], dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx:350-391).
