# dashboard/src/data/servedAges.test.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `dashboard/src/data/servedAges.test.ts`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Pins the client half of the 260703-L15 volatile-age contract (`data/servedAges.ts`): the
field-set lockstep with the server, stable equality's skip rules, and the anchor-advance math.

## Code Commentary

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Subject under test. | [servedAges.ts](agents-remember/dashboard/src/data/servedAges.ts) |
| The server set this must mirror. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-24T13:17:50Z — Added hidden-layer age-clock regression coverage. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-07T05:04+02:00 — Created for 260703-L15 S1 (13 tests).
  Verification metadata pinned until closeout stamps the L15 commit.
