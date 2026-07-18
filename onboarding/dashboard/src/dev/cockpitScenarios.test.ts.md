# dashboard/src/dev/cockpitScenarios.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/cockpitScenarios.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00 |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate |  2026-07-18T07:47:42+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pins dev-scenario isolation across stores and unresolved asynchronous authority boundaries.

## Code Commentary

The suite proves a reset clears transient cockpit/catalog/capability/announcement/lifecycle/PTY and
connection state while preserving allowed preferences. Deferred tests reuse ids across generations
and prove old authority reads, withdrawals, pollers, and catalog hydrates neither overwrite the new
owner nor delete its in-flight registration or poll-health truth.

## Invariants And Boundaries

These are race tests, not fixture snapshots: assertions must release the retired promise after the
successor authority exists.

## Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Cross-Repo References

The race suite exercises repository-local generation guards and stores; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Unit under test. | [cockpitScenarios.ts](cockpitScenarios.ts) |

## Update History

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 same-id cross-generation regressions; verification
  metadata remains blank until commit.
