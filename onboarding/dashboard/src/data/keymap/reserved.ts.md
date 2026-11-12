# dashboard/src/data/keymap/reserved.ts

## Governing Overview

[data/keymap overview](overview.md)

## Purpose

Defines the browser-forbidden chords that review keymap validation must reject. No PTY reservation, session-switch interception or hosted-harness collision-audit table remains.

## Code Commentary

The entire module exports `BROWSER_FORBIDDEN`, an `as const` tuple of chord strings. It lists Control and independent Meta browser shortcuts, `alt+f4` and `f11`; KeyboardEvent exposes Command as Meta rather than Control, so those entries are not aliases inferred by the caller. There are no `ReservedSurface` or `ChordMatch` types, structured chord/reason/forbiddenBy records, PTY reservations or matcher functions. Preference validation consumes this exclusion data; the module itself does not install bindings or observe browser/host execution.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- BROWSER_FORBIDDEN is declaration data; no PTY reserved/matching owner remains. [1]


### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Extends browser-forbidden safety to the macOS Meta equivalents of reserved browser chords. Effective user bindings must reject these just as they reject their Control variants.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
