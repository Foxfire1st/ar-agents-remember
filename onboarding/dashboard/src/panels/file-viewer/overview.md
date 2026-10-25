# dashboard/src/panels/file-viewer/ — File Viewer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/file-viewer/`              |

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`file-viewer/` implements the **File Viewer** centre tab: a general-purpose, read-only browser for code and paired onboarding across repositories, mainline scopes and worktree enclosures. It consumes `GET /api/files/{repos,list,read,onboarding}`, registered by `serving/files.py`, and supplies reusable code-pane primitives also used by the Change-Set Viewer and Knowledge reader.

The shell keeps this full-bleed view mounted and hides it across tab switches. Repository and scope selection, the open file and expanded trees therefore survive a switch.

## Hot Path Summary

First active showing → repository catalog → repository/scope selectors → shared code and onboarding explorers → code read and bidirectional pairing → read-only code plus onboarding markdown. Partnerless readable onboarding fills the pane; the effects-gated siege-tank backdrop fills it before selection. The mounted view retains its state across tab switches.

## Route Model

- [`FileViewer.tsx`](FileViewer.tsx.md) owns the page and its component state. React Aria `Select` controls choose the repository and mainline/enclosure scope from the repository catalog. Two trees browse code and onboarding; `DualPane` displays the selection. Opening a code file reads it and resolves its onboarding forward. Opening an existing file sidecar resolves its code partner and follows the same code-opening path. A partnerless onboarding document whose reverse result carries a readable body displays its own markdown full-pane; a result without that body displays an overview placeholder. Changing repository or scope clears the open code and onboarding. Split/single mode persists across file switches and reloads through `usePersistedFlag`.
- [`FileTree.tsx`](FileTree.tsx.md) adapts the shared [`grammar/ExplorerTree.tsx`](../../grammar/ExplorerTree.tsx.md). It supplies the requested side of `/api/files/list`, path-based row identity, `onOpen`, and the code side's “has onboarding” marker. The shared tree owns asynchronous loading, keyboard navigation, selection and expansion; the Knowledge reader uses the same explorer.
- [`DualPane.tsx`](DualPane.tsx.md) shows code alone in single mode or code on the left and onboarding on the right in split mode, with sizes persisted by `react-resizable-panels`. The onboarding side reuses `grammar/Markdown`. Before any file is opened, `EmptyStateBackdrop` fills the pane with an effects-gated siege-tank boomerang video (`/assets/sc2-siege-tank-boomerang.mp4`, opacity `0.18`). Markdown without a code partner fills the pane in either view mode. Binary code, missing onboarding and overview results without a body use placeholders within the pane layout.
- [`FilePane.tsx`](FilePane.tsx.md) is the reusable read-only, non-editable CodeMirror 6 pane. It wraps lines, loads the language extension asynchronously and applies the shared podracer theme. Optional `firstLine` defaults to 1; optional `fit` uses an uncapped content-sized editor with visible scroller overflow for the review reading column. Optional `highlightedLines` decorates the cited file-line range with `cm-citedLine` and scrolls its first line into view. The Knowledge reader passes this range when its locator resolves. The Change-Set Viewer uses `FilePane` for plain code and its own `changeset/DiffPane.tsx` for merge rendering with the same numbering, language and theme primitives.
- [`lineNumbering.ts`](lineNumbering.ts.md) exports `numberedFrom(first)`: ordinary `lineNumbers()` for line 1, otherwise a gutter offset to the excerpt's file-line numbers. `FilePane` and `changeset/DiffPane.tsx` share it.
- [`markGutter.tsx`](markGutter.tsx.md) supplies optional marks through `useMarkedPane(marks)`: React portals into owned hosts, a gutter per editor, a `placement` key and the `drawn` callback. The key includes each mark's id, side, line, label and compact text, so changes to those values can rebuild the pane. `FilePane` inserts the “all” gutter before its numbered gutter, calls `drawn` after construction and at teardown, and renders the portals beside its host. `DiffPane` supplies the gutter for each editor side. [`markGutter.test.tsx`](markGutter.test.tsx.md) contains cases for marked collapsed runs, focus across gutter redraws and the bounded reveal hold; this description does not report test execution.
- [`codemirrorTheme.ts`](codemirrorTheme.ts.md) maps the podracer CSS variables onto editor chrome through `EditorView.theme` and syntax tokens through `HighlightStyle`.
- [`langByExtension.ts`](langByExtension.ts.md) maps the API's language id to lazily imported JavaScript, TypeScript, JSX, TSX, Python, JSON, CSS, HTML or Markdown support. Other ids return no language extension and render as plain text; `DualPane` intercepts binary code with a placeholder.
- [`usePersistedFlag.ts`](usePersistedFlag.ts.md) provides a `localStorage`-backed boolean state hook for view-mode persistence. Its numeric sibling, `usePersistedNumber`, persists the Cockpit rails' pixel widths.

FileViewer's shared `files` left-sidebar state remembers Explorer visibility independently of split/single mode. Its toolbar toggle stays outside the Explorer panel; hidden panel and handle props leave both trees mounted. While the page is active it publishes the selected repository for tray-message routing to a chat without a task, and passes that repository into DualPane. File and onboarding reads remain read-only; the page also publishes shared tray context.

## Invariants And Boundaries

The File Viewer reads through the existing files API and owns its component state rather than mutating the dashboard store. Its code editor sets both read-only and non-editable extensions. Panda CSS styles the view, and React Aria supplies selector behaviour. The empty-state video is gated by the effects setting and reduced-motion preference. The inherited GSAP/Motion-only, no-CSS-animation intent is not withdrawn here; the reused DualPane currently has a CSS background transition, a source discrepancy rather than proof that the policy was retired.

The shell hides the mounted File Viewer on other tabs and hides the rails for this full-bleed view, as it does for Engine Room, Topology and Chats. The repository-catalog effect waits for the first active showing. A completed success or failure settles that attempt for the component lifetime, so later visibility changes do not reread the catalog. Concurrent catalog reads share an in-flight promise, including during development effect replay; the shared slot clears on settlement.

Marks use the pane's own file-line numbering; the caller chooses each mark's line and side. An empty marks list supplies no marks gutter. Once editors are drawn, the marks gutter is exposed to assistive technology while the other gutter columns remain hidden, and an unchanged collapsed run containing a mark is expanded, including its counterpart in a side-by-side diff. A returned-to mark is scrolled into view and its button focused when drawn. The subsequent hold uses passive pointer, key and wheel listeners and ends on those reader actions, focus moved elsewhere, pane teardown or the 45-frame cap. At widths up to `40rem`, gutter sizing uses the marks' compact text, or their labels when compact text is absent.

The File Viewer's DualPane also supplies a tray target from its repository and the read file's scope/path. FilePane adds the line gutter only when all three target values exist; callers such as Knowledge and review excerpts omit it. Excerpt sizing, intent marks and citation highlighting remain separate optional facilities.

## Evidence

- The marks gutter a pane hosts: portals, placement, the gutter per editor and `drawn`. [1]
- The bounded, passive hold released by the reader's pointer, key or wheel. [2]

- The code pane's optional marks. [3]

- The excerpt gutter. [4]

- The code pane's optional first line and content-sized host. [5]

- The L1 read-only files API this view consumes. [6]
- The same-origin client wrapping that API. [7]

- The shell registers and keeps the file view mounted. [8]



- The markdown renderer the sidecar pane reuses. [9]


- Fitted excerpts grow without an internal maximum-height scrolling box. [10]
- Only a fully specified tray file target installs the line-pick gutter. [11]
- DualPane passes the File Viewer repository and each file scope/path into the code pane. [12]
- File Viewer owns independent Explorer visibility and active repository tray context. [13]
- The toolbar control remains outside the mounted hidden Explorer panel and handle. [14]
