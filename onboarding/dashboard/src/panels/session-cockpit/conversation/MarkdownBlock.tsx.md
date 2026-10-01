# dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

Streaming-safe Markdown (design §12.3): ONE stable memoized component that renders a whole block from a
single markdown string, so token deltas re-render text WITHOUT remounting the DOM (no typewriter
re-mount per token). Prose wraps unbroken tokens within the stage; fenced code lives in its own
labeled, keyboard-scrollable overflow region so a long line never widens the page (§12.2, §14.3).

## Code Commentary

### Logic

- cit:([`MarkdownBlockImpl`], dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:73-84) renders `react-markdown` with `remark-gfm` inside a `prose` container that
  is `tabIndex={-1}` and carries a stable `data-testid` (default `conversation-markdown`, overridable
  via `testId`).
- cit:([`MarkdownBlock`], dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:88-88): re-renders only when the `markdown` string actually
  changes. The reducer mutates the block's string in place per delta, so a stable memo keeps React
  notification batched (§12.3).
- The `prose` recipe (L13) scopes wrapping/typography and puts fenced code (`& pre`) in its own
  `overflow-x: auto` region with `white-space: pre`, and tables in a scrollable block — honest
  overflow that never widens the page.
- **Whole-word wrapping (V10, 260718-CHATS-L5P):** `prose` (and `& a`) use `overflowWrap: break-word`,
  NOT `anywhere` — a token breaks only when it would otherwise overflow, so ordinary prose keeps
  whole-word wrapping (`Be brief.`, not `Be bri/ef.`). Inline `& code` is `whiteSpace: nowrap` — inline
  code is one unbreakable token (`ls` never splits to `l/s`); a pathological inline token is clipped by
  the surface scroller, not wrapped mid-word. NOTE: this fix is only effective because the leaf's
  `index.css` root override neutralizes `@webtui/css`'s inherited `word-break: break-all` (RV-1) — under
  `break-all` the `overflowWrap` value is inert (a break can land between any two chars). See
  [../../../index.css](../../../index.css.md).

### Invariants And Boundaries

- Incomplete fences/tables render best-effort while streaming; completion is one final stable render
  — there is no per-token remount.
- Code/tables scroll inside their own region; the stage body never scrolls horizontally.
- Prose breaks on word boundaries (`break-word`), inline code never breaks (`nowrap`) — but this holds
  only while the app-root `word-break: normal` override (index.css, RV-1) is in place; a component-level
  overflow-wrap patch cannot survive an inherited `break-all`.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Consumed by message/thinking/interaction/tool/result items as the shared prose renderer. [1]
- The house Markdown primitive precedent (react-markdown + remark-gfm, memoized) elsewhere in the cockpit. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
