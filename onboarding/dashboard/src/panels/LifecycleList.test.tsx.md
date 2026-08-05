# dashboard/src/panels/LifecycleList.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LifecycleList.test.tsx`    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T10:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

### 260731-EFA-L4 state-mark handover

Two regressions in the `LifecycleList independent Operations signals` block pin that this list hands
the lifecycle state to `Dot` at all — the row builds `item.variant` as
`lifecycle?.state ?? statusVariant(doc.status)`, so a live lifecycle's RAW state string is what
reaches the mark. `seedActivityProjection` took a second parameter (`state`, defaulting to
`"running"`) so the one activity fixture can be re-seeded in any state.

- **`awaiting-developer`** — seeds the activity leaf in that state and asserts the cell's
  `aria-label` is `"Task progress: awaiting-developer; phase: build"`, then compares the row's mark
  `outerHTML` against two bare `<Dot>` renders: it must EQUAL `bareDotOf("awaiting-developer")` and
  must NOT equal `bareDotOf("__no-such-variant__")`. The negative half is the real assertion — the
  state used to appear in neither `statusVariant` nor `Dot`'s variant list, so it fell through to
  the unrecognised-variant base and a handoff row read as nominal. The mark is read out of the DOM
  BEFORE the bare `Dot` renders, because both renders share `document.body`.
- **`paused` vs `abandoned`** — `rowMarkOf(state)` (`cleanup()` → re-seed → render → return the
  mark's `outerHTML`) is called for each and the two must differ. Both states reach `Dot` through
  this list's own `item.variant`, so this is a single-rail comparison, not a cross-panel one.

What `Dot` does with each variant is `Dot.test.tsx`'s contract; these two only prove the handover.
The tests therefore assert on rendered `outerHTML` equality rather than on any colour or glyph.

Separately, the local `projection()` builder no longer hand-lists the metric buckets — it calls
`metricsFor(lifecycles)` from the mirror. That is not cosmetic: `Metrics` extends
`LifecycleStateCounts`, a mapped type derived from the LIVE half of the state vocabulary
(`ActiveState` is `LIVE_STATES` itself, no longer `State` minus the terminal pair), so a state filed
live adds a REQUIRED bucket field and any hand-written metrics literal stops compiling. The hand-written
copy this replaced is exactly what let `awaiting-developer` be counted nowhere. No assertion in this
file reads `metrics`; the seeds simply track the contract now instead of restating a stale snapshot
of it.

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
- The state-mark tests own the HANDOVER only. They must not restate `Dot`'s per-variant colour, glyph,
  or animation — those belong to `Dot.test.tsx`, and duplicating them here would make a palette change
  fail two files for one reason. Comparison is against a bare `<Dot variant=…>` render, so the
  assertion stays true whatever treatment the variant is given.
- Seed fixtures state lifecycles and derive metrics (`metricsFor`); a hand-written metrics literal must
  not come back, because it cannot fail when the state vocabulary grows.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `operationRows` in the component under test admits root/master docs, active-enclosure-matched leaves, series fallbacks, and active-enclosure-backed lifecycle fallbacks. | `operationRows` | dashboard/src/panels/LifecycleList.tsx:477-567 |
| `docRow`/`seriesRow` build the mark as `lifecycle?.state ?? statusVariant(...)` — the handover these tests pin. | "function docRow", "function seriesRow" | dashboard/src/panels/LifecycleList.tsx:582-582; dashboard/src/panels/LifecycleList.tsx:635-635 |
| The `awaiting-developer` and `paused`-vs-`abandoned` state-mark regressions, with `rowMarkOf`/`bareDotOf`. | "gives a live awaiting-developer row the handoff dot, not the one an unknown state gets" | dashboard/src/panels/LifecycleList.test.tsx:1217-1231 |
| `seedActivityProjection` takes the seeded lifecycle `state`, so one fixture serves every state case. | "function seedActivityProjection" | dashboard/src/panels/LifecycleList.test.tsx:1134-1134 |
| `Dot` — the variant treatments these tests deliberately do not restate. | `Dot` | dashboard/src/grammar/Dot.tsx:119-129 |
| `metricsFor` / `LifecycleStateCounts` — why the seeds derive metrics instead of listing buckets. | "export type LifecycleStateCounts" | dashboard/src/types/projection.ts:284-284 |
| The regression fixture proves sidebar inclusion/exclusion for root docs, active leaves, cleanup-completed leaves, enclosure fallbacks, inactive leaves, loose leaves, and unenclosed lifecycles, plus BY REPO child depth and BY PHASE flatness. | "limits sidebar rows to root docs" | dashboard/src/panels/LifecycleList.test.tsx:234-366 |
| The numbered-leaf regression fixture proves a leaf document whose file stem is longer than `EnclosureNode.leafId` still nests under its master when its authored task id matches the enclosure leaf id. | "nests numbered leaf docs whose enclosure leaf id is shorter than the task file stem" | dashboard/src/panels/LifecycleList.test.tsx:408-462 |
| The reopen regressions prove a reopened worktree-less enclosure is hidden until restart then re-admitted, and the identity regression proves one row per `enclosureId` with lifecycle annotation (both binding directions). | "renders ONE task entry per enclosureId" | dashboard/src/panels/LifecycleList.test.tsx:584-676 |
| The orphan-lifecycle regression proves a doc-less enclosure-backed runtime row nests under its master via the computed parent key instead of floating top-level. | "nests a doc-less orphan lifecycle under its master instead of floating top-level" | dashboard/src/panels/LifecycleList.test.tsx:717-753 |
| The long-title fixture proves native row title hover text plus the row/title/metadata shrink classes on an admitted enclosure-backed task row. | "exposes the full long task title and row context on title hover" | dashboard/src/panels/LifecycleList.test.tsx:1026-1088 |
| The shared hierarchy helper supplies `findParentTaskMatch`, `taskDocHierarchyLabel`, and `taskDocParentKey` — the parent match, child task-document id, and parent key the test expects in the Operations row label. | "function findParentTaskMatch" | dashboard/src/data/taskHierarchy.ts:43-43 |
| `taskDocSelectionKey`/`seriesSelectionKey`/`lifecycleSelectionKey` and `parseTaskSelection` apply the typed task selection contract; `taskLabel`/`taskDocumentLabel` the label contract. | `taskDocSelectionKey` | dashboard/src/data/taskIdentity.ts:17-17 |
| `dashboardStore` — the Zustand projection store seeded (and `reset()`) by the test. | `dashboardStore` | dashboard/src/data/store.ts:225-347 |
| The frontend mirror of `LifecycleProjection` and `EnclosureNode`. | "interface LifecycleProjection", "interface EnclosureNode" | dashboard/src/types/projection.ts:133-133; dashboard/src/types/projection.ts:258-258 |
| The frontend mirror of `WorkspaceProjection`. | `WorkspaceProjection` | dashboard/src/types/projection.ts:517-528 |

## Current L5I Maintenance

The list tests now exercise the active/inactive rendering boundary as well as the established task
hierarchy rules, preserving the guarantee that a hidden persistent rail need not advance its local
age presentation.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges, and converted the history `(L…)` projection-mirror
  citations to `cit:`; exact non-fixing check returns zero findings.

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the three rows citing that file, each on its proving symbol:
  `metricsFor`/`LifecycleStateCounts` L173-L220 → L208-L257 (`LifecycleStateCounts` L214, `metricsFor`
  L250); `LifecycleProjection`/`EnclosureNode` L97-L141 → L132-L176; `WorkspaceProjection` L674-L689 →
  L711-L726. Corrected one sentence the change falsified: `LifecycleStateCounts` was described as
  "derived from the state vocabulary", which was the old `ActiveState = Exclude<State, TerminalState>`
  shape; `ActiveState` is now `LIVE_STATES` itself, so the mapped type is over the LIVE half and a
  state filed terminal gets no bucket.

- 2026-08-01T09:48+02:00 — 260731-EFA-L4 curator: documented the two new state-mark regressions
  (`awaiting-developer` must render the handoff dot and NOT the unknown-variant base;
  `paused` must not render as `abandoned`), `seedActivityProjection`'s new `state` parameter, the
  `rowMarkOf`/`bareDotOf` helpers, and the read-before-second-render ordering the shared
  `document.body` forces. Recorded the boundary that these assert the handover only, with `Dot`'s
  per-variant treatment left to `Dot.test.tsx`. Also documented the `projection()` builder's swap from
  a hand-listed metrics literal to `metricsFor(lifecycles)` — verified it is a superset (same
  `lifecycleCount`/`totalTokens`/empty histogram, buckets now derived from `ACTIVE_STATES` via
  `LifecycleStateCounts`) and that no assertion in this file reads `metrics`, so the swap is
  contract-tracking rather than behavioural. Repaired six citations against the current sources:
  component-under-test L252-L286;L443-L455 → `operationRows` L477-L571; the admission test L129-L260 →
  L227-L360; the numbered-leaf test L264-L318 → L401-L456; the long-title test L296-L350 → L1018-L1081
  (that old range now lands inside the L10 case-mismatch test); `dashboardStore` L1-L112 → L225-L348
  (L1-L112 held only the state interface); and the projection-mirror row L1-L80;L360-L390, which
  contained none of `LifecycleProjection` cit:(["interface LifecycleProjection"], dashboard/src/types/projection.ts:258-258), `EnclosureNode` cit:(["interface EnclosureNode"], dashboard/src/types/projection.ts:133-133) or `WorkspaceProjection`
  cit:(["interface WorkspaceProjection"], dashboard/src/types/projection.ts:517-517) — split into two rows with real ranges.

- 2026-07-24T13:17:17Z — Curator: recorded hidden-rail activity regression coverage; verification
  fields remain pre-commit.

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
