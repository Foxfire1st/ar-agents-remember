# dashboard/src/data/keymap/preferences.test.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Pins effective-keymap persistence, validation, profile behavior, and same-/cross-tab subscription.

## Code Commentary

The suite covers valid overrides and profiles; malformed payloads; collision, printable-composer,
browser-reserved, and Meta-chord refusal; immutable F6 behavior; parser normalization; same-tab
writer notification; and browser `storage` propagation.

## Invariants And Boundaries

Tests must prove both the accepted effective binding and the visible issue for rejected input. A
test that only asserts fallback would hide why an operator preference was ignored.

### 2026-07-24 Curator Delta

Preference resolution now expects Enter as the default `composer.submit` chord, while retaining
validation of browser-reserved and duplicate bindings.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The suite tests a repository-local module and browser storage doubles; no cross-repository source applies.

No applicable cross-repository source was found.

### Repo-Internal References

- Unit under test. [1]
