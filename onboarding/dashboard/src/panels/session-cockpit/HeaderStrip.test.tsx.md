# dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.test.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
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
  state + quiet age when known, the 10 s sweep bound in the tooltip; provenance badges (R7)
  render requested model/effort at the honest tier + spawn level/source — and a hand-opened
  session renders NO provenance chips (absent, never invented).
- **SessionStage (R10)** — the reserved `data-slot="working-line"` sits DIRECTLY under the header
  (rendered by L6); the focus-handoff note (F17) and the EXPLAINED empty-stage identity (R9)
  render.

### Invariants And Boundaries

The anatomy-order and empty-slot cases are the R10 regression net; the no-provenance negative is
the R7 honesty net. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two components under test. | — | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The stage container (slot order, handoff note, empty identity). | L62-L86 | [SessionStage.tsx](SessionStage.tsx) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R11): HeaderStrip anatomy/empty-slot/
  grammar/freshness/provenance cases + the SessionStage working-line-slot position, handoff note,
  and explained empty state. Verification metadata pinned to the leaf base until closeout stamps
  the L2 code commit.
