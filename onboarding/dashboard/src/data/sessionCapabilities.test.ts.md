# dashboard/src/data/sessionCapabilities.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/sessionCapabilities.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Pure/client tests for exact-session response classes, corrected effort-menu sourcing, cycling,
visibility, and evidence-backed effective markers.

## Code Commentary

### Logic

The suite pins fresh-Claude null effort despite omitted thought-level config, effortless rows,
native option order, staged-model re-gating/defaults, Pi keys, exact route URL, every HTTP class,
cycle wrap behavior, and snapshot-versus-echo timestamp precedence.

### Conventions

Deliberately unsorted fixtures prove filtering never sorts; fetch is stubbed only in client cases.

### Invariants And Boundaries

Test-only and exact-session-only; no pre-session cache fixture is accepted as a live source.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Client and pure derivations under test. | `classifySessionCapabilitiesResponse`, `deriveEffortMenu`, `visibleModelRows`, `cycleEffortTarget`, `effectiveSelection` | dashboard/src/data/sessionCapabilities.ts:71-92; dashboard/src/data/sessionCapabilities.ts:157-178; dashboard/src/data/sessionCapabilities.ts:182-186; dashboard/src/data/sessionCapabilities.ts:193-202; dashboard/src/data/sessionCapabilities.ts:219-248 |
| Shared recorded-shape fixture pack. | `ENVELOPES_BY_CACHE_STATUS` | dashboard/src/test/fixtures/capabilityEnvelopes.ts:175-179 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 2 repository-internal test-reference rows for the capability derivations and recorded fixture pack; final scoped result 0 (checker-clean).

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R1/R3/R7/R9; base metadata remains a
  pre-code-commit placeholder.
