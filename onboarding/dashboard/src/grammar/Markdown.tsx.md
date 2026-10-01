# dashboard/src/grammar/Markdown.tsx

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


## 260831-CCR-L23 Requirement-Address Anchors

L23 made `Markdown` requirement-aware. Both the block and inline renderers now
mount a custom `a` component (`requirementAnchor`) that consults
`useTaskRequirementLinks()`:

- an `href` that resolves against the registered requirement listing renders as
  a styled button (`requirement-link`, `title` names the packet path) whose
  click calls the context `open(path)`, so the packet opens in the internal
  artifact reader;
- a `requirements/...` address that is NOT registered renders as a refused
  span (`requirement-link-refused`) — no dead hyperlink;
- every other link (external URLs, section anchors) keeps its normal anchor element.

The renderer stays presentational and memoized: the listing is read from the provider
context mounted by the task reader, never fetched here, and non-requirement links are
untouched.

## Evidence

### Repo-Internal References

- The detail-panel entry delegates the reader surface to its implementation. [1]
- MasterOverview renders the objective through Markdown and composes the section readers. [2]
- MasterSection renders authored body text through Markdown and delegates shared decisions. [3]
- Bullets renders each item through inline Markdown. [4]
- DecisionList renders both decision and rationale through inline Markdown. [5]
- The leaf TaskReader composes TaskReaderSections inside the requirement-link boundary. [6]
