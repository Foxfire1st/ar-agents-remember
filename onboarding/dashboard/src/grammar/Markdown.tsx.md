# dashboard/src/grammar/Markdown.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Markdown.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T02:44+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[grammar/ overview](overview.md)

## Purpose

`Markdown` is the shared markdown-rendering grammar primitive (slice 6g). Task-doc prose — a master's
ordered `sections`, the objective/design blocks, and the folded sub-task content — is GFM markdown
(tables, blockquotes, `**bold**`, `code`, lists, links); before 6g the dashboard had no renderer, so the
task reader showed it raw. `Markdown` renders it (react-markdown + remark-gfm), making `DetailPanel`'s
task reader readable instead of literal.

## Code Commentary

### Logic

`Markdown({ children, inline })` wraps `<ReactMarkdown remarkPlugins={[remarkGfm]}>`. **Block mode**
(default) renders into a `box` styled via Panda **descendant selectors** (`& p`, `& table`, `& code`,
`& blockquote`, `& h1…h4`, …) so every rendered node is themed without hand-wrapping each; a custom
`table` component keeps a real `<table>` but wraps it in a horizontal **scroll box** (`tableScroll`) so a
wide table can't blow out the detail panel (the react-markdown `node` AST prop is stripped before the
props are spread onto the DOM element). **Inline mode** (`inline`) renders into a `<span>` with an
`inlineComponents` map that unwraps the paragraph (`p → fragment`) for one-line list items / decision
cells — no block margins, no `<p>` inside a `<span>`. The component is wrapped in **`React.memo`**:
`children` is a primitive string, so the default shallow compare skips a re-render (and the expensive
remark re-parse) when the body is unchanged.

### Conventions

Panda `css()` from `../../styled-system/css` (relative import, no path alias), like the other grammar
primitives. Theming is descendant-selector-based rather than per-element component overrides, except the
`table` (scroll-box) and inline `p` (unwrap) cases that need structural control.

### Invariants And Boundaries

Presentational + pure: it renders its `children` string with no data fetching and no state. **No raw
HTML** — react-markdown does not render embedded HTML by default, so arbitrary task-doc content is
XSS-safe. The `React.memo` is load-bearing for performance: the projection SSE re-renders `DetailPanel`
~every second, and without memo every section body would re-parse on each tick (scroll jank). A wide
table scrolls **inside** its box; the panel layout is never widened by content.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sole consumer — renders task prose / master sections / bullets / decisions through this. | — | [panels/DetailPanel.tsx](../panels/DetailPanel.tsx) |
| The shared panel chrome it sits beside in the grammar layer. | — | [grammar/Panel.tsx](Panel.tsx) |
| The grammar route overview that governs this primitive. | — | [grammar/overview.md](overview.md) |

## Update History

- 2026-06-21T02:44+02:00 — Created for slice 6g: the shared `Markdown` grammar primitive (react-markdown + remark-gfm; Panda descendant-selector styling; a GFM-table horizontal-scroll box; an `inline` variant that unwraps the paragraph for list/decision cells; `React.memo` so stable bodies aren't re-parsed on projection ticks). Renders no raw HTML (XSS-safe). Verification metadata is a placeholder pinned until closeout stamps the 6g code commit.
