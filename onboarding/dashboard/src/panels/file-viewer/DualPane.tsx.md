# dashboard/src/panels/file-viewer/DualPane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/file-viewer/DualPane.tsx`    |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T09:06+02:00                             |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a`         |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                                      |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`DualPane` is the reusable two-pane body on the right of the File Viewer: **single** (code only) or
**split** (code LEFT, sidecar RIGHT). The markdown sidecar reuses `grammar/Markdown` (deliberately **not**
CodeMirror); the code side hosts the read-only `FilePane`. Before anything is opened (`empty`) the whole
pane is filled by a faint, effects-gated **siege-tank boomerang backdrop** (`EmptyStateBackdrop`,
`/assets/sc2-siege-tank-boomerang.mp4`) instead of per-side "select a file" placeholders. A **partnerless
overview** (markdown with no code) renders its markdown **full-pane** so a route overview is readable even
in single mode. A missing partner, an overview-without-body, or a binary file still renders a
**stable-size placeholder** so the layout never flip-flops between states. Split sizes persist via
`react-resizable-panels`. L4's Change-Set Viewer reuses this same shape.

## Code Commentary

### Logic

Exports the **`SidecarView`** discriminated union (`markdown{body}` | `missing` | `overview` | `empty`) —
what the right pane shows, derived by `FileViewer` from L1 pairing. `CodeSide({code})`: `null` → a
"Select a code file" placeholder; a `binary` language → a "Binary file — N bytes" placeholder; otherwise a
fill column with an optional truncation banner ("Showing the first 2 MiB of N bytes") above a
`FilePane(content, language)`. `SidecarSide({sidecar})` switches on the state: `markdown` renders
`<Markdown>` inside a scroll box, while `overview` / `missing` / `empty` each render their own placeholder.
`DualPane({code, sidecar, split})` checks two whole-pane branches before the split: (1) `code === null &&
sidecar.state === "empty"` renders an `EmptyStateBackdrop src="/assets/sc2-siege-tank-boomerang.mp4"
opacity={0.18}` (a brighter wash than the shared 0.14 default because the siege-tank clip reads darker);
(2) `overviewOnly = code === null && sidecar.state === "markdown"` — a partnerless overview. When
`!split || overviewOnly` it renders a single fill div containing `overviewOnly ? <SidecarSide> :
<CodeSide>` (so an overview opened from the onboarding tree shows its markdown full-pane even in single
mode, where the sidecar side is otherwise never shown). Otherwise a horizontal `PanelGroup` (`autoSaveId
"fileviewer.dualpane"`) with `CodeSide` (`defaultSize 62`) | a resize handle | `SidecarSide`
(`defaultSize 38`). New import: `EmptyStateBackdrop` from `../EmptyStateBackdrop`.

### Conventions

Panda `css` from `../../../styled-system/css` (relative import). `Panel`/`PanelGroup`/`PanelResizeHandle`
from `react-resizable-panels`. Test hooks: `data-testid` `dual-pane`, `sidecar-pane`, `pane-placeholder`.
The sidecar pane is markdown via `grammar/Markdown`, never CodeMirror.

### Invariants And Boundaries

Presentational — it is **told** what to render; it does no fetching or pairing (`FileViewer` derives both
`code` and the `SidecarView`). The `empty` backdrop is pure atmosphere (`aria-hidden`, effects-gated by
`useShouldAnimate` — absent under calm-cockpit / `prefers-reduced-motion`, leaving just the prompt text).
Placeholders are stable-size (centred grid) so toggling split or switching files never flip-flops the
layout. A binary file is **never** fed to CodeMirror (placeholder instead), and
L1's read truncation (2 MiB) is surfaced via the banner. Split sizes persist (`autoSaveId`). The shape is
reused by L4 by swapping the code side for a diff view.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The read-only CodeMirror pane it hosts on the code side. | L20-L50 | [FilePane.tsx](FilePane.tsx) |
| The markdown renderer the sidecar pane reuses. | — | [Markdown.tsx](agents-remember/dashboard/src/grammar/Markdown.tsx) |
| The effects-gated boomerang backdrop the `empty` state fills the pane with. | L51-L83 | [EmptyStateBackdrop.tsx](agents-remember/dashboard/src/panels/EmptyStateBackdrop.tsx) |
| The page that supplies `code` + the derived `SidecarView`. | L222-L251 | [FileViewer.tsx](FileViewer.tsx) |
| The `FileContent` type / onboarding pairing it renders. | L42-L68 | [files.ts](agents-remember/dashboard/src/data/files.ts) |
| The route overview that governs this component. | — | [overview.md](overview.md) |

## Update History

- 2026-06-30T00:00:00+02:00 — operations-integration L5: added two whole-pane branches ahead of the split — an `empty` state that fills the pane with a faint siege-tank `EmptyStateBackdrop` (`/assets/sc2-siege-tank-boomerang.mp4`, `opacity 0.18`) replacing the per-side "select a file" placeholders, and a partnerless-overview (`code===null && state==="markdown"`) that renders its markdown full-pane via `SidecarSide` in both single and split mode. New import: `EmptyStateBackdrop`.
- 2026-06-29T09:06+02:00 — Created for operations-integration L2 (File Viewer): the reusable single|split dual-pane (code left via the read-only `FilePane`, markdown sidecar right via `grammar/Markdown`) with the exported `SidecarView` union, stable-size placeholders for missing/overview/binary, and persisted split sizes; reused by L4. Verification metadata pinned to the task base until closeout stamps the L2 code commit.
