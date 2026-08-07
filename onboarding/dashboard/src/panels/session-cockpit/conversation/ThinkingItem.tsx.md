# dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
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
| The persisted global hide-thinking preference hook (the only durable UI bit). | `useHideThinking` | dashboard/src/data/conversation/thinkingPreference.ts:38-39 |
| The content-block/item types the thinking blocks come from. | `ConversationContentBlock`, `ConversationItem` | dashboard/src/data/conversation/types.ts:63-105; dashboard/src/data/conversation/types.ts:158-176 |
| Streaming-safe Markdown renderer used for each thinking block. | `MarkdownBlock` | dashboard/src/panels/session-cockpit/conversation/MarkdownBlock.tsx:88-88 |
| The kind dispatcher that routes thinking items here. | `ConversationItemView` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:66-69 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: the L7 live-thinking renderer: the item gained the animated live indicator (shared `pulseSlow`, frozen by effects=off) and the timeline feeds it one coalesced row per active turn. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 4 citation rows and rewrote 2 prose citations; scoped citation fixing regenerated the source ranges.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 2 stale self-citations after the FB7.4
  `label` css shrank and shifted the component up a line: the `useHideThinking` call is
  (cit:([`ThinkingItem`], dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:35-56))
  and `thinkingText` is the whole helper at
  (cit:([`thinkingText`], dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:34-38)). Behaviour unchanged.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: corrected the label claim — the marker is now the
  lowercase inline `✻ thinking` (FB7.4), no longer uppercase/letterspaced. Never-clamped full-inline
  behavior + hide-thinking toggle + content-visibility bounding unchanged. Verification pinned to the
  leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the thinking item —
  full-inline never-clamped dim reasoning, the global hide-thinking toggle (instant, non-destructive),
  and content-visibility bounding for large bodies. Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
