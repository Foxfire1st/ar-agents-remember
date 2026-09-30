# dashboard/src/panels/file-viewer/lineNumbering.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/file-viewer/lineNumbering.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T09:59:20+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/file-viewer/overview.md` |

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

**One CodeMirror gutter that keeps a file's own line numbers when the document is an excerpt (MIK-R31).** The
reviewer's focused expression cards show one region of a file, and its gutter must read the file's lines, not the
excerpt's. `numberedFrom(first)` returns the plain `lineNumbers()` extension for `first = 1` (exactly the gutter the
two panes used before) and otherwise a `lineNumbers` whose `formatNumber` adds `first - 1`.

## Code Commentary

### Logic

- `FilePane` passes its `firstLine` prop (default 1); `DiffPane` passes each side's own first line, so the before
  editor of a split diff numbers from the before range's start and the after editor from the after range's start.

### Conventions

- The default path is byte-for-byte the old extension, so every existing caller renders as before.

### Invariants And Boundaries

- Presentation only: it changes which number is printed beside a line, never the text.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured; CodeMirror's `lineNumbers` option `formatNumber` is the only external
API used, and its behaviour is exercised by the mounted card cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The gutter: plain for line 1, offset otherwise. | "export function numberedFrom(first = 1): Extension {" | dashboard/src/panels/file-viewer/lineNumbering.ts:7-11 |
| The file pane's use, through its optional first line. | "numberedFrom(firstLine)," | dashboard/src/panels/file-viewer/FilePane.tsx:47-47 |
| The diff pane's use, one first line per side. | "numberedFrom(beforeFirst)"; "numberedFrom(afterFirst)" | dashboard/src/panels/changeset/DiffPane.tsx:102-102; dashboard/src/panels/changeset/DiffPane.tsx:107-107 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T09:59:20+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): created this card for the new helper MIK-R31 adds. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
