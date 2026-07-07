# dashboard/src/data/servedAges.test.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `dashboard/src/data/servedAges.test.ts`    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T05:04+02:00                     |
| lastVerifiedCommitHash | `e358c4ac520d94ae2e597ae3cbe186e07a4d1063` |
| lastVerifiedCommitDate | 2026-07-07T05:26:14+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Subject under test. | [servedAges.ts](agents-remember/dashboard/src/data/servedAges.ts) |
| The server set this must mirror. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |

## Update History

- 2026-07-07T05:04+02:00 — Created for 260703-L15 S1 (13 tests).
  Verification metadata pinned until closeout stamps the L15 commit.
