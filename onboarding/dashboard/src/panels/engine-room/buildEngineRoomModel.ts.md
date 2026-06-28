# dashboard/src/panels/engine-room/buildEngineRoomModel.ts

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/engine-room/buildEngineRoomModel.ts` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-06-24T08:09+02:00                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`             |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The enclosure-centered Engine Room process map's pure builder: it projects the resolved server collections into an `EngineRoomModel` for rendering — joining each server-composed process node to its live lifecycle, exposing the lifecycle's projected gate, lifting the shared workspace (official/main) provider stack, exposing each enclosure's stable key, and falling back to the legacy `groupEngines` view for older projections that carry worktree providers but no process surface. It is React-free, clock-free, and does no semantic inference — the server already supplies the fact-state honesty.

## Code Commentary

### Logic

`buildEngineRoomModel(engineProcesses, providers, lifecycles)` is the sole export. It calls `groupEngines(providers)` to split providers into scoped stacks, then takes `workspaceEngines` from the single `scope === "workspace"` stack (empty array when absent) and `worktreeStacks` from the `scope === "worktree"` stacks. It builds a `Map` keyed by `lifecycle.id` and maps each `EngineProcessNode` into an `EngineProcessView` carrying `enclosureKey: node.worktreeGroup` (the stable per-enclosure key), the lifecycle resolved from its optional `lifecycleId` against that map (`undefined` when unset or unmatched), and `gate: lifecycle?.gate` for the secondary Engine Room respond surface. Process views are then sorted by a local phase priority so active/setup/sync work appears before cleanup/completed/abandoned work; `leafId || taskName` is the deterministic tie-breaker. The legacy fallback fires only when `engineProcesses.length === 0 && worktreeStacks.length > 0`; `fallbackStacks` is those worktree stacks when `usesFallback`, else empty. Returns `{ processes, workspaceEngines, fallbackStacks, usesFallback }`.

### Invariants And Boundaries

Inputs are flat arrays (mirroring `buildTopology`) so the seam stays React-free and unit-testable. No re-derivation of observed/derived/planned/missing fact-state or gate semantics — those are owned by the server (`analytics.engineProcesses` and `LifecycleProjection.gate`). `enclosureKey` is always `node.worktreeGroup` (never the node `id`), so it is stable across a fleeting→real promotion. The client may sort process pods by existing lifecycle phase so current work stays selectable ahead of cleanup-pending siblings from the same series, but it does not invent phases or statuses. Fallback and the process surface are mutually exclusive: a non-empty `engineProcesses` always wins and `usesFallback` stays false.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `buildEngineRoomModel` export — pure projection -> `EngineRoomModel` | [L19-L42](../../../../../dashboard/src/panels/engine-room/buildEngineRoomModel.ts) | [buildEngineRoomModel.ts](../../../../../dashboard/src/panels/engine-room/buildEngineRoomModel.ts) |
| `enclosureKey: node.worktreeGroup` set on each view | L29-L33 | [buildEngineRoomModel.ts](../../../../../dashboard/src/panels/engine-room/buildEngineRoomModel.ts) |
| `EngineRoomModel` / `EngineProcessView` render shapes | L14-L34 | [engineRoomTypes.ts](../../../../../dashboard/src/panels/engine-room/engineRoomTypes.ts) |
| `GateNode` comes from the joined lifecycle and is exposed as `EngineProcessView.gate`. | — | [projection.ts](../../../../../dashboard/src/types/projection.ts) |
| `groupEngines` + `EngineStack.scope` workspace/worktree split | L107-L137 | [selectors.ts](../../../../../dashboard/src/data/selectors.ts) |
| `EngineProcessNode.worktreeGroup`/`lifecycleId`, `ProviderNode.scope` | L29-L68, L251-L258 | [projection.ts](../../../../../dashboard/src/types/projection.ts) |

## Update History

- 2026-06-24T08:09+02:00 — Engine Room leaf identity: process views now sort active leaf enclosures ahead of cleanup/retired siblings and use `leafId || taskName` as the tie-breaker, preventing an old cleanup-pending leaf from becoming the selected duplicate parent task. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: `EngineProcessView` now carries `gate: lifecycle?.gate`, giving
  Engine Room diagnostics/canvas a direct projected gate instead of phase/edge inference. Verification
  metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-16T01:55 — slice 5f S0: each `EngineProcessView` now carries `enclosureKey = node.worktreeGroup`
  (the stable per-enclosure key consumers render by). Behaviour otherwise unchanged. Verification
  metadata pinned until closeout stamps the S0 code commit.
- 2026-06-15T19:35 — Created for slice 5e: pure builder: projection collections -> EngineRoomModel; lifts workspace stack, joins lifecycle, groupEngines fallback. Verification metadata pinned until closeout stamps the 5e code commit.
