# dashboard/src/data/servedAges.ts

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `dashboard/src/data/servedAges.ts`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
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

L23 adds `elapsedSeconds` to `VOLATILE_AGE_FIELDS`. Lifecycle-operation elapsed time can therefore advance without making an otherwise stable served enclosure look structurally changed.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The server half: stable-form diff + the canonical volatile set. | `VOLATILE_AGE_FIELDS` | mcp/src/agents_remember/serving/delta.py:36-38 |
| The consuming merge (identity reuse + stamping on apply). | `mergeKeyed` | dashboard/src/data/store.ts:66-67; dashboard/src/data/store.ts:91-111 |
| The display sites' shared import pattern (`servedAgeSeconds` + `useNowMs`): Hangar, AttentionQueue, MemoryMirror, LifecycleList. | "import { servedAgeSeconds, useNowMs } from \"../data/servedAges\";" | dashboard/src/panels/Hangar.tsx:3-3 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T18:16+02:00 — 260731-EFA-L6 S18-B16 curator: repaired 3 citation rows: the server half (serving/delta.py L33-L56, `VOLATILE_AGE_FIELDS`), the consuming merge (data/store.ts L66-L67 + L88-L110, `mergeKeyed`), and the four display-site import lines (Hangar/AttentionQueue/MemoryMirror/LifecycleList, `servedAgeSeconds`). Scoped fixer + non-fixing recheck green under the frozen snapshot; verification metadata unchanged.

- 2026-07-24T13:17:50Z — Added active-layer local-age scheduling semantics. Verification hash/date
  remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-07T05:02+02:00 — Created for 260703-L15 S1: `VOLATILE_AGE_FIELDS` mirror,
  `stableEquals`, WeakMap arrival anchors + `servedAgeSeconds`, `useNowMs`.
  Verification metadata pinned until closeout stamps the L15 commit.
