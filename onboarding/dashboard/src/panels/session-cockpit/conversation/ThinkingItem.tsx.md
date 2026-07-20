# dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The thinking item of the harness-neutral grammar (design §12.2, §14.2): full-inline, dim/italic
reasoning that is NEVER clamped behind a Show-more. It is governed by the global hide-thinking
preference (instant, non-destructive) and uses CSS `content-visibility` so a pathological thinking
body stays sequentially readable/navigable without one enormous forced-layout DOM node.

## Code Commentary

### Logic

- `useHideThinking` (L37) reads the global preference; when hidden the item collapses to a single
  `thinking hidden` marker (L38-L44) — the content stays in the store, only rendering is suppressed
  (non-destructive).
- When shown, it renders an uppercase `thinking` label plus each block's text through `MarkdownBlock`
  (`testId="thinking-markdown"`). `thinkingText` (L30) reads `thinking`/`markdown` (`.markdown`) or
  `text` (`.text`) blocks and skips the rest.
- The wrap sets `contentVisibility: "auto"` + `containIntrinsicSize: "auto 4rem"` (L17-L20) so a huge
  reasoning body is rendered in bounded segments — accessible, never deleted (§14.2).

### Invariants And Boundaries

- Thinking is full-inline and NEVER clamped (unlike a long assistant message, which is); the only
  suppression is the global hide-thinking toggle, which is reversible and content-preserving.
- The item is styled `muted`/italic so it reads as ambient reasoning, distinct from message prose.

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
| The persisted global hide-thinking preference hook (the only durable UI bit). | L7, L37 | [../../../data/conversation/thinkingPreference.ts](../../../data/conversation/thinkingPreference.ts) |
| The content-block/item types the thinking blocks come from. | L8 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| Streaming-safe Markdown renderer used for each thinking block. | L9, L51 | [MarkdownBlock.tsx](MarkdownBlock.tsx) |
| The kind dispatcher that routes thinking items here. | — | [ConversationItemView.tsx](ConversationItemView.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the thinking item —
  full-inline never-clamped dim reasoning, the global hide-thinking toggle (instant, non-destructive),
  and content-visibility bounding for large bodies. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
