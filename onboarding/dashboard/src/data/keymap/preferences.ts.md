# dashboard/src/data/keymap/preferences.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Persists and validates the review keymap under cockpit.sessions.keymap.v1. Defaults come only from REVIEW_CHORDS; there is no composer profile or F6/chrome escape configuration.

## Code Commentary

`EffectiveKeymap` contains only `bindings`. `resolveKeymap` accepts version-1 objects, ignores unknown commands/extra fields and falls back silently to individual defaults for malformed, browser-forbidden or zone-colliding overrides. The small tinykeys parser canonicalizes known keys/modifier order and refuses repeated/incompatible modifiers. There is no issues/signature/activity result. The raw localStorage snapshot is cached and `useSyncExternalStore` subscribes only to a native storage event for the retained key: another tab can notify, but there is no same-tab write/notification API or preference screen. `bindingFor` looks up the effective review command; `ariaKeyshortcuts` converts validated chord spelling for accessibility. Preferences are browser-local, not host authority.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The preference module imports only repository-local keymap definitions and browser/React APIs; no cross-repository implementation governs validation or persistence.

No applicable cross-repository source was found.

### Repo-Internal References

- REVIEW_CHORDS is the retained default command table. [1]

- BROWSER_FORBIDDEN is the shared validation exclusion set. [2]

- Current defaults contain only REVIEW_CHORDS; the stored override and subscription surface remains. [5]


## 260718-CHATS-L4 Reviewed Candidate Delta (ariaKeyshortcuts helper)

Added the pure **`ariaKeyshortcuts(chord)`** helper: it renders a validated tinykeys chord as the
WAI-ARIA `aria-keyshortcuts` token (`Control+Shift+Period` → `Control+Shift+.`). The interrupt hook
(`conversation/useConversationControls.ts`) reads `bindingFor(useEffectiveKeymap(), "conversation.stop")?.chord`
and converts it through this helper, so a rebind of the stop chord through the `cockpit.sessions.keymap.v1`
seam keeps the assistive-tech advertisement truthful (F25) — replacing a hardcoded default constant.
Additive to the effective-keymap boundary; verification stays pinned to the FEUI-L8 base until closeout.
