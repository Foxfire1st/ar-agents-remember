# dashboard/src/panels/changeset/ChangeSetViewer.tsx

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/changeset/ChangeSetViewer.tsx`   |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-12T12:55+02:00                                 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`             |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetViewer` is the **Change-Set Viewer screen**: the up-to-3-column takeover that shows what
a task (`scope` = one active enclosure), a series master (`master` = the NET diff since the series base),
or — L4a — a single `leaf` (in `committed` or `working` `mode`) changed. It is opened
by a `DetailPanel` change-set button and hosted by `CockpitShell` as a full-bleed takeover (its `onBack`
clears it, restoring the rails).

## Code Commentary

### Logic

Series loads request the net change-set with `includeLeaves=false`. The
working leaf view now waits for its initial data, then runs list and active-file
refreshes together and schedules the next cycle only after both settle. The
viewer renders a loading placeholder until data arrives and retains the
explicit error state, while stale refresh results are ignored after teardown.

Props are `{ repo, scope?, master?, leaf?, mode?, onBack }` (`ChangeSetTarget` + `onBack`). Selection
precedence is **`leaf > master > scope`**: on mount / target change an effect fetches `leaf ?
leafChangeset(repo, master, leaf, mode) : master ? masterChangeset(repo, master) : taskChangeset(repo,
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
master, kind, path) : fileDiff(repo, scope, kind, path)` — so **every mode is per-file inspectable**
(leaf committed/working, master net, and an enclosure scope all open a real diff); `withPartner` also loads
`partnerOf(...)` into `partner` (column 3). `partnerOf` maps a code
path to `onboarding/{path}.md` when `hasSidecar`, and a memory path back to its code partner via
`partnerCodePath` (strip `onboarding/` + `.md`, rejecting `overview`/`entities`/`.index`). Column 2 shows
the `diff`'s `ChangeSetPane` (`keyPrefix="changeset.main"`) or — until a file is picked — an
**empty-state backdrop**: an `<EmptyStateBackdrop src="/assets/sc2-siege-tank-boomerang.mp4"
opacity={0.18}>` (the faint siege-tank boomerang loop the File Viewer / Operations also use; `0.18`
is brighter than the shared `0.14` default because the clip reads darker) wrapping the "Select a
changed file" prompt, inside a flex-column `emptyHost` so the backdrop's `flex:1` canvas fills the
Panel. Column 3 mounts a second `ChangeSetPane`
(`keyPrefix="changeset.partner"`) when a partner is loaded.

### Conventions

Panda `css`; `react-resizable-panels` (`PanelGroup`/`Panel`/`PanelResizeHandle`, `autoSaveId="changeset.outer"`).
Reuses the L3 `data/changeset` client + `FilesApiError`, and the shared `EmptyStateBackdrop` for the
no-file canvas. `data-testid`s: `changeset-viewer`, `changeset-back`, `changeset-counters`,
`pane-placeholder` (now the **error** display only — the no-file empty state is the `EmptyStateBackdrop`,
whose own `empty-backdrop` testid appears only when motion is enabled), `changeset-open-sidecar`.

### Invariants And Boundaries

Read-only over the L3/L4a API; owns its own component state (no store mutation). Every target opens real
per-file diffs: an enclosure `scope` diffs base→worktree, **master mode** the NET series range
(`master_base → tip`) via `masterFileDiff`, and a **leaf** its `committed` (base→code_commit) or
`working` (HEAD→worktree uncommitted) range via `leafFileDiff` — a `leaf` always carries its `master`
qualifier. The back link is the only exit it controls (the Cockpit host also clears the takeover on a
mode-bar switch or a node `open`). Placeholders are stable-size (no flip-flop).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The mount/target-change effect selects the leaf, task, or master request, fetches it through `req.then`, and reruns when target inputs change. | "const req = changesetListRequest(repo"; "void req.then("; "const listRequest = leafChangeset(repo, m, leaf, \"working\");"; "masterChangeset(repo"; "taskChangeset(repo, scope ?? \"\")" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:164-167; dashboard/src/panels/changeset/ChangeSetViewer.tsx:295-296; dashboard/src/panels/changeset/ChangeSetViewer.tsx:322-322 |
| The `open` handler invokes `loadDiff`, whose branch chooses the master or scoped file-diff path. | "const loadDiff"; "masterFileDiff("; "fileDiff("; "const open"; "void loadDiff(kind" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:182-183; dashboard/src/panels/changeset/ChangeSetViewer.tsx:442-442; dashboard/src/panels/changeset/ChangeSetViewer.tsx:445-445; dashboard/src/panels/changeset/ChangeSetViewer.tsx:450-450 |
| Code↔sidecar partner mapping uses the forward and reverse helpers. | `partnerCodePath` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:149-155 |
| The viewer invokes the L3 leaf, master, task, and file-diff client calls. | "leafChangeset(repo, master ?? \"\", leaf, mode ?? \"committed\")"; "masterChangeset(repo"; "taskChangeset(repo, scope ?? \"\")"; "fileDiff(repo, scope ?? \"\", kind, path)" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:164-190 |
| The viewer mounts a main `ChangeSetPane` and mounts a partner pane only when `partner` exists. | "ChangeSetPane diff={diff}"; "ChangeSetPane diff={partner}"; "partner ?" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:393-393; dashboard/src/panels/changeset/ChangeSetViewer.tsx:404-404; dashboard/src/panels/changeset/ChangeSetViewer.tsx:408-408 |
| The Cockpit takeover that mounts it full-bleed and supplies `onBack`. | "<ChangeSetViewer" | dashboard/src/cockpit/Cockpit.tsx:569-569 |
| The viewer renders the `EmptyStateBackdrop` whenever `diff` is absent. | "{diff ? ("; "Select a changed file" | dashboard/src/panels/changeset/ChangeSetViewer.tsx:392-392; dashboard/src/panels/changeset/ChangeSetViewer.tsx:398-399 |
| The DetailPanel controls that open it with a change-set target. | `ChangeSetButton`; `DocChangeSetBar` | dashboard/src/panels/detail-panel/changeSetBar.tsx:20-62; dashboard/src/panels/detail-panel/changeSetBar.tsx:69-115 |
| The loading, back, and master-file NET-diff behavior pinned in the tests. | "shows loading until the request resolves instead of rendering a zero-file result"; "calls onBack when the back link is clicked"; "opens a per-file NET diff from a clickable row in master mode" | dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:65-86; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:122-130; dashboard/src/panels/changeset/ChangeSetViewer.test.tsx:262-278 |

## Update History
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
