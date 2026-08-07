# dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/DiffBlock.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared ClampButton, `sourceLineCount`, and `useClampIds`. | `ClampButton`, `sourceLineCount`, `useClampIds` | dashboard/src/panels/session-cockpit/conversation/primitives.tsx:38-68; dashboard/src/panels/session-cockpit/conversation/primitives.tsx:71-74; dashboard/src/panels/session-cockpit/conversation/primitives.tsx:161-164 |
| The tool item that routes a `diff` block here (path/unified/old/new). | `diff` | dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx:115-115 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 2 citations for the body fallback and shared diff primitives.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the diff block —
  full-to-threshold with an exact hidden-line clamp, a labeled keyboard-scrollable `role="group"`
  region, and honest `synthesizeUnified` (no fabricated hunk headers). Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
