# dashboard/src/dev/scenarios.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/scenarios.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `../overview.md`                                |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Slice 5i — the scenario MODEL behind the dev bench. A scenario is an ordered list of `ScenarioFrame`s,
each a FULL `WorkspaceProjection` plus a caption; the `ScenarioPlayer` applies one complete frame at a
time to the real store so the real cockpit animates the diff (center-out charge, draw-on conduits,
promote-in-place, the landing dock, the de-materialise) — making the integrated MOTION verifiable
end-to-end, not just static frames. Frames reuse the existing engine-room fixtures (no new substrate),
so a timeline is a sequence of named fixture states wrapped into full projections.

## Code Commentary

### Logic

Two interfaces — `ScenarioFrame { caption, projection, events?, durMs? }` and
`Scenario { name, label, frames }`. `erFrame(scenarioName, caption, durMs?)` looks the named scenario up
in `ENGINE_ROOM_SCENARIOS` (from `engine-room/fixtures`) and wraps it with `engineRoomProjection()` (from
`./fixtures`); it **throws** on an unknown name so an authoring typo fails loud in dev rather than
rendering an empty stage. Three authored timelines mirror the mockup's TWO separate animations plus one
failure mode: `buildUp` (`build-up`, B0 `engine-boot-0-main-only` → B5 `engine-boot-5-nominal`, the
worktree birth), `tearDown` (`tear-down`, D0 idle → D1 closeout → **D2** `engine-landing-ffonly`
(integrate — worktree → feat/fix source, push feat → origin/feat, PR open) → **D3** `engine-landing-pushed`
(code lands — PR merged → origin/main advances → local main pulls) → **D4** `engine-landing-merged` (memory
carryover) → D5 `engine-cleanup-pending` de-materialise (held 2200ms) → D6 `engine-retired`), and
`seedFault` (a GrepAI seed fault then the CGC reindex reroute, an amber fallback). **Slice 05k split the
previously-collapsed D2·D3 frame into two beats** (D2 integrate/push/PR-open + D3 the merge/code-lands),
adding the `engine-landing-pushed` `erFrame`. The old static gallery
states fold in as single-frame `restingScenarios` via `GALLERY.map(...)`, so no coverage is lost and each
stays reachable by name. **Slice 05o** adds a fourth timeline — `memoryBlock` (`memory-block`) — mirroring the prototype's **T3B
M0→M7** over ONE `boot-demo` enclosure (lifted beat-for-beat from `podstage.html`, not authored from memory):
M1 `engine-boot-1-code-worktree` (code lane solid) → M2 `engine-boot-memory-verify` (the ledger-map scan-ring)
→ M3 `engine-boot-memory-blocked` (steady gate + ghosted memory lane, code lane solid) → M4
`engine-boot-2-memory-contract` (reconcile — the ledger maps, the gate lifts, memory materialises) → **M5**
`engine-boot-3-providers-dim` + **M6** `engine-boot-4-seeding` (the provider runtime boots **on-screen** — the
cross-stage clone **copy-arrows** sweep + the engines charge cyan; the recover does NOT teleport to nominal) →
M7 `engine-boot-5-nominal`. **Slice 05o** also adds a fifth timeline — `staleBase` (`stale-base`) — mirroring the
prototype's **T1B F0→F8** over ONE `boot-demo` enclosure, the recoverable PRE-contract failure mode (the base is
behind upstream): F0 `engine-boot-0-main-only` (main at rest) → F1 `engine-boot-stale-verify` (preflight — the
code-lane scan: is local main current with upstream?) → F2 `engine-boot-stale-blocked` (**BLOCK** — base behind
upstream: the main node prunes/dormant and a fleeting enclosure is born blocked, held 2400ms) → **F3·F4**
`engine-boot-1-code-worktree` (fast-forward — the base updates, then the code worktree copies in from the
now-current main) → F5 `engine-boot-2-memory-contract` (memory worktree copies in, the coupler binds) → **F6**
`engine-boot-3-providers-dim` + **F7** `engine-boot-4-seeding` (the provider clone **copy-arrows** sweep + engines
charge cyan on recover — NOT a teleport to nominal) → F8 `engine-boot-5-nominal`. The export `SCENARIOS` is
`[buildUp, tearDown, seedFault, memoryBlock, staleBase, ...restingScenarios]` — timelines first (with `staleBase`
inserted after `memoryBlock`), then the resting frames.

**Slice 05o** then expanded the failure-mode set to a full eight modes. `seedFault` was **rewritten** as the
**T9B** boot-demo identity (one `boot-demo` enclosure throughout): charge cyan → S5 `engine-boot-seed-fault`
(the GrepAI seed arrow flashes RED + the engine flickers, CGC unaffected, held 2400ms) → S6
`engine-boot-seed-retry` re-seed → S7 nominal — an honest re-seed recover, never a teleport (the earlier
"then the CGC reindex reroute" no longer lives in `seedFault`; that reroute is now its own mode). Five more
timelines join it: `reindexReroute` (**T9C**, soft — CGC seed REFUSED → reindex in place via
`engine-cgc-seed-refused` (amber, 2000ms) → `engine-cgc-fallback` → nominal, health never gates/STOPs);
`providerBlock` (**T7B**, pre-contract — `engine-boot-provider-verify` plan → `engine-boot-provider-blocked`
gate BEFORE the contract anchors (held 2400ms) → recover supplies the config and deploys **through the
provider clone/seed beats** `-3-providers-dim`/`-4-seeding`); `liveSync` (**T12B**, the live memory-sync block
moved to `engine-sync-moved` → `engine-sync-memory-blocked` gate on the memory lane only (2400ms) →
`engine-sync-recovered` merge — a ref/ff diff, so it does NOT pass through the provider clone beats);
`integrationConflict` (**T14C**, TERMINAL — closeout → `engine-landing-ffonly` replay (1400ms) →
`engine-integration-conflict-flash` ⚡ → `engine-integration-conflict` steady **STOP** (2600ms), no recover
tail, source branch unmoved); and `abandon` (**T18**, TERMINAL — X0 working `engine-boot-5-nominal` →
`engine-boot-abandoned` dissolves the live enclosure with no landing, the X0→X2 step IS the Motion dissolve).
The export is now `[buildUp, tearDown, seedFault, reindexReroute, memoryBlock, staleBase, providerBlock,
liveSync, integrationConflict, abandon, ...restingScenarios]` — every recoverable mode passes through the
provider clone beats (except the ff-only `liveSync`), and the two terminal modes end on a STOP/dissolve.

### Invariants And Boundaries

DEV-only (the `/dev/*` route is dropped from the production bundle). Presentation data only — no behavior.
A frame is a complete projection, never an SVG patch, so seeking applies frame `t` and the cockpit
animates from wherever it currently is. The captions are load-bearing for `scenarios.test.ts` (it matches
`worktree_start` / `idle constellation` / `removed` etc.), and the tear-down must contain a
`cleanup-pending` phase frame (the de-materialise beat). Stays in lockstep with the engine-room fixture
names: a renamed/removed fixture must be reflected here or `erFrame` throws.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `erFrame` wraps a named engine-room scenario into a full projection. | L27-L31 | [scenarios.ts](scenarios.ts) |
| `engineRoomProjection` (the shared wrap) + `GALLERY` (folded-in resting states). | — | [fixtures.ts](fixtures.ts) |
| `ENGINE_ROOM_SCENARIOS` — the named fixture states the timelines reference. | — | [engine-room/fixtures.ts](../panels/engine-room/fixtures.ts) |
| Consumed by the player transport + the bench picker. | — | [ScenarioPlayer.tsx](ScenarioPlayer.tsx) · [Bench.tsx](Bench.tsx) |
| `WorkspaceProjection` / `ObserverEvent` types each frame carries. | — | [projection.ts](../types/projection.ts) · [event.ts](../types/event.ts) |

## FEUI-L8 Reviewed Candidate Delta

Folds the dedicated Chats scenario catalog into the existing picker and projects the interaction-answer gate only for that scenario. The large Engine Room timeline file remains a registry, not a duplicate transport fixture.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-06-22T11:00 — slice 05o: rewrote `seedFault` as the **T9B** single boot-demo identity (charge → RED
  GrepAI fault → re-seed → nominal; the CGC reroute that used to live here is now its own mode) and added five
  more failure modes — `reindexReroute` (**T9C**, soft CGC refused → reindex), `providerBlock` (**T7B**,
  pre-contract plan gate → recover through the provider clone beats), `liveSync` (**T12B**, memory-lane gate +
  ghost → merge/ff, no clone beats), `integrationConflict` (**T14C**, terminal replay → ⚡ → steady STOP), and
  `abandon` (**T18**, terminal working → dissolve). All added to `SCENARIOS`; recoverable modes pass through the
  provider clone beats, the terminal modes end on the STOP/dissolve. Verification metadata pinned until closeout
  stamps the 05o code commit.
- 2026-06-22T10:45 — slice 05o T1B: added the `staleBase` (`stale-base`) timeline mirroring the prototype's T1B F0→F8
  over ONE `boot-demo` enclosure (the recoverable pre-contract failure mode — base behind upstream): F0 main-only →
  F1 preflight (the code-lane scan) → F2 **BLOCK** (the main node prunes + a fleeting enclosure is born blocked, held
  2400ms) → F3·F4 fast-forward (the base updates, the code worktree copies in) → F5 memory worktree + coupler → F6
  providers-dim + F7 seed/clone (the provider copy-arrows sweep on recover, not a teleport) → F8 nominal. Inserted
  into `SCENARIOS` after `memoryBlock`. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — slice 05o T3B: added the `memoryBlock` (`memory-block`) timeline mirroring the
  prototype's T3B M0→M7 (one `boot-demo` enclosure: code-worktree → verify scan → BLOCK gate+ghost → reconcile
  → **providers-dim + seed/clone** (the copy-arrows sweep on recover) → nominal), inserted into `SCENARIOS`
  after `seedFault`. The recover passes through `engine-boot-3-providers-dim`/`-4-seeding` so the provider clone
  arcs play on-screen rather than teleporting to nominal (a first cut dropped these two beats — caught by the
  developer reviewing against `podstage.html`). Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:27+02:00 — slice 05k: split the tear-down's collapsed D2·D3 frame into two `erFrame`s — D2
  `engine-landing-ffonly` (integrate / push feat → origin/feat / PR open) + the new D3 `engine-landing-pushed`
  (PR merged → origin/main advances → local main pulls) — so the code-lands beat is distinct from integrate.
  Verification metadata pinned until closeout stamps the 05k code commit.
- 2026-06-19T23:58+02:00 — Created for slice 5i: the scenario model — `Scenario`/`ScenarioFrame` types, the
  `erFrame` fixture-wrapper (throws on a bad name), the `build-up` (B0→B5) / `tear-down` (D0→D6, incl. the
  `cleanup-pending` de-materialise + `engine-retired`) / `seed-fault` timelines, and the folded-in
  single-frame resting scenarios from `GALLERY`. Verification metadata pinned until closeout stamps the
  code commit.
