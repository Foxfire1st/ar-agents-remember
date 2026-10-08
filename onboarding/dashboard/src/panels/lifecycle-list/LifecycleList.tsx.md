# dashboard/src/panels/lifecycle-list/LifecycleList.tsx

## Governing Overview

[panels/ overview](../overview.md)

## 260731-EFA-L8 Move

`LifecycleList.tsx` moved to `dashboard/src/panels/lifecycle-list/LifecycleList.tsx`
(canonical entry, 1,182 lines) under the frontend-rail naming rule. Its former
monolithic test suite split by behavior into `admission.test.tsx`, `gateHint.test.tsx`,
`hierarchy.test.tsx`, and `signals.test.tsx` (shared fixtures in `test-utils.tsx`).
The component behavior is unchanged.

## Purpose

> **WITHDRAWAL — the `260921-ICR-L34` curation, because the code this card's L33 paragraphs described was
> reverted.** Commit **`a9a1a41b`** (*"Revert L33's operations-list change; clear the pre-existing
> ruff-format red"*) is a **direct emergency commit with no curator pass behind it**: it deleted
> `panels/lifecycle-list/landedLeaves.ts` (177 lines), removed 250 lines from this module (1189 lines
> now), deleted 366 lines from `hierarchy.test.tsx` (355 lines now) and restored
> `useCollapsedTaskGroups.ts` to one collapse set. **The landed-leaf admission and its
> default-collapse rule do not exist in any tree**, `landedLeaves.ts` exists in neither, and
> `leafRecordsLandedWork`, `childFactsByParent`, `landedLeafDocs`, `markAutoCollapsed`, `rowIsCollapsed`,
> `openedKeys`, `setCollapsed` and `CollapseState` exist nowhere. This card's L33 narrative and its L33
> reference rows are **withdrawn in place** below and its card for the deleted module was removed; a
> reader must not act on them. The rest of the card — the pre-L33 behaviour, the pivots, the tiers, the
> row builders and the one-entry-per-`enclosureId` rule — was re-read against the reverted module and
> stands.

The Operations task list. It uses projected JSON-primary task documents as the readable task pool, but
does not put every projected document into the left sidebar. Sidebar rows are limited to root/master
task documents, leaf task documents that match an active enclosure, folder-keyed series fallbacks when
no master document is projected, and runtime lifecycle fallbacks for enclosure-backed work with no
document row. Since 260703-L11 an active enclosure is one whose worktree PHYSICALLY EXISTS — the shared
`hasLiveWorktree` rule over the projection's stat'ed `codeWorktreeExists`/`memoryWorktreeExists` flags,
never a cleanup-state proxy: retired/discarded leaves stay hidden as before (their worktrees were
reaped), and a reopened contract (`cleanup: reopened`) stays hidden until `worktree_start` recreates its
worktrees. **The existence rule is again the whole of the rule** — the L33 landed-leaf exception is
withdrawn (see the banner above): a `Completed` leaf whose worktree closeout removed has no row here,
and its work is reached through the master's own navigation and typed `taskdoc:` links. Retired,
discarded, abandoned and still-planning leaves keep the old path. The complementary identity rule (260703-L11): each leaf appears ONCE — one task entry per
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
user-facing copy as "Tasks" (`Tasks · {n}`, empty state `No tasks.`). **`n` counts task ENTRIES, not
projected documents** — every master, series and lifecycle entry, every leaf with live work, and the
landed leaves of the parents that are OPEN — and since 260921-ICR-L33 the `h2` carries that meaning in
its own native `title`, worded for the fresh render (a parent that still holds live work is open by
default, so its landed leaves are already counted before any click). Task 11's compact gate badge is
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

**The fourth pass and the default this paragraph describes are WITHDRAWN with the L33 revert.**
`markAutoCollapsed(rows)` and `appendLandedLeafRows` exist nowhere in the code tree; the module has no
landed-leaf pass, no `autoCollapsed` default and no `landedCount`. **What follows is the record of what
L33 built, kept so the withdrawal is auditable and not so a reader can act on it:** once every
non-landed row existed, `markAutoCollapsed(rows)` decided which rows the projection itself held closed,
and only then did `appendLandedLeafRows` materialize the landed leaves of the parents that were open.
The rule was two exclusions, not one: a row was auto-collapsed only when `landedCount > 0` **and**
`childCount === landedCount` (every child it carried was one of its own landed leaves) **and** it carried
no OTHER rows (`structuralChildren.get(row.key) ?? 0 === 0`). The third clause is load-bearing — on the
live projection an orchestration row that commands other masters owns a 161-row subtree, and closing it
would hide those masters' work behind a disclosure — and it is pinned by a delivered case rather than by
argument. **`rowIsCollapsed` and the `autoCollapsed` default this paragraph describes were removed with
the L33 revert** (see the banner): the reader's view of a row is the one `collapsedKeys` set in
[`useCollapsedTaskGroups`](../useCollapsedTaskGroups.ts.md), inverted by `toggleCollapsed`.
`TaskGroupSection` resolves `collapsedHere` once per group so the depth-stack walk and the
row's disclosure agree about which rows are open.

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
carries `data-depth`, `data-parent-key`, and the L14 `data-tier` for this hierarchy contract, while
lifecycle selection ids remain unchanged. Tier rows render the V4 treatment through the row `cva`'s
`tier` variants — a 13px folded-corner `_before` triangle, a `backgroundImage` ghost wash fading into
the row bg (gold/purple ghost tokens), and for orchestration a `goldDim` top hairline — plus a
`RankBadge` (size `row`) after the state `Dot`. Indentation is `indentStyle`: 22px `marginLeft` per
step, where tier rows indent by their full depth while non-tier rows keep today's `nested`
padding-left for their first level and only add margin beyond it — so a leaf under a commanded master
sits one 22px step past the master, and a flat run's rows keep byte-identical styling to pre-L14. `selectedId` is normalized with `parseTaskSelection` before
feeding React Aria `selectedKeys`, so raw lifecycle ids from older surfaces still highlight the right
typed row when a matching row exists.

`visibleHierarchyRows` is fed the resolved `collapsedHere` set rather than the raw persisted keys,
which is what lets an auto-collapsed row hide its landed leaves without the reader's own collapse state
being rewritten, and a master is given a disclosure (`hasDescendants`) when its inherited structural
descendants exist **or** it carries children of its own (`item.childCount > 0`) — so a fully landed
master still has a caret to open.

After hierarchy flattening, `descendantBearingKeys` identifies parent rows with visible descendants.
In `BY REPO`, `visibleHierarchyRows` walks the depth-first rows with a collapsed-depth stack, hiding
descendants of collapsed sprint/orchestration or master rows while preserving nested keys' independent
state. `TaskGroupDisclosure` is a native button with an accurate label and `aria-expanded`; its event
handlers stop pointer, keyboard, and click propagation so disclosure is not ListBox selection. The
heading still uses the full `rows.length`, and switching to `BY PHASE` uses the unfiltered flat rows.
`useCollapsedTaskGroups` owns the reader's collapse state and persists stable typed selection keys in
**one** array: `operations.tasks.collapsed.v1` (a key in it is a row the READER collapsed). The hook
returns `{ collapsedKeys, toggleCollapsed }` and `toggleCollapsed(key)` inverts that one key.
**The two-array form this paragraph used to describe — `operations.tasks.opened.v1` and
`setCollapsed(key, collapsed)` — was removed with the L33 revert** and exists in no tree. selectedId and
task detail remain controlled by the parent.

The row's state mark is `OperationRow.variant`, and BOTH row builders (`docRow`, `seriesRow`) compute
it as `lifecycle?.state ?? statusVariant(doc.status)`. The two sides of that `??` are different
vocabularies and the split is the point:

- **Live side** — when a lifecycle is bound, its RAW server `state` string goes to `<Dot variant>`
  untranslated. `awaiting-developer`, `blocked`, `paused` and `abandoned` all reach `Dot` on this
  path, never through `statusVariant`. Whether each one gets its own colour/glyph is `grammar/Dot.tsx`'s
  contract, not this panel's; this panel's obligation is only to hand the state over unmangled.
- **Document side** — `statusVariant` is the DOCUMENT-status map, for rows with no live lifecycle. Its
  entire input vocabulary is `tasks/document.py::DocStatus` (`planning | inProgress | Completed`),
  which arrives verbatim as `TaskDocNode.status` / `SeriesNode.status`. It therefore has exactly two
  outcomes — `Completed` → `completed`, everything else → `running` — and nothing else can arrive.
  It deliberately carries no lifecycle vocabulary: arms for `awaiting-developer`, `blocked`, `paused`
  and `abandoned` here would be permanently unreachable, since those states always take the left side
  of the `??`.

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
sidebar disappearance rule. Worktree existence is THE rule for a LIVE leaf enclosure's left-rail
eligibility (260703-L11): losing the physical worktree removes left-rail eligibility without deleting or
hiding the task document from master navigation, and no cleanup-state proxy may substitute for the
stat'ed flags. **The L33 exception to this paragraph — "a `Completed` leaf documents LANDS work, so its
row is admitted under its open master", via `landedLeafDocs`/`leafRecordsLandedWork` and the delivered
case `keeps a landed leaf that no series index resolves out of the list` — was removed by the revert and
is withdrawn:** there is no landed-leaf admission, no `landedLeaves.ts` module, and no such case in
`hierarchy.test.tsx`. Abandoned and reopened enclosures drop out through the existence rule, a
PLANNING leaf is never a row, and every master, series and lifecycle entry keeps its row regardless — so
one leaf still renders at most one task entry (per
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
untouched by tiering. The L33 landed-leaf default is not a tier: it applies by CHILD FACTS
(`childCount === landedCount`, no structural children) and never by tier, status, or row kind, so a
command row is only ever auto-collapsed when it commands nothing.

Title truncation is presentational only: row selection and React Aria `textValue` still use the resolved
task label and stable typed row key. The no-horizontal-scroll contract belongs to the Operations list
containers, not to `Panel` globally; do not make every panel hide horizontal overflow to fix this one
list.

`statusVariant` must stay a DOCUMENT-status map. Adding a lifecycle state to it (an
`awaiting-developer` arm, say) writes a branch the server can never reach, because a bound lifecycle
short-circuits it at `lifecycle?.state ?? …`; the fix for a mis-rendered lifecycle state belongs in
`grammar/Dot.tsx`'s variant recipe, not here.

The `data-testid="task-state"` span carries `aria-label`/`title` (`Task progress: {variant}; phase:
{phase}`) with **no `role`** — and that is only valid because it renders inside a React Aria
`ListBoxItem`, whose `role="option"` computes its name from content and so absorbs the label. A bare
`<span aria-label>` is a named `generic`, which ARIA prohibits (axe-core `aria-prohibited-attr`) and
which announces nothing; `AttentionQueue`'s equivalent mark has no widget role above it and therefore
had to take an explicit `role="img"`. If this span is ever lifted out of the `ListBoxItem`, it needs a
role of its own for the same reason.

## Evidence

### Repo-Internal References

- `operationRows` admits root/master task documents, active-enclosure-matched leaves, series fallback rows, and active-enclosure-backed runtime fallbacks rather than every projected task document. [1]

- `enclosureForDoc` admits leaf docs by exact case-insensitive stem/`id` joins only (reopen reuses the same leaf id since L11). [2]
- Regressions assert a reopened (cleanup=reopened, no worktrees) enclosure is hidden until restart then re-admitted, an abandoned enclosure leaves the active rows, a doc-less orphan lifecycle nests under the master, and a lifecycle bound to a doc's enclosure annotates the single row instead of duplicating it. [3]
- `groupRows`/`hierarchyRows` give BY REPO its taskHierarchy-derived parent links and `data-depth` marking, and leave BY PHASE flat. [4]
- Operations rows stay within the left panel: `sizing`/`listBox`/`section` widths, the `row` cva, then `rowId`'s ellipsis and the bounded `rowSec`/`rowGate`/`rowMeta`. [5]
- `rowId` is the shrinkable title span; `taskTitle` assembles the native hover text from label, lifecycle, repo, gate, and current-step context. [6]
- The two row builders and the variant they compute. **Re-read against the reverted module:** the ranges below are the CALL SITES (`docRow(`/`seriesRow(`), which is what this row can point at now; the builders themselves are `docRow` at `:738-786` and `seriesRow` at `:788-837`, they compute the `Dot` variant as `lifecycle?.state ?? statusVariant(...)`, and `statusVariant` maps `DocStatus` alone. [7]
- "from agents_remember.models.task_document import DocStatus" — `statusVariant`'s entire input vocabulary (imported from "from agents_remember.models.task_document import DocStatus, StepStatus"). [8]
- `Dot` owns the lifecycle-state treatments (`awaiting-developer`, `paused`, `abandoned`) this list passes through, and is `aria-hidden`. [9]
- The `task-state` span carries `aria-label` with no role, inside the React Aria `ListBoxItem` whose `role="option"` names it. [10]
- The shared hierarchy helper computes parent matches, child-id hierarchy labels, parent selection keys, and the exported `orderedByCreation`. [11]
- The L14 orchestration-command helpers this list's `commandFacts`/`seriesRow` tier derivation calls. [12]
- The V4 chevron insignia rendered on tier rows (size `row`). [13]
- L14 tier tests: the three-level hierarchy with 22px indents + the D3 flat-run regression. [14]
- Focused tests assert root docs, active-enclosure leaves, enclosure fallbacks, and tooltip context are visible while loose/inactive/cleanup-completed leaves are absent, then prove BY REPO indentation/parent keys and BY PHASE flatness. [15]
- `fmtWait` for server-computed stale/wait ages. [16]
- Shared typed selection keys (`taskDocSelectionKey`/`seriesSelectionKey`/`lifecycleSelectionKey`, `parseTaskSelection`) and the `taskLabel`/`taskDocumentLabel` helpers used by the list and detail panel. [17]
- The shared `Panel` head/sticky band the pivot sits in. [18]
- Task-row pickup spinner/check-chat notice. [19]

## 260821-CLIVE Discarded Progress Boundary

Document and series rows pass producer-owned `discardedCount` into `progressHint()`. The visible hint
keeps normal `done/total` progress and appends a distinct `N discarded` segment. A discarded-before-start
task therefore remains auditable without incrementing completion or changing active row admission.
Existing worktree-existence, identity, hierarchy, lifecycle-vs-document state, accessibility, and
keep-alive boundaries remain unchanged.

## Current L5I Maintenance

The lifecycle rail accepts an `active` signal. Its locally advancing staleness clock stops while a
kept-alive rail is hidden, while the render-heavy row/group derivation lives in a memoized child so
clock and parent renders do not reconstruct the React Aria list unnecessarily.

## MIK-R95 Comment-Only Delta

The enclosure comment no longer names the removed rail panel; no admission, join, tier, collapse, accessibility or rendering behavior changed.
