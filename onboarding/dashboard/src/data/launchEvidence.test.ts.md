# dashboard/src/data/launchEvidence.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchEvidence.test.ts`      |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

- **Exhaustive table** cit:(["launchTier — exhaustive controlState × harness × pair table"], dashboard/src/data/launchEvidence.test.ts:19-65) — harness (`claude|codex|pi`) × controlState
  (`starting|failed|ready|disconnected|unsupported|absent`) with a pair: starting→`pending`,
  failed→`refused`, ready→`readback` for codex/pi but `model-validated` for claude,
  disconnected/unsupported/absent→`pending` (no promotion without proof).
- **Both-null sweep** cit:(["a BOTH-NULL launch is 'defaults' regardless of control state (no pair was ever sent)"], dashboard/src/data/launchEvidence.test.ts:46-50) — a pairless launch is `defaults` regardless of control state
  (nothing was requested).
- **Unknown harness** cit:(["an unknown/settings-defined harness never promotes past model-validated on ready"], dashboard/src/data/launchEvidence.test.ts:52-58) — a settings-defined harness never promotes past
  `model-validated` on ready; `hasLaunchEcho` is false for unknown/undefined.
- **The review-killing invariant** cit:(["Claude launch evidence NEVER reaches readback (the review-killing invariant)"], dashboard/src/data/launchEvidence.test.ts:60-64) — Claude launch evidence NEVER reaches `readback`
  across every control state.
- **Fixture sweep** cit:(["launchTier over the R3 fixture pack (every fixture exercised)"], dashboard/src/data/launchEvidence.test.ts:67-108) — every R3 open/failed fixture classifies without fabrication:
  200-starting → `pending`, vendor-defaults → `defaults`, ALL THREE harnesses' failed rows (+ the
  Claude effort-refusal shape) → `refused` (tier uniformity ×3), `PENDING_INTERACTION_ROW`
  (ready, claude pair) → `model-validated`, FLEET's `worker-l4` (ready claude pair) →
  `model-validated` and FLEET's pairless failed `scout` → `defaults` (the L2 shared fixture,
  deliberately untouched — its bridgeError still renders in the banner).
- **`verbatimBridgeError` (R6)** cit:(["verbatimBridgeError (R6)"], dashboard/src/data/launchEvidence.test.ts:110-125) — string verbatim; non-string serialized
  (`{"code":7}`), never reworded; `null` for absence (banner states it, never invents).
- **`TIER_SENSE`** cit:(["carries an honest sentence for every tier (badge titles)"], dashboard/src/data/launchEvidence.test.ts:128-133) — an honest sentence exists for every tier.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tier machine under test. | `launchTier` | dashboard/src/data/launchEvidence.ts:29-41 |
| Failed-row/open-response fixtures (×3 harnesses + Claude effort refusal + pending interaction). | `FAILED_LAUNCH_ROWS`; `FAILED_CLAUDE_EFFORT_ROW`; `PENDING_INTERACTION_ROW` | dashboard/src/test/fixtures/openResponses.ts:140-144; dashboard/src/test/fixtures/openResponses.ts:147-160; dashboard/src/test/fixtures/openResponses.ts:164-178 |
| The shared L2 FLEET fixture (worker-l4 ready pair; pairless failed scout). | `FLEET` | dashboard/src/test/fixtures/catalogRows.ts:32-172 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 10 citation items; scoped citation check now passes.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7/R8: the exhaustive
  harness × controlState × pair table, the both-null sweep, the claude-never-readback invariant,
  the ×3-harness uniform-refusal sweep over the R3 fixtures (incl. FLEET), and the
  `verbatimBridgeError`/`TIER_SENSE` pins. Verification metadata pinned to the leaf base until
  closeout stamps the L3 code commit.
