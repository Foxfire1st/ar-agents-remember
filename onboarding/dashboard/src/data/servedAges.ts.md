# dashboard/src/data/servedAges.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `dashboard/src/data/servedAges.ts`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The client half of the 260703-L15 **change-gate volatile-age contract**. The server's SSE diff
compares stable forms (now-relative age fields stripped — `serving/delta.py`), so a node whose
only movement is its age is never re-emitted; this module (1) mirrors the exact volatile field
set for the store's stable-equality merge and (2) anchors every applied node to its arrival time
so staleness displays advance locally between real emissions ("server-anchored, client-advanced").

## Code Commentary

`VOLATILE_AGE_FIELDS` — the five now-relative keys (`staleSeconds`, `snapshotStaleSeconds`,
`ageSeconds`, `waitSeconds`, `heartbeatAgeSeconds`), a byte-for-byte mirror of
`serving/delta.py`'s set; a lockstep test pins it (`servedAges.test.ts`).

`stableEquals(a, b)` — recursive deep equality over parsed wire payloads that SKIPS the volatile
keys on both sides (so a field appearing/disappearing under `exclude_none` also compares equal).
The store's merge uses it to recognize a byte-fresh but content-equal node and keep the existing
object identity — zero store write, zero downstream re-render, original age anchor kept.

`stampServed(node, atMs?)` / `servedAgeSeconds(node, servedSeconds, nowMs)` — arrival anchors in
a module-level `WeakMap` keyed by node object identity (never retains dropped nodes), and the
display-side read: served seconds + wall-clock elapsed since arrival, clamped never-backwards.
An unanchored node (fixtures, tests) serves its value as-is; a missing served value stays
`undefined` (never fabricated).

`useNowMs(stepMs = 10_000)` — the coarse ticking clock age panels re-render on; `fmtWait`'s
grain (s → m → h → d) makes the 10 s step visually seamless above the first minute.

## Invariants And Boundaries

- **Field-set lockstep** with `serving/delta.py` `VOLATILE_AGE_FIELDS` — a drifted set silently
  reintroduces per-tick re-emission (server side) or stale-vs-live misclassification (client
  side); the mirror test is the tripwire.
- **WeakMap only** — no side table may outlive its subject (the long-session rule).
- Ages are still never *computed* from the render clock — only aged forward from the served
  anchor (localhost clocks; skew far below display grain).

### 2026-07-24 Curator Delta

`useNowMs` accepts an active flag so kept-mounted hidden layers stop their local age interval. On
re-show it catches up once from the clock, preserving visible accuracy without hidden React work.

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
| The server half: stable-form diff + the canonical volatile set. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The consuming merge (identity reuse + stamping on apply). | [store.ts](agents-remember/dashboard/src/data/store.ts) |
| Display sites (`servedAgeSeconds` + `useNowMs`): Hangar, AttentionQueue, MemoryMirror, LifecycleList. | [panels/](agents-remember/dashboard/src/panels/Hangar.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-24T13:17:50Z — Added active-layer local-age scheduling semantics. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-07T05:02+02:00 — Created for 260703-L15 S1: `VOLATILE_AGE_FIELDS` mirror,
  `stableEquals`, WeakMap arrival anchors + `servedAgeSeconds`, `useNowMs`.
  Verification metadata pinned until closeout stamps the L15 commit.
