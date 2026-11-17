# dashboard/src/panels/changeset/ChangeSetPane.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

`ChangeSetPane` is **one diff column** of the Change-Set Viewer: a toolbar of persisted toggles over a `DiffPane` (or a plain `FilePane`) for nonbinary text; binary/media sides use `MediaDiff`. It maps the task doc's three view states onto two persisted flags so
the choice survives a file switch and a reload. For nonbinary Markdown files, a rendered toggle swaps the raw diff for the shared Markdown view. The Change-Set Viewer mounts
one for the selected file (column 2) and a second for the code↔sidecar partner (column 3), each with its
own flag namespace.

`ChangeSetPane` renders one open file of the change-set viewer: a toolbar of persisted toggles over a `DiffPane` / `FilePane` for nonbinary text, or a before/after `MediaDiff` for binary/media sides. For a text diff it presents the collapsed change-set diff by default, the whole file with changes still marked, or the plain file, and flips split/inline for whichever diff is shown. On a narrow comparison viewport it defaults to inline through a session-only flag instead of the persisted one.
## Code Commentary

### Logic

Props are `{ diff: FileDiff, keyPrefix: string, narrow?: boolean, mediaSelector?: ChangeSetMediaSelector }`, with `narrow=false`. Four persisted flags use `${keyPrefix}.{fullfile,inline,highlight,rendered}`; `narrow` selects the session-only inline flag (initially true), leaving the persisted inline preference untouched.
diffContent supplies each side's content, or an empty string for an absent text value. `isMarkdown = diff.language === "markdown"` and `showRendered = isMarkdown && rendered && !binaryDiff` gate the **rendered-markdown** mode: when on, the body is a scrollable, padded `mdScroll` surface (`data-testid="changeset-rendered"`) holding `<Markdown>{after || before}</Markdown>` (after-content, falling back to the removed prose on a pure deletion so the pane is never blank), and the diff toggles are hidden — only the `rendered` toggle (`changeset-rendered-toggle`, shown only for nonbinary markdown) remains. For nonbinary text when **not** rendered: the derived `plain = fullFile && !highlight` is the **highlight-off** state, rendering the plain L2 `<FilePane content={after} language={diff.language} />` (no diff highlighter at all); otherwise `<DiffPane before after language mode={inline ? "inline" : "split"} collapse={!fullFile} />` — so change-set view collapses unchanged regions and full-file view shows everything. The toolbar is React Aria `ToggleButton`s: the `rendered` toggle only for nonbinary markdown; the rest (full-file⇄change-set always; split⇄inline only while a diff is shown, `!plain`; highlight on/off only in full-file) only for nonbinary text while **not** showing the rendered view. A right-aligned label shows
`{diff.kind} · {diff.path}`.

### Conventions

Panda `css`/`cx`; React Aria `ToggleButton` (`data-selected` mirrored for Panda conditions + tests).
Reuses `usePersistedFlag` + `FilePane` from the sibling File Viewer route; `DiffPane` from this route;
and `grammar/Markdown` for the rendered-markdown view. `data-testid`s: `changeset-pane`,
`changeset-rendered-toggle`, `changeset-rendered`.

### Invariants And Boundaries

Read-only/presentational — it only chooses how to render an already-fetched `FileDiff`; no JSON fetching or range selection, and no store mutation. Its media child requests the supplied bytes URL. For nonbinary text the diff states are `change-set` (collapsed diff), `full-file + highlight` (uncollapsed diff), `full-file + highlight-off` (plain `FilePane`); nonbinary markdown files add a `rendered` state (formatted `<Markdown>` prose instead of the text diff), offered when `diff.language === "markdown"`. There is no editable/accept
path. The per-column `keyPrefix` keeps the code column and the sidecar column's toggles (including
`rendered`) independent and persisted across file switches.

## Evidence

### Repo-Internal References




- Four per-column persisted flags control text change-set/full-file layout, inline presentation, highlighting and rendered Markdown. Media or binary sides bypass the text-diff controls. [1]





- For a text diff in full-file mode, disabling highlighting renders the plain FilePane with the after-content. Media and binary diffs use their own side rendering. [2]


- Nonbinary Markdown files get a rendered toggle that swaps the diff for rendered after-content. [3]
- The markdown renderer reused for the rendered-markdown view. Anchor: `Markdown` [4]



- For nonbinary text in diff mode, DiffPane supplies mode and collapse controls. [5]
- The localStorage-backed flag hook it reuses (per-column keyPrefix). [6]

- The plain read-only pane reused for highlight-off / full-file-plain. [7]




- The FileDiff contract carries before and after sides; each side can contain text or binary/media metadata, and an added or deleted side is null. [8]





- The screen that mounts it for the file + partner columns. Anchor: `ChangeSetViewer` [9]




- One diff column with per-column persisted flags [10]

- Narrow comparisons default to inline without touching the persisted flag [11]


- Markdown text files offer a persisted rendered-prose mode; media or binary diffs do not use that toggle. [12]
