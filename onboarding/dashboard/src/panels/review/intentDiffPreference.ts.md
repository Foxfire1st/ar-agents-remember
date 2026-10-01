# dashboard/src/panels/review/intentDiffPreference.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The reviewer's inline / side-by-side choice for changed intent wording (MIK-R35 rule 4).** It is a
browser-local UI preference in the house persisted-store idiom: a vanilla zustand store seeded from
`localStorage`, as `data/conversation/thinkingPreference.ts` does. It is not review state, and no server store
holds it (packet Exclusions: no server state).

## Code Commentary

### Logic

- `PROSE_LAYOUT_KEY` is `review.intent-diff.layout.v1`. `readProseLayout(storage)` answers `side-by-side` only when
  the stored value is exactly that; any other value, a missing storage, or a storage that throws on read answers
  `inline`.
- `proseLayoutStore` is seeded from `readProseLayout(storage())`, where `storage()` itself guards the
  `globalThis.localStorage` access. `setLayout` tries to write the key and swallows a storage failure (for example
  private mode), then sets the layout, so the toggle still works for the page's lifetime without persisting.
- `useProseLayout` subscribes a component to the layout. `IntentWordDiff.tsx`'s `ProseLayoutControl` writes it and
  every `TextPassage` reads it, so one choice switches every passage.

### Conventions

- Every storage read and write is guarded, following `thinkingPreference.ts`. The key carries a `.v1` suffix so a
  later shape can be versioned.

### Invariants And Boundaries

- When storage is unavailable the passage defaults to inline, and the toggle still switches (rule 4). A rewrite's
  per-passage "Show inline" is not this preference and is not saved (ruling Q2, 2026-09-30T11:53:13).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` live outside the
repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's statement: browser-local, the house idiom, no server store, inline when storage is unavailable. [1]
- The key and the guarded read. [2]
- The store: a guarded storage accessor, a write that never breaks the toggle, and the hook. [3]
- The house idiom it follows: a guarded read, and a write whose storage failure never breaks the toggle. [4]
- The cases: the choice kept locally; inline when storage throws, and the toggle still works. [5]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
