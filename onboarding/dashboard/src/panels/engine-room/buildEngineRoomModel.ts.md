# dashboard/src/panels/engine-room/buildEngineRoomModel.ts

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `dashboard/src/panels/engine-room/buildEngineRoomModel.ts` |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-08-02T01:42+02:00                                 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`             |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The `buildEngineRoomModel` projection function is exported here. | "function buildEngineRoomModel" | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:33-33 |
| Each view assigns `enclosureKey` from `node.worktreeGroup`. | `enclosureKey` | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:47-47 |
| `EngineRoomModel` render shape | `EngineRoomModel` | dashboard/src/panels/engine-room/engineRoomTypes.ts:28-37 |
| `EngineProcessView` render shape | `EngineProcessView` | dashboard/src/panels/engine-room/engineRoomTypes.ts:15-25 |
| The model assigns the joined lifecycle gate into the process view. | "lifecycle?.gate" | dashboard/src/panels/engine-room/buildEngineRoomModel.ts:50-50 |
| `EngineProcessView` exposes the gate field. | `EngineProcessView` | dashboard/src/panels/engine-room/engineRoomTypes.ts:15-25 |
| `groupEngines` + `EngineStack.scope` workspace/worktree split | `groupEngines` | dashboard/src/data/selectors.ts:147-165 |
| `EngineProcessNode.worktreeGroup` and `lifecycleId` | `EngineProcessNode` | dashboard/src/types/projection.ts:162-202 |
| `ProviderNode.scope` | `ProviderNode` | dashboard/src/types/projection.ts:355-366 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: applied reviewer verdict D1-D25 deterministic whole-claim repairs; corrected operative source ranges and focused assertions, removed the false Pi gate-field claim, and rechecked this card through the locked exact-document fixer/check.

- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-06-24T08:09+02:00 — Engine Room leaf identity: process views now sort active leaf enclosures ahead of cleanup/retired siblings and use `leafId || taskName` as the tie-breaker, preventing an old cleanup-pending leaf from becoming the selected duplicate parent task. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: `EngineProcessView` now carries `gate: lifecycle?.gate`, giving
  Engine Room diagnostics/canvas a direct projected gate instead of phase/edge inference. Verification
  metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-16T01:55 — slice 5f S0: each `EngineProcessView` now carries `enclosureKey = node.worktreeGroup`
  (the stable per-enclosure key consumers render by). Behaviour otherwise unchanged. Verification
  metadata pinned until closeout stamps the S0 code commit.
- 2026-06-15T19:35 — Created for slice 5e: pure builder: projection collections -> EngineRoomModel; lifts workspace stack, joins lifecycle, groupEngines fallback. Verification metadata pinned until closeout stamps the 5e code commit.
