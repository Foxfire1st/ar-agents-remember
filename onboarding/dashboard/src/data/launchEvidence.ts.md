# dashboard/src/data/launchEvidence.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchEvidence.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

The **launch-evidence tier machine** (260715-FEUI-L3 R7), pure over row facts. Tier assignment is
gated on CONTROL STATE, never on the open response — `resolvedModel`/`resolvedEffort` are the
REQUESTED pair persisted verbatim BEFORE any validation (`terminal_opener.py` `_resolved_pair`),
so rendering them as validated during the starting window (or on a failed row) would be false
evidence. The SAME function feeds the HeaderStrip, the SeatInspector, and the launch flow so one
seat can never show two tiers — the `stateGrammar` doctrine, applied to evidence.

## Code Commentary

### Logic

- `hasLaunchEcho(harness)` (L24-L26) — whether a READY harness natively echoed the launched pair
  (L5 evidence, per the ACPUI handover): `codex` (model+effort via the app-server thread) and
  `pi` (model+thinking via `get_state`) → `true`; Claude stream-json echoes the launch MODEL but
  emits NO launch-effort echo — the pair as a whole never reaches readback. The two harness-id
  literals here are per-harness echo evidence the leaf doc itself mandates, not catalog data
  (reviewer-audited against the dynamic-only ruling).
- `launchTier(row)` (L29-L41) — controlState × retained pair → ONE of the five tiers, exactly the
  leaf-doc sketch in order: both-null pair → `defaults` (no selection was ever sent — checked
  FIRST, so a pairless failed row is `defaults`, not `refused`); `starting` → `pending` (requested
  provenance, no verification glyph); `failed` → `refused` (render beside bridgeError, never as
  validated); `ready` → `readback` iff `hasLaunchEcho` else `model-validated`; default
  (disconnected/unsupported/absent) → `pending`, no promotion. Single pair tier, weakest wins
  (worker decision 3, reviewer-accepted): Claude is capped at `model-validated` even though the
  launch MODEL echoes — per-knob set-evidence is L4's domain.
- `TIER_SENSE` (L44-L51) — the honest one-line meaning per tier, shared by the EvidenceBadge
  `title` and the launch flow.
- `verbatimBridgeError(controlRaw)` (L57-L66) — the retained verbatim bridge error off
  `controlRaw` (R6): a string renders verbatim; any other retained shape is `JSON.stringify`-
  serialized rather than reworded; `null` when nothing was retained (the banner states absence,
  never invents).

### Invariants And Boundaries

- Claude launch evidence can NEVER be `readback` (dedicated invariant test) — "weakest wins,
  never promoted without proof".
- No tier ever moves on the open response alone; promotion requires row control-state truth from
  the catalog poll.
- Pure module — no store writes, no fetches; every consumer derives at render time.

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
| The echo predicate, tier machine, tier senses, and verbatim bridge-error reader. | L24-L66 | [launchEvidence.ts](launchEvidence.ts) |
| The `EvidenceTier` vocabulary this returns (L2-seeded store type). | — | [sessionCockpitStore.ts](sessionCockpitStore.ts) |
| The requested-pair persistence this refuses to treat as proof. | — | [terminal_opener.py](../../../mcp/src/agents_remember/serving/terminal_opener.py) |
| The badge rendering the tier word + glyph. | — | [../grammar/EvidenceBadge.tsx](../grammar/EvidenceBadge.tsx) |
| Header derivation from row truth (`launchTier(session)`). | — | [../panels/session-cockpit/HeaderStrip.tsx](../panels/session-cockpit/HeaderStrip.tsx) |
| The failed-launch banner consuming `verbatimBridgeError` + the refused tier. | — | [../panels/session-cockpit/FailedLaunchBanner.tsx](../panels/session-cockpit/FailedLaunchBanner.tsx) |
| The exhaustive table suite incl. the claude-never-readback invariant. | — | [launchEvidence.test.ts](launchEvidence.test.ts) |

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

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7 (evidence tiers): the pure
  control-state-gated `launchTier` machine (both-null→defaults; starting→pending; failed→refused;
  ready→readback iff `hasLaunchEcho` — codex/pi true, claude false — else model-validated;
  default→pending), the shared `TIER_SENSE` senses, and the R6 `verbatimBridgeError` reader.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
