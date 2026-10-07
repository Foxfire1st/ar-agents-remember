# dashboard/src/panels/changeset/ — Change-Set Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/changeset/`                |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## 260928-MIK-L34 The Diff Pane Can Carry Marks On Its File Lines

`MIK-R34` reaches this route through one governed source. [`DiffPane.tsx`](DiffPane.tsx.md) gains an optional `marks`
prop for the reviewer's per-hunk intent markers, inert when absent: through `file-viewer/markGutter.tsx`'s
`useMarkedPane`, each editor gets a marks gutter first in its extensions (`gutterFor("before" | "after", first)`, no
extension without marks), the pane calls `drawn` once its editors exist (which expands a collapsed run holding a mark)
and at teardown, `placement` joins the effect's dependencies, and the marks' portals render after the host. To keep the
component within the function-size rule the split and inline view builders were extracted unchanged into `splitView`
and `inlineView` over a shared `DiffBuild`. The Change-Set Viewer (`ChangeSetPane`) passes no marks, so its diff is
exactly the landed one; the reviewer's source view, lane windows and card excerpts are the only callers that pass them.

- The optional marks and the marked pane. [1]
- The two extracted view builders, each with its marks gutter. [2]

## 260928-MIK-L31 The Diff Pane Can Show An Excerpt With Its File's Line Numbers

`MIK-R31` reaches this route through one governed source. [`DiffPane.tsx`](DiffPane.tsx.md) gains two optional
props for the reviewer's focused expression cards, both inert at their defaults: `firstLine` (each side's first line
in its file, so the before and after editors number an excerpt from the file's own lines, through
`file-viewer/lineNumbering.ts`'s `numberedFrom`) and `fit` (a content-sized host, the merge view capped at `32rem`,
so the card rather than the pane scrolls). The change-set viewer passes neither and renders exactly as before. The
card that uses them is `panels/review/ExpressionCards.tsx` (`ChangedExcerpt`: a changed range's real diff with
`collapse={false}`).

- The optional first lines and the content-sized host. [3]
- The card that passes them. [4]

## 260921-ICR-L32 The Change-Set Read's Refusal Now Reaches The Control That Asked

One of this route's governed sources changed, and the change is about **what a caller can tell apart**. `panels/detail-panel/changeSetBar.tsx` (governed here because this route owns the change-set reading surface) now renders the refusal's own code and reason beside a state marker, with a read still in flight kept as its own state, while the transport half — `data/changeset.ts` carrying the refusal instead of clearing the counters — is recorded on the `dashboard/src/data` route. `ChangeSetViewer.tsx`, which this route is named for, is **byte-identical** on these bytes: the defect was in the live-leaf "committed" control's read, not in the viewer, and saying so is the point of a route record. The case that pins the rendering drives the click and asserts the rendered reason, so "the control is present" is not mistaken for "the control works" — the rule `D49` was recorded for.

## 260921-ICR-L33 The Series View Shows What The Net Is Made Of

`ICR-R33` reaches this route in three places, and the first is the one a reader would otherwise be
misled by.

**The series request now asks for the breakdown.** `ChangeSetViewer`'s `changesetListRequest` passes
`includeLeaves: true` on the master branch (and `detail-panel/changeSetBar.tsx` does the same for its
counters read), so `MasterChangeset.leaves` arrives carrying one row per leaf with its own `state` and
its own counters. A payload that predates the breakdown — or a task/leaf payload, which has no `leaves`
field at all — reads as no breakdown rather than an invented one (`seriesLeaves` keys on the field's
presence).

**The answer is rendered as attribution.** `LeafBreakdown` draws a `by leaf (N)` rail beneath the two
changed-file lists (`changeset-leaves`, one `changeset-leaf-row` per leaf, each with a
`changeset-leaf-counters` span). Each row is a button that hands the leaf id and the mode its own
`state` implies to `onOpenLeaf`: `committed` for a landed leaf — the historical route that needs no live
worktree — and `working` for a leaf still in flight, which is the range that exists for it. `Cockpit`
supplies `onOpenLeaf` from its own `openChangeSet`, so the leaf opens in THIS takeover instead of a
second screen.

**What could not be shown is named.** `ChangeSetRefusal` renders the route's own refusal — code, HTTP
status, reason, offending input and next action — under `data-review-state`/`data-review-code`, and
`ChangeSetMainPane` names a change-set that measured empty in both halves instead of showing the
pick-a-file backdrop. Both reuse the existing `ReviewFailure` vocabulary; no second decoder and no new
route were added.

- The master request now asks for the per-leaf breakdown; presence of `leaves` is the discriminant. [5]
- The rendered rail and its per-leaf counters, and the click that opens one leaf's own range. [6]
- The named refusal and the named measured-empty pane, i.e. the two states that are not a missing selection. [7]
- The cockpit re-target that keeps the opened leaf inside this route's takeover. [8]

## Purpose

`changeset/` is the **Change-Set Viewer** (operations-integration slice L4): a task-scoped screen that
shows what a task — or a series master (the NET diff between its declared endpoints, bound to the
generation the list published) — changed, as an up-to-3-column diff. It is the
frontend consumer of the L3 read-only change-set API (`GET /api/changeset/{task,file-diff,master}`,
served by `serving/changeset.py`) and reuses the L2 File Viewer primitives (`FilePane`, `codemirrorTheme`,
`langByExtension`, `usePersistedFlag`, `grammar/Markdown`). It is opened as a **takeover** from a
`DetailPanel` change-set button: `CockpitShell` renders it full-bleed in place of the railed Operations
body, and the screen's back link restores the rails.

The viewer renders an explicit loading placeholder until its first change-set
response and preserves request errors. Working leaf refreshes run the list and
active-file requests together, then schedule the next cycle only after both
settle; series requests carry the net's OWN per-leaf breakdown (`includeLeaves: true`, 260921-ICR-L33 /
R33.2) and render it as a `by leaf (N)` rail, so the net total is attributable to the leaves it sums.
(The pre-260921-ICR-L33 sentence here said the opposite — "series requests omit the unused per-leaf
summary" — and was false at this candidate: it described the `includeLeaves: false` optimisation commit
`a1521685` introduced, which R33.2 supersedes. The option itself is retained by `data/changeset.ts` and
`serving/changeset.py` for any caller that genuinely renders only the net; no dashboard master reader
is such a caller any more.)

## Route Model

- `ChangeSetViewer.tsx` — the screen. Column 1 splits into two rows — **changed code files** /
  **changed onboarding files** (path + git status + `+ins/−del`, from `taskChangeset` or
  `masterChangeset`); the active/hover row now wears the File-Viewer-tree **amber wash**
  (`color-mix(in oklab, var(--amber) 20%/12%, transparent)`) so the selected file actually looks
  selected (the old `background: bg` was invisible against the panel). Column 2 is the selected file's
  diff (`ChangeSetPane`, always visible once a row is picked) — until then it shows a faint **siege-tank
  empty-state backdrop** (`EmptyStateBackdrop`, `/assets/sc2-siege-tank-boomerang.mp4` at `opacity 0.18`)
  behind the "Select a changed file" prompt; column 3 is the code↔sidecar partner, opened from a per-row
  split affordance. A `scope`
  (one active enclosure) drives the full per-file diff via `/api/changeset/file-diff`; a `master` drives
  the **NET** series diff (`git diff <master-base> <selected-result>`, pinned to the listed generation
  when the entry carries one) via the same endpoint's `master` param, so its
  rows are equally inspectable (the per-leaf counter breakdown rides alongside, each row labelled
  `committed`/`working`, and since 260921-ICR-L33 it is RENDERED: a `by leaf (N)` rail under the
  changed-file lists, one row per leaf with both halves' file/insertion/deletion counts, whose click
  opens that leaf's own range — `committed` for a landed leaf, `working` for one still in flight —
  through `onOpenLeaf`, the hook the cockpit supplies so the reader stays in this takeover). The list response publishes the bound generation (four commits +
  deterministic digest) with its currentness, rendered as a header caption, and every file
  expansion carries it — so an opened entry stays bound after the branch advances. **L4a** adds the `leaf`
  target (`+ mode`): a leaf's `committed` (landed) or `working` (uncommitted) change-set via the `leaf` +
  `mode` selector on the same routes — equally per-file inspectable — with the header labelling the view
  (`committed · <leaf>` / `working · <leaf> · uncommitted`). A counters header + a back link sit above the
  `react-resizable-panels` columns.
- `ChangeSetPane.tsx` — one diff column with a toolbar of persisted toggles (`usePersistedFlag`,
  per-column `keyPrefix`): the task doc's three states map onto two flags — **change-set** (collapsed
  diff) / **full-file + highlight** (uncollapsed diff) / **full-file + highlight-off** (the plain L2
  `FilePane` on the after-content) — plus a split⇄inline flip for whichever diff shows. For **markdown**
  files it also offers a **"rendered"** toggle (`changeset-rendered-toggle`) that swaps the raw diff for
  a formatted `<Markdown>` view (in an `mdScroll` container), so a changed onboarding doc reads as nicely
  here as in the file reader.
- `DiffPane.tsx` — the one genuinely new CodeMirror primitive: a read-only `@codemirror/merge` pane.
  `split` = `MergeView` (a=before, b=after, side by side); `inline` = `unifiedMergeView` over a single
  `EditorView` (doc=after). It reuses `FilePane`'s exact read-only extension set (`lineNumbers` +
  `EditorState.readOnly` + `EditorView.editable.of(false)` + `lineWrapping` + `codeTheme` + the lazy
  `langExtension`) so tokens match across the plain and diff views; both are read-only (no revert/merge
  controls). Built imperatively in an effect with a `disposed` guard against a late async language
  resolve. Its `host` css also renders `.cm-changedText` as a full-height highlight **rectangle** (dark
  muted green for additions, red for deletions) rather than `@codemirror/merge`'s default thin underline
  (L4a) — dark fills, not the bright `--mint`/`--amber` tokens, so the light diff text stays legible.

## Invariants And Boundaries

- Read-only over the L3/L4a change-set API; no store mutation — the screen owns its own component state,
  fed by the `data/changeset.ts` client. An enclosure `scope` diffs base→worktree; a `master` the NET
  series range (`master_base → tip`); a `leaf` (`+ mode`) its `committed` (`base → code_commit`) or
  `working` (`HEAD → worktree`) range — all equally per-file inspectable, and a `leaf`/`master` view needs
  no live enclosure (it resolves off the contract), which is what lets the doc reader show it.
- Panda CSS owns looks, React Aria owns behaviour (the toggles are React Aria `ToggleButton`); no CSS
  animation (GSAP/Motion only — master invariant).
- Opened as a Cockpit **takeover** (rails hidden, full-bleed), not a standing mode-bar tab; the back link
  (or a mode-bar switch / a node `open()`) clears it and restores Operations. View-mode toggles persist
  across file switches via `usePersistedFlag`.

## Hot Path Summary

The Change-Set Viewer: a DetailPanel change-set button opens a full-bleed takeover — column 1 changed
code/onboarding rows (active row in an amber wash) over the L3 change-set API → column 2/3 a read-only
CodeMirror `@codemirror/merge` diff (split/inline/full-file/highlight-off, persisted) reusing the L2
FilePane, with a **rendered-markdown** toggle for `.md` files and a faint siege-tank empty-state backdrop
until a file is picked; the back link restores the railed Operations view.

## Evidence

### Repo-Internal References

- The L3 read-only change-set API this screen consumes. [9]
- The same-origin client wrapping that API. [10]
- The shell that hosts the takeover + restores the rails. [11]
- The detail panel button + counters that open this screen. [12]
- The reused read-only CodeMirror pane + theme + lang map. [13]

- The markdown renderer the sidecar column + rendered-markdown toggle reuse. [14]
- The siege-tank empty-state backdrop shown until a file is picked. [15]

## 260915-KS-L22 The Review Variant Beside The Change-Set Actions

This route gained the reviewer's target variant and the entry that produces it, and nothing else on
it changed. `ChangeSetTarget` now carries an optional `review?: { selectorKind; selectorId }` — the
reviewed subject's recorded identity — and the variant is a *dispatch* field rather than a fifth
change-set mode: the change-set viewer is never mounted for a target that carries it, so the three
ranges this screen already owns (`scope`, `master`, and `leaf` with its `mode`) keep their meaning
exactly and no request this route makes is ever issued from a review. The declaration says as much
in its own comment, which is where a reader arriving at the type will look first.

`changeSetBar.tsx` renders the reviewer entry **beside** the working and committed actions and never
in their place: a third `ChangeSetButton` labelled "Intent review" appears only when the bar's target
is a live admitted curator candidate **and the bar holds a reviewed subject** (`live && subject`).
That is the same liveness the working change-set action is gated on — now one extracted `leafIsLive`
predicate, so the two entries cannot come to disagree about what "live" means — and they appear
together.

**Superseded 2026-09-20 (260915-KS-L45): the selector is no longer a prop, and the old prop gate was
the reason the entry was unreachable.** The L22 increment gave `DocChangeSetBar` optional
`selectorKind`/`selectorId` props and gated the entry on `live && selectorId`. No production caller ever
supplied them: `taskReader.tsx` and the master header pass `kind`/`repo`/`master`/`leaf`/`onOpen` only,
so the condition could not hold on any real navigation. The props are **gone**; a live leaf's subject
is read from the server by `useReviewCatalogue`, which calls `intentReviewEntries(repo, master, leaf)`
and keeps `result.entries?.[0]`. The gate is not weakened: a refusal, an empty entry list, a rejected
promise and a non-live leaf all leave the subject `undefined`, so **no subject means no button** —
which is the L22 semantics, now reached through a source that can actually produce a subject.

What the entry carries is still an identity, not a path. Until `260921-ICR-L47` the target was
`{ repo, master, leaf, review: { selectorKind, selectorId } }` with the subject taken from the server's
catalogue. **Since L47 (`ICR-R24@v3`) the task entry carries no subject at all:** `IntentReviewEntry`
opens `{ repo, master, leaf, review: {} }` (or `{ historical: true }` for a closed leaf), and the
reviewer reads the catalogue and chooses the subject itself when it opens. The target type still admits
`selectorKind`/`selectorId` for callers that name one. The browser never chooses the candidate dataset,
because the resolution behind the route does that from the same task context. The screen that displays a
review belongs to the `panels/review/` child route; this route owns the target variant and the entry
that sets it, which is the boundary the two cards divide.

- The target variant this route's type gained. [16]
- The declaration's own statement that no change-set request comes from a review, and that an empty object on the field is the task-context entry rather than a missing selector. [17]
- **The reviewer entry: offered for every leaf beside the working/committed actions (the recorded comparison for a closed leaf, `ICR-R12`).** [18]
- **The identity the entry carries instead of a filesystem path (since `260921-ICR-L47`): the task context only, `review: {}` for a live leaf and `{ historical: true }` for a closed one — no subject.** [19]
- **The read that supplies the subject now belongs to the reviewer, taking the comparison's task context and nothing else.** [20]
- **The one liveness predicate both gated entries share.** [21]

## 260921-ICR-L13 The Series View Is Bound To Its Listed Generation

This route's series view is now generation-bound. `ChangeSetTarget` gained an optional
`generation?: MasterNetPins` — the exact recorded endpoints a listing published; empty /
absent means the declared integrated result. The viewer threads it into the list request
(a pinned list reopens the recorded net after the branch advances) and — via the list
response's own `generation`, which is newer than the entry's — into every file expansion, so
an opened entry stays bound after the branch advances. The header shows the bound generation
as a caption: short digest + currentness + the one scope this view ever serves. The viewer
implements no catalogue or drill-down; that is R24's obligation on top of what this view
exposes (`leaves[].state`, pinned params, per-view `generation`). The entry button that opens
the view (`ChangeSetButton`) carries the published generation into the target for master nets.

- **The generation the open series view is bound to, and the caption that renders it.** [22]
- **The entry button threading the published generation into the viewer target.** [23]

## 260921-ICR-L2 The Review Target May Carry No Subject

**Route meaning changed, narrowly: the change-set viewer's `ChangeSetTarget.review` field may now carry
no selector.** Its type is `{selectorKind?: ReviewSelectorKind; selectorId?: string}` and the viewer's
own behaviour is unchanged — it reads the field only to decide whether the target is a review at all, and
the cockpit's takeover dispatch is what consumes the selector — but the field's contract is now stated
where it is declared: its **presence** marks a review target, and an **empty object** is the task-context
entry, the review opened from the task alone that lists the complete source inventory. That is the shape
a task with no recorded invariant still has, and it is why the entry is no longer gated on a subject.

- **The target type whose review field may carry no selector, with presence as the marker and an empty object as the task context.** [24]
- The entry that produces the empty target for a live leaf the server offers no subject for. [25]
- The surface that receives it and asks for the task's own review. [26]

## 260921-ICR-L12 The Change-Set Target Carries The Record It Is Read From

`260921-ICR-L12` (`ICR-R12@v1`) adds one optional field to this route's `ChangeSetTarget.review`:
`historical?: boolean`. Absent is the live candidate — what every ordinary entry asks for — and `true`
is the leaf's own **recorded comparison**, the entry a closed leaf offers because its worktree is gone
and the durable generation is the only comparison there is.

**The field is part of the target's identity, not a decoration on it.** It travels from the change-set
bar through the takeover to `ReviewSurface`, which passes it to the review client and keys its state on
it, so the record the reader chose is the record the server is asked for. No filesystem path is added to
any target in any branch: the browser names a record and the server owns which comparison that record
is, exactly as it already owned which candidate the live read resolves.

The committed and working change-set actions themselves are unchanged — this route's own resolution of
a series or a leaf change-set reads nothing about records — and the change is additive for every
existing caller.
