# dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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
  cit:(["export const ConversationItemView = memo("], dashboard/src/panels/session-cockpit/conversation/ConversationItemView.tsx:66-66)

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
| The item block-grammar renderers this dispatches to. | "export function MessageItem({ item }: { item: ConversationItem }) {"; "export function ThinkingItem({ item }: { item: ConversationItem }) {"; "export function InteractionItem({ item }: { item: ConversationItem }) {"; "export function TurnResultItem({ item }: { item: ConversationItem }) {" | dashboard/src/panels/session-cockpit/conversation/MessageItem.tsx:104-104; dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:35-35; dashboard/src/panels/session-cockpit/conversation/InteractionItem.tsx:73-73; dashboard/src/panels/session-cockpit/conversation/TurnResultItem.tsx:46-46 |
| The `ConversationItem` wire type it switches on. | `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176 |
| The feed that mounts one dispatcher per article and reads the accessible name. | "export function ConversationTimeline({" | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/ConversationTimeline.tsx:56-56 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-03T02:46:45+02:00 — W3-B04 curator: curated 3 table citations and 3 prose citations (6 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the kind dispatcher — the
  pure switch mapping each normalized item to its block-grammar renderer plus the stable
  `itemAccessibleName`, `memo`ized on item identity for 10k-item timelines. Verification is pinned to
  the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
