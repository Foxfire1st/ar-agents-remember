# dashboard/src/data/servedAges.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `dashboard/src/data/servedAges.ts`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T05:02+02:00                     |
| lastVerifiedCommitHash | `6ea2a422210b4b9797d2c7c8df5f9994813f9331` |
| lastVerifiedCommitDate | 2026-07-06T21:07:46+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The server half: stable-form diff + the canonical volatile set. | [delta.py](agents-remember/mcp/src/agents_remember/serving/delta.py) |
| The consuming merge (identity reuse + stamping on apply). | [store.ts](agents-remember/dashboard/src/data/store.ts) |
| Display sites (`servedAgeSeconds` + `useNowMs`): Hangar, AttentionQueue, MemoryMirror, LifecycleList. | [panels/](agents-remember/dashboard/src/panels/Hangar.tsx) |

## Update History

- 2026-07-07T05:02+02:00 — Created for 260703-L15 S1: `VOLATILE_AGE_FIELDS` mirror,
  `stableEquals`, WeakMap arrival anchors + `servedAgeSeconds`, `useNowMs`.
  Verification metadata pinned until closeout stamps the L15 commit.
