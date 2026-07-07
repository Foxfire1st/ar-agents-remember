# dashboard/src/panels/SessionList.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionList.tsx`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-07T22:21+02:00                           |
| lastVerifiedCommitHash | `2c464cf4c29b60165fecae722bf76c307aaac6f1`       |
| lastVerifiedCommitDate | 2026-07-07T22:59:19+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **session switcher** (slice 6e-2c): the open terminal/chat sessions as a left-rail vertical list,
replacing the Chats view's old horizontal tab strip. Presentational + controlled — it takes
`sessions`, `activeId`, `onSelect`, and `onTerminate` and owns no state, so `Chats` keeps
the session lifecycle while `SessionList` only renders + reports. Selecting a row switches the active
session; each row carries one explicit destructive Terminate control. Task 11 adds a compact lifecycle
tag when a session is attached to a lifecycle for gate-response routing, and task 22 adds a compact
non-running status tag for restored exited rows. The Task 22 follow-up removed the old local-only Hide
action; End is now the only per-row command. Slice L5 adds an optional `leafNameFor` resolver so a
leaf-bound session's row appends the attached leaf's name ("who works on what"). 260703-L14 adds the
**G1 command tree**: an optional `grouped` prop (the `data/sessionGroups` model) renders sessions
inside collapsible groups — the sprint's command deck (gold insignia) on top, one group per claimed
master (purple insignia + one 22px indent step when commanded), landed work in one
collapsed-by-default archive — while unattached sessions keep the flat placement below; with no
`grouped` model or zero derived groups the component renders the pre-L14 flat list unchanged. Rows
with `spawnRole` provenance also wear a role chip; HFX-L6/L6R2 makes `architect` a known gold
owner-tier chip alongside the backend command seats, and L6R4 makes `curator` a known role chip
instead of the unknown/default path.

## Code Commentary

### Logic

A React Aria `GridList` (`selectionMode="single"`, `items={sessions}`, render-fn children keyed by
`session.id`). `selectedKeys={activeId ? [activeId] : []}` reflects the active session;
`onSelectionChange` reads the single key (`[...keys][0]`, the `LifecycleList` idiom) and calls
`onSelect` only for a string key — so toggling the active row to empty is ignored and selection never
clears itself. Each `GridListItem` renders the label `<span>`, an optional `session.lifecycleId` badge,
an optional `session.status` badge for non-running sessions, and an action group with one native
button: End (`onTerminate(id)`, destructive backend termination). The button handlers stop
pointer/click propagation so ending a row is not confused with `GridListItem` selection.
Slice L5 adds the optional `leafNameFor?: (leafKey: string) => string` prop: when a row's
`session.leafKey` is set, the label appends ` · {leafNameFor(leafKey) ?? leafKey}` (a
`chats-session-leaf-{id}` span) — the bound leaf's task-doc title, or the raw key when no resolver is
supplied — so the side rail shows which leaf each chat is working on.

260703-L14 restructures rendering around the `grouped` prop. The row markup is extracted into a
`renderRow` closure and `gridListFor(members, ariaLabel)` builds one React Aria `GridList` per
member set (every list shares `selectedKeys={activeId}` — only the list containing the active id
shows a selection). No `grouped`, or `grouped.groups.length === 0`, returns the single flat
`GridList` exactly as before. Otherwise a `chats-session-tree` column renders each `SessionGroup` as
a `<section>` (`chats-group-{key}`, `data-nested` + a 22px `marginLeft` class when `group.nested`)
headed by a native toggle button (`chats-group-toggle-{key}`, `aria-expanded`): a rotating chevron
span, a `RankBadge size="sm"` when `group.tier` is set, the ellipsized group label, and the
precomputed `countLabel` ("n chats · n live" / "· archived"). Collapse state is a UI-local
`useState<Record<string, boolean>>` keyed by group key — deliberately not persisted (L14 scope);
`isCollapsed` prefers the user's explicit toggle, else `group.defaultCollapsed` **unless the group
holds the ACTIVE session** — the landed archive defaults collapsed but must never hide the active
chat (the auto-expand rule; an explicit user collapse still wins). Collapsed groups unmount their
`GridList`; `grouped.ungrouped` renders as a trailing flat `GridList` below the groups. `renderRow`
also gained the spawn-role chip: `session.spawnRole` renders a `chats-session-role-{id}` chip via
the `roleChip` cva (`architect` and `orchestrator` gold owner-tier with gold borders, strategist
gold, manager purple, worker cyan, curator cyan, reviewer amber; unknown roles fall to the muted
base, never throw). The chip carries `data-known-role="true|false"` so tests can distinguish known role
provenance from an unknown/default chip without depending on generated class names.

### Conventions

`GridList`, not `ListBox` — each row has a focusable End action, and a `ListBox` row
is a single focus stop that would make a nested button keyboard-unreachable; `GridList` gives arrow-nav
between rows plus keyboard access to the per-row action (coding-guidelines: "do not hand-roll
interactive widgets; use the React Aria primitive"). Styling is co-located Panda `css()` keyed on
React Aria `data-*` conditions (`_selected` / `_focusVisible`); the row's `_selected` colour cascades
to the label, so selection state is read from React Aria, never re-derived in JSX. The `OpenSession` row shape is
imported from the `data/sessions` store (its definition moved there in slice 6e-4), not defined here.

### Invariants And Boundaries

Presentational + controlled: no store read, no backend, no xterm — which is why its behavior is
unit-tested directly (`SessionList.test.tsx`), unlike the Chats render-only tests. Single selection is
the active session; an empty `activeId` shows no selected row (when the active session is closed,
`Chats` clears `activeId` and the terminal falls back to its empty hint). End only reports intent; the
actual backend terminate call, local row removal, cross-tab broadcast, and terminal/WS teardown stay in
`Chats`. L14 additions keep that split: group MEMBERSHIP is decided entirely by `data/sessionGroups`
(this component renders the model verbatim and derives nothing but collapse visibility); collapse
state is UI-local and unpersisted; the active session must never be hidden by a collapse **default**
(only an explicit user toggle may hide it); and the group-less flat list (no `grouped` prop, or a
model with zero groups — every flat run) stays byte-identical to pre-L14. Insignia render only
through the shared `grammar/RankBadge` (size `sm`).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Chats view that owns session state and composes this switcher. | L318-L326 | [Chats.tsx](Chats.tsx) |
| The React Aria `ListBox` single-select idiom this mirrors (selectedKeys ↔ onSelectionChange). | — | [LifecycleList.tsx](LifecycleList.tsx) |
| The render + interaction tests for this switcher. | L17-L82 | [SessionList.test.tsx](SessionList.test.tsx) |
| The pure grouping model this renders (`SessionGroup`/`GroupedSessions`, membership + countLabels). | `groupSessions` | [sessionGroups.ts](../data/sessionGroups.ts) |
| The V4 chevron insignia on group headers (size `sm`). | — | [RankBadge.tsx](../grammar/RankBadge.tsx) |

## Update History

- 2026-07-07T22:21+02:00 — 260707-HFX-L6R4 curator spawnability fix: added
  `curator` to the known spawn-role set and role chip variants using the existing restrained cyan
  lane styling, preserving the unknown/default chip path for unrecognized roles. Verification
  metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:32+02:00 — 260707-HFX-L6 L6R2 review remediation: added `architect` to the
  known spawn-role chip set with the gold owner-tier mapping, and exposed `data-known-role` on the
  chip so the dashboard test can pin architect as a known role rather than the unknown/default chip.
  Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-06T23:56:36+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the G1 command tree —
  an optional `grouped` prop rendering collapsible group sections (chevron + `RankBadge sm` + label +
  countLabel headers; one GridList per group; 22px nested indent), UI-local collapse with the
  active-session auto-expand exception for default-collapsed groups, the ungrouped flat remainder,
  the zero-group flat fallback (pre-L14 rendering), and the spawn-role chip (`roleChip` cva) on rows
  with `spawnRole`. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added an optional `leafNameFor` resolver prop; a leaf-bound row now
  appends ` · {leaf name}` (the bound leaf's task-doc title, fallback the raw leaf key) so the side rail
  shows which leaf each chat works on. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed the local-only Hide action and `onDetach` prop;
  the row switcher now exposes only the destructive End action and reports it through `onTerminate`.
- 2026-06-27T00:33+02:00 — Task 22 follow-up: renamed the local-only Detach button to visible `Hide`
  and made row action buttons stop propagation inside the selectable GridList row, leaving `End` as the
  only destructive terminal action.
- 2026-06-26T23:05+02:00 — Task 22: split the old close action into non-destructive Detach and explicit
  Terminate callbacks, and added non-running status badges so exited catalog rows remain visible without
  implying a live terminal. Verification metadata pinned until closeout stamps the task-22 code commit.
- 2026-06-23T13:45+02:00 — Task 11: attached sessions now render their `lifecycleId` as a compact row
  badge so the hosted chat route is visible in the Chats side rail. Verification metadata pinned until
  closeout stamps the task-11 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: the `OpenSession` row-shape interface moved out of this file into the `data/sessions` store; `SessionList` now imports the type (behavior/props unchanged). Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T04:38 — Created for task 6 slice 6e-2c: extracted the Chats session switcher into a React Aria `GridList` side-panel (`sessions`/`activeId`/`onSelect`/`onClose`), replacing the horizontal tab strip. Verification metadata pinned until closeout stamps the 6e-2c code commit.
