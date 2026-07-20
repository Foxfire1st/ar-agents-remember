# dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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

- **`itemAccessibleName`** (L15-L42): a stable, human-readable text label per feed article
  (`#<globalOrdinal> <kind/phase>`, §14.2) — always a text label, never color-only.
- **`ConversationItemViewImpl`** (L44-L65): the kind switch — `message`/`plan` → `MessageItem`,
  `thinking` → `ThinkingItem`, `tool-call`/`tool-result` → `ToolItem`, `interaction` → `InteractionItem`,
  and `turn-result`/`error`/`notice`/`telemetry`/`unknown-vendor` (plus the default) → `TurnResultItem`.
- **`ConversationItemView`** (L68-L71): `memo`ized on item identity (`prev.item === next.item`), so a
  row re-renders only when its identity/revision object changes (the reducer swaps the object only on a
  real revision advance).

### Invariants And Boundaries

- Pure dispatch: no data, cursor, streaming, or store logic lives here.
- The accessible name is a text label, never color-only.
- Memoization relies on the reducer's identity-preserving item objects; a same-revision no-op keeps the
  same object and therefore skips the re-render.

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
| The kind switch and accessible-name helper. | L15-L71 | [ConversationItemView.tsx](ConversationItemView.tsx) |
| The item block-grammar renderers this dispatches to. | — | [MessageItem.tsx](MessageItem.tsx) · [ThinkingItem.tsx](ThinkingItem.tsx) · [ToolItem.tsx](ToolItem.tsx) · [InteractionItem.tsx](InteractionItem.tsx) · [TurnResultItem.tsx](TurnResultItem.tsx) |
| The `ConversationItem` wire type it switches on. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The feed that mounts one dispatcher per article and reads the accessible name. | — | [ConversationTimeline.tsx](ConversationTimeline.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the kind dispatcher — the
  pure switch mapping each normalized item to its block-grammar renderer plus the stable
  `itemAccessibleName`, `memo`ized on item identity for 10k-item timelines. Verification is pinned to
  the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
