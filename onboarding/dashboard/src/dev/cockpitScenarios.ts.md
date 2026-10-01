# dashboard/src/dev/cockpitScenarios.ts

## Governing Overview

[dashboard/src overview](../overview.md)

## 260731-EFA-L8 Change

The scenario catalog gained the `terminal-focus` scenario and its landed-cleanup
route for the repaired primary e2e suite; existing scenarios are unchanged.

## Purpose

Catalogues dedicated Chats-cockpit scenarios and drives the real data stores/clients against a
dev-only fake transport for interactive and Playwright verification.

## Code Commentary

### The Probe Types Are No Longer Exported From Here

260731-EFA-L2 moved `CockpitBenchProbe`, `CockpitBenchTransition`, `CockpitBenchRequest`,
`CockpitResetAudit` and the `declare global { interface Window { … } }` block for
`__cockpitBench` / `__cockpitBenchResetAudit` out to [`benchProbes.ts`](benchProbes.ts).
This file imports `CockpitBenchProbe` and `CockpitResetAudit` as types and **exports none of
them**; an importer that still pulls those names from `./cockpitScenarios` will not compile.

The reason is a project boundary: the Playwright drivers read `window.__cockpitBench` from
the driver tsconfig project, which does not include this file. `benchProbes.ts` is
import-free precisely so `tsconfig.driver.json` can name it without dragging the app's module
graph along.

**Nothing about the transport, the audit or the scenario catalogue changed** — the same
values are still installed on `window` at the same points (`window.__cockpitBench` at the end
of `installCockpitScenarioFetch`, `__cockpitBenchResetAudit` during reset, and the probe
deleted on teardown).

### FEUI MX-FIX-2 Request-Matched Open Simulation

The `/dev/bench` fetch injector now emits the same typed accepted HTTP body consumed in production,
with kind-specific authority. Raw requests produce terminal command/catalog identity and omit
harness/control facts. Harness requests preserve the requested harness, model/effort pair, control
identity, lifecycle, task-document, and seat facts. The accepted response and inserted scenario catalog row
are derived from the same request, so the bench exercises the real opener instead of bypassing it.

- Covers launch success/conflict/failure, set promotion, ambiguous submit reconciliation,
  interaction answer, mixed 12-seat fleet, exited/retired versus landed presentation, dropped PTY,
  and stale catalog states.
- `resetCockpitScenario` revokes catalog/capability/snapshot/submission/connection ownership before
  hydrating declared rows, clears announcements/notices/PTY harvest/per-seat state, and preserves only
  declared user preferences.
- `installCockpitScenarioFetch` serves the production routes and records a request/probe audit; the
  scenario may expose controlled transitions without replacing product stores.

### The Harness Catalog Fixture Was Serving An Impossible Shape

260731-EFA-L4. `GET /api/harnesses` answered three rows of
`{ id, name, detected, control: "ready" }`. The server's `DetectedHarness` is a `WireResponse` over
exactly `id`, `name`, `detected` — `extra="forbid"` — so `control` is a field the daemon can never
send, and nothing in the dashboard read it. The rows are now
`[{ id, name, detected }, …] satisfies HarnessInfo[]`, with `HarnessInfo` imported as a type from
`data/harnessCatalog.ts`.

**Why nothing caught it.** `HarnessInfo` lives in `data/harnessCatalog.ts`, which declares its
response type inline and carries **no mirror marker** (`// TypeScript mirror of` / `// Browser mirror
of`). `wireFixtureGuard.ts` discovers its wire vocabulary from that marker plus everything under
`src/types/`, so an unmarked module is invisible to it — and the guard's discovery is fail-closed in
one direction only: a mirror that *loses* its marker fails loudly, one that never carried a marker
never appears. With no mirror type in the vocabulary, `tsc` had nothing to compare a bare object
literal against either. The guard's own header names the blind spot and the five modules still inside
it: `data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`, `data/changeset.ts`,
`data/files.ts`, `data/notes.ts`. The `satisfies` here is the local substitute for the marker.

The same leaf removed three more `control` fields from the harness rows in
`panels/session-cockpit/LaunchFlow.test.tsx` — six across the leaf, three of them here.

### Logic

`installCockpitScenarioFetch` matches the terminal-open request, parses its body, and returns a real
accepted `Response` whose row mirrors raw or harness identity. The scenario catalog exposes the same
row so downstream reconciliation observes consistent fixture truth. Task identity is parsed from
the structured `taskDocumentRef`; the fixture does not revive a `leafKey` transport field. The `/api/harnesses` branch
returns the three-field catalog rows pinned by `satisfies HarnessInfo[]`.

### Conventions

Scenario transport replacement is explicit, request-matched, and generation-reset. Fixture rows use
the production wire shape rather than special client-only success values. Where the response type
lives in a module `wireFixtureGuard.ts` cannot see, the fixture carries a `satisfies` against the
declared client type so a re-added field fails `tsc -b` at the literal rather than passing silently.

### Invariants And Boundaries

Only transport is mocked. Old async completions must fail their generation check and may not mutate,
delete, satisfy, or announce into a newer scenario, including when session/request ids are reused.

**This injector may only answer what the daemon could answer.** Every fulfilled route body must be a
shape the server can produce; a field no server model declares is a defect here even when nothing
reads it, because a renderer branch written to match it ships permanently dead. Routes whose response
type lives in an unmarked module (`data/harnessCatalog.ts` and the four others named above) get no
help from `tsc` or `wireFixtureGuard.ts`, so they must carry an explicit `satisfies` and a matching
key-set assertion in `cockpitScenarios.test.ts`.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

Open since 260731-EFA-L4: five modules declare wire response types with no mirror marker
(`data/harnessCatalog.ts`, `data/submissionLifecycleClient.ts`, `data/changeset.ts`, `data/files.ts`,
`data/notes.ts`) and so stay outside `wireFixtureGuard.ts`'s discovered vocabulary. Both impossible
fixtures this leaf removed lived in that blind spot. Marking them is out of this leaf's scope.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

Scenario routes and fixture facts are repository-local. Vendor harness names are data values, not cross-repository code dependencies.

No applicable cross-repository source was found.

### Repo-Internal References

This table carries each claim's exact source ranges in the `Source` cell, with the anchor naming the
construct those lines contain.

- The announcer and `HarnessInfo` imports plus the `/api/harnesses` branch returning three-field rows pinned by `satisfies HarnessInfo[]`. [1]
- `HarnessInfo` declared inline (`id`, `name`, `detected`) in a module carrying no mirror marker, which is why nothing compared the old fixture against it. [2]
- The server's `DetectedHarness` / `DetectedHarnessesResponse` for `GET /api/harnesses`: exactly three fields on a `WireResponse`. [3]
- The guard's own note that its wire vocabulary is discovered from a house marker, that discovery is fail-closed in one direction only, and the five unmarked modules still in the blind spot. [4]
- The `describe` asserting the injector answers only what the daemon could: exact key sets for the catalog rows and for the withdrawal result. [5]
- Authority wrapper. [6]
- Scenario registration. [7]
- Cross-generation regressions. [8]
- The probe types and the `Window` augmentation this file installs into, shared with the Playwright driver tsconfig project. [9]
