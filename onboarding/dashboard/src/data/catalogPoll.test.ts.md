# dashboard/src/data/catalogPoll.test.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The poll-health state the beat assertions read. [2]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Adds refcounted eager/cross-tab reconciler coverage, including immediate remote termination removal, stale-echo exclusion, authoritative empty hydration, idempotent release, and one shared BroadcastChannel.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
