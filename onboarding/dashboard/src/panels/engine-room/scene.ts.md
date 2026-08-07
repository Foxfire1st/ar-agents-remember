# dashboard/src/panels/engine-room/scene.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/engine-room/scene.ts`                 |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/engine-room overview](overview.md)

## Purpose

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The scene packet and its resolving entry point. | `EnclosureScene`; `resolveScene` | dashboard/src/panels/engine-room/scene.ts:22-58; dashboard/src/panels/engine-room/scene.ts:324-369 |
| The per-aspect resolvers consumed by the layers. | `resolveEngines`; `resolveBlocks`; `resolveRecovery` | dashboard/src/panels/engine-room/scene.ts:74-110; dashboard/src/panels/engine-room/scene.ts:157-195; dashboard/src/panels/engine-room/scene.ts:292-303 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the new
  scene module extracted from `EnclosureCanvas.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
