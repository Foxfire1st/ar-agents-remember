# dashboard/src/panels/engine-room/scene.ts

## Governing Overview

[panels/engine-room overview](overview.md)


## Current enclosure-only composition

resolveEngines(node) now derives hasMemory only. EnclosureScene drops provider nodes/predicted runtimes/workspace providers/providerPlanBlocked/providerScanAt. resolveBlocks uses contract-not-written missing fact as fleeting; source-only scan pointers and node/edge gate/landing/recovery/memory movement remain.

### Maintenance boundaries

Replace provider runtime/prediction and distinct provider-plan block guarantees with hasMemory/worktree materialization, pre-contract fleeting, and source scans. Document reduced one-argument resolveScene plus unchanged geometry-gated refusal composition; method name resolveEngines remains, not a gauge owner.

Source/test/fixture inspection is not a fresh mounted capture or a passing test run.
Historical provider-shaped input data and retained compatibility definitions do not
restore removed provider visuals or tool exposure.

- resolveEngines(node) now derives hasMemory only. EnclosureScene drops provider nodes/predicted runtimes/workspace provid — source ownership, not executed visual proof. [3]
- resolveEngines(node) now derives hasMemory only. EnclosureScene drops provider nodes/predicted runtimes/workspace provid — source ownership, not executed visual proof. [4]
- resolveEngines(node) now derives hasMemory only. EnclosureScene drops provider nodes/predicted runtimes/workspace provid — source ownership, not executed visual proof. [5]

## Historical superseded account (non-operative)

The prior onboarding below is retained for provenance and unrelated design history.
It is not current provider-render, fallback, prototype-parity or execution guidance.
Current behavior and its limits are the operative contract above.



The pure scene-resolution layer of the Engine Room, extracted from `EnclosureCanvas.tsx`
by the 260731-EFA-L8 responsibility split. It derives, from one `EngineProcessNode`,
the rendered engines, materialisation state, blocked lanes, scan pointers, memory
movement, gates, recovery chips, landing refs, and the full `EnclosureScene` the layer
components render.

## Code Commentary

### Logic

`resolveEngines` maps provider runtime facts to gauge states; `resolveBlocks` derives
the node-anchored gates (including the provider-plan block); `resolveScanPointers`
places verify-scan rings; `resolveMemoryMovement` detects upstream memory movement;
`resolveGates` derives gate bars; `resolveRecovery` picks recovery chips;
`resolveLanding` resolves the landing tier; `resolveScene` composes the whole packet.

### Conventions

Everything is a pure function of the projection node; no component state, no DOM.

### Invariants And Boundaries

The scene resolver must stay in lockstep with the projection vocabulary: unknown
fields degrade to the honest absent/planned register rather than fabricating state.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The scene packet and its resolving entry point. [1]
- The per-aspect resolvers consumed by the layers. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
