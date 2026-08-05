# dashboard/src/data/catalogPoll.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/catalogPoll.test.ts`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the shared catalog poll driver (260715-FEUI-L2 S1/R1) — the behavior Chats used to
own inline, now pinned at the shared module so the hoist can never silently regress either
consumer.

## Code Commentary

### Logic

- **`hydrateTerminalSessionsFromCatalog`** — hydrates the session store from a mocked catalog and
  records a HEALTHY beat; a failed (`null`) fetch counts missed beats and flips
  `pollHealth.healthy=false` at the `POLL_STALE_MISSED_BEATS` cutoff (R15/F3); the empty-list
  guard holds (an empty catalog applies only with `allowEmpty=true`); the exclusion set keeps
  just-terminated ids out of a stale snapshot (no resurrection).
- **`startCatalogPollDriver` (refcounted)** — fake timers prove ONE 2500 ms interval exists for
  any number of subscribers, ticks call the hydrate, and the interval fully stops after the LAST
  release (double-release inert; StrictMode-symmetric start/release/start safe).

### Conventions

`vi.mock` on `./terminal` (the fetch seam) + `vi.useFakeTimers()`; both stores reset between
cases. Test-only.

### Invariants And Boundaries

The refcount cases are the regression net for the R1 hoist: they must keep failing if a second
interval ever appears or a release leaks the timer.

### 2026-07-24 Curator Delta

Regression cases now prove that one aborted catalog beat records one missed beat and the next beat
recovers, while a byte-identical catalog payload preserves state and row identity without notifying
subscribers.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `hydrateTerminalSessionsFromCatalog` | dashboard/src/data/catalogPoll.ts:139-157 |
| The poll-health state the beat assertions read. | `recordPollBeat` | dashboard/src/data/sessionCockpitStore.ts:228-228 |

## FEUI-L8 Reviewed Candidate Delta

Adds refcounted eager/cross-tab reconciler coverage, including immediate remote termination removal, stale-echo exclusion, authoritative empty hydration, idempotent release, and one shared BroadcastChannel.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: rebased the
  `hydrateTerminalSessionsFromCatalog` range; exact non-fixing check returns zero findings.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 2 citation findings; scoped check passed.

- 2026-07-24T13:17:50Z — Documented poll timeout recovery and no-op reconciliation coverage.
  Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S1 (R1/R11): hydrate + beat recording,
  stale-cutoff flip, empty-list guard, exclusion set, and the refcounted single-interval /
  full-stop driver contract under fake timers. Verification metadata pinned to the leaf base
  until closeout stamps the L2 code commit.
