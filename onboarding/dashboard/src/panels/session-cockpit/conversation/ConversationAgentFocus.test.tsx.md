# dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationAgentFocus.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The `ConversationSurface` sub-agent focus suite (R7): ArrowLeft/ArrowRight cycle
parent → agent 1 → … → agent N → parent, Escape returns to the parent, the timeline filters to the
focused lane, every switch is announced politely — and a stored focus naming an agent the roster no
longer carries recomputes to the parent, never re-applied blindly.

## Code Commentary

### Logic

- **Setup** (L21-L26, L115-L138): the announcer module and `AmbientTelemetry` (which fetches on
  mount) are mocked; jsdom has no layout, so fixed geometry (`offsetHeight`/`scrollHeight`/`scrollTo`,
  L115-L126) is pinned so the virtualizer renders rows. The REAL `activeConversationStore` is seeded
  and reset per test.
- **Fixtures** (L30-L101): a status/identity pair and four items — two parent items, a roster row
  (kind `notice`, role `system`, carrying `agent: { agentId: "t-1", nickname: "scout" }`), and one
  agent-owned message; `seed()` writes them into the store as a live projection.
- **Parent view** (L140-L148): the timeline shows parent items + roster rows, the agents area lists
  the roster (`1 agent · 1 running`, label `scout`), and no focus bar renders.
- **Cycle + filter + announce** (L150-L166): ArrowRight stores the focus, politely announces
  `viewing scout`, and filters the timeline to the agent's own items — its roster row included,
  never the parent's; Escape stores `undefined`, announces `viewing parent conversation`, and
  restores the parent view.
- **Wrap-around** (L168-L178): ArrowRight from the last agent wraps to the parent; ArrowLeft from
  the parent wraps to agent N.
- **Back-to-parent affordance** (L180-L187): the focus bar's button returns to the parent view.
- **Key ownership** (L189-L195): keys from an interactive target (an agents-area row, a button) do
  NOT cycle the focus.
- **Stale stored focus** (L197-L204): a stored focus for an agent absent after rehydrate renders the
  parent view with no focus bar — the effective-focus honesty.
- **Hidden keep-alive** (L206-L222): a `visible={false}` surface still STORES the focus switch but
  never voices it (neither polite nor assertive announcer fires).

### Invariants And Boundaries

- The suite exercises the real store and real focus primitives, so the filter/wrap/stale-focus
  assertions are non-vacuous; only the announcer side channel and the telemetry fetch are mocked.
- Timeline membership is asserted via the rendered rows' `data-row-key` (L107-L111), not via store
  internals — the pin is on what the reader sees.

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
| The surface under test. | L19 | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The real store seeded with projections (`agentFocusBySession`, `setAgentFocus`, `reset`). | L13 | [../../../data/conversation/store.ts](../../../data/conversation/store.ts) |
| The projection type + `emptyProjection` the fixtures extend. | L11-L12 | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts) |
| The item/identity/status wire types the fixtures build (incl. the `agent` ref). | L14-L18 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The mocked announcer side channel the visibility gate is asserted against. | L10 | [../../../data/announcer.ts](../../../data/announcer.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: created the sidecar for the R7 surface focus
  suite — ArrowLeft/ArrowRight parent↔agents cycling with wrap-around, Escape/back-button return,
  timeline filtering to the focused lane, polite visibility-gated announcements, interactive-target
  key exclusion, and the stale-stored-focus recompute to the parent. Verification is pinned to the
  leaf base (`842b487`) because the new source file is uncommitted; closeout owns its first source
  stamp.
