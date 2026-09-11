# dashboard/src/dev/fixtures.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/fixtures.ts`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T09:52+02:00                          |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Hand-authored bench gallery: the grammar-state × attention-taxonomy `WorkspaceProjection`s the
`--sim` replay can't produce (sim emits one lifecycle). The bench hydrates each into the store and
component tests import them directly. Slice 5e folds the enclosure-centered Engine Room process map
in by spreading `ENGINE_ROOM_SCENARIOS` into `GALLERY` and defaulting `engineProcesses` in
`EMPTY_ANALYTICS`. The shared empty analytics fixture also defaults `series: []`, matching the
folder-keyed master surface added to the served projection.

Since 260731-EFA-L4 the split of responsibility is explicit in the file's own header: **the scenarios
are this file's business; the nodes are not.** Every node builder delegates to
`src/test/fixtures/wire.ts`, and `EMPTY_ANALYTICS` is imported from there rather than declared here.
What the gallery keeps is its own *defaults* — a running lifecycle reads better in a gallery than the
snapshot's blocked one — passed explicitly to the shared builders. What it no longer keeps is a second
copy of the required-field list, which is the part that drifts.

## Code Commentary

### Logic

**The wire delegation (260731-EFA-L4).** `project()` is now a thin call to `wire.ts`'s `projection()`
carrying only the gallery's two defaults (`version: 2`, the fixed `generatedAt`) plus the caller's
`over`. The shared builder supplies the required top-level fields (`enclosures`, `providers`,
`activeWorktreeGroups: []`), merges caller `analytics` over `EMPTY_ANALYTICS`, and — the load-bearing
part — **derives `metrics` via `metricsFor(lifecycles)`**, one bucket per active state read off the
state vocabulary. What that replaced was three hand-written `filter` counts here
(`runningCount`/`blockedCount`/`pausedCount`), a copy of the reducer's bucket list that missed
`awaiting-developer` exactly as the server's own copy did — so the gallery could not show the state
either. `lifecycle()`, `enclosure()`, and `evt()` delegate the same way to `servedLifecycle`,
`servedEnclosure`, and `servedObserverEvent` while keeping their gallery defaults ahead of `...over`;
the provider factories `ok`/`down`/`indexing` delegate to `servedProvider`, with the shared
`memory`/`code` role rule lifted out into a `providerRole(id)` helper instead of repeated three times.

A fixture that type-checks through these builders is a shape **the mirror** (`types/projection.ts`)
can produce. `wire.ts` bases are assembled from `src/fixtures/snapshot.json`, which is **hand-maintained
— there is no generator anywhere under `mcp/`, `scripts/` or `dashboard/`**. `wire.ts`'s own header
carries the full chain and where it stops: fixture ⊆ mirror is held by `tsc` and `contract.test.ts`;
mirror ⊆ server is held by hand.

**Slice 5i** extracts the engine-room wrap into an exported
`engineRoomProjection(scenario)` — `project({ providers: scenario.workspace, analytics: { ...EMPTY_ANALYTICS,
engineProcesses: scenario.processes, ledgers: [OFFICIAL_LEDGER] } })` — the single mapping now shared by
**both** the `GALLERY` Engine Room entries (which call it instead of the old inline `project(...)`) and the
slice-5i scenario-player frames (`dev/scenarios.ts`). Helpers `lifecycle()`, `enclosure()`, and `evt()` fill
sensible defaults over a required key; `providerRole(id)` stamps `role` as
`memory` when the id contains `memory`/`grepai`, else `code`. `EMPTY_ANALYTICS` — imported from
`test/fixtures/wire.ts` since 260731-EFA-L4, previously declared here — includes both
`taskDocuments: []` and `series: []`, so gallery projections satisfy the full dashboard analytics shape
even when a scene has no task reader data. `GALLERY` (typed `GalleryEntry[]`)
lists the `calm`/`blocked`/`alarm`/`full`/`gate-review`/`empty` scenes (the `gate-review` scene, slice
6c, carries an open `closeout-approval` `gate` on a lifecycle + a `gate-open` attention item so the Gate
Review drawer renders), then spreads
`...ENGINE_ROOM_SCENARIOS.filter((s) => !s.name.startsWith("engine-boot-")).map(...)` — each mapped to a
projection whose `providers` = the scenario's `workspace` and whose `analytics.engineProcesses` = the
scenario's `processes`. The `engine-boot-*` build-up frames (the 6 boot-step frames) are **filtered out of
the gallery tab strip** (5h cleanup) — they are a component-test-only step-through hidden from the bench
picker (slice 5i's scenario player plays the build-up), not a bench tab — while every other Engine Room
scenario still gets a tab; they stay in `ENGINE_ROOM_SCENARIOS` for the render tests. Slice 5h's ledger
popover wires its demo data through the projection: the Engine Room gallery mapping sets
`analytics.ledgers: [OFFICIAL_LEDGER]` (imported from `engine-room/fixtures`) so the OFFICIAL coupler
resolves its repo's ledger in `EngineRoom`; the `full` cockpit scene's hand-authored `LedgerNode`s gained
`rows` to satisfy the new required field.

### Conventions

Each builder takes a `Partial<Node>` widened with the keys the gallery insists on naming
(`Pick<…, "id">` for lifecycles, `"enclosure" | "repoName" | "taskName"` for enclosures), puts its
gallery defaults first and `...over` last, and hands the result to the matching `served*` builder from
`test/fixtures/wire.ts`. Scene data is authored inline in `GALLERY`; Engine Room scenes are never
re-authored here — they are mapped from `ENGINE_ROOM_SCENARIOS` through `engineRoomProjection`.

### Todos

No open file-local todos.

### Invariants And Boundaries

`EMPTY_ANALYTICS` carries `series: []` and `engineProcesses: []`, so every projection has those keys.
`dashboard/**` is out of memory scope and the attention queues here are kept in sync with the reducer's
`build_attention_queue` by eye (sidecar-free); this onboarding file is the slice-5e exception. The
Engine Room scenes reuse the `engine-room/fixtures` source of truth rather than re-author processes.

Since 260731-EFA-L4:

- **No node builder may hold its own required-field list.** Every builder delegates to
  `test/fixtures/wire.ts`; a required field the mirror adds must fail to compile here rather than be
  filled in a second place.
- **No bucket count may be hand-written here.** `metrics` comes from `metricsFor`, which reads the
  state vocabulary. A hand-kept bucket list is what hid `awaiting-developer` from the gallery.
- Gallery *defaults* are legitimate and stay: they are presentation choices (a running lifecycle, a
  fixed `generatedAt`), passed explicitly as overrides, not a parallel definition of the shape.
- `snapshot.json` behind those builders is hand-maintained and has no generator; a green build here
  claims the **mirror** could produce the shape, not that the server sent it.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card is verified from its direct source and the shared wire fixtures it
now delegates to.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

The gallery is now a consumer of the shared wire builders rather than a second definition of the wire
shape, so both sides of that delegation are cited.

| Finding | Anchor | Source |
| --- | --- | --- |
| The header stating the split (scenarios here, nodes in `wire.ts`) and the import block pulling `EMPTY_ANALYTICS` plus the five `served*` builders. | `EMPTY_ANALYTICS` | dashboard/src/dev/fixtures.ts:1-30 |
| `project()` calls `servedProjection`. | "function project(over: Partial<WorkspaceProjection> = {}): WorkspaceProjection {"; "return servedProjection({" | dashboard/src/dev/fixtures.ts:49-49; dashboard/src/dev/fixtures.ts:54-54 |
| `lifecycle()`, provider states, `enclosure()`, and `evt()` retain gallery defaults ahead of `...over`. | `lifecycle`; `providerRole`; `ok`; `down`; `indexing`; `enclosure`; `evt` | dashboard/src/dev/fixtures.ts:32-47; dashboard/src/dev/fixtures.ts:61-62; dashboard/src/dev/fixtures.ts:64-94; dashboard/src/dev/fixtures.ts:96-116; dashboard/src/dev/fixtures.ts:118-125 |
| The gallery maps Engine Room scenarios through `engineRoomProjection`. | "export const GALLERY: GalleryEntry[] = ["; "ENGINE_ROOM_SCENARIOS.filter"; "projection: engineRoomProjection(scenario)" | dashboard/src/dev/fixtures.ts:146-146; dashboard/src/dev/fixtures.ts:484-484; dashboard/src/dev/fixtures.ts:487-487 |
| `EMPTY_ANALYTICS` now lives in the shared wire fixtures and still carries `series: []` and `engineProcesses: []`. | `EMPTY_ANALYTICS` | dashboard/src/test/fixtures/wire.ts:223-237 |
| `projection()` assigns `metrics` from `metricsFor(lifecycles)`. | `metrics` | dashboard/src/test/fixtures/wire.ts:335-344 |
| The gallery consumes each `ENGINE_ROOM_SCENARIOS` entry by projecting its `processes` and `workspace` data. | "processes: EngineProcessNode[];"; "workspace: ProviderNode[];"; "ENGINE_ROOM_SCENARIOS.filter"; "projection: engineRoomProjection(scenario)" | dashboard/src/dev/fixtures.ts:484-484; dashboard/src/dev/fixtures.ts:487-487; dashboard/src/panels/engine-room/fixtures.ts:21-22 |
| Analytics requires series and engineProcesses arrays. | "export interface Analytics {" | dashboard/src/types/projection.ts:92-106 |
| WorkspaceProjection owns analytics as a required field. | "export interface WorkspaceProjection {" | dashboard/src/types/projection.ts:817-830 |

## Cross-Repo References

No meaningful cross-repo references found. The projection shapes these fixtures build mirror server
models in `mcp/` inside this same repository; nothing here crosses a repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Series-Contract Notes

The dev projection fixture now includes `enclosureId`, `leafId`, and `taskRoot` on each `EnclosureNode`, matching the server projection after leaf enclosure contracts moved under `enclosures/<leaf-id>/series-contract.md`. Since 260703-L11 the `enclosure(...)` factory also defaults the required existence-truth flags `codeWorktreeExists`/`memoryWorktreeExists` to `true`, so the seeded gallery enclosures render as live worktrees under the tasks surface's existence-only visibility rule.

## Update History

- 2026-09-05T06:38:58+00:00 — CCR L31 dashboard citation curation: re-read the scoped claims against frozen source `ea35964985f30080488270e71ac81657ac40682b`, split pooled evidence and corrected current source boundaries. Historical claims retain their recorded provenance. This is scoped claim review; existing whole-file verification metadata is unchanged.

- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: re-anchored citation range(s) to current source after the L12 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: bound fixture delegation, gallery scenes,
  engine-room scenario inputs and their gallery consumer, and analytics ownership to exact anchors;
  narrowed the projection and metrics rows to their cited facts and removed unscoped links.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->

- 2026-08-01T09:52+02:00 — 260731-EFA-L4 curator: documented the delegation to
  `src/test/fixtures/wire.ts`. Every node builder (`lifecycle`, `project`, `enclosure`, `evt`, and
  `ok`/`down`/`indexing`) now calls the shared builder, `EMPTY_ANALYTICS` is imported rather than
  declared here, and the `memory`/`code` rule was lifted into `providerRole(id)`. The load-bearing
  change is `metrics`: three hand-written `filter` counts (`runningCount`/`blockedCount`/
  `pausedCount`) were a copy of the reducer's bucket list that missed `awaiting-developer`, and are
  replaced by `metricsFor(lifecycles)` reading the vocabulary. The gallery keeps its own defaults but
  no longer a second copy of the required-field list. Recorded that `snapshot.json` behind those
  builders is **hand-maintained with no generator** — matching the header correction landed by the
  coordinator mid-review — so a green build claims the mirror could produce the shape, not that the
  server sent it. Rebuilt the Repo-Internal citations: all four prior ranges (`L16-L28`, `L427-L433`,
  `L288-L623`, `L375-L386`) had drifted off the symbols they named. Verification metadata left
  pinned; closeout stamps the code commit.
- 2026-07-06T03:15+02:00 — 260703-L11: the `enclosure(...)` fixture defaults the new required
  `codeWorktreeExists`/`memoryWorktreeExists` flags to `true` so dev-gallery enclosures stay visible
  under the existence-based Hangar/Tasks filter. Verification metadata pinned until closeout stamps the
  L11 commit.
- 2026-06-28T07:30+02:00 — Task 33: `project()` now defaults the new required `activeWorktreeGroups: []`
  (overridable via `over`). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 analytics fixture shape: `EMPTY_ANALYTICS` now defaults
  `series: []` beside `taskDocuments`, matching the folder-keyed master surface expected by the
  dashboard projection type. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: dev fixtures now populate `enclosureId`, `leafId`, and `taskRoot` on `EnclosureNode` so dashboard scenarios match the new projection identity fields. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T23:58+02:00 — slice 5i: extracted the engine-room projection wrap into the exported
  `engineRoomProjection(scenario)` helper, now shared by the `GALLERY` Engine Room entries and the new
  scenario-player frames (`dev/scenarios.ts`); the gallery spread calls it instead of an inline `project(...)`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27+02:00 — Dev-bench tab trim (mirrors task 5's `b3f2491`): the `GALLERY` map now `.filter(s => !s.name.startsWith("engine-boot-"))` so the 6 boot-step frames drop out of the bench picker (kept in `ENGINE_ROOM_SCENARIOS` for the render tests + slice 5i). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: the gallery mapping sets `analytics.ledgers: [OFFICIAL_LEDGER]` (so the official coupler resolves its repo ledger) and the `full` scene's `LedgerNode`s gained `rows`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): the gallery spread now filters the `engine-boot-*` build-up frames out of the bench tab strip (they remain in `ENGINE_ROOM_SCENARIOS` for the component tests); refreshed the now-stale line-number citations. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00+02:00 — Task 6 slice 6c Part B: added the `gate-review` gallery scene (a lifecycle with an open `closeout-approval` `gate` + a `gate-open` attention item) so the bench renders the Gate Review drawer. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-15T19:35+02:00 — Created for slice 5e: hand-authored bench gallery; slice 5e spreads ENGINE_ROOM_SCENARIOS into GALLERY and defaults engineProcesses in EMPTY_ANALYTICS. Verification metadata pinned until closeout stamps the 5e code commit.
