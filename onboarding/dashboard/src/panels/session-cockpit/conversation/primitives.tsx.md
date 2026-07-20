# dashboard/src/panels/session-cockpit/conversation/primitives.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/primitives.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The shared conversation-item primitives that enforce the ruled cross-item behaviors ONCE so every
block reads as one grammar (design §12.2, §14.2) and matches the cockpit house style (bare color
tokens, inline amber focus ring, lowercase interpunct chips — A8). No new palette or recipe is
introduced.

## Code Commentary

### Logic

- `ClampButton` (L37): the ONLY expand/collapse control for a clamped message/tool/diff. It is a real
  `<button>` with `aria-expanded`/`aria-controls`, and it shows an exact `Show more (+N lines)` ONLY
  when a logical source-line count is known (`hiddenLines > 0`); otherwise plain `Show more`/`Show
  less`. `noun` defaults to `lines`.
- `sourceLineCount` (L70): counts logical source lines (`split("\n").length`) — the honest basis for
  an exact clamp count, never visual wrapping/pixels.
- `SourceBadge` / `sourceBadgeLabel` (L92/L108): a terse source/lane badge shown ONLY when origin
  changes interpretation (§13) — `agent bus` (agent-bus lane / durable-inbox source), `native replay`,
  `native history`, `input source unavailable` (unknown-input lane), `terminal`; ordinary
  operator/harness content is UNBADGED (returns `null`).
- `CapabilityReason` (L130): renders the exact server reason (`state: reason`) for a
  partial/unavailable/unverified capability; returns `null` when `state === "supported"` — copy is
  honest and present, but structured (A3), never a wall.
- `useClampIds` (L140): a stable `useId`-based `{buttonId, regionId}` pair binding a clamp button to
  its controlled region.

### Invariants And Boundaries

- An exact `+N lines` count is emitted only from a known logical source-line delta; a clamp with an
  unknown count degrades to plain `Show more` rather than lying (F12/§14.2).
- A badge appears only when the source changes how the content should be read; the common case is
  deliberately unbadged (no chip noise).
- `CapabilityReason` renders the SERVER's exact reason — it never fabricates or paraphrases capability
  copy.

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
| The lane/source/capability types these primitives narrow over. | L8-L12 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The clamp/badge consumers across the grammar. | — | [MessageItem.tsx](MessageItem.tsx) · [ToolItem.tsx](ToolItem.tsx) · [DiffBlock.tsx](DiffBlock.tsx) |
| The surface that renders CapabilityReason for history/live completeness. | — | [ConversationSurface.tsx](ConversationSurface.tsx) |
| The renderer suite asserting the real clamp button + source badge. | — | [renderer.test.tsx](renderer.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the shared item
  primitives — the one real ClampButton (exact `+N lines` only when known), `sourceLineCount`, the
  interpretation-changing SourceBadge (ordinary content unbadged), CapabilityReason (exact server
  reason), and useClampIds. Verification is pinned to the leaf base (`0be0099`) because the new source
  file is uncommitted; closeout owns its first source stamp.
