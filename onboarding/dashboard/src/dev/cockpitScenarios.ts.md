# dashboard/src/dev/cockpitScenarios.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/cockpitScenarios.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Catalogues dedicated Chats-cockpit scenarios and drives the real data stores/clients against a
dev-only fake transport for interactive and Playwright verification.

## Code Commentary

- Covers launch success/conflict/failure, set promotion, ambiguous submit reconciliation,
  interaction answer, mixed 12-seat fleet, exited/retired versus landed presentation, dropped PTY,
  and stale catalog states.
- `resetCockpitScenario` revokes catalog/capability/snapshot/submission/connection ownership before
  hydrating declared rows, clears announcements/notices/PTY harvest/per-seat state, and preserves only
  declared user preferences.
- `installCockpitScenarioFetch` serves the production routes and records a request/probe audit; the
  scenario may expose controlled transitions without replacing product stores.

## Invariants And Boundaries

Only transport is mocked. Old async completions must fail their generation check and may not mutate,
delete, satisfy, or announce into a newer scenario, including when session/request ids are reused.

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

## Update History

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 cockpit scenario authority and interaction coverage;
  verification metadata remains blank until commit.
