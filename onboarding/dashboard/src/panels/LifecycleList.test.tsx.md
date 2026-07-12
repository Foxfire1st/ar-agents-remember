# dashboard/src/panels/LifecycleList.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LifecycleList.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`       |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

`LifecycleList.test.tsx` covers the Operations left-rail task-list identity contract. It verifies that
the sidebar admits root/master task documents, leaf task documents that match active enclosures, and
runtime enclosure fallbacks, while excluding loose/inactive leaf documents and enclosures whose
worktrees are physically gone (260703-L11: the `enclosure()` fixture defaults
`codeWorktreeExists`/`memoryWorktreeExists` to `true` and archived/reopened cases override them to
`false`, since admission now keys on the existence flags, not the cleanup label). It pins both halves of
the L11 tasks-surface rule: visibility (a reopened leaf is hidden until `worktree_start` recreates its
worktrees, then re-admitted) and identity (one task entry per `enclosureId` — a lifecycle bound to a
doc's enclosure, by contract `lifecycleId` or by its own `enclosure` anchor, annotates the doc row's
title/gate/staleness instead of rendering a duplicate card). It also keeps standalone root `task.json`
documents visible and selectable through typed `taskdoc:<docPath>` keys. The long-title fixture is now enclosure-backed, proving that the
native `title` tooltip survives the stricter sidebar admission rule and that the row/title carry the
minimum-width, flex-basis, and metadata-ellipsis classes required for the browser to ellipsize inside
the left rail. 260703-L14 adds the orchestration-tier contract: the three-level hierarchy (an
`orchestrates`-carrying master gold at depth 0, the commanded master purple at depth 1 with a 22px
margin, its leaf at depth 2 one step further, an uncommanded master untouched) and the D3 flat-run
regression (no `orchestrates` anywhere ⇒ zero `data-tier` attributes, zero rank badges, pre-L14
depths and margins).

## Code Commentary

### Logic

The first test seeds the shared `dashboardStore` with a minimal `WorkspaceProjection` containing a root
master task doc, one active-enclosure-matched leaf task doc, one cleanup-completed enclosure-matched leaf
task doc, one enclosure-backed lifecycle without a doc, one inactive projected leaf doc, one loose
planning leaf doc, and one lifecycle without an enclosure. Rendering `LifecycleList` must show exactly
the root doc, active leaf doc, and enclosure fallback; it must not render the cleanup-completed,
inactive/loose leaves or the unenclosed lifecycle. The fixture includes `SeriesNode.subTasks` metadata so
the visible leaf label becomes `15. ...`; the local `SeriesNode` fixture also carries the required
`seriesTokenTotal` field from the current projection contract, though the sidebar does not render that
aggregate. Task 33: the file's local `projection()` builder now sets the required top-level
`activeWorktreeGroups: []`, so every seeded snapshot matches the current projection contract; the
sidebar admission logic does not read this field (active-leaf admission here keys off enclosure
`cleanup`/projected-doc state, not the Topology's worktree-group set). The test asserts the first leaf
carries `data-depth="1"` and a parent `taskdoc:` key under `BY REPO`, then toggles to `BY PHASE` and
asserts the same row is flat.

The second test seeds a task-31-shaped leaf: the enclosure leaf id is the numeric `31`, while the
task-document file stem is the readable `31_provider-state-refresh-and-engine-room-honesty`. It asserts
the row is still admitted and nested under the browser-dashboard master through the parent `taskdoc:` key.

The 260703-L11 regressions pin the worktree-truth rule. Two reopen cases: a `cleanup: "reopened"`
enclosure with both existence flags `false` renders neither a doc row nor a lifecycle row (`Tasks · 1`,
the master alone), and the same enclosure with flags `true` (after `worktree_start`) renders the leaf's
doc row again, nested under its master. The one-row-per-`enclosureId` case seeds two live enclosures
each with an un-stamped doc (`lifecycleId: undefined`) plus one bound lifecycle each — `LC-CONTRACT`
bound via the contract's `lifecycleId` (blocked, `closeout-approval` gate, `staleSeconds: 120`) and
`LC-ANCHOR` bound only via its own `lifecycle.enclosure` anchor — and asserts exactly two option rows
render (no bare `leafId` lifecycle cards), each doc row's hover `title` carries the bound lifecycle's
id/state, the gate badge and formatted `2m` staleness annotate the row, and clicking selects the
`taskdoc:` key. The L10 regression seeds the real series
shape — a lowercase enclosure leaf id (`260628-l7`) against an uppercase doc id (`260628-L7`) with a
numbered doc slug matching neither — and asserts the doc renders as a clickable `taskdoc:` row rather
than a doc-less runtime lifecycle fallback. The orphan case seeds a doc-less,
enclosure-backed runtime lifecycle and asserts that `lifecycleRow`'s computed `parentKey` nests it under
its master instead of floating as a top-level row.
The two 260703-L14 tier tests: the hierarchy case seeds an orchestration master
(`orchestrates: ["260610_browser-dashboard"]`), the named master, an unnamed "Free Standing" master,
and one enclosure-backed leaf, then asserts per row `data-tier` / `data-depth` /
`data-parent-key` / inline `style.marginLeft` ("22px" at each indent step) and the presence (or
absence) of the `[data-rank-tier]` badge — the uncommanded master must be attribute-identical to a
pre-L14 root row. The flat-run case seeds the same shapes WITHOUT `orchestrates` and asserts the
container has zero `[data-tier]`/`[data-rank-tier]` matches and today's depths/margins (D3).
The 260703-L17 supplement regression seeds an enclosure-bound doc row annotated by a running
lifecycle that carries a bare `ask` question but NO durable gate, and asserts the row's hover
`title` includes `State: running` (the binding is live) while containing neither a `Gate:` segment
nor the ask text — pinning the retired wait-loop-era `gateHint` fallback (durable gate kinds only).
The third test seeds only task documents and asserts that a standalone root `task.json` document remains
visible while a loose sibling leaf doc is absent. The fourth test seeds an active-enclosure-backed blocked
task document with an intentionally long title, a durable gate, and a `currentStep`; rendering must attach
hover text to the title span containing the full task title, lifecycle id, state, phase, repo, gate kind,
and current step. It also asserts the admitted row has `min-w_0` / `max-w_100%` and the title span uses
`flex_1_1_0`, while the row metadata span uses ellipsis and no auto left margin, which pins the
structural part of the no-horizontal-scroll contract that jsdom can see.

The 260712-TRH-L3 block adds the disclosure contract: groups default expanded; only descendant-bearing
BY REPO sprint/master rows expose native buttons; sprint and master collapse remain independent; stable
typed keys persist across remounts; disclosure activation never calls `onSelect`; selected detail remains
selected while hidden and returns under BY PHASE; the total heading count stays unchanged; and empty
masters/leaves have no false controls. This test sidecar is refreshed because the test file is a changed
source contract, while generated package assets receive no sidecars.

### 260712-TRH-L6 Operations signaling matrix

The L6 regressions keep the three Operations row signals independent. They pair a running task with an
idle hosted chat, and a pending inbox acknowledgment with that idle chat, so neither durable progress nor
delivery state can imply model work. Identity cases prove exact qualified-leaf binding wins, an unclaimed
same-lifecycle seat is only a fallback, and a session claimed by another leaf cannot leak across the join.
Multi-seat cases pin deterministic precedence and per-seat detail. Missing, landed, exited, terminated,
stale, and unknown sessions omit the indicator or render `unknown` rather than inventing activity. A live
shared-store transition test updates the same catalog snapshot used by Chats and proves Operations follows
`turnState` without adding a poller or classifier.

### Conventions

The fixture builders stay local to the test file because this is a focused component contract rather
than a reusable gallery scenario. `afterEach` calls both Testing Library `cleanup()` and
`dashboardStore.reset()` so this test does not leak seeded projection state into neighboring panel tests.

### Invariants And Boundaries

- The test proves display/selection identity only; it does not mutate lifecycle ids or projection state.
- Task-document rows select by typed `taskdoc:<docPath>` keys. Runtime-only lifecycle fallback rows select
  by typed `lifecycle:<id>` keys.
- Sidebar visibility is not equivalent to projection visibility. Inactive/planning/cleanup-completed
  leaves may be projected for detail/master navigation without becoming left-rail rows.
- The long-title test proves the full label remains available through the DOM `title` attribute and that
  the row/title/metadata shrink constraints are present, including the absence of metadata auto-margin;
  it does not attempt to measure browser ellipsis layout in jsdom.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test admits root/master docs, active-enclosure-matched leaves, series fallbacks, and active-enclosure-backed lifecycle fallbacks. | L252-L286; L443-L455 | [LifecycleList.tsx](LifecycleList.tsx) |
| The regression fixture proves sidebar inclusion/exclusion for root docs, active leaves, cleanup-completed leaves, enclosure fallbacks, inactive leaves, loose leaves, and unenclosed lifecycles, plus BY REPO child depth and BY PHASE flatness. | L129-L260 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| The numbered-leaf regression fixture proves a leaf document whose file stem is longer than `EnclosureNode.leafId` still nests under its master when its authored task id matches the enclosure leaf id. | L264-L318 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| The reopen regressions prove a reopened worktree-less enclosure is hidden until restart then re-admitted, and the identity regression proves one row per `enclosureId` with lifecycle annotation (both binding directions). | reopen-hidden + reopen-restart + one-row tests | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| The orphan-lifecycle regression proves a doc-less enclosure-backed runtime row nests under its master via the computed parent key instead of floating top-level. | orphan test | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| The long-title fixture proves native row title hover text plus the row/title/metadata shrink classes on an admitted enclosure-backed task row. | L296-L350 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| The shared hierarchy helper supplies the parent match, child task-document id, and creation-order placement that the test expects in the Operations row label. | L15-L58; L73-L88 | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| The shared helper applies typed task selection and label contracts. | L1-L76 | [taskIdentity.ts](../data/taskIdentity.ts) |
| The Zustand projection store seeded by the test. | L1-L112 | [data/store.ts](../data/store.ts) |
| The frontend mirror of `WorkspaceProjection`, `LifecycleProjection`, and `EnclosureNode`. | L1-L80; L360-L390 | [types/projection.ts](../types/projection.ts) |

## Update History

- 2026-07-12T17:50 — 260712-TRH-L6: added Operations integration coverage for running-task versus idle-chat
  separation, pending inbox versus idle chat, shared-store live transitions, and the three-axis row
  contract. Candidate source remains uncommitted; metadata is pinned until closeout.
- 2026-07-12T18:00+02:00 — 260712-TRH-L6 manager availability exception: paired the substantive
  Operations signaling-matrix body with the task-progress/chat/inbox separation, exact-leaf and lifecycle
  fallback rules, multi-seat precedence, omission behavior, and shared-store transition coverage required
  by the closeout body gate. Both dedicated curator chats were quota-blocked after the main curation pass.
- 2026-07-12T12:58+02:00 — 260712-TRH-L3: added focused regressions for expanded defaults, sprint/master
  and nested-independent collapse, stable-key persistence, selection/detail stability, BY PHASE flatness,
  total-count preservation, native keyboard/accessibility semantics, and rows without descendants.
  Candidate source is uncommitted; verification metadata is pinned to the last committed source touch
  until closeout.

- 2026-07-07T14:00+02:00 — agent-orchestration L17 (supplement): added a focused gate-hint regression test —
  a lifecycle carrying a bare `ask` but no durable gate renders NO "Gate:" line (and the ask question does
  not leak), locking the retired wait-loop fallback. Verification metadata pinned until closeout stamps the
  L17 commit.
- 2026-07-06T23:56:30+02:00 — 260703-L14 (visual hierarchy + chat grouping): added the two tier tests —
  the three-level orchestration > master > leaf hierarchy (tier/depth/parent-key/22px-margin/badge
  assertions per row, uncommanded master untouched) and the D3 flat-run regression (zero tier
  attributes or badges without `orchestrates`). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T02:40+02:00 — 260703-L11 (worktree truth): the enclosure fixture defaults the new
  existence flags true; the reopened-leaf test flipped to hidden-until-restart plus a re-admitted-after-
  restart case (existence truth supersedes the render-as-planned-doc-row behavior below); added the
  one-row-per-`enclosureId` regression (bound lifecycle annotates the doc row — contract-`lifecycleId`
  and `enclosure`-anchor directions — with no duplicate lifecycle card); the cleanup-completed and
  abandoned fixtures now carry `false` flags since admission keys on existence. Verification metadata
  pinned until closeout stamps the L11 commit.
- 2026-07-03T00:30+02:00 — L11: the suffixed-enclosure reopen-admission test is replaced by two exact-id cases — a `cleanup: reopened` enclosure renders as its planned doc row nested under the master, and an abandoned enclosure disappears from the active rows.
- 2026-07-02T21:45+02:00 — L10 binding repair: added a regression where the enclosure leaf id differs
  from the doc id only by case (lowercase `260628-l7` vs uppercase `260628-L7`, numbered doc slug
  matching neither) — the doc must render as a clickable taskdoc row instead of a doc-less runtime
  lifecycle fallback. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-06-28T16:17+02:00 — Task 35 reopen-task nesting: added two regressions — a reopened leaf whose enclosure leaf id is a cycle-suffixed slug (`…-s7`) sharing only the document lifecycle still nests under its master and never renders the suffixed id as a standalone row, and a doc-less enclosure-backed runtime lifecycle nests under its master through the computed parent key. Both would have caught the phantom standalone node a re-opened task produced. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:30+02:00 — Task 33: the `projection()` test builder gained `activeWorktreeGroups: []` for the
  new required projection field; no behavioural assertion change. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-27T23:08+02:00 — Task 31 Operations grouping: added a regression for leaf id `31` plus readable task file stem `31_provider-state-refresh-and-engine-room-honesty`, asserting the row nests under the browser-dashboard master instead of rendering as standalone. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 projection mirror upkeep: local `SeriesNode` fixtures now include
  `seriesTokenTotal` to match the served contract; LifecycleList behavior and assertions are unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T02:53+02:00 — Corrected the Operations horizontal-scroll regression test: the long-title
  fixture now asserts the admitted row keeps `min-w_0` / `max-w_100%` and the title span keeps
  `flex_1_1_0`, plus metadata ellipsis and no metadata auto-margin, so the tooltip cannot regress
  independently from the shrink/ellipsis contract. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T21:49+02:00 — Corrected Task 17 cleanup sidebar regression test: the fixture now includes
  a cleanup-completed matching leaf enclosure and asserts its task document is not admitted to the
  Operations sidebar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Corrected Task 17 Operations live-data numbering tests: active leaf fixtures
  now set child task-document ids (`15`/`16`) and assertions pin those labels. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Corrected Task 17 Operations numbering tests: BY REPO assertions now expect
  task-specific `15.` / `16.` labels from structured sub-task refs rather than generated `1.` / `2.`
  counters. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy tests: the sidebar regression now seeds
  structured series sub-task metadata, asserts numbered leaf labels, verifies child depth/parent key in
  `BY REPO`, and verifies the same row becomes flat under `BY PHASE`. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 sidebar-scope regression tests: rewrote coverage around the corrected
  Operations rule, proving root docs, enclosure-matched leaves, and enclosure fallbacks appear while
  loose/inactive leaf docs do not. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations tests: updated the promoted-leaf
  fixture for document rows and added coverage that planning/terminal unbound docs remain listed and
  select through `taskdoc:<docPath>`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:37+02:00 — Task 18 title-overflow coverage: added a long-title row fixture with gate
  and current-step context, asserting the row's native hover title preserves the full task label and
  lifecycle context while existing promoted-leaf label assertions remain green. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — No content impact: the local `EMPTY_ANALYTICS` fixture gained `series: []`
  only to satisfy the current `Analytics` shape; the lifecycle-list label contract and assertions are
  unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Reference completion: added the new `taskIdentity.ts` helper reference and
  full verification metadata for the focused promoted-leaf label regression. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:40+02:00 — Created for the Operations label fix: covers promoted fleeting lifecycle
  display through bound leaf enclosure metadata while preserving the raw lifecycle id as internal
  identity. Verification metadata pinned until closeout stamps the code commit.
