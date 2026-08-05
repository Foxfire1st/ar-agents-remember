# dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The **kind dispatcher** (design §12.1): it maps a normalized `ConversationItem` to its block-grammar
renderer and provides the stable accessible name the feed article uses. It owns no
data/paging/streaming/cursor logic — it is a pure switch plus a `memo`, so 10k-item timelines stay
cheap.

## Code Commentary

### Logic

- **`itemAccessibleName`**: a stable, human-readable text label per feed article
  (`#<globalOrdinal> <kind/phase>`, §14.2) — always a text label, never color-only.
- **`ConversationItemViewImpl`**: the kind switch — `message`/`plan` → `MessageItem`,
  `thinking` → `ThinkingItem`, `tool-call`/`tool-result` → `ToolItem`, `interaction` → `InteractionItem`,
  and `turn-result`/`error`/`notice`/`telemetry`/`unknown-vendor` (plus the default) → `TurnResultItem`.
- **`ConversationItemView`**: `memo`ized on item identity (`prev.item === next.item`), so a
  row re-renders only when its identity/revision object changes (the reducer swaps the object only on a
  real revision advance).

  cit:([`itemAccessibleName`], dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:15-42)
  cit:([`ConversationItemViewImpl`], dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:44-65)
  cit:(["export const ConversationItemView = memo("], dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:68-68)

### Invariants And Boundaries

- Pure dispatch: no data, cursor, streaming, or store logic lives here.
- The accessible name is a text label, never color-only.
- Memoization relies on the reducer's identity-preserving item objects; a same-revision no-op keeps the
  same object and therefore skips the re-render.

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
| The kind switch and accessible-name helper. | `itemAccessibleName`, `ConversationItemViewImpl` | dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:15-42; dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:44-65 |
| The item block-grammar renderers this dispatches to. | `MessageItem`, `ThinkingItem`, `ToolItem`, `InteractionItem`, `TurnResultItem` | dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-101; dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:28-28; dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:104-156; dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:35-56; dashboard/src/panels/session-cockpit/conversation/ToolItem.tsx:87-118; dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx:46-82 |
| The `ConversationItem` wire type it switches on. | `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176 |
| The feed that mounts one dispatcher per article and reads the accessible name. | "export function ConversationTimeline({" | dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-344 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-03T02:46:45+02:00 — W3-B04 curator: curated 3 table citations and 3 prose citations (6 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the kind dispatcher — the
  pure switch mapping each normalized item to its block-grammar renderer plus the stable
  `itemAccessibleName`, `memo`ized on item identity for 10k-item timelines. Verification is pinned to
  the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
