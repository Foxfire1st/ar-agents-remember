# dashboard/src/panels/file-viewer/DualPane.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`DualPane` is the reusable two-pane body on the right of the File Viewer: **single** (code only) or
**split** (code LEFT, sidecar RIGHT). The Markdown sidecar uses grammar/Markdown. The code side uses the shared FilePane for source text, MediaView for recognized media, or Markdown with a DocumentContext for rendered repository documents. Before anything is opened (`empty`) the whole
pane is filled by a faint, effects-gated **siege-tank boomerang backdrop** (`EmptyStateBackdrop`,
`/assets/sc2-siege-tank-boomerang.mp4`) instead of per-side "select a file" placeholders. A **partnerless
overview** (markdown with no code) renders its markdown **full-pane** so a route overview is readable even
in single mode. A missing partner, an overview without a body and unsupported binary content use placeholders that occupy the pane. Split sizes persist via
`react-resizable-panels`. The Change-Set Viewer shares the column layout pattern and FilePane, while composing its own ChangeSetPane.

## Code Commentary

### Logic

Exports the **`SidecarView`** discriminated union (`markdown{body}` | `missing` | `overview` | `empty`) —
what the right pane shows, derived by `FileViewer` from L1 pairing. `CodeSide` shows a selection placeholder when code is absent, `MediaView` when mediaType is recognized, and a byte-count placeholder for other binary content. Rendered repository Markdown uses the document renderer and retains its truncation banner. Source text uses `FilePane(content, language, trayLines)`; trayLines is supplied only when a repository exists, using that repository and the read file’s own scope/path. `SidecarSide({sidecar})` switches on the state: `markdown` renders
`<Markdown>` inside a scroll box, while `overview` / `missing` / `empty` each render their own placeholder.
`DualPane({code, sidecar, split, repository?})` checks two whole-pane branches before the split: (1) `code === null &&
sidecar.state === "empty"` renders an `EmptyStateBackdrop src="/assets/sc2-siege-tank-boomerang.mp4"
opacity={0.18}` (a brighter wash than the shared 0.14 default because the siege-tank clip reads darker);
(2) `overviewOnly = code === null && sidecar.state === "markdown"` — a partnerless overview. When
`!split || overviewOnly` it renders a single fill div containing `overviewOnly ? <SidecarSide> :
<CodeSide>` (so an overview opened from the onboarding tree shows its markdown full-pane even in single
mode, where the sidecar side is otherwise never shown). Otherwise a horizontal `PanelGroup` (`autoSaveId
"fileviewer.dualpane"`) with `CodeSide` (`defaultSize 62`) | a resize handle | `SidecarSide`
(`defaultSize 38`).

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). `Panel`/`PanelGroup`/`PanelResizeHandle`
from `react-resizable-panels`. Test hooks: `data-testid` `dual-pane`, `sidecar-pane`, `pane-placeholder`.
The sidecar pane is markdown via `grammar/Markdown`, never CodeMirror.

### Invariants And Boundaries

DualPane receives content and pairing from its caller and does no JSON file read or pairing itself. Its Markdown and media children can resolve references or load supplied byte addresses. The `empty` backdrop is pure atmosphere (`aria-hidden`, effects-gated by
`useShouldAnimate` — absent under calm-cockpit / `prefers-reduced-motion`, leaving just the prompt text).
Placeholders use a centered grid with the full pane height. Recognized media is dispatched before the binary placeholder; binary content is not passed to CodeMirror. Text and rendered-document modes retain the truncation banner. Split sizes persist (`autoSaveId`). The Change-Set Viewer composes its own diff columns using shared FilePane and presentation flags.

Without `repository`, CodeSide supplies no tray target. DualPane performs no JSON read, pairing or tray submission itself; its shared children render supplied document and media addresses.

## Evidence

### Repo-Internal References


- The read-only CodeMirror pane it hosts on the code side. [1]





- The markdown renderer the sidecar pane reuses. Anchor: `Markdown` [2]


- The effects-gated boomerang backdrop the `empty` state fills the pane with. [3]


- The `FileContent` type / onboarding pairing it renders. [5]




- For source text, CodeSide combines the File Viewer repository with the read file scope and path for FilePane's optional tray gutter. Picture and video content takes the media branch instead. [6]



- FileViewer passes repository and paired view state into DualPane. Anchor: "export const FileViewer = memo(FileViewerImpl);" [4]
