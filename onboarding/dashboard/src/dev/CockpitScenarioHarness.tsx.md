# dashboard/src/dev/CockpitScenarioHarness.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/CockpitScenarioHarness.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Provides the dev-only authority boundary around one real Chats cockpit scenario. It installs fake
HTTP authority before descendant polling, waits for the keyed prior shell's passive cleanup, resets
all transient state, and only then mounts the successor shell and mock PTY transport.

## Code Commentary

`CockpitScenarioHarness` installs transport in a layout effect and performs reset/readiness in a
passive effect so old descendants cannot race the new fixture. `CockpitScenarioExitBoundary` applies
the same post-unmount reset when returning to ordinary Engine Room scenarios without retaining fake
HTTP authority. Socket behavior can be live or deliberately dropped and omits irrelevant xterm banner
output in cockpit scenarios.

## Invariants And Boundaries

DEV-only; it wraps the real `CockpitShell` rather than a private UI. Readiness must remain false until
the old authority is revoked and all transient/module registries have been cleared.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Cross-Repo References

The harness composes repository-local stores, scenario fixtures, and the real CockpitShell; no external fixture framework is an implementation authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Scenario facts, reset, and fake fetch installer. | `resetCockpitScenario`; `installCockpitScenarioFetch` | dashboard/src/dev/cockpitScenarios.ts:276-315; dashboard/src/dev/cockpitScenarios.ts:381-627 |
| Bench mounts `CockpitScenarioHarness` and wraps the shell in `CockpitScenarioExitBoundary`. | "<CockpitScenarioHarness key={scenario.name} scenario={scenario.cockpit}>"; "<CockpitScenarioExitBoundary key={scenario.name}>{shell}</CockpitScenarioExitBoundary>" | dashboard/src/dev/Bench.tsx:75-75; dashboard/src/dev/Bench.tsx:79-79 |

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: anchored scenario reset/fetch setup and Bench
  composition to their exact implementation owners; narrowed the JSX-only boundary claim.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 end-to-end cockpit scenarios; verification metadata
  remains blank until the new source is committed.
