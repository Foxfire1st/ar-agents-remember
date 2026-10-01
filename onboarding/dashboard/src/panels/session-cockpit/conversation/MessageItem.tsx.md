# dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The operator/assistant/user/system message item of the harness-neutral grammar (design §12.2). It
renders full streaming Markdown with no card noise; a completed long assistant message clamps behind
a real disclosure button carrying the EXACT hidden source-line count; images always render with a
non-empty accessible alt plus supplied-vs-fallback provenance. One grammar for every harness — no
vendor-clone skin.

## Code Commentary

### Logic

- cit:([`Block`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:67-102) dispatches one `ConversationContentBlock` by `type`: `markdown`/`text`/`code` flow
  through `MarkdownBlock` (code is fenced with its language); `image-ref` renders a LABELED reference
  cit:([`imageRef`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:40-52) — the alt text plus a `· filename/type fallback` note when `altProvenance ===
  "filename-mime-fallback"` and the MIME type — with **no `<img>` fetch and no invented
  `/api/assets/...` URL** (finding F11: no asset-read route exists in the backend; `assetId` is a
  submit-side reference, so an `<img>` would 404 on every future `image-ref`; the missing asset-read
  seam is recorded in-code); `file-ref`/`resource-ref` render a 📎 name + optional MIME chip.
- cit:([`MessageItem`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:104-156) computes the clamp from LOGICAL SOURCE LINES: cit:([`combinedSourceText`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:55-65) joins
  the markdown/text blocks, `sourceLineCount` counts newlines, and a message is `clampable` only when
  it is an assistant message, `phase === "completed"`, and exceeds `CLAMP_THRESHOLD_LINES` (40, L13).
- **Clamp by slicing, not by pixels (F12):** a collapsed message renders `sourceText.split("\n").
  slice(0, 40)` and reports `hiddenLines = totalLines - 40` cit:(["hiddenLines: collapsed ? Math.max(0"], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:169-169), so the `+N lines` on the
  `ClampButton` is EXACTLY what is hidden — never a `maxHeight` visual clamp whose count diverges
  from the pixels actually hidden.
- The user role gets a distinct left-amber-border wrap and a `>` glyph cit:([`userWrap`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:16-25); the head row
  shows a `SourceBadge` that appears only when the origin changes interpretation.

### Invariants And Boundaries

- An image is NEVER shown with missing alt; the accessible alt + provenance is mandatory (§6.6).
- No invented asset URL ships; when an asset-read seam lands, swap the labeled reference for an
  `<img>` carrying the same alt/provenance.
- The clamp count is honest: it is the source-line delta, and clamping only applies to a completed
  assistant message (a streaming message is never clamped mid-flow).

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The content-block/item types this component narrows over (`image-ref`, `altProvenance`). [1]
- Streaming-safe Markdown renderer used for every prose/code block. [2]
- The shared ClampButton (real button, exact `+N`), `sourceLineCount`, `SourceBadge`, `useClampIds`. [3]
- The kind dispatcher that routes messages here. [4]
- The feed-ARIA/image-alt/clamp assertions covering this component. [5]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Current L5I Maintenance

A streaming message now carries an explicit cyan dot plus lowercase `streaming` word beside its
source badge. The phase is therefore not color-only and follows the same compact grammar as other
in-progress conversation evidence.
