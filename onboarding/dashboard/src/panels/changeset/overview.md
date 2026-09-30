# dashboard/src/panels/changeset/ — Change-Set Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/changeset/`                |
| doc_type               | `route-local-overview`                           |
| lastUpdated | 2026-09-30T20:36:31+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`       |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview      | `../overview.md`                                 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The optional marks and the marked pane. | "marks?: PaneMarks;"; "const { portals, placement, gutterFor, drawn } = useMarkedPane(marks);" | dashboard/src/panels/changeset/DiffPane.tsx:141-148 |
| The two extracted view builders, each with its marks gutter. | `splitView`; `inlineView` | dashboard/src/panels/changeset/DiffPane.tsx:77-121 |

## 260928-MIK-L31 The Diff Pane Can Show An Excerpt With Its File's Line Numbers

`MIK-R31` reaches this route through one governed source. [`DiffPane.tsx`](DiffPane.tsx.md) gains two optional
props for the reviewer's focused expression cards, both inert at their defaults: `firstLine` (each side's first line
in its file, so the before and after editors number an excerpt from the file's own lines, through
`file-viewer/lineNumbering.ts`'s `numberedFrom`) and `fit` (a content-sized host, the merge view capped at `32rem`,
so the card rather than the pane scrolls). The change-set viewer passes neither and renders exactly as before. The
card that uses them is `panels/review/ExpressionCards.tsx` (`ChangedExcerpt`: a changed range's real diff with
`collapse={false}`).

| Finding | Anchor | Source |
| --- | --- | --- |
| The optional first lines and the content-sized host. | `DiffPane`; `fitHost` | dashboard/src/panels/changeset/DiffPane.tsx:50-60; dashboard/src/panels/changeset/DiffPane.tsx:123-193 |
| The card that passes them. | `ChangedExcerpt` | dashboard/src/panels/review/ExpressionCards.tsx:463-496 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The master request now asks for the per-leaf breakdown; presence of `leaves` is the discriminant. | `includeLeaves`; `seriesLeaves` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222; dashboard/src/panels/changeset/ChangeSetViewer.tsx:294-300 |
| The rendered rail and its per-leaf counters, and the click that opens one leaf's own range. | `LeafBreakdown`; `onOpenLeaf` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:397-429; dashboard/src/panels/changeset/ChangeSetViewer.tsx:715-721 |
| The named refusal and the named measured-empty pane, i.e. the two states that are not a missing selection. | `ChangeSetRefusal`; `ChangeSetMainPane` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:506-525; dashboard/src/panels/changeset/ChangeSetViewer.tsx:530-549 |
| The cockpit re-target that keeps the opened leaf inside this route's takeover. | `onOpenLeaf` | dashboard/src/cockpit/Cockpit.tsx:601-601 |

## Update History
- 2026-09-30T20:36:31+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **route body updated for MIK-R34.** Added the section "260928-MIK-L34 The Diff Pane Can Carry Marks On Its File Lines": `DiffPane`'s optional `marks` prop and the two view builders extracted unchanged; two rows. The Change-Set Viewer passes no marks and is unchanged. The fixer normalised the three rows that cite `DiffPane.tsx`, `ExpressionCards.tsx` and `FilePane.tsx` to where their constructs now sit (`63-140` → `123-193`, `49-59` → `50-60`, `434-463` → `463-496`, `24-64` → `25-78`); no claim changed.
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No route impact: this route's governed sources are unchanged. **Reopened claim re-read and retained:** MIK-L32 changed the `IntentReviewEntry` construct (it now renders the lane's count after `+N −N`), but the entry still carries the task context only, `review: {}` for a live leaf and `{ historical: true }` for a closed one, so the claim holds; the row is re-anchored from the construct name to its line-exact declaration ("export function IntentReviewEntry({") and keeps its range (`131-171`); this pass's generated bullet for the row was removed, since its anchor changed. The installed fixer also re-pointed the `onOpenLeaf` row (its bullet kept) and normalised the rows into `DiffPane.tsx`, `Cockpit.tsx` and `ReviewSurface.tsx`; no other claim changed. No verification stamp was advanced.
- 2026-09-30T12:05:20+00:00: Generated citation repair: `onOpenLeaf` repointed to dashboard/src/cockpit/Cockpit.tsx:601-601. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): **route body updated for MIK-R31.** Added the section "260928-MIK-L31 The Diff Pane Can Show An Excerpt With Its File's Line Numbers" at the top: `DiffPane`'s optional `firstLine` and `fit` for the focused expression cards, inert at their defaults. Two rows added.
- 2026-09-28T21:39:14+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): No route impact: this change-set route did not change. The one row in the L2 section that cites the sibling reviewer was re-read after L48 split `ReviewSurface.tsx` (931 → 585 lines, record panes moved to `ReviewRecordPanes.tsx`): `ReviewTarget` still receives the change set's task and optional subject, and `ReviewSurface`/`useSurface` still ask for that task's own review, so the claim holds and its three ranges were re-derived from the declarations. No stamp advanced.
- 2026-09-28T17:05:06+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **route body updated — the task entry carries no subject any more (`ICR-R24@v3`).** The paragraph on what the entry carries now states that since L47 `IntentReviewEntry` opens the task-context target (or the recorded one) and the reviewer chooses the subject; the three rows that cited the removed `selected.selector_*` spelling and the entry-side catalogue read were reworded and re-cited. The other displaced rows into files L47 changed were re-pointed from the base-to-candidate line mapping. No stamp advanced.
- 2026-09-26T21:08:28+00:00: Generated citation repair: `leafIsLive` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:560-572. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:08:28+00:00: Generated citation repair: "onClick={() => onOpen(generation ? { ...target, generation } : target)}" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:140-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Repointed shared catalogue/grouping ownership to the extracted source; source-review entry remains available independently of knowledge.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `leafIsLive` repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:686-698. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: "onClick={() => onOpen(generation ? { ...target, generation } : target)}" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **citation repair only; no route-level fact changed.** The identity row's two anchors (`selected.selector_kind`, `selected.selector_id`) moved with `detail-panel/changeSetBar.tsx`'s own round-2 insertions and now resolve at `:595`/`:596`. No panel, takeover dispatch, target shape or claim was changed by this pass. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **route body updated — the series view shows what the net is made of, and names what it cannot show.** The new section records the `includeLeaves: true` request, the `by leaf (N)` rail and its per-leaf counters, the click that opens a landed leaf's committed range (no live worktree needed) or a working leaf's delta, the cockpit re-target, and the two named states. **One false sentence was corrected in place:** the Purpose paragraph said "series requests omit the unused per-leaf summary" — the superseded `includeLeaves: false` optimisation — and now states the new request shape with the retention of the option recorded explicitly. The Route Model's master bullet now says the breakdown is rendered rather than merely carried. **Citation accounting:** the rows this leaf's line movement displaced were re-derived against the candidate with the gate's own resolver. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **route body updated — the change-set refusal reaches the control.** The new section records the rendering half of the D01 repair on the control this route governs, states that `ChangeSetViewer.tsx` is byte-identical, and points the transport half at the `dashboard/src/data` route. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The L3 read-only change-set API this screen consumes. | `task_changeset` | mcp/src/agents_remember/serving/changeset.py:100-119 |
| The same-origin client wrapping that API. | `taskChangeset` | dashboard/src/data/changeset.ts:78-79; dashboard/src/data/changeset.ts:167-168; dashboard/src/data/changeset.ts:158-158 |
| The shell that hosts the takeover + restores the rails. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:892-948 |
| The detail panel button + counters that open this screen. | `ChangeSetButton` | dashboard/src/panels/detail-panel/changeSetBar.tsx:66-166 |
| The reused read-only CodeMirror pane + theme + lang map. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:25-78 |
| The markdown renderer the sidecar column + rendered-markdown toggle reuse. | `Markdown` | dashboard/src/grammar/Markdown.tsx:109-159 |
| The siege-tank empty-state backdrop shown until a file is picked. | `EmptyStateBackdrop` | dashboard/src/panels/EmptyStateBackdrop.tsx:52-97 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The target variant this route's type gained. | `ChangeSetTarget` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:33-55 |
| The declaration's own statement that no change-set request comes from a review, and that an empty object on the field is the task-context entry rather than a missing selector. | "never mounted for one, so no change-set" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:46-47 |
| **The reviewer entry: offered for every leaf beside the working/committed actions (the recorded comparison for a closed leaf, `ICR-R12`).** | "Intent review" | dashboard/src/panels/detail-panel/changeSetBar.tsx:1-7 |
| **The identity the entry carries instead of a filesystem path (since `260921-ICR-L47`): the task context only, `review: {}` for a live leaf and `{ historical: true }` for a closed one — no subject.** | "export function IntentReviewEntry({"; "review: live ? {} : { historical: true }" | dashboard/src/panels/detail-panel/intentReviewEntry.tsx:131-171 |
| **The read that supplies the subject now belongs to the reviewer, taking the comparison's task context and nothing else.** | `useReviewCatalogue`; `intentReviewEntries` | dashboard/src/data/useReviewCatalogue.ts:79-111; dashboard/src/data/review.ts:724-730 |
| **The one liveness predicate both gated entries share.** | `leafIsLive` | dashboard/src/panels/detail-panel/changeSetBar.tsx:397-409 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| **The generation the open series view is bound to, and the caption that renders it.** | `boundSeriesGeneration`; `SeriesGenerationTag` |dashboard/src/panels/changeset/ChangeSetViewer.tsx:305-312; dashboard/src/panels/changeset/ChangeSetViewer.tsx:317-330|
| **The entry button threading the published generation into the viewer target.** | "onClick={() => onOpen(generation ? { ...target, generation } : target)}" | dashboard/src/panels/detail-panel/changeSetBar.tsx:151-164 |

## Update History
- 2026-09-22T17:20:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **route body update for the subject catalogue (`ICR-R09@v1`).** The governed sources of this route changed (the entry half's catalogue rewrite and its client/picker consumers), so this overview's body rows naming the renamed constructs (`useReviewSubject` → `useReviewCatalogue`, `ReviewSubjectRead` → `ReviewCatalogueRead`, the selected-row target spelling) and the ranges this leaf's candidate moved were re-read and re-derived by hand; no route-level fact was otherwise changed. **Stamp accounting:** the verification pair names the leaf's base; closeout owns the stamp once the code commit exists.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **route body updated.** The section above is added at the end of this route's change narrative, immediately before this history, so no heading above it moved. It records this route's own impact: the series view bound to its listed generation (target pins, list-response preference, per-expansion binding, header caption), the entry button threading, and the R24 boundary. The Purpose and Route Model now say generation-bound instead of "since the series base"/"`<tip>`", and every row into a file this leaf moved was re-derived (serving entry, client, button, hook, predicate, target variant). One known-false prose paragraph is deliberately left for its owner (see report): the L22 section still gates the reviewer entry on `live && subject`, while ICR-R16 made it liveness-alone — reviewer-entry behavior this leaf does not change. No verification stamp was advanced; the candidate is uncommitted and the governed closeout owns the real stamp. The paragraph said the entry appears "only when the bar's target is a live admitted curator candidate and a selector id was supplied (`live && selectorId`)", and that "the new props are optional and defaulted … so every existing caller that supplies neither renders exactly what it rendered before this leaf" — true when written, and precisely the defect: no production caller supplied a selector, so the entry never rendered on any real navigation. The props are gone; the subject is read from `GET /api/review/intent/entries` by `useReviewSubject`, and the gate is `live && subject`. The card states that this is not a weakening — a refusal, an empty list, a rejected promise and a non-live leaf all leave the subject undefined, which is the L22 semantics — and that liveness was extracted into one `leafIsLive` predicate shared with the working action. Three rows that cited the removed props or the old gate were replaced with rows citing the current gate, the server-supplied identity and the shared predicate; no claim was silently dropped. No verification stamp was advanced.
- 2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **added the L22 section** — the `review` variant `ChangeSetTarget` gained and why it is a dispatch field rather than a fifth change-set mode, plus the "Intent review" entry `changeSetBar.tsx` adds beside the working/committed actions for a live candidate that names a selector. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns that stamp.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: changeset files changed only by behavior-preserving lint remediation and import-path updates.

- 2026-08-04T18:05+02:00 — 260731-EFA-L6 S18-B17 curator: re-anchored the detail-panel row from the
  `DetailPanel` memo export (cited range was a bare `);`) to the operative `ChangeSetButton`
  function (counters, fetches, and the `open-changeset` button) at its exact frozen-source extent.
  Claim wording unchanged.
- 2026-08-02T20:43+02:00 — W2-B08: anchored 7 change-set viewer citation claims and supplied exact source paths; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2 route impact: the existing Change-Set Viewer now makes series net requests without unused per-leaf summaries, exposes loading before the first response, preserves errors, and refreshes working data only after the prior cycle settles. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-30T00:00:00+02:00 — L5 (diff-viewer polish): three viewer refinements — (1) `ChangeSetPane` gains a
  **rendered-markdown** toggle (`changeset-rendered-toggle`) that, for `.md` diffs, swaps the raw merge
  diff for a formatted `<Markdown>` view (persisted per column); (2) the changed-file **row highlight**
  is fixed to the File-Viewer amber wash (`color-mix(in oklab, var(--amber) 20%/12%, transparent)`),
  replacing the invisible `background: bg`; (3) the no-file column-2 placeholder becomes a faint
  **siege-tank `EmptyStateBackdrop`** (`/assets/sc2-siege-tank-boomerang.mp4`, `opacity 0.18`) behind
  the "Select a changed file" prompt. Updated the `ChangeSetPane`/`ChangeSetViewer` Route Model bullets,
  the Hot Path Summary, and the references (added `EmptyStateBackdrop`). A new `ChangeSetPane.test.tsx`
  sidecar covers the rendered toggle. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — L4a: the screen learns the **leaf views** — `ChangeSetViewer` takes a `leaf` +
  `mode` target (committed/working, precedence `leaf > master > scope`), labels the header, and is per-file
  inspectable via `leafFileDiff`; the **working** view auto-refreshes its file list and the
  currently-open file's diff on a 2.5s interval (a live delta, not a frozen snapshot — committed/series/scope
  never poll); and `DiffPane`'s `host` css turns
  `.cm-changedText` into a full-height highlight **rectangle** (dark muted green/red fills, `!important`
  over the library theme) instead of the default underline. Updated the `ChangeSetViewer`/`DiffPane` Route
  Model bullets + the Invariants. (The takeover's back-to-origin behaviour is a `cockpit/Cockpit.tsx`
  change — see its sidecar.) Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: the **series/master view is now inspectable** — `master` drives the
  NET `git diff <master-base> <tip>` (via the file-diff `master` param) so its rows open per-file diffs like a
  leaf's (per-leaf counters kept alongside); and the `DiffPane` host makes `.cm-mergeView` the bounded scroll
  container so a long split diff scrolls. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4: the Change-Set Viewer route — a
  task-scoped takeover screen over the L3 `/api/changeset/*` API (column-1 changed code/onboarding rows,
  column-2/3 a read-only `@codemirror/merge` diff with split/inline/full-file/highlight-off toggles,
  code↔sidecar partner column), reusing the L2 File Viewer primitives; master scope is accumulated-only.
  Verification metadata pinned to the task base until closeout stamps the L4 code commit.

## 260921-ICR-L2 The Review Target May Carry No Subject

**Route meaning changed, narrowly: the change-set viewer's `ChangeSetTarget.review` field may now carry
no selector.** Its type is `{selectorKind?: ReviewSelectorKind; selectorId?: string}` and the viewer's
own behaviour is unchanged — it reads the field only to decide whether the target is a review at all, and
the cockpit's takeover dispatch is what consumes the selector — but the field's contract is now stated
where it is declared: its **presence** marks a review target, and an **empty object** is the task-context
entry, the review opened from the task alone that lists the complete source inventory. That is the shape
a task with no recorded invariant still has, and it is why the entry is no longer gated on a subject.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The target type whose review field may carry no selector, with presence as the marker and an empty object as the task context.** | `ChangeSetTarget` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:33-55 |
| The entry that produces the empty target for a live leaf the server offers no subject for. | `useReviewCatalogue`; `DocChangeSetBar` | dashboard/src/data/useReviewCatalogue.ts:79-111; dashboard/src/panels/detail-panel/changeSetBar.tsx:315-365 |
| The surface that receives it and asks for the task's own review. | `ReviewTarget`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:43-50; dashboard/src/panels/review/ReviewSurface.tsx:534-598 |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **route body updated — citation repair only, forced by this leaf's change to two sources this route overview cites, and no route-level fact changed.** `dashboard/src/panels/detail-panel/changeSetBar.tsx` no longer spells the entry's recorded subject as `subject.selector_kind`/`subject.selector_id` (it is read off the entry read's own value, ICR-R16), so the identity row that anchors that spelling was re-anchored onto the current source text and its range re-derived onto the lines that carry it (`:240-255`); the entry-hook row was re-derived onto the hook's declaration (`:93-135`). No route, panel, takeover dispatch or target shape changed on this route, and no claim's wording was weakened — the two rows still assert exactly what they asserted, against the construct that now holds it. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **citation re-derivation forced by this leaf's line shifts; no route impact.** This leaf's dashboard change is confined to the sibling `panels/review/` child and the `data/` route: `panels/review/SourceContent.tsx` is new, `panels/review/ReviewSurface.tsx` grew 462 → 549 lines (its inventory rows are now openable), and `data/review.ts` gained the expansion wire types and `reviewSourceContent`. The one row of the L2 section above that cited `ReviewSurface.tsx` by line was therefore re-derived against the candidate — `ReviewTarget`/`ReviewSurface` `27-37`/`395-462` → `30-39`/`482-549` — and it is the only row this document carries into that file. **The prose is not false and was not reworded:** `ChangeSetTarget.review`'s contract is unchanged (its presence still marks a review, an empty object is still the task-context entry), `ChangeSetViewer`'s own behaviour is unchanged, and the change-set viewer is still never mounted for a review. Nothing in this leaf touches `ChangeSetViewer.tsx`, `ChangeSetPane.tsx`, `DiffPane.tsx` or the change-set route's own API. **Stamp accounting:** the verification pair now names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — and the recorded working candidate records this leaf's uncommitted candidate; no commit contains the new bytes, so closeout owns the real stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, code base `702714fc`): **route body updated.** The review field on a change-set target may now carry no selector, and its declaration records what that means: presence marks a review, an empty object is the task-context entry. The viewer's behaviour is unchanged. The section is appended at the end of this route's narrative, and the one row of this document that cited `ChangeSetViewer.tsx` by line was re-derived against the candidate in the same pass. **No verification stamp was advanced** — the candidate is uncommitted and closeout owns the real stamp.
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

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **one enforced out-of-bounds citation rewritten to the construct it names, wording unchanged.** The row citing the surface that receives the target ended `946`, past the end of a `ReviewSurface.tsx` this leaf shortened to `910` lines when the complete source change explorer moved into its own module; the row now cites the surface component's own extent, `819-910`, which still carries both of the row's anchors (`ReviewSurface` at the declaration and `ReviewTarget` in its props type). The row's other three ranges are kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T04:31:21+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **route body updated for the review target's record (ICR-R12@v1).** The section above records the one
optional field, that it is part of the target's identity rather than a decoration, and that no
filesystem path travels with it. **Citation accounting:** every row on this overview that cited
`ChangeSetViewer.tsx` by line was re-derived against this candidate. **Stamp accounting:** no
verification stamp was advanced — the header already names this leaf's base as the production line the
reading was taken against, and nothing in this leaf is committed, so the governed closeout owns the real
stamp.
