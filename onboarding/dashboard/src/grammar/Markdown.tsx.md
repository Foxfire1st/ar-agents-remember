# dashboard/src/grammar/Markdown.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/grammar/Markdown.tsx`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `DetailPanel` renders task prose, master sections, bullets, and decisions through this primitive. | "export const DetailPanel = memo(DetailPanelImpl);"; "export function MasterOverview({"; "export function MasterSection({"; "export function Bullets({ items }: { items: string[] }) {"; "export function DecisionList({ items }: { items: TaskDecisionNode[] }) {"; "export function TaskReader({" | dashboard/src/panels/detail-panel/DetailPanel.tsx:75-75; dashboard/src/panels/detail-panel/taskReader.tsx:167-167; dashboard/src/panels/detail-panel/taskReader.tsx:264-264; dashboard/src/panels/detail-panel/taskReader.tsx:614-614; dashboard/src/panels/detail-panel/taskReader.tsx:675-675; dashboard/src/panels/detail-panel/taskReader.tsx:745-745 |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the requirement-address anchor handling — registered `requirements/...` links render as opening buttons via `useTaskRequirementLinks`, unregistered requirement addresses render as refused spans, and external/anchor links are untouched; applies to block and inline variants.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: bound task prose, master sections, bullets, and decisions to their operative `DetailPanel` consumers. Verification metadata unchanged.

- 2026-06-21T02:44+02:00 — Created for slice 6g: the shared `Markdown` grammar primitive (react-markdown + remark-gfm; Panda descendant-selector styling; a GFM-table horizontal-scroll box; an `inline` variant that unwraps the paragraph for list/decision cells; `React.memo` so stable bodies aren't re-parsed on projection ticks). Renders no raw HTML (XSS-safe). Verification metadata is a placeholder pinned until closeout stamps the 6g code commit.
