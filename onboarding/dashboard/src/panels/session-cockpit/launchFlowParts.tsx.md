# dashboard/src/panels/session-cockpit/launchFlowParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/launchFlowParts.tsx`  |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The launch-flow dialog render parts of the session cockpit, extracted from
`LaunchFlow.tsx` by the 260731-EFA-L8 split. Owns the harness section, model/effort
pickers, capability body, optional fields, launch footer, leaf-taken/conflict
outcomes, and the `LaunchFlowDialog` composition.

## Code Commentary

### Logic

`HarnessSection` renders the per-harness section; `ModelPicker`/`EffortPicker` render
the BOTH-knobs-or-NEITHER launch selection; `LeafTakenOutcome`/`ConflictOutcome`
render the fail-loud verbatim refusal states; `LaunchFlowDialog` composes them with
the overlay.

### Conventions

Presentational parts; launch state machines stay in `data/launchFlow.ts`.

### Invariants And Boundaries

No launch mutation here — outcomes render only what the flow machine reported.

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
| The dialog parts. | `HarnessSection`; `ModelPicker`; `LaunchFlowDialog` | dashboard/src/panels/session-cockpit/launchFlowParts.tsx:103-143; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:144-206; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:599-675; dashboard/src/panels/session-cockpit/launchFlowParts.tsx:571-571 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the launch
  flow parts module extracted from `LaunchFlow.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
