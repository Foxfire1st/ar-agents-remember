# dashboard/src/panels/engine-room/engineRoomTypes.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/engine-room/engineRoomTypes.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-23T13:45+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `EngineProcessView` joins a process node + lifecycle + `enclosureKey` | `EngineProcessView` | dashboard/src/panels/engine-room/engineRoomTypes.ts:15-25 |
| `EngineRoomModel` fields: processes, workspaceEngines, fallbackStacks, usesFallback | `EngineRoomModel` | dashboard/src/panels/engine-room/engineRoomTypes.ts:28-37 |
| EngineProcessNode is the generated projection contract consumed by this surface. | "export interface EngineProcessNode {" | dashboard/src/types/projection.ts:234-275 |
| LifecycleProjection is the generated projection contract consumed by this surface. | "export interface LifecycleProjection {" | dashboard/src/types/projection.ts:366-384 |
| ProviderNode is the generated projection contract consumed by this surface. | "export interface ProviderNode {" | dashboard/src/types/projection.ts:514-525 |
| `EngineStack` source type + `groupEngines` fallback producer | `EngineStack`; `groupEngines` | dashboard/src/data/selectors.ts:132-137; dashboard/src/data/selectors.ts:147-165 |

## Update History

- 2026-09-05T06:38:58+00:00 — CCR L31 dashboard citation curation: re-read the scoped claims against frozen source `ea35964985f30080488270e71ac81657ac40682b`, split pooled evidence and corrected current source boundaries. Historical claims retain their recorded provenance. This is scoped claim review; existing whole-file verification metadata is unchanged.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 3 citation claims
  (Repo-Internal reference rows); scoped result 0 findings.

- 2026-06-23T13:45+02:00 — Task 11: added `gate?: GateNode` to `EngineProcessView`, populated by
  `buildEngineRoomModel` from the joined lifecycle for the secondary Engine Room Respond surface.
  Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-16T01:55 — slice 5f S0: added `enclosureKey: string` to `EngineProcessView` (= worktreeGroup,
  the stable per-enclosure key for list rendering and the future promotion morph). Verification
  metadata pinned until closeout stamps the S0 code commit.
- 2026-06-15T19:35 — Created for slice 5e: EngineRoomModel + EngineProcessView types. Verification metadata pinned until closeout stamps the 5e code commit.
