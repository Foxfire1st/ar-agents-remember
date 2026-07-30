# dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31` |
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
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

- **Setup** (L25-L31, L119-L142): the announcer module and `AmbientTelemetry` (which fetches on
  mount) are mocked; jsdom has no layout, so fixed geometry (`offsetHeight`/`scrollHeight`/`scrollTo`)
  is pinned so the virtualizer renders rows. The REAL `activeConversationStore` is seeded
  and reset per test.
- **Fixtures** (L34-L115): a status/identity pair and four items — two parent items, a roster row
  (kind `notice`, role `system`, carrying `agent: { agentId: "t-1", nickname: "scout" }`), and one
  agent-owned message; `seed()` writes them into the store as a live projection.
- **Parent view** (L144-L157): the timeline shows parent items + roster rows, and the agents area
  stays ONE compact line (`1 agent · 1 running`) — the roster lives in the menu (no options, no
  viewing note) until Enter opens it.
- **ArrowDown primary path** (L158-L184): ArrowDown from a timeline row moves DOM focus INTO the
  agents line WITHOUT switching the view; Enter opens the menu (focus on the listbox, nothing
  announced yet); Enter selects the only agent — the store records the focus, `viewing scout` is
  announced, the menu closes with focus back on the line, and the timeline filters to the agent's
  own items (its roster row included, never the parent's) with the viewing note on the line.
- **Uniform hijack** (L185-L193): ArrowDown from the scroll VIEWPORT also moves focus into the
  agents line — the hijack is not article-only.
- **ArrowUp return** (L194-L206): ArrowUp from the agents line returns focus to the timeline's
  tabbable row.
- **Scroll-key contract** (L207-L212): the exported `OPERATOR_SCROLL_KEYS` no longer carries
  ArrowDown (PageDown/`]` remain) — the feed's scroll-key documentation matches the hijack.
- **Cycle + filter + announce** (L213-L230): ArrowRight stores the focus, politely announces
  `viewing scout`, and filters the timeline to the agent's own items; Escape stores `undefined`,
  announces `viewing parent conversation`, and restores the parent view.
- **Wrap-around** (L231-L242): ArrowRight from the last agent wraps to the parent; ArrowLeft from
  the parent wraps to agent N.
- **Back-to-parent affordance** (L243-L251): the agents line's back-to-parent button returns to
  the parent view.
- **Key ownership** (L252-L259): keys from an interactive target (the agents line, a button) do
  NOT cycle the focus.
- **Stale stored focus** (L260-L268): a stored focus for an agent absent after rehydrate renders the
  parent view with no viewing note — the effective-focus honesty.
- **Hidden keep-alive** (L269-L285): a `visible={false}` surface still STORES the focus switch but
  never voices it (neither polite nor assertive announcer fires).

### Invariants And Boundaries

- The suite exercises the real store and real focus primitives, so the filter/wrap/stale-focus
  assertions are non-vacuous; only the announcer side channel and the telemetry fetch are mocked.
- Timeline membership is asserted via the rendered rows' `data-row-key`, not via store
  internals — the pin is on what the reader sees.
- The ArrowDown hijack is pinned as focus-only at BOTH origins (article and viewport): the view
  must not switch until Enter selects inside the menu.

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
| The surface under test. | L22 | [ConversationSurface.tsx](ConversationSurface.tsx.md) |
| The exported scroll-key set the ArrowDown-absence pin imports. | L23 | [ConversationTimeline.tsx](ConversationTimeline.tsx.md) |
| The real store seeded with projections (`agentFocusBySession`, `setAgentFocus`, `reset`). | L16 | [../../../data/conversation/store.ts](../../../data/conversation/store.ts.md) |
| The projection type + `emptyProjection` the fixtures extend. | L14-L15 | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts.md) |
| The item/identity/status wire types the fixtures build (incl. the `agent` ref). | L17-L21 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts.md) |
| The mocked announcer side channel the visibility gate is asserted against. | L13 | [../../../data/announcer.ts](../../../data/announcer.ts.md) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## 260727-CHATS-IM-L2 Persisted-Focus And Retry Delta

The persisted-focus regression proves a valid effective child hydrates exactly once across
mount/remount while a stale stored id sends zero POSTs (L311-L362). The failure/retry regression
renders the server's child-scoped detail, keeps the parent projection `live` with no parent error,
retries explicitly, and clears the local error after success (L364-L405).

## Update History

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
