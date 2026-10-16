# dashboard/src/panels/changeset/ChangeSetViewer.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetViewer` is the **Change-Set Viewer screen**: the up-to-3-column takeover that shows what
a task (`scope` = one active enclosure), a series master (`master` = the NET diff between its
declared endpoints, bound to the generation the list published), or — L4a — a single `leaf`
(in `committed` or `working` `mode`) changed. It is opened
by a `DetailPanel` change-set button and hosted by `CockpitShell` as a full-bleed takeover (its `onBack`
clears it, restoring the rails).

`ChangeSetViewer` is the change-set viewer screen: a takeover that lists changed code and onboarding files and opens per-file diffs. It serves four selectors with one rendering — an enclosure scope, a series-master net, a leaf committed/working delta, and (new in W03) a recorded review comparison — and, when opened from the reviewer, filters that comparison's list by the lane destinations with per-row badges and one explanatory sentence.
## Code Commentary

### Logic

Series loads request the net change-set **with** its per-leaf breakdown
(`includeLeaves: true`, 260921-ICR-L33 / R33.2). The route already answers one
row per leaf and the viewer now renders that answer as a `by leaf (N)` rail, so
the net total beside it is attributable to the leaves it sums. The earlier
`includeLeaves=false` optimisation — "render only the net", added with the
serving escape by `a1521685` — is SUPERSEDED by this leaf rather than deleted:
the option is still supported by `data/changeset.ts` and by
`serving/changeset.py`, and any caller that genuinely renders nothing but the
net may still ask for it. The
working leaf view now waits for its initial data, then runs list and active-file
refreshes together and schedules the next cycle only after both settle. The
viewer renders a loading placeholder until data arrives, and a read that was
REFUSED or that measured empty is NAMED rather than left as an empty pane (see
the 260921-ICR-L33 section below); stale refresh results are ignored after
teardown. A current failed poll clears the prior successful value and shows its refusal; cached success is not displayed as current after failure.

Props are `ChangeSetTarget` plus `onBack`, optional `onOpenLeaf` and optional `reviewContext` (`ViewerProps`). `ChangeSetTarget` carries `comparison?: number`, while `reviewContext` is a viewer prop, not a target field. A set comparison is passed to `loadChangeSet`, whose shared URL builder selects the numbered task-endpoint read first; otherwise selection precedence remains leaf > master > scope, with `includeLeaves: true` and generation pins on master reads. The target-change effect uses the shared conditional list/file resources, ignores stale completion and resets selection-local file/diff/partner state. A 304 reuses the retained parsed identity; callbacks remain local. A leaf still qualifies its master; series mode remains master-without-leaf.
A second effect **polls the working view** every 2.5s (gated on `mode === "working"`): it refreshes `data`
(so a file edited *after* the viewer opened shows up in the list, and the counters track) AND re-fetches the
currently-open file's diff (`active`) so an edit to the file you are LOOKING AT updates in place. The
open-diff re-fetch is non-disruptive: the DiffPane only rebuilds when the before/after content actually
changed, so an unchanged poll is a no-op (no flicker / scroll-reset) — it re-renders only when that file is
the one edited. Committed and series views are snapshots; the working leaf view polls its working tree,
while the scope view reflects the selected task/base-worktree state and may change independently.

The header is a back button (`changeset-back`) + a title (`committed · {leaf}` / `working · {leaf} ·
uncommitted` for a leaf, `series {master} · net since series start` for the series, else the scope) +
a counters block (`changeset-counters`: `code +ins −del (files)` and the same for memory, from
`data.counters`). Column 1 (`PanelGroup` left `Panel`) is two scrolling sections — **changed code** and
**changed onboarding** — each row a button (status chip + ellipsised path + `Counts`); the active/hover
row now carries the File-Viewer-tree **amber wash** (`background: color-mix(in oklab, var(--amber) 20%,
transparent)` active, `12%` hover) — the old `background: bg` active state was indistinguishable from
the panel, so the selected file looked unselected. For a code row
with `hasSidecar` (or an onboarding row with a derivable partner) a small split affordance opens it
**with** its partner in column 3. `open(kind, file, withPartner?)` sets `active` and loads the diff via
`loadDiff` — `leaf ? leafFileDiff(repo, master, leaf, kind, path, mode) : master ? masterFileDiff(repo,
master, kind, path, generation) : fileDiff(repo, scope, kind, path)` — so **every mode is per-file inspectable**
(leaf committed/working, master net, and an enclosure scope all open a real diff); `withPartner` also loads
`partnerOf(...)` into `partner` (column 3). `partnerOf` maps a code
path to `onboarding/{path}.md` when `hasSidecar`, and a memory path back to its code partner via
`partnerCodePath` (strip `onboarding/` + `.md`, rejecting `overview`/`entities`/`.index`). Column 2 shows
the `diff`'s `ChangeSetPane` (`keyPrefix="changeset.main"`) or — until a file is picked — an
**empty-state backdrop**: an `<EmptyStateBackdrop src="/assets/sc2-siege-tank-boomerang.mp4"
opacity={0.18}>` (the faint siege-tank boomerang loop the File Viewer / Operations also use; `0.18`
is brighter than the shared `0.14` default because the clip reads darker) wrapping the "Select a
changed file" prompt, inside a flex-column `emptyHost` so the backdrop's `flex:1` canvas fills the
Panel. **260921-ICR-L33 split that single expression into `ChangeSetMainPane`, which owns three
states**, and the third one is the point: the picked file's diff; a NAMED measured-empty statement
(`changeset-empty` — "no changed file in either half — this change-set is measured empty (code 0
file(s) · memory 0 file(s))", rendered whenever the answer carried zero files in both halves); and
only otherwise the backdrop + prompt above. A measured zero is a measurement, not an absence of an
answer, and the pick-a-file backdrop no longer stands in for it. Column 3 mounts a second `ChangeSetPane`
(`keyPrefix="changeset.partner"`) when a partner is loaded.


**`ChangeSetTarget.review` is a cockpit dispatch identity that may carry no subject.** Its optional selector fields (and `historical` flag) are read by the cockpit: presence selects `ReviewSurface`, and an empty object opens the task-context review. This dispatch is distinct from the reviewer's All/Unexplained/Unknown changes actions, which mount `ChangeSetViewer` with a recorded `comparison` and viewer-owned `reviewContext`, issuing comparison list and file-diff reads.

**260921-ICR-L13 bound the series view to its listed generation.** `ChangeSetTarget` gained an
optional `generation?: MasterNetPins` — the exact recorded endpoints a listing published; empty /
absent means the declared integrated result. Three constructs carry it: `seriesListMeta` reads
the series list response back out when it names its own `generation` (a task/leaf payload never
carries one, so the check is the discriminant, not the entry target);
`boundSeriesGeneration` prefers the list response's generation (it is newer than the entry's)
and falls back to the entry's pins, and every file expansion below carries the bound
generation, so an opened entry stays bound after the branch advances. `SeriesGenerationTag`
renders the bound net as a header caption — short digest + currentness + the one scope this
view ever serves (`gen {digest8} · {currentness} · integrated`), only when the list response
names its generation, so older payloads read unchanged. The viewer implements no catalogue
or drill-down: that is R24's obligation on top of what this view exposes.

### Conventions

Panda `css`; `react-resizable-panels` (`PanelGroup`/`Panel`/`PanelResizeHandle`, `autoSaveId="changeset.outer"`).
Reuses the L3 `data/changeset` client + `FilesApiError`, and the shared `EmptyStateBackdrop` for the
no-file canvas. `data-testid`s: `changeset-viewer`, `changeset-back`, `changeset-counters`,
`pane-placeholder` (now the **error** display only — the no-file empty state is the `EmptyStateBackdrop`,
whose own `empty-backdrop` testid appears only when motion is enabled), `changeset-open-sidecar`.

**260915-KS-L22 introduced `ChangeSetTarget.review` as a cockpit dispatch field.** The cockpit's
review branch mounts `ReviewSurface`, not this viewer, and the optional selector names a recorded
subject rather than a path. That entry dispatch remains separate from the current reviewer's
comparison-page destination: `ReviewSurface` can mount `ChangeSetViewer` over the retained review
with a `comparison` number and `reviewContext`, so a review can now issue change-set requests.
`ReviewSelectorKind` remains a type import for the dispatch field.

### Invariants And Boundaries

Read-only over the L3/L4a API; owns selection-local component state while store-owned bounded conditional resources retain list/file results. Every target opens real
per-file diffs: an enclosure `scope` diffs base→worktree, **master mode** the NET series range
(`master_base → selected result`, pinned to the listed generation when one is bound) via `masterFileDiff`, and a **leaf** its `committed` (base→code_commit) or
`working` (HEAD→worktree uncommitted) range via `leafFileDiff` — a `leaf` always carries its `master`
qualifier. The back link is the only exit it controls (the Cockpit host also clears the takeover on a
mode-bar switch or a node `open`). Placeholders are stable-size (no flip-flop).

`ChangeSetTarget` carries `comparison?: number`; `ViewerProps` (and the exported component props) carry `reviewContext?: ReviewChangeContext`. A set comparison is selected first (`changesetListRequest` passes the complete address, including `comparison`, to `loadChangeSet`; `diffRequestFor` delegates to `comparisonFileDiff`); otherwise leaf > master > scope is unchanged. The review filter state (`all` | `unexplained` | `unknown`) starts from the reviewer's page and narrows the list through `filteredChangeSet`; `ReviewFilters` shows destination counts and `FILTER_NOTES` under a non-all filter. The comparison header names `comparison N · leaf`, offers `← Back to intent review`, and displays the two abbreviated code trees through `ComparisonTreesTag`, not all four operands. `useComparisonFirstFile` opens the initial file. Comparisons do not auto-poll; non-comparison targets remain unfiltered and retain their existing behavior.
## Evidence

### Repo-Internal References

- The mount/target-change effect selects the leaf, task, or master request (the master branch now threads the entry `generation` as pins), fetches it through `req.then`, and reruns when target inputs change. [1]
- The series view is bound to its listed generation: the list response's own generation when it names one (else the entry's pins) flows into every file expansion, with a digest/currentness/scope caption. [2]
- The `open` handler invokes `loadDiff`, whose branch chooses the master (generation-bound), leaf, or scoped file-diff path. [3]
- Code↔sidecar partner mapping uses the forward and reverse helpers. [4]
- The viewer invokes the L3 leaf, master, task, and file-diff client calls. [5]
- The viewer mounts a main `ChangeSetPane` and mounts a partner pane only when `partner` exists. [6]
- The Cockpit takeover that mounts it full-bleed and supplies `onBack`. [7]
- The middle pane's three states — the picked file's diff, a NAMED measured-empty change-set, and only otherwise the backdrop with the "Select a changed file" prompt. [8]
- The DetailPanel controls that open it with a change-set target. [9]
- The loading, back, and master-file NET-diff behavior pinned in the tests, plus the new generation-binding case. [10]

- A comparison target uses `loadChangeSet` with its numbered comparison address. [18]
- Per-file diffs on a comparison read the recorded trees [19]
- The filter row shows each destination with its lane file count [20]
- The comparison header names its number and offers the way back [21]
- The filter's first file opens on entry [22]
## 260921-ICR-L12 The Review Target Carries Which Record It Is Read From

`260921-ICR-L12` (`ICR-R12@v1`) adds one optional field to this module's `ChangeSetTarget`:
`review?: { selectorKind?: ReviewSelectorKind; selectorId?: string; historical?: boolean }`. Absent
means the live candidate, which is what every ordinary entry asks for, and `true` means the leaf's own
recorded comparison — the entry a **closed** leaf offers, where the worktree is gone and the durable
generation is the only comparison there is.

The field is part of the target's identity rather than a decoration on it, because the takeover that
reads the target hands the record to `ReviewSurface` and the surface asks the server for exactly that
record. Nothing else in the module changed: the committed and working change-set actions are untouched,
and no filesystem path is added to any target.

## 260921-ICR-L33 A Landed Master's Leaves, And What Each One Accounts For

This screen was reachable for a master whose leaves had all landed, and it showed a single
unattributable number. `260921-ICR-L33` (`ICR-R33@v1`) changes what the series read asks for and what
the screen does with the answer.

**The read asks for the breakdown.** `changesetListRequest` passes `includeLeaves: true` on the master
branch, so `MasterChangeset.leaves` arrives carrying one row per leaf with that leaf's own `state`
(`committed` | `working`) and its own `counters` for both halves. A payload that predates the
breakdown — or a task/leaf payload, which has no `leaves` field at all — reads as no breakdown rather
than an invented one: `seriesLeaves` keys on the field's PRESENCE, which is the discriminant the mixed
union already had.

**The answer renders as attribution, not a second total.** `LeafBreakdown` draws a `by leaf (N)` rail
beneath the changed-file lists (`changeset-leaves`, one `changeset-leaf-row` per leaf, each with a
`changeset-leaf-counters` span reading `code F file(s) +I −D · memory F file(s) +I −D`). Each row is a
button whose click hands the leaf id and the mode its own `state` implies to `onOpenLeaf`:
`committed` for a landed leaf — the historical route (`leafChangeset(..., "committed")`, bound to the
leaf's own `code_commit`) that R33.3 needs and that works with **no live worktree**, because closeout
removed it — and `working` for a leaf the read still reports in flight, which is the range that
actually exists for it. `onOpenLeaf` is optional: with no holder the rows render disabled rather than
silently inert.

**A leaf opened from here stays in the same takeover.** `Cockpit.tsx`'s `ChangeSetTakeover` now
threads its own `openChangeSet` action in as `onOpenLeaf`, and `ChangeSetViewer` composes the new
target (`{ repo, master, leaf: id, mode }`) from the row — so the reader re-targets ONE screen instead
of having to find the leaf somewhere else. `master` rides along as the leaf's qualifier, exactly as
every other leaf target on this route carries it.

**What could not be shown is NAMED.** `ChangeSetWorkspace` used to render `error` as a bare status
string and nothing else. `ChangeSetRefusal` now renders the route's own refusal as an answer: the
owner's code and HTTP status in their own element (`changeset-refusal`), then the reason, the offending
input and the next action the body published, under `data-review-state` / `data-review-code` for the
shared refusal vocabulary. It reuses `reviewProblemFromCause` (the same `ReviewFailure` decode
`detail-panel/changeSetBar.tsx` already used for its counters read) rather than introducing a second
decoder; the shared `TOKEN_BY_CODE[code] ?? "domain-refused"` fallback in `data/reviewTransport.ts` is
untouched, and an unknown code being carried as `domain-refused` remains its deliberate behaviour.

**The pane's third state is a measurement.** `ChangeSetMainPane` names a change-set that measured
empty in both halves (`changeset-empty`) instead of showing the pick-a-file backdrop, which would
claim there was nothing to pick rather than that nothing was measured. The refusal and the empty
statement are different facts and are rendered as different ones.

- The master branch of the list request now asks for the per-leaf breakdown; a task/leaf payload has no `leaves` field, so presence is the discriminant. [11]
- The rail that renders the breakdown: one row per leaf with its own state chip and both halves' counters. [12]
- A leaf row opens that leaf's own range — `committed` for a landed leaf, `working` for one still in flight — through the hook the cockpit supplies. [13]
- The refusal is carried as an answer: the owner's code and status, its reason, the offending input and the next action. [14]
- The measured-empty statement, and the three states of the middle pane. [15]
- The cockpit re-target that keeps a leaf opened from the net in the same takeover. [16]
- The delivered cases: per-leaf counters, opening a landed leaf and a working leaf from the rail, the named refusal, and the named measured-empty. [17]
