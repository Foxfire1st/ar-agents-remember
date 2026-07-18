# dashboard/src/dev/cockpitScenarios.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/dev/cockpitScenarios.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee` |
| lastVerifiedCommitDate |  2026-07-18T15:41:39+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pins dev-scenario isolation across stores and unresolved asynchronous authority boundaries.

## Code Commentary

### FEUI MX-FIX-2 Real-Client Open Proof

The new scenario test calls the real shared opener through the dev injector for one raw and one
harness request. It asserts both accepted identities, retained harness model/effort facts, and the
catalog projection. The raw response and catalog row must have no harness/control authority,
preventing a fixture-only fail-open from masking production behavior.

The suite proves a reset clears transient cockpit/catalog/capability/announcement/lifecycle/PTY and
connection state while preserving allowed preferences. Deferred tests reuse ids across generations
and prove old authority reads, withdrawals, pollers, and catalog hydrates neither overwrite the new
owner nor delete its in-flight registration or poll-health truth.

### Logic

The suite installs one named scenario injector, issues real raw and Codex open requests through the
production client, and asserts the returned accepted row matches each request's kind, harness,
lifecycle, leaf, and control boundary.

### Conventions

Tests use real `Response` objects and reset scenario state between cases so parser behavior, not a
partial fetch double, determines acceptance.

### Invariants And Boundaries

These are race tests, not fixture snapshots: assertions must release the retired promise after the
successor authority exists.

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

The race suite exercises repository-local generation guards and stores; no cross-repository source applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Unit under test. | [cockpitScenarios.ts](cockpitScenarios.ts) |

## Update History

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: added real-client scenario coverage for accepted raw
  and harness opens and verified raw catalog rows remain free of fabricated harness authority.
  Verification metadata remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Created for FEUI-L8 same-id cross-generation regressions; verification
  metadata remains blank until commit.
