# dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The per-file diff block of the harness-neutral grammar (design §12.2): full by default up to a logical
source-line threshold, then a summary plus a real disclosure button with an EXACT hidden-line count.
Whitespace is preserved inside a labeled, keyboard-scrollable overflow region so a wide diff never
forces page-level horizontal scroll (§14.3).

## Code Commentary

### Logic

- `body = unified ?? synthesizeUnified(oldText, newText)` (L48): the server's `unified` string is
  preferred; when only old/new text is present, `synthesizeUnified` (L81) prints a MINIMAL labeled
  `- old` / `+ new` pair rather than fabricating hunk headers — honesty over guessed diff math.
- Clamp at `DIFF_THRESHOLD_LINES` (24, L11): `sourceLineCount(body)` decides `clampable`, and a
  collapsed diff slices the lines to the threshold and reports the exact `hiddenLines` on the
  `ClampButton`.
- `DiffLine` (L29) colors `+`/`-` lines `mint`/`alarm` (skipping `+++`/`---` file headers). The diff
  renders inside a `role="group"` / `aria-label={`diff of ${path}`}` / `tabIndex={-1}` region with
  `white-space: pre` so it scrolls inside itself — Home/End land as region scroll, not feed nav.

### Invariants And Boundaries

- No fabricated diff math: absent a server `unified`, only a labeled old/new pair is shown.
- The hidden-line count is the honest source-line delta (from `sourceLineCount`), never a pixel clamp.
- The scroll region is a labeled overflow group — the timeline's Home/End exemption depends on the
  `role="group"` marker being present here.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The shared ClampButton, `sourceLineCount`, and `useClampIds`. | L9, L46-L76 | [primitives.tsx](primitives.tsx) |
| The tool item that routes a `diff` block here (path/unified/old/new). | L102-L110 | [ToolItem.tsx](ToolItem.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the diff block —
  full-to-threshold with an exact hidden-line clamp, a labeled keyboard-scrollable `role="group"`
  region, and honest `synthesizeUnified` (no fabricated hunk headers). Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
