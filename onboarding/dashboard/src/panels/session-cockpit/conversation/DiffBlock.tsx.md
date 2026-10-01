# dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The per-file diff block of the harness-neutral grammar (design §12.2): full by default up to a logical
source-line threshold, then a summary plus a real disclosure button with an EXACT hidden-line count.
Whitespace is preserved inside a labeled, keyboard-scrollable overflow region so a wide diff never
forces page-level horizontal scroll (§14.3).

## Code Commentary

### Logic

- `body = unified ?? synthesizeUnified(oldText, newText)` cit:([`body`], dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx:61-61): the server's `unified` string is
  preferred; when only old/new text is present, cit:([`synthesizeUnified`], dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx:92-99) prints a MINIMAL labeled
  `- old` / `+ new` pair rather than fabricating hunk headers — honesty over guessed diff math.
- Clamp at `DIFF_THRESHOLD_LINES` (24, L11): `sourceLineCount(body)` decides `clampable`, and a
  collapsed diff slices the lines to the threshold and reports the exact `hiddenLines` on the
  `ClampButton`.
- cit:([`DiffLine`], dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx:29-33) colors `+`/`-` lines `mint`/`alarm` (skipping `+++`/`---` file headers). The diff
  renders inside a `role="group"` / `aria-label={`diff of ${path}`}` / `tabIndex={-1}` region with
  `white-space: pre` so it scrolls inside itself — Home/End land as region scroll, not feed nav.

### Invariants And Boundaries

- No fabricated diff math: absent a server `unified`, only a labeled old/new pair is shown.
- The hidden-line count is the honest source-line delta (from `sourceLineCount`), never a pixel clamp.
- The scroll region is a labeled overflow group — the timeline's Home/End exemption depends on the
  `role="group"` marker being present here.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The shared ClampButton, `sourceLineCount`, and `useClampIds`. [1]
- The tool item that routes a `diff` block here (path/unified/old/new). [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
