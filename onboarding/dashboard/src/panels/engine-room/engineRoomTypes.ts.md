# dashboard/src/panels/engine-room/engineRoomTypes.ts

## Governing Overview

[engine-room overview](overview.md)

## Purpose

Declares the client render model for the enclosure-centered Engine Room process map. The server composes the deterministic process nodes (`analytics.engineProcesses`) carrying their fact-state honesty; this file only describes the shape the client builds by joining each node to its live lifecycle, exposing that lifecycle's gate, lifting the shared workspace stack, and keeping a legacy fallback. No semantics are re-derived here.

## Code Commentary

### Logic

Two exported interfaces, both pure type declarations (no runtime code).

- `EngineProcessView` pairs one server-composed enclosure process `node: EngineProcessNode` with the optional live session `lifecycle?: LifecycleProjection` driving it, optional `gate?: GateNode` from that lifecycle, and (slice 5f S0) a `enclosureKey: string` — the stable React key = the node's `worktreeGroup`. The optional lifecycle marks processes with no active session; `enclosureKey` survives the fleeting→real id swap so list keying and the future promotion morph stay continuous.
- `EngineRoomModel` is the panel's full render model: `processes: EngineProcessView[]` (the enclosure pods in server-supplied deterministic order), `workspaceEngines: ProviderNode[]` (the official/main shared provider stack), `fallbackStacks: EngineStack[]` (legacy per-worktree stacks), and `usesFallback: boolean` (true when the projection predates the `engineProcesses` surface and the client fell back to `groupEngines`).

### Invariants And Boundaries

- Type-only module: it imports `EngineProcessNode`, `GateNode`, `LifecycleProjection`, `ProviderNode` from `../../types/projection` and `EngineStack` from `../../data/selectors`, and emits no values.
- `enclosureKey` must equal `node.worktreeGroup` (set by `buildEngineRoomModel`); it is the identity key, not the node `id`, because the `id` changes on fleeting→real promotion while `worktreeGroup` does not (5f §8.3).
- Process ordering is owned by the server; the client must preserve the supplied order rather than re-sort.
- `fallbackStacks` is consumed only when `usesFallback` is true (no `engineProcesses` present); the two surfaces are mutually exclusive in practice.

## Evidence

### Repo-Internal References

- `EngineProcessView` joins a process node + lifecycle + `enclosureKey` [1]
- `EngineRoomModel` fields: processes, workspaceEngines, fallbackStacks, usesFallback [2]
- EngineProcessNode is the generated projection contract consumed by this surface. [3]
- LifecycleProjection is the generated projection contract consumed by this surface. [4]
- ProviderNode is the generated projection contract consumed by this surface. [5]
- `EngineStack` source type + `groupEngines` fallback producer [6]
