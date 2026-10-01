# dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom suite for the HeaderStrip AND the SessionStage container (260715-FEUI-L2 S5/R11) — the
§1.2 anatomy and the stage layer order pinned on real DOM.

## Code Commentary

### Logic

- **HeaderStrip (R10)** — the anatomy order identity → controls → state → (leaf/seat) →
  diagnostics via DOM position; FEUI-L4 mounts the real `ModelEffortControl` and trigger inside
  the reserved slot; the state
  dot + word come from the shared grammar; freshness honesty (R15 + R3): the ws marker COLLAPSES
  (is omitted, asserted `not.toContain("ws —")`) when no pane reports a state — 260718-CHATS-L5P
  changed this from the prior `ws —` placeholder assertion — with the real state + quiet age when
  known and the 10 s sweep bound still in the tooltip; a hand-opened session renders NO provenance
  chips (absent, never invented).
- **Derived provenance tiers (R7, rewritten by L3)** — the tier assertion runs on a
  PURPOSE-BUILT row (review finding 7 — not FLEET's `worker-l4`, whose claude-harness/codex-key
  pairing is an L2 fixture quirk that could silently flip the assertion if ever corrected): a
  ready claude row with `claude-fable-5[1m] · max` renders "(model-validated)" + the badge's
  `data-evidence-tier="model-validated"` (stream-json emits no launch-effort echo — the pair's
  honest ceiling); a NEW case pins a STARTING row to "(requested)" + tier `pending`.
  cit:([`launchTier`], dashboard/src/data/launchEvidence.ts:29-41) cit:(["the pending-interaction fixture (ready"], dashboard/src/data/launchEvidence.test.ts:96-98) cit:(["open 200-starting responses render the retained pair at 'pending'"], dashboard/src/data/launchEvidence.test.ts:68-77)
- **SessionStage (R10)** — the reserved `data-slot="working-line"` sits DIRECTLY under the header
  (rendered by L6); the focus-handoff note (F17) and the EXPLAINED empty-stage identity (R9)
  render.

### Invariants And Boundaries

The anatomy-order and mounted-control-slot cases are the R10/L4 regression net; the no-provenance negative is
the R7 honesty net; the purpose-built derived-tier rows are the R7 control-state-gating net (they
must not be swapped back to shared FLEET rows — finding 7). Test-only.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The two components under test. [1]
- The stage container (slot order, handoff note, empty identity). [2]
- The tier machine whose derivation the R7 cases pin. [3]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

No HeaderStrip behavior changed. Its session fixture gained empty `submitHistory` to satisfy the
expanded cockpit state while keeping model/effort header assertions independent of prompt lifecycle.

## Current L5I Maintenance

The header tests now pin the absence of duplicate provenance/seat chrome and the accessible
unclassified-state fallback, alongside existing identity and control rendering checks.
