# dashboard/src/panels/changeset/ChangeSetPane.test.tsx

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `dashboard/src/panels/changeset/ChangeSetPane.test.tsx`   |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-06-30                                                |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                             |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Mocks the CodeMirror panes so jsdom renders the markdown path only. | "ChangeSetPane markdown rendered view" | dashboard/src/panels/changeset/ChangeSetPane.test.tsx:33-61 |
| Markdown diff fixture + per-case localStorage reset. | `mdDiff` | dashboard/src/panels/changeset/ChangeSetPane.test.tsx:16-26 |
| Rendered toggle swaps the diff for the `<Markdown>` prose view. | "offers a 'rendered' toggle for markdown that draws the after-content as prose" | dashboard/src/panels/changeset/ChangeSetPane.test.tsx:34-49 |
| Non-markdown files do not offer the rendered toggle. | "does not offer the rendered toggle for non-markdown files" | dashboard/src/panels/changeset/ChangeSetPane.test.tsx:51-60 |
| Subject under test: the diff column + its rendered-markdown toggle. | `ChangeSetPane` | dashboard/src/panels/changeset/ChangeSetPane.tsx:177-218 |
| The markdown renderer the rendered view mounts. | `Markdown` | dashboard/src/grammar/Markdown.tsx:98-121 |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 12 citation findings; scoped check passed.

- 2026-06-30T00:00:00+02:00 — Created for operations-integration L5 (diff-viewer polish): vitest/jsdom test for
  `ChangeSetPane`'s markdown **"rendered" toggle** — mocks the CodeMirror `DiffPane`/`FilePane`, then
  pins that a markdown diff offers `changeset-rendered-toggle` (swapping the raw diff for the
  `changeset-rendered` `<Markdown>` prose view) while a non-markdown diff does not. Verification metadata
  pinned to the task base until closeout stamps the L5 commit.
