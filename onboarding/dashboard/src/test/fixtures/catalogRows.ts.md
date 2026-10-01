# dashboard/src/test/fixtures/catalogRows.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The shared row builder. [1]
- The mockup-mirroring terminal-row `FLEET` scenario, distinct from its task-document fixture. [2]
- The appended L6 PTY, interaction, and residual fixture pack. [3]
- The appended L5I structured-interaction fixture pack. [4]
- The appended L7 multiplexed-interaction fixture. [5]
- The wire type instantiated by these fixtures. [6]
- The rail-state fixture consumer. [7]
- The lifecycle-flow consumer of the appended fixtures. [8]
- The interaction-bar consumer, including the multiplex suite. [9]
- The PTY archetype-surface consumer. [10]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.
