# dashboard/src/data/keymap/ — Keyboard Zone Contract Overview

## Governing Overview

[data overview](../overview.md)

## Purpose

This route owns the surviving pure keyboard zone, chord, reserved-key and preference contracts and their routing/preference tests. It owns no removed Chats composer, terminal React binding, focus-cycle module or keyboard palette.

## Construction And Ownership

`chords.ts` exports `ZoneChord` and the two `REVIEW_CHORDS`. `zones.ts` resolves only chrome/review markers and printable/editable passthrough; unknown markers resolve to chrome. `reserved.ts` exports only the `BROWSER_FORBIDDEN` browser-chord tuple, not PTY reservations or a matcher. `preferences.ts` validates review overrides and exposes bindings with a native cross-tab storage subscription. `zones.test.ts` and `preferences.test.ts` describe source assertions only. The reviewer owns actual tinykeys installation and effects; no removed focus, composer, terminal or palette consumer is implied.

## Verification Boundary

Static source/intent inspection only. The removal inventory and Git history, not archived cards or historical references to removed sources, hold the deletion history. No guard is changed and no runtime, MEMORY grade or acceptance is inferred.

## Evidence

- The reviewer's zone and chords. [1]

- The reviewer's own binding on its zone. [2]

- The effective-keymap preference and validation boundary. [3]
- The readonly BROWSER_FORBIDDEN tuple lists browser exclusions; no PTY table or matcher remains. [9]
- Chrome/review marker resolution and generic printable/editable passthrough; no slash predicate. [10]
- REVIEW_CHORDS alone supplies default review commands; invalid and colliding overrides fall back silently to those defaults. [11]
- EffectiveKeymap has bindings only, a native cross-tab storage subscription and aria conversion; no profile/activity/signature or same-tab notifier. [12]

- Remaining routing and preference test sources assert their pure keyboard contracts; removed focus/binding/composer tests are not current witnesses. No new test execution. [14]
- Effective review traversal wiring and its root marker. [15]
