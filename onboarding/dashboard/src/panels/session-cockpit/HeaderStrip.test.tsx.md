# dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                    |

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
  cit:([`launchTier`], dashboard/src/data/launchEvidence.ts:29-41) cit:(["the pending-interaction fixture (ready, claude pair) sits at model-validated"], dashboard/src/data/launchEvidence.test.ts:96-98) cit:(["open 200-starting responses render the retained pair at 'pending'"], dashboard/src/data/launchEvidence.test.ts:68-77)
- **SessionStage (R10)** — the reserved `data-slot="working-line"` sits DIRECTLY under the header
  (rendered by L6); the focus-handoff note (F17) and the EXPLAINED empty-stage identity (R9)
  render.

### Invariants And Boundaries

The anatomy-order and mounted-control-slot cases are the R10/L4 regression net; the no-provenance negative is
the R7 honesty net; the purpose-built derived-tier rows are the R7 control-state-gating net (they
must not be swapped back to shared FLEET rows — finding 7). Test-only.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two components under test. | "export function HeaderStrip({", "export function SessionStage({" | dashboard/src/panels/session-cockpit/HeaderStrip.tsx:132-132; dashboard/src/panels/session-cockpit/SessionStage.tsx:46-46 |
| The stage container (slot order, handoff note, empty identity). | "export function SessionStage({" | dashboard/src/panels/session-cockpit/SessionStage.tsx:46-46 |
| The tier machine whose derivation the R7 cases pin. | `launchTier`, `TIER_SENSE` | dashboard/src/data/launchEvidence.ts:29-41; dashboard/src/data/launchEvidence.ts:44-51 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

No HeaderStrip behavior changed. Its session fixture gained empty `submitHistory` to satisfy the
expanded cockpit state while keeping model/effort header assertions independent of prompt lifecycle.

## Current L5I Maintenance

The header tests now pin the absence of duplicate provenance/seat chrome and the accessible
unclassified-state fallback, alongside existing identity and control rendering checks.

## Update History

- 2026-08-03T02:43:48+02:00 — W3-B04 curator: curated 3 table citations and 3 prose citations (6 total), supplying exact anchors and paths; the scoped fixer generated all final extents.

- 2026-07-24T13:17:17Z — Curator: recorded header declutter and state-accessibility regressions;
  verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: updated the freshness-honesty pin — the no-pane
  case now asserts the `ws —` placeholder COLLAPSES (`not.toContain("ws —")`) rather than rendering a
  bare dash (R3); the sweep-bound tooltip pin is unchanged. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5 fixture-only refresh; no HeaderStrip semantic impact.

- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R2 replaced the empty-slot assertion with proof that
  the reserved controls segment mounts one `ModelEffortControl` and its trigger; fixture state
  also carries the L4 snapshot/echo defaults. Verification metadata remains pinned to the
  contract base until code commit.
- 2026-07-17T06:10+02:00 — 260715-FEUI-L3 (R7, fix round 1 finding 7): the derived-tier assertion
  rewritten in place onto a purpose-built claude/ready row asserting "(model-validated)" + the
  badge tier (the L2 `worker-l4` fixture quirk can no longer silently flip it), plus a new
  starting→"(requested)"/pending case. This is the R7 behavior change working as specified — the
  old `(requested)` pin only held because L2's tier source was the store default. Verification
  metadata pinned to the leaf base until closeout stamps the L3 code commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R11): HeaderStrip anatomy/empty-slot/
  grammar/freshness/provenance cases + the SessionStage working-line-slot position, handoff note,
  and explained empty state. Verification metadata pinned to the leaf base until closeout stamps
  the L2 code commit.
