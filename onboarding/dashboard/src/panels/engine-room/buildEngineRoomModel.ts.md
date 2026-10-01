# dashboard/src/panels/engine-room/buildEngineRoomModel.ts

## Governing Overview

[engine-room overview](overview.md)

## Purpose

The enclosure-centered Engine Room process map's pure builder: it projects the resolved server collections into an `EngineRoomModel` for rendering — joining each server-composed process node to its live lifecycle, exposing the lifecycle's projected gate, lifting the shared workspace (official/main) provider stack, exposing each enclosure's stable key, and falling back to the legacy `groupEngines` view for older projections that carry worktree providers but no process surface. It is React-free, clock-free, and does no semantic inference — the server already supplies the fact-state honesty.

## Code Commentary

### Logic

`buildEngineRoomModel(engineProcesses, providers, lifecycles)` is the sole export. It calls `groupEngines(providers)` to split providers into scoped stacks, then takes `workspaceEngines` from the single `scope === "workspace"` stack (empty array when absent) and `worktreeStacks` from the `scope === "worktree"` stacks. It builds a `Map` keyed by `lifecycle.id` and maps each `EngineProcessNode` into an `EngineProcessView` carrying `enclosureKey: node.worktreeGroup` (the stable per-enclosure key), the lifecycle resolved from its optional `lifecycleId` against that map (`undefined` when unset or unmatched), and `gate: lifecycle?.gate` for the secondary Engine Room respond surface. Process views are then sorted by a local phase priority so active/setup/sync work appears before cleanup/completed/abandoned work; `leafId || taskName` is the deterministic tie-breaker. The legacy fallback fires only when `engineProcesses.length === 0 && worktreeStacks.length > 0`; `fallbackStacks` is those worktree stacks when `usesFallback`, else empty. Returns `{ processes, workspaceEngines, fallbackStacks, usesFallback }`.

### Invariants And Boundaries

Inputs are flat arrays (mirroring `buildTopology`) so the seam stays React-free and unit-testable. No re-derivation of observed/derived/planned/missing fact-state or gate semantics — those are owned by the server (`analytics.engineProcesses` and `LifecycleProjection.gate`). `enclosureKey` is always `node.worktreeGroup` (never the node `id`), so it is stable across a fleeting→real promotion. The client may sort process pods by existing lifecycle phase so current work stays selectable ahead of cleanup-pending siblings from the same series, but it does not invent phases or statuses. Fallback and the process surface are mutually exclusive: a non-empty `engineProcesses` always wins and `usesFallback` stays false.

## Evidence

### Repo-Internal References

- The `buildEngineRoomModel` projection function is exported here. [1]
- Each view assigns `enclosureKey` from `node.worktreeGroup`. [2]
- `EngineRoomModel` render shape [3]
- `EngineProcessView` render shape [4]
- The model assigns the joined lifecycle gate into the process view. [5]
- `EngineProcessView` exposes the gate field. [6]
- `groupEngines` + `EngineStack.scope` workspace/worktree split [7]
- `EngineProcessNode.worktreeGroup` and `lifecycleId` [8]
- `ProviderNode.scope` [9]
