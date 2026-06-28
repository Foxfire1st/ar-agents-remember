# dashboard/src/dev/fixtures.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/dev/fixtures.ts`                  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-24T12:21+02:00                          |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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

## Code Commentary

### Logic

`project()` builds a full v2 `WorkspaceProjection`, deriving `metrics` from `lifecycles` and merging
caller `analytics` over `EMPTY_ANALYTICS`. It defaults `activeWorktreeGroups: []` (task 33's required
top-level field), overridable through `over`. **Slice 5i** extracts the engine-room wrap into an exported
`engineRoomProjection(scenario)` — `project({ providers: scenario.workspace, analytics: { ...EMPTY_ANALYTICS,
engineProcesses: scenario.processes, ledgers: [OFFICIAL_LEDGER] } })` — the single mapping now shared by
**both** the `GALLERY` Engine Room entries (which call it instead of the old inline `project(...)`) and the
slice-5i scenario-player frames (`dev/scenarios.ts`). Helpers `lifecycle()`, `enclosure()`, and `evt()` fill
sensible defaults over a required key; provider factories `ok`/`down`/`indexing` stamp `role` as
`memory` when the id contains `memory`/`grepai`, else `code`. `EMPTY_ANALYTICS` includes both
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

### Invariants And Boundaries

`EMPTY_ANALYTICS` now carries `series: []` and `engineProcesses: []`, so every projection has those keys. `dashboard/**`
is out of memory scope and the attention queues here are kept in sync with the reducer's
`build_attention_queue` by eye (sidecar-free); this onboarding file is the slice-5e exception. The
Engine Room scenes reuse the `engine-room/fixtures` source of truth rather than re-author processes.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `series: []` and `engineProcesses: []` are defaulted so every projection has the current analytics keys. | L16-L28 | [fixtures.ts](fixtures.ts) |
| Engine Room scenes spread into the gallery (the `engine-boot-*` frames filtered out of the tab strip). | L427-L433 | [fixtures.ts](fixtures.ts) |
| The `ENGINE_ROOM_SCENARIOS` (`processes` + `workspace`) consumed here. | L288-L623 | [engine-room/fixtures.ts](../panels/engine-room/fixtures.ts) |
| `series` and `engineProcesses` live on `WorkspaceProjection["analytics"]`. | L375-L386 | [projection.ts](../types/projection.ts) |

## Series-Contract Notes

The dev projection fixture now includes `enclosureId`, `leafId`, and `taskRoot` on each `EnclosureNode`, matching the server projection after leaf enclosure contracts moved under `enclosures/<leaf-id>/series-contract.md`.

## Update History

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
- 2026-06-18T21:27 — Dev-bench tab trim (mirrors task 5's `b3f2491`): the `GALLERY` map now `.filter(s => !s.name.startsWith("engine-boot-"))` so the 6 boot-step frames drop out of the bench picker (kept in `ENGINE_ROOM_SCENARIOS` for the render tests + slice 5i). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — slice 5h ledger popover: the gallery mapping sets `analytics.ledgers: [OFFICIAL_LEDGER]` (so the official coupler resolves its repo ledger) and the `full` scene's `LedgerNode`s gained `rows`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00 — Task 6 slice 6c Part B: added the `gate-review` gallery scene (a lifecycle with an open `closeout-approval` `gate` + a `gate-open` attention item) so the bench renders the Gate Review drawer. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-18T15:50+02:00 — slice 5h cleanup pass (feedback): the gallery spread now filters the `engine-boot-*` build-up frames out of the bench tab strip (they remain in `ENGINE_ROOM_SCENARIOS` for the component tests); refreshed the now-stale line-number citations. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-15T19:35 — Created for slice 5e: hand-authored bench gallery; slice 5e spreads ENGINE_ROOM_SCENARIOS into GALLERY and defaults engineProcesses in EMPTY_ANALYTICS. Verification metadata pinned until closeout stamps the 5e code commit.
