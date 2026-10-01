# dashboard/src/panels/changeset/ChangeSetPane.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetPane` is **one diff column** of the Change-Set Viewer: a toolbar of persisted toggles over a
`DiffPane` (or a plain `FilePane`). It maps the task doc's three view states onto two persisted flags so
the choice survives a file switch and a reload. For **markdown** files it additionally offers a
**"rendered"** toggle that swaps the raw diff for a formatted `<Markdown>` view — so a changed
onboarding doc reads exactly as nicely here as it does in the file reader. The Change-Set Viewer mounts
one for the selected file (column 2) and a second for the code↔sidecar partner (column 3), each with its
own flag namespace.

## Code Commentary

### Logic

Props are `{ diff: FileDiff, keyPrefix: string }`. Four `usePersistedFlag` toggles keyed by
`${keyPrefix}.{fullfile,inline,highlight,rendered}`. `before`/`after` come from `diff.before?.content` /
`diff.after?.content` (`?? ""`). `isMarkdown = diff.language === "markdown"` and `showRendered =
isMarkdown && rendered` gate the **rendered-markdown** mode: when on, the body is a scrollable, padded
`mdScroll` surface (`data-testid="changeset-rendered"`) holding `<Markdown>{after || before}</Markdown>`
(after-content, falling back to the removed prose on a pure deletion so the pane is never blank), and the
diff toggles are hidden — only the `rendered` toggle (`changeset-rendered-toggle`, shown only for
markdown) remains. When **not** rendered: the derived `plain = fullFile && !highlight` is the
**highlight-off** state, rendering the plain L2 `<FilePane content={after} language={diff.language} />`
(no diff highlighter at all); otherwise `<DiffPane before after language mode={inline ? "inline" :
"split"} collapse={!fullFile} />` — so change-set view collapses unchanged regions and full-file view
shows everything. The toolbar is React Aria `ToggleButton`s: the `rendered` toggle only for markdown;
the rest (full-file⇄change-set always; split⇄inline only while a diff is shown, `!plain`; highlight
on/off only in full-file) only while **not** showing the rendered view. A right-aligned label shows
`{diff.kind} · {diff.path}`.

### Conventions

Panda `css`/`cx`; React Aria `ToggleButton` (`data-selected` mirrored for Panda conditions + tests).
Reuses `usePersistedFlag` + `FilePane` from the sibling File Viewer route; `DiffPane` from this route;
and `grammar/Markdown` for the rendered-markdown view. `data-testid`s: `changeset-pane`,
`changeset-rendered-toggle`, `changeset-rendered`.

### Invariants And Boundaries

Read-only/presentational — it only chooses how to render an already-fetched `FileDiff`; no fetching, no
store mutation. The diff states are exactly `change-set` (collapsed diff), `full-file + highlight`
(uncollapsed diff), `full-file + highlight-off` (plain `FilePane`); markdown files add a `rendered`
state (formatted `<Markdown>` prose instead of the text diff), which is the only state available to
non-diff content and is offered solely when `diff.language === "markdown"`. There is no editable/accept
path. The per-column `keyPrefix` keeps the code column and the sidecar column's toggles (including
`rendered`) independent and persisted across file switches.

## Evidence

### Repo-Internal References

- Four persisted toggles map onto the change-set / full-file / highlight-off / rendered states. [1]
- Highlight-off renders the plain L2 FilePane on the after-content. [2]
- Markdown files get a `rendered` toggle that swaps the diff for a `<Markdown>` view. [3]
- The markdown renderer reused for the rendered-markdown view. [4]
- Otherwise it mounts the DiffPane with mode/collapse. [5]
- The localStorage-backed flag hook it reuses (per-column keyPrefix). [6]
- The plain read-only pane reused for highlight-off / full-file-plain. [7]
- The `FileDiff` shape it renders. [8]
- The screen that mounts it for the file + partner columns. [9]
