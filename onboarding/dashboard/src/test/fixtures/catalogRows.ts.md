# dashboard/src/test/fixtures/catalogRows.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/catalogRows.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Catalog-row fixtures** (260715-FEUI-L2 S6) in the FULL wire shape (`TerminalCatalogRow` =
`TerminalCatalogEntry.to_json()`), placed under `src/test/fixtures/` — a NEW shared-fixture home —
to be shared with the L3 fixture pack. `catalogRow(overrides)` builds one row with sane defaults
(auto-ids via a module counter); `FLEET` is the mockup-mirroring scenario used across the
rail/model suites. **260715-FEUI-L6 (R9) appends its fixture pack after FLEET** — the two PTY
archetypes, the interaction kinds, and the stop residuals — as separate exports, so
FLEET-order-dependent tests stay byte-identical.

## Code Commentary

### Logic

- `catalogRow` (L10-L27): defaults = a running claude harness row with `seatRole: "chat"`; every
  field overridable; ids auto-increment.
- `FLEET` (L32-L172): the spec-mockup fleet — a flat command spine (architect turn-ended,
  orchestrator working), a manager with a leaf claim under the 260714 master, a 04_serving leaf
  cluster (worker working with requested model/effort provenance, reviewer + curator turn-ended),
  a second cluster (05_capabilities), two landed 01_protocol seats (the completed folder), an
  awaiting-input worker under the 260715 master with a REAL `controlPendingInteraction` (id, kind,
  prompt, choices — the R16 preview source), a failed scout (`controlState: "failed"`,
  `bridgeError` in `controlRaw`, liveness evidence), and a landed unattached pi probe.
- **The L6 pack** (L173-L282): `L6_CONTROLLED_WORKING` (archetype 1 — `controlState: "ready"`,
  working; the PTY shows the runner line-log) and `L6_LEGACY_RAW` (archetype 2 —
  `controlState: "unsupported"`, the vendor TUI in tmux; bell/OSC harvesting applies to THIS
  archetype only); the three interaction kinds — `L6_INTERACTION_CHOICES` (buttons path),
  `L6_INTERACTION_FREETEXT` (`choices: []` → composer answer-mode via the gate),
  `L6_INTERACTION_UNREPRESENTABLE` (no `interactionId` — the honest-refusal path); and the
  residual pair — `L6_RETIRED_WITH_STOP_ERROR` (a terminated+retired row carrying
  `controlRaw.retireControlStopError`, the sweep's target) and
  `L6_TERMINATE_RESPONSE_WITH_RESIDUAL` (the terminate ROUTE response shape with
  `controlStopDetail` — a response fixture, not a catalog row).

### Invariants And Boundaries

Fixtures must stay FULL-wire-shape (built on `types/terminalCatalog.ts`) so DOM-level tests can
plant provenance fields and assert they never leak into the rail (the R6 negative test). Shared
test infrastructure — extend by adding rows/overrides, not by forking a second builder.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The builder + the FLEET scenario. | L10-L172 | [catalogRows.ts](catalogRows.ts) |
| The wire type the fixtures instantiate. | L24-L90 | [../../types/terminalCatalog.ts](../../types/terminalCatalog.ts) |
| The heaviest consumers (rail-state matrix, model suites). | — | [../../panels/session-cockpit/SessionRail.test.tsx](../../panels/session-cockpit/SessionRail.test.tsx) |
| The L6 pack's consumers: lifecycle flows, interaction bar, archetype surface. | — | [../../data/sessionLifecycle.test.ts](../../data/sessionLifecycle.test.ts), [../../panels/session-cockpit/InteractionBar.test.tsx](../../panels/session-cockpit/InteractionBar.test.tsx), [../../panels/session-cockpit/PtySurface.test.tsx](../../panels/session-cockpit/PtySurface.test.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R9): appended the L6 fixture pack after FLEET — the
  controlled/legacy-raw archetype rows, the choices/freetext/unrepresentable interaction rows,
  the retired-with-stop-error row, and the terminate-response-with-residual shape. FLEET is
  byte-identical (zero removed/modified lines — reviewer-verified), keeping order-dependent
  tests stable. Verification metadata pinned to the leaf base until closeout stamps the L6 code
  commit.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S6 (R11): the shared full-wire catalog
  fixtures — `catalogRow` builder + the mockup-mirroring `FLEET` (spine, clusters, completed
  folder, awaiting-input prompt, failed scout, landed probe) — the fixture base the L3 pack
  extends. Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
