# dashboard/src/panels/file-viewer/FileViewer.tsx

| Field                  | Value                                                |
| ---------------------- | ---------------------------------------------------- |
| repository             | agents-remember                                      |
| path                   | `dashboard/src/panels/file-viewer/FileViewer.tsx`    |
| doc_type               | `file-level-onboarding`                              |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`           |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                        |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FileViewer` is the **File Viewer** centre tab (operations-integration slice L2) — the page component
itself. A repository selector + a mainline/enclosure scope selector drive two Headless Tree explorers (a
**code** tree and an **onboarding** tree) over the L1 read-only files API; the right side is the reusable
`DualPane`. Pairing is **bidirectional**: opening a code file derives its sidecar (forward), and opening a
sidecar opens its partner code file (reverse) or, for a partnerless overview, renders that doc's own
markdown full-pane (falling back to an overview placeholder only when its body is unreadable). It is the
first consumer of
the L1 files API and is kept mounted (hidden) full-bleed across tab switches, so its repo/scope selection,
open file, and tree state survive a switch.

## Code Commentary

### Logic

Holds all view state with `useState`: `repos` (the catalog), `repo`, `scope` (default `"mainline"`),
`code` (`FileContent | null`), `sidecar` (a `SidecarView`), `error`, plus `split` from
**`usePersistedFlag("fileviewer.split", true)`** so split/single survives a reload AND a file switch. A
mount effect calls **`fetchRepos()`**, stores the catalog, and selects the first repo; an `alive` flag
guards against a setState after unmount. A second effect **resets `code`/`sidecar` to empty when `repo` or
`scope` changes** so a re-root never shows a stale file. `scopeItems` derives the scope picker from the
current repo's `mainline` + `worktrees`. 260715-FEUI-L2 hardened the repos fetch: a catalog
response WITHOUT `repos` (an unexpected server shape or a generic test stub) degrades to `[]`
instead of poisoning state with `undefined` — the old `setRepos(cat.repos)` put every later
render's `repos.find` into a crash loop (a real latent robustness bug the L2 leaf's timing shift
surfaced via `ChangeSetViewer.test.tsx`'s generic fetch stub; reviewer-accepted collateral fix).
**`openCode(entry)`** guards non-file / same-file, then
`readFile` → `resolveForward` and sets the sidecar to `markdown` (when found with a body) or `missing`.
**`openSidecar(entry)`** calls `resolveReverse`; a `kind:"sidecar"` hit with `exists` re-enters `openCode`
on the partner code path (closing the loop), otherwise it clears `code` and sets the sidecar to
`{ state: "markdown", body }` when the doc is a `kind:"overview"` with a non-null `body` (so an opened
`overview.md` renders its own prose full-pane in the reader), falling back to the `{ state: "overview" }`
placeholder only when the body is unreadable or there is no onboarding. Errors are normalised by
`describeError` (a `FilesApiError.code`, else `"request failed"`).
Render: a toolbar of two `PickList`s (a local React Aria `Select` wrapper) + a split/single toggle button
(`aria-pressed`) + an error badge; then a horizontal `PanelGroup` (`autoSaveId "fileviewer.outer"`) whose
left panel stacks the two `FileTree`s and whose right panel hosts `DualPane`.

### Conventions

Panda `css`/`cva` from `../../../styled-system/css` (relative import; no path alias). React Aria `Select`
owns dropdown behaviour, Panda owns looks; `react-resizable-panels` owns the split (sizes persisted by
`autoSaveId`). Each `FileTree` is given `key={`${repo}:${scope}:side`}` so a repo/scope change **remounts**
the tree (a clean re-root). `data-testid="file-viewer"`.

### Invariants And Boundaries

Read-only over the L1 files API — no new endpoints and **no store mutation** (the page owns its own
component state). The `alive` flag on the repos fetch and the same-file guard in `openCode` avoid redundant
work / setState-after-unmount. Bidirectional pairing is the load-bearing contract: forward derives a
sidecar, reverse opens a partner code file or renders a partnerless overview's own markdown (placeholder
only when the body is unavailable). View-mode lives outside file-scoped
state so it survives file switches and reload. The page is kept mounted (hidden) by `Cockpit` across tab
switches and is full-bleed (drops the rails), like the Engine Room / Topology / Chats views.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reusable dual-pane this page mounts on the right; supplies its `SidecarView` shape. | `SidecarView` | dashboard/src/panels/file-viewer/DualPane.tsx:14-18 |
| The one tree explorer rendered twice (code + onboarding sides). | `FileTree` | dashboard/src/panels/file-viewer/FileTree.tsx:44-96 |
| The persisted split/single flag (`localStorage`-backed). | `localStorage` | dashboard/src/panels/file-viewer/usePersistedFlag.ts:1-1 |
| The files API client — `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` + types. | `fetchRepos`; `readFile`; `resolveForward`; `resolveReverse` | dashboard/src/data/files.ts:108-111; dashboard/src/data/files.ts:116-121; dashboard/src/data/files.ts:123-131; dashboard/src/data/files.ts:133-141 |
| The shell that registers + keeps this view mounted across tab switches. | `CockpitShell` | dashboard/src/cockpit/Cockpit.tsx:385-666 |
| The route overview that governs this page. | `# dashboard/src/panels/file-viewer/ — File Viewer Overview` | onboarding/dashboard/src/panels/file-viewer/overview.md:1-107 |

## Current L5I Maintenance

The mounted-but-hidden File Viewer defers its repository-catalog request until its first actual
showing. A settled success or failure is retained across later hide/show cycles, while concurrent
StrictMode effects share the in-flight request instead of multiplying boot reads; the component is
memoized between meaningful `active` transitions.

## Update History

- 2026-08-02T16:44:12+02:00 — 260731-EFA-L6 W1-B05 curator: anchored 5 citation items; scoped citation check now passes.

- 2026-07-24T13:17:17Z — Curator: documented first-visible catalog loading, settled read posture,
  and the keep-alive memo boundary; verification fields remain pre-commit.

- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (collateral, reviewer-accepted): one defensive line in
  the repos mount effect — `cat.repos ?? []` — so a `repos`-less catalog response degrades to the
  empty list instead of an `undefined` state that crash-looped `repos.find` on the next render
  (deterministic latent bug; surfaced by the L2 leaf's microtask-timing shift under
  `ChangeSetViewer.test.tsx`'s generic fetch stub, suite back to zero unhandled errors).
  Verification metadata pinned to the leaf base until closeout stamps the L2 code commit.
- 2026-06-30T00:00:00+02:00 — operations-integration L5: `openSidecar`'s overview branch now carries the doc body — it sets the sidecar to `{ state: "markdown", body }` when a `kind:"overview"` reverse-pairing has a non-null `body` (so opening an `overview.md` renders its prose full-pane), falling back to `{ state: "overview" }` only when the body is unreadable.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the File Viewer page — repo/scope selectors driving two Headless Tree explorers (code + onboarding) over the L1 files API, a reusable `DualPane` on the right, bidirectional code↔onboarding pairing, and a persisted split/single mode; kept mounted full-bleed across tab switches. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
