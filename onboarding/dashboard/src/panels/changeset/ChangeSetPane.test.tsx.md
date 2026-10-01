# dashboard/src/panels/changeset/ChangeSetPane.test.tsx

## Governing Overview

[changeset/ overview](overview.md)

## Purpose

Vitest/jsdom test for `ChangeSetPane`'s **markdown "rendered" toggle** (slice L5). It mocks the
CodeMirror primitives (`DiffPane` / `FilePane`) so the pane renders in jsdom without building a real
`MergeView`/editor — this test is about the rendered-markdown mode, which uses `react-markdown`
(jsdom-safe) instead — and pins that markdown files offer a `changeset-rendered-toggle` that swaps the
raw diff for a formatted `<Markdown>` view, while non-markdown files do not.

## Code Commentary

### Logic

`vi.mock("./DiffPane")` and `vi.mock("../file-viewer/FilePane")` replace each with a stub div
(`data-testid="diff-pane"` / `file-pane`) echoing its `after`/`content`, keeping CodeMirror out of jsdom.
A `mdDiff(over?)` helper builds a `FileDiff` defaulting to `language: "markdown"` with `before`/`after`
prose. `afterEach` cleans up AND clears `window.localStorage` (the `rendered`/diff toggles persist
per-column via `usePersistedFlag`, so each case must start fresh). Cases:

- **markdown rendered toggle** — renders `<ChangeSetPane diff={mdDiff()} keyPrefix="t.main" />`; the
  default view is the (stubbed) `diff-pane` and `changeset-rendered` is absent. Clicking
  `changeset-rendered-toggle` replaces the diff with the `changeset-rendered` surface whose text
  contains the after-content prose ("Heading", "Readable onboarding prose."), and `diff-pane` is gone.
- **non-markdown has no toggle** — a `code`/`typescript` diff renders `diff-pane` but **no**
  `changeset-rendered-toggle` (the rendered mode is offered only when `diff.language === "markdown"`).

### Invariants And Boundaries

Pure unit test: the CodeMirror panes are mocked, `localStorage` is cleared per case so the persisted
toggle state never leaks between tests. It pins the markdown-only rendered toggle and the rendered ↔ diff
swap — not the live `<Markdown>` styling or the CodeMirror diff (both covered elsewhere / by build).

## Evidence

### Repo-Internal References

- Mocks the CodeMirror panes so jsdom renders the markdown path only. [1]
- Markdown diff fixture + per-case localStorage reset. [2]
- Rendered toggle swaps the diff for the `<Markdown>` prose view. [3]
- Non-markdown files do not offer the rendered toggle. [4]
- Subject under test: the diff column + its rendered-markdown toggle. [5]
- The markdown renderer the rendered view mounts. [6]
