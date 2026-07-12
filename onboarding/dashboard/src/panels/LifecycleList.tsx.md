# dashboard/src/panels/LifecycleList.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LifecycleList.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-12T17:50 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`       |
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The Operations task list. It uses projected JSON-primary task documents as the readable task pool, but
does not put every projected document into the left sidebar. Sidebar rows are limited to root/master
task documents, leaf task documents that match an active enclosure, folder-keyed series fallbacks when
no master document is projected, and runtime lifecycle fallbacks for enclosure-backed work with no
document row. Since 260703-L11 an active enclosure is one whose worktree PHYSICALLY EXISTS — the shared
`hasLiveWorktree` rule over the projection's stat'ed `codeWorktreeExists`/`memoryWorktreeExists` flags,
never a cleanup-state proxy: retired/discarded leaves stay hidden as before (their worktrees were
reaped), and a reopened contract (`cleanup: reopened`) stays hidden until `worktree_start` recreates its
worktrees. Retired and discarded leaves stay reachable through typed `taskdoc:` links and master-internal
navigation instead of lingering in the sidebar. Planning/inactive leaves follow the same non-sidebar
path. The complementary identity rule (260703-L11): each leaf appears ONCE — one task entry per
`enclosureId` — with a bound lifecycle annotating the doc row rather than duplicating it as a card.

In the `BY REPO` pivot, admitted leaf documents are grouped below their parent/root task and rendered as
indented child rows; those leaf labels use the same child task-document numbers as the master task
list. Since 260703-L14 the hierarchy carries a third, top level: an **orchestration task** — a
`kind:"master"` doc with a non-empty `orchestrates` list — renders as a gold-tier command row, the
masters it names nest one 22px step below it with the purple management tier, and their leaves keep
today's rendering one step further. Command rows wear the developer-picked V4 treatment (folded corner,
tier ghost wash, chevron `RankBadge`, gold top hairline for orchestration); uncommanded masters — and
every row of a run with no orchestration task (the D3 ruling) — render exactly as before: no tier, no
badge, no extra indent. `BY PHASE` remains a flat lifecycle/status view. The panel uses React Aria `ListBox` rows with
typed selection keys (`taskdoc:<docPath>`, `series:<seriesId>`, `lifecycle:<id>`) and keeps the
user-facing copy as "Tasks" (`Tasks · {n}`, empty state `No tasks.`). Task 11's compact gate badge is
shown when the attached lifecycle has a durable `gate.kind` (`gateHint` returns the kind or `""`). **L17
removed the wait-loop-era fallback** to a proto `ask` (the question string, else the literal "ask"): under
notify-and-continue the attention queue carries the notification and only durable gates surface here. Long visible task labels stay
one-line: the title span is the row's shrinkable segment, truncates with ellipsis when space is tight,
and carries a native hover `title` containing the full label plus lifecycle context. The listbox,
section, and row containers are also width-constrained (`minmax(0, 1fr)` grid tracks plus `minWidth:0`
on the panel/row) so the row cannot expand the left panel horizontally before the title span gets to
ellipsis; secondary kind, gate, and wait/progress metadata are bounded with their own ellipses so they
cannot consume the whole title lane.

## Code Commentary

### Logic

Since L15 the panel's served ages advance LOCALLY: the wire carries stable forms without the volatile *Seconds fields, so the panel derives display ages from per-object arrival anchors (data/servedAges.ts) refreshed by a 10-second useNowMs ticker — the deliberate, disclosed deviation from the no-re-render ideal that replaced the per-second whole-payload churn.

L11 review follow-up (L11R-2): `lifecycleForEnclosure`'s anchor fallback is now deterministic — among lifecycles anchoring one enclosure without a contract `lifecycleId`, the greatest `lastEventTs` (most recently active) annotates the row, never projection order.

The `Panel` `head` shows `Tasks · {rows.length}`. The BY REPO | BY PHASE pivot is a React Aria
`ToggleButtonGroup` (single-select, `aria-label="Group tasks by"`) in that custom `head`; it groups the
derived `OperationRow` collection by repository or lifecycle phase/task status. `operationRows` builds
rows in this order: admitted task-document rows first, series fallback rows only when the master doc is
not already in `taskDocuments`, then runtime-only lifecycle rows for enclosure-backed lifecycles that no
document/series row represents. It first derives an active enclosure list with the shared
`hasLiveWorktree` selector (`codeWorktreeExists || memoryWorktreeExists` — 260703-L11); document
admission and runtime-only lifecycle fallbacks use that filtered list, while projected task documents
remain available to Detail/master navigation.

One row per `enclosureId` (260703-L11): a `representedEnclosureIds` set records every enclosure a doc
row resolved through, and the runtime-only lifecycle loop skips a lifecycle whose
`findLifecycleEnclosure` result is already claimed (also claiming the ids it does render, so two
lifecycles bound to one enclosure yield one row). The annotation half of the rule is
`lifecycleForEnclosure(enclosure, lifecycles, lifecycleById)`: when `runtimeForDoc` finds no lifecycle
(e.g. the doc's `lifecycleId` was cleared), the doc row falls back to the lifecycle bound to its
enclosure — by the contract's recorded `lifecycleId` or by a live lifecycle's own `enclosure` anchor —
so the lifecycle's state/gate/ask/staleness enrich the single doc row instead of rendering a second
task entry (the L9-reopen defect: the enclosure row AND the live lifecycle's card rendered for one
leaf).

A document is admitted when `isRootTaskDoc` returns true (`kind === "master"` or `task.json`) or
`enclosureForDoc` matches the document directory to `EnclosureNode.taskRoot` and either the document
stem or authored task-document `id` to `EnclosureNode.leafId` in the active enclosure list — every
leafId comparison **case-insensitive** since L10, because enclosure leaf ids are slugified lowercase
directory names (`260628-l7`) while doc ids are authored uppercase labels (`260628-L7`), the mismatch
that left active series leaves rendering as doc-less runtime rows. The `id`
join covers numbered leaf enclosures such as leaf id `31` whose readable task file is
`31_provider-state-refresh-and-engine-room-honesty.json`; it deliberately does not admit arbitrary
docs that merely share a master lifecycle. Since L11 the joins are EXACT only: `task_reopen` reuses
the original leaf id (a reopened enclosure returns to planning with `cleanup: reopened` and renders
as its planned doc row), so the old `-rN`/`-sN` suffixed-leaf-id `startsWith` admission heuristic is
gone. These comparisons are structural joins to projected
enclosure identity; they are not used to recover display numbers or ordering from task-name prefixes.
Document rows use `taskDocSelectionKey(doc.docPath)`, series fallback rows use
`seriesSelectionKey`, and runtime-only rows use `lifecycleSelectionKey`. Runtime-only lifecycle rows
also resolve a `parentKey` through `masterParentKeyForEnclosure`: it finds the series whose folder
(`pathDir(series.docPath)`) equals the enclosure `taskRoot` and points the row at the projected master
(`taskdoc:` when the master document is projected, otherwise `series:`), so a doc-less enclosure-backed
lifecycle nests under its master in `BY REPO` rather than floating as a top-level row.

Leaf document row labels and parent keys come from `data/taskHierarchy.ts`: `taskDocHierarchyLabel`
resolves the parent master sub-task ref and prepends the child task document `id` when that doc is
projected, while `taskDocParentKey` points child rows at the projected parent master (`taskdoc:` when
available, otherwise `series:`). The L14 command tier layers on top through `commandFacts(doc,
allDocs)`: a master doc that IS an orchestration task (`isOrchestrationDoc` — `kind:"master"` +
non-empty `orchestrates`) gets `tier:"orchestration"`; a master named in some orchestration doc's list
(matched forgivingly by folder / doc id / title via `orchestratorParentKey(masterCommandNames(doc), …)`,
never itself) gets `tier:"management"` and `parentKey` = the orchestration row's `taskdoc:` key.
`seriesRow` applies the same commander check to folder-keyed series fallback rows (seriesId / title /
folder names). `groupRows` keeps `BY PHASE` flat, but for `BY REPO` calls
`hierarchyRows` — since L14 a depth-first walk over the parent links to ANY depth (orchestration >
master > leaf is three levels) with a `seen` cycle guard plus a trailing sweep that appends
cycle-orphaned rows top-level so pathological parent data can never drop a row. The `ListBoxItem`
carries `data-depth`, `data-parent-key`, and (L14) `data-tier` for this hierarchy contract, while
lifecycle selection ids remain unchanged. Tier rows render the V4 treatment through the row `cva`'s
`tier` variants — a 13px folded-corner `_before` triangle, a `backgroundImage` ghost wash fading into
the row bg (gold/purple ghost tokens), and for orchestration a `goldDim` top hairline — plus a
`RankBadge` (size `row`) after the state `Dot`. Indentation is `indentStyle`: 22px `marginLeft` per
step, where tier rows indent by their full depth while non-tier rows keep today's `nested`
padding-left for their first level and only add margin beyond it — so a leaf under a commanded master
sits one 22px step past the master, and a flat run's rows keep byte-identical styling to pre-L14. `selectedId` is normalized with `parseTaskSelection` before
feeding React Aria `selectedKeys`, so raw lifecycle ids from older surfaces still highlight the right
typed row when a matching row exists.

After hierarchy flattening, `descendantBearingKeys` identifies parent rows with visible descendants.
In `BY REPO`, `visibleHierarchyRows` walks the depth-first rows with a collapsed-depth stack, hiding
descendants of collapsed sprint/orchestration or master rows while preserving nested keys' independent
state. `TaskGroupDisclosure` is a native button with an accurate label and `aria-expanded`; its event
handlers stop pointer, keyboard, and click propagation so disclosure is not ListBox selection. The
heading still uses the full `rows.length`, and switching to `BY PHASE` uses the unfiltered flat rows.
`useCollapsedTaskGroups` defaults to expanded and persists stable typed selection keys in
`operations.tasks.collapsed.v1`; selectedId and task detail remain controlled by the parent.

Task document rows attach runtime state by structured data: direct `doc.lifecycleId`, or for root
masters the sibling enclosure whose `taskRoot` matches the doc directory and whose lifecycle id is the
root task id/name. `taskLabel` is used only for runtime-only lifecycle fallback rows. Progress hints use
top-level implementation steps for leaf docs and sub-task done/total for master docs; nested substeps do
not drive the row progress number. `gateHint(gate?.kind, ask)` returns only the durable gate kind and
renders as a small amber row badge; the wait-loop-era bare `ask` payload is not a task-row affordance.

Task 23/24 adds backend-driven agent-pickup feedback. `analytics.agentPickups` is grouped by
`lifecycleId`; the first matching `AgentPickupNode` is carried on `OperationRow.pickup` and rendered by
`AgentPickupIndicator` between the secondary column and gate badge. Fresh pending operator-inbox entries
show static delivery/acknowledgment wording; entries past the five-minute pickup TTL show the
dismissible `check chat` notice. Separately, `useSessions` subscribes to the shared Chats-owned catalog
and `summarizeChatActivity` maps exact live harness `turnState` onto a compact chat indicator. Task
progress, chat turn activity, and inbox acknowledgment are three independent axes; the row never adds a
poller or derives chat activity from lifecycle state.

The listbox and list sections use `gridTemplateColumns: minmax(0, 1fr)`, `width:100%`, and
`minWidth:0` so React Aria section grid tracks cannot size themselves to a long row's min-content
width. Row containers add `minWidth:0` and `maxWidth:100%`; the LifecycleList panel class also sets
`minWidth:0` and hides horizontal overflow. The row title span then uses `minWidth:0` plus
`flex:1 1 0` with `overflow:hidden`, `textOverflow:ellipsis`, and `whiteSpace:nowrap`; the secondary
phase/repo text, gate badge, and wait/progress metadata each keep their own small bounded ellipsis.
Those metadata spans deliberately avoid auto left margins; otherwise the row can stay within the panel
but still starve the title down to zero visible pixels.
`taskTitle` builds the native hover text from the full label, lifecycle id/state/phase, optional
repo/gate, and the single bound task document's `currentStep` when present.

### Conventions

React Aria collection APIs (ListBox/Section/Item, ToggleButtonGroup); Panda `css`/`cva` for the look.

### Invariants And Boundaries

Selection is controlled by the cockpit's `selectedId`, but row identity is typed. The panel must not
derive a task-document row from parent `taskName`, display numbers, filename prefixes, or
`series-contract.md` content. The observer may project many completed/planning/inactive documents for
reading and master navigation, but the sidebar list stays finite through root/enclosure admission.
Archived/deleted docs disappear because the observer stops projecting them; status alone is not a
sidebar disappearance rule. Worktree existence is THE Operations sidebar disappearance rule for leaf
enclosures (260703-L11): losing the physical worktree removes left-rail eligibility without deleting or
hiding the task document from master navigation, and no cleanup-state proxy may substitute for the
stat'ed flags. `BY REPO` hierarchy is presentation over admitted rows only; it must not make
inactive/planning/worktree-less leaf documents sidebar-eligible. Completed/abandoned/reopened enclosures
all drop out through the same existence rule, one leaf renders at most one task entry (per
`enclosureId`), and a doc-less runtime row is nested only on the
`taskRoot`/series join; a shared master lifecycle by itself must never admit a document or re-parent a
row, so unrelated leaves under one master stay distinct rather than collapsing onto each other.
Spawned-session provenance stays visible where sessions are shown (the chats sidebar keeps its own
qualified-leaf-key rule); this list only de-duplicates task entries. Chat activity uses exact
qualified-leaf identity first, then only unclaimed lifecycle-bound fallback sessions, and omits
missing/terminal/non-harness seats. Collapse state is presentation
state only: it must not mutate task documents, task status, selection, detail, or hierarchy projection.
The L14 tier treatment is
strictly additive and orchestration-gated (D3): tier/badge/indent render only when a projected doc
carries `orchestrates` — no doc may be styled as a command row from titles, folder conventions, or
lifecycle shape, and a run without an orchestration task must render exactly as pre-L14 (pinned by
the flat-run regression test). Insignia render only through the shared `grammar/RankBadge`; the
chips/gate/progress vocabulary and the L11 worktree-truth + one-row-per-enclosure rules are
untouched by tiering.

Title truncation is presentational only: row selection and React Aria `textValue` still use the resolved
task label and stable typed row key. The no-horizontal-scroll contract belongs to the Operations list
containers, not to `Panel` globally; do not make every panel hide horizontal overflow to fix this one
list.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sidebar row admission uses root/master task documents, active-enclosure-matched leaves, series fallback rows, and active-enclosure-backed runtime fallbacks rather than every projected task document. | L306-L370; L659-L672 | [LifecycleList.tsx](LifecycleList.tsx) |
| `enclosureForDoc` admits leaf docs by exact case-insensitive stem/`id` joins only (reopen reuses the same leaf id since L11), and doc-less runtime rows are re-parented onto their master (`masterParentKeyForEnclosure`/`lifecycleRow`) so neither floats as a standalone node. | `enclosureForDoc`; `masterParentKeyForEnclosure`; `lifecycleRow` | [LifecycleList.tsx](LifecycleList.tsx) |
| Regressions assert a reopened (cleanup=reopened, no worktrees) enclosure is hidden until restart then re-admitted, an abandoned enclosure leaves the active rows, a doc-less orphan lifecycle nests under the master, and a lifecycle bound to a doc's enclosure annotates the single row instead of duplicating it. | reopen-hidden + reopen-restart + abandoned + orphan + one-row-per-enclosureId tests | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| BY REPO hierarchy uses taskHierarchy labels/parent keys, marks child rows with depth, and leaves BY PHASE flat. | L15-L20; L307-L343; L415-L447 | [LifecycleList.tsx](LifecycleList.tsx) |
| Operations rows stay within the left panel by constraining the panel/listbox/section/row widths, then ellipsizing the title span. | L38-L106; L187-L214 | [LifecycleList.tsx](LifecycleList.tsx) |
| Row titles use a shrinkable title span and native hover title assembled from label, lifecycle, repo, gate, and current-step context. | L99-L123; L212-L214; L464-L480 | [LifecycleList.tsx](LifecycleList.tsx) |
| The shared hierarchy helper computes parent matches, child-id hierarchy labels, creation-order placement, and parent selection keys. | L15-L58; L73-L88 | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| The L14 orchestration-command helpers this list's `commandFacts`/`seriesRow` tier derivation calls. | `isOrchestrationDoc`; `masterCommandNames`; `orchestratorParentKey` | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| The V4 chevron insignia rendered on tier rows (size `row`). | — | [RankBadge.tsx](../grammar/RankBadge.tsx) |
| L14 tier tests: the three-level hierarchy with 22px indents + the D3 flat-run regression. | L14 describe blocks | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| Focused tests assert root docs, active-enclosure leaves, enclosure fallbacks, and tooltip context are visible while loose/inactive/cleanup-completed leaves are absent, then prove BY REPO indentation/parent keys and BY PHASE flatness. | L130-L352 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| `fmtWait` for server-computed stale/wait ages. | L1-L40 | [data/selectors.ts](../data/selectors.ts) |
| Shared typed selection and label helpers used by the list and detail panel. | L1-L76 | [taskIdentity.ts](../data/taskIdentity.ts) |
| The shared `Panel` head/sticky band the pivot sits in. | L1-L64 | [grammar/Panel.tsx](../grammar/Panel.tsx) |
| Task-row pickup spinner/check-chat notice. | — | [AgentPickupIndicator.tsx](AgentPickupIndicator.tsx) |
| Native disclosure control and stable persisted collapse hook used by the hierarchy renderer. | L21-L45; L1-L28 | [TaskGroupDisclosure.tsx](TaskGroupDisclosure.tsx); [useCollapsedTaskGroups.ts](useCollapsedTaskGroups.ts) |

## Update History

- 2026-07-12T17:50 — 260712-TRH-L6: Operations now subscribes to the shared Chats session catalog and
  renders separate task-progress, live turn-activity, and inbox acknowledgment axes. Exact-leaf-first
  identity, unclaimed lifecycle fallback, deterministic multi-seat precedence, no second poller, and
  static pickup wording are documented here. Reviewer residuals F1 (task-label role), F2 (palette), F4
  (live-region scale), F5 (poll rerenders), and F6 (undefined-status omission) remain follow-up notes;
  F3 is recorded on the pickup sidecar. Candidate source remains uncommitted; metadata is pinned until
  closeout.
- 2026-07-12T12:58+02:00 — 260712-TRH-L3: added BY REPO-only sprint/master disclosure controls,
  depth-aware descendant filtering, and stable-key persistence under `operations.tasks.collapsed.v1`.
  The heading count, typed selection/detail, nested independence, and BY PHASE flatness remain unchanged.
  Candidate source is uncommitted; verification metadata is pinned to the last committed source touch
  until closeout.

- 2026-07-07T14:00+02:00 — agent-orchestration L17 (supplement): `gateHint` no longer falls back to the
  lifecycle's bare `ask` payload — it returns the durable `gate.kind` or `""`. The wait-loop-era chip (a
  proto `ask` rendering "Gate: <question>" / "Gate: ask") is retired under notify-and-continue; the three
  call sites drop the `ask` argument. A focused regression test locks it (a bare-ask lifecycle shows no
  "Gate:" line). Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-07T10:50+02:00 — L15: served ages advance locally (servedAges anchors + 10s ticker); volatile fields no longer arrive on the wire. Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:34+02:00 — 260703-L15 S1: row staleness advances locally — `OperationRowsInput`
  gained `nowMs` (from a component-level `useNowMs()`, 10 s tick), threaded through
  `docRow`/`seriesRow`/`lifecycleRow` into `rowMetaText` via
  `servedAgeSeconds(lifecycle, …staleSeconds, nowMs)`; the change gate stopped re-serving
  lifecycles whose only movement is their age.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:56:24+02:00 — 260703-L14 (visual hierarchy + chat grouping): the tasks tab gained the
  orchestration tier — `OperationRow.tier` derived by `commandFacts` (orchestration = a master doc
  with `orchestrates`; management = a master an orchestration doc names, matched folder/id/title,
  nesting under it via `parentKey`), `seriesRow` applying the same commander check, `hierarchyRows`
  generalized to N-depth DFS with a cycle guard, the V4 row treatment (folded-corner `_before`,
  ghost wash, gold hairline) as row-cva `tier` variants, `RankBadge` beside the Dot, `data-tier`,
  and the 22px `indentStyle` grammar. Flat runs (D3) render byte-identically to pre-L14.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T10:30+02:00 — L11 adversarial-review follow-up: L11R-2 (deterministic lastEventTs anchor fallback) and L11R-3 (re-measured row-admission citations, were stale after the diff shifted the functions). Verification metadata pinned until closeout stamps the L11 commit.

- 2026-07-06T02:35+02:00 — 260703-L11 (worktree truth): active-enclosure admission flipped from the
  cleanup-state proxy (`cleanup !== completed/abandoned`) to the shared `hasLiveWorktree` existence rule
  over `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` — a reopened leaf is now HIDDEN until
  `worktree_start` recreates its worktrees (supersedes the L11-task_reopen behavior of rendering it as a
  planned doc row). Added the one-row-per-`enclosureId` identity rule (`representedEnclosureIds` +
  claim-on-render in the runtime loop) and the `lifecycleForEnclosure` annotation fallback so a bound
  lifecycle enriches the doc row (state/gate/ask/staleness) instead of duplicating the leaf as a card.
  Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-03T00:30+02:00 — L11 task_reopen: active-enclosure admission now excludes `cleanup: abandoned`; the `-rN` suffixed-leaf-id `startsWith` reopen heuristic is removed because reopen reuses the exact leaf id, and a `cleanup: reopened` enclosure renders as its planned doc row.
- 2026-07-02T21:45+02:00 — L10 binding repair: every `enclosureForDoc` leafId comparison (stem, doc id,
  and the lifecycle-guarded reopen-suffix startsWith) is now case-insensitive, matching the
  normalization RailChat and the change-set bar already use. Enclosure leaf ids are slugified
  lowercase directory names while doc ids are authored uppercase, so active series leaf docs failed
  the admission and rendered as doc-less runtime rows. Verification metadata pinned until closeout
  stamps the L10 commit.
- 2026-06-28T16:17+02:00 — Task 35 reopen-task nesting fix: `enclosureForDoc` now admits a reopened leaf's suffixed enclosure (`leafId` = stem/`id` + cycle suffix such as `…-s7`) only when it both shares the document lifecycle and matches the suffixed-leaf-id shape, and `lifecycleRow` resolves a master `parentKey` through the new `masterParentKeyForEnclosure` helper so doc-less enclosure-backed runtime rows nest under their master. Together these stop a re-opened/edited task from appearing as a standalone phantom sidebar node, without letting a shared master lifecycle alone re-parent unrelated leaves. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T23:08+02:00 — Task 31 Operations grouping: `enclosureForDoc` now admits leaf docs when the active enclosure leaf id matches the authored task-document id, fixing numbered leaves like `31` whose file stem includes a readable slug. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-25T13:10+02:00 — Task 23/24: Operations rows now render backend-projected agent pickup state through `AgentPickupIndicator`.
- 2026-06-25T02:53+02:00 — Corrected the Operations horizontal-scroll regression: the listbox and
  section grid tracks now use `minmax(0, 1fr)`, row containers have zero minimum width and max out at
  the panel width, title plus secondary/gate/wait metadata use bounded ellipsis, and metadata avoids
  auto left margin so long task titles ellipsize instead of widening the left panel or disappearing.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T21:49+02:00 — Corrected Task 17 cleanup sidebar regression: Operations now treats
  `cleanup === "completed"` enclosures as inactive for sidebar admission/fallback rows, while the task
  document remains projected for master navigation. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T18:11+02:00 — Corrected Task 17 live-data numbering: Operations hierarchy labels now show
  the child `TaskDocNode.id` for authored leaf rows and keep the parent ref number only as fallback.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Corrected Task 17 Operations leaf numbering: BY REPO hierarchy still places
  leaves under parents using structured metadata, but labels now show the task-specific sub-task number
  from structured task metadata instead of a generated local counter. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy follow-up: `BY REPO` now groups admitted
  active leaf rows under their parent/root task with a depth marker. `BY PHASE` remains flat and sidebar
  admission is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 sidebar-scope correction: Operations no longer renders every
  projected task document as a sidebar row. It admits root/master docs, enclosure-matched leaf docs,
  series fallbacks, and enclosure-backed runtime fallbacks; inactive/planning leaves remain reachable
  through typed links and master navigation. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations: the list now builds rows from
  active task documents before runtime-only lifecycles, uses typed selection keys, attaches lifecycle
  state by structured bindings, keeps completed unarchived docs visible, and reports top-level progress
  only. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:37+02:00 — Task 18 title-overflow fix: task-row titles are now the shrinkable flex
  segment with one-line ellipsis, while phase/gate/wait metadata stay visible; the title span exposes
  a native hover title with the full task label plus lifecycle, gate, repo, and current-step context.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Helper extraction follow-up: refreshed metadata and references for the
  shared `taskIdentity.ts` label helpers used by both Operations and Detail. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:40+02:00 — Operations label fix: `LifecycleList` now resolves visible task labels from
  bound enclosure/task metadata before falling back to the raw lifecycle id, so a promoted fleeting
  lifecycle with a persistent leaf enclosure displays the leaf name while master/series rows keep the
  task label. Added focused coverage in `LifecycleList.test.tsx`. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: rows now surface gated/ask state with a compact amber badge sourced
  from `lifecycle.gate.kind` or `lifecycle.ask`, including fleeting entries. Verification metadata
  pinned until closeout stamps the task-11 code commit.
- 2026-06-23T07:25+02:00 — UI copy rename (user-facing lifecycle to task): the operations-panel header
  now reads `Tasks · {n}` (was "Lifecycles"), the empty state `No tasks.` (was "No lifecycles."), and
  the aria-labels became "Group tasks by" / "Tasks". Display copy only; the component name, types, store
  keys, and `lifecycle.id` values are unchanged. Refreshed Purpose plus Logic commentary. Verification
  metadata pinned until closeout stamps the rename code commit.
- 2026-06-15T17:00 — Created for slice 5d: the list became a React Aria `ListBox` and the pivot a
  `ToggleButtonGroup`, styled by Panda. Verification metadata pinned until closeout stamps the 5d
  code commit.
