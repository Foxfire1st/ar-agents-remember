# dashboard/src/test/fixtures/catalogRows.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/catalogRows.ts`     |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-26T15:40+0200                            |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038`       |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## 260731-EFA-L8 Change

The fixture pack gained `RAW_TERMINAL_ROW` for the repaired primary e2e suite
(terminal-continuity and keep-alive scenarios); existing fixtures are unchanged.

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

Canonical command-seat fixtures now include `spawnRepo` and `spawnSprint`. Tests that intentionally
exercise old unbound rows construct that state explicitly, preventing migration compatibility
from silently becoming the default production fixture.

- cit:([`catalogRow`], dashboard/src/test/fixtures/catalogRows.ts:10-27): defaults = a running claude harness row with `seatRole: "chat"`; every
  field overridable; ids auto-increment.
- cit:([`FLEET`], dashboard/src/test/fixtures/catalogRows.ts:32-172): the spec-mockup fleet — a flat command spine (architect turn-ended,
  orchestrator working), a manager with a leaf claim under one master, a 04_serving leaf
  cluster (worker working with requested model/effort provenance, reviewer + curator turn-ended),
  a second cluster (05_capabilities), two landed 01_protocol seats (the completed folder), an
  awaiting-input worker under a second master with a REAL `controlPendingInteraction` (id, kind,
  prompt, choices — the R16 preview source), a failed scout (`controlState: "failed"`,
  `bridgeError` in `controlRaw`, liveness evidence), and a landed unattached pi probe.
- **The `L6_*` pack** (the archetype/interaction rows plus the residual pair): `L6_CONTROLLED_WORKING` (archetype 1 —
  `controlState: "ready"`, working; the PTY shows the runner line-log) and `L6_LEGACY_RAW`
  (archetype 2 — `controlState: "unsupported"`, the vendor TUI in tmux; bell/OSC harvesting
  applies to THIS archetype only); the three interaction kinds — `L6_INTERACTION_CHOICES`
  (buttons path), `L6_INTERACTION_FREETEXT` (`choices: []` → composer answer-mode via the gate),
  `L6_INTERACTION_UNREPRESENTABLE` (no `interactionId` — the honest-refusal path); and the
  residual pair — `L6_RETIRED_WITH_STOP_ERROR` (a terminated+retired row carrying
  `controlRaw.retireControlStopError`, the sweep's target) and
  `L6_TERMINATE_RESPONSE_WITH_RESIDUAL` (the terminate ROUTE response shape with
  `controlStopDetail` — a response fixture, not a catalog row).
- **The `L5I_*` pack** (the structured interaction rows): `L5I_INTERACTION_QUESTIONS` (a structured AskUserQuestion
  interaction — two question pages, one multiSelect, each with ITS OWN option group),
  `L5I_INTERACTION_NO_LIFECYCLE` (one structured question on a seat WITHOUT a lifecycle —
  answerable via the direct session route), `L5I_INTERACTION_PERMISSION` (choices exactly
  allow/deny, direct-route `response`), and `L5I_INTERACTION_LEGACY_RUNNER` (a PRE-FIX runner row:
  no top-level `questions`, the claude-native structure at `raw.input.questions`).
- **The `L7_*` multiplexed fixture** (the multiplexed fixture): `L7_MULTIPLEXED_INTERACTIONS` — a multiplexed seat
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared row builder. | "export function catalogRow" | dashboard/src/test/fixtures/catalogRows.ts:12-12 |
| The mockup-mirroring terminal-row `FLEET` scenario, distinct from its task-document fixture. | "export const FLEET: TerminalCatalogRow[]" | dashboard/src/test/fixtures/catalogRows.ts:85-85 |
| The appended L6 PTY, interaction, and residual fixture pack. | `L6_CONTROLLED_WORKING` | dashboard/src/test/fixtures/catalogRows.ts:245-257 |
| The appended L5I structured-interaction fixture pack. | `L5I_INTERACTION_QUESTIONS` | dashboard/src/test/fixtures/catalogRows.ts:326-363 |
| The appended L7 multiplexed-interaction fixture. | `L7_MULTIPLEXED_INTERACTIONS` | dashboard/src/test/fixtures/catalogRows.ts:480-512 |
| The wire type instantiated by these fixtures. | "interface TerminalCatalogRow" | dashboard/src/types/terminalCatalog.ts:29-29 |
| The rail-state fixture consumer. | "hydrate(FLEET" | dashboard/src/panels/session-cockpit/SessionRail.test.tsx:68-68 |
| The lifecycle-flow consumer of the appended fixtures. | "const retired = fromTerminalSessionInfo(L6_RETIRED_WITH_STOP_ERROR)" | dashboard/src/data/sessionLifecycle.test.ts:89-89 |
| The interaction-bar consumer, including the multiplex suite. | "const multiplexedSession" | dashboard/src/panels/session-cockpit/InteractionBar.test.tsx:481-481 |
| The PTY archetype-surface consumer. | "const controlled = () => fromTerminalSessionInfo(L6_CONTROLLED_WORKING)" | dashboard/src/panels/session-cockpit/PtySurface.test.tsx:39-39 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## Update History

- 2026-08-14T05:26Z — L23 final curator: documented the separate sprint/master task-document
  fixture used to preserve dashboard grouping and disambiguated the terminal-row `FLEET` anchor.
  Verification remains closeout-owned.
- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `catalogRows.ts` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: bound the normal catalog fixtures to a repository+sprint
  and reserved unbound fixtures for explicit migration cases. Verification metadata remains pinned
  until closeout stamps the code commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the RAW_TERMINAL_ROW fixture addition. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T20:42:26+02:00 — W2-B07 curator: repaired 10 repository-reference citations and normalized 2 prose citations (10/10 anchored and sourced; scoped citation check clean).

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: documented the appended
  `L7_MULTIPLEXED_INTERACTIONS` seat (parent singular slot + plural list carrying the parent AND a
  labeled sub-agent approval) and the previously undocumented L5I structured pack; corrected the
  stale L6 pack citation (the L6 rows include the two archetypes, interaction kinds, and residuals,
  with the L5I rows interleaved). The L7 code is uncommitted in the code worktree;
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
