# dashboard/src/dev/cockpitScenarios.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/cockpitScenarios.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-31T16:10+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

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
identity, lifecycle, leaf, and seat facts. The accepted response and inserted scenario catalog row
are derived from the same request, so the bench exercises the real opener instead of bypassing it.

- Covers launch success/conflict/failure, set promotion, ambiguous submit reconciliation,
  interaction answer, mixed 12-seat fleet, exited/retired versus landed presentation, dropped PTY,
  and stale catalog states.
- `resetCockpitScenario` revokes catalog/capability/snapshot/submission/connection ownership before
  hydrating declared rows, clears announcements/notices/PTY harvest/per-seat state, and preserves only
  declared user preferences.
- `installCockpitScenarioFetch` serves the production routes and records a request/probe audit; the
  scenario may expose controlled transitions without replacing product stores.

### Logic

`installCockpitScenarioFetch` matches the terminal-open request, parses its body, and returns a real
accepted `Response` whose row mirrors raw or harness identity. The scenario catalog exposes the same
row so downstream reconciliation observes consistent fixture truth.

### Conventions

Scenario transport replacement is explicit, request-matched, and generation-reset. Fixture rows use
the production wire shape rather than special client-only success values.

### Invariants And Boundaries

Only transport is mocked. Old async completions must fail their generation check and may not mutate,
delete, satisfy, or announce into a newer scenario, including when session/request ids are reused.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

Scenario routes and fixture facts are repository-local. Vendor harness names are data values, not cross-repository code dependencies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Authority wrapper. | [CockpitScenarioHarness.tsx](CockpitScenarioHarness.tsx) |
| Scenario registration. | [scenarios.ts](scenarios.ts) |
| Cross-generation regressions. | [cockpitScenarios.test.ts](cockpitScenarios.test.ts) |
| The probe types and the `Window` augmentation this file installs into, shared with the Playwright driver tsconfig project. | [benchProbes.ts](benchProbes.ts) |

## Update History

- 2026-07-31T16:10+02:00 — 260731-EFA-L2: `CockpitBenchProbe`, `CockpitBenchTransition`,
  `CockpitBenchRequest`, `CockpitResetAudit` and the `Window` augmentation moved out to
  `benchProbes.ts` so the Playwright driver tsconfig project reads one declaration; this file
  now imports two of them as types and exports none. No transport, audit or scenario
  behaviour changed. Verification metadata is pinned to the leaf's reformat commit until
  closeout stamps the code commit.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: made the dev transport model authoritative raw and
  harness open responses separately; raw rows no longer fabricate harness/control facts, while
  harness rows preserve accepted identity and requested pair. Verification metadata remains pinned
  until closeout.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 cockpit scenario authority and interaction coverage;
  verification metadata remains blank until commit.
