# dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

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

- `Block` (L63) dispatches one `ConversationContentBlock` by `type`: `markdown`/`text`/`code` flow
  through `MarkdownBlock` (code is fenced with its language); `image-ref` renders a LABELED reference
  (L71-L85) — the alt text plus a `· filename/type fallback` note when `altProvenance ===
  "filename-mime-fallback"` and the MIME type — with **no `<img>` fetch and no invented
  `/api/assets/...` URL** (finding F11: no asset-read route exists in the backend; `assetId` is a
  submit-side reference, so an `<img>` would 404 on every future `image-ref`; the missing asset-read
  seam is recorded in-code); `file-ref`/`resource-ref` render a 📎 name + optional MIME chip.
- `MessageItem` (L100) computes the clamp from LOGICAL SOURCE LINES: `combinedSourceText` (L51) joins
  the markdown/text blocks, `sourceLineCount` counts newlines, and a message is `clampable` only when
  it is an assistant message, `phase === "completed"`, and exceeds `CLAMP_THRESHOLD_LINES` (40, L13).
- **Clamp by slicing, not by pixels (F12):** a collapsed message renders `sourceText.split("\n").
  slice(0, 40)` and reports `hiddenLines = totalLines - 40` (L109-L114), so the `+N lines` on the
  `ClampButton` is EXACTLY what is hidden — never a `maxHeight` visual clamp whose count diverges
  from the pixels actually hidden.
- The user role gets a distinct left-amber-border wrap and a `>` glyph (L118-L121); the head row
  shows a `SourceBadge` that appears only when the origin changes interpretation.

### Invariants And Boundaries

- An image is NEVER shown with missing alt; the accessible alt + provenance is mandatory (§6.6).
- No invented asset URL ships; when an asset-read seam lands, swap the labeled reference for an
  `<img>` carrying the same alt/provenance.
- The clamp count is honest: it is the source-line delta, and clamping only applies to a completed
  assistant message (a streaming message is never clamped mid-flow).

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
| The content-block/item types this component narrows over (`image-ref`, `altProvenance`). | L8-L9 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| Streaming-safe Markdown renderer used for every prose/code block. | L10, L63-L70 | [MarkdownBlock.tsx](MarkdownBlock.tsx) |
| The shared ClampButton (real button, exact `+N`), `sourceLineCount`, `SourceBadge`, `useClampIds`. | L11, L100-L138 | [primitives.tsx](primitives.tsx) |
| The kind dispatcher that routes messages here. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |
| The feed-ARIA/image-alt/clamp assertions covering this component. | — | [renderer.test.tsx](renderer.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the message item —
  streaming Markdown, the source-line-sliced clamp with an exact `+N lines` count (F12), and the
  labeled image reference with alt + provenance and no invented asset URL (F11). Verification is
  pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
