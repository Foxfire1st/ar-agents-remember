# dashboard/src/panels/review/intentDiffPreference.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/intentDiffPreference.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T13:18:53+02:00 |
| lastVerifiedCommitHash | `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`|
| lastVerifiedCommitDate | 2026-09-30T13:46:40+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured; the requirement packets `MIK-R35@v1` / `ICR-R35@v1` live outside the
repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's statement: browser-local, the house idiom, no server store, inline when storage is unavailable. | "It is not review state and no server"; "the passage defaults to inline" | dashboard/src/panels/review/intentDiffPreference.ts:1-5 |
| The key and the guarded read. | "export const PROSE_LAYOUT_KEY = 'review.intent-diff.layout.v1';"; "export function readProseLayout(" | dashboard/src/panels/review/intentDiffPreference.ts:12-20 |
| The store: a guarded storage accessor, a write that never breaks the toggle, and the hook. | "export const proseLayoutStore = createStore<ProseLayoutState>((set) => ({"; "export const useProseLayout = (): ProseLayout =>" | dashboard/src/panels/review/intentDiffPreference.ts:27-48 |
| The house idiom it follows: a guarded read, and a write whose storage failure never breaks the toggle. | "House persisted-store idiom"; "export const thinkingPreferenceStore = createStore<ThinkingPreferenceState>((set, get) => ({" | dashboard/src/data/conversation/thinkingPreference.ts:1-4; dashboard/src/data/conversation/thinkingPreference.ts:25-36 |
| The cases: the choice kept locally; inline when storage throws, and the toggle still works. | "switches every passage between inline and side by side and keeps the choice locally"; "defaults to inline when browser storage is unavailable, and the toggle still works" | dashboard/src/panels/review/IntentWordDiff.test.tsx:388-421 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T13:18:53+02:00 — 260928-MIK-L35 curator (staged change set on `ar/260928-mik-l35`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`; review R1 changes-required, R2 pass-with-notes, R2-1 fixed): created this card for the new preference store MIK-R35 rule 4 adds, recording ruling Q2 (the per-passage "Show inline" is not saved; 2026-09-30T11:53:13). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
