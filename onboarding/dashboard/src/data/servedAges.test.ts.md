# dashboard/src/data/servedAges.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Pins the client half of the 260703-L15 volatile-age contract (`data/servedAges.ts`): the
field-set lockstep with the server, stable equality's skip rules, and the anchor-advance math.

## Code Commentary

L23 extends the mirror assertion with `elapsedSeconds`, proving lifecycle-operation wall-clock age is treated as volatile on the browser exactly like the server delta field.

Three describes:

- **`VOLATILE_AGE_FIELDS`** — the lockstep tripwire: asserts the sorted set is exactly
  `ageSeconds`, `heartbeatAgeSeconds`, `snapshotStaleSeconds`, `staleSeconds`, `waitSeconds`
  (the byte mirror of `serving/delta.py`); a drifted mirror fails here before it ships.
- **`stableEquals`** — volatile-only differences are equal (top-level, nested in arrays and
  objects, and a volatile field appearing/disappearing under the server's `exclude_none` wire
  form); real changes (value, array length, extra key, null→node) are detected; primitives and
  null handled.
- **`servedAgeSeconds`** — a stamped node's age advances by elapsed wall-clock
  (30 s served + 45 s elapsed = 75), never advances backwards on clock skew, an unstamped node
  serves its value as-is, a missing served value stays `undefined`, and a missing node passes
  through (call sites use optional chains).

## Invariants And Boundaries

- Pure vitest — no React render, no store; `useNowMs` is exercised implicitly through the four
  age panels' suites.

### 2026-07-24 Curator Delta

The hook tests now freeze a hidden layer's local clock and assert a single current-time catch-up when
the layer becomes active again.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Subject under test. [1]
- The server set this must mirror. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
