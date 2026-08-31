# dashboard/src/data/launchEvidence.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/launchEvidence.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
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

- cit:([`hasLaunchEcho`], dashboard/src/data/launchEvidence.ts:24-26) — whether a READY harness natively echoed the launched pair
  (L5 evidence, per the ACPUI handover): `codex` (model+effort via the app-server thread) and
  `pi` (model+thinking via `get_state`) → `true`; Claude stream-json echoes the launch MODEL but
  emits NO launch-effort echo — the pair as a whole never reaches readback. The two harness-id
  literals here are per-harness echo evidence the leaf doc itself mandates, not catalog data
  (reviewer-audited against the dynamic-only ruling).
- cit:([`launchTier`], dashboard/src/data/launchEvidence.ts:29-41) — controlState × retained pair → ONE of the five tiers, exactly the
  leaf-doc sketch in order: both-null pair → `defaults` (no selection was ever sent — checked
  FIRST, so a pairless failed row is `defaults`, not `refused`); `starting` → `pending` (requested
  provenance, no verification glyph); `failed` → `refused` (render beside bridgeError, never as
  validated); `ready` → `readback` iff `hasLaunchEcho` else `model-validated`; default
  (disconnected/unsupported/absent) → `pending`, no promotion. Single pair tier, weakest wins
  (worker decision 3, reviewer-accepted): Claude is capped at `model-validated` even though the
  launch MODEL echoes — per-knob set-evidence is L4's domain.
- cit:([`TIER_SENSE`], dashboard/src/data/launchEvidence.ts:44-51) — the honest one-line meaning per tier, shared by the EvidenceBadge
  `title` and the launch flow.
- cit:([`verbatimBridgeError`], dashboard/src/data/launchEvidence.ts:57-66) — the retained verbatim bridge error off
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The echo predicate, tier machine, tier senses, and verbatim bridge-error reader. | `hasLaunchEcho`, `launchTier`, `TIER_SENSE`, `verbatimBridgeError` | dashboard/src/data/launchEvidence.ts:24-26; dashboard/src/data/launchEvidence.ts:29-41; dashboard/src/data/launchEvidence.ts:44-51; dashboard/src/data/launchEvidence.ts:57-66 |
| The `EvidenceTier` vocabulary this returns (L2-seeded store type). | `EvidenceTier` | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| The requested-pair persistence this refuses to treat as proof. | `_resolved_pair` | mcp/src/agents_remember/serving/terminal_opener.py:434-437 |
| The badge rendering the tier word + glyph. | `EvidenceBadge` | dashboard/src/grammar/EvidenceBadge.tsx:46-69 |
| Header derivation from row truth (`launchTier(session)`). | `HeaderStrip` | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:88-169 |
| The failed-launch banner consuming `verbatimBridgeError` + the refused tier. | `FailedLaunchBanner` | dashboard/src/panels/session-cockpit/FailedLaunchBanner.tsx:69-143 |
| The exhaustive table suite incl. the claude-never-readback invariant. | "launchTier — exhaustive controlState × harness × pair table" | dashboard/src/data/launchEvidence.test.ts:19-65 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-02T20:41:24+02:00 — L6 W2-B02 curator: anchored 6 repository-internal reference rows for the launch-evidence machine, opener persistence, UI consumers, and exhaustive tests; final scoped result 0 (checker-clean).

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T06:10+02:00 — Created for 260715-FEUI-L3 R7 (evidence tiers): the pure
  control-state-gated `launchTier` machine (both-null→defaults; starting→pending; failed→refused;
  ready→readback iff `hasLaunchEcho` — codex/pi true, claude false — else model-validated;
  default→pending), the shared `TIER_SENSE` senses, and the R6 `verbatimBridgeError` reader.
  Verification metadata pinned to the leaf base until closeout stamps the L3 code commit.
