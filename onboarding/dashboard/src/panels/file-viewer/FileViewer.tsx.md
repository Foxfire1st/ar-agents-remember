# dashboard/src/panels/file-viewer/FileViewer.tsx

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
**`usePersistedFlag("fileviewer.split", true)`** so split/single survives a reload AND a file switch. The
first active showing calls **`fetchRepos()`** unless a previous attempt settled, stores the catalog, and selects the first repo; an `alive` flag
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
Render: a toolbar beginning with the shared Explorer sidebar toggle, followed by two `PickList`s (a local React Aria `Select` wrapper) + a split/single toggle button
(`aria-pressed`) + an error badge; then a horizontal `PanelGroup` (`autoSaveId "fileviewer.outer"`) whose
left panel stacks the two `FileTree`s and whose right panel hosts `DualPane`.

### Conventions

Panda `css`/`cva` from `../../../styled-system/css` (relative import; no path alias). React Aria `Select`
owns dropdown behaviour, Panda owns looks; `react-resizable-panels` owns the split (sizes persisted by
`autoSaveId`). Each `FileTree` is given `key={`${repo}:${scope}:side`}` so a repo/scope change **remounts**
the tree (a clean re-root). `data-testid="file-viewer"`.

### Invariants And Boundaries

File reads and pairing remain read-only over the L1 files API. The page additionally publishes its shown repository for tray routing; this is no file or task mutation. The page’s selection/pairing state remains component-owned. The `alive` flag on the repos fetch and the same-file guard in `openCode` avoid redundant
work / setState-after-unmount. Bidirectional pairing is the load-bearing contract: forward derives a
sidecar, reverse opens a partner code file or renders a partnerless overview's own markdown (placeholder
only when the body is unavailable). View-mode lives outside file-scoped
state so it survives file switches and reload. The page is kept mounted (hidden) by `Cockpit` across tab
switches and is full-bleed (drops the rails), like the Engine Room / Topology / Chats views.

`useSidebar("files", "left")` remembers Explorer visibility separately from the split/single flag. Shared hidden panel and handle props keep both trees mounted while removing the sidebar from layout and keyboard reach. The toolbar toggle remains outside it. While active, `usePublishPageRepository("File Viewer", repo || null, active)` names this page’s repository for taskless tray messages. DualPane receives the same repository and combines it with the selected file’s scope/path for its line gutter.

## Evidence

### Repo-Internal References

- The reusable dual-pane this page mounts on the right; supplies its `SidecarView` shape. [1]
- The one tree explorer rendered twice (code + onboarding sides). [2]
- The persisted split/single flag (`localStorage`-backed). [3]
- The files API client — `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` + types. [4]

- The shell that registers + keeps this view mounted across tab switches. [5]

- The route overview that governs this page. 

## Current L5I Maintenance

The mounted-but-hidden File Viewer defers its repository-catalog request until its first actual
showing. A settled success or failure is retained across later hide/show cycles, while concurrent
StrictMode effects share the in-flight request instead of multiplying boot reads; the component is
memoized between meaningful `active` transitions.

- The page owns files-left visibility and publishes only its active repository for tray context. [7]
- The Explorer remains mounted when hidden; its external toggle and code target stay in the page. [8]
