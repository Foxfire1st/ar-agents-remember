# dashboard/src/grammar/Markdown.tsx

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Markdown` is the shared markdown-rendering grammar primitive (slice 6g). Task-doc prose — a master's
ordered `sections`, the objective/design blocks, and the folded sub-task content — is GFM markdown
(tables, blockquotes, `**bold**`, `code`, lists, links); before 6g the dashboard had no renderer, so the
task reader showed it raw. `Markdown` renders it (react-markdown + remark-gfm), making `DetailPanel`'s
task reader readable instead of literal. MIK-R79 rule 8 uses the same primitive for the Knowledge
reader's document text through two opt-in extensions rather than a second renderer.

## Code Commentary

### Logic

`Markdown({ children, inline, referenceMarkers, headingIds, components })` wraps
`<ReactMarkdown remarkPlugins={plugins}>`. **Block mode** (default) renders into a `box` styled via
Panda **descendant selectors** (`& p`, `& table`, `& code`, `& blockquote`, `& h1…h4`, …) so every
rendered node is themed without hand-wrapping each; a custom `table` component keeps a real `<table>`
but wraps it in a horizontal **scroll box** (`tableScroll`) so a wide table can't blow out the detail
panel. **Inline mode** renders into a `<span>` with an `inlineComponents` map that unwraps the
paragraph (`p → fragment`) for one-line list items and decision cells. The component is wrapped in
**`React.memo`**: `children` is a primitive string, so the default shallow compare skips a re-render
(and the expensive remark re-parse) when the body is unchanged.

**MIK-R79 opt-ins.** `referenceMarkers` adds `remarkReferenceMarkers` so the prose's `[n]` markers
link to the document's reference list. `headingIds` adds `remarkHeadingIds` and switches the box to
`data-document-headings=true`, which gives h1..h6 document typography (a chapter and a sub-chapter
look different) instead of the task-doc heading scale. `components` lets a caller (the Knowledge
reader) extend the component map. The requirement-link `a` component is the **no-override default**:
it wraps every anchor only while the caller supplies no `a` override, because a caller's components are
spread last. The Knowledge reader supplies its own `a` handler, so requirement handling is not composed
there.

### Conventions

Panda `css()` from `../../styled-system/css` (relative import), like the other grammar primitives.
Theming is descendant-selector-based rather than per-element component overrides, except the `table`
(scroll-box), inline `p` (unwrap) and the opt-in document-heading block cases that need structural
control.

### Invariants And Boundaries

Presentational and pure: it renders its `children` string with no data fetching and no state. **No raw
HTML** — react-markdown does not render embedded HTML by default, so arbitrary task-doc content is
XSS-safe. The `React.memo` is load-bearing for performance: the projection SSE re-renders `DetailPanel`
about every second, and without memo every section body would re-parse on each tick. A wide table
scrolls **inside** its box; the panel layout is never widened by content. The MIK-R79 extensions are
opt-in and text-only: with both flags off, rendering (including requirement anchors) is unchanged.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 8); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The renderer mounts its plugins only when the caller asks for markers or heading ids. [7]
- The requirement anchor resolves registered packets and refuses unregistered addresses. [8]
- The document typing used by the Knowledge reader is one opt-in block. [9]
- The marker and heading plugins the Knowledge reader opts into. [10]
- The reader's document text renders through this primitive. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
