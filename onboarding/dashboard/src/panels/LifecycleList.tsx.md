# dashboard/src/panels/LifecycleList.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/LifecycleList.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T16:17+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The Operations task list. It uses projected JSON-primary task documents as the readable task pool, but
does not put every projected document into the left sidebar. Sidebar rows are limited to root/master
task documents, leaf task documents that match an active enclosure, folder-keyed series fallbacks when
no master document is projected, and runtime lifecycle fallbacks for enclosure-backed work with no
document row. An active enclosure is a projected enclosure whose cleanup is not completed; cleanup
completed leaves stay reachable through typed `taskdoc:` links and master-internal navigation instead
of lingering in the sidebar. Planning/inactive leaves follow the same non-sidebar path.

In the `BY REPO` pivot, admitted leaf documents are grouped below their parent/root task and rendered as
indented child rows; those leaf labels use the same child task-document numbers as the master task
list. `BY PHASE` remains a flat lifecycle/status view. The panel uses React Aria `ListBox` rows with
typed selection keys (`taskdoc:<docPath>`, `series:<seriesId>`, `lifecycle:<id>`) and keeps the
user-facing copy as "Tasks" (`Tasks · {n}`, empty state `No tasks.`). Task 11's compact gate badge is
still shown when the attached lifecycle has `gate.kind` or a proto `ask`. Long visible task labels stay
one-line: the title span is the row's shrinkable segment, truncates with ellipsis when space is tight,
and carries a native hover `title` containing the full label plus lifecycle context. The listbox,
section, and row containers are also width-constrained (`minmax(0, 1fr)` grid tracks plus `minWidth:0`
on the panel/row) so the row cannot expand the left panel horizontally before the title span gets to
ellipsis; secondary kind, gate, and wait/progress metadata are bounded with their own ellipses so they
cannot consume the whole title lane.

## Code Commentary

### Logic

The `Panel` `head` shows `Tasks · {rows.length}`. The BY REPO | BY PHASE pivot is a React Aria
`ToggleButtonGroup` (single-select, `aria-label="Group tasks by"`) in that custom `head`; it groups the
derived `OperationRow` collection by repository or lifecycle phase/task status. `operationRows` builds
rows in this order: admitted task-document rows first, series fallback rows only when the master doc is
not already in `taskDocuments`, then runtime-only lifecycle rows for enclosure-backed lifecycles that no
document/series row represents. It first derives an active enclosure list by filtering out
`cleanup === "completed"`; document admission and runtime-only lifecycle fallbacks use that filtered
list, while projected task documents remain available to Detail/master navigation.

A document is admitted when `isRootTaskDoc` returns true (`kind === "master"` or `task.json`) or
`enclosureForDoc` matches the document directory to `EnclosureNode.taskRoot` and either the document
stem or authored task-document `id` to `EnclosureNode.leafId` in the active enclosure list. The `id`
join covers numbered leaf enclosures such as leaf id `31` whose readable task file is
`31_provider-state-refresh-and-engine-room-honesty.json`; it deliberately does not admit arbitrary
docs that merely share a master lifecycle. Reopening a finalized task spins up a fresh worktree whose
leaf id is the original stem/`id` plus a cycle suffix (for example `…-s7`) and shares the original
document's lifecycle; `enclosureForDoc` admits that suffixed enclosure only when **both** it shares
`doc.lifecycleId` **and** its leaf id is the suffixed form of the document stem or `id`
(`leafId.startsWith(stem + "-")` / `startsWith(id + "-")`) — the shared lifecycle alone is never
sufficient, so a reopened leaf stays nested under its master instead of surfacing as a standalone
phantom row. These comparisons are structural joins to projected
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
available, otherwise `series:`). `groupRows` keeps `BY PHASE` flat, but for `BY REPO` calls
`hierarchyRows` so parent/root rows render first and active leaf rows copy to depth `1` beneath their
parent. The `ListBoxItem` carries `data-depth` and `data-parent-key` for this hierarchy contract, while
lifecycle selection ids remain unchanged. `selectedId` is normalized with `parseTaskSelection` before
feeding React Aria `selectedKeys`, so raw lifecycle ids from older surfaces still highlight the right
typed row when a matching row exists.

Task document rows attach runtime state by structured data: direct `doc.lifecycleId`, or for root
masters the sibling enclosure whose `taskRoot` matches the doc directory and whose lifecycle id is the
root task id/name. `taskLabel` is used only for runtime-only lifecycle fallback rows. Progress hints use
top-level implementation steps for leaf docs and sub-task done/total for master docs; nested substeps do
not drive the row progress number. `gateHint(gate?.kind, ask)` returns the gate kind, the ask question,
or `ask`, and renders as a small amber row badge before row metadata.

Task 23/24 adds backend-driven agent-pickup feedback. `analytics.agentPickups` is grouped by
`lifecycleId`; the first matching `AgentPickupNode` is carried on `OperationRow.pickup` and rendered by
`AgentPickupIndicator` between the secondary column and gate badge. Fresh pending operator-inbox entries
show `waiting for agent`; entries past the five-minute pickup TTL show the dismissible `check chat`
notice. The row does not infer this state locally from clicks.

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
sidebar disappearance rule. Cleanup completion is an Operations sidebar disappearance rule for leaf
enclosures only: it removes left-rail eligibility without deleting or hiding the task document from
master navigation. `BY REPO` hierarchy is presentation over admitted rows only; it must not make
inactive/planning/cleanup-completed leaf documents sidebar-eligible. A reopened leaf's suffixed
enclosure is admitted, and a doc-less runtime row is nested, only on the combined
lifecycle-plus-structural match (shared `lifecycleId` *and* a suffixed-leaf-id or `taskRoot`/series
join); a shared master lifecycle by itself must never admit a document or re-parent a row, so unrelated
leaves under one master stay distinct rather than collapsing onto each other.

Title truncation is presentational only: row selection and React Aria `textValue` still use the resolved
task label and stable typed row key. The no-horizontal-scroll contract belongs to the Operations list
containers, not to `Panel` globally; do not make every panel hide horizontal overflow to fix this one
list.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Sidebar row admission uses root/master task documents, active-enclosure-matched leaves, series fallback rows, and active-enclosure-backed runtime fallbacks rather than every projected task document. | L306-L346; L589-L599 | [LifecycleList.tsx](LifecycleList.tsx) |
| A reopened leaf's suffixed enclosure is admitted only on shared lifecycle plus suffixed-leaf-id shape (`enclosureForDoc`), and doc-less runtime rows are re-parented onto their master (`masterParentKeyForEnclosure`/`lifecycleRow`) so neither floats as a standalone node. | `enclosureForDoc`; `masterParentKeyForEnclosure`; `lifecycleRow` | [LifecycleList.tsx](LifecycleList.tsx) |
| Regressions assert a reopened suffixed-enclosure doc and a doc-less orphan lifecycle both nest under the master instead of floating top-level. | reopen + orphan tests | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| BY REPO hierarchy uses taskHierarchy labels/parent keys, marks child rows with depth, and leaves BY PHASE flat. | L15-L20; L307-L343; L415-L447 | [LifecycleList.tsx](LifecycleList.tsx) |
| Operations rows stay within the left panel by constraining the panel/listbox/section/row widths, then ellipsizing the title span. | L38-L106; L187-L214 | [LifecycleList.tsx](LifecycleList.tsx) |
| Row titles use a shrinkable title span and native hover title assembled from label, lifecycle, repo, gate, and current-step context. | L99-L123; L212-L214; L464-L480 | [LifecycleList.tsx](LifecycleList.tsx) |
| The shared hierarchy helper computes parent matches, child-id hierarchy labels, creation-order placement, and parent selection keys. | L15-L58; L73-L88 | [taskHierarchy.ts](../data/taskHierarchy.ts) |
| Focused tests assert root docs, active-enclosure leaves, enclosure fallbacks, and tooltip context are visible while loose/inactive/cleanup-completed leaves are absent, then prove BY REPO indentation/parent keys and BY PHASE flatness. | L130-L352 | [LifecycleList.test.tsx](LifecycleList.test.tsx) |
| `fmtWait` for server-computed stale/wait ages. | L1-L40 | [data/selectors.ts](../data/selectors.ts) |
| Shared typed selection and label helpers used by the list and detail panel. | L1-L76 | [taskIdentity.ts](../data/taskIdentity.ts) |
| The shared `Panel` head/sticky band the pivot sits in. | L1-L64 | [grammar/Panel.tsx](../grammar/Panel.tsx) |
| Task-row pickup spinner/check-chat notice. | — | [AgentPickupIndicator.tsx](AgentPickupIndicator.tsx) |

## Update History

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
