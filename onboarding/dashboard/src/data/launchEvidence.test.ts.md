# dashboard/src/data/launchEvidence.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchEvidence.test.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Exhaustive table suite for the five-tier machine (260715-FEUI-L3 R7/R8) — pins that tier
assignment is gated on control state (the open response echoes the REQUESTED pair pre-validation,
so no tier ever moves on it alone) and that the refusal path is uniform across all three
harnesses.

## Code Commentary

### Logic

- **Exhaustive table** (L19-L44) — harness (`claude|codex|pi`) × controlState
  (`starting|failed|ready|disconnected|unsupported|absent`) with a pair: starting→`pending`,
  failed→`refused`, ready→`readback` for codex/pi but `model-validated` for claude,
  disconnected/unsupported/absent→`pending` (no promotion without proof).
- **Both-null sweep** (L46-L50) — a pairless launch is `defaults` regardless of control state
  (nothing was requested).
- **Unknown harness** (L52-L58) — a settings-defined harness never promotes past
  `model-validated` on ready; `hasLaunchEcho` is false for unknown/undefined.
- **The review-killing invariant** (L60-L64) — Claude launch evidence NEVER reaches `readback`
  across every control state.
- **Fixture sweep** (L67-L108) — every R3 open/failed fixture classifies without fabrication:
  200-starting → `pending`, vendor-defaults → `defaults`, ALL THREE harnesses' failed rows (+ the
  Claude effort-refusal shape) → `refused` (tier uniformity ×3), `PENDING_INTERACTION_ROW`
  (ready, claude pair) → `model-validated`, FLEET's `worker-l4` (ready claude pair) →
  `model-validated` and FLEET's pairless failed `scout` → `defaults` (the L2 shared fixture,
  deliberately untouched — its bridgeError still renders in the banner).
- **`verbatimBridgeError` (R6)** (L110-L125) — string verbatim; non-string serialized
  (`{"code":7}`), never reworded; `null` for absence (banner states it, never invents).
- **`TIER_SENSE`** (L127-L134) — an honest sentence exists for every tier.

### Conventions

Pure-function tables — no DOM, no mocks; fixtures from `test/fixtures/openResponses.ts` and the
shared L2 `catalogRows.FLEET`. Test-only.

### Invariants And Boundaries

The claude-never-readback case and the uniform ×3 refused sweep are the honesty regression net:
they must keep failing if an echo is ever invented for Claude or a harness gets special-cased
refusal treatment.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tier machine under test. | L24-L66 | [launchEvidence.ts](launchEvidence.ts) |
| Failed-row/open-response fixtures (×3 harnesses + Claude effort refusal + pending interaction). | — | [../test/fixtures/openResponses.ts](../test/fixtures/openResponses.ts) |
| The shared L2 FLEET fixture (worker-l4 ready pair; pairless failed scout). | — | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7/R8: the exhaustive
  harness × controlState × pair table, the both-null sweep, the claude-never-readback invariant,
  the ×3-harness uniform-refusal sweep over the R3 fixtures (incl. FLEET), and the
  `verbatimBridgeError`/`TIER_SENSE` pins. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
