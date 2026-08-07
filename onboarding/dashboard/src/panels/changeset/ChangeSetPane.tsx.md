# dashboard/src/panels/changeset/ChangeSetPane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/changeset/ChangeSetPane.tsx` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-06-29T16:40+02:00                             |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`         |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                      |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Four persisted toggles map onto the change-set / full-file / highlight-off / rendered states. | `ChangeSetPane` | dashboard/src/panels/changeset/ChangeSetPane.tsx:177-218 |
| Highlight-off renders the plain L2 FilePane on the after-content. | `ChangeSetPane` | dashboard/src/panels/changeset/ChangeSetPane.tsx:177-218 |
| Markdown files get a `rendered` toggle that swaps the diff for a `<Markdown>` view. | "data-testid=\"changeset-rendered-toggle\"" | dashboard/src/panels/changeset/ChangeSetPane.tsx:47-47; dashboard/src/panels/changeset/ChangeSetPane.tsx:86-86 |
| The markdown renderer reused for the rendered-markdown view. | `Markdown` | dashboard/src/grammar/Markdown.tsx:98-121 |
| Otherwise it mounts the DiffPane with mode/collapse. | `DiffPane` | dashboard/src/panels/changeset/DiffPane.tsx:48-118 |
| The localStorage-backed flag hook it reuses (per-column keyPrefix). | `usePersistedFlag` | dashboard/src/panels/file-viewer/usePersistedFlag.ts:6-25 |
| The plain read-only pane reused for highlight-off / full-file-plain. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:20-50 |
| The `FileDiff` shape it renders. | `FileDiff` | dashboard/src/data/changeset.ts:34-41 |
| The screen that mounts it for the file + partner columns. | `ChangeSetViewer` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:416-478 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:58:18+02:00 — 260731-EFA-L6 curator W2-B10: repaired 14 citation findings (7 reference rows); scoped recheck clean.

- 2026-06-30T00:00:00+02:00 — L5 (diff-viewer polish): added a markdown **"rendered" toggle**. For
  `diff.language === "markdown"` a fourth `usePersistedFlag(`${keyPrefix}.rendered`, false)` drives a
  `changeset-rendered-toggle`; when on (`showRendered`), the body swaps the raw CodeMirror merge diff
  for a scrollable `mdScroll` surface holding `<Markdown>{after || before}</Markdown>` (the
  `changeset-rendered` view), and the diff toggles are hidden — so changed onboarding/markdown docs
  render as formatted prose like the file reader. New import `Markdown`; added references to its source
  and the markdown-toggle logic, and refreshed the now-shifted line citations. Verification metadata
  pinned until closeout stamps the L5 commit.
- 2026-06-29T16:40+02:00 — Created for operations-integration L4 (Change-Set Viewer): one diff column —
  React Aria toggles persisted via `usePersistedFlag` (change-set / full-file / highlight-off + split⇄inline)
  that render `DiffPane` or, for highlight-off, the plain L2 `FilePane`. Verification metadata pinned to
  the task base until closeout stamps the L4 code commit.
