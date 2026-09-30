# dashboard/src/panels/changeset/ChangeSetViewer.tsx

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/changeset/ChangeSetViewer.tsx`   |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated | 2026-09-30T12:15:39+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`             |
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetViewer` is the **Change-Set Viewer screen**: the up-to-3-column takeover that shows what
a task (`scope` = one active enclosure), a series master (`master` = the NET diff between its
declared endpoints, bound to the generation the list published), or — L4a — a single `leaf`
(in `committed` or `working` `mode`) changed. It is opened
by a `DetailPanel` change-set button and hosted by `CockpitShell` as a full-bleed takeover (its `onBack`
clears it, restoring the rails).

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
teardown.

Props are `{ repo, scope?, master?, leaf?, mode?, generation?, onBack, onOpenLeaf? }` (`ChangeSetTarget` +
`onBack`, plus the 260921-ICR-L33 re-target hook the cockpit supplies). Selection
precedence is **`leaf > master > scope`**: on mount / target change an effect fetches `leaf ?
leafChangeset(repo, master, leaf, mode) : master ? masterChangeset(repo, master, { includeLeaves: true, pins }) : taskChangeset(repo,
scope)` into `data` (a `live` flag drops a stale resolve; a `FilesApiError` is shown as `code
(httpStatus)`), and resets the selection/diff/partner state. `isLeaf = Boolean(leaf)`; `isSeries =
Boolean(master) && !leaf` (a `leaf` carries `master` as its qualifier, so series mode is master-without-leaf).
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


**`ChangeSetTarget.review` became a target that may carry no subject.** Its type is now `{ selectorKind?: ReviewSelectorKind; selectorId?: string }`, and the comment above it records the two facts a reader needs: the field's **presence** is what marks a target as a review (the cockpit's takeover dispatch is what reads it, and the change-set viewer is never mounted for one, so no change-set request is made from a review), and an **empty object** is the task-context entry — the review opened from the task alone, which lists the complete source inventory and is what a task with no recorded invariant still has. Nothing else in the module changed: the viewer reads the field only to decide whether it is a review target at all.

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

**260915-KS-L22** gave `ChangeSetTarget` one more member and deliberately no behaviour: an optional
`review?: { selectorKind: ReviewSelectorKind; selectorId: string }`, the Intent Reviewer's own
selector, naming the reviewed subject's recorded identity rather than a filesystem path. The member
is carried by the *target* and read by the cockpit's takeover dispatch, which is what decides between
this viewer and `ReviewSurface`; the component itself never reads `review`, and `Cockpit` mounts
`ChangeSetViewer` only on the branch where `target.review` is absent. That is the invariant to hold
when reading this file: a review target can reach this module's type without reaching its mount, so
**no change-set request is ever made from a review**, and the `ReviewSelectorKind` import is a type
import on that account.

### Invariants And Boundaries

Read-only over the L3/L4a API; owns its own component state (no store mutation). Every target opens real
per-file diffs: an enclosure `scope` diffs base→worktree, **master mode** the NET series range
(`master_base → selected result`, pinned to the listed generation when one is bound) via `masterFileDiff`, and a **leaf** its `committed` (base→code_commit) or
`working` (HEAD→worktree uncommitted) range via `leafFileDiff` — a `leaf` always carries its `master`
qualifier. The back link is the only exit it controls (the Cockpit host also clears the takeover on a
mode-bar switch or a node `open`). Placeholders are stable-size (no flip-flop).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mount/target-change effect selects the leaf, task, or master request (the master branch now threads the entry `generation` as pins), fetches it through `req.then`, and reruns when target inputs change. | "const req = changesetListRequest(repo"; "void req.then("; "const listRequest = leafChangeset(repo, m, leaf, \"working\");"; "masterChangeset(repo"; "taskChangeset(repo, scope ?? \"\")" |dashboard/src/panels/changeset/ChangeSetViewer.tsx:452-452; dashboard/src/panels/changeset/ChangeSetViewer.tsx:453-453; dashboard/src/panels/changeset/ChangeSetViewer.tsx:484-484; dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222; dashboard/src/panels/changeset/ChangeSetViewer.tsx:223-223|
| The series view is bound to its listed generation: the list response's own generation when it names one (else the entry's pins) flows into every file expansion, with a digest/currentness/scope caption. | "boundSeriesGeneration"; "seriesListMeta"; "SeriesGenerationTag"; "changeset-generation" |dashboard/src/panels/changeset/ChangeSetViewer.tsx:305-305; dashboard/src/panels/changeset/ChangeSetViewer.tsx:283-283; dashboard/src/panels/changeset/ChangeSetViewer.tsx:317-317; dashboard/src/panels/changeset/ChangeSetViewer.tsx:324-324|
| The `open` handler invokes `loadDiff`, whose branch chooses the master (generation-bound), leaf, or scoped file-diff path. | "const loadDiff"; "masterFileDiff("; "fileDiff("; "const open"; "void loadDiff(kind" |dashboard/src/panels/changeset/ChangeSetViewer.tsx:684-684; dashboard/src/panels/changeset/ChangeSetViewer.tsx:239-239; dashboard/src/panels/changeset/ChangeSetViewer.tsx:240-240; dashboard/src/panels/changeset/ChangeSetViewer.tsx:687-687; dashboard/src/panels/changeset/ChangeSetViewer.tsx:692-692|
| Code↔sidecar partner mapping uses the forward and reverse helpers. | `partnerCodePath` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:201-206 |
| The viewer invokes the L3 leaf, master, task, and file-diff client calls. | "leafChangeset(repo, master ?? \"\", leaf, mode ?? \"committed\")"; "masterChangeset(repo"; "taskChangeset(repo, scope ?? \"\")"; "fileDiff(repo, scope ?? \"\", kind, path)" |dashboard/src/panels/changeset/ChangeSetViewer.tsx:217-217; dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222; dashboard/src/panels/changeset/ChangeSetViewer.tsx:223-223; dashboard/src/panels/changeset/ChangeSetViewer.tsx:240-240|
| The viewer mounts a main `ChangeSetPane` and mounts a partner pane only when `partner` exists. | "ChangeSetPane diff={diff}"; "ChangeSetPane diff={partner}"; "partner ?" |dashboard/src/panels/changeset/ChangeSetViewer.tsx:531-531; dashboard/src/panels/changeset/ChangeSetViewer.tsx:637-637; dashboard/src/panels/changeset/ChangeSetViewer.tsx:633-633|
| The Cockpit takeover that mounts it full-bleed and supplies `onBack`. | "<ChangeSetViewer" | dashboard/src/cockpit/Cockpit.tsx:601-601 |
| The middle pane's three states — the picked file's diff, a NAMED measured-empty change-set, and only otherwise the backdrop with the "Select a changed file" prompt. | `ChangeSetMainPane`; "Select a changed file" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:530-549; dashboard/src/panels/changeset/ChangeSetViewer.tsx:545-545 |
| The DetailPanel controls that open it with a change-set target. | `ChangeSetButton`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:66-166; dashboard/src/panels/detail-panel/changeSetBar.tsx:315-365 |
| The loading, back, and master-file NET-diff behavior pinned in the tests, plus the new generation-binding case. | "shows loading until the request resolves instead of rendering a zero-file result"; "calls onBack when the back link is clicked"; "opens a per-file NET diff from a clickable row in master mode"; "binds master file expansions to the generation the net listing published" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:65-86; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:122-130; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:262-280; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:280-313 |

## Update History
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `dashboard/src/cockpit/Cockpit.tsx` (two imports, the `knowledge` destination, the reader-hash initial view and the `ViewBody` case), so the citation rows into it that moved were re-pointed by the installed fixer (its generated bullets in this list) and by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T09:55:44+00:00: Generated citation repair: "<ChangeSetViewer" repointed to dashboard/src/cockpit/Cockpit.tsx:601-601. No content impact: mechanical anchor-range projection bound to citation source snapshot 33e107d812c1dd3f1f44473057fb87849c6d5f902a8c0ec12b93f5e2833dc93f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-28T17:04:44+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: the row "The DetailPanel controls that open it with a change-set target" was re-read after L47 restructured `DocChangeSetBar`; it still holds (the change-set buttons and the new `IntentReviewEntry`, mounted by the bar, open this viewer with a `ChangeSetTarget`), so its wording is retained. Its ranges and three other rows into files L47 changed were re-pointed from the base-to-candidate line mapping, each valid at base and valid after mapping. No stamp advanced.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T23:30:00+02:00 — 260921-ICR-L33 curator (candidate `ar/260921-icr-l33-ar`, uncommitted; code base `86639933d61528387ce106dbd4d7a334bd468671` plus the working-tree delta; adversarial round 2 `verify-l33.md` = `pass`): **body update — a master's landed leaves and their per-leaf scale reach this screen.** Three false sentences were corrected in place. (1) "Series loads request the net change-set with `includeLeaves=false`" and the code quote beside it (`{ includeLeaves: false, pins }`) described the optimisation commit `a1521685` added — its own docstring's "callers rendering only the net can skip those extra per-leaf git diffs" — which **R33.2 supersedes**: both readers that ask for a master's net (`ChangeSetViewer`'s own `changesetListRequest` and `detail-panel/changeSetBar.tsx`) now pass `includeLeaves: true`, and the section above states both the new behaviour and that the option itself is retained. (2) The column-2 paragraph said the pane shows the diff "or — until a file is picked — an empty-state backdrop", which is now three states, the third being a NAMED measured-empty change-set. (3) The row that anchored `{diff ? (` — a span that exists nowhere at this candidate — was re-anchored onto `ChangeSetMainPane`, the construct that now owns those states. The new section below records the per-leaf rail (`by leaf (N)` with each leaf's own code and memory files/insertions/deletions), the row that opens a landed leaf's COMMITTED range and a working leaf's working delta, the refusal carried as an answer (`ChangeSetRefusal`: `data-review-state`/`data-review-code`, the owner's code, status line, reason, offending input and next action), and the `onOpenLeaf` hook the cockpit threads so a leaf row re-targets the same takeover. **Citation accounting:** every row this leaf's line movement or re-anchoring displaced was re-derived against the candidate with the gate's own resolver rather than by adding a delta to an old number. **Two mechanical-projection bullets were RETIRED:** the 2026-09-18 and 2026-09-05 "Generated citation repair" records for the `"<ChangeSetViewer"` row were removed, because that row is now re-read and re-cited by hand at `dashboard/src/cockpit/Cockpit.tsx:595-595` and the projection record is superseded by a curator reading rather than left standing beside it; no new projection bullet was written, and this paragraph is the dated disposition of both. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **the series view is bound to its listed generation (468 → 542 lines).** The section above records `generation` on the target, `seriesListMeta`/`boundSeriesGeneration`/`SeriesGenerationTag` with the digest/currentness/scope caption, pins threaded through the list and expansion requests, and the new `binds master file expansions…` case; the Purpose and master-mode invariant now say generation-bound instead of "since the series base". **Citation accounting:** the duplicated mount-effect row is merged into one (it was the same claim twice with different stale ranges), and every row was re-derived against this candidate — the import block, `generationTag`, pin-threading and the three new helpers moved every construct below `:16`, so pre-existing ranges shifted (e.g. `partnerCodePath` `:157-162` → `:166-171`, `loadDiff`/`open` `:453-458` → `:505-513`, panes `:398-416` → `:452-468`). Each reopened claim is retained with its range regenerated onto the extent that holds its anchor's declaration. The 2026-09-21 mechanical projection bullet below that recorded the superseded ranges (`:172`/`:174`/`:175`/`:191`) is retired by this reading — those lines no longer hold their anchors, and this entry is the curator-read evidence that replaces it. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.
- 2026-09-21T23:24+02:00 — 260921-ICR-L14 curator, **sync-merge resolution of the parked candidate against the landed ICR-L3 curation.** The two sides had curated this document independently and both sets of statements are kept: the landed `260921-ICR-L3` section, rows and history entries alongside this leaf's, tables unioned key by key (a row both sides carried keeps the ranges that hold its anchors in the merged code tree, the other side's range folded in where it is also true; rows only one side carried are kept in their own order), prose sections kept whole and Update History entries merged newest-first. The header states both facts: the production line is the master tip `a8d2431926d6b130012ca81ed2e85b14721c0615` (ICR-L3 landed) and this leaf's own code is still its uncommitted candidate. **Stamp accounting:** no verification stamp was invented; the stamp names the landed production line and the candidate rows name each uncommitted reading.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the review target's selector became optional, and an empty target became a meaning.** The type and its comment now record that presence marks a review and that `{}` is the task context; the viewer's own behaviour is unchanged because it only tests presence. One citation row was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

<!-- The two 2026-09-18 / 2026-09-05 "Generated citation repair" bullets for the "<ChangeSetViewer" row were RETIRED by the 260921-ICR-L33 entry above: that row has now been re-read and re-cited by hand against this candidate, so the projection record is superseded by a curator reading rather than standing beside it. Deleting them is what the gate's own projected-range item asks for ("re-cite the location the claim is about ... and only then advance the stamp"), and no new projection bullet was written. -->
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T14:53+02:00 — 260731-EFA-L6 S18-B13 curator: closed D5 false-branch connector evidence by fixer-generated ternary/backdrop ranges for the same-reviewer closing delta.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2: added honest loading state, kept explicit errors, opted series loads out of per-leaf summaries, and replaced overlapping working polling with settle-then-schedule refreshes. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-06-30T00:00:00+02:00 — L5 (diff-viewer polish): the no-file column-2 placeholder is replaced by an
  `EmptyStateBackdrop` (the faint `/assets/sc2-siege-tank-boomerang.mp4` loop at `opacity={0.18}`,
  in a flex-column `emptyHost`) wrapping the "Select a changed file" prompt — `pane-placeholder` now
  marks only the error state. The changed-file `row`'s active/hover highlight is fixed to the
  File-Viewer amber wash (`color-mix(in oklab, var(--amber) 20%/12%, transparent)`); the old
  `background: bg` was invisible against the panel. New import `EmptyStateBackdrop`; added a reference
  to its sidecar source. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — L4a: `ChangeSetTarget` gains `leaf?` + `mode?` (`"committed" | "working"`);
  `load`/`loadDiff` route a `leaf` through `leafChangeset`/`leafFileDiff` (precedence `leaf > master >
  scope`, `isSeries = master && !leaf`), and the header labels the leaf view (`committed · {leaf}` /
  `working · {leaf} · uncommitted`). A second effect polls the **working** view every 2.5s (working-only)
  so a file edited after opening appears in the list AND the currently-open file's diff updates in place
  (the open diff only rebuilds when its content actually changed). The stale "master per-file diffs not
  available" note was corrected. Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — L4 follow-up: **master mode is now inspectable** — rows are clickable and
  `loadDiff` routes the series `master` through `masterFileDiff` (the NET `base → tip` diff) vs a leaf's
  `scope` through `fileDiff`; the title reads "net since series start" and the master placeholder is the
  normal "Select a changed file". The per-task (leaf) view is unchanged. Verification metadata pinned until
  closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): the up-to-3-column
  takeover screen over the L3 `/api/changeset/*` API (column-1 changed code/onboarding rows + counters +
  back link, column-2 `ChangeSetPane` diff, column-3 code↔sidecar partner), with master mode rendered as
  an accumulated summary (no per-file diff). Verification metadata pinned to the task base until closeout
  stamps the L4 code commit.
2026-09-18T18:10+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): **recorded the review member on `ChangeSetTarget` and the boundary that keeps it inert
here.** The interface gained an optional `review?: { selectorKind: ReviewSelectorKind; selectorId:
string }` naming the Intent Reviewer's reviewed subject, with the comment stating that the cockpit's
takeover dispatch is what reads it and that this viewer is never mounted for a review — so a review
makes no change-set request. The new paragraph above states that boundary in the card's own voice,
because a reader who saw the field in the type would otherwise have to guess whether this component
honours it. No target, request, poll or render behaviour inside `ChangeSetViewer` changed, and the
card's existing Logic, Conventions and reference rows are left as they stand; ranges into this
source are the citation-reprojection engine's to move, not this pass's. The metadata block above
names this leaf's uncommitted candidate as what was read, and the two verification stamps are left
exactly as they were because no commit holds this candidate. The body was changed substantively and
this entry is the history record, not a metadata-only refresh.
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The master branch of the list request now asks for the per-leaf breakdown; a task/leaf payload has no `leaves` field, so presence is the discriminant. | `includeLeaves`; `seriesLeaves` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222; dashboard/src/panels/changeset/ChangeSetViewer.tsx:294-300 |
| The rail that renders the breakdown: one row per leaf with its own state chip and both halves' counters. | `LeafBreakdown`; `leafCountText`; "by leaf (" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:387-391; dashboard/src/panels/changeset/ChangeSetViewer.tsx:397-430 |
| A leaf row opens that leaf's own range — `committed` for a landed leaf, `working` for one still in flight — through the hook the cockpit supplies. | `onOpenLeaf`; "data-leaf-state" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:397-421; dashboard/src/panels/changeset/ChangeSetViewer.tsx:649-655; dashboard/src/panels/changeset/ChangeSetViewer.tsx:715-721 |
| The refusal is carried as an answer: the owner's code and status, its reason, the offending input and the next action. | `ChangeSetRefusal`; `reviewProblemFromCause` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:506-525; dashboard/src/panels/changeset/ChangeSetViewer.tsx:20-20; dashboard/src/panels/changeset/ChangeSetViewer.tsx:460-460 |
| The measured-empty statement, and the three states of the middle pane. | `ChangeSetMainPane`; "this change-set is measured empty" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:530-549; dashboard/src/panels/changeset/ChangeSetViewer.tsx:534-541 |
| The cockpit re-target that keeps a leaf opened from the net in the same takeover. | `onOpenLeaf`; `onOpenChangeSet` | dashboard/src/cockpit/Cockpit.tsx:567-577; dashboard/src/cockpit/Cockpit.tsx:601-601; dashboard/src/cockpit/Cockpit.tsx:912-944 |
| The delivered cases: per-leaf counters, opening a landed leaf and a working leaf from the rail, the named refusal, and the named measured-empty. | "lists the master net's leaves, each with its own code and memory counters (R33.2)"; "opens a landed leaf's committed change-set — and a working leaf's working delta — from the net (R33.3)"; "names the refusal when a landed leaf's committed range cannot be shown (R33.3)"; "names a measured-empty change-set instead of leaving the pane to the pick-a-file backdrop (R33.3)" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:363-387; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:388-420; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:421-453; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:454-473 |

## Update History
- 2026-09-23T04:30:48+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): **the review target carries which record it is read from (ICR-R12@v1).** One optional `historical`
field on the review target, absent for the live candidate and `true` for a closed leaf's recorded
comparison; the committed and working actions are unchanged. **Citation accounting:** the rows this
leaf's change moved were re-derived against the candidate. **Stamp accounting:** no verification stamp
was advanced — the candidate is uncommitted and the governed closeout owns the real stamp.
