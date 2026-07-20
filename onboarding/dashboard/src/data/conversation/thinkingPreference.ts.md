# dashboard/src/data/conversation/thinkingPreference.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/thinkingPreference.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The developer-ruled GLOBAL hide-thinking preference (design §12.2, §14.2). It is a UI preference —
not per-harness behavior — that suppresses the RENDERING of thinking items; the reducer always keeps
the normalized thinking content, so the toggle is instant and non-destructive. This boolean is the
**only persisted state in the entire conversation data layer**: the R1 no-durable-browser-index rule
permits exactly this one UI preference bit and nothing conversation-content-bearing.

## Code Commentary

### Logic

- `STORAGE_KEY = "cockpit.chats.hide-thinking.v1"` (L9) — the versioned localStorage key (house
  `cockpit.*.vN` convention, matching `keymap/preferences.ts`'s `cockpit.sessions.keymap.v1`).
- `readInitial()` (L11-L17) — seeds `hidden` from `localStorage` (`"1"` ⇒ true), swallowing any
  storage-access throw (private mode) to `false`.
- `thinkingPreferenceStore` (L25-L36) — a vanilla zustand store; `setHidden` writes through to
  localStorage (swallowing a private-mode failure so the toggle still works in-session, just
  unpersisted) then `set({ hidden })`; `toggle` flips it.
- `useHideThinking()` (L38-L39) — the thin React selector hook the surface/toggle read.

### Invariants And Boundaries

- Non-destructive: hiding thinking never removes normalized items from the projection — only
  `ThinkingItem` rendering is suppressed. Re-showing is instant with no re-fetch.
- A storage write failure is tolerated (in-session toggle still works); persistence is best-effort.
- This is the sole durable UI bit the R1 reconstructable-store rule permits; nothing here caches
  conversation content.

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
| The full-inline thinking item whose rendering this toggle suppresses. | — | [../../panels/session-cockpit/conversation/ThinkingItem.tsx](../../panels/session-cockpit/conversation/ThinkingItem.tsx) |
| The surface toolbar hosting the toggle control. | — | [../../panels/session-cockpit/conversation/ConversationSurface.tsx](../../panels/session-cockpit/conversation/ConversationSurface.tsx) |
| The house persisted-preference idiom this mirrors. | — | [../keymap/preferences.ts](../keymap/preferences.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the global hide-thinking
  preference — the sole persisted UI bit the R1 reconstructable-store rule permits, non-destructive
  (the reducer keeps thinking content; only rendering is suppressed). Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
