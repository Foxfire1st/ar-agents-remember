# dashboard/src/test/fixtures/catalogRows.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/catalogRows.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Catalog-row fixtures** (260715-FEUI-L2 S6) in the FULL wire shape (`TerminalCatalogRow` =
`TerminalCatalogEntry.to_json()`), placed under `src/test/fixtures/` — a NEW shared-fixture home —
to be shared with the L3 fixture pack. `catalogRow(overrides)` builds one row with sane defaults
(auto-ids via a module counter); `FLEET` is the mockup-mirroring scenario used across the
rail/model suites.

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

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S6 (R11): the shared full-wire catalog
  fixtures — `catalogRow` builder + the mockup-mirroring `FLEET` (spine, clusters, completed
  folder, awaiting-input prompt, failed scout, landed probe) — the fixture base the L3 pack
  extends. Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
