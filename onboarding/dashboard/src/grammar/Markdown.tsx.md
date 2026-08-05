# dashboard/src/grammar/Markdown.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Markdown.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-21T02:44+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| `DetailPanel` renders task prose, master sections, bullets, and decisions through this primitive. | `DetailPanel`; `MasterSection`; `Bullets`; `DecisionList`; `MasterOverview`; `TaskReader` | dashboard/src/panels/DetailPanel.tsx:723-723; dashboard/src/panels/DetailPanel.tsx:1036-1104; dashboard/src/panels/DetailPanel.tsx:1116-1144; dashboard/src/panels/DetailPanel.tsx:1303-1388; dashboard/src/panels/DetailPanel.tsx:1415-1425; dashboard/src/panels/DetailPanel.tsx:1476-1491 |

## Update History

- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: bound task prose, master sections, bullets, and decisions to their operative `DetailPanel` consumers. Verification metadata unchanged.

- 2026-06-21T02:44+02:00 — Created for slice 6g: the shared `Markdown` grammar primitive (react-markdown + remark-gfm; Panda descendant-selector styling; a GFM-table horizontal-scroll box; an `inline` variant that unwraps the paragraph for list/decision cells; `React.memo` so stable bodies aren't re-parsed on projection ticks). Renders no raw HTML (XSS-safe). Verification metadata is a placeholder pinned until closeout stamps the 6g code commit.
