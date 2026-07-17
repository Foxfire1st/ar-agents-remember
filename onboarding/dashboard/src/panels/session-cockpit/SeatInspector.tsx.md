# dashboard/src/panels/session-cockpit/SeatInspector.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SeatInspector.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The focused seat's **read-only identity/provenance card** (260715-FEUI-L2 R7 + R17): the inspector
half of moat 1 — spawn provenance, requested model/effort at its honest tier, the spawned-by edge,
landed/retired reasons, liveness evidence — rendered from catalog truth only. The L7 inspector
(Evidence / Capabilities / Bus tabs) REPLACES this pane; the card keeps the facts visible until
then.

## Code Commentary

### Logic

- `Fact` (L33-L43): a label/value `dl` row that renders nothing for absent values (absent, never
  invented) with the full value as `title`.
- The card (L45-L110): **Seat** (label, grammar state word, harness, leafKey) → **Provenance**
  (spawn role, seat role, `level (source)`, `model <resolved> · <effort> (requested|tier)` —
  the same honest-tier wording as the HeaderStrip — spawned-by session, the frozen original
  label) → **Outcome** (only when landed/retired reasons exist: landed reason/at, retired
  reason/by — R17) → **Liveness** (only when evidence exists: liveness/exit evidence, first
  failed at). No focused seat ⇒ "no focused seat".

### Invariants And Boundaries

- READ-ONLY catalog truth; no store writes, no actions — the L7 tabbed inspector owns the
  interactive replacement.
- The requested-pair honesty boundary applies here identically to the HeaderStrip (tier word only
  with proof).
- Sections render only when their facts exist — the card never fabricates an empty scaffold.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Fact primitive + the sectioned card. | L33-L110 | [SeatInspector.tsx](SeatInspector.tsx) |
| The grammar supplying the state word. | L88-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The evidence tier consumed for the model wording. | L61 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The view mounting it in the inspector pane. | L610-L620 | [SessionsView.tsx](SessionsView.tsx) |
| The wire fields it mirrors (provenance, outcome, liveness). | L24-L90 | [../../types/terminalCatalog.ts](../../types/terminalCatalog.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 (R7/R17): the read-only provenance card in
  the inspector pane — seat identity + grammar state, spawn role/level/requested-pair at its
  honest tier, spawned-by + original label, landed/retired outcome reasons, and liveness
  evidence; placeholder until the L7 tabbed inspector. Verification metadata pinned to the leaf
  base until closeout stamps the L2 code commit.
