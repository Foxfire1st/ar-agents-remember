# dashboard/src/panels/session-cockpit/ModelEffortControl.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ModelEffortControl.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Header-mounted live model/effort readout, exact-session picker, staged apply flow, and acceptance
chip surface.

## Code Commentary

### Logic

Opening the controlled popover fetches only the live session snapshot. The trigger reads effective
selection and source; model options are visible snapshot rows, and effort options are re-gated to
the staged model's session-settable row. Model-only and effort-only apply one set; an explicitly
staged pair enters the serialized model-then-effort flow. Fetch errors render verbatim with retry,
while the adjacent chip row exposes pending and completed evidence.

### Conventions

Staged values are requests, not markers, and reset on open/session changes. A staged model's
default effort is only a visual pre-highlight until the user explicitly selects it.

### Invariants And Boundaries

The control renders only for live harness sessions. It never reads the pre-session catalog,
inherits an old row's effort options, or treats a missing echoed effort as an empty menu.

### Todos

- Reviewer sev-4 observation 6: before the first exact-session readback, the trigger fallback is
  visually indistinguishable from an echo-verified effective value even though its accessible
  description names the source.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Trigger, exact-session menus, staging, serialized apply, error, and chip UI. | L148-L383 | [ModelEffortControl.tsx](ModelEffortControl.tsx) |
| Sourcing, corrected menu, apply, and chip regression matrix. | L62-L371 | [ModelEffortControl.test.tsx](ModelEffortControl.test.tsx) |
| Live-session client and actions. | L1-L433 | [../../data/setClient.ts](../../data/setClient.ts) |
| Menu and effective-marker derivation. | L1-L248 | [../../data/sessionCapabilities.ts](../../data/sessionCapabilities.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Current L5I Maintenance

The trigger shows only a real running model/effort pair: freshest echoed evidence first, then the
launch-resolved value. Missing effort now removes its segment instead of emitting an unsupported
sentinel; the live menu remains the authority for choosing a value.

## Update History

- 2026-07-24T13:17:17Z — Curator: corrected missing-effort presentation to omission rather than a
  fabricated sentinel; verification fields remain pre-commit.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1–R3/R5/R6 through fix round 3 and
  final reviewer PASS. Sev-4 observation 6 remains recorded. Verification metadata is pinned to
  the contract base until code commit.
