# dashboard/src/data/conversation/thinkingPreference.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/thinkingPreference.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

- `STORAGE_KEY = "cockpit.chats.hide-thinking.v1"` — the versioned localStorage key (house
  `cockpit.*.vN` convention, matching `keymap/preferences.ts`'s `cockpit.sessions.keymap.v1`). cit:([`STORAGE_KEY`], dashboard/src/data/conversation/thinkingPreference.ts:9-9)
- cit:([`readInitial`], dashboard/src/data/conversation/thinkingPreference.ts:11-17) — seeds `hidden` from `localStorage` (`"1"` ⇒ true), swallowing any
  storage-access throw (private mode) to `false`.
- cit:([`thinkingPreferenceStore`], dashboard/src/data/conversation/thinkingPreference.ts:25-36) — a vanilla zustand store; `setHidden` writes through to
  localStorage (swallowing a private-mode failure so the toggle still works in-session, just
  unpersisted) then `set({ hidden })`; `toggle` flips it.
- cit:([`useHideThinking`], dashboard/src/data/conversation/thinkingPreference.ts:38-39) — the thin React selector hook the surface/toggle read.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The full-inline thinking item whose rendering this toggle suppresses. | `ThinkingItem` | dashboard/src/panels/session-cockpit/conversation/ThinkingItem.tsx:35-56 |
| The surface toolbar hosting the toggle control. | "export function ConversationSurface" | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:269-269 |
| The house persisted-preference idiom this mirrors. | `KEYMAP_STORAGE_KEY` | dashboard/src/data/keymap/preferences.ts:17-17 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B20 curator: regenerated the out-of-bounds
  `ConversationSurface` range via the scoped fixer; exact non-fixing check returns zero findings.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 6 citations (three local prose anchors and three repository-internal references); no content claims changed.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the global hide-thinking
  preference — the sole persisted UI bit the R1 reconstructable-store rule permits, non-destructive
  (the reducer keeps thinking content; only rendering is suppressed). Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
