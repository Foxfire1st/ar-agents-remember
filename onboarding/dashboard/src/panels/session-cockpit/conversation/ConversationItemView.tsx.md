# dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx

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
  cit:(["export const ConversationItemView = memo("], dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:66-66)

### Invariants And Boundaries

- Pure dispatch: no data, cursor, streaming, or store logic lives here.
- The accessible name is a text label, never color-only.
- Memoization relies on the reducer's identity-preserving item objects; a same-revision no-op keeps the
  same object and therefore skips the re-render.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The kind switch and accessible-name helper. [1]
- The item block-grammar renderers this dispatches to. [2]
- The `ConversationItem` wire type it switches on. [3]
- The feed that mounts one dispatcher per article and reads the accessible name. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
