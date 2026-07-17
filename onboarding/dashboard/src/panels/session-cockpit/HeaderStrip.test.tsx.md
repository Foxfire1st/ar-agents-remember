# dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T06:10+02:00                           |
| lastVerifiedCommitHash | `96e1d6db63454438b57a7485382c27784a60776f`       |
| lastVerifiedCommitDate | 2026-07-17T06:28:52+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The jsdom suite for the HeaderStrip AND the SessionStage container (260715-FEUI-L2 S5/R11) — the
§1.2 anatomy and the stage layer order pinned on real DOM.

## Code Commentary

### Logic

- **HeaderStrip (R10)** — the anatomy order identity → controls → state → (leaf/seat) →
  diagnostics via DOM position; the ModelEffortControl slot ships EMPTY (L4 fills it); the state
  dot + word come from the shared grammar; freshness honesty (R15): `ws —` with no pane, real
  state + quiet age when known, the 10 s sweep bound in the tooltip; a hand-opened session
  renders NO provenance chips (absent, never invented).
- **Derived provenance tiers (R7, rewritten by L3)** (L68-L107) — the tier assertion runs on a
  PURPOSE-BUILT row (review finding 7 — not FLEET's `worker-l4`, whose claude-harness/codex-key
  pairing is an L2 fixture quirk that could silently flip the assertion if ever corrected): a
  ready claude row with `claude-fable-5[1m] · max` renders "(model-validated)" + the badge's
  `data-evidence-tier="model-validated"` (stream-json emits no launch-effort echo — the pair's
  honest ceiling); a NEW case pins a STARTING row to "(requested)" + tier `pending`.
- **SessionStage (R10)** — the reserved `data-slot="working-line"` sits DIRECTLY under the header
  (rendered by L6); the focus-handoff note (F17) and the EXPLAINED empty-stage identity (R9)
  render.

### Invariants And Boundaries

The anatomy-order and empty-slot cases are the R10 regression net; the no-provenance negative is
the R7 honesty net; the purpose-built derived-tier rows are the R7 control-state-gating net (they
must not be swapped back to shared FLEET rows — finding 7). Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two components under test. | — | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The stage container (slot order, handoff note, empty identity). | L62-L87 | [SessionStage.tsx](SessionStage.tsx) |
| The tier machine whose derivation the R7 cases pin. | L29-L41 | [../../data/launchEvidence.ts](../../data/launchEvidence.ts) |

## Update History

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
