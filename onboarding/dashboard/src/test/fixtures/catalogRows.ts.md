# dashboard/src/test/fixtures/catalogRows.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/catalogRows.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-26T15:40+0200                            |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f`       |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**Catalog-row fixtures** in the FULL wire shape (`TerminalCatalogRow` =
`TerminalCatalogEntry.to_json()`), placed under `src/test/fixtures/` — a NEW shared-fixture home —
to be shared with later fixture packs. `catalogRow(overrides)` builds one row with sane defaults
(auto-ids via a module counter); `FLEET` is the mockup-mirroring scenario used across the
rail/model suites. Later packs are **appended after FLEET as separate exports** — the `L6_*` PTY
archetypes + interaction kinds + stop residuals, the `L5I_*` structured-interaction rows, and the
`L7_*` multiplexed seat — so FLEET-order-dependent tests stay byte-identical.

## Code Commentary

### Logic

- `catalogRow` (L10-L27): defaults = a running claude harness row with `seatRole: "chat"`; every
  field overridable; ids auto-increment.
- `FLEET` (L32-L172): the spec-mockup fleet — a flat command spine (architect turn-ended,
  orchestrator working), a manager with a leaf claim under one master, a 04_serving leaf
  cluster (worker working with requested model/effort provenance, reviewer + curator turn-ended),
  a second cluster (05_capabilities), two landed 01_protocol seats (the completed folder), an
  awaiting-input worker under a second master with a REAL `controlPendingInteraction` (id, kind,
  prompt, choices — the R16 preview source), a failed scout (`controlState: "failed"`,
  `bridgeError` in `controlRaw`, liveness evidence), and a landed unattached pi probe.
- **The `L6_*` pack** (L178-L255; L384-L409): `L6_CONTROLLED_WORKING` (archetype 1 —
  `controlState: "ready"`, working; the PTY shows the runner line-log) and `L6_LEGACY_RAW`
  (archetype 2 — `controlState: "unsupported"`, the vendor TUI in tmux; bell/OSC harvesting
  applies to THIS archetype only); the three interaction kinds — `L6_INTERACTION_CHOICES`
  (buttons path), `L6_INTERACTION_FREETEXT` (`choices: []` → composer answer-mode via the gate),
  `L6_INTERACTION_UNREPRESENTABLE` (no `interactionId` — the honest-refusal path); and the
  residual pair — `L6_RETIRED_WITH_STOP_ERROR` (a terminated+retired row carrying
  `controlRaw.retireControlStopError`, the sweep's target) and
  `L6_TERMINATE_RESPONSE_WITH_RESIDUAL` (the terminate ROUTE response shape with
  `controlStopDetail` — a response fixture, not a catalog row).
- **The `L5I_*` pack** (L257-L380): `L5I_INTERACTION_QUESTIONS` (a structured AskUserQuestion
  interaction — two question pages, one multiSelect, each with ITS OWN option group),
  `L5I_INTERACTION_NO_LIFECYCLE` (one structured question on a seat WITHOUT a lifecycle —
  answerable via the direct session route), `L5I_INTERACTION_PERMISSION` (choices exactly
  allow/deny, direct-route `response`), and `L5I_INTERACTION_LEGACY_RUNNER` (a PRE-FIX runner row:
  no top-level `questions`, the claude-native structure at `raw.input.questions`).
- **The `L7_*` multiplexed fixture** (L411-L446): `L7_MULTIPLEXED_INTERACTIONS` — a multiplexed seat
  (review R6): the parent's SINGULAR `controlPendingInteraction` slot PLUS the
  additive plural `controlPendingInteractions` carrying the parent AND a sub-agent approval with
  its adapter-bound label (`raw: { threadId: "agent-thread-1", agentLabel: "agent agent-t" }`) —
  the InteractionBar renders and answers one bar per pending interaction. Consumed by the
  InteractionBar multiplex suite.

### Invariants And Boundaries

Fixtures must stay FULL-wire-shape (built on `types/terminalCatalog.ts`) so DOM-level tests can
plant provenance fields and assert they never leak into the rail (the R6 negative test). Shared
test infrastructure — extend by appending rows/overrides, never by reshaping FLEET or forking a
second builder.

### 2026-07-24 Curator Delta

The shared catalog fixtures now cover structured multi-question and permission interactions, direct
responses without a lifecycle, and a legacy runner's nested native question shape.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The builder + the FLEET scenario. | L10-L172 | [catalogRows.ts](catalogRows.ts) |
| The appended packs: `L6_*` archetypes/kinds/residuals, `L5I_*` structured rows, `L7_*` multiplexed seat. | L178-L409; L411-L446 | [catalogRows.ts](catalogRows.ts) |
| The wire type the fixtures instantiate. | L24-L93 | [../../types/terminalCatalog.ts](../../types/terminalCatalog.ts) |
| The heaviest consumers (rail-state matrix, model suites). | — | [../../panels/session-cockpit/SessionRail.test.tsx](../../panels/session-cockpit/SessionRail.test.tsx) |
| The appended packs' consumers: lifecycle flows, interaction bar (incl. the multiplex suite), archetype surface. | — | [../../data/sessionLifecycle.test.ts](../../data/sessionLifecycle.test.ts), [../../panels/session-cockpit/InteractionBar.test.tsx](../../panels/session-cockpit/InteractionBar.test.tsx), [../../panels/session-cockpit/PtySurface.test.tsx](../../panels/session-cockpit/PtySurface.test.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Update History

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: documented the appended
  `L7_MULTIPLEXED_INTERACTIONS` seat (parent singular slot + plural list carrying the parent AND a
  labeled sub-agent approval) and the previously undocumented L5I structured pack; corrected the
  stale "L6 pack L173-L282" citation (the L6 rows are L178-L255 with the residuals at L384-L409,
  the L5I rows interleaved at L257-L380). The L7 code is uncommitted in the code worktree;
  closeout re-stamps verification.

- 2026-07-24T13:17:50Z — Added interaction-routing fixture coverage. Verification hash/date remain
  pinned to the pre-commit source stamp.

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
