# dashboard/src/data/conversation/thinkingPreference.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The full-inline thinking item whose rendering this toggle suppresses. [1]
- The surface toolbar hosting the toggle control. [2]
- The house persisted-preference idiom this mirrors. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
