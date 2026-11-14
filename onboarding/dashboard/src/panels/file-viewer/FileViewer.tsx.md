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

The repository catalog hook owns repos, repo and error; the page owns scope and the persisted split/single flag. The history owns opened content, paired sidecars, Rendered/Source choices and saved scroll positions. The
first active showing calls **`fetchRepos()`** unless a previous attempt settled, stores the catalog, and selects the first repo; an `alive` flag
guards against a setState after unmount. Changing repository or scope clears the opened-entry history and active index, so the derived code and sidecar are empty. `scopeItemsFor` derives the scope picker from the current repository's mainline and worktrees. A catalog response without `repos` uses an empty list.
openCode ignores non-file entries, reads the code and its forward pairing, then pushes an opened history entry.
openSidecar resolves the reverse pairing. An existing code partner is read and pushed as a code history entry; a partnerless document is pushed with its readable Markdown body or an overview placeholder. Errors are normalised by
`describeError` (a `FilesApiError.code`, else `"request failed"`).
The toolbar contains the shared Explorer sidebar toggle, Back and Forward, repository and scope pickers, a Rendered/Source choice for Markdown, a split/single toggle and any error badge. The horizontal fileviewer.outer panel group places the two file trees beside DualPane.

### Conventions

Panda `css`/`cva` from `../../../styled-system/css` (relative import; no path alias). React Aria `Select`
owns dropdown behaviour, Panda owns looks; `react-resizable-panels` owns the split (sizes persisted by
`autoSaveId`). Each `FileTree` is given `key={`${repo}:${scope}:side`}` so a repo/scope change **remounts**
the tree (a clean re-root). `data-testid="file-viewer"`.

### Invariants And Boundaries

File reads and pairing remain read-only over the L1 files API. The page additionally publishes its shown repository for tray routing; this is no file or task mutation. The page’s selection/pairing state remains component-owned. The alive flag prevents repository-catalog state updates after effect cleanup. Bidirectional pairing is the load-bearing contract: forward derives a
sidecar, reverse opens a partner code file or renders a partnerless overview's own markdown (placeholder
only when the body is unavailable). Split/single mode is persisted outside history entries; a code entry keeps its own Rendered/Source choice. The page is kept mounted (hidden) by `Cockpit` across tab
switches and is full-bleed (drops the rails), like the Engine Room / Topology / Chats views.

`useSidebar("files", "left")` remembers Explorer visibility separately from the split/single flag. Shared hidden panel and handle props keep both trees mounted while removing the sidebar from layout and keyboard reach. The toolbar toggle remains outside it. While active, `usePublishPageRepository("File Viewer", repo || null, active)` names this page’s repository for taskless tray messages. DualPane receives the same repository and combines it with the selected file’s scope/path for its line gutter.

New repository Markdown entries start rendered. The header offers Rendered and Source for the current Markdown entry. Back and Forward restore the selected entry and its saved scroll position, including zero. A first-arrival heading anchor is used only when no position is saved. Opening a file after Back discards the forward branch. Old text bodies can be released over the 8 MiB UTF-8 body budget without removing navigable entries; the current body stays retained and released entries reload when revisited.

## Evidence

### Repo-Internal References

- The reusable dual-pane this page mounts on the right; supplies its `SidecarView` shape. [1]
- The one tree explorer rendered twice (code + onboarding sides). [2]
- The persisted split/single flag (`localStorage`-backed). [3]


- The files API client — `fetchRepos`/`readFile`/`resolveForward`/`resolveReverse` + types. [4]


- The shell that registers + keeps this view mounted across tab switches. 

- The route overview that governs this page. 

## Current L5I Maintenance

The mounted-but-hidden File Viewer defers its repository-catalog request until its first actual
showing. A settled success or failure is retained across later hide/show cycles, while concurrent
StrictMode effects share the in-flight request instead of multiplying boot reads; the component is
memoized between meaningful `active` transitions.



- The page owns files-left visibility and publishes only its active repository for tray context. Anchor: "const [repo, setRepo] = useState<string>("");" [9]



- The Explorer remains mounted when hidden; its external toggle and code target stay in the page. Anchor: "{/* MIK-R89 v2 rule 8: the explorer's shared toggle, first on the line above it. */}" [10]




- The shell that registers + keeps this view mounted across tab switches. Anchor: `FileViewer` [5]


- Retired at the fifth freeze d59c3493: dashboard/src/cockpit/Cockpit.tsx::CockpitShell - the bytes it recorded now occur 13 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
