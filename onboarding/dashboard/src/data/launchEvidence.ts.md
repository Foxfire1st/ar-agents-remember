# dashboard/src/data/launchEvidence.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The echo predicate, tier machine, tier senses, and verbatim bridge-error reader. [1]
- The `EvidenceTier` vocabulary this returns (L2-seeded store type). [2]
- The requested-pair persistence this refuses to treat as proof. [3]
- The badge rendering the tier word + glyph. [4]
- Header derivation from row truth (`launchTier(session)`). [5]
- The failed-launch banner consuming `verbatimBridgeError` + the refused tier. [6]
- The exhaustive table suite incl. the claude-never-readback invariant. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
