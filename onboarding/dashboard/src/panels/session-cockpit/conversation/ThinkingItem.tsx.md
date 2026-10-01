# dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The thinking item of the harness-neutral grammar (design §12.2, §14.2): full-inline, dim/italic
reasoning that is NEVER clamped behind a Show-more. It is governed by the global hide-thinking
preference (instant, non-destructive) and uses CSS `content-visibility` so a pathological thinking
body stays sequentially readable/navigable without one enormous forced-layout DOM node.

## Code Commentary

### Logic

- cit:(["export const useHideThinking = (): boolean =>"], dashboard/src/data/conversation/thinkingPreference.ts:38-38) reads the global preference; when hidden the item collapses to a single
  `thinking hidden` marker (cit:([`hiddenMarker`], dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:27-27)) — the content stays in the store, only rendering is suppressed
  (non-destructive).
- When shown, it renders the marker label plus each block's text through `MarkdownBlock`
  (`testId="thinking-markdown"`). cit:([`thinkingText`], dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:34-38) reads `thinking`/`markdown` (`.markdown`) or
  `text` (`.text`) blocks and skips the rest. **FB7.4 (260718-CHATS-L5P):** the label is now Claude
  Code's inline lowercase marker `✻ thinking` at meta size — the uppercase/letterspaced `textTransform`
  was dropped (it was a boxed web-chip idiom the well does not use).
- The wrap sets `contentVisibility: "auto"` + `containIntrinsicSize: "auto 4rem"` (cit:([`wrap`], dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:11-20)) so a huge
  reasoning body is rendered in bounded segments — accessible, never deleted (§14.2).

### Invariants And Boundaries

- Thinking is full-inline and NEVER clamped (unlike a long assistant message, which is); the only
  suppression is the global hide-thinking toggle, which is reversible and content-preserving.
- The item is styled `muted`/italic so it reads as ambient reasoning, distinct from message prose.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The persisted global hide-thinking preference hook (the only durable UI bit). [1]
- The content-block/item types the thinking blocks come from. [2]
- Streaming-safe Markdown renderer used for each thinking block. [3]
- The kind dispatcher that routes thinking items here. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
