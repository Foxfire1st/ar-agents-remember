# dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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
| The content-block/item types this component narrows over (`image-ref`, `altProvenance`). | `altProvenance` | dashboard/src/data/conversation/types.ts:83-83 |
| Streaming-safe Markdown renderer used for every prose/code block. | "export const MarkdownBlock" | dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:88-88 |
| The shared ClampButton (real button, exact `+N`), `sourceLineCount`, `SourceBadge`, `useClampIds`. | "export function ClampButton" | dashboard/src/panels/session-cockpit/conversation/primitives.tsx:38-38 |
| The kind dispatcher that routes messages here. | "export const ConversationItemView" | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:66-66 |
| The feed-ARIA/image-alt/clamp assertions covering this component. | "exposes a role=feed and articles keyed to the server globalOrdinal" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/feedSemantics.test.tsx:8-8 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

A streaming message now carries an explicit cyan dot plus lowercase `streaming` word beside its
source badge. The phase is therefore not color-only and follows the same compact grammar as other
in-progress conversation evidence.

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the superseded `(L…)`
  prose citations and the `n/a` rows with exact anchors and ranges; exact non-fixing check returns
  zero findings.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations. The four lines
  the streaming-phase cue added (the `streamDot`/`phaseWord` recipes and their comment, L28-L31)
  shifted everything below them by +4: `combinedSourceText` L51 → L55-L65, `Block` L63 → L67-L102,
  `MessageItem` L100 → L104-L156. cit:([`CLAMP_THRESHOLD_LINES`], dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:13-13) sits above the insert and was
  already correct.

- 2026-07-24T13:17:17Z — Curator: documented the visible, non-color-only streaming phase cue;
  verification fields remain pre-commit.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the message item —
  streaming Markdown, the source-line-sliced clamp with an exact `+N lines` count (F12), and the
  labeled image reference with alt + provenance and no invented asset URL (F11). Verification is
  pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
