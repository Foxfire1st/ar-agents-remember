# dashboard/src/panels/changeset/ChangeSetPane.tsx

| Field                  | Value                                              |
| ---------------------- | -------------------------------------------------- |
| repository             | agents-remember                                    |
| path                   | `dashboard/src/panels/changeset/ChangeSetPane.tsx` |
| doc_type               | `file-level-onboarding`                            |
| lastUpdated            | 2026-09-30T20:14:26+02:00                             |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`         |
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
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
| The markdown renderer reused for the rendered-markdown view. | `Markdown` | dashboard/src/grammar/Markdown.tsx:109-159 |
| Otherwise it mounts the DiffPane with mode/collapse. | "export function DiffPane({" | dashboard/src/panels/changeset/DiffPane.tsx:123-193 |
| The localStorage-backed flag hook it reuses (per-column keyPrefix). | `usePersistedFlag` | dashboard/src/panels/file-viewer/usePersistedFlag.ts:6-25 |
| The plain read-only pane reused for highlight-off / full-file-plain. | `FilePane` | dashboard/src/panels/file-viewer/FilePane.tsx:25-78 |
| The `FileDiff` shape it renders. | `FileDiff` | dashboard/src/data/changeset.ts:51-58 |
| The screen that mounts it for the file + partner columns. | `ChangeSetViewer` |dashboard/src/panels/changeset/ChangeSetViewer.tsx:645-725|

## Update History
- 2026-09-30T20:14:26+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): No content impact: `DiffPane.tsx` gained an optional `marks` prop and its two view builders were extracted (MIK-R34), so the `DiffPane` row was re-pointed by the generated repair above (`48-118` → `123-193`) and reopened as a changed construct bound by that bullet. Its claim was re-read and holds (this pane passes no `marks`, so the diff is the landed one); it is retained and re-anchored on the line-exact declaration `"export function DiffPane({"`. The generated bullet is kept. The fixer also normalised the `FilePane` row (`20-50` → `25-78`) and, in a file this leaf did not change, the `Markdown` row (`98-121` → `109-159`). No stamp advanced.
- 2026-09-30T18:04:53+00:00: Generated citation repair: `DiffPane` repointed to dashboard/src/panels/changeset/DiffPane.tsx:123-193. No content impact: mechanical anchor-range projection bound to citation source snapshot dd511ab0f1e150e6e017fdffb93a370d587225cb8c691b071ace179d457746ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `FileDiff` repointed to dashboard/src/data/changeset.ts:51-58. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
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
